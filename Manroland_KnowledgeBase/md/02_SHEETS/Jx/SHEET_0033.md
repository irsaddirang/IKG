---
doc: "+Jx"
sheet: 33
sheet_total: 214
document_code: "039G38F308"
section_de: "NOT AUS"
section_en: "EMERGENCY STOP"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "03.01.10"
image: "../../../images/+Jx/Jx_0033.png"
columns: "A-B-C-D-E-F-G-H"
---

# +Jx — Sheet 33 of 214 — NOT AUS

**EMERGENCY STOP**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+Jx` covers the **1st printing module + feed register** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+Jx`  (039G38F308) |
| Sheet | **33** of 214 |
| Section (DE) | NOT AUS |
| Section (EN) | EMERGENCY STOP |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 03.01.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G, H |
| Path numbers | — |
| Labels on sheet | 93 |
| Cross-refs out | 7 |
| Cross-refs in | 27 |

**Previous:** [+Jx sheet 32](SHEET_0032.md) · **Next:** [+Jx sheet 34](SHEET_0034.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+Jx) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+Jx sheet 33](../../../images/+Jx/Jx_0033.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/111.B` | [+Jx sheet 111](SHEET_0111.md) | B | — | A597 | REFERENZMODUL | C |
| `/111.D` | [+Jx sheet 111](SHEET_0111.md) | D | — | A598 | REFERENZMODUL | E |
| `/111.G` | [+Jx sheet 111](SHEET_0111.md) | G | — | — | REFERENZMODUL | F |
| `/11.E` | [+Jx sheet 11](SHEET_0011.md) | E | — | 24V.X29.A710:43 X28.A710:4 | SPANNUNGSVERSORGUNG, SCHALTSCHRANKBELÜFTUNG | D |
| `/34.F` | [+Jx sheet 34](SHEET_0034.md) | F | — | — | NOT AUS | H |
| `/34.D` | [+Jx sheet 34](SHEET_0034.md) | D | — | — | NOT AUS | A |
| `/30.D` | [+Jx sheet 30](SHEET_0030.md) | D | — | — | LACKNIVEAUÜBERWACHUNG | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+Jx#11](SHEET_0011.md) | E | `/11.E` | — | 1 | — |
| [+Jx#30](SHEET_0030.md) | D | `/30.D` | — | 1 | — |
| [+Jx#34](SHEET_0034.md) | D, E | `/34.D`, `/34.E` | — | 2 | X28.A710:4 |
| [+Jx#111](SHEET_0111.md) | B, D, F | `/111.B`, `/111.D`, `/111.F` | — | 3 | — |
| [+Jx#133](SHEET_0133.md) | C | `/133.C` | — | 4 | — |
| [+Jx#141](SHEET_0141.md) | C, H | `/141.C`, `/141.H` | — | 6 | — |
| [+Jx#142](SHEET_0142.md) | B, C | `/142.B`, `/142.C` | — | 4 | — |
| [+Jx#147](SHEET_0147.md) | C | `/147.C` | — | 6 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `S000` | S | Schalter / switch | C | — | — | — |
| `A597` | A | Baugruppe / assembly, module, PC board | C | — | — | — |
| `S000` | S | Schalter / switch | E | — | — | — |
| `A598` | A | Baugruppe / assembly, module, PC board | E | — | — | — |
| `S000` | S | Schalter / switch | F | — | — | — |
| `A609` | A | Baugruppe / assembly, module, PC board | F | — | — | — |
| `A710` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `X7.A597` | — | cross-device reference | C | — | — | — |
| `X7.A597` | — | cross-device reference | C | — | — | — |
| `X7.A598` | — | cross-device reference | E | — | — | — |
| `X7.A598` | — | cross-device reference | E | — | — | — |
| `NR.` | — | cross-device reference | F | — | — | — |
| `23.08.10` | — | cross-device reference | G | — | — | — |
| `X19.A573.B` | — | cross-device reference | F | — | — | — |
| `X19.A573.A` | — | cross-device reference | F | — | — | — |
| `X21.A710` | — | cross-device reference | B | — | — | — |
| `X29.A710` | — | cross-device reference | A | — | — | — |
| `X22.A710` | — | cross-device reference | D | — | — | — |
| `X29.A710` | — | cross-device reference | E | — | — | — |
| `X23.A710` | — | cross-device reference | F | — | — | — |
| `X29.A710` | — | cross-device reference | G | — | — | — |
| `X29.A710` | — | cross-device reference | C | — | — | — |
| `X28.A710:4` | — | cross-device reference | H | — | 4 | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `24V` | 1 | A | `A710`, `X29` | `43` |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| C | 61.2 | — | — | `X7.A597 1` |
| E | 61.2 | — | — | `X7.A598 1` |
| C | 79.6 | — | — | `1` |
| E | 79.6 | — | — | `1` |
| F | 79.6 | — | — | `+JA A609` |
| C | 82.4 | — | `/111.B` | `A597` |
| E | 82.4 | — | `/111.D` | `A598` |
| G | 82.5 | — | — | `11` |
| F | 108.7 | — | `/111.G` | — |
| C | 112.7 | — | — | `S000` |
| E | 112.7 | — | — | `S000` |
| F | 119.7 | — | — | `S000` |
| D | 185.3 | — | — | `S S` |
| F | 185.3 | — | — | `S` |
| G | 205.8 | — | — | `12` |
| C | 208.6 | — | — | `2` |
| E | 208.6 | — | — | `2` |
| C | 224.2 | — | — | `X7.A597 2` |
| E | 224.2 | — | — | `X7.A598 2` |
| F | 263.9 | — | — | `X19.A573.A 11` |
| F | 276.5 | — | — | `+JA` |
| G | 279.5 | — | — | `12` |
| F | 296.5 | — | — | `X19.A573.B 11` |
| G | 296.5 | — | — | `12` |
| F | 312.0 | — | — | `+JA` |
| G | 314.9 | — | — | `2` |
| D | 337.6 | — | `/11.E` | `24V.X29.A710:43 X28.A710:4` |
| H | 347.4 | — | `/34.F` | — |
| F | 385.3 | — | — | `1` |
| C | 401.3 | — | — | `X29.A710 43 X21.A710 1 2 X22.A710 1` |
| E | 401.3 | — | — | `X29.A710 44 46 X23.A710 1 2 X29.A710 50` |
| E | 402.8 | — | — | `2` |
| A | 455.2 | — | — | `A710` |
| A | 468.3 | — | `/34.D`, `/30.D` | — |
| E | 507.6 | — | — | `X29.A710 47` |
| F | 509.1 | — | — | `49` |
| C | 655.4 | — | — | `DRUCKWERK: B SEITE KEY: EMERGENCY STOP PRINTING UNIT: B SIDE TASTE: NOT AUS` |
| E | 655.4 | — | — | `DRUCKWERK: A SEITE KEY: EMERGENCY STOP PRINTING UNIT: A SIDE TASTE: NOT AUS` |
| F | 655.5 | — | — | `KEY EMERGENCY STOP TASTE NOT AUS` |
| A | 697.9 | — | — | `2 NUR BEI ONLY FOR` |
| A | 697.9 | — | — | `LTL LTTL +JA` |
| G | 733.0 | — | — | `001 23.08.10 SLEI/SCH HINWEIS 1 UND 2 HINZU` |
| A | 733.3 | — | — | `1 ENTFÄLLT BEI DELETED IN CASE OF` |
| B | 733.3 | — | — | `LTL LTTL +JA` |
| G | 747.1 | — | — | `NR. TAG NAME ÄNDERUNG` |


## Reconstructed tables

This sheet carries tabular content (pin map / terminal assignment / index). The grid below was rebuilt from the drawing's own rule lines, so each row is exactly one physical row of the table.

### Table 1 — 4 data rows × 16 columns (at x=226.8, y=34.0)

|  |  | X7.A597 | 1 |  |  |  |  | X7.A598 | 1 |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | `A597 /111.B S000 S` | `1 2` |  |  |  |  | `A598 /111.D S000 S` | `1 2` |  |  |  | `A609 +JA /111.G S000 S` | `11 12` |  |
|  |  | `X7.A597` | `2` |  |  |  |  | `X7.A598` | `2` | `X19.A573.A X19.A573.B` | `+JA +JA` | `11 11` |  | `12 12` | `2` |
| `X21.A710 43` | `1` |  | `2` | `X29.A710` | `44` | `X22.A710 46` | `1` |  | `2` | `X23.A710` |  | `1` | `1` | `2` | `X29.A710` |
|  |  |  |  |  |  |  |  | `X29.A710` | `47` |  |  | `49` |  |  |  |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `TASTE NOT AUS` | F | 655.5 |
| `KEY EMERGENCY STOP` | F | 665.49 |
| `+JA` | F | 92.27 |
| `TAG` | G | 747.23 |
| `NAME` | G | 747.22 |
| `ÄNDERUNG` | G | 747.25 |
| `SLEI/SCH` | G | 733.08 |
| `HINWEIS 1 UND 2 HINZU` | H | 733.06 |
| `S` | C | 185.26 |
| `S` | E | 185.26 |
| `TASTE: NOT AUS` | E | 655.38 |
| `DRUCKWERK: A SEITE` | E | 665.98 |
| `KEY: EMERGENCY STOP` | E | 676.64 |
| `PRINTING UNIT: A SIDE` | E | 687.27 |
| `TASTE: NOT AUS` | C | 655.38 |
| `DRUCKWERK: B SEITE` | C | 665.98 |
| `KEY: EMERGENCY STOP` | C | 676.64 |
| `PRINTING UNIT: B SIDE` | C | 687.27 |
| `S` | F | 185.26 |
| `ENTFÄLLT BEI` | A | 733.3 |
| `DELETED IN CASE OF` | A | 743.96 |
| `LTL` | B | 733.3 |
| `LTTL` | B | 743.95 |
| `+JA` | B | 740.38 |
| `NUR BEI` | A | 697.86 |
| `ONLY FOR` | A | 708.55 |
| `LTL` | A | 697.87 |
| `LTTL` | A | 708.51 |
| `+JA` | A | 704.94 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 337.5 | 111.4 | → | potential | `24V.X29.A710:43` |
| A | 347.4 | 172.3 | → | cross-reference | `/11.E` |
| A | 401.3 | 170.1 | → | device ref | `X29.A710` |
| A | 455.2 | 149.4 | → | device tag | `A710` |
| A | 468.3 | 156.5 | → | cross-reference | `/34.D` |
| A | 480.7 | 156.5 | → | cross-reference | `/30.D` |
| A | 697.9 | 87.3 | → | text | `NUR BEI` |
| A | 697.9 | 137.6 | → | text | `LTL` |
| A | 703.2 | 75.1 | → | number | `2` |
| A | 704.9 | 166.3 | → | text | `+JA` |
| A | 708.5 | 87.6 | → | text | `ONLY FOR` |
| A | 708.5 | 137.6 | → | text | `LTTL` |
| A | 733.3 | 87.3 | → | text | `ENTFÄLLT BEI` |
| A | 738.6 | 75.4 | → | number | `1` |
| A | 744.0 | 87.3 | → | text | `DELETED IN CASE OF` |
| B | 401.3 | 269.3 | → | device ref | `X21.A710` |
| B | 402.8 | 229.6 | → | number | `43` |
| B | 402.8 | 328.0 | → | number | `1` |
| B | 733.3 | 194.3 | → | text | `LTL` |
| B | 740.4 | 222.9 | → | text | `+JA` |
| B | 743.9 | 194.3 | → | text | `LTTL` |
| C | 61.2 | 360.0 | → | device ref | `X7.A597` |
| C | 62.6 | 413.0 | → | number | `1` |
| C | 79.6 | 415.8 | → | number | `1` |
| C | 82.4 | 359.7 | → | device tag | `A597` |
| C | 96.2 | 360.0 | → | cross-reference | `/111.B` |
| C | 112.7 | 383.8 | → | device tag | `S000` |
| C | 185.3 | 378.6 | → | text | `S` |
| C | 208.6 | 416.7 | → | number | `2` |
| C | 224.2 | 361.4 | → | device ref | `X7.A597` |
| C | 225.6 | 413.9 | → | number | `2` |
| C | 401.3 | 453.5 | → | device ref | `X29.A710` |
| C | 402.8 | 413.9 | → | number | `2` |
| C | 655.4 | 354.3 | → | text | `TASTE: NOT AUS` |
| C | 666.0 | 353.8 | → | text | `DRUCKWERK: B SEITE` |
| C | 676.6 | 353.8 | → | text | `KEY: EMERGENCY STOP` |
| C | 687.3 | 353.8 | → | text | `PRINTING UNIT: B SIDE` |
| D | 401.3 | 595.3 | → | device ref | `X22.A710` |
| D | 402.8 | 513.1 | → | number | `44` |
| D | 402.8 | 555.6 | → | number | `46` |
| E | 61.2 | 686.3 | → | device ref | `X7.A598` |
| E | 62.6 | 739.0 | → | number | `1` |
| E | 79.6 | 741.8 | → | number | `1` |
| E | 82.4 | 685.7 | → | device tag | `A598` |
| E | 96.3 | 686.0 | → | cross-reference | `/111.D` |
| E | 112.7 | 709.8 | → | device tag | `S000` |
| E | 185.3 | 704.6 | → | text | `S` |
| E | 208.6 | 742.7 | → | number | `2` |
| E | 224.2 | 687.7 | → | device ref | `X7.A598` |
| E | 225.6 | 739.8 | → | number | `2` |
| E | 402.8 | 654.0 | → | number | `1` |
| E | 402.8 | 739.8 | → | number | `2` |
| E | 507.6 | 681.7 | → | device ref | `X29.A710` |
| E | 509.1 | 739.8 | → | number | `47` |
| E | 655.4 | 680.3 | → | text | `TASTE: NOT AUS` |
| E | 666.0 | 679.7 | → | text | `DRUCKWERK: A SEITE` |
| E | 676.6 | 679.7 | → | text | `KEY: EMERGENCY STOP` |
| E | 687.3 | 679.7 | → | text | `PRINTING UNIT: A SIDE` |
| F | 79.6 | 871.4 | → | device tag | `A609` |
| F | 92.3 | 871.1 | → | text | `+JA` |
| F | 108.6 | 871.7 | → | cross-reference | `/111.G` |
| F | 119.7 | 892.6 | → | device tag | `S000` |
| F | 185.3 | 881.7 | → | text | `S` |
| F | 263.9 | 769.0 | → | device ref | `X19.A573.A` |
| F | 276.5 | 810.4 | → | text | `+JA` |
| F | 279.5 | 838.2 | → | number | `11` |
| F | 296.5 | 838.2 | → | number | `11` |
| F | 299.3 | 769.6 | → | device ref | `X19.A573.B` |
| F | 312.0 | 810.4 | → | text | `+JA` |
| F | 385.3 | 876.9 | → | number | `1` |
| F | 401.3 | 779.5 | → | device ref | `X23.A710` |
| F | 402.8 | 838.2 | → | number | `1` |
| F | 509.1 | 839.1 | → | number | `49` |
| F | 655.5 | 864.3 | → | text | `TASTE NOT AUS` |
| F | 665.5 | 864.0 | → | text | `KEY EMERGENCY STOP` |
| F | 733.0 | 887.6 | → | number | `001` |
| F | 747.1 | 886.8 | → | device ref | `NR.` |
| G | 82.5 | 926.1 | → | number | `11` |
| G | 205.8 | 926.1 | → | number | `12` |
| G | 279.5 | 923.2 | → | number | `12` |
| G | 296.5 | 923.2 | → | number | `12` |
| G | 314.9 | 961.8 | → | number | `2` |
| G | 401.3 | 949.6 | → | device ref | `X29.A710` |
| G | 402.8 | 924.1 | → | number | `2` |
| G | 402.8 | 1008.9 | → | number | `50` |
| G | 733.1 | 921.9 | → | device ref | `23.08.10` |
| G | 733.1 | 976.3 | → | text | `SLEI/SCH` |
| G | 747.2 | 928.5 | → | text | `TAG` |
| G | 747.2 | 981.8 | → | text | `NAME` |
| G | 747.3 | 1024.0 | → | text | `ÄNDERUNG` |
| H | 337.6 | 1050.0 | → | device ref | `X28.A710:4` |
| H | 347.4 | 1040.3 | → | cross-reference | `/34.F` |
| H | 733.1 | 1023.4 | → | text | `HINWEIS 1 UND 2 HINZU` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
 337.5  111.4  net          24V.X29.A710:43
 347.4  172.3  xref         /11.E
 401.3  170.1  devref       X29.A710
 455.2  149.4  devtag       A710
 468.3  156.5  xref         /34.D
 480.7  156.5  xref         /30.D
 697.9   87.3  text         NUR BEI
 697.9  137.6  text         LTL
 703.2   75.1  numeric      2
 704.9  166.3  text         +JA
 708.5   87.6  text         ONLY FOR
 708.5  137.6  text         LTTL
 733.3   87.3  text         ENTFÄLLT BEI
 738.6   75.4  numeric      1
 744.0   87.3  text         DELETED IN CASE OF
=== Column B ===
 401.3  269.3  devref       X21.A710
 402.8  229.6  numeric      43
 402.8  328.0  numeric      1
 733.3  194.3  text         LTL
 740.4  222.9  text         +JA
 743.9  194.3  text         LTTL
=== Column C ===
  61.2  360.0  devref       X7.A597
  62.6  413.0  numeric      1
  79.6  415.8  numeric      1
  82.4  359.7  devtag       A597
  96.2  360.0  xref         /111.B
 112.7  383.8  devtag       S000
 185.3  378.6  text         S
 208.6  416.7  numeric      2
 224.2  361.4  devref       X7.A597
 225.6  413.9  numeric      2
 401.3  453.5  devref       X29.A710
 402.8  413.9  numeric      2
 655.4  354.3  text         TASTE: NOT AUS
 666.0  353.8  text         DRUCKWERK: B SEITE
 676.6  353.8  text         KEY: EMERGENCY STOP
 687.3  353.8  text         PRINTING UNIT: B SIDE
=== Column D ===
 401.3  595.3  devref       X22.A710
 402.8  513.1  numeric      44
 402.8  555.6  numeric      46
=== Column E ===
  61.2  686.3  devref       X7.A598
  62.6  739.0  numeric      1
  79.6  741.8  numeric      1
  82.4  685.7  devtag       A598
  96.3  686.0  xref         /111.D
 112.7  709.8  devtag       S000
 185.3  704.6  text         S
 208.6  742.7  numeric      2
 224.2  687.7  devref       X7.A598
 225.6  739.8  numeric      2
 402.8  654.0  numeric      1
 402.8  739.8  numeric      2
 507.6  681.7  devref       X29.A710
 509.1  739.8  numeric      47
 655.4  680.3  text         TASTE: NOT AUS
 666.0  679.7  text         DRUCKWERK: A SEITE
 676.6  679.7  text         KEY: EMERGENCY STOP
 687.3  679.7  text         PRINTING UNIT: A SIDE
=== Column F ===
  79.6  871.4  devtag       A609
  92.3  871.1  text         +JA
 108.6  871.7  xref         /111.G
 119.7  892.6  devtag       S000
 185.3  881.7  text         S
 263.9  769.0  devref       X19.A573.A
 276.5  810.4  text         +JA
 279.5  838.2  numeric      11
 296.5  838.2  numeric      11
 299.3  769.6  devref       X19.A573.B
 312.0  810.4  text         +JA
 385.3  876.9  numeric      1
 401.3  779.5  devref       X23.A710
 402.8  838.2  numeric      1
 509.1  839.1  numeric      49
 655.5  864.3  text         TASTE NOT AUS
 665.5  864.0  text         KEY EMERGENCY STOP
 733.0  887.6  numeric      001
 747.1  886.8  devref       NR.
=== Column G ===
  82.5  926.1  numeric      11
 205.8  926.1  numeric      12
 279.5  923.2  numeric      12
 296.5  923.2  numeric      12
 314.9  961.8  numeric      2
 401.3  949.6  devref       X29.A710
 402.8  924.1  numeric      2
 402.8 1008.9  numeric      50
 733.1  921.9  devref       23.08.10
 733.1  976.3  text         SLEI/SCH
 747.2  928.5  text         TAG
 747.2  981.8  text         NAME
 747.3 1024.0  text         ÄNDERUNG
=== Column H ===
 337.6 1050.0  devref       X28.A710:4
 347.4 1040.3  xref         /34.F
 733.1 1023.4  text         HINWEIS 1 UND 2 HINZU
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_JX_039G38F308_p`, sheet 33._
