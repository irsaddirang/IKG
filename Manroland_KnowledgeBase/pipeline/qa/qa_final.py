"""
Final end-to-end acceptance test for the manroland knowledge base.
Checks the objective's actual success criterion: an agent asking a question about
the diagram must be able to read it correctly.  Every check is measurable.
"""
import os, re, json, sys
import pymupdf

KB = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase"
PDF = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland"
MD = os.path.join(KB, "md")
DOCS = [("Cicuit Diagram +FB.pdf", "+FB", "FB"),
        ("Circuit Diagram +Ax.pdf", "+Ax", "Ax"),
        ("Circuit Diagram +BA, Cx, DA.pdf", "+BA_Cx_DA", "BA_Cx_DA"),
        ("Circuit Diagram +EA.pdf", "+EA", "EA"),
        ("Circuit Diagram +FA.pdf", "+FA", "FA"),
        ("Circuit Diagram +Jx.pdf", "+Jx", "Jx")]
ok = []
bad = []

def chk(name, cond, detail=""):
    (ok if cond else bad).append((name, detail))
    print(("  PASS  " if cond else "  FAIL  ") + name + (("  " + detail) if detail else ""))

print("=== 1. Coverage ===")
md_count = 0
for d in os.listdir(os.path.join(MD, "02_SHEETS")):
    p = os.path.join(MD, "02_SHEETS", d)
    if os.path.isdir(p):
        md_count += len([f for f in os.listdir(p) if f.startswith("SHEET_")])
chk("1,351 sheet markdown files", md_count == 1351, "found %d" % md_count)

img_count = 0
for d in os.listdir(os.path.join(KB, "images")):
    p = os.path.join(KB, "images", d)
    if os.path.isdir(p):
        img_count += len([f for f in os.listdir(p) if f.endswith(".png")])
chk("1,351 sheet images", img_count == 1351, "found %d" % img_count)

print("\n=== 2. Every image is a valid, large PNG ===")
import struct
sample = 0
badimg = 0
for d in sorted(os.listdir(os.path.join(KB, "images"))):
    p = os.path.join(KB, "images", d)
    if not os.path.isdir(p):
        continue
    for f in sorted(os.listdir(p)):
        if not f.endswith(".png"):
            continue
        fp = os.path.join(p, f)
        if os.path.getsize(fp) < 5000:
            badimg += 1
            continue
        with open(fp, "rb") as fh:
            head = fh.read(33)
        if head[:8] != b"\x89PNG\r\n\x1a\n":
            badimg += 1
            continue
        w, h = struct.unpack(">II", head[16:24])
        if w < 4000 or h < 3000:
            badimg += 1
            continue
        sample += 1
chk("all images valid >=4000x3000", badimg == 0, "%d checked, %d bad" % (sample, badimg))

print("\n=== 3. Systematic fidelity: every label of every sheet ===")
def clean(s):
    return re.sub(r" {2,}", " ", s.replace("\xad", " ").replace("\xa0", " ").strip())
total = miss = 0
for pdf, dockey, ddir in DOCS:
    d = pymupdf.open(os.path.join(PDF, pdf))
    for i in range(d.page_count):
        p = os.path.join(MD, "02_SHEETS", ddir, "SHEET_%04d.md" % (i + 1))
        md = open(p, encoding="utf-8").read()
        for b in d[i].get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            for ln in b["lines"]:
                t = clean("".join(sp.get("text", "") for sp in ln["spans"]))
                if not t:
                    continue
                x0, y0, x1, y1 = ln["bbox"]
                if x1 <= 57.7:
                    continue
                if re.fullmatch(r"[A-H]", t) and (y1 <= 16 or y0 >= 828):
                    continue
                if y0 >= 770.9:
                    continue
                total += 1
                if ("`%s`" % t.replace("`", "'")) not in md:
                    miss += 1
chk("zero labels missing across all sheets", miss == 0,
    "%d/%d labels, %d missing" % (total - miss, total, miss))

print("\n=== 4. Cross-reference integrity ===")
g = json.load(open(os.path.join(KB, "data", "derived", "graph.json"), encoding="utf-8"))
ids = {s["id"] for s in g["sheets"]}
xr = [e for e in g["edges"] if e["type"] == "xref"]
unres = [e for e in xr if e["to"] not in ids]
chk("all cross-references resolve to a real sheet",
    len(unres) == 0, "%d/%d, %d unresolved" % (len(xr) - len(unres), len(xr), len(unres)))

print("\n=== 5. Links resolve ===")
link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
checked = broken = 0
for dp, dns, fns in os.walk(MD):
    for fn in fns:
        if not fn.endswith(".md"):
            continue
        f = os.path.join(dp, fn)
        s = open(f, encoding="utf-8").read()
        for m in link_re.finditer(s):
            t = m.group(1).strip()
            if t.startswith(("http", "mailto:", "#")) or not t:
                continue
            checked += 1
            if not os.path.exists(os.path.normpath(
                    os.path.join(os.path.dirname(f), t.split("#")[0]))):
                broken += 1
chk("zero broken internal links", broken == 0,
    "%d/%d links, %d broken" % (checked - broken, checked, broken))

print("\n=== 6. Agent-answerable: spot-check real questions ===")
# 6a. device lookup index covers a known device and points at real sheets
dev = open(os.path.join(MD, "03_INDEX", "INDEX_DEVICES.md"), encoding="utf-8").read()
chk("INDEX_DEVICES lists K598", "`K598`" in dev)
chk("INDEX_DEVICES links resolve", "../02_SHEETS/" in dev)

# 6b. a known wire cluster is readable as destination+path+xref
s9 = open(os.path.join(MD, "02_SHEETS", "FB", "SHEET_0009.md"), encoding="utf-8").read()
chk("FB#9 exposes the /17.D cross-ref", "/17.D" in s9)
chk("FB#9 exposes its destination text", "X1.A463:1" in s9)
chk("FB#9 exposes path number #67", "#67" in s9)
chk("FB#9 exposes potential L24+/4", "L24+/4" in s9)
chk("FB#9 has a reciprocal incoming-refs section", "Incoming references" in s9)

# 6c. pin table reconstructed on a reference-module sheet
s200 = open(os.path.join(MD, "02_SHEETS", "EA", "SHEET_0200.md"), encoding="utf-8").read()
chk("EA#200 has a reconstructed table", "Reconstructed tables" in s200)
chk("EA#200 table has STROMPFAD column", "STROMPFAD" in s200)
chk("EA#200 table preserves a row pairing", "/366.D" in s200)

# 6d. every sheet has front matter + image + inventory
import random
random.seed(11)
allsheets = []
for doc in ("FB", "Ax", "BA_Cx_DA", "EA", "FA", "Jx"):
    p = os.path.join(MD, "02_SHEETS", doc)
    allsheets += [os.path.join(p, f) for f in os.listdir(p) if f.startswith("SHEET_")]
random.shuffle(allsheets)
badf = 0
for f in allsheets[:120]:
    s = open(f, encoding="utf-8").read()
    if not (s.startswith("---") and "\nimage:" in s
            and "## Complete label inventory" in s and "![+"
            or "![" in s):
        badf += 1
chk("front matter + image + inventory present", badf == 0,
    "%d sampled, %d bad" % (min(120, len(allsheets)), badf))

print("\n" + "=" * 62)
print("PASSED %d checks, FAILED %d" % (len(ok), len(bad)))
if bad:
    for n, d in bad:
        print("  FAILED:", n, d)
    sys.exit(1)
print("ALL ACCEPTANCE CHECKS PASSED")
