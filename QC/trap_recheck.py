"""
trap_recheck.py -- verify the hard-case traps are now unambiguous in the MD.
Each check answers the question using only the generated Markdown.
"""
import io, os, re

KB = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase"
MD = os.path.join(KB, "md")
ok = fail = 0

def chk(name, cond, detail=""):
    global ok, fail
    if cond:
        ok += 1
        print("  PASS  %s  %s" % (name, detail))
    else:
        fail += 1
        print("  FAIL  %s  %s" % (name, detail))

def read(p):
    return io.open(p, encoding="utf-8").read()

print("=== TRAP 1: two side-by-side pin tables must not be merged ===")
s = read(os.path.join(MD, "02_SHEETS", "EA", "SHEET_0200.md"))
tables = re.findall(r"### Table \d+ — (\d+) data rows × (\d+) columns \([^)]*\)(?: — \*\*(.+?)\*\*)?", s)
chk("two tables split", len(tables) == 2, "found %d" % len(tables))
if len(tables) == 2:
    chk("table 1 is A356/13", tables[0][2] == "A356/13", str(tables[0]))
    chk("table 2 is A356/14", tables[1][2] == "A356/14", str(tables[1]))
    chk("each is 5 columns (not merged 11)", tables[0][1] == "5" and tables[1][1] == "5",
        "%s / %s" % (tables[0][1], tables[1][1]))
    chk("each is 24 data rows", tables[0][0] == "24" and tables[1][0] == "24",
        "%s / %s" % (tables[0][0], tables[1][0]))

# Q9 / Q10 answered structurally
i1 = s.find("— **A356/13**")
i2 = s.find("— **A356/14**")
seg1 = s[i1:i2]
seg2 = s[i2:]
chk("Q9 A356/13 4A/4B/4C -> 0.1 -> /328.B",
    "| `4A` | `4B` | `4C` | `0.1` | `/328.B` |" in seg1)
m = re.search(r"\| `26A` \| `26B` \| `26C` \| `18\.7` \|(.*?)\|", seg1)
chk("Q10 A356/13 26A/26B/26C = 18.7 with EMPTY strompfad",
    bool(m) and m.group(1).strip() == "", repr(m.group(1)) if m else "no row")
chk("Q10 the 21.7 value lives in the OTHER table (A356/14)",
    "| `26A` | `26B` | `26C` | `21.7` | `/191.G` |" in seg2)
chk("A356/13 segment does NOT contain 21.7", "21.7" not in seg1)

print("\n=== TRAP 2: two K598 wires on FB#9, both present ===")
s9 = read(os.path.join(MD, "02_SHEETS", "FB", "SHEET_0009.md"))
chk("K598:A2 -> /14.F", "K598:A2" in s9 and "/14.F" in s9)
chk("K598:2 -> /14.D", "K598:2" in s9 and "/14.D" in s9)
chk("both path numbers present", "#65" in s9 and "#64" in s9)

print("\n=== TRAP 3: /999.A and K9999 must be absent ===")
import glob
blob = []
for dp, dn, fn in os.walk(MD):
    for f in fn:
        if f.endswith(".md"):
            blob.append(read(os.path.join(dp, f)))
allmd = "\n".join(blob)
chk("/999.A absent", "/999.A" not in allmd)
chk("K9999 absent", "K9999" not in allmd)

print("\n=== TRAP 4: #67 is not global (4 wires on one sheet) ===")
rows67 = [l for l in s9.splitlines() if "`#67`" in l]
chk("FB#9 has multiple #67 rows", len(rows67) >= 4, "%d rows" % len(rows67))
xrefs = set(re.findall(r"`/(\d+\.[A-H])`", "\n".join(rows67)))
chk("those #67 rows go to different destinations", len(xrefs) >= 3, sorted(xrefs))

print("\n=== TRAP 5: order codes documented, not attributed as part numbers ===")
s14 = read(os.path.join(MD, "02_SHEETS", "FB", "SHEET_0014.md"))
chk("8037D44A002 indexed", "8037D44A002" in s14)
chk("explicit warning present", "NOT device part numbers" in s14)

print("\n=== TRAP 6: series-maximum rule stated ===")
sread = read(os.path.join(MD, "00_READ_ME_FIRST.md"))
chk("series maximum stated", "series maximum" in sread.lower())
chk("points to INDEX", "INDEX" in sread)

print("\n=== TRAP 7: net counting rule explicit ===")
nets = read(os.path.join(MD, "03_INDEX", "INDEX_NETS.md"))
chk("counting rule stated", "Counting rule" in nets)
chk("per-document table present", "Sheets per document" in nets)

print("\n" + "=" * 60)
print("TRAP RECHECK: %d passed, %d failed" % (ok, fail))
