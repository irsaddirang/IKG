---
doc: "+BA_Cx_DA"
sheet: 106
sheet_total: 247
document_code: "8039G38J415"
section_de: "MOTOR: SCHRÄGREGISTER"
section_en: "MOTOR: TRANSVERSAL REGISTER"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "28.06.10"
image: "../../../images/+BA_Cx_DA/BA_Cx_DA_0106.png"
columns: "A-B-C-D-E-F-G-H"
---

# +BA_Cx_DA — Sheet 106 of 247 — MOTOR: SCHRÄGREGISTER

**MOTOR: TRANSVERSAL REGISTER**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+BA_Cx_DA` covers the **Printing units / main switch cabinet** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+BA_Cx_DA`  (8039G38J415) |
| Sheet | **106** of 247 |
| Section (DE) | MOTOR: SCHRÄGREGISTER |
| Section (EN) | MOTOR: TRANSVERSAL REGISTER |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 28.06.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G, H |
| Path numbers | — |
| Labels on sheet | 73 |
| Cross-refs out | 2 |
| Cross-refs in | 24 |

**Previous:** [+BA_Cx_DA sheet 105](SHEET_0105.md) · **Next:** [+BA_Cx_DA sheet 107](SHEET_0107.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+BA_Cx_DA) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+BA_Cx_DA sheet 106](../../../images/+BA_Cx_DA/BA_Cx_DA_0106.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/107.A` | [+BA_Cx_DA sheet 107](SHEET_0107.md) | A | — | — | MOTOR: SEITENMARKE, A SEITE | A |
| `/105.A` | [+BA_Cx_DA sheet 105](SHEET_0105.md) | A | — | — | MOTOR: SEITENREGISTER | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+BA_Cx_DA#105](SHEET_0105.md) | A | `/105.A` | — | 1 | — |
| [+BA_Cx_DA#107](SHEET_0107.md) | A | `/107.A` | — | 1 | — |
| [+BA_Cx_DA#145](SHEET_0145.md) | H | `/145.H` | — | 2 | — |
| [+BA_Cx_DA#148](SHEET_0148.md) | B | `/148.B` | — | 9 | — |
| [+BA_Cx_DA#165](SHEET_0165.md) | C | `/165.C` | — | 9 | — |
| [+BA_Cx_DA#166](SHEET_0166.md) | B | `/166.B` | — | 2 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `B339` | B | Umformer / transducer, sensor | F | — | — | — |
| `A302` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `F5` | F | Schutz / protection device (fuse, circuit breaker) | D | — | — | — |
| `X1.M339` | — | cross-device reference | A | — | — | — |
| `X1.B339` | — | cross-device reference | E | — | — | — |
| `X8.A302` | — | cross-device reference | A | — | — | — |
| `X9.A302` | — | cross-device reference | F | — | — | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `0V` | 2 | D | — | — |
| `24V` | 2 | B | — | — |
| `M339` | 1 | A | — | — |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| C | 87.4 | — | — | `24V 0V` |
| D | 115.1 | — | — | `F5` |
| D | 128.1 | — | — | `T6,3A` |
| A | 129.3 | — | — | `A302` |
| A | 142.3 | — | `/107.A`, `/105.A` | — |
| A | 210.1 | — | — | `X8.A302 1` |
| F | 210.1 | — | — | `X9.A302 1` |
| C | 211.5 | — | — | `2 3 4 5 6 7 8 9` |
| F | 211.5 | — | — | `2` |
| A | 222.8 | — | — | `+Cx,DA` |
| F | 222.8 | — | — | `+Cx,DA` |
| F | 357.5 | — | — | `2 2` |
| C | 360.3 | — | — | `X1.M339 1 2 3 4 5 6 7 8 9` |
| F | 360.3 | — | — | `X1.B339 3 1` |
| G | 364.8 | — | — | `1 NUR BEI` |
| G | 372.0 | — | — | `ONLY FOR +Cx,DA` |
| G | 410.2 | — | — | `FRONT VIEW ONTO ANSICHT VON VORNE AUF BUCHSENGEHÄUSE` |
| G | 422.5 | — | — | `2 THE SOCKET CASES 4` |
| B | 428.6 | — | — | `FREIGABE RS485` |
| C | 428.6 | — | — | `POSITIONIERANTRIEBE FREIGABE` |
| D | 428.6 | — | — | `NULL POSITION` |
| H | 435.3 | — | — | `3 1` |
| B | 439.3 | — | — | `RELEASE RS485` |
| D | 439.3 | — | — | `ZERO POSITION` |
| C | 441.8 | — | — | `24V 0V` |
| C | 449.9 | — | — | `POSITIONING DRIVES RELEASE` |
| A | 497.8 | — | — | `M339` |
| C | 540.3 | — | — | `M` |
| F | 540.3 | — | — | `B339` |
| F | 641.2 | — | — | `DETECTOR: ZERO POSITION, SENSOR: NULL POSITION, SCHRÄGREGISTER` |
| A | 641.3 | — | — | `MOTOR: SCHRÄGREGISTER MOTOR: TRANSVERSAL REGISTER` |
| C | 641.3 | — | — | `TRANSFERTROMMEL: B SEITE NACH OBEN TRANSFER DRUM: B SIDE UP` |
| F | 673.1 | — | — | `TRANSVERSAL REGISTER` |
| C | 683.8 | — | — | `TRANSFERTROMMEL: B SEITE NACH UNTEN TRANSFER DRUM: B SIDE DOWN` |
| A | 697.1 | — | — | `1` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `M` | C | 540.33 |
| `MOTOR: SCHRÄGREGISTER` | A | 641.27 |
| `MOTOR: TRANSVERSAL REGISTER` | A | 651.89 |
| `SENSOR: NULL POSITION,` | F | 641.25 |
| `SCHRÄGREGISTER` | F | 651.9 |
| `DETECTOR: ZERO POSITION,` | F | 662.51 |
| `TRANSVERSAL REGISTER` | F | 673.15 |
| `+Cx,DA` | A | 222.83 |
| `T6,3A` | D | 128.12 |
| `+Cx,DA` | F | 222.83 |
| `FREIGABE` | C | 428.61 |
| `POSITIONIERANTRIEBE` | C | 439.27 |
| `RELEASE` | C | 449.88 |
| `POSITIONING DRIVES` | C | 460.54 |
| `FREIGABE RS485` | B | 428.64 |
| `RELEASE RS485` | B | 439.28 |
| `NULL POSITION` | D | 428.65 |
| `ZERO POSITION` | D | 439.29 |
| `TRANSFERTROMMEL: B SEITE NACH OBEN` | C | 641.26 |
| `TRANSFER DRUM: B SIDE UP` | C | 651.9 |
| `TRANSFERTROMMEL: B SEITE NACH UNTEN` | C | 683.79 |
| `TRANSFER DRUM: B SIDE DOWN` | C | 694.4 |
| `ANSICHT VON VORNE` | G | 410.24 |
| `AUF BUCHSENGEHÄUSE` | G | 420.87 |
| `FRONT VIEW ONTO` | G | 431.47 |
| `THE SOCKET CASES` | G | 442.11 |
| `NUR BEI` | G | 364.83 |
| `ONLY FOR` | G | 375.52 |
| `+Cx,DA` | G | 372.01 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 129.3 | 108.3 | → | device tag | `A302` |
| A | 142.4 | 110.6 | → | cross-reference | `/107.A` |
| A | 154.8 | 110.6 | → | cross-reference | `/105.A` |
| A | 210.1 | 134.9 | → | device ref | `X8.A302` |
| A | 211.5 | 186.2 | → | number | `1` |
| A | 222.8 | 142.0 | → | text | `+Cx,DA` |
| A | 360.3 | 186.2 | → | number | `1` |
| A | 363.1 | 131.8 | → | device ref | `X1.M339` |
| A | 497.8 | 92.4 | → | potential | `M339` |
| A | 641.3 | 127.0 | → | text | `MOTOR: SCHRÄGREGISTER` |
| A | 651.9 | 127.0 | → | text | `MOTOR: TRANSVERSAL REGISTER` |
| A | 697.1 | 83.3 | → | number | `1` |
| B | 87.5 | 247.7 | → | potential | `24V` |
| B | 211.5 | 243.5 | → | number | `2` |
| B | 211.5 | 300.2 | → | number | `3` |
| B | 360.3 | 243.5 | → | number | `2` |
| B | 360.3 | 300.2 | → | number | `3` |
| B | 428.6 | 299.3 | → | text | `FREIGABE RS485` |
| B | 439.3 | 300.7 | → | text | `RELEASE RS485` |
| B | 441.8 | 231.6 | → | potential | `24V` |
| C | 211.5 | 356.9 | → | number | `4` |
| C | 211.5 | 413.6 | → | number | `5` |
| C | 211.5 | 470.3 | → | number | `6` |
| C | 360.3 | 356.9 | → | number | `4` |
| C | 360.3 | 413.6 | → | number | `5` |
| C | 360.3 | 470.3 | → | number | `6` |
| C | 428.6 | 394.8 | → | text | `FREIGABE` |
| C | 439.3 | 374.8 | → | text | `POSITIONIERANTRIEBE` |
| C | 449.9 | 396.2 | → | text | `RELEASE` |
| C | 460.5 | 377.6 | → | text | `POSITIONING DRIVES` |
| C | 540.3 | 406.6 | → | text | `M` |
| C | 641.3 | 410.7 | → | text | `TRANSFERTROMMEL: B SEITE NACH OBEN` |
| C | 651.9 | 410.7 | → | text | `TRANSFER DRUM: B SIDE UP` |
| C | 683.8 | 410.7 | → | text | `TRANSFERTROMMEL: B SEITE NACH UNTEN` |
| C | 694.4 | 410.7 | → | text | `TRANSFER DRUM: B SIDE DOWN` |
| D | 87.4 | 589.7 | → | potential | `0V` |
| D | 115.1 | 558.7 | → | device tag | `F5` |
| D | 128.1 | 548.5 | → | text | `T6,3A` |
| D | 211.5 | 527.0 | → | number | `7` |
| D | 211.5 | 583.7 | → | number | `8` |
| D | 360.3 | 527.0 | → | number | `7` |
| D | 360.3 | 583.7 | → | number | `8` |
| D | 428.7 | 466.9 | → | text | `NULL POSITION` |
| D | 439.3 | 467.7 | → | text | `ZERO POSITION` |
| D | 441.8 | 575.6 | → | potential | `0V` |
| E | 211.5 | 640.3 | → | number | `9` |
| E | 360.3 | 640.3 | → | number | `9` |
| E | 363.1 | 743.0 | → | device ref | `X1.B339` |
| F | 210.1 | 744.4 | → | device ref | `X9.A302` |
| F | 211.5 | 795.7 | → | number | `1` |
| F | 211.5 | 852.9 | → | number | `2` |
| F | 222.8 | 751.5 | → | text | `+Cx,DA` |
| F | 357.5 | 813.0 | → | number | `2` |
| F | 357.5 | 869.7 | → | number | `2` |
| F | 360.3 | 796.3 | → | number | `3` |
| F | 360.3 | 852.4 | → | number | `1` |
| F | 540.3 | 808.4 | → | device tag | `B339` |
| F | 641.3 | 765.1 | → | text | `SENSOR: NULL POSITION,` |
| F | 651.9 | 765.1 | → | text | `SCHRÄGREGISTER` |
| F | 662.5 | 764.5 | → | text | `DETECTOR: ZERO POSITION,` |
| F | 673.2 | 765.1 | → | text | `TRANSVERSAL REGISTER` |
| G | 364.8 | 965.8 | → | text | `NUR BEI` |
| G | 370.2 | 954.1 | → | number | `1` |
| G | 372.0 | 1020.2 | → | text | `+Cx,DA` |
| G | 375.5 | 966.3 | → | text | `ONLY FOR` |
| G | 410.2 | 970.9 | → | text | `ANSICHT VON VORNE` |
| G | 420.9 | 970.9 | → | text | `AUF BUCHSENGEHÄUSE` |
| G | 426.9 | 953.9 | → | number | `2` |
| G | 431.5 | 970.0 | → | text | `FRONT VIEW ONTO` |
| G | 442.1 | 970.6 | → | text | `THE SOCKET CASES` |
| H | 422.5 | 1096.4 | → | number | `4` |
| H | 435.3 | 1083.7 | → | number | `3` |
| H | 435.3 | 1109.6 | → | number | `1` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
 129.3  108.3  devtag       A302
 142.4  110.6  xref         /107.A
 154.8  110.6  xref         /105.A
 210.1  134.9  devref       X8.A302
 211.5  186.2  numeric      1
 222.8  142.0  text         +Cx,DA
 360.3  186.2  numeric      1
 363.1  131.8  devref       X1.M339
 497.8   92.4  net          M339
 641.3  127.0  text         MOTOR: SCHRÄGREGISTER
 651.9  127.0  text         MOTOR: TRANSVERSAL REGISTER
 697.1   83.3  numeric      1
=== Column B ===
  87.5  247.7  net          24V
 211.5  243.5  numeric      2
 211.5  300.2  numeric      3
 360.3  243.5  numeric      2
 360.3  300.2  numeric      3
 428.6  299.3  text         FREIGABE RS485
 439.3  300.7  text         RELEASE RS485
 441.8  231.6  net          24V
=== Column C ===
 211.5  356.9  numeric      4
 211.5  413.6  numeric      5
 211.5  470.3  numeric      6
 360.3  356.9  numeric      4
 360.3  413.6  numeric      5
 360.3  470.3  numeric      6
 428.6  394.8  text         FREIGABE
 439.3  374.8  text         POSITIONIERANTRIEBE
 449.9  396.2  text         RELEASE
 460.5  377.6  text         POSITIONING DRIVES
 540.3  406.6  text         M
 641.3  410.7  text         TRANSFERTROMMEL: B SEITE NACH OBEN
 651.9  410.7  text         TRANSFER DRUM: B SIDE UP
 683.8  410.7  text         TRANSFERTROMMEL: B SEITE NACH UNTEN
 694.4  410.7  text         TRANSFER DRUM: B SIDE DOWN
=== Column D ===
  87.4  589.7  net          0V
 115.1  558.7  devtag       F5
 128.1  548.5  text         T6,3A
 211.5  527.0  numeric      7
 211.5  583.7  numeric      8
 360.3  527.0  numeric      7
 360.3  583.7  numeric      8
 428.7  466.9  text         NULL POSITION
 439.3  467.7  text         ZERO POSITION
 441.8  575.6  net          0V
=== Column E ===
 211.5  640.3  numeric      9
 360.3  640.3  numeric      9
 363.1  743.0  devref       X1.B339
=== Column F ===
 210.1  744.4  devref       X9.A302
 211.5  795.7  numeric      1
 211.5  852.9  numeric      2
 222.8  751.5  text         +Cx,DA
 357.5  813.0  numeric      2
 357.5  869.7  numeric      2
 360.3  796.3  numeric      3
 360.3  852.4  numeric      1
 540.3  808.4  devtag       B339
 641.3  765.1  text         SENSOR: NULL POSITION,
 651.9  765.1  text         SCHRÄGREGISTER
 662.5  764.5  text         DETECTOR: ZERO POSITION,
 673.2  765.1  text         TRANSVERSAL REGISTER
=== Column G ===
 364.8  965.8  text         NUR BEI
 370.2  954.1  numeric      1
 372.0 1020.2  text         +Cx,DA
 375.5  966.3  text         ONLY FOR
 410.2  970.9  text         ANSICHT VON VORNE
 420.9  970.9  text         AUF BUCHSENGEHÄUSE
 426.9  953.9  numeric      2
 431.5  970.0  text         FRONT VIEW ONTO
 442.1  970.6  text         THE SOCKET CASES
=== Column H ===
 422.5 1096.4  numeric      4
 435.3 1083.7  numeric      3
 435.3 1109.6  numeric      1
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_BA_CX_DA_8039G38J415_p`, sheet 106._
