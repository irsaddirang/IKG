"""
gt3.py -- corrected comparison: PDF sheet counts vs KB sheet counts, for both
reasonable definitions of "sheet touches potential N".
"""
import os, re, json
import pymupdf

PDF = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland"
KB = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase"
DOCS = [("Cicuit Diagram +FB.pdf", "+FB"),
        ("Circuit Diagram +Ax.pdf", "+Ax"),
        ("Circuit Diagram +BA, Cx, DA.pdf", "+BA_Cx_DA"),
        ("Circuit Diagram +EA.pdf", "+EA"),
        ("Circuit Diagram +FA.pdf", "+FA"),
        ("Circuit Diagram +Jx.pdf", "+Jx")]

cache = {}
for pdf, dockey in DOCS:
    d = pymupdf.open(os.path.join(PDF, pdf))
    cache[dockey] = [
        [w[4].replace("\xad", " ").strip() for w in d[i].get_text("words")]
        for i in range(d.page_count)]

graph = json.load(open(os.path.join(KB, "data", "derived", "graph.json"), encoding="utf-8"))
kb_nets = {n["net"]: n for n in graph["nets"]}
kb_dev = {d["tag"]: d for d in graph["devices"]}

NETS = ["24V", "0V", "PE", "L24+/4", "M24+", "L1", "N"]
print("=== POTENTIALS: sheets in PDF vs sheets in KB ===")
print("%-10s %7s %7s %7s  %s" % ("net", "A_lit", "B_dot", "KB", "verdict"))
for net in NETS:
    A = set()
    B = set()
    for _f, dk in DOCS:
        for i, words in enumerate(cache[dk]):
            for w in words:
                if w == net:
                    A.add((dk, i + 1))
                    B.add((dk, i + 1))
                elif w.startswith(net + ".") and re.match(
                        r"^" + re.escape(net) + r"\.[A-Za-z0-9]", w):
                    B.add((dk, i + 1))
    kb = set()
    if net in kb_nets:
        for sid in kb_nets[net]["sheets"]:
            doc, sh = sid.rsplit("#", 1)
            kb.add((doc, int(sh)))
    ok = "OK" if kb == B else ("KB>PDF %d" % (len(kb - B)) if kb > B else "KB<PDF %d" % (len(B - kb)))
    print("%-10s %7d %7d %7d  %s" % (net, len(A), len(B), len(kb), ok))

print()
print("=== DEVICES: sheets in PDF vs sheets in KB (whole-word match) ===")
tags = ["K598", "Q001", "K160", "X001", "XB11", "M102/1", "A244:bn", "G006",
        "W1751", "S001", "B001", "Y011", "U101", "F029", "H240/01", "X020"]
print("%-12s %7s %7s  %s" % ("tag", "PDF", "KB", "verdict"))
mism = 0
for tag in tags:
    pdf_sheets = set()
    for _f, dk in DOCS:
        for i, words in enumerate(cache[dk]):
            if tag in words:
                pdf_sheets.add((dk, i + 1))
    kb_sheets = set()
    if tag in kb_dev:
        for sid in kb_dev[tag]["sheets"]:
            doc, sh = sid.rsplit("#", 1)
            kb_sheets.add((doc, int(sh)))
    missing = pdf_sheets - kb_sheets
    extra = kb_sheets - pdf_sheets
    v = "OK"
    if missing:
        v = "MISSING %d %s" % (len(missing), sorted(missing)[:3])
        mism += 1
    elif extra:
        v = "KB-extra %d" % len(extra)
    print("%-12s %7d %7d  %s" % (tag, len(pdf_sheets), len(kb_sheets), v))
print()
print("tags with PDF sheets missing from KB index:", mism)
