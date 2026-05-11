# Handover Prompt — Bundle A: L3 v0.2 Quality Fixes + L1 CSS Regression (2026-04-29)

Self-contained prompt for a fresh session. Does not require prior conversation context.

---

## START PROMPT

I need you to fix 7 quality issues in the European AI Labour Market suite identified during Phil's manual inspection of the 2026-04-29 fix session. 6 issues are in L3 (european-disruptions-map); 1 is a CSS regression in L1 (european-ai-exposure-map) introduced by the Gostev panel addition. Bundle A backlog at `projects/european-ai-labour-synthesis/bundle-a-l3-fixes-handover-2026-04-29.md` (this file).

Before starting, read the L6 spec at `projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — do NOT modify it. Note the locked decisions block and the orthogonality finding section.

Repos:
- L3: `/Users/philippmaul/Documents/projects/european-disruptions-map/`
- L1: `/Users/philippmaul/Documents/projects/european-ai-exposure-map/`

Both are public live sites on Netlify. Test before deploy. Phil does all `git commit` + `git push`.

### Issue 1 (P0, ~1–2 days) — L3 v0.2: Populate medium-feasibility cases with actual values + uncertainty bands

**Repo:** european-disruptions-map/

The 2026-04-14 retrofit shipped 7 high-feasibility cases with full 5-metric values into `site/disruptions-data.json` under `structured_metrics.high_feasibility_cases`. The 8 medium-feasibility cases currently show only confidence flags (H/M/L/U) under `structured_metrics.medium_feasibility_cases_note` — no actual metric values. The cases.html page shipped in the 2026-04-29 fix renders these as "Per-cell confidence flags — full metric values pending v0.2 of the cross-case dataset" — Phil rejects this placeholder phrase.

**Task:** Populate the 8 medium-feasibility cases with actual metric values for the 5 metrics:
- (a) Time to 50% Task Displacement (years from commercial viability to 50% task substitution)
- (b) Institutional Response Lag (years between first measurable displacement and first major policy/regulatory/retraining response; pre-1930 cases not applicable)
- (c) Reskilling Adjacency (qualitative: adjacent / orthogonal)
- (d) Geographic/Demographic Concentration (qualitative: strong / medium / distributed)
- (e) Peak Annual Displacement Rate (peak % decline in affected occupation employment per year)

Per BR-21: every derived metric ships with `derivation_method` field + `uncertainty_band` field, NOT clean numbers. Where uncertainty is genuinely high (U flag from feasibility matrix), use a wide range (e.g., "10–40%") with explicit note. Where data is L flag, use a narrower range. Where M or H, use point estimate or tight range.

Source approach:
1. Read `site/disruptions-data.json` to identify the 8 medium-feasibility cases (in `structured_metrics.medium_feasibility_cases_note` or referenced from `feasibility_matrix_appendix`)
2. For each case + metric, fetch primary sources where available (existing primary sources in `site/sources.html` may already cover; if not, fetch new sources and add them)
3. Where primary sources are thin, fall back to the existing `displaced_worker_cases` narrative data and convert qualitative claims into bounded quantitative estimates with explicit derivation notes
4. Update `disruptions-data.json` to add a new `medium_feasibility_cases` key (parallel to `high_feasibility_cases`) with full structured metrics
5. Extend the render script for `cases.html` to display medium cases the same way as high cases, with the U-flag handling rule below

### Issue 2 (P1, ~30 min) — L3: Hide values when uncertainty=U; range for L; exact for M/H

**Repo:** european-disruptions-map/

Phil's read on the current rendering: showing a number alongside a U (uncertain) flag implies false precision and undermines trust. Implement the following rule in the render script for cases.html:

| Uncertainty flag | Display |
|---|---|
| **U** (uncertain) | Hide the numeric value; show only the flag with a tooltip explaining "data not reliable enough to estimate" |
| **L** (low confidence) | Show as wide range (e.g., "10–40 years") |
| **M** (medium confidence) | Show as narrow range (e.g., "12–18 years") |
| **H** (high confidence) | Show as point estimate or very tight range |

Update the rendering logic + the legend. Apply consistently across all metric cells in cases.html.

### Issue 3 (P1, ~1 hour) — L3: Dedupe Spreadsheets Counterfactual / Two Eras / Methodological Appendix

**Repo:** european-disruptions-map/

Currently these 3 sections appear in BOTH `findings.html` AND `analysis.html` (Deep Analysis). Pick one canonical home:
- **Decision (Phil 2026-04-29):** analysis.html holds canonical content
- findings.html keeps a one-paragraph summary + jump link to analysis.html for each section

Update findings.html render to:
1. Replace the full Spreadsheets Counterfactual section with a 2–3 sentence summary + "Read full analysis →" link to analysis.html#spreadsheets-counterfactual (or equivalent anchor)
2. Same treatment for Two Eras of Institutional Response section
3. Same treatment for Methodological Appendix section

Verify the analysis.html versions are complete + readable before deduplicating findings.html.

### Issue 4 (P1, ~15 min) — L3: Add top-level explanation of "cross-case structured metric"

**Repo:** european-disruptions-map/

The cases.html page renders structured metrics blocks per case but never explains what a "cross-case structured metric" is. Phil's note: *"I don't know, so how should anyone else know."*

Add:
1. A top-level explanation paragraph (2–4 sentences) at the start of the cases.html section describing what cross-case structured metrics are, why we use them, and what the 5 metrics measure. Place this BEFORE the first case accordion.
2. Inside each case accordion's metrics block, add a collapsible legend (default collapsed) showing the 5-metric definitions inline, so readers don't have to scroll back up.

Source the metric definitions from `structured_metrics.metric_definitions` in the JSON.

### Issue 5 (P1, ~10 min) — L3: Fix doubled numbering in findings counterfactual

**Repo:** european-disruptions-map/

The findings.html "Three Conditions for Augmentation" section renders as `1. **1. exposure to augmentation...**`, `2. **2. intact skill ladder**`, etc. — doubled numbering. Markdown numbered list + explicit bold-prefix-with-number both render.

**Fix:** In the source markdown (or the render template), strip the inner `1.`, `2.`, `3.` from the bold prefix. Result should be `1. **Exposure to augmentation innovations AND elastic output demand.** ...` etc.

### Issue 6 (P1, ~10 min) — L3: Add category names to metric definition legend

**Repo:** european-disruptions-map/

The findings.html "Methodology / Metric Definitions" legend currently shows "a. Years from commercial viability...", "b. Years between first measurable displacement...", etc. — letter + raw definition with no category name.

**Fix:** Prepend a bolded category name to each definition:
- a. **Time to 50% Task Displacement** — Years from commercial viability of the technology to 50% task displacement in the primary affected occupation. Task-level, not employment-level.
- b. **Institutional Response Lag** — Years between first measurable displacement and first major policy, regulatory, or retraining response. Structurally unavailable for pre-1930 cases (see scope statement).
- c. **Reskilling Adjacency** — Qualitative. Adjacent = displaced workers moved to skill-near roles with transferable skill ladder. Orthogonal = displaced workers moved to skill-far roles or dropped out of labour force.
- d. **Geographic / Demographic Concentration** — Qualitative. Strong = clear geographic or demographic concentration of displacement documented. Medium = partial concentration. Distributed = no clear concentration.
- e. **Peak Annual Displacement Rate** — Peak percentage decline in affected occupation employment per year during the fastest displacement phase. Derived from stock series; uncertainty bands reflect distributional assumptions.

Apply the same naming convention in `structured_metrics.metric_definitions` JSON for consistency (so other layers reading the JSON get the names too).

### Issue 7 (P1, ~30 min–2 hours) — L1: Diagnose + fix navbar/header overlay regression

**Repo:** european-ai-exposure-map/

The 2026-04-29 Gostev panel addition introduced a CSS regression — navbar overlaps with sidebar occupation detail headers + page headers (analysis page etc.). Panel itself renders correctly; only surrounding layout broke.

**Task:**
1. Inspect recent diff to `site/index.html` (and any associated CSS) for what changed in the Gostev panel commit
2. Likely culprits: z-index conflict between panel container and navbar; sticky/fixed positioning side-effect; padding/margin regression on header containers
3. Fix without removing the Gostev panel functionality
4. Verify on multiple pages: index occupation detail (desktop sidebar + mobile sheet), analysis.html, methodology.html, sources.html

**Acceptance test:** No header overlap with navbar on any page; Gostev panel still renders correctly across all 4 variants (quantitative / general / slow / slow_rs).

### Sequencing

Issues 1, 2 must be done together (Issue 2 depends on Issue 1's data structure changes). Issues 3, 4, 5, 6 are independent and can be batched. Issue 7 is L1, separate repo, fully independent.

Suggested order:
1. Issue 7 (L1 CSS) — quick, independent, unblocks L1 deployment confidence
2. Issues 3, 4, 5, 6 (L3 small fixes) — batched, ~1.5 hours total
3. Issues 1, 2 (L3 v0.2 data) — biggest item, ~1–2 days

### Constraints + reminders

- All affected sites are live on Netlify. Test locally before deploy.
- Do NOT modify `projects/european-ai-labour-synthesis/layer-6-lens-framework.md` (locked spec).
- Do NOT touch L4 (demographics) or L5 (reskilling) — no issues.
- Phil does all `git commit` and `git push` operations. Stage changes + write commit messages; Phil executes.
- Per CLAUDE.md Rule 12: Captures line at end of substantive responses.

### When done

Update `projects/ai-labour-suite-BACKLOG.md` items 23–26 with v0.2 completion notes. Report back with:
- 7 issues fixed (or which remain)
- v0.2 medium-cases data populated (8 cases × 5 metrics = 40 cells; report which cells are H/M/L/U)
- Any new issues surfaced during the fix
- Suggested deploy order for Phil's commits

## END PROMPT
