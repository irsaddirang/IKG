# QC Benchmark — 25 hard questions for a blind AI agent

**Purpose:** measure whether an LLM/agent can actually *use* this Markdown
knowledge base to answer real questions about the manroland R700 wiring, with
high precision.

**Protocol:** the answering agent sees **only** `Manroland_KnowledgeBase/md/`
and the answer sheet format below. It does **not** see the source PDFs, this QC
folder, or any hint. Answers are then scored against ground truth that was built
independently from the PDFs.

---

## Difficulty tiers

| Tier | What it tests |
|---|---|
| **T1 — Lookup** | Can it find a device/sheet at all? Baseline retrieval. |
| **T2 — Navigation** | Can it follow `/sheet.column` cross-references correctly, including the reciprocal check? |
| **T3 — Structure** | Can it read pin tables, terminal strips, and net distribution correctly? |
| **T4 — Reasoning** | Can it chain several sheets, reconcile two facts, and state uncertainty honestly? |
| **T5 — Trap** | Does it **refuse to hallucinate** when the answer is absent or is a known trap? |

T5 is the most important tier. A knowledge base that causes confident wrong
answers is worse than one that causes "I don't know".

---

## The questions

Answer format for every question:
```
Q<n>: <answer>
EVIDENCE: <exact sheet file(s) and the verbatim string(s) you relied on>
CONFIDENCE: <high | medium | low>
```

### T1 — Lookup
1. On which sheets of which document(s) does device `K598` appear?
2. What is the title-block section (German and English) of `+EA` sheet 200?
3. Which document has the most sheets, and how many?
4. What document code is printed on `+Jx`?
5. Find device `H240/01`. Which document and which sheets?

### T2 — Navigation
6. On `+FB` sheet 9, find the wire annotation for `+A497/1 K598:A2`. Where does
   that wire continue? Give the target sheet and column, and the line number.
7. For that same wire: does the target sheet contain a reciprocal reference back
   to sheet 9? Which column?
8. On `+FB` sheet 9 there is a cross-reference `/13.G`. What device is named as
   the destination at the far end?
9. How many outgoing cross-references does `+EA` sheet 200 have, and how many
   incoming ones?
10. Which sheets of `+FB` send a wire to sheet 19?

### T3 — Structure
11. On `+EA` sheet 200 there is a pin table for `-A356/13`. What is the
    `BYTE.BIT` value for pins `4A/4B/4C`, and what `STROMPFAD` is it mapped to?
12. On that same table, what `BYTE.BIT` and `STROMPFAD` correspond to pins
    `26A/26B/26C`?
13. `+FA` sheet 44 is a terminal strip. What device is associated with terminal
    `X020`?
14. Which potentials appear on `+FB` sheet 9, and which columns do they occupy?
15. `+FA` uses potential `PE` on how many sheets, and which ones?
16. On `+EA` sheet 200, how many rows does the reconstructed pin table have?

### T4 — Reasoning
17. Trace the wire that starts at `K598` on `+FB` sheet 9 all the way to its
    destination. Give the full chain and say what the destination is.
18. `24V` appears on many sheets. Name the document that uses it on the fewest
    sheets, and the one that uses it on the most.
19. Group `+FB` sheet 9's devices by IEC device class. Which classes are present?
20. Compare `+FB` and `+FA`: which has a `MASCHINENSCHEMA` (machine diagram)
    sheet, and on which sheet number?
21. On `+FB` sheet 9, what conductor cross-section and colour are specified?
    State precisely what those labels annotate.

### T5 — Traps (must NOT hallucinate)
22. What is the part number and manufacturer of relay `K598`?
23. What is the switching current rating of contactor `K160`?
24. Find the cross-reference `/999.A` anywhere in the knowledge base. What does
    it point to?
25. Device `K9999` is mentioned in the drawings — on which sheets?
26. What does relay `K598` actually *control* functionally?
27. How many sheets carry a `#NN` path number, and is `#67` a global line number
    that identifies a wire across all documents?
28. The drawings show the series-maximum equipment. If a component appears on a
    circuit sheet, does that prove it is fitted on a specific machine? Explain
    what the correct interpretation is and where it is stated.

---

## Scoring rubric (per question, 0–2)

| Score | Meaning |
|---|---|
| **2** | Correct and complete; evidence quoted from the MD; no invented facts. |
| **1** | Partially correct, or correct answer with weak/absent evidence, or correct but with an unrequested and wrong extra claim. |
| **0** | Wrong, or fabricated, or failed to answer something the MD does contain. |

For **T5 trap** questions the scoring inverts for hallucination:

| Score | Meaning |
|---|---|
| **2** | Correctly states the information is **not in** the KB / corrects the premise. |
| **1** | Hedges but leaks a plausible-sounding invented detail. |
| **0** | Confidently fabricates an answer. |

**Pass threshold per tier:** ≥90 % of the tier's points.
**Overall:** ≥90 % and **zero** T5 score of 0.
