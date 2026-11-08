#!/usr/bin/env python
"""
extract.py -- Stage 1: structured, lossless extraction from the manroland R700
IEC/UL wiring-diagram PDFs.

The source PDFs are born-vector CAE exports (CIM-TEAM GmbH, 2010-2012).  Every
label is real selectable text at real coordinates, so this stage reads the
PDF's own text layer and vector geometry.  OCR is never used.

Key insight used throughout: the PDF's own *text block* grouping is already
semantic.  A wire-end annotation block contains, on one visual row,

    [target description] [path number] [cross reference]

e.g.  'A244:bn'  '#67'  '/13.G'   ->  "this wire continues on sheet 13,
column G, line 67, at terminal A244:bn".

Output: data/raw/<dockey>/<sheet>.json

Usage
-----
    python extract.py
    python extract.py --only +Ax
    python extract.py --pages 1-40
    python extract.py --force
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import traceback
from collections import Counter, defaultdict

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import grammar as G  # noqa: E402
from schema import (  # noqa: E402
    DOCUMENTS, DOC_TITLE_CODE, NOTICE_X_MAX, TITLE_Y0, clean,
    column_index, column_of,
)

ROOT = os.path.dirname(HERE)

# ---------------------------------------------------------------------------
# Title-block zones (x_lo, x_hi, y_lo, y_hi), valid across both layouts
# ---------------------------------------------------------------------------
ZONES = {
    "created_date": (125, 205, 772.5, 778.0),
    "created_by": (84, 146, 786.5, 793.5),
    "modified_by": (84, 146, 814.0, 821.0),
    "approved_by": (125, 215, 799.5, 806.5),
    "section": (596, 692, 795.0, 802.0),
    "machine_type": (690, 762, 794.5, 802.0),
    "document_code": (898, 1064, 771.8, 778.0),
    "sheet": (938, 982, 793.2, 798.5),
    "sheet_total": (984, 1016, 793.2, 798.5),
    "replaces": (938, 1066, 814.5, 821.0),
    "serie": (760, 862, 786.0, 793.5),
    "norm": (796, 908, 786.0, 826.5),
    "title_de": (330, 612, 771.8, 781.0),
    "title_en": (330, 612, 785.5, 794.0),
    "paper": (1010, 1078, 792.0, 799.5),
}


def word_items(page):
    out = []
    for w in page.get_text("words"):
        t = clean(w[4])
        if not t:
            continue
        out.append({"t": t, "x": w[0], "y": w[1], "x1": w[2], "y1": w[3]})
    return out


def in_zone(i, z):
    lo, hi, ylo, yhi = ZONES[z]
    return lo <= i["x"] <= hi and ylo <= i["y"] <= yhi


def zone_items(items, z):
    out = [i for i in items if in_zone(i, z)]
    out.sort(key=lambda i: (round(i["y"], 1), i["x"]))
    return out


def zone_text(items, z, sep=" "):
    return sep.join(i["t"] for i in zone_items(items, z)).strip()


# ---------------------------------------------------------------------------
# Title block
# ---------------------------------------------------------------------------
def parse_title_block(page):
    items = word_items(page)
    tb = {
        "created_date": None, "created_by": None, "modified_date": None,
        "modified_by": None, "approved_by": None, "section": None,
        "machine_type": None, "document_code": None, "sheet": None,
        "sheet_total": None, "replaces": None, "serie": None,
        "norm_rows": [], "section_title_de": None, "section_title_en": None,
        "paper": None, "drawing_title_de": None, "drawing_title_en": None,
    }

    cd = [i for i in zone_items(items, "created_date") if G.T_DATE.match(i["t"])]
    tb["created_date"] = cd[0]["t"] if cd else None

    cb = [i for i in zone_items(items, "created_by")
          if not G.T_EMPTY_MARK.match(i["t"])]
    tb["created_by"] = cb[0]["t"] if cb else None

    mb = [i for i in zone_items(items, "modified_by")
          if not G.T_EMPTY_MARK.match(i["t"])]
    tb["modified_by"] = mb[0]["t"] if mb else None

    ab = [i for i in zone_items(items, "approved_by")
          if not G.T_EMPTY_MARK.match(i["t"])]
    tb["approved_by"] = ab[0]["t"] if ab else None

    sec = [i for i in zone_items(items, "section") if G.T_SECTION.match(i["t"])]
    tb["section"] = sec[0]["t"] if sec else None
    if tb["section"] is None:
        # 'Ort' cell may hold the section; scan a wider band in that cell
        alt = [i for i in items if 596 <= i["x"] <= 695 and 793 <= i["y"] <= 803
               and G.T_SECTION.match(i["t"])]
        if alt:
            tb["section"] = alt[0]["t"]

    mt = [i for i in zone_items(items, "machine_type") if G.T_MACHINE.match(i["t"])]
    tb["machine_type"] = mt[0]["t"] if mt else None

    dc = [i for i in zone_items(items, "document_code")
          if G.T_DOCCODE_LOOSE.match(i["t"])]
    if not dc:
        dc = [i for i in items if G.T_DOCCODE_LOOSE.match(i["t"])
              and 898 <= i["x"] <= 1080 and 770 <= i["y"] <= 780]
    tb["document_code"] = max(dc, key=lambda i: len(i["t"]))["t"] if dc else None

    nums = [i for i in items if G.T_NUM.match(i["t"])
            and 793.0 <= i["y"] <= 798.6 and 936 <= i["x"] <= 1018]
    nums.sort(key=lambda i: i["x"])
    if nums:
        tb["sheet"] = int(nums[0]["t"])
        if len(nums) > 1:
            tb["sheet_total"] = int(nums[1]["t"])

    rp = zone_items(items, "replaces")
    tb["replaces"] = rp[0]["t"] if rp else None

    se = [i for i in items
          if 760 <= i["x"] <= 900 and 786.0 <= i["y"] <= 794.0
          and re.fullmatch(r"\d{3,5}", i["t"])]
    se.sort(key=lambda i: (i["y"], i["x"]))
    tb["serie"] = se[0]["t"] if se else None

    cur = None
    for i in zone_items(items, "norm"):
        if G.T_NORMROW.match(i["t"]) or G.T_NORMODERN.match(i["t"]):
            cur = {"row": i["t"].rstrip(":"), "items": []}
            tb["norm_rows"].append(cur)
        elif cur is not None:
            cur["items"].append(i["t"])
    for row in tb["norm_rows"]:
        row["text"] = " ".join(row.pop("items")).strip()

    def strip_boiler(v):
        if not v:
            return None
        v = re.sub(r"\b(STROMLAUFPLAN|CIRCUIT\s+DIAGRAM|CIRCUIT|DIAGRAM)\b", "", v)
        v = re.sub(r"\s{2,}", " ", v).strip(" ,")
        return v or None

    tb["section_title_de"] = strip_boiler(zone_text(items, "title_de"))
    tb["section_title_en"] = strip_boiler(zone_text(items, "title_en"))

    if any(G.T_PAPER.match(i["t"]) for i in zone_items(items, "paper")):
        tb["paper"] = "DIN A3"

    # The drawing class is always STROMLAUFPLAN / CIRCUIT DIAGRAM
    tb["drawing_title_de"] = "STROMLAUFPLAN"
    tb["drawing_title_en"] = "CIRCUIT DIAGRAM"
    return tb


# ---------------------------------------------------------------------------
# Classification of one label line
# ---------------------------------------------------------------------------
def classify(text):
    t = text.strip()
    if not t:
        return None, None

    m = G.RE_XREF.match(t)
    if m:
        return "xref", {"sheet": int(m.group(1)), "column": m.group(2),
                        "pin": m.group(3)}

    m = G.RE_PATH.match(t)
    if m:
        return "path", {"path": int(m.group(1))}

    m = G.RE_PINPAIR.match(t)
    if m:
        return "pinpair", {"pin": int(m.group(1)), "of": int(m.group(2))}

    m = G.RE_XSECTION.match(t)
    if m:
        return "xsection", {"mm2": float(m.group(1).replace(",", "."))}

    low = t.lower()
    if low in G.WIRE_COLOURS:
        code, de, en = G.WIRE_COLOURS[low]
        return "colour", {"code": code, "de": de, "en": en}

    if t in ("X", "x"):
        return "placeholder", None

    # -- device order code / part-number marker -----------------------------
    if G.RE_ORDER_CODE.match(t) and t not in G.DOCUMENT_CODES:
        return "ordercode", {"code": t}
    if G.RE_NO_PART.match(t):
        return "nopart", {"marker": t}

    # -- potential with a DC/AC qualifier, e.g. "24V DC" ---------------------
    mq = G.RE_NET_QUALIFIER.match(t)
    if mq:
        mc = G.RE_NET_CORE.match(mq.group("net"))
        if mc:
            sign = mc.group("sign") or ""
            return "net", {"net": sign + mc.group("net"), "raw": t,
                           "devices": [], "terminal": None,
                           "qualifier": mq.group("qual")}

    # -- several potentials written as one label, e.g. "400V,24V" ------------
    if "," in t and " " not in t:
        parts = [x for x in G.RE_NET_LIST_SPLIT.split(t) if x]
        if len(parts) >= 2:
            nets = []
            for raw_part in parts:
                mc = G.RE_NET_CORE.match(raw_part)
                if mc:
                    sign = mc.group("sign") or ""
                    nets.append(sign + mc.group("net"))
            if nets:
                return "net", {"net": nets[0], "nets": nets, "raw": t,
                               "devices": [], "terminal": None, "list": True}

    # -- dotted reference chain ---------------------------------------------
    # Normalise the exporter's occasional space after the dot ("24V. X001:23")
    # so the reference still parses.
    t_probe = G.RE_DOTTED_SPACE.sub(r"\1.\2", t)

    if G.RE_DOTTED.match(t_probe) or G.RE_DOTTED_PLACEHOLDER.match(t_probe):
        head = re.split(r"[.:(\s]", t_probe)[0]
        m2 = G.RE_NET_CORE.match(head)
        body = t_probe.split(":")[0]
        tail = t_probe.split(":")[-1].strip() if ":" in t_probe else None
        if tail is not None and tail in G.PLACEHOLDER_TERMINALS:
            tail = None
        middle = [x for x in body.split(".")[1:] if x and x != " "]
        # Reject prose such as "N. Hitzel" (a person's name): a real reference
        # segment looks like X001 / A345 / X404A / X214\1, is all digits, or is
        # a bare letter placeholder such as "M".
        SEG = re.compile(r"^(?:[A-Z]|\d+|[A-Z]{1,3}\d{1,4}[A-Z]{0,2}(?:\\{1,2}\d{1,2})?)$")
        if any(not SEG.match(seg.replace(" ", "")) for seg in middle):
            return "text", None
        if m2:
            sign = m2.group("sign") or ""
            return "net", {"net": sign + m2.group("net"), "raw": t,
                           "devices": middle, "terminal": tail}
        return "devref", {"raw": t, "head": head, "devices": middle,
                          "terminal": tail}

    m = G.RE_NET_CORE.match(t)
    if m:
        sign = m.group("sign") or ""
        return "net", {"net": sign + m.group("net"), "raw": t,
                       "devices": [], "terminal": None}

    # -- potential with a conductor index, e.g. "PE/3" -----------------------
    # Checked AFTER the device-tag forms below, because "M102/1" and "H240/01"
    # are device designators (class letter + number + sub-unit), not rails.
    # This block is intentionally placed after RE_DEV_BARE.

    m = G.RE_DEV_SIGNED.match(t)
    if m:
        return "devtag", {"sign": m.group("sign"), "cls": m.group("cls"),
                          "num": m.group("num"), "sub": m.group("sub"),
                          "loc": m.group("loc"), "pin": m.group("pin"),
                          "tag": t}

    m = G.RE_DEV_BARE.match(t)
    if m and re.search(r"\d", t) and len(t) <= 24:
        # guard against ordinary words such as "INPUT", "DINA3"
        return "devtag", {"sign": None, "cls": m.group("cls"),
                          "num": m.group("num"), "sub": m.group("sub"),
                          "loc": m.group("loc"), "pin": m.group("pin"),
                          "tag": t}

    # -- potential with a conductor index, e.g. "PE/3" -----------------------
    # Deliberately restricted: the base must be an unambiguous rail name
    # (contains 'V', or is PE/N).  Without this guard "M102/1" and "H240/01"
    # - genuine device designators - would be mis-read as rails, because the
    # class letters L, M and H can also start a potential name.
    mi = G.RE_NET_INDEX.match(t)
    if mi:
        base = mi.group("net")
        mc = G.RE_NET_CORE.match(base)
        if mc and ("V" in base.upper() or base.upper() in ("PE", "N")):
            sign = mc.group("sign") or ""
            return "net", {"net": sign + mc.group("net"), "raw": t,
                           "devices": [], "terminal": None,
                           "index": int(mi.group("idx"))}

    # Anything carrying a letter is prose/reference, not a bare number.
    if re.search(r"[A-Za-zÄÖÜäöüß]", t):
        toks = [x for x in re.split(r"[\s,]+", t) if x]
        parsed = []
        for tok in toks:
            mt = G.RE_DEV_SIGNED.match(tok) or G.RE_DEV_BARE.match(tok)
            if mt and re.search(r"\d", tok):
                parsed.append(tok)
            elif G.RE_DOTTED.match(tok) and re.search(r"\d", tok):
                parsed.append(tok)
        return "text", ({"tokens": parsed} if parsed else None)

    if re.fullmatch(r"[0-9.,\-+/ ]+", t):
        return "numeric", None
    return "other", None
def is_boilerplate(x0, y0, x1, y1, text):
    if x1 <= NOTICE_X_MAX + 1:
        return True
    if re.fullmatch(r"[A-H]", text) and (y1 <= 16 or y0 >= 828):
        return True
    if y0 >= TITLE_Y0:
        return True
    return False


# ---------------------------------------------------------------------------
# Annotations: one PDF text block == one wire-end annotation
# ---------------------------------------------------------------------------
def build_annotations(lines):
    by_blk = defaultdict(list)
    for ln in lines:
        by_blk[ln["blk"]].append(ln)

    annos = []
    for blk, grp in by_blk.items():
        grp.sort(key=lambda l: (l["y0"], l["x0"]))
        x0 = min(l["x0"] for l in grp)
        y0 = min(l["y0"] for l in grp)
        x1 = max(l["x1"] for l in grp)
        y1 = max(l["y1"] for l in grp)
        annos.append({
            "blk": blk,
            "bbox": [round(x0, 2), round(y0, 2), round(x1, 2), round(y1, 2)],
            "col": column_of((x0 + x1) / 2.0),
            "col_idx": column_index((x0 + x1) / 2.0),
            "rot": grp[0]["rot"],
            "text": " ".join(l["text"] for l in grp),
            "kinds": [l["kind"] for l in grp],
            "xref": [l["payload"] for l in grp
                     if l["kind"] == "xref" and l["payload"]],
            "paths": [l["payload"]["path"] for l in grp
                      if l["kind"] == "path" and l["payload"]],
            "targets": [l["text"] for l in grp
                        if l["kind"] not in ("xref", "path", "pinpair")],
            "lines": [{"t": l["text"], "k": l["kind"], "p": l["payload"],
                       "rot": l["rot"], "bbox": l["bbox"]}
                      for l in sorted(grp, key=lambda l: l["x0"])],
        })
    annos.sort(key=lambda a: (round(a["bbox"][1], 1), round(a["bbox"][0], 1)))
    return annos


# ---------------------------------------------------------------------------
# One page
# ---------------------------------------------------------------------------
def extract_page(page, dockey, sheet_no):
    raw = page.get_text("dict")
    lines = []

    for bno, blk in enumerate(raw["blocks"]):
        if blk.get("type") != 0:
            continue
        for ln in blk["lines"]:
            txt = clean("".join(sp.get("text", "") for sp in ln["spans"]))
            if not txt:
                continue
            x0, y0, x1, y1 = ln["bbox"]
            if is_boilerplate(x0, y0, x1, y1, txt):
                continue
            dy = ln["dir"][1]
            rot = 0 if abs(dy) < 0.35 else (-90 if dy < 0 else 90)
            kind, payload = classify(txt)
            sizes = [sp.get("size", 0) for sp in ln["spans"]]
            lines.append({
                "text": txt, "kind": kind, "payload": payload,
                "bbox": [round(v, 2) for v in ln["bbox"]],
                "x0": x0, "y0": y0, "x1": x1, "y1": y1,
                "col": column_of((x0 + x1) / 2.0),
                "col_idx": column_index((x0 + x1) / 2.0),
                "rot": rot,
                "size": round(max(sizes), 2) if sizes else None,
                "blk": bno,
            })

    tb = parse_title_block(page)
    annos = build_annotations(lines)

    bucket = defaultdict(list)
    for ln in lines:
        base = {"col": ln["col"], "col_idx": ln["col_idx"],
                "bbox": ln["bbox"], "rot": ln["rot"], "text": ln["text"]}
        k = ln["kind"]
        if k == "placeholder":
            bucket["placeholders"].append(base)
        elif k in ("devtag", "devref", "net", "xsection", "colour",
                   "text", "numeric", "pinpair", "other", "ordercode", "nopart"):
            rec = {**base}
            if isinstance(ln["payload"], dict):
                rec.update(ln["payload"])
            bucket[k].append(rec)

    xrefs_out = []
    for a in annos:
        if not a["xref"]:
            continue
        tgt = " ".join(a["targets"]).strip()
        for xr in a["xref"]:
            xrefs_out.append({
                "to_sheet": xr["sheet"],
                "to_column": xr["column"],
                "to_pin": xr.get("pin"),
                "path": a["paths"][0] if a["paths"] else None,
                "target": tgt or None,
                "col": a["col"], "col_idx": a["col_idx"],
                "bbox": a["bbox"],
            })
    xrefs_out.sort(key=lambda x: (x["bbox"][1], x["bbox"][0]))

    paths_on_sheet = sorted({l["payload"]["path"] for l in lines
                             if l["kind"] == "path" and l["payload"]})

    return {
        "doc": dockey,
        "doc_title_code": DOC_TITLE_CODE.get(dockey),
        "sheet": sheet_no,
        "sheet_total": tb.get("sheet_total"),
        "title_block": tb,
        "path_numbers": paths_on_sheet,
        "counts": {
            "lines": len(lines),
            "annotations": len(annos),
            "devtag": len(bucket["devtag"]),
            "devref": len(bucket["devref"]),
            "net": len(bucket["net"]),
            "xrefs_out": len(xrefs_out),
            "text": len(bucket["text"]),
            "xsections": len(bucket["xsection"]),
            "colours": len(bucket["colour"]),
            "placeholders": len(bucket["placeholders"]),
            "numeric": len(bucket["numeric"]),
        },
        "annotations": annos,
        "xrefs_out": xrefs_out,
        "devtag": bucket["devtag"],
        "devref": bucket["devref"],
        "nets": bucket["net"],
        "xsections": bucket["xsection"],
        "colours": bucket["colour"],
        "texts": bucket["text"],
        "numerics": bucket["numeric"],
        "ordercodes": bucket["ordercode"],
        "noparts": bucket["nopart"],
        "placeholders": bucket["placeholders"],
        "lines": lines,
    }


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def parse_ranges(spec, nmax):
    keep = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            keep.update(range(int(a), int(b) + 1))
        else:
            keep.add(int(part))
    return {p for p in keep if 1 <= p <= nmax}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--pages")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    pdf_dir = os.path.join(os.path.dirname(ROOT), "Diagram Manroland")
    out_dir = os.path.join(ROOT, "data", "raw")
    log_dir = os.path.join(ROOT, "logs")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)
    logf = open(os.path.join(log_dir, "extract.log"), "a", encoding="utf-8")

    def log(m):
        print(m, flush=True)
        logf.write(m + "\n")
        logf.flush()

    t_start = time.time()
    grand = Counter()
    failures = []

    for pdf_name, dockey, _code in DOCUMENTS:
        if args.only and args.only not in (dockey, pdf_name):
            continue
        path = os.path.join(pdf_dir, pdf_name)
        if not os.path.exists(path):
            log("MISSING PDF %s" % path)
            failures.append((dockey, 0, "missing pdf"))
            continue
        d = pymupdf.open(path)
        sub = os.path.join(out_dir, dockey.lstrip("+"))
        os.makedirs(sub, exist_ok=True)
        want = parse_ranges(args.pages, d.page_count) if args.pages else None
        done = skipped = 0
        t0 = time.time()
        for i in range(d.page_count):
            sheet = i + 1
            if want is not None and sheet not in want:
                continue
            fp = os.path.join(sub, "%04d.json" % sheet)
            if not args.force and os.path.exists(fp) and os.path.getsize(fp) > 500:
                skipped += 1
                continue
            try:
                rec = extract_page(d[i], dockey, sheet)
                # Some exporters omit the "M" of "Blatt: N - M" on most sheets
                # (all 247 sheets of +BA_Cx_DA except sheet 1).  Fall back to
                # the document's real page count, which is what M denotes.
                if not rec.get("sheet_total"):
                    rec["sheet_total"] = d.page_count
                    rec["title_block"]["sheet_total"] = d.page_count
                    rec["title_block"]["sheet_total_source"] = "document page count"
                with open(fp, "w", encoding="utf-8") as f:
                    json.dump(rec, f, ensure_ascii=False)
                done += 1
                for k, v in rec["counts"].items():
                    grand[k] += v
            except Exception as exc:  # noqa: BLE001
                failures.append((dockey, sheet, repr(exc)))
                log("FAIL %s:%d %r" % (dockey, sheet, exc))
                log(traceback.format_exc())
        log("%-10s pages=%3d extracted=%3d skipped=%3d %.1fs"
            % (dockey, d.page_count, done, skipped, time.time() - t0))

    log("")
    log("TOTAL %s" % dict(sorted(grand.items())))
    log("failures=%d elapsed=%.1fs" % (len(failures), time.time() - t_start))
    logf.close()
    if failures:
        print("FAILED:", failures[:20])
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
