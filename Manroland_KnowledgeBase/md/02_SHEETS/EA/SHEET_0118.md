---
doc: "+EA"
sheet: 118
sheet_total: 407
document_code: "8039G38E915"
section_de: "FORMATEINSTELLUNG: GREIFERÖFFNUNGSKURVE"
section_en: "FORMAT ADJUSTMENT: GRIPPER OPENING CAM"
section_code: "CIRCUIT"
machine_type: "R700"
serie: "7758"
created: "25.03.10"
image: "../../../images/+EA/EA_0118.png"
columns: "A-B-C-D-E-F-G"
---

# +EA — Sheet 118 of 407 — FORMATEINSTELLUNG: GREIFERÖFFNUNGSKURVE

**FORMAT ADJUSTMENT: GRIPPER OPENING CAM**

> Part of the manroland **R700** printing press IEC/UL circuit diagrams.
> Drawing class: **Stromlaufplan / Circuit diagram** (DIN A3).
> Document `+EA` covers the **Printing unit** machine section.

## At a glance

| Field | Value |
|---|---|
| Document | `+EA`  (8039G38E915) |
| Sheet | **118** of 407 |
| Section (DE) | FORMATEINSTELLUNG: GREIFERÖFFNUNGSKURVE |
| Section (EN) | FORMAT ADJUSTMENT: GRIPPER OPENING CAM |
| Section type | CIRCUIT — Circuit diagram |
| Machine type | `R700` |
| Series | `7758` |
| Created | 25.03.10 |
| Replaces | — |
| Columns used | A, B, C, D, E, F, G |
| Path numbers | — |
| Labels on sheet | 80 |
| Cross-refs out | 2 |
| Cross-refs in | 24 |

**Previous:** [+EA sheet 117](SHEET_0117.md) · **Next:** [+EA sheet 119](SHEET_0119.md) · **Document TOC:** [_TOC.md](_TOC.md)  (+EA) · **Master TOC:** [all sheets](../_MASTER_TOC.md)

## Sheet image (300 DPI, exact vector render)

![+EA sheet 118](../../../images/+EA/EA_0118.png)

_Rendered directly from the PDF vector layer at 300 DPI (1-bit), no OCR and no resampling. Use it to confirm anything ambiguous in the text below._

## Cross-references on this sheet

Each entry is a wire leaving this sheet. The printed token is `/sheet.column`; the link resolves to that sheet inside the same document.

| Ref | Target sheet | Col | Path | Destination on target | Target section | From col |
|---|---|---|---|---|---|---|
| `/119.D` | [+EA sheet 119](SHEET_0119.md) | D | — | — | PROZESSMAGAZIN: HANDTERMINAL | A |
| `/117.A` | [+EA sheet 117](SHEET_0117.md) | A | — | — | FORMATEINSTELLUNG: BOGENGERADESTOSSER | A |

### Incoming references (sheets that point here)

Every other sheet that sends a wire to this one. `Back-ref` is the token printed on *that* sheet; `Path` is its line number.

| From sheet | Cols | Back-ref | Path | Refs | What continues there |
|---|---|---|---|---|---|
| [+EA#117](SHEET_0117.md) | A | `/117.A` | — | 1 | — |
| [+EA#119](SHEET_0119.md) | D | `/119.D` | — | 1 | — |
| [+EA#217](SHEET_0217.md) | B | `/217.B` | — | 2 | — |
| [+EA#218](SHEET_0218.md) | G | `/218.G` | — | 9 | — |
| [+EA#253](SHEET_0253.md) | G | `/253.G` | — | 9 | — |
| [+EA#255](SHEET_0255.md) | F | `/255.F` | — | 2 | — |


## Devices on this sheet

| Tag | Class | Class meaning (IEC) | Col | Sub | Terminal | Sign |
|---|---|---|---|---|---|---|
| `B349` | B | Umformer / transducer, sensor | F | — | — | — |
| `A302` | A | Baugruppe / assembly, module, PC board | A | — | — | — |
| `F6` | F | Schutz / protection device (fuse, circuit breaker) | D | — | — | — |
| `X447/1` | X | Klemme / terminal, plug connector | C | 1 | — | — |
| `X447` | X | Klemme / terminal, plug connector | C | — | — | — |
| `X1.M349` | — | cross-device reference | A | — | — | — |
| `X1.B349` | — | cross-device reference | E | — | — | — |
| `X11.A302` | — | cross-device reference | E | — | — | — |
| `X10.A302` | — | cross-device reference | A | — | — | — |
| `NR.` | — | cross-device reference | F | — | — | — |
| `16.09.10` | — | cross-device reference | F | — | — | — |

## Potentials / nets

| Potential | Count | Columns | Attached devices | Terminals |
|---|---|---|---|---|
| `0V` | 2 | D | — | — |
| `24V` | 2 | B | — | — |
| `M349` | 1 | A | — | — |


A potential such as `L24+/4` or `M24+` is a named supply/return rail; every place it appears on this sheet is electrically common.

## Wire-end annotations (grouped as printed)

A wire that continues elsewhere is annotated with a small cluster: the destination description, the path/line number `#NN`, and the `/sheet.column` cross reference. Each row below is one such cluster exactly as it is grouped on the drawing.

| Col | Y | Path | Cross-ref | Text on the wire |
|---|---|---|---|---|
| A | 46.0 | — | — | `POSITIONIERANTRIEBE DISTRIBUTOR: POSITIONING DRIVES VERTEILER:` |
| C | 101.6 | — | — | `24V 0V` |
| D | 129.3 | — | — | `F6` |
| D | 142.3 | — | — | `T6,3A` |
| A | 157.6 | — | — | `A302` |
| A | 170.7 | — | `/119.D`, `/117.A` | — |
| D | 252.6 | — | — | `X10.A302 1 2 3 4 5 6 7 8 9 X11.A302 1 2` |
| F | 356.9 | — | — | `1 1` |
| D | 360.3 | — | — | `X1.M349 1 2 3 4 5 6 7 8 9 X1.B349 3 1` |
| B | 428.6 | — | — | `FREIGABE RS485` |
| C | 428.6 | — | — | `POSITIONIERANTRIEBE FREIGABE` |
| D | 428.6 | — | — | `NULL POSITION` |
| B | 439.3 | — | — | `RELEASE RS485` |
| D | 439.3 | — | — | `ZERO POSITION` |
| C | 441.8 | — | — | `24V 0V` |
| C | 449.9 | — | — | `POSITIONING DRIVES RELEASE` |
| A | 497.8 | — | — | `M349` |
| C | 504.9 | — | — | `X447/1` |
| C | 540.3 | — | — | `M` |
| F | 540.3 | — | — | `B349` |
| C | 554.5 | — | — | `X447` |
| F | 641.2 | — | — | `DETECTOR: ZERO POSITION, SENSOR: NULL POSITION, GREIFERÖFFNUNGSKURVE` |
| A | 641.3 | — | — | `MOTOR: GREIFERÖFFNUNGSKURVE MOTOR: GRIPPER OPENING CAM` |
| D | 641.3 | — | — | `GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (GRÖSSER) GRIPPER OPENING CAM: SIZE ADJUSTMENT (LARGER)` |
| F | 673.2 | — | — | `GRIPPER OPENING CAM` |
| D | 683.8 | — | — | `GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (KLEINER) GRIPPER OPENING CAM: SIZE ADJUSTMENT (SMALLER)` |
| A | 707.9 | — | — | `FRONT VIEW ONTO ANSICHT VON VORNE AUF BUCHSENGEHÄUSE` |
| A | 720.2 | — | — | `1 THE SOCKET CASES 4` |
| B | 732.9 | — | — | `3 1` |
| G | 733.0 | — | — | `001 16.09.10 SLEI/AES TEXT HINZU` |
| G | 747.1 | — | — | `NR. TAG NAME ÄNDERUNG` |


## Reconstructed tables

This sheet carries tabular content (pin map / terminal assignment / index). The grid below was rebuilt from the drawing's own rule lines, so each row is exactly one physical row of the table.

### Table 1 — 2 data rows × 4 columns (at x=85.0, y=161.6) — **A302 /119.D /117.A**

| X10.A302 X1.M349 | 1 1 |  | 2 2 |
|---|---|---|---|
| `M349 MOTOR: MOTOR: GRIPPER` |  | `24V GREIFERÖFFNUNGSKURVE OPENING CAM` |  |
| `ANSICHT VON VORNE AUF BUCHSENGEHÄUSE FRONT VIEW ONTO THE SOCKET CASES` |  | `4 3 1` |  |


### Table 2 — 1 data rows × 3 columns (at x=297.6, y=161.6)

| 3 3 | 4 4 | 5 5 |
|---|---|---|
| `FREIGABE RS485 RELEASE RS485` | `FREIGABE POSITIONIERANTRIEBE RELEASE POSITIONING` | `DRIVES M X447 GRIPPER GRIPPER` |


### Table 3 — 1 data rows × 3 columns (at x=467.7, y=161.6)

| 6 6 | 7 7 | 8 8 |
|---|---|---|
| `NULL POSITION ZERO POSITION X447/1 GREIFERÖFFNUNGSKURVE: OPENING CAM: SIZE GREIFERÖFFNUNGSKURVE: OPENING CAM: SIZE` | `FORMATEINSTELLUNG ADJUSTMENT FORMATEINSTELLUNG ADJUSTMENT` | `(GRÖSSER) (LARGER) (KLEINER) (SMALLER)` |


## Notes and free text on this sheet

| Text | Col | Y (pt) |
|---|---|---|
| `MOTOR: GREIFERÖFFNUNGSKURVE` | A | 641.27 |
| `MOTOR: GRIPPER OPENING CAM` | A | 651.9 |
| `M` | C | 540.33 |
| `SENSOR: NULL POSITION,` | F | 641.25 |
| `GREIFERÖFFNUNGSKURVE` | F | 651.9 |
| `DETECTOR: ZERO POSITION,` | F | 662.51 |
| `GRIPPER OPENING CAM` | F | 673.16 |
| `VERTEILER:` | A | 45.96 |
| `POSITIONIERANTRIEBE` | A | 56.59 |
| `DISTRIBUTOR:` | A | 67.22 |
| `POSITIONING DRIVES` | A | 77.86 |
| `T6,3A` | D | 142.3 |
| `TAG` | F | 747.27 |
| `NAME` | G | 747.25 |
| `ÄNDERUNG` | G | 747.31 |
| `SLEI/AES` | G | 733.13 |
| `TEXT HINZU` | G | 733.13 |
| `FREIGABE` | C | 428.61 |
| `POSITIONIERANTRIEBE` | C | 439.27 |
| `RELEASE` | C | 449.88 |
| `POSITIONING DRIVES` | C | 460.54 |
| `FREIGABE RS485` | B | 428.64 |
| `RELEASE RS485` | B | 439.28 |
| `NULL POSITION` | D | 428.65 |
| `ZERO POSITION` | D | 439.29 |
| `ANSICHT VON VORNE` | A | 707.88 |
| `AUF BUCHSENGEHÄUSE` | A | 718.51 |
| `FRONT VIEW ONTO` | A | 729.1 |
| `THE SOCKET CASES` | A | 739.75 |
| `GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (KLEINER)` | D | 683.79 |
| `GRIPPER OPENING CAM: SIZE ADJUSTMENT (SMALLER)` | D | 694.41 |
| `GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (GRÖSSER)` | D | 641.27 |
| `GRIPPER OPENING CAM: SIZE ADJUSTMENT (LARGER)` | D | 651.89 |

## Complete label inventory (exact text from the drawing)

Every text object inside the drawing area of this sheet, in DIN reading order (column A→H, then top→bottom). This is the authoritative list: if a string is not here it is not printed on this sheet.

| Col | Y | X | Dir | Type | Text |
|---|---|---|---|---|---|
| A | 46.0 | 141.7 | → | text | `VERTEILER:` |
| A | 56.6 | 140.9 | → | text | `POSITIONIERANTRIEBE` |
| A | 67.2 | 140.9 | → | text | `DISTRIBUTOR:` |
| A | 77.9 | 140.9 | → | text | `POSITIONING DRIVES` |
| A | 157.6 | 108.3 | → | device tag | `A302` |
| A | 170.7 | 110.6 | → | cross-reference | `/119.D` |
| A | 183.1 | 110.6 | → | cross-reference | `/117.A` |
| A | 252.6 | 129.0 | → | device ref | `X10.A302` |
| A | 254.0 | 186.2 | → | number | `1` |
| A | 360.3 | 186.2 | → | number | `1` |
| A | 363.1 | 131.8 | → | device ref | `X1.M349` |
| A | 497.8 | 106.6 | → | potential | `M349` |
| A | 641.3 | 141.2 | → | text | `MOTOR: GREIFERÖFFNUNGSKURVE` |
| A | 651.9 | 141.2 | → | text | `MOTOR: GRIPPER OPENING CAM` |
| A | 707.9 | 92.1 | → | text | `ANSICHT VON VORNE` |
| A | 718.5 | 92.1 | → | text | `AUF BUCHSENGEHÄUSE` |
| A | 724.5 | 75.4 | → | number | `1` |
| A | 729.1 | 91.3 | → | text | `FRONT VIEW ONTO` |
| A | 739.8 | 91.8 | → | text | `THE SOCKET CASES` |
| B | 101.6 | 245.8 | → | potential | `24V` |
| B | 254.0 | 243.5 | → | number | `2` |
| B | 254.0 | 300.2 | → | number | `3` |
| B | 360.3 | 243.5 | → | number | `2` |
| B | 360.3 | 300.2 | → | number | `3` |
| B | 428.6 | 299.3 | → | text | `FREIGABE RS485` |
| B | 439.3 | 300.7 | → | text | `RELEASE RS485` |
| B | 441.8 | 231.6 | → | potential | `24V` |
| B | 720.2 | 217.7 | → | number | `4` |
| B | 732.9 | 204.9 | → | number | `3` |
| B | 732.9 | 230.9 | → | number | `1` |
| C | 254.0 | 356.9 | → | number | `4` |
| C | 254.0 | 413.6 | → | number | `5` |
| C | 254.0 | 470.3 | → | number | `6` |
| C | 360.3 | 356.9 | → | number | `4` |
| C | 360.3 | 413.6 | → | number | `5` |
| C | 360.3 | 470.3 | → | number | `6` |
| C | 428.6 | 394.8 | → | text | `FREIGABE` |
| C | 439.3 | 374.8 | → | text | `POSITIONIERANTRIEBE` |
| C | 449.9 | 396.2 | → | text | `RELEASE` |
| C | 460.5 | 377.6 | → | text | `POSITIONING DRIVES` |
| C | 504.9 | 460.3 | → | device tag | `X447/1` |
| C | 540.3 | 406.6 | → | text | `M` |
| C | 554.5 | 439.1 | → | device tag | `X447` |
| D | 101.6 | 589.7 | → | potential | `0V` |
| D | 129.3 | 558.7 | → | device tag | `F6` |
| D | 142.3 | 548.5 | → | text | `T6,3A` |
| D | 254.0 | 527.0 | → | number | `7` |
| D | 254.0 | 583.7 | → | number | `8` |
| D | 360.3 | 527.0 | → | number | `7` |
| D | 360.3 | 583.7 | → | number | `8` |
| D | 428.7 | 466.9 | → | text | `NULL POSITION` |
| D | 439.3 | 467.7 | → | text | `ZERO POSITION` |
| D | 441.8 | 575.6 | → | potential | `0V` |
| D | 641.3 | 439.1 | → | text | `GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (GRÖSSER)` |
| D | 651.9 | 439.1 | → | text | `GRIPPER OPENING CAM: SIZE ADJUSTMENT (LARGER)` |
| D | 683.8 | 439.1 | → | text | `GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (KLEINER)` |
| D | 694.4 | 439.1 | → | text | `GRIPPER OPENING CAM: SIZE ADJUSTMENT (SMALLER)` |
| E | 252.6 | 724.3 | → | device ref | `X11.A302` |
| E | 254.0 | 640.3 | → | number | `9` |
| E | 360.3 | 640.3 | → | number | `9` |
| E | 363.1 | 728.8 | → | device ref | `X1.B349` |
| F | 254.0 | 781.5 | → | number | `1` |
| F | 254.0 | 838.8 | → | number | `2` |
| F | 356.9 | 799.0 | → | number | `1` |
| F | 356.9 | 855.7 | → | number | `1` |
| F | 360.3 | 782.1 | → | number | `3` |
| F | 360.3 | 838.2 | → | number | `1` |
| F | 540.3 | 794.3 | → | device tag | `B349` |
| F | 641.3 | 750.9 | → | text | `SENSOR: NULL POSITION,` |
| F | 651.9 | 750.9 | → | text | `GREIFERÖFFNUNGSKURVE` |
| F | 662.5 | 750.3 | → | text | `DETECTOR: ZERO POSITION,` |
| F | 673.2 | 750.9 | → | text | `GRIPPER OPENING CAM` |
| F | 733.0 | 845.2 | → | number | `001` |
| F | 733.1 | 879.0 | → | device ref | `16.09.10` |
| F | 747.1 | 844.2 | → | device ref | `NR.` |
| F | 747.3 | 885.8 | → | text | `TAG` |
| G | 733.1 | 934.0 | → | text | `SLEI/AES` |
| G | 733.1 | 981.2 | → | text | `TEXT HINZU` |
| G | 747.3 | 939.2 | → | text | `NAME` |
| G | 747.3 | 981.8 | → | text | `ÄNDERUNG` |

## Reading-order text block

The same content as a plain block, grouped by DIN column — convenient to paste or to match against a visual description.

```text
=== Column A ===
  46.0  141.7  text         VERTEILER:
  56.6  140.9  text         POSITIONIERANTRIEBE
  67.2  140.9  text         DISTRIBUTOR:
  77.9  140.9  text         POSITIONING DRIVES
 157.6  108.3  devtag       A302
 170.7  110.6  xref         /119.D
 183.1  110.6  xref         /117.A
 252.6  129.0  devref       X10.A302
 254.0  186.2  numeric      1
 360.3  186.2  numeric      1
 363.1  131.8  devref       X1.M349
 497.8  106.6  net          M349
 641.3  141.2  text         MOTOR: GREIFERÖFFNUNGSKURVE
 651.9  141.2  text         MOTOR: GRIPPER OPENING CAM
 707.9   92.1  text         ANSICHT VON VORNE
 718.5   92.1  text         AUF BUCHSENGEHÄUSE
 724.5   75.4  numeric      1
 729.1   91.3  text         FRONT VIEW ONTO
 739.8   91.8  text         THE SOCKET CASES
=== Column B ===
 101.6  245.8  net          24V
 254.0  243.5  numeric      2
 254.0  300.2  numeric      3
 360.3  243.5  numeric      2
 360.3  300.2  numeric      3
 428.6  299.3  text         FREIGABE RS485
 439.3  300.7  text         RELEASE RS485
 441.8  231.6  net          24V
 720.2  217.7  numeric      4
 732.9  204.9  numeric      3
 732.9  230.9  numeric      1
=== Column C ===
 254.0  356.9  numeric      4
 254.0  413.6  numeric      5
 254.0  470.3  numeric      6
 360.3  356.9  numeric      4
 360.3  413.6  numeric      5
 360.3  470.3  numeric      6
 428.6  394.8  text         FREIGABE
 439.3  374.8  text         POSITIONIERANTRIEBE
 449.9  396.2  text         RELEASE
 460.5  377.6  text         POSITIONING DRIVES
 504.9  460.3  devtag       X447/1
 540.3  406.6  text         M
 554.5  439.1  devtag       X447
=== Column D ===
 101.6  589.7  net          0V
 129.3  558.7  devtag       F6
 142.3  548.5  text         T6,3A
 254.0  527.0  numeric      7
 254.0  583.7  numeric      8
 360.3  527.0  numeric      7
 360.3  583.7  numeric      8
 428.7  466.9  text         NULL POSITION
 439.3  467.7  text         ZERO POSITION
 441.8  575.6  net          0V
 641.3  439.1  text         GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (GRÖSSER)
 651.9  439.1  text         GRIPPER OPENING CAM: SIZE ADJUSTMENT (LARGER)
 683.8  439.1  text         GREIFERÖFFNUNGSKURVE: FORMATEINSTELLUNG (KLEINER)
 694.4  439.1  text         GRIPPER OPENING CAM: SIZE ADJUSTMENT (SMALLER)
=== Column E ===
 252.6  724.3  devref       X11.A302
 254.0  640.3  numeric      9
 360.3  640.3  numeric      9
 363.1  728.8  devref       X1.B349
=== Column F ===
 254.0  781.5  numeric      1
 254.0  838.8  numeric      2
 356.9  799.0  numeric      1
 356.9  855.7  numeric      1
 360.3  782.1  numeric      3
 360.3  838.2  numeric      1
 540.3  794.3  devtag       B349
 641.3  750.9  text         SENSOR: NULL POSITION,
 651.9  750.9  text         GREIFERÖFFNUNGSKURVE
 662.5  750.3  text         DETECTOR: ZERO POSITION,
 673.2  750.9  text         GRIPPER OPENING CAM
 733.0  845.2  numeric      001
 733.1  879.0  devref       16.09.10
 747.1  844.2  devref       NR.
 747.3  885.8  text         TAG
=== Column G ===
 733.1  934.0  text         SLEI/AES
 733.1  981.2  text         TEXT HINZU
 747.3  939.2  text         NAME
 747.3  981.8  text         ÄNDERUNG
```

---
_Generated from the PDF vector text layer; no OCR. Source: `R700_7758_IEC_UL_EA_8039G38E915_p`, sheet 118._
