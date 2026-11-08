"""Check code-fence integrity and that template pseudo-headings are fenced."""
import io, os

P = r"C:\Users\muham\OneDrive\ドキュメント\Github\IKG\agent.md"
s = io.open(P, encoding="utf-8").read()
lines = s.splitlines()

FENCE = "`" * 3
fence_open = False
inside = []
n_fences = 0
for i, l in enumerate(lines, 1):
    if l.startswith(FENCE):
        n_fences += 1
        fence_open = not fence_open
        continue
    if fence_open and l.startswith("### "):
        inside.append((i, l[:70]))

print("total fence markers:", n_fences)
print("balanced (even):", n_fences % 2 == 0)
print("unclosed at EOF:", fence_open)
print()
print("pseudo-headings that are INSIDE code fences (correct, won't render as headings):")
for i, l in inside:
    print("   line %-4d %s" % (i, l))
print()
# real H2/H3 headings outside fences
fence_open = False
real = []
for i, l in enumerate(lines, 1):
    if l.startswith(FENCE):
        fence_open = not fence_open
        continue
    if not fence_open and (l.startswith("## ") or l.startswith("### ")):
        real.append((i, l))
print("real rendered headings: %d" % len(real))
for i, l in real:
    print("   line %-4d %s" % (i, l))
