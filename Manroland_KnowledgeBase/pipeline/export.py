#!/usr/bin/env python
"""
export.py -- emit machine-readable companions to the Markdown knowledge base,
for agents and RAG pipelines that prefer structured data over prose.

Outputs in md/ + data/exports/
  data/exports/sheets.jsonl     one JSON object per sheet (RAG-friendly chunks)
  data/exports/chunks.jsonl     finer chunks: per sheet section, with metadata
  data/exports/devices.jsonl    one object per device designator
  data/exports/nets.jsonl       one object per potential
  md/03_INDEX/CATALOG.md        compact human/agent-facing catalog
"""

from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from schema import DOCUMENTS  # noqa: E402

ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "data", "raw")
DER = os.path.join(ROOT, "data", "derived")
EXP = os.path.join(ROOT, "data", "exports")
MD = os.path.join(ROOT, "md")

DIR = {d: d.lstrip("+") for (_f, d, _c) in DOCUMENTS}
ORDER = ["+FB", "+Ax", "+BA_Cx_DA", "+EA", "+FA", "+Jx"]


def load_raw():
    out = {}
    for dockey in ORDER:
        sub = os.path.join(RAW, DIR[dockey])
        if not os.path.isdir(sub):
            continue
        recs = []
        for fn in sorted(os.listdir(sub)):
            if fn.endswith(".json"):
                with open(os.path.join(sub, fn), encoding="utf-8") as f:
                    recs.append(json.load(f))
        recs.sort(key=lambda r: r["sheet"])
        out[dockey] = recs
    return out


def main():
    os.makedirs(EXP, exist_ok=True)
    with open(os.path.join(DER, "graph.json"), encoding="utf-8") as f:
        graph = json.load(f)

    by_id = {s["id"]: s for s in graph["sheets"]}
    xref_in = {}
    for e in graph["edges"]:
        if e["type"] == "xref":
            xref_in.setdefault(e["to"], []).append(e)

    raw = load_raw()
    n_sheets = 0
    chunk_counts = [0]

    sheets_f = open(os.path.join(EXP, "sheets.jsonl"), "w", encoding="utf-8")
    chunks_f = open(os.path.join(EXP, "chunks.jsonl"), "w", encoding="utf-8")

    for dockey, recs in raw.items():
        for r in recs:
            sid = "%s#%d" % (dockey, r["sheet"])
            tb = r["title_block"]
            inc = xref_in.get(sid, [])
            base = {
                "id": sid,
                "doc": dockey,
                "sheet": r["sheet"],
                "sheet_total": r.get("sheet_total"),
                "document_code": tb.get("document_code"),
                "section_de": tb.get("section_title_de"),
                "section_en": tb.get("section_title_en"),
                "machine_type": tb.get("machine_type"),
                "serie": tb.get("serie"),
                "created": tb.get("created_date"),
                "replaces": tb.get("replaces"),
                "columns_used": sorted({l["col"] for l in r["lines"]}),
                "path_numbers": r.get("path_numbers") or [],
                "md": "../md/02_SHEETS/%s/SHEET_%04d.md" % (DIR[dockey], r["sheet"]),
                "image": "images/%s/%s_%04d.png" % (dockey, DIR[dockey], r["sheet"]),
                "counts": r["counts"],
            }

            # ---- per-sheet record ----
            sheets_f.write(json.dumps({
                **base,
                "devices": [d.get("tag") for d in r.get("devtag") or []],
                "devrefs": [d.get("raw") for d in r.get("devref") or []],
                "nets": sorted({n.get("net") or n.get("raw")
                                for n in r.get("nets") or []}),
                "xrefs_out": [
                    {"to": "/%d.%s" % (x["to_sheet"], x["to_column"]),
                     "path": x["path"], "target": x["target"],
                     "from_column": x["col"]}
                    for x in r.get("xrefs_out") or []
                ],
                "xrefs_in": [
                    {"from": e["from"], "from_column": e["from_column"],
                     "path": e.get("path"), "target": e.get("target")}
                    for e in inc
                ],
                "labels": [{"t": l["text"], "k": l["kind"], "c": l["col"],
                            "x": round(l["x0"], 1), "y": round(l["y0"], 1),
                            "rot": l["rot"]} for l in r["lines"]],
            }, ensure_ascii=False) + "\n")
            n_sheets += 1

            # ---- chunked records (one chunk per logical section) ----
            emitted = [0]

            def emit(kind, text, extra=None):
                if not text or not text.strip():
                    return
                rec = {**base, "chunk_type": kind, "text": text.strip()}
                if extra:
                    rec.update(extra)
                chunks_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                emitted[0] += 1
                chunk_counts[0] += 1

            emit("header",
                 "Sheet %s #%d of %s — %s / %s. Machine R700, series %s, "
                 "document code %s, created %s."
                 % (dockey, r["sheet"], r.get("sheet_total") or "?",
                    tb.get("section_title_de") or "?", tb.get("section_title_en") or "?",
                    tb.get("serie") or "?", tb.get("document_code") or "?",
                    tb.get("created_date") or "?"))

            if r.get("xrefs_out"):
                emit("cross_references",
                     "; ".join(
                         "wire continues to sheet %d column %s (%s)%s"
                         % (x["to_sheet"], x["to_column"],
                            x.get("target") or "no destination text",
                            (", line #%d" % x["path"]) if x.get("path") else "")
                         for x in r["xrefs_out"]),
                     {"count": len(r["xrefs_out"])})

            if inc:
                emit("incoming_references",
                     "; ".join(
                         "sheet %s column %s points here (%s)"
                         % (e["from"], e["from_column"],
                            e.get("target") or "no destination text")
                         for e in inc),
                     {"count": len(inc)})

            devs = r.get("devtag") or []
            if devs:
                emit("devices",
                     "Devices on this sheet: " + ", ".join(
                         "%s (class %s%s)" % (d.get("tag"), d.get("cls"),
                                              (", column " + d["col"]) if d.get("col") else "")
                         for d in devs),
                     {"count": len(devs)})

            nets = r.get("nets") or []
            if nets:
                agg = {}
                for n in nets:
                    k = n.get("net") or n.get("raw")
                    agg[k] = agg.get(k, 0) + 1
                emit("potentials",
                     "Potentials on this sheet: " + ", ".join(
                         "%s x%d" % (k, v) for k, v in sorted(agg.items())),
                     {"count": len(nets)})

            if r.get("annotations"):
                emit("annotations",
                     "Wire-end annotations: " + " | ".join(
                         a["text"] for a in r["annotations"] if a["kinds"]),
                     {"count": len(r["annotations"])})

            # full label inventory as one chunk (this is the ground truth)
            emit("labels_full",
                 "Complete label inventory in reading order: " + " | ".join(
                     "%s[%s] %s" % (l["col"], l["kind"], l["text"])
                     for l in sorted(r["lines"],
                                     key=lambda l: (l["col_idx"],
                                                    round(l["y0"], 1), l["x0"]))),
                 {"count": len(r["lines"])})

            tfile = os.path.join(DER, "tables",
                                 "%s_%04d.json" % (dockey.lstrip("+"), r["sheet"]))
            if os.path.exists(tfile):
                with open(tfile, encoding="utf-8") as tf:
                    tabs = json.load(tf).get("tables") or []
                for ti, t in enumerate(tabs, 1):
                    rows_txt = "\n".join(
                        " | ".join(c for c in row["cells"]) for row in t["rows"])
                    emit("table", "Table %d (%d rows):\n%s"
                         % (ti, t["n_rows"], rows_txt))

    sheets_f.close()
    chunks_f.close()

    with open(os.path.join(EXP, "devices.jsonl"), "w", encoding="utf-8") as f:
        for d in graph["devices"]:
            f.write(json.dumps({
                "tag": d["tag"], "class": d.get("cls"),
                "occurrences": d["occurrences"],
                "sheets": sorted(d["sheets"]),
                "columns": d["columns"],
            }, ensure_ascii=False) + "\n")

    with open(os.path.join(EXP, "nets.jsonl"), "w", encoding="utf-8") as f:
        for n in graph["nets"]:
            f.write(json.dumps({
                "net": n["net"], "occurrences": n["occurrences"],
                "sheets": sorted(n["sheets"]),
            }, ensure_ascii=False) + "\n")

    # ---- catalog ----
    L = ["# Catalog (machine-readable index summary)", ""]
    L.append("Compact overview for an agent that needs the shape of the corpus "
             "before searching. The full data lives in `data/exports/*.jsonl`.")
    L.append("")
    L.append("| Doc | Sheets | Section code | Section DE | Section EN | Labels | Xrefs out |")
    L.append("|---|---:|---|---|---|---:|---:|")
    for dockey, recs in raw.items():
        # group by section
        cur = None
        for r in recs:
            tb = r["title_block"]
            key = (tb.get("section_title_de"), tb.get("section_title_en"))
            if cur is None:
                cur = {"k": key, "n": 0, "labels": 0, "xrefs": 0, "from": r["sheet"]}
            if cur["k"] != key:
                L.append("| `%s` | %d–%d | | %s | %s | %d | %d |"
                         % (dockey, cur["from"], cur["from"] + cur["n"] - 1,
                            cur["k"][0] or "—", cur["k"][1] or "—",
                            cur["labels"], cur["xrefs"]))
                cur = {"k": key, "n": 0, "labels": 0, "xrefs": 0, "from": r["sheet"]}
            cur["n"] += 1
            cur["labels"] += r["counts"]["lines"]
            cur["xrefs"] += len(r.get("xrefs_out") or [])
        if cur:
            L.append("| `%s` | %d–%d | | %s | %s | %d | %d |"
                     % (dockey, cur["from"], cur["from"] + cur["n"] - 1,
                        cur["k"][0] or "—", cur["k"][1] or "—",
                        cur["labels"], cur["xrefs"]))
    L.append("")
    with open(os.path.join(MD, "03_INDEX", "CATALOG.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))

    print("sheets.jsonl: %d records" % n_sheets)
    print("chunks.jsonl: %d chunks" % chunk_counts[0])
    print("devices.jsonl: %d" % len(graph["devices"]))
    print("nets.jsonl: %d" % len(graph["nets"]))
    print("CATALOG.md written")


if __name__ == "__main__":
    main()
