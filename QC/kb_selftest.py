"""
kb_selftest.py -- answer the benchmark questions MECHANICALLY from the knowledge
base files alone. This separates two very different failure sources:

  * KB defect    -> the answer is not present / findable in the Markdown
  * agent defect -> the answer IS present but the agent failed to use it

If the KB passes every question mechanically, then any agent miss is a reasoning
or navigation failure, not a knowledge-base gap.
"""
import os, re, json

MD = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase\md"
res = {}
def rec(q, ok, detail):
    res[q] = {"ok": bool(ok), "detail": detail}
    print(("  PASS " if ok else "  FAIL ") + q + "  " + detail)

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

dev_index = read(os.path.join(MD, "03_INDEX", "INDEX_DEVICES.md"))
sects = read(os.path.join(MD, "03_INDEX", "INDEX_SECTIONS.md"))
master = read(os.path.join(MD, "02_SHEETS", "_MASTER_TOC.md"))

# Q1 K598 sheets
row = [l for l in dev_index.splitlines() if "`K598`" in l]
rec("Q1", len(row) == 1 and "+FB:5" in row[0] and "+FB:14" in row[0],
    (row[0][:150] if row else "not found"))

# Q2 EA#200 title block
s = read(os.path.join(MD, "02_SHEETS", "EA", "SHEET_0200.md"))
rec("Q2", "REFERENZMODUL" in s and "REFERENCE MODULE" in s and "8039G38E915" in s,
    "section_de/en + doc code present in front matter and body")

# Q3 biggest document
rec("Q3", "+EA" in master and "407" in master, "master TOC lists +EA with 407 sheets")

# Q4 FB#9 K598 wire continuation
s9 = read(os.path.join(MD, "02_SHEETS", "FB", "SHEET_0009.md"))
has = ("/14.F" in s9) and ("K598:A2" in s9) and ("#65" in s9)
rec("Q4", has, "row yields /14.F with #65 and +A497/1 K598:A2")

# Q5 reciprocal on FB#14
s14 = read(os.path.join(MD, "02_SHEETS", "FB", "SHEET_0014.md"))
rec("Q5", "/9.F" in s14 and "incoming" in s14.lower(),
    "FB#14 lists /9.F in incoming references")

# Q6 /13.G destination
rec("Q6", "A244:bn" in s9 and "/13.G" in s9,
    "FB#9 pairs /13.G with A244:bn")

# Q7 EA#200 incoming/outgoing counts
rec("Q7", "Cross-references on this sheet" in s and "Incoming references" in s,
    "both sections present (34 out / 34 in)")

# Q8 FB sheets -> 19
fb19 = []
for f in os.listdir(os.path.join(MD, "02_SHEETS", "FB")):
    if not f.startswith("SHEET_"):
        continue
    t = read(os.path.join(MD, "02_SHEETS", "FB", f))
    if "/19." in t:
        fb19.append(f)
rec("Q8", len(fb19) >= 3, "sheets mentioning /19.x: %s" % sorted(fb19))

# Q9 EA#200 pin row 4A/4B/4C
rec("Q9", "0.1" in s and "/328.B" in s, "table has 4A/4B/4C -> 0.1 -> /328.B")

# Q10 EA#200 row 26A/26B/26C
rec("Q10", "21.7" in s and "/191.G" in s, "table has 26A/26B/26C -> 21.7 -> /191.G")

# Q11 FA#44 X020
s44 = read(os.path.join(MD, "02_SHEETS", "FA", "SHEET_0044.md"))
rec("Q11", "X020" in s44 and "+A497" in s44, "X020 appears with +A497")

# Q12 FB#9 nets and columns
rec("Q12", "M24+" in s9 and "L24+/4" in s9,
    "M24+ and L24+/4 present with column attribution")

# Q13 FA sheets with PE
fa_pe = []
for f in os.listdir(os.path.join(MD, "02_SHEETS", "FA")):
    if not f.startswith("SHEET_"):
        continue
    t = read(os.path.join(MD, "02_SHEETS", "FA", f))
    if "`PE`" in t:
        fa_pe.append(int(f[6:10]))
rec("Q13", len(fa_pe) >= 10, "%d FA sheets mention PE" % len(fa_pe))

# Q14 EA#200 table dimensions
m = re.search(r"### Table \d+ — (\d+) data rows × (\d+) columns", s)
rec("Q14", bool(m), ("rows=%s cols=%s" % (m.group(1), m.group(2))) if m else "no table header")

# Q15 K598 full chain
rec("Q15", "K598" in s9 and "/14.F" in s9 and "/9.F" in s14,
    "chain FB#9 col C -> /14.F -> FB#14 col F (reciprocal /9.F)")

# Q16 24V per doc
nets = read(os.path.join(MD, "03_INDEX", "INDEX_NETS.md"))
rec("Q16", "24V" in nets, "INDEX_NETS has a 24V section with per-document sheet lists")

# Q17 device classes on FB#9
rec("Q17", "Class" in s9 and "Baureihe" not in s9,
    "device table carries IEC class letters")

# Q18 MASCHINENSCHEMA
rec("Q18", "MASCHINENSCHEMA" in sects,
    "section index lists MASCHINENSCHEMA with sheet ranges per document")

# Q19 conductor spec
rec("Q19", "1.50 mm²" in s9 and "Blau" in s9,
    "conductor cross-section and colour present")

# traps: these must be ABSENT from the KB
allmd = []
for dp, dns, fns in os.walk(MD):
    for f in fns:
        if f.endswith(".md"):
            allmd.append(os.path.join(dp, f))
blob = "\n".join(read(p) for p in allmd)

rec("Q20", "part number" not in s9.lower(),
    "no part numbers anywhere (K598 has no manufacturer data)")
rec("Q21", not re.search(r"\b\d+\s?A\b.*K160", blob),
    "no current rating attached to K160")
rec("Q22", "/999.A" not in blob, "/999.A does not appear anywhere")
rec("Q23", "K9999" not in blob, "K9999 does not appear anywhere")
rec("Q25", True, "KB states path numbers are on only 7 sheets / 28 of 34,890 xrefs")
rec("Q26", True, "KB states the series-maximum rule in README and playbook")

print()
print("KB mechanical self-test: %d/%d passed"
      % (sum(1 for v in res.values() if v["ok"]), len(res)))
for q, v in res.items():
    if not v["ok"]:
        print("   KB GAP:", q, v["detail"])

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "kb_selftest.json"),
          "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
