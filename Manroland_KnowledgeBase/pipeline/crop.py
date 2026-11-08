#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crop.py -- render an arbitrary rectangular region of one diagram sheet at very
high resolution, so a human or an AI can zoom into any detail.

Coordinates are **PDF points** with the origin at the TOP-LEFT of the page
(matching PyMuPDF / MuPDF page space).  A3 landscape sheets are 1190.55 x 841.89 pt,
so `--box 0,0,1190.55,841.89` reproduces the whole page.

Examples
--------
  # title block of +Ax sheet 21, at 600 DPI (the default)
  python crop.py --doc +Ax --sheet 21 --box 20,760,600,841.89 --out crop.png

  # a cross-reference annotation at 1200 DPI
  python crop.py --doc +EA --sheet 200 --box 400,300,560,380 --dpi 1200 --out xref.png

  # whole page, grayscale
  python crop.py --doc +FB --sheet 9 --out fb9.png --mode gray

Output defaults to grayscale (anti-aliased) because at 600+ DPI that is the most
faithful thing to read text from; pass --mode bilevel for hard 2-level edges or
--mode rgb to keep colour.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:  # pragma: no cover
    sys.exit("PyMuPDF is required: import pymupdf failed")

from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
DEFAULT_SRC = Path(r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland")

DOCUMENTS: dict[str, str] = {
    "+FB": "Cicuit Diagram +FB.pdf",
    "+Ax": "Circuit Diagram +Ax.pdf",
    "+BA_Cx_DA": "Circuit Diagram +BA, Cx, DA.pdf",
    "+EA": "Circuit Diagram +EA.pdf",
    "+FA": "Circuit Diagram +FA.pdf",
    "+Jx": "Circuit Diagram +Jx.pdf",
}

DEFAULT_DPI = 600


def resolve_pdf(doc: str, src: Path) -> Path:
    """Accept a document key ('+Ax'), a bare filename, or a full path."""
    raw = Path(doc)
    if raw.exists():
        return raw
    key = doc.strip()
    if key in DOCUMENTS:
        return src / DOCUMENTS[key]
    # try to match a filename directly
    cand = src / doc
    if cand.exists():
        return cand
    # try loose key match, e.g. "Ax" or "+ba_cx_da"
    low = key.lower().lstrip("+")
    for k, fname in DOCUMENTS.items():
        if k.lower().lstrip("+") == low:
            return src / fname
    raise SystemExit(
        f"unknown document {doc!r}. Known keys: {', '.join(DOCUMENTS)} "
        f"(or pass a path to a PDF)"
    )


def parse_box(text: str) -> pymupdf.Rect:
    parts = [p.strip() for p in text.replace(";", ",").split(",") if p.strip()]
    if len(parts) != 4:
        raise SystemExit(f"--box needs 4 comma-separated numbers x0,y0,x1,y1 (got {text!r})")
    try:
        x0, y0, x1, y1 = (float(p) for p in parts)
    except ValueError:
        raise SystemExit(f"--box values must be numbers (got {text!r})")
    if x1 < x0:
        x0, x1 = x1, x0
    if y1 < y0:
        y0, y1 = y1, y0
    if x1 - x0 <= 0 or y1 - y0 <= 0:
        raise SystemExit("--box has zero area")
    return pymupdf.Rect(x0, y0, x1, y1)


def build_lut(threshold: int) -> list[int]:
    t = max(0, min(255, int(threshold)))
    return [0] * (t + 1) + [255] * (255 - t)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="High-DPI crop of one diagram sheet (box in PDF points, top-left origin).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--doc", required=True,
                   help="document key ('+Ax'), PDF filename, or full path")
    p.add_argument("--sheet", type=int, required=True, help="1-based sheet number")
    p.add_argument("--dpi", type=float, default=DEFAULT_DPI, help="rasterisation DPI")
    p.add_argument("--box", default=None,
                   help="crop rectangle x0,y0,x1,y1 in PDF points; omit for the whole page")
    p.add_argument("--out", required=True, help="output PNG path")
    p.add_argument("--mode", choices=("gray", "bilevel", "rgb"), default="gray",
                   help="output colour mode")
    p.add_argument("--threshold", type=int, default=160,
                   help="bilevel cutoff 0-255 (only with --mode bilevel)")
    p.add_argument("--pad", type=float, default=0.0,
                   help="expand the box by this many PDF points on every side")
    p.add_argument("--src", default=str(DEFAULT_SRC), help="directory holding the source PDFs")
    args = p.parse_args(argv)

    src = Path(args.src)
    pdf_path = resolve_pdf(args.doc, src)
    if not pdf_path.exists():
        raise SystemExit(f"source PDF not found: {pdf_path}")

    doc = pymupdf.open(pdf_path)
    try:
        if not (1 <= args.sheet <= len(doc)):
            raise SystemExit(f"--sheet {args.sheet} out of range 1..{len(doc)}")
        page = doc[args.sheet - 1]
        page_rect = page.rect

        if args.box:
            clip = parse_box(args.box)
        else:
            clip = pymupdf.Rect(page_rect)
        if args.pad:
            clip = pymupdf.Rect(clip.x0 - args.pad, clip.y0 - args.pad,
                                clip.x1 + args.pad, clip.y1 + args.pad)
        clip = clip & page_rect                       # clamp to the page
        if clip.is_empty:
            raise SystemExit(f"crop box {tuple(clip)} does not intersect the page "
                             f"{page_rect.width:.2f} x {page_rect.height:.2f} pt")

        zoom = args.dpi / 72.0
        matrix = pymupdf.Matrix(zoom, zoom)

        if args.mode == "rgb":
            pix = page.get_pixmap(matrix=matrix, clip=clip,
                                  colorspace=pymupdf.csRGB, alpha=False)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        else:
            pix = page.get_pixmap(matrix=matrix, clip=clip,
                                  colorspace=pymupdf.csGRAY, alpha=False)
            gray = Image.frombytes("L", (pix.width, pix.height), pix.samples)
            img = gray if args.mode == "gray" else \
                gray.point(build_lut(args.threshold)).convert("1", dither=Image.NONE)

        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        img.save(out, "PNG", optimize=True)
        size = out.stat().st_size

        print(f"doc={args.doc} sheet={args.sheet} dpi={args.dpi:g} mode={args.mode}")
        print(f"page={page_rect.width:.2f}x{page_rect.height:.2f}pt  "
              f"box=({clip.x0:.2f},{clip.y0:.2f})-({clip.x1:.2f},{clip.y1:.2f})pt  "
              f"({clip.width:.2f}x{clip.height:.2f}pt)")
        print(f"out={out}  {img.width}x{img.height}px  {size / 1024:.1f} KB  "
              f"({img.width / clip.width:.2f} px/pt)")
    finally:
        doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
