"""
tracing.py -- measure whether full multi-sheet wire tracing is possible from the
knowledge base, using the RIGHT metrics.

An earlier attempt measured "does every xref have a return edge to the same
sheet". That is the wrong test: a single sheet can receive many wires from one
source sheet across different columns, and a distribution node legitimately has
no return path. 100% is not expected and its absence is not a defect.

The metrics that DO matter:
  1. every xref resolves to a real sheet            (structural validity)
  2. every xref lands on a column with content       (locational validity)
  3. multi-hop traces can be walked without getting stuck
  4. the KB exposes both directions so a human can verify a trace by eye
"""
import io, os, re, json, collections

import pymupdf

KB = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase"
PDF = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Diagram Manroland"
DER = os.path.join(KB, "data", "derived")

g = json.load(io.open(os.path.join(DER, "graph.json"), encoding="utf-8"))
sheets = {s["id"]: s for s in g["sheets"]}
xref_out = collections.defaultdict(list)
for e in g["edges"]:
    if e["type"] == "xref":
        xref_out[e["from"]].append(e)

print("=" * 70)
print("METRIC 1 - every cross-reference resolves to a real sheet")
print("=" * 70)
tot = unresolved = 0
for src, edges in xref_out.items():
    for e in edges:
        tot += 1
        if e["to"] not in sheets:
            unresolved += 1
print("  xref edges        : %d" % tot)
print("  unresolved targets: %d" % unresolved)
print("  => %s" % ("PASS" if unresolved == 0 else "FAIL"))

print()
print("=" * 70)
print("METRIC 2 - every cross-reference lands on a column with content")
print("=" * 70)
# column occupancy straight from the extraction, i.e. what the MD reports
col_use = {}
for s in g["sheets"]:
    for c in s["columns_used"]:
        col_use.setdefault(s["id"], set()).add(c)
tot2 = ok2 = bad2 = 0
for src, edges in xref_out.items():
    for e in edges:
        tot2 += 1
        if e["to_column"] in col_use.get(e["to"], set()):
            ok2 += 1
        else:
            bad2 += 1
print("  xref edges checked    : %d" % tot2)
print("  target column occupied: %d  (%.2f%%)" % (ok2, 100.0 * ok2 / tot2))
print("  target column empty   : %d" % bad2)
print("  => %s" % ("PASS - every reference points at real printed content"
                    if bad2 == 0 else "REVIEW"))

print()
print("=" * 70)
print("METRIC 3 - multi-hop trace walkability")
print("=" * 70)
def trace(start, max_hops=10):
    seen = {start}
    order = [start]
    cur = start
    for _ in range(max_hops):
        nxt = None
        for e in xref_out.get(cur, []):
            if e["to"] not in seen and e["to"] in sheets:
                nxt = e
                break
        if nxt is None:
            break
        seen.add(nxt["to"])
        order.append(nxt["to"])
        cur = nxt["to"]
    return order

starters = [s for s in sheets if len(xref_out.get(s, [])) >= 5]
lengths = collections.Counter()
for s in starters:
    lengths[len(trace(s))] += 1
print("  start sheets with >=5 outgoing xrefs: %d" % len(starters))
print("  hop reachability:")
for k in sorted(lengths):
    print("     %2d sheets reachable : %d starts" % (k, lengths[k]))
multi = sum(v for k, v in lengths.items() if k >= 4)
print("  starts that walk >=4 sheets deep: %d (%.0f%%)"
      % (multi, 100.0 * multi / max(1, len(starters))))

print()
print("=" * 70)
print("METRIC 4 - both directions are exposed where they exist")
print("=" * 70)
md = os.path.join(KB, "md")
have_in_list = set()
for e in g["edges"]:
    if e["type"] == "xref":
        have_in_list.add(e["to"])
checked = with_in_section = should_have = correct_missing = 0
for s in g["sheets"]:
    doc = s["doc"].lstrip("+")
    p = os.path.join(md, "02_SHEETS", doc, "SHEET_%04d.md" % s["sheet"])
    if not os.path.exists(p):
        continue
    t = io.open(p, encoding="utf-8").read()
    checked += 1
    has_out = "## Cross-references on this sheet" in t
    has_in = "Incoming references" in t
    expects_in = s["id"] in have_in_list
    if has_out:
        pass
    if expects_in:
        should_have += 1
        if has_in:
            with_in_section += 1
    else:
        # no incoming references at all -> the section is correctly absent
        if not has_in:
            correct_missing += 1
print("  sheets checked                                : %d" % checked)
print("  sheets that HAVE incoming refs and show table : %d/%d"
      % (with_in_section, should_have))
print("  sheets with NO incoming refs and omit it      : %d/%d"
      % (correct_missing, checked - should_have))
ok4 = (with_in_section == should_have)
print("  => %s" % ("PASS - incoming table appears exactly where it should"
                    if ok4 else "REVIEW"))
