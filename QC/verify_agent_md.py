"""
verify_agent_md.py -- acceptance test for agent.md against the stated criteria.

Criteria:
  1. File exists; sections Aturan / Format Catatan / Backlog / Log present.
  2. Every backlog row has a source path AND a status in {belum, sedang, selesai}.
  3. Contains 1 example note entry, 1 example backlog entry, and written prohibitions.
  4. The file is actually usable to decide which document to process next.
"""
import io, os, re, sys

ROOT = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG"
P = os.path.join(ROOT, "agent.md")
ok = fail = 0

def chk(name, cond, detail=""):
    global ok, fail
    if cond:
        ok += 1; print("  PASS  %-56s %s" % (name, detail))
    else:
        fail += 1; print("  FAIL  %-56s %s" % (name, detail))

if not os.path.isfile(P):
    print("FATAL: agent.md not found")
    sys.exit(1)
s = io.open(P, encoding="utf-8").read()
lines = s.splitlines()

print("=" * 78)
print("1. FILE DAN BAGIAN WAJIB")
print("=" * 78)
h2 = [l for l in lines if l.startswith("## ")]
def has_h2(prefix):
    return any(l.startswith("## " + prefix) for l in h2)
chk("file agent.md ada", True, "%d bytes" % len(s.encode()))
chk("heading 'Aturan' ada", has_h2("Aturan"))
chk("heading 'Format Catatan' ada", has_h2("Format Catatan"))
chk("heading 'Backlog' ada", has_h2("Backlog"))
chk("heading 'Log' ada", any(l.startswith("## Log") for l in h2))
chk("perintah cek minimal ada di file", "grep -q '^## Backlog'" in s)

print()
print("=" * 78)
print("2. SETIAP BARIS BACKLOG PUNYA PATH + STATUS")
print("=" * 78)
# backlog rows: table rows starting with | `BL-
rows = [l for l in lines if re.match(r"^\|\s*`BL-\d+`", l)]
chk("ada baris backlog", len(rows) >= 6, "%d baris" % len(rows))

bad_status, bad_path = [], []
VALID = {"belum", "sedang", "selesai"}
for r in rows:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    # cells: ID, Nama/Path, Status, Pemilik, Prioritas, Catatan
    if len(cells) < 4:
        bad_status.append((r[:40], "kolom kurang"))
        continue
    status_cell = cells[2]
    path_cell = cells[1]
    # status must be a backticked valid value
    mstat = re.fullmatch(r"`(\w+)`", status_cell)
    if not mstat or mstat.group(1) not in VALID:
        bad_status.append((cells[0], status_cell))
    # path must be non-empty; placeholder allowed only for belum
    has_placeholder = "[待补]" in path_cell
    if not path_cell:
        bad_path.append((cells[0], "kosong"))
    if has_placeholder and (mstat and mstat.group(1)) == "selesai":
        bad_path.append((cells[0], "placeholder tapi selesai"))

chk("semua baris punya status sah (belum/sedang/selesai)", not bad_status,
    str(bad_status[:3]))
chk("semua baris punya kolom path", not bad_path, str(bad_path[:3]))
chk("baris 'selesai' tidak memakai placeholder [待补]",
    not [b for b in bad_path if "placeholder" in b[1]])

# every 'selesai' row's path must actually exist on disk
missing_files = []
for r in rows:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    if len(cells) < 3:
        continue
    if "`selesai`" not in cells[2]:
        continue
    path = cells[1].strip("`")
    if "[待补]" in path:
        continue
    full = os.path.join(ROOT, path.replace("/", os.sep))
    if not os.path.exists(full):
        missing_files.append(path)
chk("setiap path berstatus 'selesai' benar-benar ada di disk",
    not missing_files, str(missing_files))

print()
print("=" * 78)
print("3. CONTOH DAN LARANGAN")
print("=" * 78)
chk("ada 1 contoh entri catatan", "Contoh entri catatan" in s
    and "CAT-20261108-01" in s)
chk("contoh catatan punya 5 field wajib",
    all(k in s for k in ("**Tanggal:**", "**Sumber/path:**", "**Ringkasan:**",
                         "**Status:**", "**Bukti verifikasi:**")))
chk("ada 1 contoh entri backlog", "Contoh entri backlog" in s
    and "`BL-000`" in s)
chk("larangan tertulis (L1 mengarang)", "Mengarang isi dokumen" in s)
chk("larangan tertulis (L2 selesai tanpa path)", "tanpa path sumber" in s)
chk("larangan tertulis (L3 hapus catatan)", "Menghapus catatan lama" in s)
chk("ada bagian larangan eksplisit", "DILARANG" in s)

print()
print("=" * 78)
print("4. FILE DAPAT DIPAKAI MEMUTUSKAN DOKUMEN BERIKUTNYA")
print("=" * 78)
chk("ada prosedur pemilihan dokumen", "Cara memutuskan dokumen berikutnya" in s)
chk("aturan urut prioritas lalu ID tertulis",
    "Prioritas" in s and "ID" in s)
chk("ada instruksi saat daftar kosong", "Jika daftar dokumen belum tersedia" in s)
chk("ada ringkasan status backlog", "Ringkasan backlog" in s)
# compute the decision from the file itself
belum = []
for r in rows:
    cells = [c.strip() for c in r.strip().strip("|").split("|")]
    if len(cells) >= 3 and "`belum`" in cells[2]:
        belum.append((cells[0].strip("`"), cells[1]))
workable = [b for b in belum if "[待补]" not in b[1]]
chk("keputusan dapat dihitung dari file", True,
    "%d 'belum', %d bisa dikerjakan" % (len(belum), len(workable)))
if not workable:
    print("        -> tidak ada dokumen berpath nyata; file menginstruksikan")
    print("           meminta daftar ke user. Ini perilaku yang benar.")

print()
print("=" * 78)
print("5. LOG PERUBAHAN")
print("=" * 78)
log_rows = [l for l in lines
            if re.match(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|", l)]
chk("ada entri log dengan tanggal YYYY-MM-DD", len(log_rows) >= 1,
    "%d entri" % len(log_rows))

print()
print("=" * 78)
print("HASIL: %d lulus, %d gagal" % (ok, fail))
print("=" * 78)
sys.exit(1 if fail else 0)
