# Handover Prompt — Scenarios Page Editorial Iteration

Bounded editorial session. 9 distinct edits on `site/scenarios.html`. Includes a **math error fix** (current page shows S1+S3 combined probability as 25%→5%; SOT shows correct 20%→13%). All copy is Phil-locked verbatim from the message of 2026-05-09. **Output mode: surgical text edits + 1 numeric correction.** No schema/data/SOT changes. ~2–3 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** This is editorial; code-craft applies only to inline grep/diff snippets.

---

## Research scope

**Corpus-only.** All Phil-locked copy is in this brief verbatim. SOT verifications for the math fix + speed-gap explanation come from `site/data.json` (lines 7206, 7217, 7220 for the speed-gap derivation; `scenarios.S1.probability_per_regime` + `scenarios.S3.probability_per_regime` for the math).

---

## Context

`site/scenarios.html` carries the 8-scenario page. Phil's 2026-05-09 review surfaced 9 distinct edits:

1. Page hero + subheader rewrite
2. §1 (Spectrum) heading change
3. Polycrisis Drag text rewrite (S8 block)
4. **Math error fix** — page currently says S1+S3 combined goes from "25% to 5%"; SOT confirms correct is **20% to 13%**. Two locations affected (the SM 2 support text + the weather-cluster note).
5. S4 reskilling-capacity gap text rewrite
6. S4 optimism path text rewrite
7. S5 capability-floor breach text rewrite
8. Four small "normal text size" replacements (weather-pattern intro + trajectory chart caption + CI explanation + squeeze-flag note)
9. **Question to verify and surface to readers**: the math behind the "AI-vs-system speed gap runs 5–9 years" claim — should be clarified in plain language somewhere on the page.

---

## START PROMPT

Execute the 9 edits below on `site/scenarios.html`. All copy verbatim from this brief; do not author or paraphrase. Math fix has explicit before/after numbers. Speed-gap explanation must be added (anchor text provided). Verify md5 on `site/data.json` + `layer-6-deliverable-data.json` is unchanged at close.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — target file
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` lines 7206, 7217, 7220 — speed-gap SOT
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` `scenarios.S1.probability_per_regime` + `scenarios.S3.probability_per_regime` — math fix SOT verification

**Voice / discipline reference:**
- `skills/linkedin-playbook/references/banned-phrases.md` — Tier 1/2/3 scan
- `skills/layer-site-architecture/SKILL.md` — L1–L5 voice register

### The 9 edits

#### Edit 1 — Page hero (h1) + subheader (lede)

**New h1:**
> *Eight storylines for the next decade, with the odds shaped by each country's economic regime.*

**New lede (page subheader):**
> *An optimism-pessimism spectrum from full reinstatement to a parallel-cascade collapse, three economic regimes that change which future is most likely, and the country-level trajectories underneath.*

Find current h1 + lede on scenarios.html and replace.

#### Edit 2 — §1 Spectrum heading

**New §1 lead:**
> *How the next decade plays out for European labour markets isn't one question, it's at least eight.*

Replace whatever currently leads §1.

#### Edit 3 — Polycrisis Drag (S8) text

**New text — replace the existing S8 prose block verbatim:**

> S8 Polycrisis Drag is a "pick-your-poison" parallel-cascade pattern, not a point on the routine spectrum. War and defence spending, budget stress, climate adaptation costs, global decoupling, political turmoil, social division, and Ukraine reconstruction combine to overwhelm institutional capacity at the same time. It is carried as a conditional that can be triggered on top of any routine variant, not folded into the spectrum.
>
> This combination has no analogue in the 580 years of historical disruptions reviewed earlier in this analysis project (link to part 3). There is no clean historical case base to ground these joint dynamics. That is why it is treated as a conditional "parallel risk," rather than as the worst point on the routine spectrum.

Note: "link to part 3" should be a real hyperlink to the Disruptions sister site (`https://disruptions.nexalps.com/`) or wherever the 580-year corpus lives. Sub-session resolves the target URL.

#### Edit 4 — MATH ERROR FIX (two locations)

**Current** (page line 282 SM 2 support + page line 341 weather-cluster note):
> "the standard tech-led recovery path drops from about **25%** probability to about **5%**"
> "Their combined probability under growth is around 25%; under post-growth, around 5%."

**Correct math per SOT** (`site/data.json`):
- S1 growth-baseline central: 0.10; S3 growth-baseline central: 0.10 → combined **20%**
- S1 post-growth-empirical central: 0.05; S3 post-growth-empirical central: 0.08 → combined **13%**

**New text — replace both locations:**
- SM 2 support sentence: *"In post-growth, the standard tech-led recovery path drops from about **20%** probability to about **13%**, while **Climate Adaptation Boom** rises from about **22%** to about **30%**. Same menu of futures; different odds."*
- Weather-cluster note: *"Note: 'tech-led recovery' here refers to **S1 Reinstatement Revival + S3 Jobs Transform**, both tech-led optimistic scenarios. Their combined probability under growth is around 20%; under post-growth, around 13%."*

Pre-flight grep to verify the original "25%" + "5%" combo still in page:
```
grep -n "25%.*probability to about.*5%\|combined probability under growth is around 25" site/scenarios.html
```

Post-flight grep should return 0 hits.

#### Edit 5 — S4 reskilling-capacity gap text

**New text — replace whatever S4 reskilling-capacity prose currently exists:**

> ### The reskilling-capacity gap
>
> Europe needs to retrain about **7.55 million** people by 2035 due to AI effects. At first glance, the basic annual training throughput of ~3.34 M makes that seem doable. But after subtracting statistical retraining churn (~2.89 M), there is only room to retrain about **450,000 extra people per year**. At that pace, the 7.55 M cohort would take roughly **15 years** to clear. That is far slower than how quickly AI could change jobs, and it does not even count the training already needed for normal job turnover.
>
> This anchors the pessimism side and serves as the quantitative spine of the 15-country Class III diagnosis. Even allocating disproportionately to Class III would absorb only a marginal share of the deficit without channel expansion.

#### Edit 6 — S4 optimism path text

**New text — replace whatever S4 optimism-path text currently exists:**

> ### The optimism path narrows to climate Zone-C
>
> For three countries — **Austria, Luxembourg, Turkey** — the only realistic "good outcome" left in the model is the "Climate Adaptation Boom" scenario where lots of new work comes from climate adaptation. The usual "tech boom brings jobs back" path does not work for them. All six other routine variants produce a corridor 2 or 3 outcome. Anchored on Cedefop 2025 country-level employment projections plus the EU Net-Zero Industry Act €100 B clean-manufacturing envelope.

#### Edit 7 — S5 capability-floor breach text

**New text — replace the S5 capability-floor description:**

> 12 countries breach the institutional adaptive-capacity floor at the 2-digit ESCO level. This result should be read as a conservative estimate at this level of aggregation. Finer-grained data would likely surface 1–2 more.
>
> A capability-floor breach means the country's institutions cannot routinely absorb the kind of labour-market shocks the scenarios describe.

#### Edit 8 — Four small "normal text size" texts

Sub-session locates the four sentences currently rendered in some emphasised / non-normal-body style (italic, sub-text, etc.) and replaces them with these versions in normal body style:

**Weather-pattern intro (currently around S2 weather-cluster intro):**
> Two countries can face the same AI "story," but if one economy is growing and the other is stuck or shrinking, the same shock will land differently. That is why the project groups countries into three "weather patterns" (growth, stagnation, post-growth) to adjust which futures are more likely.

**Trajectory chart caption (around the country-trajectory chart):**
> Each line on the chart shows how one country moves from its 2026 starting "corridor" (how safe or stressed its labour market is) to where it ends up in 2035 under a specific scenario, with upward bends meaning improvement and downward bends meaning getting worse.

**Confidence-interval explanation:**
> These probabilities are our best estimate of how likely each scenario is, given the country's economic regime. The "80% confidence interval (CI)" is the range where we think the true probability likely falls 8 out of 10 times.

**Squeeze-flag note (around S6 or S7 where squeeze cluster is referenced):**
> The squeeze flag is a capital-flight signal, not a labour-displacement signal. The risk is that AI investment leaves rather than that workers are displaced at home. Quantification rests on per-country counts of approximately 40 high-risk EU AI Act Annex III deployer occupations and approximately 29 Product Liability Directive post-market duty occupations. Two distinct mechanisms warrant two distinct mitigations.

Sub-session locates each of the four spots, swaps text, and ensures CSS/HTML class on the surrounding element drops back to normal body styling (drop `.section-sub`, `.italic`, `.note`, or whatever emphasis class was applied; render as standard `<p>`).

#### Edit 9 — 5–9 year speed gap explanation (add)

Phil flagged: *"whats the math behind '...the AI-vs-system speed gap runs 5–9 years.'?"* — readers see "5–9 years" without explanation.

**SOT derivation** (from `site/data.json` lines 7217, 7220):
- AI disrupts in 1–3 years (per OpenAI / Anthropic productivity RCT evidence; admin clerks / customer service / writers / translators hit fastest)
- European VET (vocational education and training) + university systems take 5–9 years to retool curricula + spin up new tracks
- Difference = the gap

**Plain-language addition — sub-session decides best placement (likely near where 5–9 years currently appears):**

> The 5–9 year figure is how long European vocational training and university systems take to respond to a major shift — to retool curricula, accredit new programmes, and run cohorts through to graduation. AI disrupts the affected jobs in 1–3 years (per the productivity studies in section 4). That difference — 3–5 years where the displacement is in progress but the training response is still being built — is the structural problem.

### Discipline

- **All copy verbatim from this brief.** Do not author or paraphrase. The math fix has explicit numbers (20% / 13%); do not invent.
- **Banned-phrase scan on all new copy.** Tier 1/2/3 reference: `skills/linkedin-playbook/references/banned-phrases.md` + broader 25–80 word AI-tell vocab per `skills/layer-site-architecture/SKILL.md` L3.
- **BR-19 fabrication discipline** — the 580-year disruptions claim, the 7.55M / 3.34M / 2.89M / 450K numerics, the 12-country capability-floor breach, the 40 + 29 occupation counts: all are SOT-anchored. Verify against `site/data.json` if uncertain. The Polycrisis Drag mechanism components (war/defence, budget, climate, decoupling, political turmoil, social division, Ukraine reconstruction) are also SOT-anchored.
- **No SOT edits.** `site/data.json` + `layer-6-deliverable-data.json` md5-verified pre/post. All edits are page-side only.
- **md5 audit** on `site/scenarios.html` changes pre/post.

### Verification (before reporting back)

1. **md5 on data files** — `site/data.json` + `layer-6-deliverable-data.json` UNCHANGED.
2. **Hero + lede landed** verbatim from this brief.
3. **§1 spectrum heading landed** verbatim.
4. **Polycrisis Drag block landed** verbatim with the part-3 hyperlink resolved.
5. **Math fix** — grep for "25%.*probability to about.*5%" returns 0 hits; grep for "20%" + "13%" finds the new locations.
6. **S4 reskilling + optimism + S5 capability-floor blocks** landed verbatim.
7. **Four "normal text size" sentences landed** in normal body styling (no italic / sub-text class).
8. **5–9 year explanation added** near the existing 5–9 reference, in plain language.
9. **Banned-phrase grep across all new copy** returns 0 hits.
10. **Visual preview check** — render scenarios.html via preview; spot-check the 9 edits visually.

### Report-back format

Single markdown file: `scenarios-page-iteration-report-2026-05-09.md`. Same directory.

1. **TL;DR** — 9 bullets, one per edit, with file:line pointer for each
2. **Math fix audit** — before/after grep result + SOT verification check
3. **Verification checklist (1–10)** — pass/fail per item
4. **Phil-iteration handoff** — flag 2–3 things you're least sure about (Polycrisis Drag link target, placement of 5–9 explanation, the four "normal text size" sentence locations)
5. **Brain capture candidates** (if any) — likely none beyond what surfaced in prior iteration rounds

---

## Out of scope

- SOT edits (data.json / layer-6-deliverable-data.json — read-only)
- Other pages (findings, europe, methodology, sources, glossary)
- Long-read PDF regeneration
- Italy / Conclusion propagation to deliverable docs (held for separate cleanup pass)
- Card narrative_one_liner rewrite (held — running as separate sub-session)

---

*This brief is the dispatch prompt for the scenarios-page editorial iteration. Sub-session executes the 9 edits verbatim, verifies math fix against SOT, verifies copy / discipline / md5, reports back. ~2–3 h.*
