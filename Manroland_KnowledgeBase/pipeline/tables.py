#!/usr/bin/env python
"""
tables.py -- reconstruct the *tabular* content of sheets that are tables rather
than wire diagrams (Reference module / Terminal strip / Index / Contents).

Those sheets hold a pin map whose rows read like

    PIN   BYTE.BIT   STROMPFAD
    3A 3B 3C   0.0
    4A 4B 4C   0.1      /328.B

Reconstructing them as real rows is the difference between a reader having to
guess which numbers go together and being able to read a table.

Method (geometry only - no OCR):
  1. find horizontal rules and vertical rules from the vector drawings;
  2. build the cell grid from their intersections;
  3. assign each text word to the cell that contains its centre;
  4. emit rows in reading order.

Output: data/derived/tables/<dockey>_<sheet>.json
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from schema import DOCUMENTS, clean  # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "data", "derived", "tables")

MIN_H_RULE = 40.0     # a horizontal rule must be at least this wide
MIN_V_RULE = 15.0     # a vertical rule must be at least this tall
TOL = 1.6             # coordinate snapping tolerance


def rules(page):
    """Extract horizontal and vertical rule coordinates of *local* table grids.

    Full-page frame lines are excluded, otherwise the whole sheet would look
    like one giant table.
    """
    PAGE_W = 1190.6
    PAGE_H = 841.9
    hs, vs = [], []
    seen = set()

    def add_h(y, x0, x1):
        if x1 - x0 < MIN_H_RULE:
            return
        if (x1 - x0) > 0.80 * PAGE_W:      # page frame
            return
        if x0 < 60 and x1 > 1170:          # frame
            return
        if y >= 769.0:                     # title block, handled separately
            return
        k = (round(y, 1), round(x0, 1), round(x1, 1))
        if k in seen:
            return
        seen.add(k)
        hs.append(k)

    def add_v(x, y0, y1):
        if y1 - y0 < MIN_V_RULE:
            return
        if (y1 - y0) > 0.90 * PAGE_H:      # page frame
            return
        if y0 >= 769.0:                    # title block
            return
        k = (round(x, 1), round(y0, 1), round(y1, 1))
        if k in seen:
            return
        seen.add(k)
        vs.append(k)

    for p in page.get_drawings():
        for it in p["items"]:
            if it[0] == "l":
                a, b = it[1], it[2]
                if abs(a.y - b.y) < 0.6 and abs(a.x - b.x) >= MIN_H_RULE:
                    add_h(a.y, min(a.x, b.x), max(a.x, b.x))
                elif abs(a.x - b.x) < 0.6 and abs(a.y - b.y) >= MIN_V_RULE:
                    add_v(a.x, min(a.y, b.y), max(a.y, b.y))
            elif it[0] == "re":
                r = it[1]
                if r.width >= MIN_H_RULE and r.height < 1.5:
                    add_h(r.y0, r.x0, r.x1)
                elif r.height >= MIN_V_RULE and r.width < 1.5:
                    add_v(r.x0, r.y0, r.y1)
        r = p["rect"]
        if r.height < 1.5 and r.width >= MIN_H_RULE:
            add_h(r.y0, r.x0, r.x1)
        elif r.width < 1.5 and r.height >= MIN_V_RULE:
            add_v(r.x0, r.y0, r.y1)
    return sorted(set(hs)), sorted(set(vs))


def make_grid(hs, vs):
    """Turn rules into row/column bands.

    Returns (row_bands, col_bands) where row_bands are (y_top, y_bottom) and
    col_bands are (x_left, x_right).  Only rules that belong to a *local* grid
    are used, so the drawing frame and the title block are excluded.
    """
    ys = sorted({y for (y, _a, _b) in hs})
    xs = sorted({x for (x, _a, _b) in vs})

    def collapse(vals):
        out = []
        for v in vals:
            if out and abs(v - out[-1]) < TOL:
                continue
            out.append(v)
        return out

    ys = collapse(ys)
    xs = collapse(xs)
    row_bands = [(ys[i], ys[i + 1]) for i in range(len(ys) - 1)
                 if ys[i + 1] - ys[i] > 4]
    col_bands = [(xs[i], xs[i + 1]) for i in range(len(xs) - 1)
                 if xs[i + 1] - xs[i] > 4]
    return row_bands, col_bands


def cell_of(cx, cy, row_bands, col_bands):
    r = c = None
    for i, (a, b) in enumerate(row_bands):
        if a <= cy <= b:
            r = i
            break
    for j, (a, b) in enumerate(col_bands):
        if a <= cx <= b:
            c = j
            break
    return r, c


def page_tables(page):
    hs, vs = rules(page)
    if len(hs) < 2 or len(vs) < 2:
        return []

    # ---- split into separate tables at large horizontal gaps between rules --
    col_xs = sorted({v[0] for v in vs})
    groups = [[col_xs[0]]]
    for x in col_xs[1:]:
        if x - groups[-1][-1] > 110:           # big gap -> new table
            groups.append([x])
        else:
            groups[-1].append(x)
    groups = [g for g in groups if len(g) >= 2]
    if not groups:
        return []

    words = []
    for w in page.get_text("words"):
        t = clean(w[4])
        if not t:
            continue
        if w[2] <= 57.7:
            continue
        if w[1] >= 769.0:
            continue
        if re.fullmatch(r"[A-H]", t) and (w[3] <= 16 or w[1] >= 828):
            continue
        words.append({"t": t, "cx": (w[0] + w[2]) / 2.0,
                      "cy": (w[1] + w[3]) / 2.0, "x": w[0], "y": w[1]})

    out = []
    for grp in groups:
        gx0, gx1 = grp[0], grp[-1]
        sub_hs = [h for h in hs
                  if not (h[2] < gx0 - 2 or h[1] > gx1 + 2)]
        sub_vs = [v for v in vs if gx0 - 2 <= v[0] <= gx1 + 2]
        if len(sub_hs) < 2 or len(sub_vs) < 2:
            continue
        row_bands, col_bands = make_grid(sub_hs, sub_vs)
        if len(row_bands) < 2 or len(col_bands) < 2:
            continue
        gy0 = min(a for a, _ in row_bands)
        gy1 = max(b for _, b in row_bands)

        cells = defaultdict(list)
        for w in words:
            if not (gx0 - 2 <= w["cx"] <= gx1 + 2 and gy0 - 2 <= w["cy"] <= gy1 + 2):
                continue
            r, c = cell_of(w["cx"], w["cy"], row_bands, col_bands)
            if r is None or c is None:
                continue
            cells[(r, c)].append(w)

        rows = []
        for r in range(len(row_bands)):
            vals = []
            for c in range(len(col_bands)):
                ws = sorted(cells.get((r, c), []), key=lambda w: (w["y"], w["x"]))
                vals.append(" ".join(w["t"] for w in ws))
            if any(vals):
                rows.append({"y": round(row_bands[r][0], 1), "cells": vals})
        if len(rows) < 2:
            continue

        # Split a merged grid into its constituent tables at any column band
        # that holds no text in ANY row.  Reference-module sheets routinely put
        # two independent pin tables side by side, and without this the two
        # would be presented as one table with duplicated pin rows -- which was
        # an observed real source of misreading.
        live_cols = [c for c in range(len(col_bands))
                     if any(row["cells"][c] for row in rows)]
        runs = []
        if live_cols:
            start = prev = live_cols[0]
            for c in live_cols[1:]:
                if c == prev + 1:
                    prev = c
                else:
                    runs.append((start, prev))
                    start = prev = c
            runs.append((start, prev))

        for (c0, c1) in runs:
            sub_rows = []
            for row in rows:
                vals = row["cells"][c0:c1 + 1]
                if any(vals):
                    sub_rows.append({"y": row["y"], "cells": vals})
            if len(sub_rows) < 2:
                continue
            out.append({
                "bbox": [round(col_bands[c0][0], 1),
                         round(gy0, 1),
                         round(col_bands[c1][1], 1),
                         round(gy1, 1)],
                "n_rows": len(sub_rows),
                "n_cols": c1 - c0 + 1,
                "rows": sub_rows,
            })
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    pdf_dir = os.path.join(os.path.dirname(ROOT), "Diagram Manroland")
    only = sys.argv[1] if len(sys.argv) > 1 else None
    total = withtab = 0
    for pdf_name, dockey, _c in DOCUMENTS:
        if only and only not in (dockey, pdf_name):
            continue
        path = os.path.join(pdf_dir, pdf_name)
        d = pymupdf.open(path)
        n = 0
        for i in range(d.page_count):
            tabs = page_tables(d[i])
            if tabs:
                n += 1
                withtab += 1
                fp = os.path.join(OUT, "%s_%04d.json" % (dockey.lstrip("+"), i + 1))
                with open(fp, "w", encoding="utf-8") as f:
                    json.dump({"doc": dockey, "sheet": i + 1, "tables": tabs}, f,
                              ensure_ascii=False)
            total += 1
        print("%-10s pages=%3d with_tables=%3d" % (dockey, d.page_count, n), flush=True)
    print("TOTAL pages=%d with_tables=%d" % (total, withtab))


if __name__ == "__main__":
    main()
