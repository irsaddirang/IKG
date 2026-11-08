# QC REPORT — Can an AI agent actually use this knowledge base?

**The question being answered:** *lakukan full test, QA dan QC, cari case-case sulit
pada mesin, apakah MD ini bisa digunakan dengan baik — apakah agent AI / LLM bisa
menggunakannya?*

## Verdict: **YES — and it measurably improved after the test exposed its weaknesses**

| Round | Blind benchmark | Fabrications |
|---|---|---|
| **Round 1** (original KB) | 51/52 — **98.1 %** | **0** |
| **Round 2** (after fixes) | **6/6 — 100 %** on the previously hardest questions | **0** |

Round 1 was scored against ground truth recomputed from the PDFs. Round 2 re-ran the
hardest questions against the fixed KB: the case that had been most at risk of
misreading — two side-by-side pin tables with identical pin labels — is now answered
correctly and cited from the table's own device label.

The test found **11 real defects** across two rounds. All are fixed, and a
**consistency checker** now runs inside the build so documentation cannot drift again.

---

## 1. Why this is a real test and not self-assessment

The obvious failure mode of "test your own KB" is marking your own homework.
Four controls prevent that:

**a) Independent ground truth.** Every answer key is recomputed **from the source
PDFs** by separate scripts (`gt*.py`, `answersheet.py`) that never read the generated
Markdown.

**b) Blind agents.** Agents are spawned *fresh*, restricted by prompt to
`Manroland_KnowledgeBase/md/`, and forbidden the PDFs, `QC/`, `data/`, `pipeline/`.

**c) A separate mechanical KB self-test.** `kb_selftest.py` answers all 26 questions
**programmatically from the Markdown alone**. This separates three different things:

```
PDF ──► answer_key.json ....... is the fact FINDABLE?            (ground truth)
MD  ──► kb_selftest.py ........ is the fact IN the MD?           (KB quality)
MD  ──► blind agents .......... can an agent RETRIEVE + USE it?  (usability)
```

**d) Disputed answers re-verified against the PDF.** Every agent claim that
conflicted with the answer key was re-checked in the source. Four round-1 scores were
revised **upward** on that evidence (Q11, Q14, Q21, Q24). The rubric was fixed before
answers were read.

---

## 2. Round 1 — 26 questions, 3 agents

| Tier | What it measures | Score |
|---|---|---|
| T1 Lookup | Find a device, title-block field, document | **6/6 — 100 %** |
| T2 Navigation | Follow `/sheet.column` cross-refs both ways | **10/10 — 100 %** |
| T3 Structure | Read pin tables, terminal strips, nets, columns | **12/12 — 100 %** |
| T4 Reasoning | Multi-sheet chains, grouping, comparison | **9/10 — 90 %** |
| **T5 Traps** | **Refuse to invent when the answer is absent** | **14/14 — 100 %** |
| **Overall** | 26 questions | **51/52 — 98.1 %** |

**Fabrications: 0. Fully correct: 25/26.** The single imperfect answer (Q16) came
from an ambiguous question plus an under-specified counting rule — now fixed.

---

## 3. Round 2 — 6 questions, fresh agent, after the fixes

Re-tested exactly the cases that had been trappy.

| Q | Case | Result |
|---|---|---|
| Q1 | `A356/13` row `4A/4B/4C` → BYTE.BIT + STROMPFAD | **correct** (`0.1` / `/328.B`) |
| Q2 | **the trap**: `A356/13` row `26A/26C` vs the neighbouring `A356/14` | **correct** (`18.7`, empty) and explicitly rejected `21.7 / /191.G` as the other table |
| Q3 | table dimensions | **correct** (24 data rows × 5 columns) |
| Q4 | `24V` most/fewest per document | **correct** (`+EA` 156, `+FB` 0) and **quoted the KB's counting rule verbatim** |
| Q5 | all `K598` wires on `FB#9` | **correct** — found both, with line numbers `#65` and `#64` |
| Q6 | part number of `K598` | **correct refusal**; identified `8037D44A002` as an order code that must not be attributed |

**6/6. Zero fabrication.** For Q2 and Q4 it cited the KB's own explanatory text —
evidence that adding the *explanation*, not just the data, is what made it reliable.

---

## 4. All 11 defects found and fixed

### Round 1

| # | Defect | Fixed by |
|---|---|---|
| 1 | **Net coverage gap** — 63 sheets with `24V.…` missing (numeric device segments, `\` sub-units, `( )` placeholder pins, spaced dots) | widened grammar |
| 2 | **False-positive regression** — `N. Hitzel` read as net `N`; prose `SPANNUNGSVERSORGUNG: 24V` read as a wire | segment-shape guard; 0 false positives verified |
| 3 | **Device/potential collision** — `M102/1`, `H240/01` re-read as potentials | `/n` is a rail only if the base has `V` or is `PE`/`N` |
| 4 | **Undocumented order codes** — the most likely place to invent a part number | new `ordercode`/`nopart` classes + reader's-guide §8.1 |
| 5 | **Overclaim** — "no part numbers exist" while order codes plainly did | corrected to "no *catalog* part numbers" |
| 6 | **Table caption wrong** — said 27 rows, rendered 24 | counts rendered body rows |
| 7 | **Contradictory conductor counts** — "×8 labels" vs "6 occurrences" | reworded: inventory vs blocks-containing-both |
| 8 | **Net counting rule implicit** (cause of the only imperfect answer) | rule stated explicitly + per-document table |

### Round 2

| # | Defect | Fixed by |
|---|---|---|
| 9 | **`A_HOW_TO_READ.md` §6 quoted stale net figures** (24V = 1,096/388) contradicting `INDEX_NETS.md` (1,327/447) | §6 table is now **auto-generated** by `pipeline/sync_docs.py`; `consistency.py` fails if they ever disagree |
| 10 | **Cross-document contradiction** — one page said order codes are on "5 of 1,351 sheets", another "9" | corrected to the **measured 8**; the checker derives the expected value from data instead of hard-coding it |
| 11 | **Two side-by-side pin tables merged** into one 11-column grid with duplicated pin labels — the single most misleading spot on `EA` 200 | `tables.py` splits a grid at any column band empty in every row; each table is labelled with its own device (`-A356/13`, `-A356/14`) |

Defect 11 was the most consequential: it converted a *layout trap* into a structural
impossibility. `trap_recheck.py` now asserts that the `A356/13` segment does not
contain `21.7` at all, so the confusion cannot reappear.

---

## 5. Verified final state

| Check | Result |
|---|---|
| Acceptance test | **17/17** |
| Label fidelity (whole corpus) | **180,916 / 180,916 — 0 missing** |
| Internal links | **0 broken / 108,821** |
| KB mechanical self-test | **25/25** |
| Trap recheck (structural) | **22/22** |
| Documentation consistency | **13/13** |
| Net coverage `24V` | 447 / 451 |
| Net coverage `0V` | 401 / 403 |
| Devices with PDF sheets missing from index | **0** |
| Order codes documented | **19 of 19** + 5 `noPart` markers |
| `sheet_total` present | **1,351 / 1,351** |

`PE`, `L24+/4`, `M24+`, `L1` match the PDF **exactly**. Residual net gaps (4 `24V`,
2 `0V`, 1 `N`) were each inspected: every one is a **prose mention**
(`SPANNUNGSVERSORGUNG: 24V`, `(24V)`, `IEC (N)`, `N. Hitzel`), not a wire.

---

## 6. Underlying capability — can wires actually be traced?

A usability score means little if the graph itself is unsound, so this was measured
separately (`tracing.py`):

| Metric | Result |
|---|---|
| Cross-references resolving to a real sheet | **34,890 / 34,890** |
| Cross-references landing on a column with printed content | **34,833 / 34,890 (99.84 %)** |
| Start sheets that walk ≥ 4 sheets deep | **97 %** |
| Both directions (outgoing + incoming) exposed on every sheet | **yes** |

The 57 non-landing references were inspected individually: their "empty" column
contains **only the DIN margin letter** (`G`, `A`, `F`, `C`), which the KB correctly
excludes. So these are a **limit of the occupancy test, not a KB defect**.

An earlier metric ("does every reference have a reciprocal reference back") was
**discarded as invalid**: a many-to-one distribution node legitimately has no return
path, so 40.5 % reciprocity is expected rather than a fault. Reporting that metric
would have raised a false alarm — recorded here so it is not repeated.

---

## 7. Reproduce

```powershell
$py = "C:\Users\muham\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"
cd QC

& $py gt3.py             # PDF-vs-KB coverage
& $py answersheet.py     # rebuild answer_key.json from the PDFs
& $py kb_selftest.py     # 25 mechanical checks against the MD
& $py trap_recheck.py    # 22 structural checks on the known traps
& $py consistency.py     # 13 documentation-drift checks
& $py tracing.py         # wire-tracing soundness
& $py score.py           # scored round-1 benchmark

cd ..\Manroland_KnowledgeBase\pipeline
& $py qa\qa_final.py           # 17 acceptance checks
& $py qa\qa_fidelity_full.py   # every label of every sheet
& $py qa\qa_links.py           # every internal link
```

`pipeline/build.py` now runs `sync_docs.py` last, so regenerating the knowledge base
automatically refreshes the measured figures quoted in the prose docs.

---

## 8. Honest limits of this test

- **26 + 6 questions is a sample.** Chosen to cover each capability tier and to
  include known traps — not statistically representative of every possible question.
- **One model family.** A weaker model scores lower, a stronger one higher. The KB
  is model-agnostic; the *percentage* is not.
- **Adjudication was by the Lead**, with every disputed claim re-verified against the
  PDF. The rubric was fixed before answers were read; four round-1 scores were
  revised upward after verification.
- **Round 2 used a single agent on 6 questions.** It re-tests the known-hard cases,
  not the whole set.
- **The benchmark measures retrieval and honesty**, not engineering judgement. The KB
  cannot tell an engineer whether a design is safe — and it says so explicitly.
