# Handover Prompt — Country Card Plain-Language Rewrite

Bounded composition session. Rewrites the per-country `narrative_one_liner` field in `site/data.json` and `layer-6-deliverable-data.json` for all 37 countries (36 + Ukraine reference panel). **Tight one-liner per country**, plain language, where/what/lever framing, no technical terms. **Output mode: SOT edit on two specific fields per country; no schema extension, no render code changes.** ~3 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** Mostly composition + JSON editing; code-craft applies to any inline grep/diff snippets and to the JSON edit discipline (preserve field order, don't break JSON).

---

## Research scope

**Corpus-only.** All content derives from existing SOT (`layer-6-deliverable-data.json`) plus per-country mechanism descriptions in `site/scenarios.html` + corridor/class definitions in `site/methodology.html`. No external WebSearch.

---

## Context

The corridor-map cards on `site/findings.html` currently render the per-country `narrative_one_liner` field from `data.json`. Current content is analyst shorthand — example:

> **Bulgaria · BG** — Class II / Corridor C2 / growth baseline
> *"Growth-baseline C2 reaching C3 only under S6/S7 stress; aggregate."*

For Phil's advisory audience (Cembra-class boards, policy desks, executive search), this notation is opaque. The chips (Class II / Corridor C2 / growth baseline) already carry the technical encoding. The narrative line should give a **plain-language one-liner** that says **where the country sits + what it means + what could shift it (lever)**.

**Style discipline** (Phil-locked 2026-05-09):

- **One sentence per country** — tight, single line on the card
- **Plain language only** — no technical terms; specifically: no Klinger references, no Gini values, no Lens N codes (Lens 1, Lens 5, etc.), no scenario codes (S1, S6, S7, S8), no corridor codes (C1, C2, C3), no regime codes (growth_baseline, secular_stagnation_warning, post_growth_empirical), no acronyms (ALMP, ESCO, ISCO, NACE, etc.)
- **Where / what / lever framing** — three implicit beats: where the country sits (current position), what that means (consequence in plain language), what could shift it (the lever — what would make things better or worse)
- **Voice register** — matches the rest of the synthesis site: plain conversational, no marketing-speak, no flattery
- **Banned-phrase scan applies** — `skills/linkedin-playbook/references/banned-phrases.md` Tier 1/2/3 plus the broader 25–80 word AI-tell vocabulary per `skills/layer-site-architecture/SKILL.md` L3 (delve, tapestry, leverage, synergy, optimise, streamline, empower, paradigm, robust [unless as a class name], crucially, navigate, harness, unleash, seamless, cutting-edge, elevate, vibrant, pivotal, showcasing, boasts, stands as, ever-evolving, multifaceted, nuanced, holistic)

---

## START PROMPT

Rewrite the per-country `narrative_one_liner` field for all 37 country entries in both `site/data.json` and `layer-6-deliverable-data.json` to plain-language one-liners. Where/what/lever framing. No technical terms. Output two files (both updated) + a report showing all 37 rewrites for Phil-lock.

### Read FIRST (absolute paths)

**Source-of-truth + mirror:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — canonical SOT
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — site-render mirror (must update in lockstep)

**Context for the rewrites (per-country mechanism + classification):**
- Each country block in `layer-6-deliverable-data.json` carries: `fragility_class`, `corridor`, `regime`, `narrative_one_liner` (current), `scenario_distribution_language`, `regime_implications_note`, plus per-country mechanism notes for scenarios where applicable
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — plain-language scenario descriptions (use these to translate S1–S8 into plain narrative)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — corridor + fragility class definitions in plain language

**Voice register reference:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — current locked voice register (recently-edited Italy block, Conclusion, lede are good register reference)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` — overview-page SMs (recent tighter locks)
- `/Users/philippmaul/Documents/second-brain/skills/layer-site-architecture/SKILL.md` — L1–L5 voice/register patterns
- `/Users/philippmaul/Documents/second-brain/skills/linkedin-playbook/references/banned-phrases.md` — Tier 1/2/3 + em-dash discipline

### The rewrite specification

For each of the 37 countries, the new `narrative_one_liner` should be **one sentence** (max ~30 words) covering:

1. **Where** — the country's current position in plain terms (coping / partial absorption / already past the threshold / institutional collapse)
2. **What** — what that position means for workers and labour markets in this country (the consequence)
3. **Lever** — what could shift the placement (the policy/economic/demographic factor that could improve or worsen the outcome)

Three implicit beats can be folded into a single fluent sentence. Don't enumerate them as "where: X, what: Y, lever: Z" — write naturally.

#### Example: Bulgaria

- **Current `narrative_one_liner`**: *"Growth-baseline C2 reaching C3 only under S6/S7 stress; aggregate."*
- **Plain-language target**: *"Bulgaria is coping for now, but a weakening of the historical job-replacement pattern or stretched institutional bandwidth could push it into displacement; its expanding economy gives it room to add reskilling capacity if it chooses."*

#### Example: Germany

- **Current**: *"Post-growth + S2-dependent: optimism path runs through climate Zone-C wage premium; S7 cascade reaches C3."*
- **Plain-language target**: *"Germany's traditional job-replacement story is structurally weaker because the economy has stopped growing, so the most plausible recovery path runs through climate-adaptation work rather than conventional tech jobs."*

#### Example: Norway (Class I)

- **Plain-language target**: *"Norway sits among the most resilient European labour markets thanks to deep ALMP capacity and sovereign-wealth buffer, but its trade-decoupling exposure means resilience is conditional on continued global integration."* (note: "ALMP" and "sovereign-wealth" are mild jargon — sub-session can choose plainer wording: "active labour-market policy" and "national savings fund" or similar)

#### Example: Ukraine (Class IV reference)

- **Plain-language target**: *"Ukraine sits as a reference case for institutional collapse already underway: war-damaged training infrastructure, refugee outflow, and 40% defence-spending share mean its labour market is at the upper bound of what European peers could face under worst-case conditions."*

### Per-country reference data

For each country, before writing, surface (in your scratchpad):

- Country code + name
- Fragility class (Class I / II / III / IV — translate to plain: "robust under stress," "fragile under stress," "already in displacement," "institutional collapse")
- Corridor (C1 / C2 / C3 — translate: "coping," "partial absorption," "displacement-without-absorption")
- Regime (growth-baseline / secular-stagnation-warning / post-growth-empirical — translate: "expanding economy," "stagnation warning," "no longer growing in the conventional sense")
- Per-country mechanism specifics (scenarios where the country reaches different corridors; specific country flags like squeeze, breach, candidate-partial-coverage, s2_dependent)

The resulting one-liner SHOULD reflect these specifics in plain language. The country shouldn't be generic — it should be specifically about Norway / Germany / Bulgaria etc.

### Edge cases

- **Class IV countries (MK, RS, TR, UA reference)**: institutional collapse framing per the recent Phil-locked term "Currently Failing." Each has different mechanism (MK + RS: high polycrisis + EU candidate status; TR: Climate-Adaptation-Boom-dependent + Class IV; UA: war-damaged + reference panel).
- **s2_dependent countries (AT, LU, TR)**: optimism path only runs through climate work, not tech.
- **Squeeze cluster (BE, DE, DK, FI, FR, NL, NO, SE — 8 worker-protection economies)**: dual mechanism. Nordic sub-cluster carries trade-decoupling exposure; Continental sub-cluster carries UK-adjacency + capital-flight risk.
- **Candidate-partial-coverage (BA, MK, RS, TR)**: data-coverage caveat — note carefully but don't make the candidate-status the lede.
- **UK**: standalone (post-EU). Carries Mode-1 weak-protection adjacency role for the Continental squeeze cluster.

### Discipline

- **Banned-phrase scan on every rewrite.** Tier 1/2/3 reference + the 25–80 word AI-tell vocab in `skills/layer-site-architecture/SKILL.md` L3. Particular attention to: em-dash overuse (≤2 per one-liner is fine); avoid the "It's not X — it's Y" / "not just X but Y" formulas; avoid "structurally" / "load-bearing" / "the analysis is built to surface"; avoid colon-fragment openers ("Reality:", "The truth:", etc.).
- **No technical terms in output.** Specifically forbidden: Lens N codes, S1–S8, C1–C3, growth_baseline / secular_stagnation / post_growth_empirical, ESCO, ISCO, NACE, Klinger, Gini, Autor 2024, El-Sahli, Dell'Acqua, Cedefop unless integral to the explanation, ALMP (translate to "active labour-market policy" or simpler), reinstatement (use "job-replacement" or "old-jobs-disappear-new-jobs-appear" mechanism), specific scenario names (S2 Climate Adaptation Boom → "climate-adaptation work"; S6 Reinstatement Failure → "historical job-replacement pattern weakening"; S7 Bandwidth Fracture → "institutions getting stretched too thin").
- **BR-19 fabrication discipline** — every per-country claim must trace to a field in `layer-6-deliverable-data.json` for that country. Don't invent country specifics. If you can't find the mechanism for a country in SOT, flag and skip rather than guess.
- **JSON discipline** — preserve field order; don't break JSON syntax; do not change other fields; the only edit per country is the `narrative_one_liner` string value. Pre-flight: md5 the file. Post-flight: parse-validate the JSON; md5 to confirm only the targeted lines changed.
- **Lockstep both files** — every change in `layer-6-deliverable-data.json` must mirror in `site/data.json` and vice versa. Discrepancy = bug. md5 should change on both files; field counts should match.

### Verification (before reporting back)

1. **Both JSONs parse as valid JSON.** Use `python3 -c "import json; json.load(open('site/data.json'))"` and same for `layer-6-deliverable-data.json`.
2. **37 country entries rewritten** in each file. Field count match.
3. **Banned-phrase grep** across the 37 new one-liners returns 0 hits (Tier 1/2/3 + 25-word AI-tell vocab).
4. **No forbidden technical terms** across the 37 new one-liners (grep for `Lens 1`, `Lens 5`, `S2`, `S6`, `S7`, `S8`, `C1`, `C2`, `C3`, `growth_baseline`, `secular_stagnation`, `post_growth_empirical`, `Klinger`, `Gini`, `ALMP`, `ESCO`, `ISCO`, `NACE` — 0 hits expected).
5. **md5 verification** — only the targeted `narrative_one_liner` lines changed in each file; other SOT fields untouched.
6. **Render check** — open `site/findings.html` corridor map view in preview; click 3-5 countries (DE, NO, BG, MK, IT); confirm cards render new plain-language strings; no rendering errors.

### Report-back format

Single markdown file: `cards-plain-language-rewrite-report-2026-05-09.md`. Same directory.

1. **TL;DR** — 5-7 bullets: total countries rewritten, before/after sample, banned-phrase scan result, JSON validity, render check pass/fail
2. **Per-country table** — 37 rows: `code | country | new narrative_one_liner` for Phil-lock review
3. **Mechanism-fidelity flags** — countries where the original SOT mechanism was ambiguous or thin; rewrites flagged for Phil-verification
4. **Banned-phrase scan results** — clean or hit list
5. **JSON validation + md5** — pre-/post audit
6. **Phil-iteration handoff** — flag 3-5 countries you're least sure about (mechanism clarity, voice fit, length)
7. **Brain capture candidates** (if any) — likely none; this is composition not pattern-discovery

---

## Out of scope

- Schema changes (no new fields)
- Render code changes in `findings.html` (the existing `showDetail()` function continues to render `narrative_one_liner`)
- Multi-sentence cards (one-liner only per Phil's lock)
- Other SOT fields (do not edit `scenario_distribution_language`, `regime_implications_note`, etc.)
- Card UI redesign (chips, layout, hover state — all unchanged)
- Brain skill enrichment — surface capture candidates only; do not auto-write

---

*This brief is the dispatch prompt for the cards plain-language rewrite. Sub-session reads each country's mechanism context, writes a tight plain-language one-liner per country, edits both JSON files in lockstep, verifies, reports the 37 rewrites for Phil-lock. ~3 h. Output: updated `site/data.json` + `layer-6-deliverable-data.json` + report.*
