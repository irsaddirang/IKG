---
doc: "+EA"
sheet: 323
sheet_total: 407
document_code: "8039G38E915"
section_de: "OPTION: VERLÄNGERUNG 3656,8MM"
section_en: "OPTION: EXTENSION 3656,8MM"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "25.03.10"
image: "../../../images/+EA/EA_0323.png"
columns: "A-B-C-D-E-F-G-H"
---

# +EA — Sheet 323 of 407 — OPTION: VERLÄNGERUNG 3656,8MM

**OPTION: EXTENSION 3656,8MM**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+EA` covers the **Printing unit** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+EA`  (8039G38E915) |
| Sheet | **323** of 407 |
| Section (DE) | OPTION: VERLÄNGERUNG 3656,8MM |
| Section (EN) | OPTION: EXTENSION 3656,8MM |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 25.03.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G, H |
| Path numbers | — |
| Labels on sheet | 101 |
| Cross-refs out | 9 |
| Cross-refs in | 32 |

**Previous:** [+EA sheet 322](SHEET_0322.md) · **Next:** [+EA sheet 324](SHEET_0324.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+EA) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+EA sheet 323](../../../images/+EA/EA_0323.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/198.H` | [+EA sheet 198](SHEET_0198.md) | H | — | — | REFERENZMODUL | D |
| `/198.H` | [+EA sheet 198](SHEET_0198.md) | H | — | — | REFERENZMODUL | F |
| `/198.H` | [+EA sheet 198](SHEET_0198.md) | H | — | — | REFERENZMODUL | G |
| `/320.F` | [+EA sheet 320](SHEET_0320.md) | F | — | X1.A649:6 | OPTION: VERLÄNGERUNG 3656,8MM | B |
| `/324.D` | [+EA sheet 324](SHEET_0324.md) | D | — | — | OPTION: VERLÄNGERUNG 3656,8MM | C |
| `/322.C` | [+EA sheet 322](SHEET_0322.md) | C | — | — | OPTION: VERLÄNGERUNG 3656,8MM | C |
| `/320.E` | [+EA sheet 320](SHEET_0320.md) | E | — | 24V.X1.A649:2 | OPTION: VERLÄNGERUNG 3656,8MM | B |
| `/320.E` | [+EA sheet 320](SHEET_0320.md) | E | — | 0V.X1.A649:1 | OPTION: VERLÄNGERUNG 3656,8MM | A |
| `/203.G` | [+EA sheet 203](SHEET_0203.md) | G | — | A649 | REFERENZMODUL | H |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+EA#198](SHEET_0198.md) | H | `/198.H` | — | 3 | — |
| [+EA#203](SHEET_0203.md) | G | `/203.G` | — | 1 | — |
| [+EA#208](SHEET_0208.md) | E | `/208.E` | — | 3 | — |
| [+EA#214](SHEET_0214.md) | A | `/214.A` | — | 6 | — |
| [+EA#220](SHEET_0220.md) | G | `/220.G` | — | 8 | — |
| [+EA#244](SHEET_0244.md) | E | `/244.E` | — | 3 | — |
| [+EA#252](SHEET_0252.md) | E | `/252.E` | — | 3 | — |
| [+EA#320](SHEET_0320.md) | E, F | `/320.E`, `/320.F` | — | 3 | 0V.X1.A649:1; X1.A649:6 |
| [+EA#322](SHEET_0322.md) | C | `/322.C` | — | 1 | — |
| [+EA#324](SHEET_0324.md) | C | `/324.C` | — | 1 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `A306` | A | Baugruppe / assembly, module, PC board | C | — | — | — |
| `A356/07` | A | Baugruppe / assembly, module, PC board | D | 07 | — | — |
| `A356/07` | A | Baugruppe / assembly, module, PC board | G | 07 | — | — |
| `A356/07` | A | Baugruppe / assembly, module, PC board | F | 07 | — | — |
| `A649` | A | Baugruppe / assembly, module, PC board | H | — | — | — |
| `A649` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `X1.A306` | — | cross-device reference | D | — | — | — |
| `XB9.A356` | — | cross-device reference | D | — | — | — |
| `X6.A306` | — | cross-device reference | D | — | — | — |
| `X1.A649` | — | cross-device reference | B | — | — | — |
| `X1.M501.A649.B` | — | cross-device reference | H | — | — | — |
| `X1.M501.A649.A` | — | cross-device reference | H | — | — | — |
| `X1.A649:6` | — | cross-device reference | B | — | 6 | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `0V` | 1 | A | `A649`, `X1` | `1` |
| `24V` | 1 | B | `A649`, `X1` | `2` |
| `M501` | 1 | H | — | — |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| D | 65.8 | — | — | `D/A` |
| E | 65.8 | — | — | `D/A` |
| G | 65.8 | — | — | `D/A` |
| A | 67.2 | — | — | `BOGENFÜHRUNGSELEMENT, SOLLWERT` |
| A | 72.6 | — | — | `A SHEET GUIDING ELEMENT, NOMINAL VALUE` |
| D | 79.7 | — | — | `A356/07` |
| F | 79.7 | — | — | `A356/07` |
| G | 79.7 | — | — | `A356/07` |
| D | 94.5 | — | `/198.H` | — |
| F | 94.5 | — | `/198.H` | — |
| G | 94.5 | — | `/198.H` | — |
| A | 95.6 | — | — | `BOGENFÜHRUNGSELEMENT, STÖRMELDESIGNAL` |
| A | 100.9 | — | — | `B SHEET GUIDING ELEMENT, TROUBLE MESSAGE SIGNAL` |
| D | 122.8 | — | — | `SOLLWERT 3` |
| E | 122.9 | — | — | `INPUT 3` |
| G | 122.9 | — | — | `OUTPUT 3` |
| A | 123.9 | — | — | `BOGENFÜHRUNGSELEMENT LINKS / RECHTS` |
| A | 129.3 | — | — | `C SHEET GUIDING ELEMENT LEFT / RIGHT` |
| D | 139.2 | — | — | `9B` |
| F | 139.2 | — | — | `10B` |
| G | 139.2 | — | — | `11B` |
| D | 153.4 | — | — | `XB9.A356 7` |
| F | 154.8 | — | — | `8` |
| G | 154.8 | — | — | `9` |
| D | 195.9 | — | — | `X1.A306 7` |
| F | 204.4 | — | — | `8 9` |
| B | 238.4 | — | `/320.F` | `X1.A649:6` |
| C | 242.7 | — | — | `A306` |
| C | 255.8 | — | `/324.D`, `/322.C` | — |
| B | 266.7 | — | `/320.E` | `24V.X1.A649:2` |
| E | 280.9 | — | — | `X6.A306 3 4 5` |
| A | 295.1 | — | `/320.E` | `0V.X1.A649:1` |
| H | 366.5 | — | — | `X1.M501.A649.B` |
| H | 367.4 | — | — | `X1.M501.A649.A` |
| H | 409.9 | — | — | `1` |
| H | 409.9 | — | — | `2 5 3` |
| B | 422.7 | — | — | `X1.A649 1` |
| H | 426.9 | — | — | `1` |
| H | 426.9 | — | — | `2 5 3` |
| E | 431.2 | — | — | `2 6 3 5 4` |
| F | 448.8 | — | — | `A B C` |
| A | 477.8 | — | — | `A649` |
| H | 492.0 | — | — | `+ B A` |
| H | 530.4 | — | `/203.G` | `A649` |
| H | 571.5 | — | — | `M` |
| D | 578.6 | — | — | `M` |
| H | 604.8 | — | — | `M501` |
| H | 630.6 | — | — | `LÜFTER: BOGENFÜHRUNG` |
| H | 651.9 | — | — | `SHEET GUIDING DEVICE VENTILATOR:` |
| A | 669.3 | — | — | `2` |
| H | 675.8 | — | — | `1` |
| B | 698.0 | — | — | `BOGENFÜHRUNGSELEMENT: VERLÄNGERUNG (3656,8MM)` |
| B | 708.6 | — | — | `SHEET GUIDING ELEMENT EXTENSION (3656,8MM)` |
| B | 733.2 | — | — | `1 PP S+W OPTION OPTION` |
| D | 733.2 | — | — | `PP S+W` |
| B | 733.4 | — | — | `EXTENSION VERLÄNGERUNG` |
| D | 733.4 | — | — | `2 ENTFÄLLT BEI DELETED IN CASE OF EXTENSION VERLÄNGERUNG` |
| D | 733.4 | — | — | `OPTION OPTION` |


## Reconstructed tables

This sheet carries tabular content (pin map / terminal assignment / index). The grid below was rebuilt from the drawing's own rule lines, so each row is exactly one physical row of the table.

### Table 1 — 4 data rows × 5 columns (at x=226.8, y=62.4)

| VALUE STÖRMELDESIGNAL MESSAGE SIGNAL |  |  | D/A | A356/07 /198.H |
|---|---|---|---|---|
| `RECHTS` |  |  | `SOLLWERT` | `3` |
| `RIGHT 24V.X1.A649:2 /320.E` | `X1.A649:6 /320.F` | `A306 /324.D /322.C` | `XB9.A356 X1.A306 X6.A306` | `9B 7 7 3` |
| `1` | `2` | `6` |  | `3 A` |
|  |  |  | `M` |  |


### Table 2 — 3 data rows × 2 columns (at x=708.7, y=62.4)

| D/A | A356/07 /198.H |
|---|---|
| `INPUT` | `3` |
|  | `10B 8 8 4` |
|  | `5 B` |


### Table 3 — 4 data rows × 8 columns (at x=921.3, y=62.4)

| D/A | A356/07 /198.H |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| `OUTPUT` | `3` |  |  |  |  |  |  |
|  | `11B 9 9 5` |  |  |  |  |  |  |
|  | `4 C` | `X1.M501.A649.B` | `X1.M501.A649.A` | `1 1` | `2 2` | `5 5` | `3 3` |
|  |  |  |  | `+ A649 /203.G` | `M M501` | `B` | `A` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `9B` | D | 139.17 |
| `D/A` | D | 65.78 |
| `SOLLWERT` | D | 122.83 |
| `11B` | G | 139.18 |
| `D/A` | G | 65.78 |
| `OUTPUT` | G | 122.89 |
| `10B` | F | 139.18 |
| `D/A` | E | 65.78 |
| `INPUT` | E | 122.88 |
| `M` | H | 571.51 |
| `LÜFTER:` | H | 630.59 |
| `BOGENFÜHRUNG` | H | 641.27 |
| `VENTILATOR:` | H | 651.88 |
| `SHEET GUIDING DEVICE` | H | 662.52 |
| `B` | H | 492.04 |
| `A` | H | 492.04 |
| `M` | D | 578.6 |
| `BOGENFÜHRUNGSELEMENT: VERLÄNGERUNG (3656,8MM)` | B | 697.97 |
| `SHEET GUIDING ELEMENT EXTENSION (3656,8MM)` | B | 708.6 |
| `S+W` | A | 733.24 |
| `PP` | A | 743.87 |
| `OPTION` | B | 733.35 |
| `VERLÄNGERUNG` | B | 733.4 |
| `EXTENSION` | B | 743.98 |
| `S+W` | D | 733.24 |
| `PP` | D | 743.87 |
| `OPTION` | D | 733.35 |
| `VERLÄNGERUNG` | D | 733.4 |
| `EXTENSION` | D | 743.98 |
| `ENTFÄLLT BEI` | C | 733.35 |
| `DELETED IN CASE OF` | C | 744 |
| `BOGENFÜHRUNGSELEMENT, SOLLWERT` | A | 67.24 |
| `SHEET GUIDING ELEMENT, NOMINAL VALUE` | A | 77.88 |
| `A` | A | 72.59 |
| `BOGENFÜHRUNGSELEMENT, STÖRMELDESIGNAL` | A | 95.6 |
| `SHEET GUIDING ELEMENT, TROUBLE MESSAGE SIGNAL` | B | 106.22 |
| `B` | A | 100.93 |
| `BOGENFÜHRUNGSELEMENT LINKS / RECHTS` | A | 123.94 |
| `SHEET GUIDING ELEMENT LEFT / RIGHT` | A | 134.57 |
| `C` | A | 129.29 |
| `A` | D | 448.81 |
| `B` | F | 448.81 |
| `C` | G | 448.92 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 67.2 | 115.4 | → | text | `BOGENFÜHRUNGSELEMENT, SOLLWERT` |
| A | 72.6 | 102.8 | → | text | `A` |
| A | 77.9 | 115.9 | → | text | `SHEET GUIDING ELEMENT, NOMINAL VALUE` |
| A | 95.6 | 115.4 | → | text | `BOGENFÜHRUNGSELEMENT, STÖRMELDESIGNAL` |
| A | 100.9 | 102.6 | → | text | `B` |
| A | 123.9 | 115.4 | → | text | `BOGENFÜHRUNGSELEMENT LINKS / RECHTS` |
| A | 129.3 | 102.5 | → | text | `C` |
| A | 134.6 | 115.9 | → | text | `SHEET GUIDING ELEMENT LEFT / RIGHT` |
| A | 295.1 | 130.1 | → | potential | `0V.X1.A649:1` |
| A | 305.0 | 167.8 | → | cross-reference | `/320.E` |
| A | 477.8 | 143.2 | → | device tag | `A649` |
| A | 669.3 | 182.3 | → | number | `2` |
| A | 733.2 | 186.8 | → | text | `S+W` |
| A | 738.7 | 174.6 | → | number | `1` |
| A | 743.9 | 186.2 | → | text | `PP` |
| B | 106.2 | 115.9 | → | text | `SHEET GUIDING ELEMENT, TROUBLE MESSAGE SIGNAL` |
| B | 238.4 | 309.3 | → | device ref | `X1.A649:6` |
| B | 266.7 | 206.4 | → | potential | `24V.X1.A649:2` |
| B | 276.6 | 252.9 | → | cross-reference | `/320.E` |
| B | 422.7 | 177.4 | → | device ref | `X1.A649` |
| B | 431.2 | 228.8 | → | number | `1` |
| B | 431.2 | 314.4 | → | number | `2` |
| B | 698.0 | 197.6 | → | text | `BOGENFÜHRUNGSELEMENT: VERLÄNGERUNG (3656,8MM)` |
| B | 708.6 | 198.1 | → | text | `SHEET GUIDING ELEMENT EXTENSION (3656,8MM)` |
| B | 733.4 | 208.1 | → | text | `OPTION` |
| B | 733.4 | 250.9 | → | text | `VERLÄNGERUNG` |
| B | 744.0 | 208.1 | → | text | `OPTION` |
| B | 744.0 | 250.0 | → | text | `EXTENSION` |
| C | 242.7 | 462.6 | → | device tag | `A306` |
| C | 248.3 | 338.2 | → | cross-reference | `/320.F` |
| C | 255.8 | 464.9 | → | cross-reference | `/324.D` |
| C | 268.2 | 464.9 | → | cross-reference | `/322.C` |
| C | 431.2 | 399.4 | → | number | `6` |
| C | 733.3 | 398.8 | → | text | `ENTFÄLLT BEI` |
| C | 738.7 | 386.9 | → | number | `2` |
| C | 744.0 | 398.8 | → | text | `DELETED IN CASE OF` |
| D | 65.8 | 544.0 | → | text | `D/A` |
| D | 79.7 | 531.4 | → | device tag | `A356/07` |
| D | 94.5 | 540.3 | → | cross-reference | `/198.H` |
| D | 122.8 | 499.9 | → | text | `SOLLWERT` |
| D | 122.9 | 578.7 | → | number | `3` |
| D | 139.2 | 555.3 | → | text | `9B` |
| D | 153.4 | 496.3 | → | device ref | `XB9.A356` |
| D | 154.8 | 555.3 | → | number | `7` |
| D | 195.9 | 503.4 | → | device ref | `X1.A306` |
| D | 204.4 | 555.3 | → | number | `7` |
| D | 280.9 | 503.4 | → | device ref | `X6.A306` |
| D | 282.4 | 555.3 | → | number | `3` |
| D | 431.2 | 555.3 | → | number | `3` |
| D | 448.8 | 556.9 | → | text | `A` |
| D | 578.6 | 548.4 | → | text | `M` |
| D | 733.2 | 505.7 | → | text | `S+W` |
| D | 733.4 | 527.0 | → | text | `OPTION` |
| D | 733.4 | 569.8 | → | text | `VERLÄNGERUNG` |
| D | 743.9 | 505.1 | → | text | `PP` |
| D | 744.0 | 527.0 | → | text | `OPTION` |
| D | 744.0 | 568.9 | → | text | `EXTENSION` |
| E | 65.8 | 756.6 | → | text | `D/A` |
| E | 122.9 | 723.5 | → | text | `INPUT` |
| F | 79.7 | 744.0 | → | device tag | `A356/07` |
| F | 94.5 | 752.9 | → | cross-reference | `/198.H` |
| F | 122.9 | 791.3 | → | number | `3` |
| F | 139.2 | 767.3 | → | text | `10B` |
| F | 154.8 | 767.9 | → | number | `8` |
| F | 204.4 | 767.9 | → | number | `8` |
| F | 282.4 | 767.9 | → | number | `4` |
| F | 431.2 | 767.9 | → | number | `5` |
| F | 448.8 | 769.2 | → | text | `B` |
| G | 65.8 | 969.2 | → | text | `D/A` |
| G | 79.7 | 956.6 | → | device tag | `A356/07` |
| G | 94.5 | 965.5 | → | cross-reference | `/198.H` |
| G | 122.9 | 931.6 | → | text | `OUTPUT` |
| G | 122.9 | 1003.9 | → | number | `3` |
| G | 139.2 | 979.9 | → | text | `11B` |
| G | 154.8 | 980.5 | → | number | `9` |
| G | 204.4 | 980.5 | → | number | `9` |
| G | 282.4 | 980.5 | → | number | `5` |
| G | 431.2 | 980.5 | → | number | `4` |
| G | 448.9 | 981.9 | → | text | `C` |
| H | 366.5 | 1059.1 | ↕ | device ref | `X1.M501.A649.B` |
| H | 367.4 | 1073.2 | ↕ | device ref | `X1.M501.A649.A` |
| H | 409.9 | 1093.3 | → | number | `1` |
| H | 409.9 | 1108.1 | → | number | `2` |
| H | 409.9 | 1122.2 | → | number | `5` |
| H | 409.9 | 1136.4 | → | number | `3` |
| H | 426.9 | 1093.3 | → | number | `1` |
| H | 426.9 | 1108.1 | → | number | `2` |
| H | 426.9 | 1122.2 | → | number | `5` |
| H | 426.9 | 1136.4 | → | number | `3` |
| H | 492.0 | 1121.7 | → | text | `B` |
| H | 492.0 | 1136.7 | → | text | `A` |
| H | 492.1 | 1093.9 | → | number | `+` |
| H | 530.4 | 1084.0 | → | device tag | `A649` |
| H | 542.8 | 1084.3 | → | cross-reference | `/203.G` |
| H | 571.5 | 1108.2 | → | text | `M` |
| H | 604.8 | 1098.1 | → | potential | `M501` |
| H | 630.6 | 1062.1 | → | text | `LÜFTER:` |
| H | 641.3 | 1062.1 | → | text | `BOGENFÜHRUNG` |
| H | 651.9 | 1063.0 | → | text | `VENTILATOR:` |
| H | 662.5 | 1062.7 | → | text | `SHEET GUIDING DEVICE` |
| H | 675.8 | 1047.1 | → | number | `1` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
  67.2  115.4  text         BOGENFÜHRUNGSELEMENT, SOLLWERT
  72.6  102.8  text         A
  77.9  115.9  text         SHEET GUIDING ELEMENT, NOMINAL VALUE
  95.6  115.4  text         BOGENFÜHRUNGSELEMENT, STÖRMELDESIGNAL
 100.9  102.6  text         B
 123.9  115.4  text         BOGENFÜHRUNGSELEMENT LINKS / RECHTS
 129.3  102.5  text         C
 134.6  115.9  text         SHEET GUIDING ELEMENT LEFT / RIGHT
 295.1  130.1  net          0V.X1.A649:1
 305.0  167.8  xref         /320.E
 477.8  143.2  devtag       A649
 669.3  182.3  numeric      2
 733.2  186.8  text         S+W
 738.7  174.6  numeric      1
 743.9  186.2  text         PP
=== Column B ===
 106.2  115.9  text         SHEET GUIDING ELEMENT, TROUBLE MESSAGE SIGNAL
 238.4  309.3  devref       X1.A649:6
 266.7  206.4  net          24V.X1.A649:2
 276.6  252.9  xref         /320.E
 422.7  177.4  devref       X1.A649
 431.2  228.8  numeric      1
 431.2  314.4  numeric      2
 698.0  197.6  text         BOGENFÜHRUNGSELEMENT: VERLÄNGERUNG (3656,8MM)
 708.6  198.1  text         SHEET GUIDING ELEMENT EXTENSION (3656,8MM)
 733.4  208.1  text         OPTION
 733.4  250.9  text         VERLÄNGERUNG
 744.0  208.1  text         OPTION
 744.0  250.0  text         EXTENSION
=== Column C ===
 242.7  462.6  devtag       A306
 248.3  338.2  xref         /320.F
 255.8  464.9  xref         /324.D
 268.2  464.9  xref         /322.C
 431.2  399.4  numeric      6
 733.3  398.8  text         ENTFÄLLT BEI
 738.7  386.9  numeric      2
 744.0  398.8  text         DELETED IN CASE OF
=== Column D ===
  65.8  544.0  text         D/A
  79.7  531.4  devtag       A356/07
  94.5  540.3  xref         /198.H
 122.8  499.9  text         SOLLWERT
 122.9  578.7  numeric      3
 139.2  555.3  text         9B
 153.4  496.3  devref       XB9.A356
 154.8  555.3  numeric      7
 195.9  503.4  devref       X1.A306
 204.4  555.3  numeric      7
 280.9  503.4  devref       X6.A306
 282.4  555.3  numeric      3
 431.2  555.3  numeric      3
 448.8  556.9  text         A
 578.6  548.4  text         M
 733.2  505.7  text         S+W
 733.4  527.0  text         OPTION
 733.4  569.8  text         VERLÄNGERUNG
 743.9  505.1  text         PP
 744.0  527.0  text         OPTION
 744.0  568.9  text         EXTENSION
=== Column E ===
  65.8  756.6  text         D/A
 122.9  723.5  text         INPUT
=== Column F ===
  79.7  744.0  devtag       A356/07
  94.5  752.9  xref         /198.H
 122.9  791.3  numeric      3
 139.2  767.3  text         10B
 154.8  767.9  numeric      8
 204.4  767.9  numeric      8
 282.4  767.9  numeric      4
 431.2  767.9  numeric      5
 448.8  769.2  text         B
=== Column G ===
  65.8  969.2  text         D/A
  79.7  956.6  devtag       A356/07
  94.5  965.5  xref         /198.H
 122.9  931.6  text         OUTPUT
 122.9 1003.9  numeric      3
 139.2  979.9  text         11B
 154.8  980.5  numeric      9
 204.4  980.5  numeric      9
 282.4  980.5  numeric      5
 431.2  980.5  numeric      4
 448.9  981.9  text         C
=== Column H ===
 366.5 1059.1  devref       X1.M501.A649.B
 367.4 1073.2  devref       X1.M501.A649.A
 409.9 1093.3  numeric      1
 409.9 1108.1  numeric      2
 409.9 1122.2  numeric      5
 409.9 1136.4  numeric      3
 426.9 1093.3  numeric      1
 426.9 1108.1  numeric      2
 426.9 1122.2  numeric      5
 426.9 1136.4  numeric      3
 492.0 1121.7  text         B
 492.0 1136.7  text         A
 492.1 1093.9  numeric      +
 530.4 1084.0  devtag       A649
 542.8 1084.3  xref         /203.G
 571.5 1108.2  text         M
 604.8 1098.1  net          M501
 630.6 1062.1  text         LÜFTER:
 641.3 1062.1  text         BOGENFÜHRUNG
 651.9 1063.0  text         VENTILATOR:
 662.5 1062.7  text         SHEET GUIDING DEVICE
 675.8 1047.1  numeric      1
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_EA_8039G38E915_p`, sheet 323._
