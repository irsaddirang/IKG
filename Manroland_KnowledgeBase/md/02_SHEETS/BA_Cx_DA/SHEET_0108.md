---
doc: "+BA_Cx_DA"
sheet: 108
sheet_total: 247
document_code: "8039G38J415"
section_de: "MOTOR: SEITENMARKE, B SEITE"
section_en: "MOTOR: SIDE GUIDE, B SIDE"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "28.06.10"
image: "../../../images/+BA_Cx_DA/BA_Cx_DA_0108.png"
columns: "A-B-C-D-E-F-G-H"
---

# +BA_Cx_DA — Sheet 108 of 247 — MOTOR: SEITENMARKE, B SEITE

**MOTOR: SIDE GUIDE, B SIDE**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+BA_Cx_DA` covers the **Printing units / main switch cabinet** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+BA_Cx_DA`  (8039G38J415) |
| Sheet | **108** of 247 |
| Section (DE) | MOTOR: SEITENMARKE, B SEITE |
| Section (EN) | MOTOR: SIDE GUIDE, B SIDE |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 28.06.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G, H |
| Path numbers | — |
| Labels on sheet | 71 |
| Cross-refs out | 2 |
| Cross-refs in | 24 |

**Previous:** [+BA_Cx_DA sheet 107](SHEET_0107.md) · **Next:** [+BA_Cx_DA sheet 109](SHEET_0109.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+BA_Cx_DA) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+BA_Cx_DA sheet 108](../../../images/+BA_Cx_DA/BA_Cx_DA_0108.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/109.A` | [+BA_Cx_DA sheet 109](SHEET_0109.md) | A | — | — | MOTOR: HEBERSTREIFENBREITE | A |
| `/107.A` | [+BA_Cx_DA sheet 107](SHEET_0107.md) | A | — | — | MOTOR: SEITENMARKE, A SEITE | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+BA_Cx_DA#107](SHEET_0107.md) | A | `/107.A` | — | 1 | — |
| [+BA_Cx_DA#109](SHEET_0109.md) | A | `/109.A` | — | 1 | — |
| [+BA_Cx_DA#146](SHEET_0146.md) | A | `/146.A` | — | 2 | — |
| [+BA_Cx_DA#148](SHEET_0148.md) | F | `/148.F` | — | 9 | — |
| [+BA_Cx_DA#174](SHEET_0174.md) | A, B | `/174.A`, `/174.B` | — | 11 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `A302` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `B397` | B | Umformer / transducer, sensor | F | — | — | — |
| `F11` | F | Schutz / protection device (fuse, circuit breaker) | D | — | — | — |
| `X1.M397` | — | cross-device reference | A | — | — | — |
| `X20.A302` | — | cross-device reference | A | — | — | — |
| `X1.B397` | — | cross-device reference | E | — | — | — |
| `X21.A302` | — | cross-device reference | E | — | — | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `0V` | 2 | D | — | — |
| `24V` | 2 | B | — | — |
| `M397` | 1 | A | — | — |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| D | 87.4 | — | — | `F11 0V` |
| B | 87.5 | — | — | `24V` |
| D | 122.5 | — | — | `T6,3A` |
| A | 129.3 | — | — | `A302` |
| A | 142.3 | — | `/109.A`, `/107.A` | — |
| C | 210.1 | — | — | `X20.A302 1 2 3 4 5 6 7 8 9` |
| F | 210.1 | — | — | `X21.A302 1 2` |
| F | 357.5 | — | — | `2 2` |
| C | 360.3 | — | — | `X1.M397 1 2 3 4 5 6 7 8 9` |
| F | 360.3 | — | — | `X1.B397 3 1` |
| G | 379.0 | — | — | `1 NUR BEI` |
| G | 386.1 | — | — | `ONLY FOR +BA` |
| G | 417.3 | — | — | `FRONT VIEW ONTO ANSICHT VON VORNE AUF BUCHSENGEHÄUSE` |
| B | 428.6 | — | — | `FREIGABE RS485` |
| C | 428.6 | — | — | `POSITIONIERANTRIEBE FREIGABE` |
| C | 428.6 | — | — | `NULL POSITION` |
| H | 429.6 | — | — | `4` |
| G | 434.0 | — | — | `2 3 1` |
| B | 439.3 | — | — | `RELEASE RS485` |
| C | 439.3 | — | — | `ZERO POSITION` |
| C | 441.8 | — | — | `24V 0V` |
| G | 449.2 | — | — | `THE SOCKET CASES` |
| C | 449.9 | — | — | `POSITIONING DRIVES RELEASE` |
| A | 497.8 | — | — | `M397` |
| C | 540.3 | — | — | `M` |
| F | 540.3 | — | — | `B397` |
| A | 641.2 | — | — | `MOTOR: SEITENMARKE (B SEITE) MOTOR: SIDE GUIDE (B SIDE)` |
| F | 641.2 | — | — | `DETECTOR: ZERO POSITION, SENSOR: NULL POSITION, SEITENMARKE, B SEITE` |
| C | 641.3 | — | — | `SEITENMARKE: AUF MAX FORMAT SIDE GUIDE: TO MAX SIZE` |
| F | 673.1 | — | — | `SIDE GUIDE, B SIDE` |
| C | 683.8 | — | — | `SEITENMARKE: AUF MIN FORMAT SIDE GUIDE: TO MIN SIZE` |
| A | 697.1 | — | — | `1` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `MOTOR: SEITENMARKE (B SEITE)` | A | 641.25 |
| `MOTOR: SIDE GUIDE (B SIDE)` | A | 651.89 |
| `M` | C | 540.33 |
| `T6,3A` | D | 122.51 |
| `SENSOR: NULL POSITION,` | F | 641.25 |
| `SEITENMARKE, B SEITE` | F | 651.87 |
| `DETECTOR: ZERO POSITION,` | F | 662.51 |
| `SIDE GUIDE, B SIDE` | F | 673.14 |
| `FREIGABE` | C | 428.61 |
| `POSITIONIERANTRIEBE` | C | 439.27 |
| `RELEASE` | C | 449.88 |
| `POSITIONING DRIVES` | C | 460.54 |
| `FREIGABE RS485` | B | 428.64 |
| `RELEASE RS485` | B | 439.28 |
| `NULL POSITION` | C | 428.65 |
| `ZERO POSITION` | C | 439.29 |
| `SEITENMARKE: AUF MIN FORMAT` | C | 683.78 |
| `SIDE GUIDE: TO MIN SIZE` | C | 694.39 |
| `SEITENMARKE: AUF MAX FORMAT` | C | 641.26 |
| `SIDE GUIDE: TO MAX SIZE` | C | 651.87 |
| `ANSICHT VON VORNE` | G | 417.32 |
| `AUF BUCHSENGEHÄUSE` | G | 427.96 |
| `FRONT VIEW ONTO` | G | 438.55 |
| `THE SOCKET CASES` | G | 449.2 |
| `NUR BEI` | G | 379 |
| `ONLY FOR` | G | 389.69 |
| `+BA` | G | 386.11 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 129.3 | 94.1 | → | device tag | `A302` |
| A | 142.4 | 96.4 | → | cross-reference | `/109.A` |
| A | 154.8 | 96.4 | → | cross-reference | `/107.A` |
| A | 210.1 | 114.8 | → | device ref | `X20.A302` |
| A | 211.5 | 172.1 | → | number | `1` |
| A | 360.3 | 172.1 | → | number | `1` |
| A | 363.1 | 117.6 | → | device ref | `X1.M397` |
| A | 497.8 | 92.4 | → | potential | `M397` |
| A | 641.3 | 127.0 | → | text | `MOTOR: SEITENMARKE (B SEITE)` |
| A | 651.9 | 127.0 | → | text | `MOTOR: SIDE GUIDE (B SIDE)` |
| A | 697.1 | 83.3 | → | number | `1` |
| B | 87.5 | 231.6 | → | potential | `24V` |
| B | 211.5 | 229.3 | → | number | `2` |
| B | 211.5 | 286.0 | → | number | `3` |
| B | 360.3 | 229.3 | → | number | `2` |
| B | 360.3 | 286.0 | → | number | `3` |
| B | 428.6 | 285.1 | → | text | `FREIGABE RS485` |
| B | 439.3 | 286.5 | → | text | `RELEASE RS485` |
| B | 441.8 | 217.4 | → | potential | `24V` |
| C | 211.5 | 342.7 | → | number | `4` |
| C | 211.5 | 399.4 | → | number | `5` |
| C | 211.5 | 456.1 | → | number | `6` |
| C | 360.3 | 342.7 | → | number | `4` |
| C | 360.3 | 399.4 | → | number | `5` |
| C | 360.3 | 456.1 | → | number | `6` |
| C | 428.6 | 380.6 | → | text | `FREIGABE` |
| C | 428.7 | 452.7 | → | text | `NULL POSITION` |
| C | 439.3 | 360.6 | → | text | `POSITIONIERANTRIEBE` |
| C | 439.3 | 453.5 | → | text | `ZERO POSITION` |
| C | 449.9 | 382.0 | → | text | `RELEASE` |
| C | 460.5 | 363.4 | → | text | `POSITIONING DRIVES` |
| C | 540.3 | 392.5 | → | text | `M` |
| C | 641.3 | 396.6 | → | text | `SEITENMARKE: AUF MAX FORMAT` |
| C | 651.9 | 396.6 | → | text | `SIDE GUIDE: TO MAX SIZE` |
| C | 683.8 | 396.6 | → | text | `SEITENMARKE: AUF MIN FORMAT` |
| C | 694.4 | 396.6 | → | text | `SIDE GUIDE: TO MIN SIZE` |
| D | 87.4 | 575.6 | → | potential | `0V` |
| D | 100.9 | 540.0 | → | device tag | `F11` |
| D | 122.5 | 533.5 | → | text | `T6,3A` |
| D | 211.5 | 512.8 | → | number | `7` |
| D | 211.5 | 569.5 | → | number | `8` |
| D | 360.3 | 512.8 | → | number | `7` |
| D | 360.3 | 569.5 | → | number | `8` |
| D | 441.8 | 561.4 | → | potential | `0V` |
| E | 210.1 | 738.4 | → | device ref | `X21.A302` |
| E | 211.5 | 626.2 | → | number | `9` |
| E | 360.3 | 626.2 | → | number | `9` |
| E | 363.1 | 743.0 | → | device ref | `X1.B397` |
| F | 211.5 | 795.7 | → | number | `1` |
| F | 211.5 | 852.9 | → | number | `2` |
| F | 357.5 | 813.0 | → | number | `2` |
| F | 357.5 | 869.7 | → | number | `2` |
| F | 360.3 | 796.3 | → | number | `3` |
| F | 360.3 | 852.4 | → | number | `1` |
| F | 540.3 | 808.4 | → | device tag | `B397` |
| F | 641.3 | 765.1 | → | text | `SENSOR: NULL POSITION,` |
| F | 651.9 | 765.1 | → | text | `SEITENMARKE, B SEITE` |
| F | 662.5 | 764.5 | → | text | `DETECTOR: ZERO POSITION,` |
| F | 673.1 | 765.1 | → | text | `SIDE GUIDE, B SIDE` |
| G | 379.0 | 965.8 | → | text | `NUR BEI` |
| G | 384.4 | 954.1 | → | number | `1` |
| G | 386.1 | 1016.6 | → | text | `+BA` |
| G | 389.7 | 966.3 | → | text | `ONLY FOR` |
| G | 417.3 | 970.9 | → | text | `ANSICHT VON VORNE` |
| G | 428.0 | 970.9 | → | text | `AUF BUCHSENGEHÄUSE` |
| G | 434.0 | 953.9 | → | number | `2` |
| G | 438.6 | 970.0 | → | text | `FRONT VIEW ONTO` |
| G | 449.2 | 970.6 | → | text | `THE SOCKET CASES` |
| H | 429.6 | 1117.7 | → | number | `4` |
| H | 442.4 | 1104.9 | → | number | `3` |
| H | 442.4 | 1130.9 | → | number | `1` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
 129.3   94.1  devtag       A302
 142.4   96.4  xref         /109.A
 154.8   96.4  xref         /107.A
 210.1  114.8  devref       X20.A302
 211.5  172.1  numeric      1
 360.3  172.1  numeric      1
 363.1  117.6  devref       X1.M397
 497.8   92.4  net          M397
 641.3  127.0  text         MOTOR: SEITENMARKE (B SEITE)
 651.9  127.0  text         MOTOR: SIDE GUIDE (B SIDE)
 697.1   83.3  numeric      1
=== Column B ===
  87.5  231.6  net          24V
 211.5  229.3  numeric      2
 211.5  286.0  numeric      3
 360.3  229.3  numeric      2
 360.3  286.0  numeric      3
 428.6  285.1  text         FREIGABE RS485
 439.3  286.5  text         RELEASE RS485
 441.8  217.4  net          24V
=== Column C ===
 211.5  342.7  numeric      4
 211.5  399.4  numeric      5
 211.5  456.1  numeric      6
 360.3  342.7  numeric      4
 360.3  399.4  numeric      5
 360.3  456.1  numeric      6
 428.6  380.6  text         FREIGABE
 428.7  452.7  text         NULL POSITION
 439.3  360.6  text         POSITIONIERANTRIEBE
 439.3  453.5  text         ZERO POSITION
 449.9  382.0  text         RELEASE
 460.5  363.4  text         POSITIONING DRIVES
 540.3  392.5  text         M
 641.3  396.6  text         SEITENMARKE: AUF MAX FORMAT
 651.9  396.6  text         SIDE GUIDE: TO MAX SIZE
 683.8  396.6  text         SEITENMARKE: AUF MIN FORMAT
 694.4  396.6  text         SIDE GUIDE: TO MIN SIZE
=== Column D ===
  87.4  575.6  net          0V
 100.9  540.0  devtag       F11
 122.5  533.5  text         T6,3A
 211.5  512.8  numeric      7
 211.5  569.5  numeric      8
 360.3  512.8  numeric      7
 360.3  569.5  numeric      8
 441.8  561.4  net          0V
=== Column E ===
 210.1  738.4  devref       X21.A302
 211.5  626.2  numeric      9
 360.3  626.2  numeric      9
 363.1  743.0  devref       X1.B397
=== Column F ===
 211.5  795.7  numeric      1
 211.5  852.9  numeric      2
 357.5  813.0  numeric      2
 357.5  869.7  numeric      2
 360.3  796.3  numeric      3
 360.3  852.4  numeric      1
 540.3  808.4  devtag       B397
 641.3  765.1  text         SENSOR: NULL POSITION,
 651.9  765.1  text         SEITENMARKE, B SEITE
 662.5  764.5  text         DETECTOR: ZERO POSITION,
 673.1  765.1  text         SIDE GUIDE, B SIDE
=== Column G ===
 379.0  965.8  text         NUR BEI
 384.4  954.1  numeric      1
 386.1 1016.6  text         +BA
 389.7  966.3  text         ONLY FOR
 417.3  970.9  text         ANSICHT VON VORNE
 428.0  970.9  text         AUF BUCHSENGEHÄUSE
 434.0  953.9  numeric      2
 438.6  970.0  text         FRONT VIEW ONTO
 449.2  970.6  text         THE SOCKET CASES
=== Column H ===
 429.6 1117.7  numeric      4
 442.4 1104.9  numeric      3
 442.4 1130.9  numeric      1
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_BA_CX_DA_8039G38J415_p`, sheet 108._
