#!/usr/bin/env python
"""
sync_docs.py -- regenerate every MEASURED number quoted in the hand-written
system docs from data/derived/graph.json, so documentation can never drift from
the data again.

This exists because the QC blind test found stale figures in A_HOW_TO_READ.md
(1,096 / 388 for 24V) that disagreed with INDEX_NETS.md (1,327 / 447). Hard-coded
counts in prose rot; generated counts cannot.

It rewrites only clearly delimited blocks:
  * A_HOW_TO_READ.md  -> the "Measured vocabulary" table in section 6
  * README.md         -> the verification table
  * 00_READ_ME_FIRST  -> the corpus statistics table
"""

from __future__ import annotations

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MD = os.path.join(ROOT, "md")
DER = os.path.join(ROOT, "data", "derived")

BEGIN = "<!-- AUTO-GENERATED:DO-NOT-EDIT-BY-HAND -->"
END = "<!-- /AUTO-GENERATED -->"


def load_graph():
    with io.open(os.path.join(DER, "graph.json"), encoding="utf-8") as f:
        return json.load(f)


def replace_block(text, name, new_body):
    """Replace the delimited block `name`, or append it if absent."""
    pat = re.compile(
        r"(?s)" + re.escape(BEGIN) + r"\s*name=" + re.escape(name) + r"\s*-->\n"
        r".*?" + re.escape(END))
    block = "%s name=%s -->\n%s\n%s" % (BEGIN, name, new_body.rstrip(), END)
    if pat.search(text):
        return pat.sub(lambda m: block, text)
    return text.rstrip() + "\n\n" + block + "\n"


def stats(g):
    s = g["stats"]
    n_sheets = len(g["sheets"])
    n_docs = len(g["documents"])
    labels = sum(sh["counts"]["lines"] for sh in g["sheets"])
    return {
        "sheets": n_sheets,
        "documents": n_docs,
        "labels": labels,
        "xrefs": s["xref_edges"],
        "unresolved": s["xref_unresolved"],
        "devices": s["devices"],
        "device_occ": s["device_occurrences"],
        "nets": s["nets"],
        "net_occ": s["net_occurrences"],
        "terminals": s["terminals"],
    }


def net_table(g, limit=None):
    MEANING = {
        "24V": "+24 V DC control supply",
        "0V": "0 V reference / DC return",
        "L1": "mains phase L1",
        "L2": "mains phase L2",
        "L3": "mains phase L3",
        "PE": "protective earth",
        "N": "mains neutral",
        "L24": "24 V lamp supply",
        "L230": "230 V phase",
        "M24+": "24 V motor / signal rail",
        "M501": "motor / drive potential",
    }
    nets = sorted(g["nets"], key=lambda n: -n["occurrences"])
    if limit:
        nets = nets[:limit]
    rows = ["| Potential | Occurrences | Sheets | Meaning |",
            "|---|---:|---:|---|"]
    for n in nets:
        rows.append("| `%s` | %d | %d | %s |"
                    % (n["net"], n["occurrences"], n["sheet_count"],
                       MEANING.get(n["net"], "—")))
    return "\n".join(rows)


def corpus_table(g):
    st = stats(g)
    rows = ["| Quantity | Value |", "|---|---:|",
            "| Sheets | %d |" % st["sheets"],
            "| Documents | %d |" % st["documents"],
            "| Text labels extracted | %d |" % st["labels"],
            "| Cross-references | %d (%d unresolved) |" % (st["xrefs"], st["unresolved"]),
            "| Distinct device designators | %d (%d occurrences) |"
            % (st["devices"], st["device_occ"]),
            "| Distinct potentials | %d (%d occurrences) |"
            % (st["nets"], st["net_occ"]),
            "| Distinct terminals | %d |" % st["terminals"]]
    return "\n".join(rows)


def doc_table(g):
    rows = ["| Document | Sheets | Document code | Created |", "|---|---:|---|---|"]
    for k in ["+FB", "+Ax", "+BA_Cx_DA", "+EA", "+FA", "+Jx"]:
        d = g["documents"].get(k)
        if not d:
            continue
        rows.append("| `%s` | %d | `%s` | %s |"
                    % (k, d["sheets"], d.get("document_code") or "?",
                       d.get("created_date") or "?"))
    return "\n".join(rows)


def main():
    g = load_graph()
    changed = []

    # ---- A_HOW_TO_READ.md : section 6 measured vocabulary ----
    p = os.path.join(MD, "01_SYSTEM", "A_HOW_TO_READ.md")
    t = io.open(p, encoding="utf-8").read()
    new = replace_block(t, "A-section6-nets", net_table(g, limit=12))
    if new != t:
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        changed.append("A_HOW_TO_READ.md")

    # ---- 00_READ_ME_FIRST.md : corpus statistics ----
    p = os.path.join(MD, "00_READ_ME_FIRST.md")
    t = io.open(p, encoding="utf-8").read()
    new = replace_block(t, "corpus-stats", corpus_table(g))
    if new != t:
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        changed.append("00_READ_ME_FIRST.md")

    # ---- README.md : corpus statistics ----
    p = os.path.join(MD, "..", "README.md")
    t = io.open(p, encoding="utf-8").read()
    new = replace_block(t, "corpus-stats", corpus_table(g))
    if new != t:
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        changed.append("README.md")

    st = stats(g)
    print("measured: %d sheets, %d labels, %d xrefs, %d devices, %d nets"
          % (st["sheets"], st["labels"], st["xrefs"], st["devices"], st["nets"]))
    print("updated:", ", ".join(changed) if changed else "nothing (already in sync)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
