---
doc: "+Ax"
sheet: 112
sheet_total: 403
document_code: "8039G38I902"
section_de: "FORMATEINSTELLUNG MOTORISCH, SEITLICHE"
section_en: "STAPELABTASTUNG (POSITIONIERANTRIEB)"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "17.05.10"
image: "../../../images/+Ax/Ax_0112.png"
columns: "A-B-C-D-E-F"
---

# +Ax — Sheet 112 of 403 — FORMATEINSTELLUNG MOTORISCH, SEITLICHE

**STAPELABTASTUNG (POSITIONIERANTRIEB)**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+Ax` covers the **Central control console** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+Ax`  (8039G38I902) |
| Sheet | **112** of 403 |
| Section (DE) | FORMATEINSTELLUNG MOTORISCH, SEITLICHE |
| Section (EN) | STAPELABTASTUNG (POSITIONIERANTRIEB) |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 17.05.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F |
| Path numbers | — |
| Labels on sheet | 54 |
| Cross-refs out | 2 |
| Cross-refs in | 22 |

**Previous:** [+Ax sheet 111](SHEET_0111.md) · **Next:** [+Ax sheet 113](SHEET_0113.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+Ax) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+Ax sheet 112](../../../images/+Ax/Ax_0112.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/113.A` | [+Ax sheet 113](SHEET_0113.md) | A | — | — | FORMATEINSTELLUNG MOTORISCH, SEITLICHE | A |
| `/111.A` | [+Ax sheet 111](SHEET_0111.md) | A | — | — | ANLEGEREINSATZPUNKTEINSTELLUNG | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+Ax#111](SHEET_0111.md) | A | `/111.A` | — | 1 | — |
| [+Ax#113](SHEET_0113.md) | A | `/113.A` | — | 1 | — |
| [+Ax#214](SHEET_0214.md) | F | `/214.F` | — | 9 | — |
| [+Ax#243](SHEET_0243.md) | F | `/243.F` | — | 9 | — |
| [+Ax#246](SHEET_0246.md) | A | `/246.A` | — | 2 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `A302` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `X1.M343` | — | cross-device reference | A | — | — | — |
| `X10.A302` | — | cross-device reference | A | — | — | — |
| `X11.A302` | — | cross-device reference | E | — | — | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `0V` | 2 | D | — | — |
| `24V` | 2 | B | — | — |
| `M343` | 1 | A | — | — |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| D | 66.2 | — | — | `0V` |
| D | 87.4 | — | — | `F6 6,3A T` |
| B | 87.5 | — | — | `24V` |
| A | 129.3 | — | — | `A302` |
| A | 142.0 | — | — | `+AB` |
| A | 157.2 | — | `/113.A`, `/111.A` | — |
| F | 193.8 | — | — | `X11.A302 1 2` |
| A | 210.1 | — | — | `X10.A302 1` |
| C | 211.5 | — | — | `2 3 4 5 6 7 8 9` |
| E | 219.9 | — | — | `+AB` |
| A | 222.8 | — | — | `+AB` |
| A | 344.7 | — | — | `X1.M343 1` |
| C | 357.4 | — | — | `+AB 2 3 4 5 6 7 8 9` |
| B | 428.6 | — | — | `FREIGABE RS485` |
| C | 428.6 | — | — | `POSITIONIERANTRIEBE FREIGABE` |
| D | 428.6 | — | — | `NULL POSITION` |
| B | 439.3 | — | — | `RELEASE RS485` |
| D | 439.3 | — | — | `ZERO POSITION` |
| C | 441.8 | — | — | `24V 0V` |
| C | 449.9 | — | — | `POSITIONING DRIVES RELEASE` |
| A | 490.7 | — | — | `M343` |
| A | 503.4 | — | — | `+AB` |
| C | 533.2 | — | — | `M` |
| D | 648.3 | — | — | `LATERAL STOP, A SIDE, MAX. SEITENANSCHLAG, A SEITE, MAX.` |
| A | 655.4 | — | — | `MOTOR: SEITENANSCHLAG, A SEITE (FORMATEINSTELLUNG) MOTOR: SIDE STOP, A SIDE (FORMAT ADJUSTMENT)` |
| D | 697.9 | — | — | `LATERAL STOP, A SIDE, MIN. SEITENANSCHLAG, A SEITE, MIN.` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `+AB` | A | 503.38 |
| `MOTOR: SEITENANSCHLAG, A SEITE` | A | 655.42 |
| `(FORMATEINSTELLUNG)` | A | 666.08 |
| `MOTOR: SIDE STOP, A SIDE` | A | 676.68 |
| `(FORMAT ADJUSTMENT)` | A | 687.34 |
| `M` | C | 533.24 |
| `+AB` | E | 219.92 |
| `SEITENANSCHLAG, A SEITE, MAX.` | D | 648.33 |
| `LATERAL STOP, A SIDE, MAX.` | D | 658.95 |
| `SEITENANSCHLAG, A SEITE, MIN.` | D | 697.94 |
| `LATERAL STOP, A SIDE, MIN.` | D | 708.56 |
| `FREIGABE` | C | 428.61 |
| `POSITIONIERANTRIEBE` | C | 439.27 |
| `RELEASE` | C | 449.88 |
| `POSITIONING DRIVES` | C | 460.54 |
| `FREIGABE RS485` | B | 428.64 |
| `RELEASE RS485` | B | 439.28 |
| `NULL POSITION` | D | 428.65 |
| `ZERO POSITION` | D | 439.29 |
| `F6 6,3A T` | D | 87.43 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 129.3 | 108.3 | → | device tag | `A302` |
| A | 142.0 | 116.2 | → | text | `+AB` |
| A | 157.2 | 110.6 | → | cross-reference | `/113.A` |
| A | 169.6 | 110.6 | → | cross-reference | `/111.A` |
| A | 210.1 | 129.0 | → | device ref | `X10.A302` |
| A | 211.5 | 186.2 | → | number | `1` |
| A | 222.8 | 158.7 | → | text | `+AB` |
| A | 344.7 | 131.8 | → | device ref | `X1.M343` |
| A | 357.4 | 157.3 | → | text | `+AB` |
| A | 360.3 | 186.2 | → | number | `1` |
| A | 490.7 | 106.6 | → | potential | `M343` |
| A | 503.4 | 116.2 | → | text | `+AB` |
| A | 655.4 | 141.2 | → | text | `MOTOR: SEITENANSCHLAG, A SEITE` |
| A | 666.1 | 141.2 | → | text | `(FORMATEINSTELLUNG)` |
| A | 676.7 | 141.2 | → | text | `MOTOR: SIDE STOP, A SIDE` |
| A | 687.3 | 141.2 | → | text | `(FORMAT ADJUSTMENT)` |
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
| C | 533.2 | 406.6 | → | text | `M` |
| D | 66.2 | 589.7 | → | potential | `0V` |
| D | 87.4 | 595.0 | → | text | `F6 6,3A T` |
| D | 211.5 | 527.0 | → | number | `7` |
| D | 211.5 | 583.7 | → | number | `8` |
| D | 360.3 | 527.0 | → | number | `7` |
| D | 360.3 | 583.7 | → | number | `8` |
| D | 428.7 | 466.9 | → | text | `NULL POSITION` |
| D | 439.3 | 467.7 | → | text | `ZERO POSITION` |
| D | 441.8 | 575.6 | → | potential | `0V` |
| D | 648.3 | 439.1 | → | text | `SEITENANSCHLAG, A SEITE, MAX.` |
| D | 659.0 | 438.5 | → | text | `LATERAL STOP, A SIDE, MAX.` |
| D | 697.9 | 439.1 | → | text | `SEITENANSCHLAG, A SEITE, MIN.` |
| D | 708.6 | 438.5 | → | text | `LATERAL STOP, A SIDE, MIN.` |
| E | 207.2 | 722.8 | → | device ref | `X11.A302` |
| E | 211.5 | 640.3 | → | number | `9` |
| E | 219.9 | 752.6 | → | text | `+AB` |
| E | 360.3 | 640.3 | → | number | `9` |
| F | 193.8 | 785.8 | → | number | `1` |
| F | 193.8 | 843.0 | → | number | `2` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
 129.3  108.3  devtag       A302
 142.0  116.2  text         +AB
 157.2  110.6  xref         /113.A
 169.6  110.6  xref         /111.A
 210.1  129.0  devref       X10.A302
 211.5  186.2  numeric      1
 222.8  158.7  text         +AB
 344.7  131.8  devref       X1.M343
 357.4  157.3  text         +AB
 360.3  186.2  numeric      1
 490.7  106.6  net          M343
 503.4  116.2  text         +AB
 655.4  141.2  text         MOTOR: SEITENANSCHLAG, A SEITE
 666.1  141.2  text         (FORMATEINSTELLUNG)
 676.7  141.2  text         MOTOR: SIDE STOP, A SIDE
 687.3  141.2  text         (FORMAT ADJUSTMENT)
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
 533.2  406.6  text         M
=== Column D ===
  66.2  589.7  net          0V
  87.4  595.0  text         F6 6,3A T
 211.5  527.0  numeric      7
 211.5  583.7  numeric      8
 360.3  527.0  numeric      7
 360.3  583.7  numeric      8
 428.7  466.9  text         NULL POSITION
 439.3  467.7  text         ZERO POSITION
 441.8  575.6  net          0V
 648.3  439.1  text         SEITENANSCHLAG, A SEITE, MAX.
 659.0  438.5  text         LATERAL STOP, A SIDE, MAX.
 697.9  439.1  text         SEITENANSCHLAG, A SEITE, MIN.
 708.6  438.5  text         LATERAL STOP, A SIDE, MIN.
=== Column E ===
 207.2  722.8  devref       X11.A302
 211.5  640.3  numeric      9
 219.9  752.6  text         +AB
 360.3  640.3  numeric      9
=== Column F ===
 193.8  785.8  numeric      1
 193.8  843.0  numeric      2
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_AX_8039G38I902_p`, sheet 112._
