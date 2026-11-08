"""
gt.py -- build an INDEPENDENT ground-truth dataset for benchmarking.

Independence matters: this script must NOT reuse the pipeline's classify() logic
or the generated Markdown. It queries the source PDFs directly with a different
method (raw text search over page words), so a benchmark answer that disagrees
with it is a real disagreement, not a shared bug.

Each fact is recorded with the exact PDF evidence needed to verify it by hand.
"""
import os, re, json, random
import pymupdf

PDF = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland"
OUT = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\QC"
DOCS = [("Cicuit Diagram +FB.pdf", "+FB"),
        ("Circuit Diagram +Ax.pdf", "+Ax"),
        ("Circuit Diagram +BA, Cx, DA.pdf", "+BA_Cx_DA"),
        ("Circuit Diagram +EA.pdf", "+EA"),
        ("Circuit Diagram +FA.pdf", "+FA"),
        ("Circuit Diagram +Jx.pdf", "+Jx")]

os.makedirs(OUT, exist_ok=True)

# Cache page text: list of (sheet, full_text, words)
cache = {}
for pdf, dockey in DOCS:
    d = pymupdf.open(os.path.join(PDF, pdf))
    pages = []
    for i in range(d.page_count):
        t = d[i].get_text("text").replace("\xad", " ").replace("\xa0", " ")
        w = [(x[0], x[1], x[4].replace("\xad", " ").strip()) for x in d[i].get_text("words")]
        pages.append({"sheet": i + 1, "text": t, "words": w})
    cache[dockey] = pages
    print("cached", dockey, len(pages), "pages", flush=True)


def pages_with(dockey, token, exact_word=False):
    """Sheets of dockey where token appears (as a whole word by default)."""
    out = []
    for p in cache[dockey]:
        if exact_word:
            if any(w[2] == token for w in p["words"]):
                out.append(p["sheet"])
        else:
            # word-ish boundary that tolerates the PDF's soft-hyphen spacing
            if re.search(r"(?<![0-9A-Za-z])" + re.escape(token) + r"(?![0-9A-Za-z])",
                         p["text"]):
                out.append(p["sheet"])
    return out


def find_rows(dockey, sheet, needle):
    """Return the words on the same visual row (y within +-2pt) as needle."""
    p = cache[dockey][sheet - 1]
    hits = [w for w in p["words"] if w[2] == needle]
    out = []
    for h in hits:
        row = [(round(y, 1), round(x, 1), t) for (x, y, t) in p["words"]
               if abs(y - h[1]) < 2.2 and t]
        row.sort(key=lambda r: r[1])
        out.append({"anchor": (round(h[1], 1), round(h[0], 1)),
                    "row": [r[2] for r in row]})
    return out


# ---------------------------------------------------------------------------
# FACTS: each is verified against raw PDF text, never against the markdown
# ---------------------------------------------------------------------------
facts = {}

# --- A. device occurrence (single-device lookup) ---
for tag in ["K598", "Q001", "K160", "Y011", "U101", "F029", "X001"]:
    per = {dk: pages_with(dk, tag) for _f, dk in DOCS}
    per = {k: v for k, v in per.items() if v}
    facts["dev_" + tag] = {"tag": tag, "documents": per}

# --- B. a specific cross-reference cluster, verbatim ---
# pick from FB sheet 9 (already manually verified earlier)
rows = find_rows("+FB", 9, "#67")
facts["fb9_path67_rows"] = rows

# --- C. reference-module pin table row ---
# EA sheet 200: find the row containing '4C' and read neighbours
facts["ea200_row_4C"] = find_rows("+EA", 200, "4C")
facts["ea200_row_26C"] = find_rows("+EA", 200, "26C")

# --- D. terminal strip content ---
facts["fa44_rows_X020"] = find_rows("+FA", 44, "X020")

# --- E. potential distribution ---
for net in ["24V", "0V", "PE", "L24+/4"]:
    tot = 0
    sheets = {}
    for _f, dk in DOCS:
        s = pages_with(dk, net, exact_word=True)
        if s:
            sheets[dk] = s
            tot += len(s)
    facts["net_" + net.replace("+", "p").replace("/", "_")] = {
        "net": net, "total_sheets": tot, "per_doc_sheets": {k: len(v) for k, v in sheets.items()}}

# --- F. which documents mention a function (German) ---
for term in ["NOT AUS", "KLEMMLEISTE", "SPANNUNGSVERSORGUNG", "MASCHINENSCHEMA"]:
    per = {}
    for _f, dk in DOCS:
        s = pages_with(dk, term)
        if s:
            per[dk] = s
    facts["term_" + term.replace(" ", "_")] = {"term": term, "documents": per}

# --- G. negative controls: tokens that must NOT exist anywhere ---
for fake in ["K9999", "ZZQX", "X88888"]:
    found = []
    for _f, dk in DOCS:
        if pages_with(dk, fake, exact_word=True):
            found.append(dk)
    facts["absent_" + fake] = {"token": fake, "found_in": found}

# --- H. section ranges (from title block, raw scan) ---
sec = {}
for _f, dk in DOCS:
    spans = []
    cur = None
    for p in cache[dk]:
        m = re.search(r"(STROMLAUFPLAN|CIRCUIT DIAGRAM)\s*\n(.*?)\n", p["text"])
        title = None
        # title block EN line: line after CIRCUIT DIAGRAM usually holds the EN title
        lines = [l.strip() for l in p["text"].splitlines() if l.strip()]
        for i, l in enumerate(lines):
            if l.replace(" ", "") == "CIRCUITDIAGRAM" and i + 1 < len(lines):
                title = lines[i + 1]
                break
        if title != cur:
            spans.append({"from": p["sheet"], "title": title})
            cur = title
    sec[dk] = spans
facts["sections"] = sec

with open(os.path.join(OUT, "ground_truth.json"), "w", encoding="utf-8") as f:
    json.dump(facts, f, ensure_ascii=False, indent=1)

print("\n=== GROUND TRUTH BUILD ===")
for k, v in facts.items():
    if k.startswith("dev_"):
        print("%-22s docs=%s" % (k, {d: len(s) for d, s in v["documents"].items()}))
    elif k.startswith("net_"):
        print("%-22s sheets=%d %s" % (k, v["total_sheets"], v["per_doc_sheets"]))
    elif k.startswith("term_"):
        print("%-22s docs=%s" % (k, sorted(v["documents"])))
    elif k.startswith("absent_"):
        print("%-22s found_in=%s" % (k, v["found_in"]))
print("\nfb9 #67 rows:", len(facts["fb9_path67_rows"]))
for r in facts["fb9_path67_rows"][:5]:
    print("   ", r["anchor"], r["row"])
print("\nea200 row 4C:", facts["ea200_row_4C"][:2])
print("\nea200 row 26C:", facts["ea200_row_26C"][:2])
print("\nfa44 X020:", facts["fa44_rows_X020"][:2])
