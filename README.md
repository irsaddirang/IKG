# IKG — Knowledge Base dari Dokumen Teknis

Repositori ini mengubah dokumen teknis (PDF gambar teknik) menjadi **knowledge
base Markdown** yang dapat dibaca dan dipakai dengan tepat oleh LLM / agent AI.

**Status saat ini:** 1 dokumen-set selesai — diagram kelistrikan **manroland R700**
(6 PDF, **1.351 sheet** DIN A3) → knowledge base + QC buta terukur.

> **Agent / kontributor baru: mulai dari [`agent.md`](agent.md).**
> Di situ ada aturan kerja, larangan, format catatan, prosedur menambah dokumen,
> dan backlog. Jangan mulai dari file lain.

---

## Isi repositori

| Path | Isi |
|---|---|
| [`agent.md`](agent.md) | **Deliverable utama.** Aturan agent, format catatan, prosedur, backlog, log perubahan |
| [`Diagram Manroland/`](Diagram%20Manroland) | Sumber: 6 PDF diagram kelistrikan (vektor, bukan scan) |
| [`Manroland_KnowledgeBase/README.md`](Manroland_KnowledgeBase/README.md) | Gambaran hasil & cara rebuild |
| [`Manroland_KnowledgeBase/md/`](Manroland_KnowledgeBase/md) | **Knowledge base**: 1.351 file sheet + indeks + panduan notasi |
| [`Manroland_KnowledgeBase/md/01_SYSTEM/A_HOW_TO_READ.md`](Manroland_KnowledgeBase/md/01_SYSTEM/A_HOW_TO_READ.md) | Cara membaca diagram (wajib sebelum menjawab) |
| [`Manroland_KnowledgeBase/md/03_INDEX/`](Manroland_KnowledgeBase/md/03_INDEX) | Indeks: section, sheet, device, net, katalog |
| [`Manroland_KnowledgeBase/images/`](Manroland_KnowledgeBase/images) | 1.351 render 300 DPI (1-bit) |
| [`Manroland_KnowledgeBase/pipeline/`](Manroland_KnowledgeBase/pipeline) | Pipeline reproducible + QA harness |
| [`QC/`](QC) | Harness QC: ground truth, benchmark buta, konsistensi |
| [`QC/QC_REPORT.md`](QC/QC_REPORT.md) | Laporan QC: 2 putaran benchmark buta, 11 cacat ditemukan |

---

## Temuan inti: PDF ini bukan scan

Keputusan teknis paling penting di proyek ini, dan alasannya:

| Metode | Hasil pada sheet padat |
|---|---|
| OCR Tesseract @300 DPI | **~50% confidence** — tag perangkat rusak |
| Text layer PDF tersemat | **string persis, koordinat persis** |

PDF sumber adalah ekspor vektor CAE (CIM-TEAM, 2010–2012) dengan text layer
lengkap — dan pengelompokan *text block* bawaan PDF-nya sudah semantik: satu
anotasi ujung kawat = satu block berisi `tujuan` + `#line` + `/sheet.column`.

**Karena itu knowledge base dibangun dari text layer + geometri vektor, bukan dari
piksel.** Render 300 DPI tetap disertakan, tetapi hanya untuk **konfirmasi
topologi visual** — bukan sumber label.

---

## Hasil terukur

| Pemeriksaan | Hasil |
|---|---|
| Sheet diproses | **1.351 / 1.351** |
| Label diekstrak | **180.916** |
| **Fidelitas label vs PDF** | **180.916 / 180.916 — 0 hilang** |
| Cross-reference ter-resolve | **34.890 / 34.890** |
| Link internal Markdown | **108.821 — 0 rusak** |
| Berkas sheet Markdown | 1.351 (satu per sheet) |
| Render 300 DPI | 1.351, 1-bit |
| **QC buta putaran 1** | **51/52 (98,1%) — 0 fabrikasi** |
| **QC buta putaran 2** (setelah perbaikan) | **6/6 pada soal tersulit — 0 fabrikasi** |

Metode QC: agent **tidak** melihat PDF; ground truth dihitung ulang dari PDF oleh
skrip terpisah. Detail di [`QC/QC_REPORT.md`](QC/QC_REPORT.md).

---

## Tiga konsep untuk membaca diagram

1. **Lokasi = dokumen + sheet + kolom.** Kolom DIN `A`–`H` tercetak di margin atas
   dan bawah, lebar ~140 pt.
2. **`/17.D` = "berlanjut di sheet 17 kolom D dokumen yang sama."** Enam PDF adalah
   enam set terpisah; cross-reference tidak pernah keluar dokumen.
3. **Anotasi ujung kawat adalah klaster**, dibaca kiri→kanan:
   `tujuan` → `#line` → `/sheet.column`, contoh:
   ```
   +A497/2 X1.A463:1     #67     /17.D
   ```
   Bisa menyebut beberapa tujuan sekaligus.

---

## Batasan yang dinyatakan (bukan disembunyikan)

- Gambar menunjukkan **perlengkapan maksimum seri**, bukan yang terpasang di mesin
  tertentu. Penentu kelengkapan = sheet `INDEX` opsi (`X` = tidak terpasang).
- Tidak ada **part number katalog, rating, atau deskripsi fungsi**. Ada 19 *order
  code* (bukan part number) di 8 sheet — lihat
  [`A_HOW_TO_READ.md` §8.1](Manroland_KnowledgeBase/md/01_SYSTEM/A_HOW_TO_READ.md).
- `#NN` nomor jalur hanya ada di **7 dari 1.351** sheet — bukan koordinat global.
- Knowledge base tidak dapat menilai **keamanan** sebuah desain.

---

## Reproduksi

```powershell
$py = "C:\Users\muham\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
cd Manroland_KnowledgeBase\pipeline

& $py build.py               # extract + tables + graph + md + export + sync
& $py build.py --with-images # sekaligus render 1.351 gambar (~70 s)

# verifikasi
& $py qa\qa_final.py           # 17 acceptance check
& $py qa\qa_fidelity_full.py   # setiap label setiap sheet vs PDF
& $py qa\qa_links.py           # setiap link internal
```

Artefak antara **`Manroland_KnowledgeBase/data/raw/`** tidak dikomit karena
100% dapat diregenerasi dari PDF sumber (lihat `.gitignore`).

---

## Sumber

Diagram kelistrikan manroland **R700** (sheet-fed offset press), digambar oleh
CIM-TEAM GmbH, 2010–2012, untuk manroland.

| Dokumen | Sheet | Document code |
|---|---:|---|
| `+FB` — Delivery / coating module | 22 | `8039G38K159` |
| `+Ax` — Central control console | 403 | `8039G38I902` |
| `+BA_Cx_DA` — Printing units / main switch cabinet | 247 | `8039G38J415` |
| `+EA` — Printing unit | 407 | `8039G38E915` |
| `+FA` — Delivery | 58 | `8039G38K212` |
| `+Jx` — 1st printing module + feed register | 214 | `039G38F308` |

Repositori ini **private**.
