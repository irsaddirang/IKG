#!/usr/bin/env python
"""
graph.py -- Stage 2: build the navigable knowledge graph from the raw
per-sheet extraction.

Produces data/derived/graph.json containing

  * documents[]      one entry per PDF: sheet count, section title map
  * sheets[]         per sheet: id, section, title, columns used, path numbers
  * nodes[]          every addressable thing: sheets, devices, nets, terminals
  * edges[]          typed, directed relations:
                       xref        sheet -> sheet (wire continues)
                       has_device  sheet -> device
                       net_uses    net    -> device
                       continues   annotation -> annotation (via xref)
  * index            inverted indexes for fast lookup

Sheet ids are globally unique: "<dockey>#<sheet>" e.g. "+Ax#21".
A cross reference "/17.D" is resolved *within the same document*, which is
how the drawings work: each PDF is a self-contained drawing set.

Output is deterministic so it can be diffed between runs.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from schema import DOCUMENTS, SECTION_TOPICS  # noqa: E402

ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "data", "raw")
DER = os.path.join(ROOT, "data", "derived")


def topic_of(de, en):
    blob = ("%s %s" % (de or "", en or "")).upper()
    for pat, label, code in SECTION_TOPICS:
        if pat.upper() in blob:
            return code, label
    return "CIRCUIT", "Circuit diagram"


def load_all():
    sheets = []
    for _pdf, dockey, _code in DOCUMENTS:
        sub = os.path.join(RAW, dockey.lstrip("+"))
        if not os.path.isdir(sub):
            continue
        for fn in sorted(os.listdir(sub)):
            if not fn.endswith(".json"):
                continue
            with open(os.path.join(sub, fn), encoding="utf-8") as f:
                sheets.append(json.load(f))
    sheets.sort(key=lambda s: (s["doc"], s["sheet"]))
    return sheets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    os.makedirs(DER, exist_ok=True)

    sheets = load_all()
    if not sheets:
        print("no raw data; run extract.py first")
        return 1

    def sid(rec):
        return "%s#%d" % (rec["doc"], rec["sheet"])

    # ------------------------------------------------------------------
    # documents
    # ------------------------------------------------------------------
    docs = {}
    for rec in sheets:
        d = rec["doc"]
        ent = docs.setdefault(d, {
            "dockey": d, "title_code": rec.get("doc_title_code"),
            "sheets": 0, "sections": Counter(),
            "document_code": rec["title_block"].get("document_code"),
            "created_date": rec["title_block"].get("created_date"),
        })
        ent["sheets"] += 1
        code, label = topic_of(rec["title_block"].get("section_title_de"),
                               rec["title_block"].get("section_title_en"))
        ent["sections"][code] += 1
        if not ent.get("document_code"):
            ent["document_code"] = rec["title_block"].get("document_code")
        if not ent.get("created_date"):
            ent["created_date"] = rec["title_block"].get("created_date")

    for ent in docs.values():
        ent["sections"] = dict(ent["sections"])

    # ------------------------------------------------------------------
    # sheets
    # ------------------------------------------------------------------
    sheet_recs = []
    edges = []
    for rec in sheets:
        tb = rec["title_block"]
        code, label = topic_of(tb.get("section_title_de"),
                               tb.get("section_title_en"))
        s = {
            "id": sid(rec),
            "doc": rec["doc"],
            "sheet": rec["sheet"],
            "sheet_total": rec.get("sheet_total") or tb.get("sheet_total"),
            "section_code": code,
            "section_topic": label,
            "title_de": tb.get("section_title_de"),
            "title_en": tb.get("section_title_en"),
            "document_code": tb.get("document_code"),
            "created_date": tb.get("created_date"),
            "replaces": tb.get("replaces"),
            "norm_rows": tb.get("norm_rows") or [],
            "path_numbers": rec.get("path_numbers") or [],
            "columns_used": sorted({l["col"] for l in rec["lines"]}),
            "counts": rec["counts"],
        }
        sheet_recs.append(s)

        for x in rec["xrefs_out"]:
            edges.append({
                "type": "xref",
                "from": s["id"],
                "from_column": x["col"],
                "to": "%s#%d" % (rec["doc"], x["to_sheet"]),
                "to_sheet": x["to_sheet"],
                "to_column": x["to_column"],
                "path": x["path"],
                "target": x["target"],
            })

    # ------------------------------------------------------------------
    # devices / nets / terminals
    # ------------------------------------------------------------------
    device_use = defaultdict(lambda: {
        "tag": None, "cls": None, "num": None, "sub": None,
        "sheets": Counter(), "columns": Counter(), "occurrences": 0,
    })
    net_use = defaultdict(lambda: {"net": None, "sheets": Counter(),
                                   "columns": Counter(), "occurrences": 0})
    terminal_use = defaultdict(lambda: {"tag": None, "pin": None,
                                        "sheets": Counter(), "occurrences": 0})
    device_edges = []
    net_edges = []
    sheetcol_refs = Counter()

    for rec in sheets:
        s = sid(rec)
        for d in rec["devtag"]:
            key = d.get("tag") or ""
            if not key:
                continue
            ent = device_use[key]
            ent["tag"] = key
            ent["cls"] = d.get("cls")
            ent["num"] = d.get("num")
            ent["sub"] = d.get("sub")
            ent["sheets"][s] += 1
            ent["columns"][d.get("col")] += 1
            ent["occurrences"] += 1
            device_edges.append({"type": "has_device", "from": s,
                                 "to": key, "column": d.get("col")})
        # Device tokens embedded in multi-token labels, e.g.
        # "+ A497/2 X1.A463:1" or "+A497/2 K160/1:A2, +A497/2 K160:A2".
        for d in rec.get("texts") or []:
            for tok in (d.get("tokens") or []):
                ent = device_use[tok]
                ent["tag"] = tok
                if not ent.get("cls"):
                    mcls = re.match(r"^[+\-]?([A-Za-z]{1,3})\d", tok)
                    if mcls:
                        ent["cls"] = mcls.group(1).upper()
                ent["sheets"][s] += 1
                ent["columns"][d.get("col")] += 1
                ent["occurrences"] += 1
                device_edges.append({"type": "has_device_inline", "from": s,
                                     "to": tok, "column": d.get("col")})
        for d in rec["devref"]:
            raw = d.get("raw") or ""
            if not raw:
                continue
            # A bare "<sheet>.<col>" token (e.g. 005.C) on a terminal-strip
            # sheet is a sheet/column location reference, not a device.
            if re.fullmatch(r"\d{1,3}\.[A-H]", raw):
                sheetcol_refs[raw] += 1
                continue
            # "BYTE.BIT" is a column header on the reference-module pin tables,
            # not a device reference.
            if raw.upper() in ("BYTE.BIT", "BYTE", "BIT"):
                continue
            ent = device_use[raw]
            ent["tag"] = raw
            # derive the class letter from the leading atom, e.g. "X26.A342:1" -> X
            mcls = re.match(r"^[+\-]?([A-Za-z]{1,3})\d", raw)
            if mcls:
                ent["cls"] = mcls.group(1).upper()
            ent["sheets"][s] += 1
            ent["columns"][d.get("col")] += 1
            ent["occurrences"] += 1
            device_edges.append({"type": "has_devref", "from": s,
                                 "to": raw, "column": d.get("col")})
        for n in rec["nets"]:
            # A single label can name several potentials, e.g. "400V,24V".
            keys = n.get("nets") or [n.get("net") or n.get("raw")]
            for key in keys:
                if not key:
                    continue
                ent = net_use[key]
                ent["net"] = key
                ent["sheets"][s] += 1
                ent["columns"][n.get("col")] += 1
                ent["occurrences"] += 1
                net_edges.append({"type": "has_net", "from": s, "to": key,
                                  "column": n.get("col")})
            for dev in n.get("devices") or []:
                net_edges.append({"type": "net_on_device", "from": keys[0],
                                  "to": dev, "sheet": s,
                                  "terminal": n.get("terminal")})
        for t in rec["devtag"]:
            if t.get("pin"):
                tk = "%s:%s" % (t.get("tag"), t.get("pin"))
                ent = terminal_use[tk]
                ent["tag"] = t.get("tag")
                ent["pin"] = t.get("pin")
                ent["sheets"][s] += 1
                ent["occurrences"] += 1

    # ------------------------------------------------------------------
    # cross-reference resolution + integrity
    # ------------------------------------------------------------------
    by_id = {s["id"]: s for s in sheet_recs}
    unresolved = []
    xref_in = Counter()
    for e in edges:
        xref_in[e["to"]] += 1
        if e["to"] not in by_id:
            unresolved.append(e)

    # column-level confirmation: the target sheet must actually have content
    # in the stated column
    col_mismatch = []
    for e in edges:
        tgt = by_id.get(e["to"])
        if not tgt:
            continue
        if not (e["to_column"] in tgt["columns_used"]):
            col_mismatch.append(e)

    for s in sheet_recs:
        s["xref_in_count"] = xref_in.get(s["id"], 0)
        s["xref_out_count"] = sum(1 for e in edges if e["from"] == s["id"])

    # ------------------------------------------------------------------
    # serialise
    # ------------------------------------------------------------------
    def finish(counter_rec, keys):
        out = []
        for k, v in sorted(counter_rec.items()):
            rec = {keys[0]: k}
            for kk in keys[1:]:
                rec[kk] = v.get(kk)
            rec["occurrences"] = v["occurrences"]
            rec["sheets"] = dict(v["sheets"])
            rec["sheet_count"] = len(v["sheets"])
            rec["columns"] = dict(v.get("columns") or {})
            out.append(rec)
        return out

    devices = finish(device_use, ("tag", "cls", "num", "sub"))
    nets = finish(net_use, ("net",))
    terminals = finish(terminal_use, ("tag", "pin"))

    # inverted indexes
    by_sheet = defaultdict(list)
    for e in edges:
        by_sheet[e["from"]].append(e["to"])

    graph = {
        "documents": {k: v for k, v in sorted(docs.items())},
        "sheets": sheet_recs,
        "devices": devices,
        "nets": nets,
        "terminals": terminals,
        "edges": edges,
        "device_edges": device_edges,
        "net_edges": net_edges,
        "sheetcol_refs": dict(sorted(sheetcol_refs.items())),
        "stats": {
            "sheets": len(sheet_recs),
            "documents": len(docs),
            "xref_edges": len([e for e in edges if e["type"] == "xref"]),
            "xref_unresolved": len(unresolved),
            "xref_column_mismatch": len(col_mismatch),
            "devices": len(devices),
            "nets": len(nets),
            "terminals": len(terminals),
            "device_occurrences": sum(d["occurrences"] for d in devices),
            "net_occurrences": sum(n["occurrences"] for n in nets),
        },
    }

    with open(os.path.join(DER, "graph.json"), "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=1)

    # unresolved list for QA
    with open(os.path.join(DER, "xref_issues.json"), "w", encoding="utf-8") as f:
        json.dump({"unresolved": unresolved[:2000],
                   "column_mismatch": col_mismatch[:2000],
                   "counts": {"unresolved": len(unresolved),
                              "column_mismatch": len(col_mismatch)}},
                  f, ensure_ascii=False, indent=1)

    if not args.quiet:
        print(json.dumps(graph["stats"], indent=2))
        print("\nper document:")
        for k, v in graph["documents"].items():
            print("  %-10s sheets=%3d code=%s sections=%s"
                  % (k, v["sheets"], v["document_code"], v["sections"]))
        print("\nunresolved xrefs:", len(unresolved))
        for e in unresolved[:10]:
            print("   ", e)
        print("column mismatches:", len(col_mismatch))
        for e in col_mismatch[:5]:
            print("   ", e)
    return 0


if __name__ == "__main__":
    sys.exit(main())
