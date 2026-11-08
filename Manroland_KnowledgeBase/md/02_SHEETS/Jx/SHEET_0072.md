---
doc: "+Jx"
sheet: 72
sheet_total: 214
document_code: "039G38F308"
section_de: "MOTOR: SCHRÄGREGISTER"
section_en: "MOTOR: TRANSVERSAL REGISTER"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "03.01.10"
image: "../../../images/+Jx/Jx_0072.png"
columns: "A-B-C-D-E-F"
---

# +Jx — Sheet 72 of 214 — MOTOR: SCHRÄGREGISTER

**MOTOR: TRANSVERSAL REGISTER**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+Jx` covers the **1st printing module + feed register** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+Jx`  (039G38F308) |
| Sheet | **72** of 214 |
| Section (DE) | MOTOR: SCHRÄGREGISTER |
| Section (EN) | MOTOR: TRANSVERSAL REGISTER |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 03.01.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F |
| Path numbers | — |
| Labels on sheet | 66 |
| Cross-refs out | 2 |
| Cross-refs in | 24 |

**Previous:** [+Jx sheet 71](SHEET_0071.md) · **Next:** [+Jx sheet 73](SHEET_0073.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+Jx) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+Jx sheet 72](../../../images/+Jx/Jx_0072.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/73.A` | [+Jx sheet 73](SHEET_0073.md) | A | — | — | BEDRUCKSTOFFEINSTELLUNG | A |
| `/71.A` | [+Jx sheet 71](SHEET_0071.md) | A | — | — | MOTOR: SEITENREGISTER | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+Jx#71](SHEET_0071.md) | A | `/71.A` | — | 1 | — |
| [+Jx#73](SHEET_0073.md) | A | `/73.A` | — | 1 | — |
| [+Jx#117](SHEET_0117.md) | C | `/117.C` | — | 2 | — |
| [+Jx#118](SHEET_0118.md) | G | `/118.G` | — | 9 | — |
| [+Jx#133](SHEET_0133.md) | G | `/133.G` | — | 9 | — |
| [+Jx#134](SHEET_0134.md) | E | `/134.E` | — | 2 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `A302` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `B339` | B | Umformer / transducer, sensor | F | — | — | — |
| `F5` | F | Schutz / protection device (fuse, circuit breaker) | D | — | — | — |
| `X8.A302` | — | cross-device reference | A | — | — | — |
| `X9.A302` | — | cross-device reference | F | — | — | — |
| `X1.M339` | — | cross-device reference | A | — | — | — |
| `X1.B339` | — | cross-device reference | E | — | — | — |

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
| B | 87.4 | — | — | `24V` |
| D | 87.4 | — | — | `0V` |
| D | 115.0 | — | — | `F5` |
| C | 128.1 | — | — | `A302 T6,3A` |
| A | 156.4 | — | `/73.A`, `/71.A` | — |
| C | 238.3 | — | — | `X8.A302 1 2 3 4 5 6 7 8 9` |
| F | 238.3 | — | — | `X9.A302 1 2` |
| F | 328.6 | — | — | `1 1` |
| C | 331.9 | — | — | `X1.M339 1 2 3 4 5 6 7 8 9` |
| F | 331.9 | — | — | `X1.B339 3 1` |
| B | 400.2 | — | — | `FREIGABE RS485` |
| C | 400.2 | — | — | `POSITIONIERANTRIEBE FREIGABE` |
| D | 400.3 | — | — | `NULL POSITION` |
| B | 410.9 | — | — | `RELEASE RS485` |
| D | 410.9 | — | — | `ZERO POSITION` |
| C | 413.4 | — | — | `24V 0V` |
| C | 421.5 | — | — | `POSITIONING DRIVES RELEASE` |
| A | 469.4 | — | — | `M339` |
| C | 511.9 | — | — | `M` |
| F | 511.9 | — | — | `B339` |
| A | 612.9 | — | — | `MOTOR: SCHRÄGREGISTER MOTOR: TRANSVERSAL REGISTER` |
| C | 612.9 | — | — | `TRANSFERTROMMEL: B SEITE NACH OBEN TRANSFER DRUM: B SIDE UP` |
| F | 612.9 | — | — | `DETECTOR: ZERO POSITION, SENSOR: NULL POSITION, SCHRÄGREGISTER` |
| F | 644.8 | — | — | `TRANSVERSAL REGISTER` |
| C | 655.4 | — | — | `TRANSFERTROMMEL: B SEITE NACH UNTEN TRANSFER DRUM: B SIDE DOWN` |
| A | 707.8 | — | — | `FRONT VIEW ONTO ANSICHT VON VORNE AUF BUCHSENGEHÄUSE` |
| A | 720.1 | — | — | `1 THE SOCKET CASES 4` |
| B | 732.9 | — | — | `3 1` |


## Reconstructed tables

This sheet carries tabular content (pin map / terminal assignment / index). The grid below was rebuilt from the drawing's own rule lines, so each row is exactly one physical row of the table.

### Table 1 — 2 data rows × 4 columns (at x=85.0, y=147.4) — **A302 /73.A /71.A**

| X8.A302 X1.M339 | 1 1 |  | 2 2 |
|---|---|---|---|
| `M339 MOTOR: MOTOR:` | `TRANSVERSAL` | `24V SCHRÄGREGISTER REGISTER` |  |
| `ANSICHT VON VORNE AUF BUCHSENGEHÄUSE FRONT VIEW ONTO THE SOCKET CASES` |  | `4 3 1` |  |


### Table 2 — 1 data rows × 7 columns (at x=297.6, y=147.4)

| 3 3 | 4 4 | 5 5 |  | 6 6 | 7 7 | 8 8 |
|---|---|---|---|---|---|---|
| `FREIGABE RS485 RELEASE RS485` | `FREIGABE POSITIONIERANTRIEBE RELEASE POSITIONING` | `DRIVES M TRANSFERTROMMEL: TRANSFER DRUM: TRANSFERTROMMEL: TRANSFER DRUM:` | `B SIDE B SIDE` | `NULL POSITION ZERO POSITION B SEITE NACH OBEN UP B SEITE NACH UNTEN DOWN` |  |  |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `T6,3A` | D | 128.06 |
| `M` | C | 511.92 |
| `MOTOR: SCHRÄGREGISTER` | A | 612.88 |
| `MOTOR: TRANSVERSAL REGISTER` | A | 623.5 |
| `SENSOR: NULL POSITION,` | F | 612.86 |
| `SCHRÄGREGISTER` | F | 623.51 |
| `DETECTOR: ZERO POSITION,` | F | 634.12 |
| `TRANSVERSAL REGISTER` | F | 644.76 |
| `ANSICHT VON VORNE` | A | 707.83 |
| `AUF BUCHSENGEHÄUSE` | A | 718.46 |
| `FRONT VIEW ONTO` | A | 729.06 |
| `THE SOCKET CASES` | A | 739.71 |
| `FREIGABE` | C | 400.23 |
| `POSITIONIERANTRIEBE` | C | 410.88 |
| `RELEASE` | C | 421.5 |
| `POSITIONING DRIVES` | C | 432.15 |
| `FREIGABE RS485` | B | 400.25 |
| `RELEASE RS485` | B | 410.89 |
| `NULL POSITION` | D | 400.27 |
| `ZERO POSITION` | D | 410.9 |
| `TRANSFERTROMMEL: B SEITE NACH OBEN` | C | 612.87 |
| `TRANSFER DRUM: B SIDE UP` | C | 623.51 |
| `TRANSFERTROMMEL: B SEITE NACH UNTEN` | C | 655.4 |
| `TRANSFER DRUM: B SIDE DOWN` | C | 666.01 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 143.4 | 108.3 | → | device tag | `A302` |
| A | 156.5 | 115.4 | → | cross-reference | `/73.A` |
| A | 168.9 | 115.4 | → | cross-reference | `/71.A` |
| A | 238.4 | 134.9 | → | device ref | `X8.A302` |
| A | 239.8 | 186.2 | → | number | `1` |
| A | 331.9 | 186.2 | → | number | `1` |
| A | 334.7 | 131.5 | → | device ref | `X1.M339` |
| A | 469.4 | 106.3 | → | potential | `M339` |
| A | 612.9 | 141.2 | → | text | `MOTOR: SCHRÄGREGISTER` |
| A | 623.5 | 141.2 | → | text | `MOTOR: TRANSVERSAL REGISTER` |
| A | 707.8 | 92.1 | → | text | `ANSICHT VON VORNE` |
| A | 718.5 | 92.1 | → | text | `AUF BUCHSENGEHÄUSE` |
| A | 724.5 | 75.4 | → | number | `1` |
| A | 729.1 | 91.6 | → | text | `FRONT VIEW ONTO` |
| A | 739.7 | 92.1 | → | text | `THE SOCKET CASES` |
| B | 87.4 | 245.8 | → | potential | `24V` |
| B | 239.8 | 243.8 | → | number | `2` |
| B | 239.8 | 300.2 | → | number | `3` |
| B | 331.9 | 243.8 | → | number | `2` |
| B | 331.9 | 300.2 | → | number | `3` |
| B | 400.3 | 299.5 | → | text | `FREIGABE RS485` |
| B | 410.9 | 300.9 | → | text | `RELEASE RS485` |
| B | 413.4 | 231.6 | → | potential | `24V` |
| B | 720.1 | 217.8 | → | number | `4` |
| B | 732.9 | 204.9 | → | number | `3` |
| B | 732.9 | 230.7 | → | number | `1` |
| C | 239.8 | 357.2 | → | number | `4` |
| C | 239.8 | 413.6 | → | number | `5` |
| C | 239.8 | 470.3 | → | number | `6` |
| C | 331.9 | 357.2 | → | number | `4` |
| C | 331.9 | 413.6 | → | number | `5` |
| C | 331.9 | 470.3 | → | number | `6` |
| C | 400.2 | 394.9 | → | text | `FREIGABE` |
| C | 410.9 | 374.8 | → | text | `POSITIONIERANTRIEBE` |
| C | 421.5 | 396.3 | → | text | `RELEASE` |
| C | 432.2 | 377.7 | → | text | `POSITIONING DRIVES` |
| C | 511.9 | 406.6 | → | text | `M` |
| C | 612.9 | 396.9 | → | text | `TRANSFERTROMMEL: B SEITE NACH OBEN` |
| C | 623.5 | 396.9 | → | text | `TRANSFER DRUM: B SIDE UP` |
| C | 655.4 | 396.9 | → | text | `TRANSFERTROMMEL: B SEITE NACH UNTEN` |
| C | 666.0 | 396.9 | → | text | `TRANSFER DRUM: B SIDE DOWN` |
| D | 87.4 | 589.7 | → | potential | `0V` |
| D | 115.1 | 558.4 | → | device tag | `F5` |
| D | 128.1 | 548.8 | → | text | `T6,3A` |
| D | 239.8 | 527.0 | → | number | `7` |
| D | 239.8 | 583.7 | → | number | `8` |
| D | 331.9 | 527.0 | → | number | `7` |
| D | 331.9 | 583.7 | → | number | `8` |
| D | 400.3 | 467.1 | → | text | `NULL POSITION` |
| D | 410.9 | 467.7 | → | text | `ZERO POSITION` |
| D | 413.4 | 575.6 | → | potential | `0V` |
| E | 239.8 | 640.3 | → | number | `9` |
| E | 331.9 | 640.3 | → | number | `9` |
| E | 334.7 | 742.7 | → | device ref | `X1.B339` |
| F | 238.4 | 744.4 | → | device ref | `X9.A302` |
| F | 239.8 | 795.7 | → | number | `1` |
| F | 239.8 | 853.2 | → | number | `2` |
| F | 328.6 | 813.1 | → | number | `1` |
| F | 328.6 | 869.8 | → | number | `1` |
| F | 331.9 | 796.3 | → | number | `3` |
| F | 331.9 | 852.4 | → | number | `1` |
| F | 511.9 | 808.2 | → | device tag | `B339` |
| F | 612.9 | 765.1 | → | text | `SENSOR: NULL POSITION,` |
| F | 623.5 | 765.1 | → | text | `SCHRÄGREGISTER` |
| F | 634.1 | 764.8 | → | text | `DETECTOR: ZERO POSITION,` |
| F | 644.8 | 765.4 | → | text | `TRANSVERSAL REGISTER` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
 143.4  108.3  devtag       A302
 156.5  115.4  xref         /73.A
 168.9  115.4  xref         /71.A
 238.4  134.9  devref       X8.A302
 239.8  186.2  numeric      1
 331.9  186.2  numeric      1
 334.7  131.5  devref       X1.M339
 469.4  106.3  net          M339
 612.9  141.2  text         MOTOR: SCHRÄGREGISTER
 623.5  141.2  text         MOTOR: TRANSVERSAL REGISTER
 707.8   92.1  text         ANSICHT VON VORNE
 718.5   92.1  text         AUF BUCHSENGEHÄUSE
 724.5   75.4  numeric      1
 729.1   91.6  text         FRONT VIEW ONTO
 739.7   92.1  text         THE SOCKET CASES
=== Column B ===
  87.4  245.8  net          24V
 239.8  243.8  numeric      2
 239.8  300.2  numeric      3
 331.9  243.8  numeric      2
 331.9  300.2  numeric      3
 400.3  299.5  text         FREIGABE RS485
 410.9  300.9  text         RELEASE RS485
 413.4  231.6  net          24V
 720.1  217.8  numeric      4
 732.9  204.9  numeric      3
 732.9  230.7  numeric      1
=== Column C ===
 239.8  357.2  numeric      4
 239.8  413.6  numeric      5
 239.8  470.3  numeric      6
 331.9  357.2  numeric      4
 331.9  413.6  numeric      5
 331.9  470.3  numeric      6
 400.2  394.9  text         FREIGABE
 410.9  374.8  text         POSITIONIERANTRIEBE
 421.5  396.3  text         RELEASE
 432.2  377.7  text         POSITIONING DRIVES
 511.9  406.6  text         M
 612.9  396.9  text         TRANSFERTROMMEL: B SEITE NACH OBEN
 623.5  396.9  text         TRANSFER DRUM: B SIDE UP
 655.4  396.9  text         TRANSFERTROMMEL: B SEITE NACH UNTEN
 666.0  396.9  text         TRANSFER DRUM: B SIDE DOWN
=== Column D ===
  87.4  589.7  net          0V
 115.1  558.4  devtag       F5
 128.1  548.8  text         T6,3A
 239.8  527.0  numeric      7
 239.8  583.7  numeric      8
 331.9  527.0  numeric      7
 331.9  583.7  numeric      8
 400.3  467.1  text         NULL POSITION
 410.9  467.7  text         ZERO POSITION
 413.4  575.6  net          0V
=== Column E ===
 239.8  640.3  numeric      9
 331.9  640.3  numeric      9
 334.7  742.7  devref       X1.B339
=== Column F ===
 238.4  744.4  devref       X9.A302
 239.8  795.7  numeric      1
 239.8  853.2  numeric      2
 328.6  813.1  numeric      1
 328.6  869.8  numeric      1
 331.9  796.3  numeric      3
 331.9  852.4  numeric      1
 511.9  808.2  devtag       B339
 612.9  765.1  text         SENSOR: NULL POSITION,
 623.5  765.1  text         SCHRÄGREGISTER
 634.1  764.8  text         DETECTOR: ZERO POSITION,
 644.8  765.4  text         TRANSVERSAL REGISTER
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_JX_039G38F308_p`, sheet 72._
