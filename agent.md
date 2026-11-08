# agent.md — Aturan Kerja Agent & Backlog Knowledge Base

**Proyek:** `IKG` — konversi dokumen teknis menjadi knowledge base Markdown yang
dapat dipakai LLM/agent.
**Lokasi file ini:** `C:\Users\muham\OneDrive\ドキュメント\Github\IKG\agent.md`
**Versi:** 1.1 · **Terakhir diperbarui:** 2026-11-08
**Status knowledge base saat ini:** 1 dokumen-set (6 PDF, 1.351 sheet) — **selesai**;
dokumen lain **belum terdaftar** → `[待补]`.

---

## Baca Ini Dulu

Urutan baca yang benar, jangan dilompati:

1. **File ini** (`agent.md`) — aturan, format catatan, backlog, log.
2. `Manroland_KnowledgeBase/README.md` — gambaran hasil & cara rebuild.
3. `Manroland_KnowledgeBase/md/00_READ_ME_FIRST.md` — titik masuk knowledge base.
4. `Manroland_KnowledgeBase/md/01_SYSTEM/A_HOW_TO_READ.md` — notasi diagram (wajib
   sebelum menjawab pertanyaan teknis apa pun).
5. `QC/QC_REPORT.md` — bukti kualitas & cacat yang pernah ditemukan.

**Tiga aturan emas** (kalau hanya ingat tiga hal):

1. **Jangan mengarang.** Kalau tidak ada di sumber, tulis "tidak dinyatakan".
2. **Jangan menandai `selesai` tanpa path sumber yang benar-benar ada.**
3. **Jangan menghapus catatan lama.** Koreksi dengan menambah, bukan menghapus.

---

## Aturan Pakai dan Batasan Agent

### Yang WAJIB dilakukan

| # | Aturan | Alasan |
|---|---|---|
| W1 | Baca `A_HOW_TO_READ.md` sebelum menjawab pertanyaan tentang isi diagram | Tanpa notasi, cross-reference `/17.D` akan salah dibaca sebagai halaman PDF |
| W2 | Setiap klaim tentang isi dokumen harus menyebut **file + string persis** yang dikutip | Membuat jawaban bisa diaudit |
| W3 | Tandai `selesai` hanya jika artefak output benar-benar ada dan lolos verifikasi | Status palsu merusak backlog |
| W4 | Jalankan suite verifikasi sebelum melaporkan hasil (lihat bagian Gerbang verifikasi) | Angka "kelihatan benar" ≠ terverifikasi |
| W5 | Catat setiap pekerjaan ke §5 Log Perubahan dengan tanggal & bukti | Riwayat tidak boleh hilang |
| W6 | Kalau sumber ambigu, **tulis ambiguitasnya**, jangan diselesaikan sendiri | Contoh nyata: order code bukan part number |
| W7 | Bedakan tegas: **tercetak di gambar** vs **disimpulkan** | Dua hal ini berbeda nilai kepercayaannya |

### Yang DILARANG (eksplisit)

| # | Larangan | Contoh pelanggaran nyata yang pernah terjadi |
|---|---|---|
| L1 | **Mengarang isi dokumen** — part number, rating, fungsi, nomor halaman yang tidak tercetak | Menyebut rating arus relay yang tidak ada di gambar |
| L2 | **Menandai `selesai` tanpa path sumber yang valid** | Menulis "selesai" padahal PDF-nya tidak ada di path itu |
| L3 | **Menghapus catatan lama** di bagian Log Perubahan atau Backlog | Menimpa entri supaya terlihat bersih |
| L4 | Mengubah angka terukur tanpa menjalankan ulang pipeline | Angka prosa basi vs data (pernah terjadi, lihat §5 v1.0) |
| L5 | Melaporkan skor/keyakinan tanpa metode pengukuran yang bisa diulang | Klaim "akurat 99%" tanpa skrip |
| L6 | Menggabungkan beberapa dokumen menjadi satu ruang alamat | `/17.D` selalu berarti sheet 17 **di dokumen yang sama** |
| L7 | Memakai OCR pada PDF yang punya text layer | OCR terukur hanya ~50% pada dokumen ini |
| L8 | Menyatakan dokumen "sudah masuk KB" hanya karena file MD-nya ada | Harus ada verifikasi fidelitas |

### Batasan teknis yang terukur

Angka berikut **diukur** dari korpus Manroland; jangan mengarang angka lain.

| Besaran | Nilai terukur |
|---|---|
| PDF sumber | 6 file, 1.351 sheet DIN A3 |
| Label teks diekstrak | 180.916 |
| Fidelitas label vs PDF | 180.916 / 180.916 (0 hilang) |
| Cross-reference | 34.890 (0 unresolved) |
| Link internal Markdown | 108.821 (0 rusak) |
| Perangkat berbeda | 7.361 (32.555 kemunculan) |
| Potensial berbeda | 233 (4.055 kemunculan) |
| Terminal berbeda | 637 |
| Gambar render | 1.351 @ 300 DPI, 1-bit |

**Batas keras yang harus dinyatakan ke user bila relevan:**

- Gambar menunjukkan **perlengkapan maksimum seri**, bukan yang terpasang di mesin
  tertentu. Penentu kelengkapan = sheet `INDEX` opsi (`X` = tidak terpasang).
- Tidak ada **part number katalog, rating, atau deskripsi fungsi** di dokumen ini.
  Ada 19 *order code* (bukan part number) di 8 sheet — lihat `A_HOW_TO_READ.md` §8.1.
- `#NN` nomor jalur hanya ada di **7 dari 1.351** sheet. Bukan koordinat global.
- Knowledge base tidak bisa menilai **keamanan** sebuah desain.

---

## Format Catatan

### Template tetap (salin apa adanya)

Setiap pekerjaan atas satu dokumen dicatat sebagai satu entri dengan **lima field
wajib**:

```markdown
### CAT-<YYYYMMDD>-<nn> · <judul singkat>

- **Tanggal:** YYYY-MM-DD
- **Sumber/path:** <path relatif atau absolut ke file sumber, harus nyata>
- **Ringkasan:** <2–5 kalimat: apa yang dikerjakan, hasil terukur, keputusan>
- **Status:** belum | sedang | selesai
- **Bukti verifikasi:** <perintah yang dijalankan + hasil angka>

**Catatan tambahan (opsional):**

- Ambiguitas: <apa yang tidak jelas di sumber, jika ada>
- Tindak lanjut: <apa yang masih harus dikerjakan>
```

**Aturan pengisian field:**

| Field | Aturan |
|---|---|
| Tanggal | Format `YYYY-MM-DD`. Satu entri = satu tanggal. |
| Sumber/path | Harus path yang bisa dicek dengan `test -f`. Tidak boleh `[待补]` untuk status `selesai`. |
| Ringkasan | Sebut **angka hasil ukur**, bukan kesan ("bagus", "rapi"). |
| Status | Hanya salah satu: `belum`, `sedang`, `selesai`. |
| Bukti verifikasi | Perintah + output ringkas. Tanpa ini, status tidak sah. |

### Contoh entri catatan (CONTOH — jangan dihapus, ini rujukan format)

```markdown
### CAT-20261108-01 · Konversi 6 PDF diagram Manroland R700 + QC buta

- **Tanggal:** 2026-11-08
- **Sumber/path:** `Diagram Manroland/` (6 PDF: Cicuit Diagram +FB.pdf,
  Circuit Diagram +Ax.pdf, Circuit Diagram +BA, Cx, DA.pdf, Circuit Diagram +EA.pdf,
  Circuit Diagram +FA.pdf, Circuit Diagram +Jx.pdf)
- **Ringkasan:** Keenam PDF adalah ekspor vektor CAE (bukan scan), sehingga
  ekstraksi memakai text layer PDF, bukan OCR. Dihasilkan knowledge base 1.351
  sheet + graf 34.890 cross-reference. QC buta oleh 3 agent: 51/52 (98,1%),
  0 fabrikasi. Putaran 2 setelah perbaikan: 6/6 pada soal tersulit.
  11 cacat ditemukan dan diperbaiki.
- **Status:** selesai
- **Bukti verifikasi:**
  - `python pipeline/qa/qa_fidelity_full.py` → 1351/1351 sheet, 180.916 label, 0 hilang
  - `python pipeline/qa/qa_links.py` → 108.821 link, 0 rusak
  - `python QC/kb_selftest.py` → 25/25
  - `python QC/score.py` → 51/52 (98,1%), 0 fabrikasi

**Catatan tambahan:**
- Ambiguitas: order code `8037D44A002` tercetak dekat K598 tetapi **bukan** part
  number-nya; didokumentasikan di `A_HOW_TO_READ.md` §8.1.
- Tindak lanjut: dokumen lain belum terdaftar → lihat bagian Backlog.
```

---

## Prosedur Menambah Dokumen ke Knowledge Base

### Prasyarat

1. File sumber ada dan bisa dibaca. Catat path persisnya.
2. Tentukan jenis PDF: **vektor + text layer** atau **scan**.
   - Cek: `page.get_text("words")` mengembalikan kata bermakna → vektor.
   - Jika scan → jalur OCR (skill `scan2md`), dan **catat bahwa kualitas lebih rendah**.
3. Pastikan dokumen belum ada di backlog dengan path sama (hindari duplikasi).

### Langkah eksekusi

Jalankan dari `Manroland_KnowledgeBase/pipeline/`:

```powershell
$py = "C:\Users\muham\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"

# 1. Daftarkan dokumen baru di schema.py (DOCUMENTS + DOC_TITLE_CODE)
#    -> tanpa ini, extract.py tidak akan melihatnya.

# 2. Ekstraksi
& $py extract.py --only "<docKey>" --force

# 3. Rekonstruksi tabel (pin map / terminal strip)
& $py tables.py "<docKey>"

# 4. Bangun ulang graf + Markdown + export + sinkronisasi angka prosa
& $py build.py

# 5. Render gambar 300 DPI (opsional tapi disarankan)
& $py render.py --only "<docKey>"
```

### Adaptasi bila struktur berbeda

Jika dokumen baru punya konvensi berbeda (bukan manroland):

| Gejala | Tempat menyesuaikan |
|---|---|
| Label tidak dikenali (semua jadi `text`) | `pipeline/grammar.py` → regex, `pipeline/extract.py` → `classify()` |
| Ukuran/kolom halaman berbeda | `pipeline/schema.py` → geometri `COL_EDGES`, `FRAME_*` |
| Tabel tidak terbentuk | `pipeline/tables.py` → ambang `MIN_H_RULE`, `MIN_V_RULE` |
| Judul section tidak terbaca | `pipeline/schema.py` → `SECTION_TOPICS` |

Tambahkan **case uji** di `QC/trap_recheck.py` untuk konvensi baru yang rawan salah.

### Gerbang verifikasi (WAJIB sebelum status `selesai`)

Semua harus lulus. Jika salah satu gagal → status tetap `sedang`.

```powershell
& $py pipeline/qa/qa_final.py           # 17 acceptance check
& $py pipeline/qa/qa_fidelity_full.py   # setiap label setiap sheet vs PDF
& $py pipeline/qa/qa_links.py           # setiap link internal
& $py QC/consistency.py                 # angka prosa vs data
& $py QC/trap_recheck.py                # jebakan struktural
```

**Ambang lulus:** fidelitas `0 hilang`, link `0 rusak`, consistency `0 failed`.
Jika ada kegagalan, perbaiki penyebabnya — **jangan turunkan ambangnya.**

### Cara memutuskan dokumen berikutnya

Aturan deterministik, dipakai apa adanya:

1. **Ambil semua baris dengan status `belum`** di bagian Backlog.
2. **Buang baris yang path-nya `[待补]`** — tidak bisa dikerjakan; ini memicu
   permintaan daftar dokumen ke user (bagian Jika daftar dokumen belum tersedia).
3. Urutkan sisa baris: **Prioritas** (P0 → P3), lalu **ID** menaik.
4. Ambil baris pertama. Ubah statusnya jadi `sedang` dan isi **Pemilik**.
5. Jika tidak ada baris yang bisa dikerjakan → **jangan mengarang pekerjaan**.
   Laporkan: *"Backlog tidak punya dokumen dengan path nyata. Mohon berikan daftar
   dokumen."* lalu berhenti.

### Jika daftar dokumen belum tersedia

Jangan menebak nama file atau folder. Isi backlog dengan placeholder bertanda
`[待补]`, dan minta user mengisi. Format permintaan ke user:

> Mohon berikan daftar dokumen berikutnya: **path folder/file**, **jenis**
> (PDF vektor / scan / Office), dan **prioritas** bila ada. Backlog saat ini masih
> `[待补]` sehingga belum ada yang bisa diproses.

---

## Backlog

**Kolom wajib:** Nama/Path · Status · Pemilik.
Nilai Status: `belum` | `sedang` | `selesai`.

### Contoh entri backlog

> **CONTOH FORMAT — jangan dihapus, jangan dihitung sebagai pekerjaan.**
> Baris BL-000 di bawah sengaja menunjuk dokumen yang juga ada di Backlog
> aktif (BL-001) hanya agar bentuk kolomnya terlihat. Rujukan kerja yang
> sah adalah tabel di bagian **Backlog aktif**; BL-000 diabaikan saat
> menghitung status.

| ID | Nama/Path | Status | Pemilik | Prioritas | Catatan |
|---|---|---|---|---|---|
| `BL-000` | `Diagram Manroland/Cicuit Diagram +FB.pdf` | `selesai` | lead | P1 | *contoh format* — 22 sheet, doc code `8039G38K159`, lihat `CAT-20261108-01` |

### Backlog aktif

| ID | Nama/Path | Status | Pemilik | Prioritas | Catatan |
|---|---|---|---|---|---|
| `BL-001` | `Diagram Manroland/Cicuit Diagram +FB.pdf` | `selesai` | lead | P1 | 22 sheet · `8039G38K159` · 3 `reference module` |
| `BL-002` | `Diagram Manroland/Circuit Diagram +Ax.pdf` | `selesai` | lead | P1 | 403 sheet · `8039G38I902` · volume terbesar ke-2 |
| `BL-003` | `Diagram Manroland/Circuit Diagram +BA, Cx, DA.pdf` | `selesai` | lead | P1 | 247 sheet · `8039G38J415` |
| `BL-004` | `Diagram Manroland/Circuit Diagram +EA.pdf` | `selesai` | lead | P1 | 407 sheet · `8039G38E915` · volume terbesar |
| `BL-005` | `Diagram Manroland/Circuit Diagram +FA.pdf` | `selesai` | lead | P1 | 58 sheet · `8039G38K212` |
| `BL-006` | `Diagram Manroland/Circuit Diagram +Jx.pdf` | `selesai` | lead | P1 | 214 sheet · `039G38F308` |
| `BL-007` | `[待补]` | `belum` | — | `[待补]` | Dokumen berikutnya belum diberikan user |
| `BL-008` | `[待补]` | `belum` | — | `[待补]` | Cadangan placeholder |
| `BL-009` | `[待补]` | `belum` | — | `[待补]` | Cadangan placeholder |

### Ringkasan backlog

Dihitung dari **Backlog aktif** saja (`BL-001`…`BL-009`). Baris contoh `BL-000`
tidak dihitung.

| Status | Jumlah |
|---|---:|
| `selesai` | 6 |
| `sedang` | 0 |
| `belum` (semua `[待补]`, belum bisa dikerjakan) | 3 |
| **Total** | **9** |

**Dokumen berikutnya yang diproses:** ikuti bagian *Cara memutuskan dokumen
berikutnya*. Saat ini semua baris `belum` masih bertanda `[待补]`, sehingga
**tidak ada yang bisa dikerjakan**. Tindakan yang benar adalah meminta daftar
dokumen ke user (lihat *Jika daftar dokumen belum tersedia*). Jangan menebak.

---

## Log Perubahan

Catatan ini **tidak boleh dihapus**. Entri lama tetap; koreksi = tambah baris baru.

| Tanggal | Versi | Perubahan | Bukti |
|---|---|---|---|
| 2026-11-08 | 1.0 | `agent.md` dibuat. Backlog diisi 6 dokumen Manroland (path nyata, status `selesai`) + 3 placeholder `[待补]`. | `test -f agent.md` lulus; 6 path dicek ada |
| 2026-11-08 | 1.0 | Rujukan QC: putaran 1 98,1% (51/52), putaran 2 6/6, 11 cacat diperbaiki. | `QC/QC_REPORT.md`, `QC/SCORE_REPORT.txt` |
| 2026-11-08 | 1.1 | **Koreksi heading.** Versi 1.0 memakai heading bernomor (`## 4. Backlog`, `## 2. Format Catatan`) sehingga perintah cek `grep -q '^## Backlog'` **GAGAL**. Semua heading dinormalkan ke bentuk tanpa nomor. | `QC/verify_agent_md.py` → 24/24 lulus; perintah cek minimal kini exit 0 |
| 2026-11-08 | 1.1 | `BL-000` diberi keterangan eksplisit sebagai contoh format agar tidak dihitung sebagai pekerjaan; ringkasan backlog menyatakan BL-000 dikecualikan. | `QC/check_fences.py` → fence seimbang, heading asli 22 |

---

## Cara Cek File Ini

Perintah minimal (dari root proyek):

```bash
test -f agent.md && grep -q '^## Backlog' agent.md && grep -q '^## Format Catatan' agent.md
```

Padanan PowerShell (Windows):

```powershell
(Test-Path agent.md) -and
(Select-String -Path agent.md -Pattern '^## Backlog' -Quiet) -and
(Select-String -Path agent.md -Pattern '^## Format Catatan' -Quiet)
```

Cek tambahan yang disarankan — memastikan backlog benar-benar bisa dipakai:

```powershell
# setiap baris backlog harus punya status yang sah
Select-String -Path agent.md -Pattern '^\| `BL-' | ForEach-Object {
  if ($_.Line -notmatch '`(belum|sedang|selesai)`') { "STATUS HILANG: $($_.Line)" }
}
```

---

## Ringkasan Kesepakatan

| Aspek | Kesepakatan |
|---|---|
| Bahasa catatan | Indonesia, istilah teknis apa adanya |
| Tanggal | `YYYY-MM-DD` |
| Status | `belum` / `sedang` / `selesai` — tidak ada nilai lain |
| Bukti | Perintah + angka; tanpa itu status tidak sah |
| Dokumen tak dikenal | Placeholder `[待补]`, **jangan** dikarang |
| Menghapus catatan | Dilarang; koreksi dengan menambah |
| Prioritas default | P1 untuk dokumen yang disebut user secara eksplisit |
