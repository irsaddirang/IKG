# Render decisions — manroland R700 IEC wiring diagrams

Status: **decided and implemented** in `pipeline/render.py`.
Final setting: **1-bit bilevel PNG @ 300 DPI, threshold 160** (`v <= 160` → black, no dithering).

## 1. What the source actually is

Measured, not assumed (PyMuPDF 1.28.6):

| Property | Measured value |
|---|---|
| Page size | 1190.55 × 841.89 pt (A3 landscape) on **all 1351 pages** |
| Page rotation | 0 on every page |
| Text | real embedded text on every page (1,000–2,900 chars/sheet) — **no OCR needed** |
| Vector drawings | 260–1,942 drawing items per sheet |
| Stroke widths | **0.85 pt** for 21,171 of 21,480 items (the rest have no explicit width) |
| Body text sizes | 6.89–7.53 pt (≈600k chars) and 8.76–8.82 pt; small tail at 3.99 pt and 2.91–2.95 pt |
| Colours | black line work on white |

Two consequences drive the whole decision:

1. **Worst-case hairline.** A 0.85 pt line at 300 DPI is **3.54 px** wide. In the worst
   sub-pixel phase (the line centred exactly between two pixel rows) the anti-aliased
   coverage splits 1.77 / 1.77. Both rows are above a 0.5 threshold, so a hairline
   *cannot* disappear at 300 DPI. At 200 DPI it would be 2.36 px (1.18 / 1.18) —
   still above threshold but with far less headroom, and the 3.99 pt text would
   fall to ~11 px em height. 300 DPI is the first resolution with real margin.
2. **Nothing here needs grey.** There are no photographs, no gradients, and no
   anti-aliasing that carries information. Every tonal value in the raster is an
   artefact of rendering a hard-edged vector; binarising it recovers the original
   geometry rather than destroying detail.

## 2. Candidate comparison — measured on the densest sheets

Byte sizes are real `optimize=True` PNGs written by `render.py`'s encoder, on the
four busiest sheets found by scanning all 1351 pages (+EA 28 at 1,942 paths,
+BA_Cx_DA 21 at 1,928, +FB 4 at 1,796, +Ax 125 at 1,508).

| Candidate | +EA 28 | +BA_Cx_DA 21 | +FB 4 | +Ax 125 | Verdict |
|---|---:|---:|---:|---:|---|
| RGB @ 200 (3308×2339) | 528.8 KB | 428.3 KB | 448.1 KB | 497.9 KB | largest of all, **lowest** resolution — rejected on both axes |
| GRAY @ 300 (4961×3508) | 393.3 KB | 300.9 KB | 313.8 KB | 354.6 KB | 3.5× bigger than bilevel for zero information gain |
| GRAY @ 400 (6615×4678) | 542.2 KB | 415.7 KB | 431.8 KB | 477.9 KB | biggest of the 8-bit options |
| **1-bit @ 300 t160** | **111.6 KB** | **84.1 KB** | **65.0 KB** | **90.5 KB** | **chosen** |
| 1-bit @ 400 t160 | 157.2 KB | 119.8 KB | 92.4 KB | 128.2 KB | 1.4× the size, no added legibility |
| 1-bit @ 200 t160 | 70.6 KB | 55.3 KB | 39.7 KB | 55.5 KB | smallest, but only 96 DPI-equivalent margins for 4 pt text |

Threshold is almost irrelevant to file size (t150 vs t170 differs by <0.3 % on every
page), so threshold was chosen purely on fidelity — see §3.

**1-bit @ 300 DPI is ~3.5× smaller than grayscale at the identical pixel grid and
~4.7× smaller than RGB @ 200 while being 2.25× the linear resolution of that RGB
option.**

## 3. Proving 1-bit loses nothing

Four independent tests, run on +EA 28, +BA_Cx_DA 21, +FB 4 and +Ax 125 at both
300 and 400 DPI, at thresholds 150 / 160 / 170.

**a) Solid-ink recall — 1.000000.** Every pixel that was solid ink in the grayscale
render (gray < 128) is still black in the bilevel image. Exactly zero solid-ink
pixels are lost, at every threshold and DPI.

**b) No speckle.** `false_pos_white` = 0.0 — not one black pixel appears on a pure
white pixel (gray > 245). Dithering is explicitly disabled (`dither=Image.NONE`),
so there is no stippling.

**c) No fragmentation.** 8-connected component analysis: **0 components of ≤2 px**
on every page. The ~1,000–3,000 components per sheet are the real glyphs and
symbols; nothing has degenerated into dot patterns. Component counts are stable
across thresholds, confirming the image is a faithful 1:1 map of the vector art.

**d) Hairline continuity along real geometry.** Rather than eyeball it, the probe
read the page's *own* vector segments, kept only thin solid straight lines
(width ≤ 1.2 pt, not dashed, ≥ 40 pt long), and walked a 1-px-step sample along
each one checking that every along-axis column contained an inked pixel in its
perpendicular ±3 px window. A dotted or broken line would show up as gap samples.

| Page | Thin segments tested | Samples | **Gap samples** |
|---|---:|---:|---:|
| +EA 28 | 163 | 42,917 | **0** |
| +BA_Cx_DA 21 | 134 | 39,344 | **0** |
| +FB 4 | 125 | 44,075 | **0** |
| +Ax 125 | 177 | 50,647 | **0** |

Zero gaps over 177k samples: **no hairline is broken, dotted, or intermittent.**

**e) Small text.** A per-character test clipped every text bbox from
`get_text("rawdict")` and checked that at least one black pixel survived. The
first pass flagged **0.44–0.50 %** of characters as "empty" — but the value was
*identical at t150, t160 and t170*, which is impossible if thresholding caused it.
Inspecting the survivors showed why: those boxes have `min_gray` 186–216 and
`mean_gray` 254.6–254.9, i.e. **99.9 % white with no glyph present at all** — stray
faint marks in the PDF (the same coordinates recur on every sheet, e.g.
`[14.4, 344.4, 23.2, 346.9]`), not text. Once characters with no real ink are
excluded, **threshold-induced glyph loss is 0.000 % at t150, t160 and t170.**

`miss_ink` of 4–10 % is therefore exactly what it should be: the anti-aliasing
fringe (gray 128–200) around each stroke. Discarding it changes line *weight*, not
line *presence* or text *legibility*.

**Threshold 160** was chosen inside the flat plateau (t160 and t170 gave identical
glyph results; t150 kept slightly more fringe). It sits symmetric in the middle of
the histogram between the white field (245+) and the antialiased edges (~186–216),
far from both. The 0.85 pt hairline renders at gray 0 with 1.77-covered neighbours,
so the exact threshold value has no leverage on the geometry — verified by the
identical results across t150–t170.

## 4. Visual confirmation

Crops rendered at 300 DPI bilevel and inspected at native resolution:

* **Title block, +Ax sheet 21** (`R700`, `Masch.-Type:`, `Blatt: 21 - 403`,
  `DIN A3`, `8039G38I902`, zone letters `E/F/G/H`) — all crisp, letterforms closed,
  slashed zeros (`0`) rendered as slashes, not blobs.
* **Annotations and wires, +FB sheet 9** — `+A497/2-X1.A463:1`, `#67`, `/17.D`,
  `/17.E`, `/12.C`, `/13.G`, `-A244:bn`. The `#` glyph, the decimal points, the
  `:` and the `/` are all individually resolvable at 300 DPI, and the horizontal
  and vertical 0.85 pt wires are continuous, single-weight, unbroken.
* Small `:1` and `:4` suffixes inside those reference strings — the tightest text
  in the drawing — remain separable.

Conclusion: text is fully legible in a native-resolution crop, which is the hard
requirement. Anything the reader still needs to magnify can be re-rendered on
demand at 600–1200 DPI with `pipeline/crop.py`.

## 5. Why not 1-bit @ 400

1.44× the bytes, and the densest sheet already passes every test at 300. The
limiting factor for future OCR/reading is not pixel count but the source's own
0.85 pt stroke and 6.9 pt text, both comfortably resolved at 300 DPI. `crop.py`
exists precisely so that per-region 600/1200 DPI zooming is available without
paying 4,000 PNGs' worth of extra disk.

## 6. Final numbers (actual production run)

All 1351 pages rendered, **0 failures**, 93.55 MB on disk (89.22 MiB),
1351 PNGs at 4961×3508 px, mean **67.6 KB/page** — versus an estimated
~320 MB had grayscale @300 been used and ~470 MB for RGB @200.

| Document | Sheets | Size | Avg/page |
|---|---:|---:|---:|
| `+FB` | 22 | 1.34 MB | 62.2 KB |
| `+Ax` | 403 | 26.82 MB | 68.1 KB |
| `+BA_Cx_DA` | 247 | 15.87 MB | 65.8 KB |
| `+EA` | 407 | 27.10 MB | 68.2 KB |
| `+FA` | 58 | 3.77 MB | 66.5 KB |
| `+Jx` | 214 | 14.33 MB | 68.5 KB |
| **Total** | **1351** | **93.55 MB** | **67.6 KB** |

Full integrity checks, manifest reconciliation and the three visual spot-checks
are in `logs/render_verification.md`.
