# manroland R700 — Wiring Diagram Knowledge Base

A complete, machine-readable knowledge base of the electrical wiring diagrams for
the **manroland R700** sheet-fed offset printing press, built from six PDF
drawing sets totalling **1,351 DIN A3 sheets**.

**Start here → [`md/00_READ_ME_FIRST.md`](md/00_READ_ME_FIRST.md)**

---

## Why this exists

The goal: *when you ask a question about the diagrams, an AI reads them
correctly.* That is harder than it sounds — these sheets are dense (1,900 vector
paths, ~2,900 characters each), and a vision model misreads them badly.

### The key discovery

The source PDFs are **not scans**. They are born-vector CAE exports from the
CIM-TEAM system with a **real, complete text layer**, and the PDF's own text-block
grouping is already semantic: a wire-end annotation is one block containing
`destination` + `#line` + `/sheet.column`.

Measured on a dense sheet:

| Method | Result |
|---|---|
| Tesseract OCR @300 DPI | **~50 % confidence**, heavily garbled |
| Embedded PDF text layer | **exact strings at exact coordinates** |

So the knowledge base is derived from **the vector text layer and vector
geometry**, not from pixels. Precision equals the CAD export's precision.

The 300 DPI renders are included, but only for **visual confirmation of
topology** — never as the source of a label.

---

## What was built

```
Manroland_KnowledgeBase/
├── md/                                  the knowledge base
│   ├── 00_READ_ME_FIRST.md              orientation + limitations
│   ├── 00_QUERY_PLAYBOOK.md             how to answer questions correctly
│   ├── 01_SYSTEM/                       the notation reference
│   │   ├── A_HOW_TO_READ.md             ← the definitive reader's guide
│   │   ├── B_DEVICE_TAG_PREFIXES.md     every device class, with counts
│   │   ├── C_GLOSSARY_DE_EN.md          German↔English + printed titles
│   │   ├── D_DOCUMENT_MAP.md            what each volume covers
│   │   └── E_INDEX_SHEETS.md            contents/revision/option/legend sheets
│   ├── 02_SHEETS/
│   │   ├── _MASTER_TOC.md
│   │   └── <doc>/SHEET_NNNN.md          1,351 self-contained sheet files
│   └── 03_INDEX/
│       ├── INDEX_SECTIONS.md            section → sheet range
│       ├── INDEX_SHEETS.md              all 1,351 sheets
│       ├── INDEX_DEVICES.md             every designator → every sheet
│       ├── INDEX_NETS.md                every potential → where it appears
│       ├── DEVICES/CLASS_*.md           devices grouped by class
│       └── CATALOG.md
├── images/<doc>/<doc>_NNNN.png          1,351 renders @300 DPI (1-bit)
├── data/
│   ├── raw/<doc>/NNNN.json              lossless per-sheet extraction
│   ├── derived/graph.json               the knowledge graph
│   ├── derived/tables/*.json            reconstructed pin/terminal tables
│   └── exports/*.jsonl                  RAG-ready: sheets, chunks, devices, nets
├── pipeline/                            reproducible build
│   ├── build.py                         one-command orchestrator
│   ├── extract.py  tables.py  graph.py  mdgen.py  export.py  render.py
│   ├── schema.py   grammar.py           geometry + label grammar
│   ├── crop.py                          zoom into any region at 600 DPI
│   └── qa/                              verification harness
└── logs/                                build logs, render proof, QA report
```

---

## The three concepts an AI must know

**1. Location = document + sheet + column.**
Columns `A`–`H` are printed in the top and bottom margins, each ~140 pt wide.

**2. `/17.D` = "continues on sheet 17, column D of the same document."**
Each document is a closed set — cross-references never leave it. Follow it, then
confirm with the reciprocal reference on the target sheet.

**3. A wire-end annotation is a cluster read left→right:**
`destination` → `#line` → `/sheet.column`, e.g.

```
+A497/2 X1.A463:1     #67     /17.D
```

It may name several destinations at once. Do not read only the first token.

Full treatment in [`md/01_SYSTEM/A_HOW_TO_READ.md`](md/01_SYSTEM/A_HOW_TO_READ.md).

---

## Verification

Every claim below was measured, not estimated.

| Check | Result |
|---|---|
| Sheets processed | **1,351 / 1,351** (0 failures) |
| Labels extracted | **180,916** |
| **Label fidelity vs source PDF** | **180,916 / 180,916 — 0 missing (0.0000 %)** |
| Cross-references resolved | **34,890 / 34,890 — 0 unresolved** |
| Internal Markdown links | **101,052 / 101,052 — 0 broken** |
| Sheet renders | 1,351 @ 300 DPI, 1-bit, verified 0 missing / 0 corrupt |
| Render fidelity | solid-ink recall 1.000000; 0 thin-line gaps over 177,000 samples |
| Tables reconstructed | 1,114 sheets with rule-derived grids |
| RAG export | 1,351 sheet records, 9,536 chunks, 6,324 devices, 232 nets |

The fidelity check is end-to-end: for every sheet, every text object inside the
drawing area of the source PDF is compared **character-for-character** against
the generated Markdown.

---

## Reproducing the build

Python: the bundled runtime
`…\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe`
(dependencies: `pymupdf`, `Pillow`).

```powershell
cd Manroland_KnowledgeBase\pipeline
$py = "C:\Users\muham\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"

& $py build.py              # 1-5: extract, tables, graph, markdown, exports
& $py build.py --with-images # also re-render all 1,351 images (~70 s)
```

Individual stages: `extract.py` → `tables.py` → `graph.py` → `mdgen.py` →
`export.py` → `render.py`. Each is resumable and accepts `--only <doc>` /
`--force`.

### Verify the build

```powershell
& $py qa\qa_final.py          # 17 acceptance checks (coverage, fidelity, links)
& $py qa\qa_fidelity_full.py  # every label of every sheet vs the source PDF
& $py qa\qa_links.py          # every internal Markdown link
```

Design decisions worth knowing:

- **`extract.py` uses the PDF's native text blocks** as the semantic unit, because
  measurement showed a wire-end annotation is exactly one block.
- **`tables.py` rebuilds grids from the drawing's own rule lines** rather than
  guessing from text proximity — 327 Reference-module and 12 Terminal-strip
  sheets are pure pin tables and would otherwise be unreadable.
- **`render.py` chose 1-bit PNG @ 300 DPI** because stroke width is 0.85 pt on
  21,171 of 21,480 items (3.54 px at 300 DPI, so a hairline cannot vanish), and
  black line art carries no tonal information. ~3.5× smaller than grayscale at the
  identical pixel grid.

---

## Known limitations (also stated in the knowledge base)

- **The drawings document the series maximum equipment**, not the fitted
  configuration. The plans say so explicitly. Use the `INDEX` sheets and their
  `NUR BEI` / `ENTFÄLLT BEI` qualifiers to decide what is actually present.
- **`#NN` line numbers are rare** — only 7 of 1,351 sheets carry any. Position is
  given by sheet + column; do not invent a path number.
- **No functional descriptions, catalog part numbers, ratings, or behaviour** exist in these
  drawings. Do not infer what a device *does* beyond its printed caption.
- **Conductor colour/cross-section labels annotate the adjacent wire**, not the
  sheet. The per-sheet conductor tables are inventories, not a per-wire map.
- Cross-references with a `:pin` suffix name the far terminal; where none is
  printed, the drawing is silent about it.

---

## Source documents

| Document | File | Sheets | Code | Machine section |
|---|---|---:|---|---|
| `+FB` | `Cicuit Diagram +FB.pdf` *(sic)* | 22 | 8039G38K159 | Delivery / coating module |
| `+Ax` | `Circuit Diagram +Ax.pdf` | 403 | 8039G38I902 | Central control console |
| `+BA_Cx_DA` | `Circuit Diagram +BA, Cx, DA.pdf` | 247 | 8039G38J415 | Printing units / main switch cabinet |
| `+EA` | `Circuit Diagram +EA.pdf` | 407 | 8039G38E915 | Printing unit |
| `+FA` | `Circuit Diagram +FA.pdf` | 58 | 8039G38K212 | Delivery |
| `+Jx` | `Circuit Diagram +Jx.pdf` | 214 | 039G38F308 | 1st printing module + feed register |

Drawn by CIM-TEAM GmbH (2010–2012) for manroland.

<!-- AUTO-GENERATED:DO-NOT-EDIT-BY-HAND --> name=corpus-stats -->
| Quantity | Value |
|---|---:|
| Sheets | 1351 |
| Documents | 6 |
| Text labels extracted | 180916 |
| Cross-references | 34890 (0 unresolved) |
| Distinct device designators | 7361 (32555 occurrences) |
| Distinct potentials | 233 (4055 occurrences) |
| Distinct terminals | 637 |
<!-- /AUTO-GENERATED -->
