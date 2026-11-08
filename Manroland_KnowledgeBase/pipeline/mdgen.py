#!/usr/bin/env python
"""
mdgen.py -- Stage 3: turn the extraction + graph into a Markdown knowledge base
optimised for LLM / NotebookLLM / agent retrieval.

Layout produced
---------------
md/
  00_READ_ME_FIRST.md
  00_QUERY_PLAYBOOK.md
  01_SYSTEM/            (hand-written reference docs; not touched here)
  02_SHEETS/<doc>/SHEET_NNNN.md   one self-contained file per sheet
  02_SHEETS/<doc>/_TOC.md         per-document sheet list
  02_SHEETS/_MASTER_TOC.md
  03_INDEX/INDEX_SECTIONS.md
  03_INDEX/INDEX_SHEETS.md
  03_INDEX/INDEX_DEVICES.md
  03_INDEX/DEVICES/<class>.md
  03_INDEX/INDEX_NETS.md

Design rules that matter for retrieval quality
----------------------------------------------
1. Every sheet file is SELF-CONTAINED: identity, section, document, all labels,
   all cross references (resolved), the image, and the navigation neighbours.
2. Exact strings from the drawing are preserved verbatim, so an agent can do
   literal matching as well as semantic retrieval.
3. Every cross reference is expressed twice: as the printed token (`/17.D`)
   AND as a resolved link with the target's section title, so the reader never
   has to guess what /17.D means.
4. YAML front matter gives chunkers reliable metadata to attach to fragments.
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
from grammar import DEVICE_CLASSES  # noqa: E402
from schema import DOCUMENTS  # noqa: E402

ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "data", "raw")
DER = os.path.join(ROOT, "data", "derived")
MD = os.path.join(ROOT, "md")

DOC_DIR = {d: d.lstrip("+") for (_f, d, _c) in DOCUMENTS}

# Friendly names for the machine sections
DOC_FRIENDLY = {
    "+FB": "Delivery / Coating module",
    "+Ax": "Central control console",
    "+BA_Cx_DA": "Printing units / main switch cabinet",
    "+EA": "Printing unit",
    "+FA": "Delivery",
    "+Jx": "1st printing module + feed register",
}

KIND_ORDER = ["xref", "path", "pinpair", "devtag", "devref", "net",
              "xsection", "colour", "text", "numeric", "placeholder", "other"]

KIND_LABEL = {
    "xref": "cross-reference",
    "path": "path no.",
    "pinpair": "pin pair",
    "devtag": "device tag",
    "devref": "device ref",
    "net": "potential",
    "xsection": "cross-section",
    "colour": "wire colour",
    "text": "text",
    "numeric": "number",
    "placeholder": "not fitted",
    "other": "other",
}


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------
def esc(s):
    """Escape text for a Markdown table cell."""
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def code(s):
    """Inline code span that survives a table cell."""
    if s is None or s == "":
        return ""
    s = str(s).replace("|", "\\|")
    if "`" in s:
        s = s.replace("`", "'")
    return "`%s`" % s


def table(headers, rows, align=None):
    if not rows:
        return "_none_\n"
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out) + "\n"


def load_raw(dockey):
    sub = os.path.join(RAW, DOC_DIR[dockey])
    recs = []
    if not os.path.isdir(sub):
        return recs
    for fn in sorted(os.listdir(sub)):
        if fn.endswith(".json"):
            with open(os.path.join(sub, fn), encoding="utf-8") as f:
                recs.append(json.load(f))
    recs.sort(key=lambda r: r["sheet"])
    return recs


def sheet_link(dockey, sheet, text=None):
    """Link to a sheet file from another sheet file (same directory)."""
    return "[%s](SHEET_%04d.md)" % (text or ("%s sheet %d" % (dockey, sheet)),
                                    sheet)


def sheet_link_cross(dockey, sheet, text=None):
    """Link to a sheet file from a sheet in a *different* document dir."""
    return "[%s](../%s/SHEET_%04d.md)" % (
        text or ("%s sheet %d" % (dockey, sheet)), DOC_DIR[dockey], sheet)


def sheet_link_from_index(dockey, sheet, text=None):
    return "[%s](../02_SHEETS/%s/SHEET_%04d.md)" % (
        text or ("%s sheet %d" % (dockey, sheet)), DOC_DIR[dockey], sheet)


def img_rel(dockey, sheet):
    """Image path as seen from md/02_SHEETS/<doc>/SHEET_NNNN.md"""
    return "../../../images/%s/%s_%04d.png" % (dockey, DOC_DIR[dockey], sheet)


# ---------------------------------------------------------------------------
# section index: consecutive sheets sharing a section title
# ---------------------------------------------------------------------------
def build_sections(sheets_by_doc):
    out = {}
    for dockey, recs in sheets_by_doc.items():
        spans = []
        cur = None
        for r in recs:
            tb = r["title_block"]
            de = (tb.get("section_title_de") or "").strip()
            en = (tb.get("section_title_en") or "").strip()
            key = (de, en)
            if cur and cur["key"] == key:
                cur["to"] = r["sheet"]
            else:
                cur = {"key": key, "de": de, "en": en,
                       "from": r["sheet"], "to": r["sheet"]}
                spans.append(cur)
        out[dockey] = spans
    return out


def topic_of(de, en):
    from schema import SECTION_TOPICS
    blob = ("%s %s" % (de or "", en or "")).upper()
    for pat, label, code_ in SECTION_TOPICS:
        if pat.upper() in blob:
            return code_, label
    return "CIRCUIT", "Circuit diagram"


# ---------------------------------------------------------------------------
# per-sheet markdown
# ---------------------------------------------------------------------------
def sheet_md(rec, graph, ctx):
    doc = rec["doc"]
    sh = rec["sheet"]
    tb = rec["title_block"]
    de = (tb.get("section_title_de") or "").strip()
    en = (tb.get("section_title_en") or "").strip()
    topic_code, topic_label = topic_of(de, en)

    lines = []
    A = lines.append

    # ---------------- front matter ----------------
    A("---")
    A('doc: "%s"' % doc)
    A("sheet: %d" % sh)
    A("sheet_total: %s" % (rec.get("sheet_total") or tb.get("sheet_total") or ""))
    A('document_code: "%s"' % (tb.get("document_code") or ""))
    A('section_de: "%s"' % de.replace('"', "'"))
    A('section_en: "%s"' % en.replace('"', "'"))
    A('section_code: "%s"' % topic_code)
    A('machine_type: "%s"' % (tb.get("machine_type") or ""))
    A('serie: "%s"' % (tb.get("serie") or ""))
    A('created: "%s"' % (tb.get("created_date") or ""))
    A('image: "%s"' % img_rel(doc, sh))
    A('columns: "%s"' % "-".join(rec.get("cols_used") or []))
    A("---")
    A("")

    # ---------------- title ----------------
    A("# %s — Sheet %d of %s%s" % (
        doc, sh, rec.get("sheet_total") or "?" ,
        (" — " + de) if de else ""))
    A("")
    if en:
        A("**%s**" % en)
        A("")

    A("> Part of the manroland **R700** printing press IEC/UL circuit diagrams.")
    A("> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).")
    A("> Document `%s` covers the **%s** machine section."
      % (doc, DOC_FRIENDLY.get(doc, doc)))
    A("")

    # ---------------- at a glance ----------------
    A("## At a glance")
    A("")
    rows = [
        ["Document", code(doc) + "  (" + (tb.get("document_code") or "?") + ")"],
        ["Sheet", "**%d** of %s" % (sh, rec.get("sheet_total") or "?")],
        ["Section (DE)", esc(de) or "—"],
        ["Section (EN)", esc(en) or "—"],
        ["Section type", "%s — %s" % (topic_code, topic_label)],
        ["Machine type", code(tb.get("machine_type") or "?")],
        ["Series", code(tb.get("serie") or "?")],
        ["Created", esc(tb.get("created_date") or "?")],
        ["Replaces", code(tb.get("replaces")) if tb.get("replaces") else "—"],
        ["Columns used", ", ".join(rec.get("cols_used") or []) or "—"],
        ["Path numbers", ", ".join(str(p) for p in (rec.get("path_numbers") or [])) or "—"],
        ["Labels on sheet", str(rec["counts"]["lines"])],
        ["Cross-refs out", str(len(rec.get("xrefs_out") or []))],
        ["Cross-refs in", str(ctx["xref_in"].get("%s#%d" % (doc, sh), 0))],
    ]
    A(table(["Field", "Value"], rows))

    # ---------------- navigation ----------------
    nav = []
    if ctx["prev"]:
        p = ctx["prev"]
        lnk = (sheet_link if p["doc"] == doc else sheet_link_cross)
        nav.append("**Previous:** " + lnk(p["doc"], p["sheet"],
                   "%s sheet %d" % (p["doc"], p["sheet"])))
    if ctx["next"]:
        n = ctx["next"]
        lnk = (sheet_link if n["doc"] == doc else sheet_link_cross)
        nav.append("**Next:** " + lnk(n["doc"], n["sheet"],
                   "%s sheet %d" % (n["doc"], n["sheet"])))
    nav.append("**Document TOC:** [_TOC.md](_TOC.md)  (%s)" % doc)
    nav.append("**Master TOC:** [all sheets](../_MASTER_TOC.md)")
    A(" · ".join(nav))
    A("")

    # ---------------- image ----------------
    A("## Sheet image (300 DPI, exact vector render)")
    A("")
    A("![%s sheet %d](%s)" % (doc, sh, img_rel(doc, sh)))
    A("")
    A("_Rendered directly from the PDF vector layer at 300 DPI (1-bit), "
      "no OCR and no resampling. Use it to confirm anything ambiguous in the "
      "text below._")
    A("")

    # ---------------- cross references out ----------------
    A("## Cross-references on this sheet")
    A("")
    A("Each entry is a wire leaving this sheet. The printed token is "
      "`/sheet.column`; the link resolves to that sheet inside the same "
      "document.")
    A("")
    if rec.get("xrefs_out"):
        rows = []
        for x in rec["xrefs_out"]:
            tgt_id = "%s#%d" % (doc, x["to_sheet"])
            tgt = ctx["by_id"].get(tgt_id)
            tgt_title = ""
            if tgt:
                tgt_title = esc(tgt.get("title_de") or tgt.get("section_en") or "")
            rows.append([
                code("/%d.%s" % (x["to_sheet"], x["to_column"])),
                sheet_link(doc, x["to_sheet"]),
                x["to_column"],
                code("#%d" % x["path"]) if x["path"] else "—",
                esc(x.get("target") or "—"),
                tgt_title or "—",
                x["col"],
            ])
        A(table(["Ref", "Target sheet", "Col", "Path", "Destination on target",
                 "Target section", "From col"], rows))
    else:
        A("_No outgoing cross-references on this sheet._")
        A("")

    # ---------------- cross references in ----------------
    inc = ctx["xref_in_list"].get("%s#%d" % (doc, sh), [])
    if inc:
        A("### Incoming references (sheets that point here)")
        A("")
        A("Every other sheet that sends a wire to this one. `Back-ref` is the "
          "token printed on *that* sheet; `Path` is its line number.")
        A("")
        agg = defaultdict(lambda: {"n": 0, "paths": set(), "targets": set(),
                                   "cols": set()})
        for e in inc:
            key = e["from"]
            a = agg[key]
            a["n"] += 1
            if e.get("path"):
                a["paths"].add(e["path"])
            if e.get("target"):
                a["targets"].add(e["target"])
            a["cols"].add(e.get("from_column"))
        rows = []
        for frm, a in sorted(agg.items(),
                             key=lambda kv: (kv[0].split("#")[0],
                                             int(kv[0].split("#")[1]))):
            fdoc, fsheet = frm.rsplit("#", 1)
            lnk = (sheet_link if fdoc == doc else sheet_link_cross)
            cols = sorted(c for c in a["cols"] if c)
            rows.append([
                lnk(fdoc, int(fsheet), frm),
                ", ".join(cols),
                ", ".join(code("/%s.%s" % (fsheet, c)) for c in cols),
                ", ".join(code("#%d" % p) for p in sorted(a["paths"])) or "—",
                str(a["n"]),
                esc("; ".join(sorted(a["targets"]))[:160]) or "—",
            ])
        A(table(["From sheet", "Cols", "Back-ref", "Path", "Refs",
                 "What continues there"], rows))
        A("")

    # ---------------- devices ----------------
    A("## Devices on this sheet")
    A("")
    devs = rec.get("devtag") or []
    refs = rec.get("devref") or []
    if devs or refs:
        rows = []
        for d in devs:
            cls = d.get("cls") or ""
            rows.append([
                code(d.get("tag")),
                cls,
                esc(DEVICE_CLASSES.get(cls, "")),
                d.get("col"),
                d.get("sub") or "—",
                d.get("pin") or "—",
                d.get("sign") or "—",
            ])
        for d in refs:
            rows.append([
                code(d.get("raw")),
                "—",
                "cross-device reference",
                d.get("col"),
                "—",
                d.get("terminal") or "—",
                "—",
            ])
        A(table(["Tag", "Class", "Class meaning (IEC)", "Col", "Sub", "Terminal",
                 "Sign"], rows))
    else:
        A("_No device designators on this sheet._")
        A("")

    # ---------------- potentials ----------------
    A("## Potentials / nets")
    A("")
    nets = rec.get("nets") or []
    if nets:
        agg = defaultdict(lambda: {"n": 0, "cols": Counter(), "devices": Counter(),
                                   "terms": Counter()})
        for n in nets:
            k = n.get("net") or n.get("raw")
            a = agg[k]
            a["n"] += 1
            a["cols"][n.get("col")] += 1
            for dv in (n.get("devices") or []):
                a["devices"][dv] += 1
            if n.get("terminal"):
                a["terms"][n["terminal"]] += 1
        rows = []
        for k, a in sorted(agg.items()):
            rows.append([
                code(k), a["n"],
                ", ".join(sorted(c for c in a["cols"] if c)),
                ", ".join(code(d) for d in sorted(a["devices"])) or "—",
                ", ".join(code(t) for t in sorted(a["terms"])) or "—",
            ])
        A(table(["Potential", "Count", "Columns", "Attached devices", "Terminals"],
                rows))
        A("")
        A("A potential such as `L24+/4` or `M24+` is a named supply/return rail; "
          "every place it appears on this sheet is electrically common.")
        A("")
    else:
        A("_No named potentials on this sheet._")
        A("")

    # ---------------- wire data ----------------
    xs = rec.get("xsections") or []
    cols = rec.get("colours") or []
    if xs or cols:
        A("## Conductor data")
        A("")
        A("Each label annotates **the wire beside it**, not the sheet. These "
          "summaries are inventories of what is printed; they are not a "
          "per-wire map. For a specific conductor, read the label that sits on "
          "that wire (see the label inventory below, or the sheet image).")
        A("")
        if xs:
            agg = Counter(x["mm2"] for x in xs)
            A("**Cross-section labels printed on this sheet:** " +
              ", ".join("%s mm² (×%d)" % (("%g" % k), v)
                        for k, v in sorted(agg.items())))
            A("")
        if cols:
            agg = Counter((c.get("code"), c.get("de"), c.get("en")) for c in cols)
            A("**Wire-colour labels printed on this sheet:** " +
              ", ".join("%s = %s / %s (×%d)" % (k[0], k[1], k[2], v)
                        for k, v in sorted(agg.items())))
            A("")
        # Only pair section+colour when they sit in the SAME PDF text block,
        # which is how the exporter groups one wire's two specification labels.
        # Pairing by sheet alone would double-count, so the numbers here are
        # explicitly "blocks that contain both".
        pairs = Counter()
        for a in rec.get("annotations") or []:
            kinds = [l["k"] for l in a["lines"]]
            if "xsection" in kinds and "colour" in kinds:
                for l in a["lines"]:
                    if l["k"] != "xsection":
                        continue
                    c = next((x["p"]["de"] for x in a["lines"]
                              if x["k"] == "colour"), None)
                    if c:
                        pairs[(l["p"]["mm2"], c)] += 1
        if pairs:
            A("**Cross-section + colour appearing together in one annotation "
              "block:**")
            A("")
            A(table(["Cross-section", "Colour (DE)", "Colour (EN)",
                     "Blocks containing both"],
                    [[("%g mm²" % k[0]), k[1],
                      next((l["p"]["en"] for a in rec["annotations"]
                            for l in a["lines"] if l["k"] == "colour"
                            and l["p"]["de"] == k[1]), "—"), v]
                     for k, v in sorted(pairs.items())]))
            A("")
            A("_This counts annotation blocks that carry both labels. It can be "
              "lower than the number of individual labels above, because a "
              "block may hold two cross-section labels or two colour labels._")
            A("")

    # ---------------- wire-end annotations ----------------
    annos = [a for a in (rec.get("annotations") or []) if a["kinds"]]
    if annos:
        A("## Wire-end annotations (grouped as printed)")
        A("")
        A("A wire that continues elsewhere is annotated with a small cluster: "
          "the destination description, the path/line number `#NN`, and the "
          "`/sheet.column` cross reference. Each row below is one such cluster "
          "exactly as it is grouped on the drawing.")
        A("")
        rows = []
        for a in annos:
            xr = ", ".join(code("/%d.%s" % (x["sheet"], x["column"]))
                           for x in a["xref"]) or "—"
            pth = ", ".join(code("#%d" % p) for p in a["paths"]) or "—"
            rest = " ".join(l["t"] for l in a["lines"]
                            if l["k"] not in ("xref", "path"))
            rows.append([a["col"], "%.1f" % a["bbox"][1], pth, xr,
                         code(rest) if rest else "—"])
        A(table(["Col", "Y", "Path", "Cross-ref", "Text on the wire"], rows))
        A("")

    # ---------------- reconstructed tables ----------------
    if ctx.get("tables"):
        A("## Reconstructed tables")
        A("")
        A("This sheet carries tabular content (pin map / terminal assignment / "
          "index). The grid below was rebuilt from the drawing's own rule lines, "
          "so each row is exactly one physical row of the table.")
        A("")
        for ti, t in enumerate(ctx["tables"], 1):
            rows = t["rows"]
            # Pick the header row: prefer the row that names the printed column
            # labels. Rows above it hold the device title (e.g. -A356/13).
            HEADER_WORDS = ("PIN", "BYTE.BIT", "STROMPFAD", "STROM", "Option",
                            "BS", "No:", "NR", "TAG", "NAME", "Type",
                            "Torque", "UL", "IEC", "Reference")
            hdr_idx = None
            for i, r in enumerate(rows[:8]):
                joined = " ".join(c for c in r["cells"] if c)
                if sum(1 for w in HEADER_WORDS if w in joined) >= 2:
                    hdr_idx = i
                    break
            if hdr_idx is None:
                for i, r in enumerate(rows[:4]):
                    if sum(1 for c in r["cells"] if c) >= 2:
                        hdr_idx = i
                        break
            if hdr_idx is not None:
                hdr = [c for c in rows[hdr_idx]["cells"]]
                body = rows[hdr_idx + 1:]
            else:
                hdr = ["C%d" % (i + 1) for i in range(len(rows[0]["cells"]))]
                body = rows
            # Any populated row ABOVE the header names the table's subject,
            # e.g. "-A356/13" / "-A356/14" on pin maps, or "X020 / +A497" on a
            # terminal strip.  Surface it explicitly: two side-by-side tables
            # with identical pin labels are otherwise easy to confuse, and that
            # was an observed real misreading.
            title = None
            if hdr_idx is not None:
                head_rows = rows[:hdr_idx]
                parts = []
                for hr in head_rows:
                    for c in hr["cells"]:
                        if c and c not in parts:
                            parts.append(c)
                if parts:
                    title = " ".join(parts)
            ncol = max(len(r["cells"]) for r in rows)
            # A header cell may legitimately be blank: on a pin map the "PIN"
            # column spans the three sub-columns A/B/C, so one cell is labelled
            # and the next is continuation.  Show blanks as blank, not as "—",
            # so the reader can see the span rather than an unknown value.
            hdr = (hdr + [""] * ncol)[:ncol]
            trows = []
            for r in body:
                cells = (r["cells"] + [""] * ncol)[:ncol]
                if not any(cells):
                    continue
                trows.append([code(c) if c else "" for c in cells])
            subject = (" — **%s**" % esc(title)) if title else ""
            A("### Table %d — %d data rows × %d columns (at x=%s, y=%s)%s"
              % (ti, len(trows), ncol, t["bbox"][0], t["bbox"][1], subject))
            A("")
            A(table([esc(h) for h in hdr], trows))
            A("")

    # ---------------- order codes / no-part markers ----------------
    ocs = rec.get("ordercodes") or []
    nps = rec.get("noparts") or []
    if ocs or nps:
        A("## Device order codes printed on this sheet")
        A("")
        A("> **These are NOT device part numbers and must not be attributed to "
          "a single device.** They are order/manufacturing codes that sit inside "
          "the same annotation cluster as a device, with no printed label and no "
          "leader line binding them to one item. Measured across the whole set: "
          "such codes appear on **8 of 1,351 sheets** (see "
          "`01_SYSTEM/A_HOW_TO_READ.md` §8.1).")
        A("")
        rows = []
        for o in ocs:
            rows.append([code(o.get("code")), o.get("col"), "%.1f" % o["bbox"][1], "order code"])
        for o in nps:
            rows.append([code(o.get("marker")), o.get("col"), "%.1f" % o["bbox"][1],
                         "no orderable part (marker)"])
        A(table(["Token", "Col", "Y (pt)", "What it is"], rows))
        A("")

    # ---------------- notes ----------------
    texts = [t for t in (rec.get("texts") or [])]
    if texts:
        A("## Notes and free text on this sheet")
        A("")
        seen = set()
        rows = []
        for t in texts:
            key = (t.get("text"), t.get("col"))
            if key in seen:
                continue
            seen.add(key)
            rows.append([code(t.get("text")), t.get("col"),
                         "%g" % t["bbox"][1]])
        A(table(["Text", "Col", "Y (pt)"], rows))

    # ---------------- complete label inventory ----------------
    A("## Complete label inventory (exact text from the drawing)")
    A("")
    A("Every text object inside the drawing area of this sheet, in DIN reading "
      "order (column A→H, then top→bottom). This is the authoritative list: if "
      "a string is not here it is not printed on this sheet.")
    A("")
    ordered = sorted(rec["lines"], key=lambda l: (l["col_idx"], round(l["y0"], 1),
                                                  l["x0"]))
    rows = []
    for l in ordered:
        rows.append([
            l["col"],
            "%.1f" % l["y0"],
            "%.1f" % l["x0"],
            "↕" if l["rot"] else "→",
            KIND_LABEL.get(l["kind"], l["kind"]),
            code(l["text"]),
        ])
    A(table(["Col", "Y", "X", "Dir", "Type", "Text"], rows))

    # ---------------- reading order block ----------------
    A("## Reading-order text block")
    A("")
    A("The same content as a plain block, grouped by DIN column — convenient to "
      "paste or to match against a visual description.")
    A("")
    A("```text")
    bycol = defaultdict(list)
    for l in ordered:
        bycol[l["col"]].append(l)
    for c in "ABCDEFGH":
        if c not in bycol:
            continue
        A("=== Column %s ===" % c)
        for l in bycol[c]:
            A("%6.1f %6.1f  %-12s %s"
              % (l["y0"], l["x0"], l["kind"], l["text"]))
    A("```")
    A("")

    A("---")
    A("_Generated from the PDF vector text layer; no OCR. "
      "Source: `%s`, sheet %d._" % (rec.get("doc_title_code") or doc, sh))
    A("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# document TOC
# ---------------------------------------------------------------------------
def doc_toc_md(dockey, recs, sections):
    de_names = DOC_FRIENDLY.get(dockey, dockey)
    L = []
    A = L.append
    A("# %s — %s" % (dockey, de_names))
    A("")
    A("Document code: `%s`. %d sheets."
      % (recs[0]["title_block"].get("document_code") or "?", len(recs)))
    A("")
    A("## Sections")
    A("")
    rows = []
    for s in sections[dockey]:
        code_, label = topic_of(s["de"], s["en"])
        span = ("%d" % s["from"]) if s["from"] == s["to"] else \
               ("%d–%d" % (s["from"], s["to"]))
        first = next((r for r in recs if r["sheet"] == s["from"]), None)
        n = s["to"] - s["from"] + 1
        rows.append([esc(s["de"]) or "—", esc(s["en"]) or "—", code_,
                     span, str(n),
                     "[open](../%s/SHEET_%04d.md)" % (DOC_DIR[dockey], s["from"])])
    A(table(["Section (DE)", "Section (EN)", "Type", "Sheets", "Count", "Open"],
            rows))
    A("")
    A("## All sheets")
    A("")
    rows = []
    for r in recs:
        tb = r["title_block"]
        rows.append([
            str(r["sheet"]),
            "[SHEET_%04d](../%s/SHEET_%04d.md)" % (r["sheet"], DOC_DIR[dockey],
                                                   r["sheet"]),
            esc(tb.get("section_title_de") or "—"),
            esc(tb.get("section_title_en") or "—"),
            str(r["counts"]["lines"]),
            str(len(r.get("xrefs_out") or [])),
        ])
    A(table(["#", "Sheet", "Section DE", "Section EN", "Labels", "Xrefs"], rows))
    A("")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# indexes
# ---------------------------------------------------------------------------
def index_sections_md(sheets_by_doc, sections, by_id):
    A = ["# Index of sections", ""]
    A.append("Every drawing section in every document, with its sheet range. "
             "Use this to jump straight to the part of the machine you need.")
    A.append("")
    rows = []
    for dockey in sorted(sheets_by_doc):
        for s in sections[dockey]:
            code_, label = topic_of(s["de"], s["en"])
            span = ("%d" % s["from"]) if s["from"] == s["to"] else \
                   ("%d–%d" % (s["from"], s["to"]))
            n = s["to"] - s["from"] + 1
            rows.append([code(dockey), esc(s["de"]) or "—", esc(s["en"]) or "—",
                         code_, span, str(n),
                         "[open](../02_SHEETS/%s/SHEET_%04d.md)"
                         % (DOC_DIR[dockey], s["from"])])
    A.append(table(["Doc", "Section (DE)", "Section (EN)", "Type", "Sheets",
                    "Count", "Open"], rows))
    A.append("")
    return "\n".join(A)


def index_sheets_md(sheets_by_doc, by_id):
    A = ["# Index of all 1351 sheets", ""]
    A.append("Master table. `Labels` = number of text objects on the sheet, "
             "`Xrefs out` = number of wire continuations off the sheet.")
    A.append("")
    rows = []
    for dockey in sorted(sheets_by_doc):
        for r in sheets_by_doc[dockey]:
            tb = r["title_block"]
            rows.append([
                code(dockey), str(r["sheet"]),
                "[%d](../02_SHEETS/%s/SHEET_%04d.md)"
                % (r["sheet"], DOC_DIR[dockey], r["sheet"]),
                esc(tb.get("section_title_de") or "—"),
                esc(tb.get("section_title_en") or "—"),
                str(r["counts"]["lines"]),
                str(len(r.get("xrefs_out") or [])),
            ])
    A.append(table(["Doc", "#", "Sheet", "Section DE", "Section EN", "Labels",
                    "Xrefs out"], rows))
    A.append("")
    return "\n".join(A)


def index_devices_md(graph):
    devs = graph["devices"]
    A = ["# Index of devices", ""]
    A.append("Every device designator that appears anywhere in the six "
             "documents, with every sheet it appears on. Click a sheet to open "
             "it.")
    A.append("")
    by_class = defaultdict(list)
    for d in devs:
        by_class[(d.get("cls") or "?")].append(d)
    A.append("## Devices by class")
    A.append("")
    rows = []
    for cls in sorted(by_class):
        lst = by_class[cls]
        rows.append([code(cls), DEVICE_CLASSES.get(cls, "—"), str(len(lst)),
                     "[list](DEVICES/CLASS_%s.md)" % (cls if cls.isalnum() else "X")])
    A.append(table(["Class", "Meaning (IEC 81346 / DIN 40719)", "Count",
                    "List"], rows))
    A.append("")
    A.append("## All devices (A–Z)")
    A.append("")
    rows = []
    for d in devs:
        sheets = sorted(d["sheets"].items(),
                        key=lambda kv: (kv[0].split("#")[0], int(kv[0].split("#")[1])))
        loc = ", ".join(
            "[%s:%s](../02_SHEETS/%s/SHEET_%04d.md)"
            % (doc, sh, DOC_DIR[doc], int(sh))
            for doc, sh in [(s.split("#")[0], s.split("#")[1]) for s, _ in sheets])
        rows.append([code(d["tag"]), d.get("cls") or "—",
                     DEVICE_CLASSES.get(d.get("cls") or "", "—"),
                     str(d["occurrences"]), loc])
    A.append(table(["Tag", "Class", "Meaning", "Occurrences", "Sheets"], rows))
    A.append("")

    # per-class files
    out = {}
    for cls, lst in by_class.items():
        B = ["# Devices of class `%s` — %s" % (cls, DEVICE_CLASSES.get(cls, "?")), ""]
        B.append("%d distinct designators." % len(lst))
        B.append("")
        rows = []
        for d in lst:
            sheets = sorted(d["sheets"].items(),
                            key=lambda kv: (kv[0].split("#")[0],
                                            int(kv[0].split("#")[1])))
            loc = ", ".join(
                "[%s:%s](../../02_SHEETS/%s/SHEET_%04d.md)"
                % (doc, sh, DOC_DIR[doc], int(sh))
                for doc, sh in [(s.split("#")[0], s.split("#")[1]) for s, _ in sheets])
            rows.append([code(d["tag"]), str(d["occurrences"]), loc])
        B.append(table(["Tag", "Occurrences", "Sheets"], rows))
        B.append("")
        out[cls if cls.isalnum() else "X"] = "\n".join(B)
    return "\n".join(A), out


def index_nets_md(graph):
    nets = graph["nets"]
    A = ["# Index of potentials (nets)", ""]
    A.append("Named electrical potentials used across the drawings. A potential "
             "is electrically one node: every sheet that mentions it is "
             "connected.")
    A.append("")
    A.append("**Counting rule.** A sheet counts here if it prints the potential "
             "either as a standalone label (`24V`) *or* as the head of a "
             "dotted wire reference (`24V.X001:15`). Prose mentions such as "
             "`SPANNUNGSVERSORGUNG: 24V` or `(24V)` in a title or note are "
             "**not** counted, because they name a topic rather than a wire. "
             "A document that never prints the potential therefore legitimately "
             "shows **0** — that is a measured zero, not missing data.")
    A.append("")
    A.append(table(["Potential", "Occurrences", "Sheets"],
                   [[code(n["net"]), str(n["occurrences"]), str(n["sheet_count"])]
                    for n in nets]))
    A.append("")
    A.append("## Sheets per document")
    A.append("")
    A.append("Useful when a question asks *which volume* uses a potential most "
             "or least.")
    A.append("")
    docs_used = ["+FB", "+Ax", "+BA_Cx_DA", "+EA", "+FA", "+Jx"]
    hdr = ["Potential"] + ["`%s`" % d for d in docs_used] + ["Total"]
    rows = []
    for n in nets:
        per = Counter()
        for sid in n["sheets"]:
            per[sid.split("#")[0]] += 1
        rows.append([code(n["net"])] + [str(per.get(d, 0)) for d in docs_used]
                    + [str(sum(per.values()))])
    A.append(table(hdr, rows))
    A.append("")
    A.append("## Where each potential appears")
    A.append("")
    for n in nets:
        A.append("### `%s`" % n["net"])
        A.append("")
        sheets = sorted(n["sheets"].items(),
                        key=lambda kv: (kv[0].split("#")[0],
                                        int(kv[0].split("#")[1])))
        A.append(", ".join(
            "[%s:%s](../02_SHEETS/%s/SHEET_%04d.md)"
            % (doc, sh, DOC_DIR[doc], int(sh))
            for doc, sh in [(s.split("#")[0], s.split("#")[1]) for s, _ in sheets]))
        A.append("")
    return "\n".join(A)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    with open(os.path.join(DER, "graph.json"), encoding="utf-8") as f:
        graph = json.load(f)

    by_id = {s["id"]: s for s in graph["sheets"]}
    xref_in = Counter()
    xref_in_list = defaultdict(list)
    for e in graph["edges"]:
        if e["type"] != "xref":
            continue
        xref_in[e["to"]] += 1
        xref_in_list[e["to"]].append(e)

    sheets_by_doc = {}
    for _pdf, dockey, _c in DOCUMENTS:
        if args.only and args.only != dockey:
            continue
        recs = load_raw(dockey)
        if not recs:
            continue
        for r in recs:
            r["cols_used"] = sorted({l["col"] for l in r["lines"]})
            r["cols_used"].sort(key="ABCDEFGH".index)
        sheets_by_doc[dockey] = recs

    sections = build_sections(sheets_by_doc)

    # flat ordered list for prev/next
    flat = []
    for dockey in ["+FB", "+Ax", "+BA_Cx_DA", "+EA", "+FA", "+Jx"]:
        for r in sheets_by_doc.get(dockey, []):
            flat.append(r)
    pos = {(r["doc"], r["sheet"]): i for i, r in enumerate(flat)}

    os.makedirs(MD, exist_ok=True)
    n_written = 0

    # ---- per sheet ----
    for dockey, recs in sheets_by_doc.items():
        ddir = os.path.join(MD, "02_SHEETS", DOC_DIR[dockey])
        os.makedirs(ddir, exist_ok=True)
        for i, r in enumerate(recs):
            if args.limit and i >= args.limit:
                break
            p = pos.get((r["doc"], r["sheet"]))
            tfile = os.path.join(ROOT, "data", "derived", "tables",
                                 "%s_%04d.json" % (r["doc"].lstrip("+"), r["sheet"]))
            tabs = None
            if os.path.exists(tfile):
                try:
                    with open(tfile, encoding="utf-8") as tf:
                        tabs = json.load(tf).get("tables")
                except Exception:
                    tabs = None
            ctx = {
                "by_id": by_id,
                "xref_in": xref_in,
                "xref_in_list": xref_in_list,
                "tables": tabs,
                "prev": flat[p - 1] if p is not None and p > 0 else None,
                "next": flat[p + 1] if p is not None and p + 1 < len(flat) else None,
            }
            md = sheet_md(r, graph, ctx)
            with open(os.path.join(ddir, "SHEET_%04d.md" % r["sheet"]),
                      "w", encoding="utf-8") as f:
                f.write(md)
            n_written += 1

    # ---- per document TOC ----
    if not args.limit:
        for dockey, recs in sheets_by_doc.items():
            with open(os.path.join(MD, "02_SHEETS", DOC_DIR[dockey], "_TOC.md"),
                      "w", encoding="utf-8") as f:
                f.write(doc_toc_md(dockey, recs, sections))

        # ---- master TOC ----
        A = ["# Master table of contents", ""]
        A.append("The six documents together hold **1351 A3 sheets**:")
        A.append("")
        rows = []
        for dockey in ["+FB", "+Ax", "+BA_Cx_DA", "+EA", "+FA", "+Jx"]:
            recs = sheets_by_doc.get(dockey, [])
            dcode = recs[0]["title_block"].get("document_code") if recs else "?"
            rows.append([
                code(dockey), DOC_FRIENDLY.get(dockey, ""), str(len(recs)),
                code(dcode or "?"),
                "[TOC](%s/_TOC.md)" % DOC_DIR[dockey],
            ])
        A.append(table(["Document", "Machine section", "Sheets", "Doc code",
                        "Contents"], rows))
        A.append("")
        A.append("## Sections across every document")
        A.append("")
        rows = []
        for dockey in ["+FB", "+Ax", "+BA_Cx_DA", "+EA", "+FA", "+Jx"]:
            for s in sections.get(dockey, []):
                cd, label = topic_of(s["de"], s["en"])
                span = ("%d" % s["from"]) if s["from"] == s["to"] else \
                       ("%d–%d" % (s["from"], s["to"]))
                rows.append([code(dockey), esc(s["de"]) or "—",
                             esc(s["en"]) or "—", cd, span,
                             "[open](%s/SHEET_%04d.md)"
                             % (DOC_DIR[dockey], s["from"])])
        A.append(table(["Doc", "Section DE", "Section EN", "Type", "Sheets",
                        "Open"], rows))
        with open(os.path.join(MD, "02_SHEETS", "_MASTER_TOC.md"),
                  "w", encoding="utf-8") as f:
            f.write("\n".join(A))

        # ---- indexes ----
        idx = os.path.join(MD, "03_INDEX")
        os.makedirs(idx, exist_ok=True)
        os.makedirs(os.path.join(idx, "DEVICES"), exist_ok=True)

        for name, content in [
            ("INDEX_SECTIONS.md", index_sections_md(sheets_by_doc, sections, by_id)),
            ("INDEX_SHEETS.md", index_sheets_md(sheets_by_doc, by_id)),
            ("INDEX_NETS.md", index_nets_md(graph)),
        ]:
            with open(os.path.join(idx, name), "w", encoding="utf-8") as f:
                f.write(content)

        dev_content, per_class = index_devices_md(graph)
        with open(os.path.join(idx, "INDEX_DEVICES.md"), "w",
                  encoding="utf-8") as f:
            f.write(dev_content)
        for cls, content in per_class.items():
            with open(os.path.join(idx, "DEVICES", "CLASS_%s.md" % cls),
                      "w", encoding="utf-8") as f:
                f.write(content)

    print("wrote %d sheet files" % n_written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
