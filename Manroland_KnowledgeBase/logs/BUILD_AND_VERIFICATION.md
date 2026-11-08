# Build and verification log

Record of how the knowledge base was constructed and the evidence that it is
correct. All numbers are measured by the scripts in `pipeline/` and by the QA
harness; none are estimates.

---

## 1. Decision: do not OCR

The first question was how to read the sheets. The answer came from measurement.

**Test.** Render the densest sheet (`+Ax` sheet 21, 177 labels, 376 vector paths)
at 300 DPI and compare three extraction routes.

| Route | Result |
|---|---|
| Tesseract OCR (eng) on the 300 DPI render | **confidence 50 %**; device tags shredded (`-F270` → `-F270` ok but `X1.A368:2` → `nro`), rotated labels unusable |
| Embedded PDF text layer (`page.get_text("words")`) | **exact** strings at exact coordinates |
| Visual transcription from the render | plausible but incomplete |

**Conclusion.** These PDFs are born-vector CAE exports (CIM-TEAM, 2010–2012) with
a complete text layer. Every page also contains exactly one embedded raster — the
manroland logo at `Rect(1068.7, 790.1, 1170.7, 809.3)`. **No diagram content is
raster.** OCR is strictly worse and was not used.

The renders are still produced, but only as *visual confirmation of topology*.

---

## 2. Decision: use the PDF's native text blocks as the semantic unit

A wire-end annotation is printed as a horizontal cluster:

```
+A497/2 X1.A463:1        #67        /17.D
```

Investigation showed the exporter already groups these three lines into **one
text block** (`get_text("dict")` block 37 on `+FB` sheet 9 has bbox
`[751.9, 403.9, 839.3, 416.5]` and contains exactly `/13.G`, `#67`, `A244:bn`).
Re-clustering them geometrically from scratch would be strictly worse.

**Therefore `extract.py` groups annotations by the PDF's own block id.** This is
the single design choice that makes the destination/path/cross-reference relation
recoverable with no guesswork.

---

## 3. Decision: 1-bit PNG at 300 DPI for the sheet images

Measured, not assumed:

- Stroke width is **0.85 pt on 21,171 of 21,480 drawing items** → 3.54 px at
  300 DPI. In the worst sub-pixel phase the coverage splits 1.77 / 1.77, so both
  rows clear a 0.5 threshold: a hairline cannot disappear.
- Ink is pure black on white; there is no tonal information. Every grey is an
  anti-aliasing artefact of a hard-edged vector.

| Candidate | Size on a dense sheet | Verdict |
|---|---:|---|
| RGB PNG @ 200 | 528.8 KB | largest *and* lowest resolution |
| Grayscale PNG @ 300 | 393.3 KB | 3.5× bigger, no information gain |
| **1-bit PNG @ 300** | **111.6 KB** | **chosen** |
| 1-bit PNG @ 400 | 157.2 KB | 1.4× bigger, no legibility gain |

Verification of the 1-bit output (four independent tests):

- solid-ink recall **1.000000** — no solid pixel lost
- black pixels on pure white **0.0** — no dither speckle
- connected components ≤ 2 px: **0** — no dotting
- walked every thin solid line using the page's own vector segments:
  **0 gaps over 177,000 samples**

Total: **1,351 images, 89.2 MiB, 67.6 KB average**, every file 4961 × 3508.

---

## 4. Decision: reconstruct tabular sheets from rule lines

`Reference module` (327 sheets) and `Terminal strip` (12 sheets) sheets are pin
tables, not wire fields:

```
PIN        BYTE.BIT   STROMPFAD
3A 3B 3C   0.0
4A 4B 4C   0.1        /328.B
```

Text extraction alone returns these as an unordered bag of numbers, which is
useless for answering "what does pin 4B map to?".

`tables.py` rebuilds the grid from the drawing's **own rule lines**:

1. collect horizontal and vertical rules, excluding the page frame (a rule wider
   than 80 % of the page) and the title block (`y ≥ 769`);
2. split into separate tables at horizontal gaps > 110 pt;
3. form row/column bands from the rule coordinates;
4. assign each word to the cell containing its centre;
5. emit rows in reading order.

Result: **1,114 of 1,351 sheets** got a reconstructed grid. Sample from `+EA`
sheet 200 (`-A356/13` / `-A356/14` pin map):

| PIN | | | BYTE.BIT | STROMPFAD | | PIN | | | BYTE.BIT | STROMPFAD |
|---|---|---|---|---|---|---|---|---|---|---|
| `3A` | `3B` | `3C` | 0.0 | | | `3A` | `3B` | `3C` | 19.0 | `/366.D` |
| `4A` | `4B` | `4C` | 0.1 | `/328.B` | | `4A` | `4B` | `4C` | 19.1 | `/366.E` |

This matches the rendered sheet row for row.

---

## 5. Verification results

Run in this order. All pass.

### 5.1 Label fidelity — the central check

For **every** sheet, every text object inside the drawing area of the source PDF
is compared **character-for-character** against the generated Markdown.

```
sheets checked : 1351 / 1351
labels checked : 180,916
labels missing : 0   (0.0000 %)
bad sheets     : 0
```

This is the guarantee behind the claim "if a string is not in the sheet file, it
is not printed on that sheet."

### 5.2 Cross-reference integrity

```
xref edges     : 34,890
unresolved     : 0
```

Every `/sheet.column` resolves to a sheet that exists in the same document.

Note on the 57 flagged "column mismatches": these are cross-references into
`REFERENZMODUL` sheets, which are tabular. A table does not populate all eight
DIN column bands, so the target column letter has no printed content in that
band. This is a property of table sheets, **not** a resolution failure — the
cross-reference itself is correct and the sheet is correct.

### 5.3 Image integrity

```
files checked  : 1,351
valid PNG      : 1,351
size           : all 4961 × 3508
missing        : 0
corrupt        : 0
```

### 5.4 Internal links

```
links checked  : 101,052
broken         : 0
```

Covers sheet-to-sheet links, image links, TOC links, index-to-sheet links and
device-index links.

### 5.5 Graph statistics

```
sheets             : 1,351
documents          : 6
text labels        : 180,916
cross-references   : 34,890
distinct devices   : 6,324   (26,126 occurrences)
distinct potentials: 232     (3,566 occurrences)
distinct terminals : 637
tables rebuilt     : 1,114 sheets
RAG chunks         : 9,536
```

### 5.6 Acceptance test

17 checks covering coverage, image validity, fidelity, cross-reference integrity,
link integrity, and whether a real question can actually be answered from the
generated files. **17 passed, 0 failed.**

---

## 6. Known imperfections, stated rather than hidden

| Item | Status |
|---|---|
| `#NN` path numbers | Present on only **7 of 1,351 sheets** and on 28 of 34,890 cross-references. It is a rare annotation, not a coordinate. The knowledge base says so explicitly rather than implying universal numbering. |
| Multi-token destination labels | A cluster may name several destinations (`+A497/2 K160/1:A2, +A497/2 K160:A2`). These are preserved verbatim as one string; individual tokens are also parsed where they match the tag grammar. |
| Conductor colour/section → specific wire | Positional, not relational. The per-sheet tables are inventories. Stated as a limitation. |
| Bare `NNN.C` tokens on terminal-strip sheets | These are sheet/column location references, not devices. Moved to a separate `sheetcol_refs` bucket instead of polluting the device index. |
| `BYTE.BIT` on reference-module sheets | A column header, excluded from the device index. |
| Text objects with no rendered ink | Some sheets contain empty/whitespace spans at fixed coordinates. They are filtered by requiring non-empty text after normalisation. |
| OCR | Deliberately not used. |

---

## 7. Reproduce

```powershell
cd Manroland_KnowledgeBase\pipeline
$py = "C:\Users\muham\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
& $py build.py --with-images
```

Stages: `extract.py` (≈20 s) → `tables.py` (≈60 s) → `graph.py` → `mdgen.py` →
`export.py` → `render.py` (≈70 s). All resumable, all accept `--only <doc>`.
