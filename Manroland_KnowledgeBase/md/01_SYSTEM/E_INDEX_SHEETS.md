# E — Navigation sheets: contents, revision index, index, accessories

Four kinds of sheet do not contain wiring. They are navigation and
configuration metadata, and they are the fastest way to find your way around.

---

## 1. `INHALTSVERZEICHNIS` / `CONTENTS` — table of contents

Present in every document (usually sheet 1, sometimes 1–2).

It lists, per topic, the **sheet range** and the German + English title. The
sheet files render this as a table, but the authoritative machine-readable form
is `03_INDEX/INDEX_SECTIONS.md`, which reconstructs the same spans from the
title block of every sheet (so it cannot drift out of sync).

**How the raw TOC sheet reads.** Each entry is a cluster like:

```
SPANNUNGSVERSORGUNG / KUNDENZULEITUNG        005  007
VOLTAGE SUPPLY / CUSTOMER SUPPLY CABLE
```

Reading rule: the two numbers at the end are the **first and last sheet** of
that section (here sheets 5–7). When only one number is given, the section is
a single sheet. The German line comes first, the English line under it.

> Careful: the numbers can appear **before or after** the title text in the
> extracted order, because the CAD exporter emits them as separate text
> objects. Prefer the generated section index over re-parsing the TOC sheet.

---

## 2. `ÄNDERUNGSINDEX` / `MODIFICATION INDEX` — revision index

Present where the document has revisions. It is a table with columns:

| Column | Meaning |
|---|---|
| `No:` | revision number |
| `Revision:` | revision letter/level |
| `Datum:` / `Date:` | date of the revision |
| `Name:` | who made it |

**Beware:** on many sheets this table is mostly rendered as `X` placeholders,
which is the CAE marker for an empty cell — **not** a data value. A sheet full
of `X` in the revision index means *no revisions recorded*, not *X revision*.

The reliable revision signal on any individual sheet is the title-block field
**`anstatt:` / replaces** — the document code that sheet supersedes. 80 sheets
across the set carry one; check the per-sheet *At a glance* table, row
**Replaces**.

---

## 3. `INDEX` — the machine option / equipment index

This is the most misunderstood sheet in the set. It lists the machine
**options** and, for each, which variant configuration includes it.

Typical columns: `No:`, `Option`, `Option / Beschreibung`, `Option / description`.

### What the marks mean

| Mark | Meaning |
|---|---|
| `X` | the option is **not fitted / not present** in this configuration |
| a text entry | the option applies, with the stated qualifier |
| blank cell | no statement for that configuration |

Entries can carry qualifiers such as:

- `NOT EL6_60` — not applicable for equipment variant EL6_60
- `ENTFÄLLT BEI: …` / `DELETED IN CASE OF: …` — the option is dropped when the
  named other option is present
- `NUR BEI …` / `ONLY FOR …` — only present on the named variant

The index is what tells you **whether a sheet applies to the machine you are
working on**. A wiring sheet for an option that the index marks `X` may be
printed in the document (the documents show the *series maximum equipment*,
see below) but may not exist physically on the machine.

> **Series-maximum warning.** The disposition plans state explicitly:
> *"DIESER PLAN STELLT DIE SERIENMAXIMALAUSSTATTUNG DAR. DIE TATSÄCHLICHE
> AUSSTATTUNG IST DEM STROMLAUFPLAN ZU ENTNEHMEN."* / *"THIS PLAN SHOWS THE
> MAX. EQUIPMENT OF THE SERIES. FOR THE ACTUAL EQUIPMENT, SEE THE CIRCUIT
> DIAGRAM."* — so a component appearing on a plan is not proof it is fitted.

---

## 4. `BEIPACK` / `ACCESSORIES` — loose parts pack

Lists the loose/accessory parts supplied with the machine (connectors,
terminals, spare links). It is a bill-of-material style sheet, not a wiring
sheet. Useful for identifying an unlabelled connector type.

---

## 5. `MASCHINENSCHEMA` / `MACHINE DIAGRAM` — the block diagram

Present in most documents (usually sheet 3). It shows the paper path and the
module blocks with arrows:

```
anleger  →  Druckwerk  →  Lackmodul  →  Ausleger
feeder   →  printing   →  coating    →  delivery
```

and annotates each block with which documentation covers it (`+JX`, `+EA`,
`+FB`, `+FA`, …). This is the single best sheet for answering *"which document
do I need?"*.

---

## 6. `ALLGEMEINE HINWEISE` / `GENERAL INDICATIONS` — the legend

The legend sheet defines the symbol vocabulary and prints the safety notes. It
is the reference for *how a contact, coil, fuse, motor, frequency converter is
drawn* in this particular set of drawings.

Safety notes printed on it (verbatim, bilingual) include:

- *"SCHALTEN SIE VOR ALLEN WARTUNGSARBEITEN DEN HAUPTSCHALTER DER MASCHINE
  UND ALLE WEITEREN HAUPTSCHALTER DER DRUCKANLAGE AUS UND SICHERN SIE IHN MIT
  EINEM VORHAENGESCHLOSS."* / *"BEFORE CARRYING OUT ANY MAINTENACE TASKS,
  TURN OFF THE MACHINE AT THE MAIN DISCONNECT SWITCH AND AT ALL OTHER MAIN
  DISCONNECT SWITCHES OF THE PRESS SYSTEM AND PADLOCK THEM."*
- *"NACH NETZABSCHALTUNG GEFAHR EINER MOEGLICHEN RESTSPANNUNG VON UEBER 60V AN
  DEN FREQUENZUMRICHTERN UND AN DEN ANGESCHLOSSENEN GERAETEN!"* / *"AFTER
  MAINS DISCONNECTION DANGER OF RESIDUAL VOLTAGE OF MORE THAN 60V AT THE
  FREQUENCY CONVERTERS AND ALL CONNECTED DEVICES."*
- *"BEACHTEN SIE DIE ENTLADEZEIT AM FREQUENZUMRICHTER!"* / *"OBSERVE THE
  DISCHARGING TIME ON THE FREQUENCY CONVERTER!"*

> These are **safety-critical**. If a user asks how to work on a circuit,
> quote the disconnection and residual-voltage warnings.

---

## 7. `ANORDNUNGSPLAN` / `DISPOSITION PLAN` — physical layout

Shows where components physically sit in/on the machine, with leader lines to
component tags. Unlike the wiring sheets it is **spatial**, not schematic.
Use it to answer *"where is `-A368` located?"* type questions — cross-checked
with the machine-diagram sheet.

---

## Summary: which sheet answers what

| Question | Sheet type |
|---|---|
| Which document covers the printing unit? | `MASCHINENSCHEMA` |
| What sheets cover emergency stop? | `INHALTSVERZEICHNIS` / `INDEX_SECTIONS` |
| Is this option fitted on my machine? | `INDEX` (+ `NUR BEI` / `ENTFÄLLT BEI` qualifiers) |
| What does this symbol mean? | `ALLGEMEINE HINWEISE` |
| Where is this component physically? | `ANORDNUNGSPLAN` |
| Which terminal does this wire land on? | `KLEMMLEISTE` |
| What PLC address is this signal? | `REFERENZMODUL` |
| How is this device wired? | the circuit sheets for its section |
