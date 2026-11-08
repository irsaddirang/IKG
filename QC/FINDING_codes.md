# QC finding — unexplained alphanumeric codes beside devices

**Discovered by:** `blind-agent-c`, question Q20 (part-number trap).
**Severity:** medium — it does not produce a wrong answer, but it is the single most
likely place for a future agent to *manufacture* one.

## The observation

On several sheets there are long alphanumeric codes printed next to device tags,
for example on `+FB` sheet 14:

| Code | Printed beside | Location |
|---|---|---|
| `8037D44A002` | `+A497/1`, `K598` | col E, y ≈ 558.4 |
| `8Z37D51A008` | `K180` | col E |
| `8037B443600` | `S275` | col E |
| `8001L131905` | `Y077` | col E |

These look like part numbers / order codes. The knowledge base does **not** currently
explain what they are, and does not label them. That is the ambiguity.

## Why it matters

The KB correctly says "no part numbers in these drawings". An agent that then sees
`8037D44A002` sitting right next to `K598` is in an awkward position: the KB gives it
a code, denies that part numbers exist, and does not reconcile the two. A careless
agent could answer "the part number of K598 is 8037D44A002" — which is exactly the
class of confident fabrication this project is built to prevent.

## Resolution

Determine what these codes actually are from the source, then document them
explicitly in `01_SYSTEM/A_HOW_TO_READ.md` with a factual label and a warning that
they are **not** to be attributed to a device unless the drawing states so.

To settle it: inspect the geometry around those codes (which device the leader line
or adjacency actually binds to), and check whether the same code appears on the
`ANORDNUNGSPLAN` (disposition plan) sheets, which carry physical part ordering
information.

See `code_probe.py` for the measurement.
