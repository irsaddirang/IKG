# 00 — READ ME FIRST

You are looking at a complete, machine-readable knowledge base of the electrical
wiring diagrams for the **manroland R700** sheet-fed offset printing press.

It was built from six PDF drawing sets totalling **1,351 DIN A3 sheets**, and it
exists so that an AI agent or an engineer can answer questions about the press
electrical system **accurately and with traceable evidence**.

---

## What is in here

| Path | What it is | Use it when |
|---|---|---|
| `01_SYSTEM/A_HOW_TO_READ.md` | **The reader's guide.** Coordinate system, cross-references, device grammar, nets, traps | Read this first, always |
| `01_SYSTEM/B_DEVICE_TAG_PREFIXES.md` | Every device class letter with counts and real examples | You see a tag and need to know what it is |
| `01_SYSTEM/C_GLOSSARY_DE_EN.md` | German ↔ English glossary + every section title as printed | Translating a question into drawing vocabulary |
| `01_SYSTEM/D_DOCUMENT_MAP.md` | What each document covers, sheet ranges, reading order | Deciding which volume to search |
| `01_SYSTEM/E_INDEX_SHEETS.md` | Contents / revision / option-index / legend sheets explained | Interpreting navigation sheets |
| `02_SHEETS/_MASTER_TOC.md` | All sections across all six documents | Orientation |
| `02_SHEETS/<doc>/_TOC.md` | Full sheet list for one document | Browsing a volume |
| `02_SHEETS/<doc>/SHEET_NNNN.md` | **One self-contained file per sheet** | The actual lookup |
| `03_INDEX/INDEX_SECTIONS.md` | Every section + sheet range | Finding a functional area |
| `03_INDEX/INDEX_SHEETS.md` | All 1,351 sheets in one table | Finding a specific sheet |
| `03_INDEX/INDEX_DEVICES.md` | Every device designator → every sheet it appears on | **Start here for a device question** |
| `03_INDEX/DEVICES/CLASS_*.md` | Devices grouped by class letter | Browsing a device category |
| `03_INDEX/INDEX_NETS.md` | Every potential (24V, 0V, L1, PE…) → where it appears | Power/rail questions |
| `images/<doc>/<doc>_NNNN.png` | 300 DPI exact render of every sheet | Visual confirmation |

Documents: `+FB` (22), `+Ax` (403), `+BA_Cx_DA` (247), `+EA` (407), `+FA` (58),
`+Jx` (214).

---

## What each sheet file contains

Every `SHEET_NNNN.md` is deliberately **self-contained**, so a retrieval step can
chunk on it without losing context. It contains, in order:

1. **YAML front matter** — document, sheet, section DE/EN, section code, machine
   type, series, date, image path, columns used. Filterable metadata.
2. **At a glance** — identity and counts.
3. **Navigation** — previous / next / document TOC / master TOC.
4. **Sheet image** — the 300 DPI render, embedded.
5. **Cross-references out** — every wire leaving the sheet, as `/sheet.column`,
   with the resolved target sheet, line number, destination text and target
   section title.
6. **Incoming references** — every other sheet that sends a wire here.
7. **Devices** — every designator with class, meaning, column, sub-unit, terminal.
8. **Potentials / nets** — rails present, how many times, which columns, which
   devices, which terminals.
9. **Conductor data** — cross-sections and wire colours present.
10. **Wire-end annotations** — the annotation clusters exactly as grouped on the
    drawing (destination + `#path` + `/xref`).
11. **Notes and free text.**
12. **Complete label inventory** — *every* text object on the sheet in DIN reading
    order (column A→H, top→bottom), with column, x, y, orientation, type and the
    exact string.
13. **Reading-order text block** — the same content as plain text per column.

Point 12 is the guarantee: **if a string is not in that table, it is not printed
on that sheet.** That is what lets you answer "what exactly does this sheet say?"
without re-reading the image.

---

## How this was built (and why you can trust it)

The source PDFs are **vector CAE exports**, not scans. Every label is real
selectable text at real coordinates. So:

- **No OCR was used.** OCR was measured at ~50 % confidence on these dense
  sheets. The text layer is exact.
- **No image transcription was used for labels.** The 300 DPI images exist for
  *visual confirmation of topology only*.
- Every cross-reference was **resolved and validated**: 34,890 of 34,890 resolve
  to an existing sheet in the correct document.
- Counts quoted throughout are measured, not estimated:

| Quantity | Value |
|---|---:|
| Sheets | 1,351 |
| Documents | 6 |
| Text labels extracted | 180,916 |
| Cross-references | 34,890 (0 unresolved) |
| Distinct device designators | 6,324 (26,126 occurrences) |
| Distinct potentials | 232 (3,566 occurrences) |
| Distinct terminals | 637 |
| Sheet renders | 1,351 at 300 DPI, 1-bit, ~94 MB total |

Regenerate everything with `pipeline/extract.py` → `pipeline/graph.py` →
`pipeline/mdgen.py` (and `pipeline/render.py` for images).

---

## The three things that make this readable

If you remember nothing else, remember these:

**1. Everything is addressed by sheet + column.**
A location is `+EA` sheet 137, column D. The DIN columns are `A`–`H`, printed in
the top and bottom margins, ~140 pt wide each.

**2. `/17.D` means "continues on sheet 17, column D of the same document".**
Each document is a closed set: cross-references never leave a document. Follow
the cross-reference, then check the reciprocal reference on the target sheet to
confirm you are on the same wire.

**3. A wire-end annotation is a cluster, not a single label.**
It reads left-to-right as **destination → `#line` → `/sheet.column`**, e.g.

```
+A497/2 X1.A463:1     #67     /17.D
```

and it may name several destinations at once. Do not read only the first token.

---

## Best practice when answering a question

1. **Start with the index, not the sheets.** Device question →
   `INDEX_DEVICES.md`. Functional question → `INDEX_SECTIONS.md`. Power question
   → `INDEX_NETS.md`.
2. **Open the sheet file(s) named by the index.**
3. **Quote exact strings** from the label inventory when you state what is
   printed.
4. **Give the chain** when you traced connectivity:
   `+FB#9 col F → /17.D → +FB#17 col D`.
5. **Say when the drawing is silent.** If no terminal is printed, or no
   cross-section is given, say so instead of inferring.
6. **Use the image** only to confirm topology or to resolve a genuinely ambiguous
   spatial question.

More on this in `00_QUERY_PLAYBOOK.md`.

---

## Important limitations — state these when relevant

- **The drawings show the series maximum equipment.** The disposition plans say
  so explicitly: *"THIS PLAN SHOWS THE MAX. EQUIPMENT OF THE SERIES. FOR THE
  ACTUAL EQUIPMENT, SEE THE CIRCUIT DIAGRAM."* A component appearing in the
  drawings is **not** proof it is fitted on a given machine. The `INDEX` sheets
  and their `NUR BEI` / `ENTFÄLLT BEI` qualifiers govern what is fitted.
- **No functional descriptions, catalog part numbers, ratings, or timing
  behaviour** are in these
  documents. They are wiring drawings. Do not invent device functions beyond what
  the German caption states.
- **`#NN` line numbers are rare** (7 sheets only). Do not treat them as a general
  coordinate.
- **Conductor colour/cross-section labels annotate the adjacent wire**, not the
  whole sheet. The per-sheet conductor tables are inventories, not a per-wire map.
- **Six documents, not one drawing.** The same device designator can exist in
  more than one volume. Always resolve a tag together with its document.

---

_Generated knowledge base. Source: `Diagram Manroland/` — six CIM-TEAM CAE
exports for the manroland R700 (document codes 8039G38K159, 8039G38I902,
8039G38J415, 8039G38E915, 8039G38K212, 039G38F308)._

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
