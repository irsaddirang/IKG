# A — How to read these wiring diagrams

**Audience:** an AI agent, an engineer, or a technician who must answer a question
about the manroland R700 printing press electrical system from this knowledge base.

**Status of this document:** every rule below was measured against the 1,351
source sheets. Where something is genuinely inconsistent in the drawings, that is
stated explicitly instead of being papered over. Nothing here is guessed.

---

## 1. What the source actually is

Six PDF files, 1,351 sheets total. They are **not scans**. Each sheet is a
vector drawing exported from a CIM-TEAM CAE system, with a real, selectable text
layer. Every label in this knowledge base was read from that text layer at its
exact coordinates — **no OCR was used anywhere**, because OCR measured only ~50 %
confidence on these dense sheets while the text layer is exact.

| Property | Measured value |
|---|---|
| Sheet size | 1190.55 × 841.89 pt = **DIN A3 landscape** |
| Page rotation | 0 (all pages portrait-in-landscape basis, i.e. never rotated) |
| Text per sheet | 42 – 2,900 characters, all real text |
| Vector paths per sheet | 260 – 1,942 |
| Line width | 0.85 pt for 21,171 of 21,480 drawing items |
| Ink | black on white only; one embedded raster (the manroland logo) |
| Embedded images | exactly 1 per sheet — the logo only. **No diagram content is raster.** |

> **Why this matters:** the precision of this knowledge base is the precision of
> the CAD export, not the precision of a vision model. Strings such as
> `+A497/2 X4.A463/1:4` are reproduced character-exact.

### The six documents

| Doc key | Source file | Sheets | Document code | Created | Covers |
|---|---|---:|---|---|---|
| `+FB` | `Cicuit Diagram +FB.pdf` *(sic — "Cicuit")* | 22 | `8039G38K159` | 08.12.2010 | Delivery / coating module |
| `+Ax` | `Circuit Diagram +Ax.pdf` | 403 | `8039G38I902` | 17.05.2010 | Central control console |
| `+BA_Cx_DA` | `Circuit Diagram +BA, Cx, DA.pdf` | 247 | `8039G38J415` | 28.06.2010 | Printing units / main switch cabinet |
| `+EA` | `Circuit Diagram +EA.pdf` | 407 | `8039G38E915` | 25.03.2010 | Printing unit |
| `+FA` | `Circuit Diagram +FA.pdf` | 58 | `8039G38K212` | 17.01.2011 | Delivery |
| `+Jx` | `Circuit Diagram +Jx.pdf` | 214 | `039G38F308` | 03.01.2010 | 1st printing module + feed register |

**Each document is self-contained.** A cross-reference `/17.D` always means
*sheet 17 of the same document* — never sheet 17 of a different file. The
cross-reference resolver in this knowledge base enforces exactly that, and all
**34,890** cross-references resolve to an existing sheet.

---

## 2. The coordinate system: three axes

To name any location in the drawing you need three things. All three are present
on every sheet.

```
┌────────────────────────────────────────────────────────────┐
│  A    B    C    D    E    F    G    H     ← column letters │
│ ┌────┬────┬────┬────┬────┬────┬────┬────┐                  │
│ │    │    │    │    │    │    │    │    │                  │
│ │    │    │    │    │    │    │    │    │                  │
│ └────┴────┴────┴────┴────┴────┴────┴────┘                  │
│  A    B    C    D    E    F    G    H     ← repeated below │
│ ┌────────────────────────────────────────────────────────┐ │
│ │  title block: document, sheet, section, date, codes    │ │
│ └────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

### 2.1 Sheet number
The sheet you are looking at, e.g. **sheet 21 of 403**. Printed in the title
block as `Blatt: 21 – 403`.

### 2.2 Column letter A–H
Eight DIN columns across the width. Measured centres: x ≈ 128.9, 269.5, 411.2,
552.9, 694.6, 836.1, 978.1, 1120.1 pt, so each band is ~140 pt wide. The letters
are printed in the top margin (y ≈ 2.8–14.9 pt) **and** repeated in the bottom
margin (y ≈ 829.8 pt).

Every label in this knowledge base carries its column, computed from its own
x-coordinate. So "column D" is not a guess — it is arithmetic on the measured
label position.

### 2.3 Path / line number `#NN`
A `#`-prefixed number such as `#67`. **Important, measured fact:** these are
*rare*. Only **7 of the 1,351 sheets** carry any `#NN` label, and only **28 of
34,890** cross-references are accompanied by one. They appear exclusively on
sheets that have a dense wire-fan ("Spannungsversorgung" / option wiring sections
of `+FB` and `+FA`).

> **Do not claim `#NN` is a general coordinate.** On the overwhelming majority
> of sheets the position of a wire is given by **sheet + column** only, and the
> fine position by the *annotation cluster* it belongs to (see §4).

The observed values live in the range 51–287.

---

## 3. Cross-references: `/sheet.column`

A label of the form

```
/17.D
```

means: **this wire continues on sheet 17, column D of the same document.** That
is the whole convention. It is the single most important navigation primitive in
these drawings, and it is how IEC multi-sheet schematics express a wire leaving
the page.

Reading order of a cross-reference:

1. Take the sheet number before the dot.
2. Take the column letter after the dot.
3. Go to that sheet, find that column, and look for the **reciprocal**
   cross-reference pointing back at you.

**Reciprocity is the ground truth.** If sheet 9 column F says `/17.D`, then on
sheet 17 in column D there is a wire end whose annotation points back to sheet 9.
This knowledge base records both directions: every sheet page lists
*Cross-references on this sheet* (outgoing) and *Incoming references* (who points
here). A wire is fully traced when you have walked both ends.

Some cross-references carry an extra `:pin` suffix, e.g. `/14.C:12`. When
present, it names the terminal/pin at the far end.

---

## 4. The wire-end annotation cluster

This is the structure that makes the drawings readable, and the one an AI is most
likely to mis-parse. A wire that leaves a sheet carries a small **horizontal
cluster** of labels, laid out left-to-right on one visual row:

```
   +A497/2 X1.A463:1      #67        /17.D
   └──────┬─────────┘   └──┬──┘    └──┬──┘
   where it goes        line no.   destination
   (what is on the      (optional,  (sheet 17,
    far end)             rare)       column D)
```

Real examples, verbatim from `+FB` sheet 9 (their exact y is given so you can
locate them visually on the sheet image):

| y (pt) | col | Cluster as printed |
|---:|---|---|
| 335.8 | F | `+ A497/2 X1.A463:1` `#67` `/17.D` |
| 358.5 | F | `+A497/2 X4.A463/1:4` `#67` `/17.E` |
| 381.2 | F | `X1.A368:2` `#67` `/12.C` |
| 403.9 | F | `A244:bn` `#67` `/13.G` |
| 449.2 | C | `+A497/2 K160/1:A2, +A497/2 K160:A2` `#65` `/13.E` |

**Rules that follow from this:**

- The three parts belong together *even though they are separate text objects*.
  They share a baseline and sit within ~100 pt of each other horizontally.
- The destination description comes **first** (leftmost), the cross-reference
  **last** (rightmost). On a right-hand column the cluster may be right-aligned,
  so the cross-reference sits at the column edge.
- A cluster may name **several** destinations at once — comma-separated, e.g.
  `+A497/2 K160/1:A2, +A497/2 K160:A2`. That means the one wire feeds several
  contacts. Do not read only the first.
- Some clusters carry no cross-reference: they annotate a wire that stays on the
  sheet (e.g. a colour/section spec).

In this knowledge base each cluster is preserved as one **annotation** record
with its own bounding box and column, and is reproduced in the sheet file under
*Wire-end annotations (grouped as printed)*.

---

## 5. Device designators

### 5.1 Grammar

```
  +A497/2         +   A   497   /2        sign, class letter, number, sub-unit
  -X3.A497            X   3     .A497     sign, class, number, mounting location
  -X1.A368:1          X   1     .A368 :1  ... and terminal/pin 1
  A244:bn             A   244   :bn       terminal letter (not a digit)
  X001                X   001             terminal strip
```

| Part | Meaning |
|---|---|
| leading `+` | the device/module is **in** this drawing set (a main item, e.g. `+A497` = a PC board assembly) |
| leading `-` | the item is referenced as a **component within** an assembly (e.g. `-X3` a plug on `+A497`) |
| class letter | device class (see table below) |
| number | unique number within that class |
| `/n` | sub-unit / partial device — the nth part of a multi-part device |
| `.Axxx` | **mounting location**: which assembly it sits on |
| `:n` or `:xy` | **terminal / pin** on that device |

Measured form distribution across all 6,117 distinct designators:

| Form | Count | Example |
|---|---:|---|
| `CLASS` + number | 3,613 | `K001`, `X001`, `W5106` |
| `CLASS:Pin` | 2,060 | `X001:1`, `M102/1:U` |
| `CLASS/Sub` | 324 | `+A497/2`, `B007/1` |
| `CLASS/Sub:Pin` | 120 | `M102/1:U` |

### 5.2 Class letters (IEC 81346 / DIN 40719)

Present in these documents, with measured counts:

| Letter | Meaning | Count | Example tags |
|---|---|---:|---|
| `A` | assembly / module / PC board | 483 | `+A457`, `+A497/1`, `A016` |
| `B` | transducer / sensor | 156 | `B001`, `B009/01` |
| `D` | binary / digital element | 5 | `D001`, `D1` |
| `E` | miscellaneous | 13 | `E000`, `E057` |
| `F` | protection (fuse, breaker) | 128 | `F002`, `F029/1` |
| `G` | power supply | 136 | `G000`, `G006:A1` |
| `H` | indicator / signal lamp | 9 | `H240/01` |
| `J` | connector / jumper | 37 | `J1`, `J31` |
| `K` | relay / contactor | 225 | `K001`, `K004:21` |
| `M` | motor | 21 | `M102/1:U` |
| `N` | power unit / amplifier | 1 | `N230` |
| `P` | measuring instrument | 6 | `P001` |
| `Q` | power switching device | 141 | `Q001`, `Q027:14` |
| `R` | resistor | 18 | `R035`, `R201/2` |
| `S` | switch | 224 | `S000` … `S012` |
| `T` | transformer | 3 | `T011`, `T011/1` |
| `U` | frequency converter / converter | 33 | `U101:7`, `U002` |
| `V` | diode / semiconductor | 21 | `V002`, `V400` |
| `W` | cable / line | 107 | `W1751`, `W2454` |
| `X` | terminal / plug connector | 309 | `X001`, `XB11`, `XA028:L1` |
| `Y` | solenoid valve / actuator | 128 | `Y001`, `Y011/1` |
| `Z` | miscellaneous / options | 9 | `Z002`, `Z012:L1` |

Composite terminal classes also occur: `XA` (mains terminals, `XA028:L1/L2/L3`),
`XB` (`XB11`), `XG` (`XG053:14`), `XU` (`XU101:1`).

See **B_DEVICE_TAG_PREFIXES.md** for the full enumeration with counts and examples.

---

## 6. Potentials (nets)

A potential name is a **node name**. Everything carrying the same potential name
is electrically common, wherever it appears.

Measured vocabulary and frequency (top entries). This table is **generated** from
`data/derived/graph.json` by `pipeline/sync_docs.py`, so it can never drift out of
step with `03_INDEX/INDEX_NETS.md`:

<!-- AUTO-GENERATED:DO-NOT-EDIT-BY-HAND -->
<!-- AUTO-GENERATED name=A-section6-nets -->
| Potential | Occurrences | Sheets | Meaning |
|---|---:|---:|---|
| `24V` | 1327 | 447 | +24 V DC control supply |
| `0V` | 1231 | 401 | 0 V reference / DC return |
| `L1` | 201 | 73 | mains phase L1 |
| `L2` | 187 | 69 | mains phase L2 |
| `PE` | 187 | 49 | protective earth |
| `L3` | 158 | 63 | mains phase L3 |
| `L24` | 42 | 13 | 24 V lamp supply |
| `M24+` | 40 | 11 | 24 V motor / signal rail |
| `M501` | 40 | 20 | motor / drive potential |
| `N` | 39 | 15 | mains neutral |
| `L230` | 24 | 11 | 230 V phase |
<!-- /AUTO-GENERATED -->

### The `+` / `-` / `/n` suffixes

- `24V`, `0V`, `L1`, `N`, `PE` — plain rail names.
- `L24+/4`, `M24+` — the trailing `/n` indexes **which conductor / which segment**
  of that rail (e.g. the 4th conductor of the L24 rail). It does **not** mean
  "4 volts" and it is not a division.
- `M24+` and `M501`, `H451` etc. are **named rails**, not arithmetic.

### Dotted reference chains

A potential label can be appended with the device chain it lands on:

```
24V.X001:15      -> potential 24V, at terminal 15 of X001
0V.X12.A343:1    -> potential 0V, at terminal 1 of A343, mounted on X12
X26.A342:1       -> no potential name; terminal 1 of A342 on X26
```

The first dotted atom is the potential (if it parses as one); the rest is a
descent path: **connector → assembly → pin**. Read it right-to-left to find the
physical point.

---

## 7. Conductor data on a wire

A wire is often annotated with two more labels, usually rotated 90° so they read
bottom-to-top along the wire:

```
   1.50 mm²        cross-section
   Blau            colour (German)
```

Measured vocabulary:

| German | Abbrev | English |
|---|---|---|
| Blau | BL | blue |
| Braun | BR | brown |
| Schwarz | SW | black |
| Rot | RT | red |
| Grau | GR | grey |
| Weiss | WS | white |
| Gelb | GE | yellow |
| Gruen / Grün | GN | green |
| Violett | VI | violet |
| Orange | OR | orange |
| Rosa | RS | pink |
| Tuerkis | TK | turquoise |
| GNG | GNG | green-yellow |
| WSBR | WSBR | white-brown |
| BRBL | BRBL | brown-blue |

Cross-sections observed are in mm² (e.g. `1.50 mm²`, `2,5 mm²` — note the German
decimal **comma** in some sheets, and the `mm2`/`mm²` spelling variance; all are
normalised to a numeric `mm2` value in the data).

**A caution:** cross-section and colour label the *wire next to them*. They are
not global sheet properties. Pairing them to a specific annotation is
positional — if a question demands "what gauge and colour is the wire between X
and Y", read it off the sheet image at the relevant location, and treat the
generated *Conductor specifications* table as an inventory, not as a per-wire
mapping.

---

## 8. The title block

Located at the bottom of every sheet (y ≈ 771.0 – 827.7 pt). Two layout
generations exist; both are handled.

| Field | German label | Content |
|---|---|---|
| Created | `erstellt am:` | date, `DD.MM.YY` or `DD.MM.YYYY` |
| Created by | `Name:` | initials / department, e.g. `JDes`, `EJEN/AES`, `SLEI/AES` |
| Modified | `geändert am:` | date; often `X` = none |
| Approved | `Freigabe:` | often `X` = none |
| Location | `Ort:` | machine section designator, e.g. `+FB`, `+Ax`, `+BA,Cx,DA` |
| Machine type | `Masch. Type:` | `R700` / `=R700` |
| Series | `Serie:` | `7758` or `7759` |
| Norm / frequency | `Norm/Frequenz:` | `B2_10: IEC/50Hz`, `B2_15: IEC/60Hz`, `B2_20: UL/cUL/60Hz` — **or**, on the later layout, `IEC (N)` / `UL (M)` |
| Sheet | `Blatt:` | `N – M`, i.e. this sheet of total |
| Replaces | `anstatt:` | the document code this sheet supersedes (80 sheets have one) |
| Paper | | `DIN A3` |
| Document code | | 9–11 char alphanumeric, e.g. `8039G38K159` |
| Drawing class | | `STROMLAUFPLAN` / `CIRCUIT DIAGRAM` |
| Section title | | German (line 1) + English (line 2) |

**The section title is the most useful metadata.** It tells you what the sheet is
about (`SPANNUNGSVERSORGUNG` / `VOLTAGE SUPPLY`, `KLEMMLEISTE` / `TERMINAL
STRIP`, `REFERENZMODUL` / `REFERENCE MODULE`, …). Every sheet file in this
knowledge base carries it in the YAML front matter, so it is filterable.

### 8.1 Order codes printed on the drawings — read this before answering "part number" questions

The title block carries **no** part numbers, manufacturer names or component
ratings. However, the drawings **do** print a small number of manroland
**order / manufacturing codes**, and they are easy to mistake for part numbers.
Measured shape: four digits, a capital letter, then five to nine further
alphanumerics, for example:

```
8037D44A002     8037B44A131     8237B447093     8098O442024     8337M518169
```

Measured extent: **19 distinct order codes, plus 5 distinct `noPart` markers,
44 printed tokens in total, on 8 of 1,351 sheets**, concentrated in the `+FB`
disposition plans (sheets 13, 14, 21, 22), with single occurrences on `+FB` 10,
`+FA` 2, `+JX` 4, `+EA` 4 and `+BA_Cx_DA` 4.

| What is established | What must NOT be assumed |
|---|---|
| The codes are printed text, verified at exact coordinates | that they are *order* numbers rather than drawing/assembly numbers |
| They sit in the device/connector annotation cluster or table cell | which single device a code belongs to when several share a cluster |
| Some connectors instead carry `Stecker_noPart…` — meaning **no orderable part** | any price, stock, supplier or alternative-part data |
| They are a *different* identifier from the document code in the title block | that a document code is a part number (it is the drawing set's ID) |

> **Rule for an AI reader.** You may report that a specific code is printed on a
> specific sheet at a specific position. You must **not** assert that a given
> device's part number *is* that code, because no drawing binds the two with a
> label or a leader line. The correct answer to *"what is the part number of
> K598?"* is: **not stated as such** — an order code `8037D44A002` is printed near
> K598 on `+FB` sheet 14, but nothing on the drawing declares it to be K598's
> part number. Quote the code and state the ambiguity; do not resolve it for the
> reader.

The `Stecker_noPart_*` markers are separately useful: they record that a connector
has **no orderable part number at all**.

---

## 9. Sheet types you will meet

| Sheet type | DE | Content |
|---|---|---|
| Contents | `INHALTSVERZEICHNIS` | table of contents, sheet ranges per topic |
| Revision index | `ÄNDERUNGSINDEX` | modification history |
| Machine diagram | `MASCHINENSCHEMA` | block layout of the press: feeder → printing units → coating → delivery, with which document covers which module |
| Disposition plan | `ANORDNUNGSPLAN` | physical arrangement / location of components |
| General indications | `ALLGEMEINE HINWEISE` | **legend and safety notes** — read this before interpreting symbols |
| Index | `INDEX` | option list; `X` = not fitted, blank/`NOT`-prefixed = variant-specific |
| Voltage supply | `SPANNUNGSVERSORGUNG` | incoming supply, distribution, cabinet ventilation |
| Earthing | `ERDUNG UND POTENTIALAUSGLEICH` | earth and potential equalisation |
| Terminal strip | `KLEMMLEISTE` | terminal-strip assignment table: terminal, wire, cross-ref, torque |
| Reference module | `REFERENZMODUL` | dense signal-level reference tables (PLC I/O style pin maps) |
| Option pages | `OPTION: …` | wiring for a specific machine option |
| Circuit pages | (section names vary) | the actual point-to-point wiring |

### Why "Reference module" sheets look different

On these sheets the content is a **table**, not a wire field. You will see long
runs like `16.0`, `16.1`, `16.2` … and `BYTE.BIT`, `PIN`, `INPUT`. These are
signal address / pin maps. They use the same sheet + column grid but their
content is tabular, so the column-letter bands are often only partly populated.
Their cross-references still follow the normal `/sheet.column` rule.

---

## 10. Reading procedure (the reliable algorithm)

To answer *any* question about a wire, follow this order:

1. **Locate the starting point** — search the device indexes
   (`03_INDEX/INDEX_DEVICES.md`) for the tag, e.g. `K598`.
2. **Open every sheet it appears on.** Each sheet file lists all devices,
   potentials, wire-end annotations and the exact label inventory.
3. **Find the wire-end annotation** that names your device and read its cluster:
   destination description → `#path` → `/sheet.column`.
4. **Follow the cross-reference** to the target sheet, and cross-check the
   *Incoming references* section there to confirm the wire really is the same
   one (the reciprocal `/sheet.column` should point back at you).
5. **Confirm on the image** if anything is ambiguous. Every sheet file embeds the
   300 DPI render of that exact sheet.
6. **For terminal-level questions**, use `03_INDEX/INDEX_NETS.md` for potentials
   and the per-sheet *Potentials / nets* table for which devices sit on a rail.

### Confidence discipline

- If the answer comes from the label inventory or a table in this knowledge base,
  the string is **exact** — quote it.
- If you inferred connectivity by *walking* several cross-references, say so and
  give the chain (e.g. `+FB#9 col F → /17.D → +FB#17 col D`).
- If the drawing does not state it (e.g. which physical terminal a wire lands on
  when no `:pin` is printed), **say it is not stated** rather than inventing it.

---

## 11. Common traps — avoid these

| Trap | Reality |
|---|---|
| Treating the six PDFs as one continuous 1,351-sheet drawing | They are **six independent drawing sets**. `/17.D` means sheet 17 *of that document*. |
| Assuming `#NN` path numbers are everywhere | They appear on **7 of 1,351 sheets** only. Default position is sheet + column. |
| Reading `/17.D` as a page in the PDF viewer | It is *sheet 17*, which equals page 17 only because sheet 1 = page 1 within a document. Cross-document navigation is the trap. |
| Parsing a wire cluster by taking the first token | The **destination is leftmost, the cross-ref is rightmost**; and a cluster may list **several** destinations. |
| Treating `L24+/4` as "24 V divided by 4" | `/4` indexes the *conductor/segment*, not a division. |
| Assuming a `-` sign means "negative" | `+`/`-` distinguish *main item in this set* vs *component of an assembly*. |
| Reading the colour/section labels as sheet-wide | They annotate the adjacent wire only. |
| Treating `X` in the Index sheet as an error | `X` is the CAE "not fitted / not present" marker. |
| Mixing German and English section names | Both are printed; they are the same section. This KB stores both. |
| Trusting a rendered image over the text layer | The text layer is exact; the render is for *visual confirmation of topology only*. |

---

## 12. What is exact here, and what is not

**Exact (text-layer derived):**
sheet numbers, columns, every device designator, every potential, every
cross-reference, every cross-section and colour word, title-block metadata,
section titles, document codes, and the full label inventory of every sheet.

**Derived/positional (high confidence, but positional):**
which labels form one annotation cluster, which devices are "on the same wire",
and conductor cross-section/colour pairing.

**Not contained in the source at all:**
functional descriptions of devices, catalog part numbers, ratings, cable
schedules beyond what is
printed, and any behaviour or timing. Do not answer those from this knowledge
base without flagging that the drawings do not state them.

---

_Every number in this document was measured from the source PDFs. Regenerate with
`pipeline/extract.py` → `pipeline/graph.py` → `pipeline/mdgen.py`._

<!-- AUTO-GENERATED:DO-NOT-EDIT-BY-HAND --> name=A-section6-nets -->
| Potential | Occurrences | Sheets | Meaning |
|---|---:|---:|---|
| `24V` | 1327 | 447 | +24 V DC control supply |
| `0V` | 1231 | 401 | 0 V reference / DC return |
| `L1` | 201 | 73 | mains phase L1 |
| `L2` | 187 | 69 | mains phase L2 |
| `PE` | 187 | 49 | protective earth |
| `L3` | 158 | 63 | mains phase L3 |
| `L24` | 42 | 13 | 24 V lamp supply |
| `M24+` | 40 | 11 | 24 V motor / signal rail |
| `M501` | 40 | 20 | motor / drive potential |
| `N` | 39 | 15 | mains neutral |
| `M24` | 35 | 9 | — |
| `L230` | 24 | 11 | 230 V phase |
<!-- /AUTO-GENERATED -->
