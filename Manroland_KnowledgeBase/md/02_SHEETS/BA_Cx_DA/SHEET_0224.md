---
doc: "+BA_Cx_DA"
sheet: 224
sheet_total: 247
document_code: "8039G38J415"
section_de: "OPTION: INLINEOBSERVER"
section_en: "OPTION: INLINEOBSERVER"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "28.06.10"
image: "../../../images/+BA_Cx_DA/BA_Cx_DA_0224.png"
columns: "A-B-C-D-E-F-G-H"
---

# +BA_Cx_DA — Sheet 224 of 247 — OPTION: INLINEOBSERVER

**OPTION: INLINEOBSERVER**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+BA_Cx_DA` covers the **Printing units / main switch cabinet** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+BA_Cx_DA`  (8039G38J415) |
| Sheet | **224** of 247 |
| Section (DE) | OPTION: INLINEOBSERVER |
| Section (EN) | OPTION: INLINEOBSERVER |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 28.06.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G, H |
| Path numbers | — |
| Labels on sheet | 80 |
| Cross-refs out | 2 |
| Cross-refs in | 30 |

**Previous:** [+BA_Cx_DA sheet 223](SHEET_0223.md) · **Next:** [+BA_Cx_DA sheet 225](SHEET_0225.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+BA_Cx_DA) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+BA_Cx_DA sheet 224](../../../images/+BA_Cx_DA/BA_Cx_DA_0224.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/225.B` | [+BA_Cx_DA sheet 225](SHEET_0225.md) | B | — | SCHALTBOX: VIDEOKAMERA SWITCH BOX: VIDEO CAMERA | OPTION: INLINEOBSERVER | B |
| `/223.A` | [+BA_Cx_DA sheet 223](SHEET_0223.md) | A | — | SCHALTBOX: VIDEOKAMERA SWITCH BOX: VIDEO CAMERA | OPTION: INLINEOBSERVER | B |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+BA_Cx_DA#144](SHEET_0144.md) | F, G, H | `/144.F`, `/144.G`, `/144.H` | — | 21 | — |
| [+BA_Cx_DA#149](SHEET_0149.md) | G | `/149.G` | — | 7 | — |
| [+BA_Cx_DA#223](SHEET_0223.md) | B | `/223.B` | — | 1 | SCHALTBOX: VIDEOKAMERA SWITCH BOX: VIDEO CAMERA |
| [+BA_Cx_DA#225](SHEET_0225.md) | B | `/225.B` | — | 1 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `U043` | U | Umrichter / frequency converter | A | — | — | — |
| `B009/03` | B | Umformer / transducer, sensor | D | 03 | — | — |
| `B009/04` | B | Umformer / transducer, sensor | G | 04 | — | — |
| `B009/02` | B | Umformer / transducer, sensor | A | 02 | — | — |
| `X1.2.U043` | — | cross-device reference | A | — | — | — |

## Potentials / nets

_No named potentials on this sheet._

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| A | 207.2 | — | — | `U043` |
| B | 220.3 | — | `/225.B`, `/223.A` | `SCHALTBOX: VIDEOKAMERA SWITCH BOX: VIDEO CAMERA` |
| B | 263.9 | — | — | `X1.2.U043 1 2 3 4 5 6 7` |
| A | 486.4 | — | — | `X1.B009/02 1` |
| C | 486.4 | — | — | `+AB 2 3 4 5 6 7 X1.B009/03 1` |
| F | 486.4 | — | — | `X1.B009/04 1` |
| E | 502.1 | — | — | `2 3 4 5 6 7` |
| G | 502.1 | — | — | `2 3 4 5 6 7` |
| A | 568.6 | — | — | `B009/02` |
| D | 568.6 | — | — | `B009/03` |
| G | 568.6 | — | — | `B009/04` |
| A | 581.3 | — | — | `+AB` |
| A | 590.6 | — | — | `1` |
| C | 597.7 | — | — | `4 2` |
| A | 604.8 | — | — | `3` |
| B | 612.9 | — | — | `VIDEOKAMERA: ANLEGER TAKTROLLE VIDEO CAMERA: FEEDER FORWARDER WHEEL` |
| D | 612.9 | — | — | `VIDEOKAMERA: WENDEABLAUF VIDEO CAMERA: REVERSING PROCESS` |
| G | 612.9 | — | — | `VIDEOKAMERA: TRANSFERTER NACH 1.WENDUNG VIDEO CAMERA: TRANSFERTER TO FIRST REVERSING` |
| A | 619.0 | — | — | `4` |
| C | 619.0 | — | — | `3 5` |
| F | 619.0 | — | — | `4 6` |
| A | 683.8 | — | — | `DRUCKWERK VOR DER WENDUNG PRINTING UNIT BEFORE REVERSING POINT` |
| C | 696.2 | — | — | `2 6 ALLE DRUCKWERKE NACH DER 1.WENDUNG ALL PRINTING UNITS AFTER 1ST REVERSING` |
| B | 697.9 | — | — | `4 INLINEOBSERVER INLINEOBSERVER` |
| C | 698.0 | — | — | `COMPLETE EQUIPEMENT VOLLAUSSTATTUNG` |
| A | 733.3 | — | — | `1 NUR BEI` |
| C | 733.4 | — | — | `3 INLINEOBSERVER INLINEOBSERVER STARTERKIT STARTING SET` |
| D | 733.4 | — | — | `5 DRUCKWERK VOR DER 2.WENDUNG PRINTING UNIT BEFORE SECOND REVERSING` |
| A | 740.4 | — | — | `ONLY FOR +AB` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `SCHALTBOX: VIDEOKAMERA` | C | 230.23 |
| `SWITCH BOX: VIDEO CAMERA` | C | 240.85 |
| `X1.B009/02` | A | 486.45 |
| `+AB` | A | 499.13 |
| `X1.B009/03` | D | 486.45 |
| `VIDEOKAMERA: WENDEABLAUF` | D | 612.9 |
| `VIDEO CAMERA: REVERSING PROCESS` | D | 623.54 |
| `X1.B009/04` | F | 486.45 |
| `VIDEOKAMERA: TRANSFERTER NACH 1.WENDUNG` | G | 612.91 |
| `VIDEO CAMERA: TRANSFERTER TO FIRST REVERSING` | G | 623.54 |
| `VIDEOKAMERA: ANLEGER TAKTROLLE` | A | 612.91 |
| `VIDEO CAMERA: FEEDER FORWARDER WHEEL` | B | 623.53 |
| `NUR BEI` | A | 733.33 |
| `ONLY FOR` | A | 744.02 |
| `STARTERKIT` | C | 733.37 |
| `STARTING SET` | C | 744 |
| `INLINEOBSERVER` | C | 733.37 |
| `VOLLAUSSTATTUNG` | C | 697.96 |
| `COMPLETE EQUIPEMENT` | C | 708.59 |
| `DRUCKWERK VOR DER 2.WENDUNG` | D | 733.37 |
| `PRINTING UNIT BEFORE SECOND REVERSING` | D | 744.02 |
| `ALLE DRUCKWERKE NACH DER 1.WENDUNG` | D | 697.94 |
| `ALL PRINTING UNITS AFTER 1ST REVERSING` | D | 708.58 |
| `DRUCKWERK VOR DER WENDUNG` | A | 683.76 |
| `PRINTING UNIT BEFORE REVERSING POINT` | A | 694.41 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 207.2 | 93.5 | → | device tag | `U043` |
| A | 220.3 | 96.7 | → | cross-reference | `/225.B` |
| A | 232.7 | 96.4 | → | cross-reference | `/223.A` |
| A | 263.9 | 186.2 | → | number | `1` |
| A | 264.6 | 125.6 | → | device ref | `X1.2.U043` |
| A | 486.5 | 118.8 | → | text | `X1.B009/02` |
| A | 499.1 | 157.3 | → | text | `+AB` |
| A | 502.1 | 186.2 | → | number | `1` |
| A | 568.7 | 155.9 | → | device tag | `B009/02` |
| A | 581.3 | 178.6 | → | text | `+AB` |
| A | 590.6 | 90.1 | → | number | `1` |
| A | 604.8 | 89.7 | → | number | `3` |
| A | 612.9 | 127.6 | → | text | `VIDEOKAMERA: ANLEGER TAKTROLLE` |
| A | 619.0 | 89.7 | → | number | `4` |
| A | 683.8 | 88.4 | → | text | `DRUCKWERK VOR DER WENDUNG` |
| A | 694.4 | 88.4 | → | text | `PRINTING UNIT BEFORE REVERSING POINT` |
| A | 696.2 | 75.1 | → | number | `2` |
| A | 733.3 | 87.0 | → | text | `NUR BEI` |
| A | 738.7 | 75.4 | → | number | `1` |
| A | 740.4 | 137.9 | → | text | `+AB` |
| A | 744.0 | 87.6 | → | text | `ONLY FOR` |
| B | 263.9 | 215.1 | → | number | `2` |
| B | 263.9 | 243.5 | → | number | `3` |
| B | 263.9 | 271.8 | → | number | `4` |
| B | 263.9 | 300.2 | → | number | `5` |
| B | 263.9 | 328.5 | → | number | `6` |
| B | 502.1 | 215.1 | → | number | `2` |
| B | 502.1 | 243.5 | → | number | `3` |
| B | 502.1 | 271.8 | → | number | `4` |
| B | 502.1 | 300.2 | → | number | `5` |
| B | 502.1 | 328.5 | → | number | `6` |
| B | 623.5 | 127.6 | → | text | `VIDEO CAMERA: FEEDER FORWARDER WHEEL` |
| B | 703.3 | 301.9 | → | number | `4` |
| B | 738.7 | 301.7 | → | number | `3` |
| C | 230.2 | 424.9 | → | text | `SCHALTBOX: VIDEOKAMERA` |
| C | 240.8 | 424.9 | → | text | `SWITCH BOX: VIDEO CAMERA` |
| C | 263.9 | 356.9 | → | number | `7` |
| C | 502.1 | 356.9 | → | number | `7` |
| C | 597.7 | 458.2 | → | number | `4` |
| C | 597.7 | 472.5 | → | number | `2` |
| C | 619.0 | 458.2 | → | number | `3` |
| C | 619.0 | 472.4 | → | number | `5` |
| C | 697.9 | 313.8 | → | text | `INLINEOBSERVER` |
| C | 698.0 | 392.6 | → | text | `VOLLAUSSTATTUNG` |
| C | 708.6 | 313.8 | → | text | `INLINEOBSERVER` |
| C | 708.6 | 392.3 | → | text | `COMPLETE EQUIPEMENT` |
| C | 733.4 | 313.8 | → | text | `INLINEOBSERVER` |
| C | 733.4 | 392.3 | → | text | `STARTERKIT` |
| C | 744.0 | 313.8 | → | text | `INLINEOBSERVER` |
| C | 744.0 | 392.3 | → | text | `STARTING SET` |
| D | 486.5 | 487.3 | → | text | `X1.B009/03` |
| D | 502.1 | 554.7 | → | number | `1` |
| D | 502.1 | 583.7 | → | number | `2` |
| D | 502.1 | 612.0 | → | number | `3` |
| D | 568.7 | 524.4 | → | device tag | `B009/03` |
| D | 612.9 | 496.1 | → | text | `VIDEOKAMERA: WENDEABLAUF` |
| D | 623.5 | 496.1 | → | text | `VIDEO CAMERA: REVERSING PROCESS` |
| D | 697.9 | 542.8 | → | text | `ALLE DRUCKWERKE NACH DER 1.WENDUNG` |
| D | 703.3 | 528.7 | → | number | `6` |
| D | 708.6 | 542.8 | → | text | `ALL PRINTING UNITS AFTER 1ST REVERSING` |
| D | 733.4 | 542.0 | → | text | `DRUCKWERK VOR DER 2.WENDUNG` |
| D | 738.7 | 528.5 | → | number | `5` |
| D | 744.0 | 542.0 | → | text | `PRINTING UNIT BEFORE SECOND REVERSING` |
| E | 502.1 | 640.3 | → | number | `4` |
| E | 502.1 | 668.7 | → | number | `5` |
| E | 502.1 | 697.0 | → | number | `6` |
| E | 502.1 | 725.4 | → | number | `7` |
| F | 486.5 | 855.8 | → | text | `X1.B009/04` |
| F | 619.0 | 826.7 | → | number | `4` |
| F | 619.0 | 840.9 | → | number | `6` |
| G | 502.1 | 923.2 | → | number | `1` |
| G | 502.1 | 952.2 | → | number | `2` |
| G | 502.1 | 980.5 | → | number | `3` |
| G | 502.1 | 1008.9 | → | number | `4` |
| G | 502.1 | 1037.2 | → | number | `5` |
| G | 568.7 | 892.9 | → | device tag | `B009/04` |
| G | 612.9 | 864.6 | → | text | `VIDEOKAMERA: TRANSFERTER NACH 1.WENDUNG` |
| G | 623.5 | 864.6 | → | text | `VIDEO CAMERA: TRANSFERTER TO FIRST REVERSING` |
| H | 502.1 | 1065.5 | → | number | `6` |
| H | 502.1 | 1093.9 | → | number | `7` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
 207.2   93.5  devtag       U043
 220.3   96.7  xref         /225.B
 232.7   96.4  xref         /223.A
 263.9  186.2  numeric      1
 264.6  125.6  devref       X1.2.U043
 486.5  118.8  text         X1.B009/02
 499.1  157.3  text         +AB
 502.1  186.2  numeric      1
 568.7  155.9  devtag       B009/02
 581.3  178.6  text         +AB
 590.6   90.1  numeric      1
 604.8   89.7  numeric      3
 612.9  127.6  text         VIDEOKAMERA: ANLEGER TAKTROLLE
 619.0   89.7  numeric      4
 683.8   88.4  text         DRUCKWERK VOR DER WENDUNG
 694.4   88.4  text         PRINTING UNIT BEFORE REVERSING POINT
 696.2   75.1  numeric      2
 733.3   87.0  text         NUR BEI
 738.7   75.4  numeric      1
 740.4  137.9  text         +AB
 744.0   87.6  text         ONLY FOR
=== Column B ===
 263.9  215.1  numeric      2
 263.9  243.5  numeric      3
 263.9  271.8  numeric      4
 263.9  300.2  numeric      5
 263.9  328.5  numeric      6
 502.1  215.1  numeric      2
 502.1  243.5  numeric      3
 502.1  271.8  numeric      4
 502.1  300.2  numeric      5
 502.1  328.5  numeric      6
 623.5  127.6  text         VIDEO CAMERA: FEEDER FORWARDER WHEEL
 703.3  301.9  numeric      4
 738.7  301.7  numeric      3
=== Column C ===
 230.2  424.9  text         SCHALTBOX: VIDEOKAMERA
 240.8  424.9  text         SWITCH BOX: VIDEO CAMERA
 263.9  356.9  numeric      7
 502.1  356.9  numeric      7
 597.7  458.2  numeric      4
 597.7  472.5  numeric      2
 619.0  458.2  numeric      3
 619.0  472.4  numeric      5
 697.9  313.8  text         INLINEOBSERVER
 698.0  392.6  text         VOLLAUSSTATTUNG
 708.6  313.8  text         INLINEOBSERVER
 708.6  392.3  text         COMPLETE EQUIPEMENT
 733.4  313.8  text         INLINEOBSERVER
 733.4  392.3  text         STARTERKIT
 744.0  313.8  text         INLINEOBSERVER
 744.0  392.3  text         STARTING SET
=== Column D ===
 486.5  487.3  text         X1.B009/03
 502.1  554.7  numeric      1
 502.1  583.7  numeric      2
 502.1  612.0  numeric      3
 568.7  524.4  devtag       B009/03
 612.9  496.1  text         VIDEOKAMERA: WENDEABLAUF
 623.5  496.1  text         VIDEO CAMERA: REVERSING PROCESS
 697.9  542.8  text         ALLE DRUCKWERKE NACH DER 1.WENDUNG
 703.3  528.7  numeric      6
 708.6  542.8  text         ALL PRINTING UNITS AFTER 1ST REVERSING
 733.4  542.0  text         DRUCKWERK VOR DER 2.WENDUNG
 738.7  528.5  numeric      5
 744.0  542.0  text         PRINTING UNIT BEFORE SECOND REVERSING
=== Column E ===
 502.1  640.3  numeric      4
 502.1  668.7  numeric      5
 502.1  697.0  numeric      6
 502.1  725.4  numeric      7
=== Column F ===
 486.5  855.8  text         X1.B009/04
 619.0  826.7  numeric      4
 619.0  840.9  numeric      6
=== Column G ===
 502.1  923.2  numeric      1
 502.1  952.2  numeric      2
 502.1  980.5  numeric      3
 502.1 1008.9  numeric      4
 502.1 1037.2  numeric      5
 568.7  892.9  devtag       B009/04
 612.9  864.6  text         VIDEOKAMERA: TRANSFERTER NACH 1.WENDUNG
 623.5  864.6  text         VIDEO CAMERA: TRANSFERTER TO FIRST REVERSING
=== Column H ===
 502.1 1065.5  numeric      6
 502.1 1093.9  numeric      7
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_BA_CX_DA_8039G38J415_p`, sheet 224._
