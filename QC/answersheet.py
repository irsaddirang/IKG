"""
answersheet.py -- compute the correct answers for the QC benchmark directly from
the source PDFs (independent of the generated Markdown), so scoring is objective.
"""
import os, re, json, collections
import pymupdf

PDF = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland"
OUT = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\QC"
DOCS = [("Cicuit Diagram +FB.pdf", "+FB"),
        ("Circuit Diagram +Ax.pdf", "+Ax"),
        ("Circuit Diagram +BA, Cx, DA.pdf", "+BA_Cx_DA"),
        ("Circuit Diagram +EA.pdf", "+EA"),
        ("Circuit Diagram +FA.pdf", "+FA"),
        ("Circuit Diagram +Jx.pdf", "+Jx")]

pages = {}
for pdf, dk in DOCS:
    d = pymupdf.open(os.path.join(PDF, pdf))
    pages[dk] = [{"sheet": i + 1,
                  "words": [(round(w[0], 1), round(w[1], 1),
                             w[4].replace("\xad", " ").strip())
                            for w in d[i].get_text("words")],
                  "text": d[i].get_text("text").replace("\xad", " ").replace("\xa0", " ")}
                 for i in range(d.page_count)]

ANS = {}

def sheets_with(dk, tok):
    return [p["sheet"] for p in pages[dk]
            if any(w[2] == tok for w in p["words"])]

# ---- Q1 / Q15: K598 ----
ANS["Q1"] = {dk: sheets_with(dk, "K598") for _f, dk in DOCS
             if sheets_with(dk, "K598")}

# ---- Q2: EA#200 title block ----
p = pages["+EA"][199]
ANS["Q2"] = {
    "section_de": "REFERENZMODUL",
    "section_en": "REFERENCE MODULE",
    "document_code": "8039G38E915",
    "evidence_ok": ("REFERENZMODUL" in p["text"] and "REFERENCE MODULE" in p["text"]
                    and "8039G38E915" in p["text"]),
}

# ---- Q3: biggest doc ----
ANS["Q3"] = {"doc": "+EA", "sheets": 407,
             "all": {dk: len(pages[dk]) for _f, dk in DOCS}}

# ---- Q4/Q5: FB#9 K598:A2 wire + reciprocal ----
fb9 = pages["+FB"][8]
rows = collections.defaultdict(list)
for (x, y, t) in fb9["words"]:
    rows[round(y / 4)].append((x, t))
def row_of(tok, sheet="+FB", idx=8):
    for (x, y, t) in pages[sheet][idx]["words"]:
        if t == tok:
            near = sorted([(xx, tt) for (xx, yy, tt) in pages[sheet][idx]["words"]
                           if abs(yy - y) < 3.0], key=lambda r: r[0])
            return [tt for _xx, tt in near]
    return None

ANS["Q4"] = {"annotation_block": "/14.F #65 +A497/1 K598:A2"}
ANS["Q4_expected"] = {"to_sheet": 14, "to_column": "F", "path": 65}

# reciprocal on FB#14: which /9.x refs exist there
d14 = pymupdf.open(os.path.join(PDF, "Cicuit Diagram +FB.pdf"))
ANS["Q5"] = {"refs_back_to_9_on_sheet_14":
             sorted({w[4].replace("\xad", " ").strip()
                     for w in d14[13].get_text("words")
                     if re.fullmatch(r"/9\.[A-H]", w[4].replace("\xad", " ").strip())}),
             "expected_back_ref": "/9.F",
             "expected_column": "F"}

# ---- Q6: /13.G destination ----
row = row_of("A244:bn")
ANS["Q6"] = {"row": row, "expected_target": "A244:bn"}

# ---- Q7: EA#200 xref counts ----
p = pages["+EA"][199]
words = [w[2] for w in p["words"]]
ANS["Q7"] = {"xref_tokens_out": len([w for w in words if re.fullmatch(r"/\d{1,3}\.[A-H]", w)])}

# ---- Q8: which FB sheets point to sheet 19 ----
out19 = []
for p in pages["+FB"]:
    if any(re.fullmatch(r"/19\.[A-H]", w[2]) for w in p["words"]):
        out19.append(p["sheet"])
ANS["Q8"] = {"sheets": out19}

# ---- Q9/Q10: EA#200 pin table ----
def table_row(anchor):
    for (x, y, t) in pages["+EA"][199]["words"]:
        if t == anchor:
            near = sorted([(xx, tt) for (xx, yy, tt) in pages["+EA"][199]["words"]
                           if abs(yy - y) < 3.0], key=lambda r: r[0])
            return [tt for _xx, tt in near]
    return None

ANS["Q9"] = {"row_4C": table_row("4C"),  "expected_bit": "0.1", "expected_path": "/328.B"}
ANS["Q10"] = {"row_26C": table_row("26C"), "expected_bit": "21.7", "expected_path": "/191.G"}

# ---- Q11: FA#44 X020 ----
ANS["Q11"] = {"row": table_row("X020") if False else None}
r = []
for (x, y, t) in pages["+FA"][43]["words"]:
    if t == "X020":
        r = sorted([(xx, tt) for (xx, yy, tt) in pages["+FA"][43]["words"]
                    if abs(yy - y) < 3.0], key=lambda q: q[0])
ANS["Q11"] = {"row": [tt for _xx, tt in r], "expected": "+A497"}

# ---- Q12: FB#9 nets + columns ----
net_tokens = collections.Counter()
for (x, y, t) in fb9["words"]:
    if re.fullmatch(r"(24V|0V|L24\+/4|M24\+|PE|L1|N)", t) or re.match(r"^(24V|0V|L24\+/4|M24\+)\.", t):
        head = re.split(r"[.:]", t)[0]
        net_tokens[head] += 1
ANS["Q12"] = {"nets": dict(net_tokens)}

# ---- Q13: FA sheets with PE ----
ANS["Q13"] = {"sheets": sheets_with("+FA", "PE")}

# ---- Q14: EA#200 table dims (rows = distinct pin labels) ----
pins = sorted({t for (x, y, t) in pages["+EA"][199]["words"]
               if re.fullmatch(r"\d{1,2}[ABC]", t)})
ANS["Q14"] = {"distinct_pin_labels": len(pins), "sample": pins[:6]}

# ---- Q16: 24V per document ----
c = {dk: len(sheets_with(dk, "24V")) for _f, dk in DOCS}
ANS["Q16"] = {"per_doc": c, "min": min(c, key=c.get), "max": max(c, key=c.get)}

# ---- Q17: device classes on FB#9 ----
cls = collections.Counter()
for p in [fb9]:
    for (x, y, t) in p["words"]:
        m = re.fullmatch(r"[+\-]?([A-Z]{1,3})(\d{2,4})(?:/\d{1,2})?(?:\.([A-Z]{1,3}\d{1,4}))?(?::[0-9A-Za-z]{1,6})?", t)
        if m and len(t) <= 12:
            cls[m.group(1)] += 1
ANS["Q17"] = {"frozenset_like": dict(cls)}

# ---- Q18: MASCHINENSCHEMA docs ----
ms = {}
for _f, dk in DOCS:
    s = [p["sheet"] for p in pages[dk] if "MASCHINENSCHEMA" in p["text"]]
    if s:
        ms[dk] = s
ANS["Q18"] = ms

# ---- Q19: conductor on FB#9 ----
xs = [t for (x, y, t) in fb9["words"] if re.fullmatch(r"\d\.\d{2}", t)]
col = [t for (x, y, t) in fb9["words"] if t.lower() in ("blau", "braun", "schwarz")]
ANS["Q19"] = {"xsection_tokens": xs, "colour_tokens": col,
              "expected": "1.50 mm² and Blau, annotating a specific wire"}

# ---- traps ----
ANS["Q20"] = {"answer": "NOT STATED — no part numbers in these drawings"}
ANS["Q21"] = {"answer": "NOT STATED — no current ratings in these drawings"}
ANS["Q22"] = {"answer": "Does not exist; /999.A is outside the 1..407 sheet range"}
ANS["Q23"] = {"answer": "K9999 does not appear anywhere"}
ANS["Q24"] = {"answer": "NOT STATED — drawings give no functional description"}
ANS["Q25"] = {"sheets_with_path_numbers": 7,
              "answer": "#67 is not global; on 7 sheets only, 28 of 34,890 xrefs"}
ANS["Q26"] = {"answer": "No. Series-maximum warning is printed on the disposition "
                        "plans; actual equipment must be taken from the circuit diagram "
                        "and the INDEX option sheets."}

with open(os.path.join(OUT, "answer_key.json"), "w", encoding="utf-8") as f:
    json.dump(ANS, f, ensure_ascii=False, indent=1)

print(json.dumps(ANS, ensure_ascii=False, indent=1)[:6000])
