---
doc: "+Ax"
sheet: 111
sheet_total: 403
document_code: "8039G38I902"
section_de: "ANLEGEREINSATZPUNKTEINSTELLUNG"
section_en: "(POSITIONIERANTRIEB)"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "17.05.10"
image: "../../../images/+Ax/Ax_0111.png"
columns: "A-B-C-D-E-F-G-H"
---

# +Ax — Sheet 111 of 403 — ANLEGEREINSATZPUNKTEINSTELLUNG

**(POSITIONIERANTRIEB)**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+Ax` covers the **Central control console** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+Ax`  (8039G38I902) |
| Sheet | **111** of 403 |
| Section (DE) | ANLEGEREINSATZPUNKTEINSTELLUNG |
| Section (EN) | (POSITIONIERANTRIEB) |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 17.05.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G, H |
| Path numbers | — |
| Labels on sheet | 72 |
| Cross-refs out | 2 |
| Cross-refs in | 24 |

**Previous:** [+Ax sheet 110](SHEET_0110.md) · **Next:** [+Ax sheet 112](SHEET_0112.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+Ax) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+Ax sheet 111](../../../images/+Ax/Ax_0111.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/112.A` | [+Ax sheet 112](SHEET_0112.md) | A | — | — | FORMATEINSTELLUNG MOTORISCH, SEITLICHE | A |
| `/110.A` | [+Ax sheet 110](SHEET_0110.md) | A | — | — | SAUGKOPF LÄNGSEINSTELLUNG / | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+Ax#110](SHEET_0110.md) | A | `/110.A` | — | 1 | — |
| [+Ax#112](SHEET_0112.md) | A | `/112.A` | — | 1 | — |
| [+Ax#213](SHEET_0213.md) | F | `/213.F` | — | 2 | — |
| [+Ax#214](SHEET_0214.md) | F | `/214.F` | — | 9 | — |
| [+Ax#237](SHEET_0237.md) | F | `/237.F` | — | 9 | — |
| [+Ax#240](SHEET_0240.md) | E | `/240.E` | — | 2 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `A302` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `B342` | B | Umformer / transducer, sensor | F | — | — | — |
| `X1.M342` | — | cross-device reference | A | — | — | — |
| `X1.B342` | — | cross-device reference | E | — | — | — |
| `X9.A302` | — | cross-device reference | E | — | — | — |
| `X8.A302` | — | cross-device reference | A | — | — | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `0V` | 2 | D | — | — |
| `24V` | 2 | B | — | — |
| `M342` | 1 | A | — | — |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| D | 66.2 | — | — | `0V` |
| D | 87.4 | — | — | `F5 6,3A T` |
| B | 87.5 | — | — | `24V` |
| A | 129.3 | — | — | `A302` |
| A | 142.0 | — | — | `+AB` |
| A | 157.2 | — | `/112.A`, `/110.A` | — |
| A | 210.1 | — | — | `X8.A302 1` |
| E | 210.1 | — | — | `X9.A302 1` |
| C | 211.5 | — | — | `2 3 4 5 6 7 8 9` |
| F | 211.5 | — | — | `2` |
| A | 222.8 | — | — | `+AB` |
| E | 222.8 | — | — | `+AB` |
| A | 341.9 | — | — | `X1.M342` |
| E | 341.9 | — | — | `X1.B342` |
| C | 354.6 | — | — | `+AB 2 3 4 3` |
| E | 354.6 | — | — | `5 6 7 8 9 +AB 1` |
| F | 356.9 | — | — | `1 1` |
| A | 360.3 | — | — | `1` |
| B | 428.6 | — | — | `FREIGABE RS485` |
| C | 428.6 | — | — | `POSITIONIERANTRIEBE FREIGABE` |
| D | 428.6 | — | — | `NULL POSITION` |
| B | 439.3 | — | — | `RELEASE RS485` |
| D | 439.3 | — | — | `ZERO POSITION` |
| C | 441.8 | — | — | `24V 0V` |
| C | 449.9 | — | — | `POSITIONING DRIVES RELEASE` |
| A | 497.8 | — | — | `M342` |
| A | 510.5 | — | — | `+AB` |
| C | 540.3 | — | — | `M` |
| F | 540.3 | — | — | `B342` |
| F | 553.0 | — | — | `+AB` |
| G | 580.3 | — | — | `FRONT VIEW ONTO ANSICHT VON VORNE AUF BUCHSENGEHÄUSE` |
| G | 592.6 | — | — | `1 THE SOCKET CASES 4` |
| H | 605.4 | — | — | `3 1` |
| F | 641.2 | — | — | `DETECTOR: ZERO POSITION, FEEDER TIMING SENSOR: NULL POSITION, ANLEGEREINSATZPUNKT` |
| C | 641.3 | — | — | `MOTOR: ANLEGEREINSATZPUNKTEINSTELLUNG MOTOR: FEEDER TIMING` |
| C | 690.9 | — | — | `BOGENANKUNFT, SPÄTER` |
| C | 701.5 | — | — | `SHEET ARRIVAL, LATER` |
| C | 726.3 | — | — | `BOGENANKUNFT, FRÜHER` |
| C | 736.9 | — | — | `SHEET ARRIVAL, EARLIER` |


## Reconstructed tables

This sheet carries tabular content (pin map / terminal assignment / index). The grid below was rebuilt from the drawing's own rule lines, so each row is exactly one physical row of the table.

### Table 1 — 2 data rows × 4 columns (at x=779.5, y=104.9)

| 1 1 3 | 2 1 1 |  |  |
|---|---|---|---|
| `B342 +AB` |  |  |  |
|  | `1` | `ANSICHT VON VORNE AUF BUCHSENGEHÄUSE FRONT VIEW ONTO THE SOCKET CASES` | `4 3 1` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `+AB` | A | 510.47 |
| `MOTOR: ANLEGEREINSATZPUNKTEINSTELLUNG` | C | 641.26 |
| `MOTOR: FEEDER TIMING` | C | 651.89 |
| `+AB` | E | 354.56 |
| `M` | C | 540.33 |
| `+AB` | F | 552.99 |
| `SENSOR: NULL POSITION,` | F | 641.25 |
| `ANLEGEREINSATZPUNKT` | F | 651.89 |
| `DETECTOR: ZERO POSITION,` | F | 662.51 |
| `FEEDER TIMING` | F | 673.14 |
| `FREIGABE` | C | 428.61 |
| `POSITIONIERANTRIEBE` | C | 439.27 |
| `RELEASE` | C | 449.88 |
| `POSITIONING DRIVES` | C | 460.54 |
| `FREIGABE RS485` | B | 428.64 |
| `RELEASE RS485` | B | 439.28 |
| `NULL POSITION` | D | 428.65 |
| `ZERO POSITION` | D | 439.29 |
| `ANSICHT VON VORNE` | G | 580.32 |
| `AUF BUCHSENGEHÄUSE` | G | 590.95 |
| `FRONT VIEW ONTO` | G | 601.54 |
| `THE SOCKET CASES` | G | 612.19 |
| `F5 6,3A T` | D | 87.43 |
| `BOGENANKUNFT, SPÄTER` | C | 690.86 |
| `SHEET ARRIVAL, LATER` | C | 701.49 |
| `BOGENANKUNFT, FRÜHER` | C | 726.3 |
| `SHEET ARRIVAL, EARLIER` | C | 736.92 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 129.3 | 108.3 | → | device tag | `A302` |
| A | 142.0 | 116.2 | → | text | `+AB` |
| A | 157.2 | 110.6 | → | cross-reference | `/112.A` |
| A | 169.6 | 110.6 | → | cross-reference | `/110.A` |
| A | 210.1 | 134.9 | → | device ref | `X8.A302` |
| A | 211.5 | 186.2 | → | number | `1` |
| A | 222.8 | 158.7 | → | text | `+AB` |
| A | 341.9 | 131.8 | → | device ref | `X1.M342` |
| A | 354.6 | 157.3 | → | text | `+AB` |
| A | 360.3 | 186.2 | → | number | `1` |
| A | 497.8 | 106.6 | → | potential | `M342` |
| A | 510.5 | 116.2 | → | text | `+AB` |
| B | 87.5 | 245.8 | → | potential | `24V` |
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
| C | 641.3 | 396.3 | → | text | `MOTOR: ANLEGEREINSATZPUNKTEINSTELLUNG` |
| C | 651.9 | 396.3 | → | text | `MOTOR: FEEDER TIMING` |
| C | 690.9 | 438.5 | → | text | `BOGENANKUNFT, SPÄTER` |
| C | 701.5 | 439.1 | → | text | `SHEET ARRIVAL, LATER` |
| C | 726.3 | 438.5 | → | text | `BOGENANKUNFT, FRÜHER` |
| C | 736.9 | 439.1 | → | text | `SHEET ARRIVAL, EARLIER` |
| D | 66.2 | 589.7 | → | potential | `0V` |
| D | 87.4 | 595.0 | → | text | `F5 6,3A T` |
| D | 211.5 | 527.0 | → | number | `7` |
| D | 211.5 | 583.7 | → | number | `8` |
| D | 360.3 | 527.0 | → | number | `7` |
| D | 360.3 | 583.7 | → | number | `8` |
| D | 428.7 | 466.9 | → | text | `NULL POSITION` |
| D | 439.3 | 467.7 | → | text | `ZERO POSITION` |
| D | 441.8 | 575.6 | → | potential | `0V` |
| E | 210.1 | 730.2 | → | device ref | `X9.A302` |
| E | 211.5 | 640.3 | → | number | `9` |
| E | 222.8 | 754.0 | → | text | `+AB` |
| E | 341.9 | 728.8 | → | device ref | `X1.B342` |
| E | 354.6 | 752.6 | → | text | `+AB` |
| E | 360.3 | 640.3 | → | number | `9` |
| F | 211.5 | 781.5 | → | number | `1` |
| F | 211.5 | 838.8 | → | number | `2` |
| F | 356.9 | 799.0 | → | number | `1` |
| F | 356.9 | 855.7 | → | number | `1` |
| F | 360.3 | 782.1 | → | number | `3` |
| F | 360.3 | 838.2 | → | number | `1` |
| F | 540.3 | 794.3 | → | device tag | `B342` |
| F | 553.0 | 802.2 | → | text | `+AB` |
| F | 641.3 | 750.9 | → | text | `SENSOR: NULL POSITION,` |
| F | 651.9 | 751.2 | → | text | `ANLEGEREINSATZPUNKT` |
| F | 662.5 | 750.3 | → | text | `DETECTOR: ZERO POSITION,` |
| F | 673.1 | 750.3 | → | text | `FEEDER TIMING` |
| G | 580.3 | 942.5 | → | text | `ANSICHT VON VORNE` |
| G | 591.0 | 942.5 | → | text | `AUF BUCHSENGEHÄUSE` |
| G | 597.0 | 925.8 | → | number | `1` |
| G | 601.5 | 941.7 | → | text | `FRONT VIEW ONTO` |
| G | 612.2 | 942.2 | → | text | `THE SOCKET CASES` |
| H | 592.6 | 1068.1 | → | number | `4` |
| H | 605.4 | 1055.3 | → | number | `3` |
| H | 605.4 | 1081.3 | → | number | `1` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
 129.3  108.3  devtag       A302
 142.0  116.2  text         +AB
 157.2  110.6  xref         /112.A
 169.6  110.6  xref         /110.A
 210.1  134.9  devref       X8.A302
 211.5  186.2  numeric      1
 222.8  158.7  text         +AB
 341.9  131.8  devref       X1.M342
 354.6  157.3  text         +AB
 360.3  186.2  numeric      1
 497.8  106.6  net          M342
 510.5  116.2  text         +AB
=== Column B ===
  87.5  245.8  net          24V
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
 641.3  396.3  text         MOTOR: ANLEGEREINSATZPUNKTEINSTELLUNG
 651.9  396.3  text         MOTOR: FEEDER TIMING
 690.9  438.5  text         BOGENANKUNFT, SPÄTER
 701.5  439.1  text         SHEET ARRIVAL, LATER
 726.3  438.5  text         BOGENANKUNFT, FRÜHER
 736.9  439.1  text         SHEET ARRIVAL, EARLIER
=== Column D ===
  66.2  589.7  net          0V
  87.4  595.0  text         F5 6,3A T
 211.5  527.0  numeric      7
 211.5  583.7  numeric      8
 360.3  527.0  numeric      7
 360.3  583.7  numeric      8
 428.7  466.9  text         NULL POSITION
 439.3  467.7  text         ZERO POSITION
 441.8  575.6  net          0V
=== Column E ===
 210.1  730.2  devref       X9.A302
 211.5  640.3  numeric      9
 222.8  754.0  text         +AB
 341.9  728.8  devref       X1.B342
 354.6  752.6  text         +AB
 360.3  640.3  numeric      9
=== Column F ===
 211.5  781.5  numeric      1
 211.5  838.8  numeric      2
 356.9  799.0  numeric      1
 356.9  855.7  numeric      1
 360.3  782.1  numeric      3
 360.3  838.2  numeric      1
 540.3  794.3  devtag       B342
 553.0  802.2  text         +AB
 641.3  750.9  text         SENSOR: NULL POSITION,
 651.9  751.2  text         ANLEGEREINSATZPUNKT
 662.5  750.3  text         DETECTOR: ZERO POSITION,
 673.1  750.3  text         FEEDER TIMING
=== Column G ===
 580.3  942.5  text         ANSICHT VON VORNE
 591.0  942.5  text         AUF BUCHSENGEHÄUSE
 597.0  925.8  numeric      1
 601.5  941.7  text         FRONT VIEW ONTO
 612.2  942.2  text         THE SOCKET CASES
=== Column H ===
 592.6 1068.1  numeric      4
 605.4 1055.3  numeric      3
 605.4 1081.3  numeric      1
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_AX_8039G38I902_p`, sheet 111._
