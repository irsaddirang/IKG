"""Full-corpus fidelity QA: every label of every sheet."""
import os, re, sys
import pymupdf

PDF_DIR = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland"
MD = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase\md"

DOCS = [
    ("Cicuit Diagram +FB.pdf", "+FB", "FB"),
    ("Circuit Diagram +Ax.pdf", "+Ax", "Ax"),
    ("Circuit Diagram +BA, Cx, DA.pdf", "+BA_Cx_DA", "BA_Cx_DA"),
    ("Circuit Diagram +EA.pdf", "+EA", "EA"),
    ("Circuit Diagram +FA.pdf", "+FA", "FA"),
    ("Circuit Diagram +Jx.pdf", "+Jx", "Jx"),
]

def clean(s):
    return re.sub(r" {2,}", " ", s.replace("\xad", " ").replace("\xa0", " ").strip())

total = missing = sheets_bad = sheets = 0
worst = []
for pdf, dockey, ddir in DOCS:
    d = pymupdf.open(os.path.join(PDF_DIR, pdf))
    for i in range(d.page_count):
        sheet = i + 1
        p = os.path.join(MD, "02_SHEETS", ddir, "SHEET_%04d.md" % sheet)
        if not os.path.exists(p):
            print("MISSING", dockey, sheet)
            sheets_bad += 1
            continue
        md = open(p, encoding="utf-8").read()
        sheets += 1
        miss = []
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
                    miss.append(t)
        if miss:
            missing += len(miss)
            sheets_bad += 1
            worst.append((dockey, sheet, len(miss), miss[:4]))
    print("%s done: sheets=%d labels=%d missing=%d" % (dockey, sheets, total, missing), flush=True)

print("=" * 60)
print("FULL CORPUS: sheets=%d/%d labels=%d missing=%d (%.4f%%) bad_sheets=%d"
      % (sheets, 1351, total, missing, 100.0 * missing / max(1, total), sheets_bad))
for w in worst[:20]:
    print("  ", w)
