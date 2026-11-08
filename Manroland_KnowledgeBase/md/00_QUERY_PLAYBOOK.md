# 00 — Query playbook

How to get a **correct** answer out of this knowledge base, and how to tell the
difference between a fact the drawing states and something you inferred.

Read `01_SYSTEM/A_HOW_TO_READ.md` first if you do not know the notation.

---

## The one-minute orientation

- **6 documents**, **1,351 sheets**. Each document is a closed drawing set:
  a cross-reference never leaves its document.
- A location is **document + sheet + column** (`+EA` sheet 137, column D).
- `/17.D` = "continues on sheet 17, column D of the same document".
- A wire-end annotation is a **cluster**: destination → `#line` → `/sheet.column`.
- Every sheet has a file `02_SHEETS/<doc>/SHEET_NNNN.md` that contains **every
  label on that sheet**, verbatim, in reading order.

---

## Decision tree: which file do I open?

```
Question about a DEVICE (e.g. "where is K598?")
   └─> 03_INDEX/INDEX_DEVICES.md        (tag -> every sheet)
        └─> the sheet file(s) it names

Question about a FUNCTION / AREA (e.g. "emergency stop", "voltage supply")
   └─> 03_INDEX/INDEX_SECTIONS.md       (section title -> sheet range)
        └─> the sheet files in that range

Question about a POTENTIAL / RAIL (e.g. "24V", "0V", "PE")
   └─> 03_INDEX/INDEX_NETS.md

Question about WHICH DOCUMENT covers a module
   └─> 01_SYSTEM/D_DOCUMENT_MAP.md

Question about WHAT A SYMBOL / TAG MEANS
   └─> 01_SYSTEM/B_DEVICE_TAG_PREFIXES.md
   └─> 01_SYSTEM/C_GLOSSARY_DE_EN.md

Question about a SPECIFIC SHEET
   └─> 02_SHEETS/<doc>/SHEET_NNNN.md

Question "is this option fitted?"
   └─> the INDEX sheet of that document  (see 01_SYSTEM/E_INDEX_SHEETS.md)
```

---

## Worked example A — "What is connected to relay K598?"

1. **Index first.** Look up `K598` in `03_INDEX/INDEX_DEVICES.md`. It gives every
   document+sheet where `K598` occurs.
2. **Open the sheet.** In `+FB` sheet 9 the wire-end annotation reads:

   ```
   +A497/1 K598:A2   #65   /14.F
   ```

   That is: the wire from `K598` terminal `A2` continues on **sheet 14, column F**.
3. **Follow it.** Open `02_SHEETS/FB/SHEET_0014.md` and check its *Incoming
   references* table — it should list `+FB#9`, column `C`, back-ref `/9.C`.
4. **Report with the chain:**

   > `K598` (relay, in `+FB`) terminal `A2` connects via line `#65` to sheet 14
   > column F of the same document (`/14.F`). Chain: `+FB#9 col C → /14.F →
   > +FB#14 col F`.

That chain is the answer, and it is auditable.

---

## Worked example B — "Which sheets cover the voltage supply?"

1. Open `03_INDEX/INDEX_SECTIONS.md`.
2. Filter the `Section (EN)` column for `VOLTAGE SUPPLY`.
3. You get every span in every document, e.g. `+FB` sheets 9, `+Ax` 5–7,
   `+EA` 6–7, and the option pages.
4. Then browse `02_SHEETS/<doc>/SHEET_NNNN.md` for the detail.

---

## Worked example C — "Is the ColorPilot fitted?"

1. Open the `INDEX` sheet of the relevant document (see
   `01_SYSTEM/E_INDEX_SHEETS.md`).
2. Read the option row. `X` = **not fitted**. A text entry = applies, subject to
   its `NUR BEI …` / `ENTFÄLLT BEI …` qualifier.
3. **Also state the series-maximum caveat**: the plans document the maximum
   series equipment, and the drawings explicitly say the actual equipment must be
   taken from the circuit diagram. So the drawing's existence of ColorPilot wiring
   is not proof of fitment.

---

## Answer quality rules

### Always
- **Quote exact strings** from the label inventory when saying what is printed.
- **Cite the sheet** as `+FB` sheet 9 (or `+FB#9`), and the column.
- **Show the cross-reference chain** when you traced connectivity.
- **Distinguish** "printed on the drawing" from "inferred by tracing".

### Never
- Never invent a terminal number, cross-section, or colour that is not printed.
- Never merge two documents into one address space.
- Never claim a `#NN` line number exists where none is printed (only 7 sheets
  have them).
- Never present a conductor colour/section as belonging to a specific wire unless
  you read it positionally off the sheet image.
- Never answer functional/behavioural questions ("what does this relay do?") from
  these documents — they are wiring drawings. Say the documents do not state it.

### When the drawing is silent
Say so plainly, e.g.:

> Sheet `+FB` 9 annotates the wire `+A497/1 K598:A2` with cross-reference
> `/14.F` but prints no terminal at the far end, so the target terminal is not
> stated on this sheet.

---

## Handling the four common ambiguity traps

| Situation | Correct handling |
|---|---|
| A cluster names **several** destinations (`+A497/2 K160/1:A2, +A497/2 K160:A2`) | Report **all** of them; the single wire feeds several contacts. |
| A tag appears in **more than one document** | Resolve it per document. Never assume the same physical device. |
| The same **column letter** appears twice (top and bottom margin) | It is the same column; the letter is repeated for convenience. |
| An `X` mark appears where you expected data | It is the CAE "not fitted / empty" marker, not a value. |

---

## What this knowledge base can and cannot answer

**Can answer (with high confidence):**
- Where a device appears, on which sheets and columns.
- What a specific sheet prints, verbatim.
- Which sheet a wire continues to, and the reverse.
- Which potentials exist, and which sheets/devices they touch.
- What each document and section covers.
- What the legend, machine diagram, terminal strip and reference module say.

**Cannot answer (not in the source):**
- Device function or behaviour beyond the printed German/English caption.
- Catalog part numbers, ratings, supplier data, physical dimensions.
  (Order codes *are* printed on 9 sheets — see A_HOW_TO_READ §8.1.)
- Wire routing through cable ducts, or harness construction.
- PLC program logic.
- Anything about a machine's *actual* fitted equipment without the option index.

State this limitation rather than guessing.

---

## Fast keyword lookup tips

The drawings use German. If a search returns nothing, try the German term from
`01_SYSTEM/C_GLOSSARY_DE_EN.md`:

| English | German to search |
|---|---|
| feeder | `ANLEGER` |
| delivery | `AUSLEGER` |
| printing unit | `DRUCKWERK` |
| voltage supply | `SPANNUNGSVERSORGUNG` |
| terminal strip | `KLEMMLEISTE` |
| emergency stop | `NOT AUS` |
| relay | `RELAIS` / `RELAY` |
| solenoid valve | `MAGNETVENTIL` |
| limit switch | `ENDSCHALTER` |
| motor protection switch | `MOTORSCHUTZSCHALTER` |
| earthing | `ERDUNG` |
| general indications (legend) | `ALLGEMEINE HINWEISE` |

Note the drawings use `UE`/`OE`/`AE` transliteration in some all-caps notes
(`GEFAHR`, `MOEGLICHEN`, `UEBER`) while section titles use real umlauts
(`SPANNUNGSVERSORGUNG`, `ERDUNG`). Search for the stem, not the diacritic.
