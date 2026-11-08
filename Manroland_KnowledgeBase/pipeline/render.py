#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render.py -- render every page of the manroland R700 IEC wiring-diagram PDFs to PNG.

WHY THIS CONFIGURATION (measured, see logs/render_decisions.md)
--------------------------------------------------------------
The source PDFs are A3 landscape (1190.55 x 841.89 pt), pure vector + real text,
no rotation, and their drawing geometry is almost entirely **0.85 pt** hairlines
(21171 of 21480 drawing items).  Body text is 6.9-7.5 pt and 8.8 pt, with a small
tail of 3-4 pt annotation text.

At 300 DPI a 0.85 pt line is 3.54 px wide.  Even in the worst possible sub-pixel
phase (line centred exactly between two pixel rows) the anti-aliased coverage
splits 1.77 / 1.77, so *both* rows are above a 0.5 threshold -- a hairline
therefore cannot be lost at 300 DPI.  Measured on the four densest sheets:
  * 100% of solid-ink pixels (gray < 128) survive binarisation  (recall_dark = 1.0)
  * 0 black pixels appear on pure white  (no dither speckle, false_pos_white = 0.0)
  * 0 connected components of <= 2 px  (no dotting / fragmentation)
  * 0 gaps across 39k-68k along-line samples taken from the page's own vector
    segments (125-177 thin solid segments per page)
1-bit PNG at 300 DPI is ~4.3x smaller than 8-bit grayscale at the same DPI
(111 KB vs 393 KB on the densest sheet), ~5.4x smaller than RGB @200, and
~2.5x smaller than 1-bit @400 while already being far beyond print resolution.

Output layout
-------------
    images/<DOCKEY>/<DOCKEY-without-plus>_<SHEET:04d>.png
    e.g. images/+Ax/Ax_0021.png

Usage
-----
    python render.py                       # render everything (resumable)
    python render.py --only +Ax            # one document
    python render.py --pages 1-50,60       # sheet filter
    python render.py --force               # ignore existing files
    python render.py --jobs 4              # parallel workers
    python render.py --dpi 400             # override resolution
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import struct
import sys
import time
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

try:
    import pymupdf
except ImportError:  # pragma: no cover
    sys.exit("PyMuPDF is required: import pymupdf failed")

from PIL import Image

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

DEFAULT_DPI = 300
DEFAULT_THRESHOLD = 160        # of 0..255; v <= threshold -> black
DEFAULT_MODE = "bilevel"       # bilevel | gray | rgb

#: logical document key -> source PDF filename (exact, including the "Cicuit" typo)
DOCUMENTS: list[tuple[str, str]] = [
    ("+FB", "Cicuit Diagram +FB.pdf"),
    ("+Ax", "Circuit Diagram +Ax.pdf"),
    ("+BA_Cx_DA", "Circuit Diagram +BA, Cx, DA.pdf"),
    ("+EA", "Circuit Diagram +EA.pdf"),
    ("+FA", "Circuit Diagram +FA.pdf"),
    ("+Jx", "Circuit Diagram +Jx.pdf"),
]

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
IMAGES_DIR = ROOT / "images"
MANIFEST_PATH = ROOT / "data" / "derived" / "image_manifest.json"
LOG_PATH = ROOT / "logs" / "render.log"
FAILURE_PATH = ROOT / "logs" / "render_failures.json"

DEFAULT_SRC = Path(r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland")

MIN_VALID_PNG_BYTES = 512      # anything smaller is a truncated / failed write
PNG_SIG = b"\x89PNG\r\n\x1a\n"

_DOCKEY_SAFE = re.compile(r"^[A-Za-z0-9_+.\-]+$")


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

class Logger:
    """Append-only run log, flushed on every write, mirrored to stdout."""

    def __init__(self, path: Path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = open(path, "a", encoding="utf-8", newline="\n")

    def __call__(self, msg: str) -> None:
        line = f"[{_dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
        self._fh.write(line + "\n")
        self._fh.flush()
        try:
            print(line, flush=True)
        except UnicodeEncodeError:      # exotic console code page
            print(line.encode("ascii", "replace").decode("ascii"), flush=True)

    def close(self) -> None:
        try:
            self._fh.close()
        except Exception:
            pass


def dockey_for(filename: str) -> str:
    """Derive the sanitised ASCII dockey for a source PDF filename.

    'Circuit Diagram +BA, Cx, DA.pdf' -> '+BA_Cx_DA'
    'Cicuit Diagram +FB.pdf'          -> '+FB'
    """
    stem = Path(filename).stem
    stem = re.sub(r"^(?:Circuit|Cicuit)\s+Diagram\s+", "", stem, flags=re.I)
    stem = stem.strip()
    if stem.startswith("+"):
        plus, rest = "+", stem[1:]
    else:
        plus, rest = "", stem
    rest = re.sub(r"[^A-Za-z0-9]+", "_", rest).strip("_")
    key = plus + rest
    return key or "DOC"


def file_part(dockey: str) -> str:
    """'+Ax' -> 'Ax'  (filename prefix, without the '+')."""
    return dockey.lstrip("+").strip() or "DOC"


def png_dims(path: Path):
    """Read width/height from a PNG IHDR chunk header without decoding pixels.

    Returns (w, h) or None when the file is missing / not a readable PNG.
    """
    try:
        if path.stat().st_size < 33:
            return None
        with open(path, "rb") as fh:
            if fh.read(8) != PNG_SIG:
                return None
            length = fh.read(4)
            if len(length) != 4:
                return None
            if fh.read(4) != b"IHDR":
                return None
            w, h = struct.unpack(">II", fh.read(8))
            return int(w), int(h)
    except OSError:
        return None


def parse_pages(spec: str | None, total: int) -> list[int]:
    """'1-50,60,70' -> [1..50, 60, 70] clamped to 1..total. None -> all."""
    if not spec:
        return list(range(1, total + 1))
    wanted: set[int] = set()
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.fullmatch(r"(\d+)\s*-\s*(\d+)", chunk)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if a > b:
                a, b = b, a
            wanted.update(range(a, b + 1))
        elif re.fullmatch(r"\d+", chunk):
            wanted.add(int(chunk))
        else:
            raise ValueError(f"bad --pages component: {chunk!r}")
    return sorted(n for n in wanted if 1 <= n <= total)


def build_lut(threshold: int) -> list[int]:
    """256-entry lookup: v <= threshold -> 0 (black), else 255 (white)."""
    t = max(0, min(255, int(threshold)))
    return [0] * (t + 1) + [255] * (255 - t)


# --------------------------------------------------------------------------
# Rendering core
# --------------------------------------------------------------------------

def render_page_image(doc, sheet: int, dpi: float, mode: str, threshold: int) -> Image.Image:
    """Render one 1-based sheet to a PIL image in the requested mode."""
    page = doc[sheet - 1]
    zoom = dpi / 72.0
    matrix = pymupdf.Matrix(zoom, zoom)

    if mode == "rgb":
        pix = page.get_pixmap(matrix=matrix, colorspace=pymupdf.csRGB, alpha=False)
        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    pix = page.get_pixmap(matrix=matrix, colorspace=pymupdf.csGRAY, alpha=False)
    gray = Image.frombytes("L", (pix.width, pix.height), pix.samples)
    if mode == "gray":
        return gray
    # bilevel: hard threshold, no dithering (these are line drawings, not photos)
    return gray.point(build_lut(threshold)).convert("1", dither=Image.NONE)


def out_path(dockey: str, sheet: int) -> Path:
    return IMAGES_DIR / dockey / f"{file_part(dockey)}_{sheet:04d}.png"


def save_png_atomic(img: Image.Image, path: Path) -> int:
    """Write via a .tmp sibling then os.replace, so an interrupted run can never
    leave a half-written PNG that the resume logic would happily skip."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(str(path) + ".tmp")
    try:
        img.save(tmp, "PNG", optimize=True)
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
    return path.stat().st_size


def expected_dims(doc, sheet: int, dpi: float) -> tuple[int, int]:
    r = doc[sheet - 1].rect
    zoom = dpi / 72.0
    return int(round(r.width * zoom)), int(round(r.height * zoom))


def render_one(doc, dockey: str, sheet: int, dpi: float, mode: str,
               threshold: int, force: bool) -> dict:
    """Render (or skip) a single sheet. Never raises; returns a result dict."""
    path = out_path(dockey, sheet)
    res = {"doc": dockey, "sheet": sheet, "path": str(path)}

    if not force and path.exists():
        size = path.stat().st_size
        dims = png_dims(path)
        if size >= MIN_VALID_PNG_BYTES and dims is not None:
            ew, eh = expected_dims(doc, sheet, dpi)
            if abs(dims[0] - ew) <= 1 and abs(dims[1] - eh) <= 1:
                res.update(status="skipped", bytes=size, w=dims[0], h=dims[1])
                return res
            res["note"] = f"existing {dims[0]}x{dims[1]} != expected {ew}x{eh}; re-rendering"

    try:
        img = render_page_image(doc, sheet, dpi, mode, threshold)
        nbytes = save_png_atomic(img, path)
        res.update(status="done", bytes=nbytes, w=img.width, h=img.height)
    except Exception as exc:                      # noqa: BLE001 - never kill the run
        res.update(status="failed", error=f"{type(exc).__name__}: {exc}",
                   traceback=traceback.format_exc()[-2000:])
    return res


# --------------------------------------------------------------------------
# Worker (module level so ProcessPoolExecutor can pickle it)
# --------------------------------------------------------------------------

def _worker_chunk(args) -> tuple[list[dict], list[str]]:
    """Render a contiguous chunk of sheets for one document inside a worker process."""
    dockey, pdf_path, sheets, dpi, mode, threshold, force = args
    import pymupdf as _pymupdf          # re-import in the child process
    results: list[dict] = []
    logs: list[str] = []
    try:
        doc = _pymupdf.open(pdf_path)
    except Exception as exc:                      # noqa: BLE001
        for s in sheets:
            results.append({"doc": dockey, "sheet": s, "status": "failed",
                            "error": f"open failed: {type(exc).__name__}: {exc}"})
        return results, [f"FAILED to open {pdf_path}: {exc}"]
    try:
        for sheet in sheets:
            r = render_one(doc, dockey, sheet, dpi, mode, threshold, force)
            results.append(r)
            if r.get("note"):
                logs.append(f"{dockey} sheet {sheet}: {r['note']}")
    finally:
        doc.close()
    return results, logs


# --------------------------------------------------------------------------
# Manifest
# --------------------------------------------------------------------------

def build_manifest(documents: list[tuple[str, str]], src: Path, dpi: float,
                   mode: str, threshold: int) -> dict:
    """Describe the images that actually exist on disk (not just this run's work),
    so a filtered or resumed run still produces a truthful manifest."""
    docs_meta: dict[str, dict] = {}
    pages: list[dict] = []
    px_per_pt = round(dpi / 72.0, 4)

    for dockey, filename in documents:
        pdf_path = src / filename
        entry = {"pdf": filename, "pages": None, "dockey": dockey,
                 "rendered_pages": 0}
        total = 0
        try:
            doc = pymupdf.open(pdf_path)
            total = len(doc)
            doc.close()
        except Exception:                          # noqa: BLE001
            pass
        entry["pages"] = total

        d = IMAGES_DIR / dockey
        if d.is_dir():
            for p in sorted(d.glob("*.png")):
                m = re.fullmatch(rf"{re.escape(file_part(dockey))}_(\d{{4}})\.png", p.name)
                if not m:
                    continue
                dims = png_dims(p)
                if dims is None:
                    continue
                sheet = int(m.group(1))
                pages.append({
                    "doc": dockey,
                    "sheet": sheet,
                    "file": f"{dockey}/{p.name}",
                    "w": dims[0],
                    "h": dims[1],
                    "px_per_pt": px_per_pt,
                    "bytes": p.stat().st_size,
                })
                entry["rendered_pages"] += 1
        docs_meta[dockey] = entry

    order = {d: i for i, (d, _) in enumerate(documents)}
    pages.sort(key=lambda r: (order.get(r["doc"], 99), r["sheet"]))
    return {
        "generated": _dt.datetime.now().isoformat(timespec="seconds"),
        "dpi": dpi,
        "mode": mode,
        "threshold": threshold if mode == "bilevel" else None,
        "documents": docs_meta,
        "page_count": len(pages),
        "total_bytes": sum(p["bytes"] for p in pages),
        "pages": pages,
    }


def write_manifest(manifest: dict) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(str(MANIFEST_PATH) + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, ensure_ascii=False)
    os.replace(tmp, MANIFEST_PATH)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Render manroland R700 wiring-diagram PDFs to PNG (resumable).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--src", default=str(DEFAULT_SRC), help="directory holding the source PDFs")
    p.add_argument("--only", action="append", default=None,
                   help="document key(s) to render, e.g. --only +Ax --only +EA "
                        "(comma-separated also accepted)")
    p.add_argument("--pages", default=None, help="sheet filter, e.g. 1-50,60,70-72")
    p.add_argument("--dpi", type=float, default=DEFAULT_DPI, help="rasterisation DPI")
    p.add_argument("--mode", choices=("bilevel", "gray", "rgb"), default=DEFAULT_MODE,
                   help="output colour mode")
    p.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD,
                   help="bilevel cutoff 0-255; v <= threshold becomes black")
    p.add_argument("--force", action="store_true", help="re-render even if a valid PNG exists")
    p.add_argument("--jobs", type=int, default=1, help="worker processes (1 = sequential)")
    p.add_argument("--no-manifest", action="store_true", help="skip manifest rebuild")
    p.add_argument("--quiet", action="store_true", help="only log summary lines")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    log = Logger(LOG_PATH)
    started = time.time()

    src = Path(args.src)
    log("=" * 78)
    log(f"render.py start  dpi={args.dpi:g} mode={args.mode} threshold={args.threshold} "
        f"jobs={args.jobs} force={args.force}")
    log(f"  src     : {src}")
    log(f"  images  : {IMAGES_DIR}")
    log(f"  manifest: {MANIFEST_PATH}")

    # ---- select documents -------------------------------------------------
    requested: list[str] = []
    if args.only:
        for item in args.only:
            requested.extend(x.strip() for x in item.split(",") if x.strip())
    by_key = {k: f for k, f in DOCUMENTS}
    unknown = [k for k in requested if k not in by_key]
    if unknown:
        log(f"WARNING unknown --only key(s) ignored: {unknown}")
    selected = [(k, f) for k, f in DOCUMENTS if not requested or k in requested]
    if not selected:
        log("ERROR no documents selected")
        log.close()
        return 2

    # ---- verify sources exist --------------------------------------------
    available = []
    for dockey, filename in selected:
        if (src / filename).exists():
            available.append((dockey, filename))
        else:
            log(f"WARNING missing source PDF, skipping document {dockey}: {src / filename}")
    if not available:
        log("ERROR no source PDFs found -- nothing to render")
        log.close()
        return 2

    # ---- build the work list ---------------------------------------------
    tasks: list[tuple] = []
    plan: dict[str, int] = {}
    for dockey, filename in available:
        try:
            doc = pymupdf.open(src / filename)
            total = len(doc)
            doc.close()
        except Exception as exc:                   # noqa: BLE001
            log(f"ERROR cannot open {filename}: {type(exc).__name__}: {exc}")
            continue
        sheets = parse_pages(args.pages, total)
        plan[dockey] = len(sheets)
        if not sheets:
            continue
        chunk = 20
        for i in range(0, len(sheets), chunk):
            tasks.append((dockey, str(src / filename), sheets[i:i + chunk],
                          args.dpi, args.mode, args.threshold, args.force))

    total_planned = sum(plan.values())
    log(f"planned: {total_planned} pages across {len(plan)} document(s) "
        f"({', '.join(f'{k}={v}' for k, v in plan.items())}) "
        f"in {len(tasks)} chunk(s)")

    if total_planned == 0:
        log("nothing to do")
        log.close()
        return 0

    # ---- execute ----------------------------------------------------------
    results: list[dict] = []
    failures: list[dict] = []
    done = skipped = failed = 0
    total_bytes = 0
    processed = 0
    last_report = time.time()

    def absorb(batch: list[dict], extra_logs: list[str]) -> None:
        nonlocal done, skipped, failed, total_bytes, processed, last_report
        for line in extra_logs:
            log(line)
        for r in batch:
            st = r.get("status")
            if st == "done":
                done += 1
                total_bytes += r.get("bytes", 0)
            elif st == "skipped":
                skipped += 1
                total_bytes += r.get("bytes", 0)
            else:
                failed += 1
                failures.append({"doc": r["doc"], "sheet": r["sheet"],
                                 "error": r.get("error", "unknown")})
                log(f"FAILED {r['doc']} sheet {r['sheet']}: {r.get('error')}")
        processed += len(batch)
        now = time.time()
        if not args.quiet and now - last_report > 10:
            elapsed = now - started
            rate = processed / elapsed if elapsed else 0
            eta = (total_planned - processed) / rate if rate else 0
            log(f"progress {processed}/{total_planned} "
                f"({processed / total_planned * 100:5.1f}%) "
                f"done={done} skipped={skipped} failed={failed} "
                f"{rate:.1f} pg/s eta={eta / 60:.1f} min")
            last_report = now

    if args.jobs > 1:
        workers = min(max(args.jobs, 1), 8, os.cpu_count() or 1, len(tasks))
        log(f"parallel mode: {workers} worker process(es)")
        with ProcessPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(_worker_chunk, t): t for t in tasks}
            for fut in as_completed(futures):
                try:
                    batch, extra = fut.result()
                except Exception as exc:           # noqa: BLE001
                    t = futures[fut]
                    log(f"FATAL worker chunk {t[0]}: {type(exc).__name__}: {exc}")
                    for s in t[2]:
                        failed += 1
                        failures.append({"doc": t[0], "sheet": s,
                                         "error": f"worker crashed: {exc}"})
                    continue
                absorb(batch, extra)
    else:
        doc_cache: dict[str, object] = {}
        try:
            for t in tasks:
                dockey, pdf_path, sheets = t[0], t[1], t[2]
                if pdf_path not in doc_cache:
                    doc_cache[pdf_path] = pymupdf.open(pdf_path)
                doc = doc_cache[pdf_path]
                batch = []
                extra = []
                for sheet in sheets:
                    r = render_one(doc, dockey, sheet, args.dpi, args.mode,
                                   args.threshold, args.force)
                    batch.append(r)
                    if r.get("note"):
                        extra.append(f"{dockey} sheet {sheet}: {r['note']}")
                absorb(batch, extra)
        finally:
            for d in doc_cache.values():
                try:
                    d.close()
                except Exception:
                    pass

    # ---- failures file ----------------------------------------------------
    if failures:
        try:
            FAILURE_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(FAILURE_PATH, "w", encoding="utf-8") as fh:
                json.dump({"generated": _dt.datetime.now().isoformat(timespec="seconds"),
                           "count": len(failures), "failures": failures},
                          fh, indent=1, ensure_ascii=False)
        except OSError as exc:
            log(f"WARNING could not write failure report: {exc}")

    # ---- manifest ---------------------------------------------------------
    if not args.no_manifest:
        try:
            man = build_manifest(DOCUMENTS, src, args.dpi, args.mode, args.threshold)
            write_manifest(man)
            log(f"manifest: {MANIFEST_PATH}  ({man['page_count']} pages, "
                f"{man['total_bytes'] / 1e6:.1f} MB on disk)")
        except Exception as exc:                   # noqa: BLE001
            log(f"ERROR manifest rebuild failed: {type(exc).__name__}: {exc}")

    # ---- summary ----------------------------------------------------------
    elapsed = time.time() - started
    log("-" * 78)
    log(f"SUMMARY  dpi={args.dpi:g} mode={args.mode}"
        + (f" threshold={args.threshold}" if args.mode == "bilevel" else ""))
    log(f"  pages done   : {done}")
    log(f"  pages skipped: {skipped}")
    log(f"  pages failed : {failed}")
    log(f"  total bytes  : {total_bytes}  ({total_bytes / 1e6:.1f} MB)")
    log(f"  elapsed      : {elapsed:.1f} s ({elapsed / 60:.1f} min)")
    if failures:
        log(f"  FAILURE LIST ({len(failures)}):")
        for f in failures[:50]:
            log(f"    - {f['doc']} sheet {f['sheet']}: {f['error']}")
        if len(failures) > 50:
            log(f"    ... and {len(failures) - 50} more (see {FAILURE_PATH})")
    log("render.py end")
    log.close()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
