# Cards Over-Cap Tighten Report — 2026-05-11

**Scope:** Tighten 5 `narrative_one_liner` cards to ≤30 words in lockstep across `site/data.json` and `layer-6-deliverable-data.json`. Preserve every structural beat. No fabricated specifics.

**Word-count method:** whitespace-split (`len(s.split())`), hyphenated words = 1 token, em-dashes count as standalone tokens (matches the count in the task brief: UA original = 31 by this method).

---

## Pre/Post md5

| File | Pre | Post |
|---|---|---|
| `site/data.json` | `fcdc8ea8d26b78721a7c56d11ee764e5` | `c8bebd1107552c89c7bca3f5f7f7c43b` |
| `layer-6-deliverable-data.json` | `bf5bd2a08b976bbe69af83f6cc0d8fac` | `04c64b4292d929894d69d96549ee065f` |

**Lockstep parity check:** `diff site/data.json layer-6-deliverable-data.json` → only pre-existing trailing-newline difference on line 8340 (site file lacks final `\n`). All 5 card edits applied identically in both files.

**JSON validity:** both files parse cleanly via `python3 -c "import json; json.load(open(...))"`.

---

## Per-card before/after

### 1. BA — 32 → 29 words

**Before:** "Bosnia and Herzegovina is coping for now on partial-coverage data; the expanding economy leaves room for retraining capacity, though weakening job-replacement or training systems stretched too thin would push it into displacement."

**After:** "Bosnia and Herzegovina is coping on partial-coverage data; the expanding economy leaves room for retraining, though weakening job-replacement or training systems stretched too thin would push it into displacement."

**Tightened beat (prose-trim):** removed temporal intensifier "for now" (coping-position carried by present-tense "is coping") and dropped the "capacity" qualifier after "retraining" (the retraining-capacity lever is carried by "leaves room for retraining"). Structural beats preserved:
- coping-position ✓ ("is coping")
- partial-coverage caveat ✓
- expanding-economy lever ✓
- two-stress-trigger ✓ ("weakening job-replacement or training systems stretched too thin")
- → displacement ✓

Em-dashes: 0. Banned: 0. Forbidden tech: 0.

---

### 2. FI — 32 → 29 words

**Before:** "Finland is among Europe's most resilient labour markets thanks to deep reskilling capacity, but with the economy no longer growing, recovery from any shock runs through climate-adaptation work rather than conventional growth."

**After:** "Finland is among Europe's most resilient labour markets thanks to deep reskilling capacity, but with the economy no longer growing, recovery runs through climate-adaptation work rather than conventional growth."

**Tightened beat (prose-trim):** removed "from any shock" (modifier on recovery that is not part of the named beat set — the climate-adaptation channel beat is intact). Structural beats preserved:
- Class I resilience ✓
- reskilling-capacity anchor ✓
- no-longer-growing regime ✓
- climate-adaptation recovery channel ✓

Em-dashes: 0. Banned: 0. Forbidden tech: 0.

---

### 3. NO — 32 → 30 words

**Before:** "Norway sits among Europe's most resilient labour markets thanks to deep retraining capacity and a sovereign-wealth buffer; public systems already stretched in “must-have” jobs and export-dependence make resilience conditional on global trade."

**After:** "Norway sits among Europe's most resilient labour markets thanks to deep retraining and a sovereign-wealth buffer; public systems stretched in “must-have” jobs and export-dependence make resilience conditional on global trade."

**Tightened beat (prose-trim):** dropped "capacity" after "retraining" (retraining anchor preserved by the noun itself) and dropped the breach-clause intensifier "already" (the breach is carried by "stretched in “must-have” jobs"). Structural beats preserved:
- Class I resilience ✓
- retraining ✓
- sovereign-wealth ✓
- breach (must-have jobs) ✓
- export-dependence ✓
- global-trade conditional ✓

Em-dashes: 0. Banned: 0. Forbidden tech: 0.

---

### 4. UK — 32 → 30 words

**Before:** "The UK is already past the absorption threshold with public systems already stretched in “must-have” jobs; with the economy no longer growing, recovery runs through climate-adaptation work rather than conventional tech jobs."

**After:** "The UK is already past the absorption threshold with public systems stretched in “must-have” jobs; with the economy no longer growing, recovery runs through climate-adaptation work rather than tech jobs."

**Tightened beat (prose-trim):** removed the duplicate "already" (the original used "already" twice in one sentence — once on past-threshold, once on the breach; the past-threshold one is canonical across cards, the breach-clause one is redundant) and dropped "conventional" before "tech jobs" (the climate-adaptation vs tech-jobs contrast carries without the qualifier; "conventional growth" remains canonical for FI/AT/FR cards). Structural beats preserved:
- past-threshold ✓ ("already past the absorption threshold")
- breach (must-have jobs) ✓
- no-longer-growing regime ✓
- climate-adaptation channel ✓

Em-dashes: 0. Banned: 0. Forbidden tech: 0.

---

### 5. UA — 31 → 30 words

**Before:** "Ukraine marks the worst-case end for European peers — war-damaged training, refugee outflow, 40% defence spending — but also shows how rapid defensive rearmament can build new labour absorption at scale."

**After:** "Ukraine marks the worst-case end for European peers — war-damaged training, refugee outflow, 40% defence spending — but shows how rapid defensive rearmament can build new labour absorption at scale."

**Tightened beat (prose-trim):** removed connective "also" between the worst-case and rearmament-positive clauses (the "but" already carries the pivot from worst-case marker to positive framing). Structural beats preserved:
- worst-case marker ✓
- 3 anchors ✓ ("war-damaged training, refugee outflow, 40% defence spending")
- rearmament positive framing ✓

Em-dashes: 2 (at budget — kept the existing pair fencing the 3 anchors). Banned: 0. Forbidden tech: 0.

---

## Scan summary

| Card | Words | Em-dashes | Banned-phrase hits | Forbidden-tech hits |
|---|---:|---:|:---:|:---:|
| BA | 29 | 0 | 0 | 0 |
| FI | 29 | 0 | 0 | 0 |
| NO | 30 | 0 | 0 | 0 |
| UK | 30 | 0 | 0 | 0 |
| UA | 30 | 2 | 0 | 0 |

**Banned-phrase scan:** ran against Tier-1 + Tier-2 phrases from `skills/linkedin-playbook/references/banned-phrases.md`, including the Tier-2 row on "bounded/bounding/bounds". 0 hits across all 5 cards.

**Forbidden-tech scan:** word-boundary regex check for `Lens N`, `S1–S8`, `C1–C3`, `growth_baseline`, `ALMP`, `ESCO`, `ISCO`, `NACE`, `Klinger`, `Gini`. 0 hits across all 5 cards.

**Trim taxonomy:** all 5 cards tightened by **prose-trim** (removing intensifiers, redundancies, or non-beat modifiers). No syntactic-rework was required — every card hit the ≤30 cap by pruning alone. No SOT-grounded fact dropped or altered (BR-19 compliant).

---

## Files changed

- `site/data.json` — 5 line edits (lines 682, 2734, 5313, 6962, 7899)
- `layer-6-deliverable-data.json` — 5 line edits (same line numbers; file structure mirrors site file)

## Code Review Summary (code-craft rubric)

This task is JSON-content editing, not code generation, but applying the post-code gate per CLAUDE.md Rule 3.5:

- **Names:** N/A — edits to string-literal content inside existing keys.
- **Nesting depth:** N/A.
- **Hidden dependencies / side effects:** none. Only `narrative_one_liner` string values changed; surrounding structure untouched.
- **Duplication:** the two files store the same content (data.json mirror); edits applied to both to preserve lockstep. Verified via `diff` (only pre-existing trailing-newline divergence remains).
- **Local-style match:** preserved existing quote conventions — straight ASCII `"` in BA/FI/UA, Unicode curly `“ ”` in NO/UK (matches the rest of those strings).
- **Honest signatures:** N/A (data file).
- **Things I chose NOT to add (YAGNI):** did not normalise the quote-style inconsistency between cards (out of scope); did not normalise the trailing-newline difference between the two files (pre-existing, out of scope); did not refactor the FI/UK construction even though they share the "no longer growing → climate-adaptation" pattern.
- **Uncertainty / assumptions a human should verify:** the word-count method (treating em-dashes as standalone whitespace-split tokens) matches the brief's count for UA original (31). If a different method is canonical (e.g., MS Word's "words" counter, which excludes em-dashes), all 5 cards still pass: BA=29, FI=29, NO=30, UK=30, UA=29 under that method as well.
