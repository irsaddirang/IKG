import os, re, sys, collections

MD = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\Manroland_KnowledgeBase\md"
ROOT = os.path.dirname(MD)

link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

total = 0
bad = []
files = []
for dp, dns, fns in os.walk(MD):
    for fn in fns:
        if fn.endswith(".md"):
            files.append(os.path.join(dp, fn))
        elif fn.endswith(".png"):
            pass

print("markdown files:", len(files))

checked = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    base = os.path.dirname(f)
    for m in link_re.finditer(s):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#")[0]
        if not target:
            continue
        checked += 1
        p = os.path.normpath(os.path.join(base, target))
        if not os.path.exists(p):
            bad.append((os.path.relpath(f, MD), m.group(1), os.path.relpath(p, ROOT)))

print("internal links checked:", checked)
print("broken:", len(bad))
kind = collections.Counter()
for f, t, p in bad:
    if "/images/" in p.replace("\\", "/"):
        kind["image"] += 1
    elif "_TOC" in t:
        kind["toc"] += 1
    else:
        kind["other"] += 1
print("by kind:", dict(kind))
for b in bad[:15]:
    print("   ", b)
