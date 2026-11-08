---
doc: "+Jx"
sheet: 204
sheet_total: 214
document_code: "039G38F308"
section_de: "OPTION: INLINEOBSERVER"
section_en: "OPTION: INLINEOBSERVER"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "03.01.10"
image: "../../../images/+Jx/Jx_0204.png"
columns: "A-B-C-D-E-F-G"
---

# +Jx — Sheet 204 of 214 — OPTION: INLINEOBSERVER

**OPTION: INLINEOBSERVER**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+Jx` covers the **1st printing module + feed register** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+Jx`  (039G38F308) |
| Sheet | **204** of 214 |
| Section (DE) | OPTION: INLINEOBSERVER |
| Section (EN) | OPTION: INLINEOBSERVER |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 03.01.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G |
| Path numbers | — |
| Labels on sheet | 96 |
| Cross-refs out | 2 |
| Cross-refs in | 47 |

**Previous:** [+Jx sheet 203](SHEET_0203.md) · **Next:** [+Jx sheet 205](SHEET_0205.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+Jx) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+Jx sheet 204](../../../images/+Jx/Jx_0204.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/6.F` | [+Jx sheet 6](SHEET_0006.md) | F | — | 24V.X2.U043\1:1 | SPANNUNGSVERSORGUNG, SCHALTSCHRANKBELÜFTUNG | A |
| `/6.C` | [+Jx sheet 6](SHEET_0006.md) | C | — | 0V.X2.U043\1:2 | SPANNUNGSVERSORGUNG, SCHALTSCHRANKBELÜFTUNG | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+Jx#6](SHEET_0006.md) | C, F | `/6.C`, `/6.F` | — | 2 | 0V.X2.U043\1:2 |
| [+Jx#116](SHEET_0116.md) | E, F | `/116.E`, `/116.F` | — | 14 | — |
| [+Jx#120](SHEET_0120.md) | B | `/120.B` | — | 7 | — |
| [+Jx#127](SHEET_0127.md) | E | `/127.E` | — | 2 | — |
| [+Jx#129](SHEET_0129.md) | B | `/129.B` | — | 11 | — |
| [+Jx#130](SHEET_0130.md) | H | `/130.H` | — | 11 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `U043/1` | U | Umrichter / frequency converter | A | 1 | — | — |
| `B009/08` | B | Umformer / transducer, sensor | C | 08 | — | — |
| `B009/10` | B | Umformer / transducer, sensor | E | 10 | — | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `0V` | 1 | A | `U043\1`, `X2` | `2` |
| `24V` | 1 | A | `U043\1`, `X2` | `1` |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| A | 87.4 | — | — | `X3.A015:1,+EA` |
| G | 87.4 | — | — | `X4.U043:1,+JA` |
| A | 101.5 | — | — | `X3.A015:9,+EA` |
| G | 101.5 | — | — | `X4.U043:9,+JA` |
| A | 115.7 | — | — | `X3.A015:3,+EA` |
| G | 115.7 | — | — | `X4.U043:3,+JA` |
| A | 129.9 | — | — | `X3.A015:10,+EA` |
| G | 129.9 | — | — | `X4.U043:10,+JA` |
| A | 144.1 | — | — | `X3.A015:7,+EA` |
| G | 144.1 | — | — | `X4.U043:7,+JA` |
| A | 158.2 | — | — | `X3.A015:8,+EA` |
| G | 158.2 | — | — | `X4.U043:8,+JA` |
| A | 172.4 | — | — | `X3.A015:4,+EA` |
| G | 172.4 | — | — | `X4.U043:4,+JA` |
| A | 186.6 | — | — | `X3.A015:12,+EA` |
| G | 186.6 | — | — | `X4.U043:12,+JA` |
| A | 200.8 | — | — | `X3.A015:13,+EA` |
| G | 200.8 | — | — | `X4.U043:13,+JA` |
| A | 214.9 | — | — | `X3.A015:6,+EA` |
| G | 214.9 | — | — | `X4.U043:6,+JA` |
| F | 289.4 | — | — | `X3.U043/1 1 9 3 10 7 8 4 12 13 6 5` |
| C | 291.5 | — | — | `X4.U043/1 1 9 3 10 7 8 4 12 13 6 5` |
| G | 322.3 | — | — | `SCHALTBOX: VIDEOKAMERA SWITCH BOX: VIDEO CAMERA` |
| A | 356.0 | — | — | `U043/1` |
| D | 419.8 | — | — | `X2.U043/1 1 2 1 2 3 4 5 6 7` |
| C | 419.8 | — | — | `X1.1.U043/1 1 2 3 4 5 6 7` |
| E | 419.8 | — | — | `X1.1.U043/1` |
| A | 465.1 | — | `/6.F` | `24V.X2.U043\1:1` |
| A | 493.4 | — | `/6.C` | `0V.X2.U043\1:2` |
| C | 558.7 | — | — | `X1.B009/08 1 3 2 5 4 6 7` |
| F | 558.7 | — | — | `X1.B009/10 1 3 2 5 4 6 7` |
| C | 632.4 | — | — | `B009/08` |
| E | 632.4 | — | — | `B009/10` |
| C | 669.6 | — | — | `VIDEOKAMERA: TRANSFERTER TRANSFERMODUL NACH DEM LACKMODUL VIDEO CAMERA: TRANSFERTER TRANSFER MODULE AFTER THE COATING MODUL` |
| F | 669.6 | — | — | `VIDEOKAMERA: TRANSFERTER TRANSFERMODUL VOR DEM LACKMODUL VIDEO CAMERA: TRANSFERTER TRANSFER MODULE BEFORE THE COATING MODUL` |
| B | 682.9 | — | — | `1` |
| A | 733.4 | — | — | `1 COMPLETE EQUIPEMENT VOLLAUSSTATTUNG` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `SCHALTBOX: VIDEOKAMERA` | G | 322.31 |
| `SWITCH BOX: VIDEO CAMERA` | G | 332.93 |
| `X4.U043/1` | B | 291.51 |
| `X3.A015:4,+EA` | A | 172.41 |
| `X3.A015:13,+EA` | A | 200.76 |
| `X3.A015:6,+EA` | A | 214.93 |
| `X3.A015:12,+EA` | A | 186.59 |
| `X3.A015:8,+EA` | A | 158.24 |
| `X3.A015:7,+EA` | A | 144.07 |
| `X3.A015:10,+EA` | A | 129.9 |
| `X3.A015:3,+EA` | A | 115.72 |
| `X3.A015:1,+EA` | A | 87.37 |
| `X3.A015:9,+EA` | A | 101.55 |
| `X3.U043/1` | D | 289.38 |
| `X4.U043:13,+JA` | G | 200.77 |
| `X4.U043:6,+JA` | G | 214.94 |
| `X4.U043:12,+JA` | G | 186.6 |
| `X4.U043:4,+JA` | G | 172.42 |
| `X4.U043:7,+JA` | G | 144.07 |
| `X4.U043:1,+JA` | G | 87.38 |
| `X4.U043:9,+JA` | G | 101.55 |
| `X4.U043:3,+JA` | G | 115.73 |
| `X4.U043:10,+JA` | G | 129.9 |
| `X4.U043:8,+JA` | G | 158.25 |
| `X1.B009/08` | C | 558.67 |
| `X1.1.U043/1` | C | 420.49 |
| `VIDEOKAMERA: TRANSFERTER TRANSFERMODUL NACH DEM LACKMODUL` | C | 669.57 |
| `VIDEO CAMERA: TRANSFERTER TRANSFER MODULE AFTER THE COATING MODUL` | C | 680.2 |
| `X2.U043/1` | B | 422.61 |
| `X1.B009/10` | E | 558.67 |
| `VIDEOKAMERA: TRANSFERTER TRANSFERMODUL VOR DEM LACKMODUL` | E | 669.57 |
| `VIDEO CAMERA: TRANSFERTER TRANSFER MODULE BEFORE THE COATING MODUL` | F | 680.2 |
| `VOLLAUSSTATTUNG` | A | 733.35 |
| `COMPLETE EQUIPEMENT` | A | 743.98 |
| `X1.1.U043/1` | E | 419.78 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 87.4 | 156.2 | → | text | `X3.A015:1,+EA` |
| A | 101.5 | 156.2 | → | text | `X3.A015:9,+EA` |
| A | 115.7 | 156.2 | → | text | `X3.A015:3,+EA` |
| A | 129.9 | 151.4 | → | text | `X3.A015:10,+EA` |
| A | 144.1 | 156.2 | → | text | `X3.A015:7,+EA` |
| A | 158.2 | 156.2 | → | text | `X3.A015:8,+EA` |
| A | 172.4 | 156.2 | → | text | `X3.A015:4,+EA` |
| A | 186.6 | 151.4 | → | text | `X3.A015:12,+EA` |
| A | 200.8 | 151.4 | → | text | `X3.A015:13,+EA` |
| A | 214.9 | 156.2 | → | text | `X3.A015:6,+EA` |
| A | 356.0 | 142.9 | → | device tag | `U043/1` |
| A | 465.1 | 128.7 | → | potential | `24V.X2.U043\1:1` |
| A | 493.4 | 135.2 | → | potential | `0V.X2.U043\1:2` |
| A | 503.4 | 191.1 | → | cross-reference | `/6.C` |
| A | 733.3 | 87.9 | → | text | `VOLLAUSSTATTUNG` |
| A | 738.6 | 75.4 | → | number | `1` |
| A | 744.0 | 87.6 | → | text | `COMPLETE EQUIPEMENT` |
| B | 291.5 | 197.9 | → | text | `X4.U043/1` |
| B | 293.7 | 257.1 | → | number | `1` |
| B | 293.7 | 286.0 | → | number | `9` |
| B | 293.7 | 314.4 | → | number | `3` |
| B | 422.6 | 183.7 | → | text | `X2.U043/1` |
| B | 424.0 | 242.9 | → | number | `1` |
| B | 424.0 | 272.1 | → | number | `2` |
| B | 475.0 | 191.9 | → | cross-reference | `/6.F` |
| B | 682.9 | 310.0 | → | number | `1` |
| C | 293.7 | 342.1 | → | number | `10` |
| C | 293.7 | 371.1 | → | number | `7` |
| C | 293.7 | 399.4 | → | number | `8` |
| C | 293.7 | 428.0 | → | number | `4` |
| C | 293.7 | 455.5 | → | number | `12` |
| C | 419.8 | 413.0 | → | number | `1` |
| C | 419.8 | 442.2 | → | number | `2` |
| C | 419.8 | 470.3 | → | number | `3` |
| C | 420.5 | 345.0 | → | text | `X1.1.U043/1` |
| C | 558.7 | 347.0 | → | text | `X1.B009/08` |
| C | 558.7 | 413.0 | → | number | `1` |
| C | 558.7 | 441.9 | → | number | `3` |
| C | 558.7 | 470.6 | → | number | `2` |
| C | 632.4 | 382.7 | → | device tag | `B009/08` |
| C | 669.6 | 333.1 | → | text | `VIDEOKAMERA: TRANSFERTER TRANSFERMODUL NACH DEM LACKMODUL` |
| C | 680.2 | 333.1 | → | text | `VIDEO CAMERA: TRANSFERTER TRANSFER MODULE AFTER THE COATING MODUL` |
| D | 289.4 | 594.7 | → | text | `X3.U043/1` |
| D | 293.7 | 483.9 | → | number | `13` |
| D | 293.7 | 512.8 | → | number | `6` |
| D | 293.7 | 541.1 | → | number | `5` |
| D | 419.8 | 498.9 | → | number | `4` |
| D | 419.8 | 527.0 | → | number | `5` |
| D | 419.8 | 555.3 | → | number | `6` |
| D | 419.8 | 583.7 | → | number | `7` |
| D | 558.7 | 498.6 | → | number | `5` |
| D | 558.7 | 527.2 | → | number | `4` |
| D | 558.7 | 555.3 | → | number | `6` |
| D | 558.7 | 583.7 | → | number | `7` |
| E | 289.4 | 654.0 | → | number | `1` |
| E | 289.4 | 682.9 | → | number | `9` |
| E | 289.4 | 711.2 | → | number | `3` |
| E | 289.4 | 739.0 | → | number | `10` |
| E | 419.8 | 655.4 | → | text | `X1.1.U043/1` |
| E | 419.8 | 724.8 | → | number | `1` |
| E | 419.8 | 754.0 | → | number | `2` |
| E | 558.7 | 658.8 | → | text | `X1.B009/10` |
| E | 558.7 | 724.8 | → | number | `1` |
| E | 558.7 | 753.7 | → | number | `3` |
| E | 632.4 | 694.5 | → | device tag | `B009/10` |
| E | 669.6 | 652.0 | → | text | `VIDEOKAMERA: TRANSFERTER TRANSFERMODUL VOR DEM LACKMODUL` |
| F | 289.4 | 767.9 | → | number | `7` |
| F | 289.4 | 796.3 | → | number | `8` |
| F | 289.4 | 824.9 | → | number | `4` |
| F | 289.4 | 852.4 | → | number | `12` |
| F | 289.4 | 880.7 | → | number | `13` |
| F | 419.8 | 782.1 | → | number | `3` |
| F | 419.8 | 810.7 | → | number | `4` |
| F | 419.8 | 838.8 | → | number | `5` |
| F | 419.8 | 867.1 | → | number | `6` |
| F | 419.8 | 895.5 | → | number | `7` |
| F | 558.7 | 782.4 | → | number | `2` |
| F | 558.7 | 810.4 | → | number | `5` |
| F | 558.7 | 839.1 | → | number | `4` |
| F | 558.7 | 867.1 | → | number | `6` |
| F | 558.7 | 895.5 | → | number | `7` |
| F | 680.2 | 652.0 | → | text | `VIDEO CAMERA: TRANSFERTER TRANSFER MODULE BEFORE THE COATING MODUL` |
| G | 87.4 | 942.2 | → | text | `X4.U043:1,+JA` |
| G | 101.6 | 942.2 | → | text | `X4.U043:9,+JA` |
| G | 115.7 | 942.2 | → | text | `X4.U043:3,+JA` |
| G | 129.9 | 942.2 | → | text | `X4.U043:10,+JA` |
| G | 144.1 | 942.2 | → | text | `X4.U043:7,+JA` |
| G | 158.2 | 942.2 | → | text | `X4.U043:8,+JA` |
| G | 172.4 | 942.2 | → | text | `X4.U043:4,+JA` |
| G | 186.6 | 942.2 | → | text | `X4.U043:12,+JA` |
| G | 200.8 | 942.2 | → | text | `X4.U043:13,+JA` |
| G | 214.9 | 942.2 | → | text | `X4.U043:6,+JA` |
| G | 289.4 | 909.6 | → | number | `6` |
| G | 289.4 | 938.0 | → | number | `5` |
| G | 322.3 | 998.9 | → | text | `SCHALTBOX: VIDEOKAMERA` |
| G | 332.9 | 998.9 | → | text | `SWITCH BOX: VIDEO CAMERA` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
  87.4  156.2  text         X3.A015:1,+EA
 101.5  156.2  text         X3.A015:9,+EA
 115.7  156.2  text         X3.A015:3,+EA
 129.9  151.4  text         X3.A015:10,+EA
 144.1  156.2  text         X3.A015:7,+EA
 158.2  156.2  text         X3.A015:8,+EA
 172.4  156.2  text         X3.A015:4,+EA
 186.6  151.4  text         X3.A015:12,+EA
 200.8  151.4  text         X3.A015:13,+EA
 214.9  156.2  text         X3.A015:6,+EA
 356.0  142.9  devtag       U043/1
 465.1  128.7  net          24V.X2.U043\1:1
 493.4  135.2  net          0V.X2.U043\1:2
 503.4  191.1  xref         /6.C
 733.3   87.9  text         VOLLAUSSTATTUNG
 738.6   75.4  numeric      1
 744.0   87.6  text         COMPLETE EQUIPEMENT
=== Column B ===
 291.5  197.9  text         X4.U043/1
 293.7  257.1  numeric      1
 293.7  286.0  numeric      9
 293.7  314.4  numeric      3
 422.6  183.7  text         X2.U043/1
 424.0  242.9  numeric      1
 424.0  272.1  numeric      2
 475.0  191.9  xref         /6.F
 682.9  310.0  numeric      1
=== Column C ===
 293.7  342.1  numeric      10
 293.7  371.1  numeric      7
 293.7  399.4  numeric      8
 293.7  428.0  numeric      4
 293.7  455.5  numeric      12
 419.8  413.0  numeric      1
 419.8  442.2  numeric      2
 419.8  470.3  numeric      3
 420.5  345.0  text         X1.1.U043/1
 558.7  347.0  text         X1.B009/08
 558.7  413.0  numeric      1
 558.7  441.9  numeric      3
 558.7  470.6  numeric      2
 632.4  382.7  devtag       B009/08
 669.6  333.1  text         VIDEOKAMERA: TRANSFERTER TRANSFERMODUL NACH DEM LACKMODUL
 680.2  333.1  text         VIDEO CAMERA: TRANSFERTER TRANSFER MODULE AFTER THE COATING MODUL
=== Column D ===
 289.4  594.7  text         X3.U043/1
 293.7  483.9  numeric      13
 293.7  512.8  numeric      6
 293.7  541.1  numeric      5
 419.8  498.9  numeric      4
 419.8  527.0  numeric      5
 419.8  555.3  numeric      6
 419.8  583.7  numeric      7
 558.7  498.6  numeric      5
 558.7  527.2  numeric      4
 558.7  555.3  numeric      6
 558.7  583.7  numeric      7
=== Column E ===
 289.4  654.0  numeric      1
 289.4  682.9  numeric      9
 289.4  711.2  numeric      3
 289.4  739.0  numeric      10
 419.8  655.4  text         X1.1.U043/1
 419.8  724.8  numeric      1
 419.8  754.0  numeric      2
 558.7  658.8  text         X1.B009/10
 558.7  724.8  numeric      1
 558.7  753.7  numeric      3
 632.4  694.5  devtag       B009/10
 669.6  652.0  text         VIDEOKAMERA: TRANSFERTER TRANSFERMODUL VOR DEM LACKMODUL
=== Column F ===
 289.4  767.9  numeric      7
 289.4  796.3  numeric      8
 289.4  824.9  numeric      4
 289.4  852.4  numeric      12
 289.4  880.7  numeric      13
 419.8  782.1  numeric      3
 419.8  810.7  numeric      4
 419.8  838.8  numeric      5
 419.8  867.1  numeric      6
 419.8  895.5  numeric      7
 558.7  782.4  numeric      2
 558.7  810.4  numeric      5
 558.7  839.1  numeric      4
 558.7  867.1  numeric      6
 558.7  895.5  numeric      7
 680.2  652.0  text         VIDEO CAMERA: TRANSFERTER TRANSFER MODULE BEFORE THE COATING MODUL
=== Column G ===
  87.4  942.2  text         X4.U043:1,+JA
 101.6  942.2  text         X4.U043:9,+JA
 115.7  942.2  text         X4.U043:3,+JA
 129.9  942.2  text         X4.U043:10,+JA
 144.1  942.2  text         X4.U043:7,+JA
 158.2  942.2  text         X4.U043:8,+JA
 172.4  942.2  text         X4.U043:4,+JA
 186.6  942.2  text         X4.U043:12,+JA
 200.8  942.2  text         X4.U043:13,+JA
 214.9  942.2  text         X4.U043:6,+JA
 289.4  909.6  numeric      6
 289.4  938.0  numeric      5
 322.3  998.9  text         SCHALTBOX: VIDEOKAMERA
 332.9  998.9  text         SWITCH BOX: VIDEO CAMERA
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_JX_039G38F308_p`, sheet 204._
