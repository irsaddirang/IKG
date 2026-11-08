"""
consistency.py -- catch documentation drift: numbers quoted in prose that disagree
with the data, and cross-document contradictions.

The blind test found A_HOW_TO_READ.md quoting 24V = 1,096/388 while
INDEX_NETS.md said 1,327/447, and one page saying order codes are on "5 of 1,351
sheets" while another said "9 of 1,351". Both are now impossible for the
auto-generated tables, but prose can still drift, so this checker enforces it.
"""
import io, os, re, json, sys

KB = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase"
MD = os.path.join(KB, "md")
g = json.load(io.open(os.path.join(KB, "data", "derived", "graph.json"),
                      encoding="utf-8"))

ok = fail = 0
def chk(name, cond, detail=""):
    global ok, fail
    if cond:
        ok += 1; print("  PASS  %-58s %s" % (name, detail))
    else:
        fail += 1; print("  FAIL  %-58s %s" % (name, detail))

def read(p):
    return io.open(p, encoding="utf-8").read()

print("=" * 78)
print("1. Every MEASURED net figure quoted in the system docs must match the data")
print("=" * 78)
nets = {n["net"]: n for n in g["nets"]}
a_read = read(os.path.join(MD, "01_SYSTEM", "A_HOW_TO_READ.md"))
# within the generated block only
m = re.search(r"(?s)AUTO-GENERATED name=A-section6-nets -->(.*?)<!-- /AUTO-GENERATED",
              a_read)
block = m.group(1) if m else ""
bad = []
for net in ["24V", "0V", "L1", "L2", "PE", "L3", "L24", "M24+", "M501", "N", "L230"]:
    r = re.search(r"\| `%s` \| (\d+) \| (\d+) \|" % re.escape(net), block)
    if not r:
        bad.append((net, "missing"))
        continue
    occ, sh = int(r.group(1)), int(r.group(2))
    real = nets.get(net)
    if not real:
        bad.append((net, "not in graph"))
    elif occ != real["occurrences"] or sh != real["sheet_count"]:
        bad.append((net, "doc %d/%d vs data %d/%d" %
                    (occ, sh, real["occurrences"], real["sheet_count"])))
chk("A_HOW_TO_READ §6 net table matches graph.json", not bad, str(bad))

# and INDEX_NETS.md
nets_md = read(os.path.join(MD, "03_INDEX", "INDEX_NETS.md"))
bad2 = []
for net in ["24V", "0V", "PE", "L1"]:
    r = re.search(r"\| `%s` \| (\d+) \| (\d+) \|" % re.escape(net), nets_md)
    if not r:
        bad2.append((net, "missing"))
    else:
        real = nets[net]
        if int(r.group(1)) != real["occurrences"] or int(r.group(2)) != real["sheet_count"]:
            bad2.append((net, "mismatch"))
chk("INDEX_NETS.md matches graph.json", not bad2, str(bad2))

print()
print("=" * 78)
print("2. Cross-document contradiction: order-code sheet count")
print("=" * 78)
claims = {}
for rel in ("01_SYSTEM/A_HOW_TO_READ.md",):
    t = read(os.path.join(MD, rel))
    for mm in re.finditer(r"(\d+)\s+of\s+1,?351\s+sheets", t):
        claims.setdefault(rel, set()).add(int(mm.group(1)))
# sheet pages
sheet_claims = set()
for doc in os.listdir(os.path.join(MD, "02_SHEETS")):
    d = os.path.join(MD, "02_SHEETS", doc)
    if not os.path.isdir(d):
        continue
    for f in os.listdir(d):
        if f.startswith("SHEET_") and f.endswith(".md"):
            t = read(os.path.join(d, f))
            if "order/manufacturing codes" in t:
                for mm in re.finditer(r"(\d+)\s+of\s+1,351\s+sheets", t):
                    sheet_claims.add(int(mm.group(1)))
chk("sheet pages agree on the order-code sheet count",
    len(sheet_claims) <= 1, "values seen: %s" % sorted(sheet_claims))

# measured, computed from the extraction rather than hard-coded
import glob
n_sheets_with_codes = 0
distinct_codes = set()
distinct_nopart = set()
for p in glob.glob(os.path.join(KB, "data", "raw", "*", "*.json")):
    r = json.load(io.open(p, encoding="utf-8"))
    oc = r.get("ordercodes") or []
    np_ = r.get("noparts") or []
    if oc or np_:
        n_sheets_with_codes += 1
        distinct_codes.update(o["code"] for o in oc)
        distinct_nopart.update(o["marker"] for o in np_)

chk("documented sheet count equals the measured count",
    sheet_claims == {n_sheets_with_codes},
    "docs say %s, measured %d" % (sorted(sheet_claims), n_sheets_with_codes))

# the documented distinct-code figure must also match
m_codes = re.search(r"\*\*(\d+) distinct order codes", a_read)
chk("documented distinct order-code count matches",
    bool(m_codes) and int(m_codes.group(1)) == len(distinct_codes),
    "docs say %s, measured %d" % (m_codes.group(1) if m_codes else "?",
                                  len(distinct_codes)))
m_np = re.search(r"(\d+) distinct `noPart` markers", a_read)
chk("documented noPart marker count matches",
    bool(m_np) and int(m_np.group(1)) == len(distinct_nopart),
    "docs say %s, measured %d" % (m_np.group(1) if m_np else "?",
                                  len(distinct_nopart)))

print()
print("=" * 78)
print("3. Headline counts quoted in README / README_FIRST match the data")
print("=" * 78)
st = g["stats"]
labels = sum(s["counts"]["lines"] for s in g["sheets"])
for rel in ("../README.md", "00_READ_ME_FIRST.md"):
    p = os.path.normpath(os.path.join(MD, rel))
    t = read(p)
    checks = [
        ("sheets", str(len(g["sheets"]))),
        ("labels", "{:,}".format(labels)),
        ("xrefs", "{:,}".format(st["xref_edges"])),
    ]
    miss = [k for k, v in checks if v not in t]
    chk("%s quotes current headline counts" % os.path.basename(p),
        not miss, "missing %s" % miss)

print()
print("=" * 78)
print("4. No stale 'part numbers do not exist' overclaim remains")
print("=" * 78)
for rel in ("00_READ_ME_FIRST.md", "00_QUERY_PLAYBOOK.md",
            "01_SYSTEM/A_HOW_TO_READ.md", "../README.md"):
    p = os.path.normpath(os.path.join(MD, rel))
    t = read(p)
    # the corrected wording should mention "catalog" or point at §8.1 / order codes
    okk = ("catalog part number" in t.lower()
           or "order code" in t.lower())
    chk("%s acknowledges order codes" % os.path.basename(p), okk)

print()
print("=" * 78)
print("5. Every net with occurrences > 0 appears in INDEX_NETS")
print("=" * 78)
missing = [n["net"] for n in g["nets"] if "`%s`" % n["net"] not in nets_md]
chk("all nets listed", not missing, "missing %s" % missing[:5])

print()
print("=" * 78)
print("CONSISTENCY: %d passed, %d failed" % (ok, fail))
print("=" * 78)
sys.exit(1 if fail else 0)
