# Handover Prompt — Fix L1–L5 issues identified in Layer 6 scoping (2026-04-29)

Use this as the opening prompt for a new session. Self-contained — does not require prior conversation context.

---

## START PROMPT

I need you to fix 4 issues across Layers 1–5 of the European AI Labour Market suite that were surfaced during the 2026-04-29 Layer 6 scoping session. Full verification log is at `projects/layer-6-suite-verification-2026-04-29.md`. Backlog items 23–26 in `projects/ai-labour-suite-BACKLOG.md` document each issue. Layer 6 spec is at `projects/layer-6-lens-framework.md` — do NOT modify it; this is a layer-input fix session, not L6 build.

The 5 layer repos live in `/Users/philippmaul/Documents/projects/`:
- L1: `european-ai-exposure-map/` → `ai-exposure.nexalps.com` (live, v2.4.0)
- L2: `european-careers-map/` → `job-market.nexalps.com` (live, v1.0)
- L3: `european-disruptions-map/` → `disruptions.nexalps.com` (live, render gap)
- L4: `european-demographics-map/` → `demographics.nexalps.com` (live, README stale — Phil handling separately, skip)
- L5: `european-reskilling-map/` → `reskilling.nexalps.com` (live, no issues)

All 4 layers (excluding L4) are public live sites on Netlify. Be careful with deploys.

### Issue 1 (P0, ~1 day) — L3 render gap

**Repo:** `european-disruptions-map/`

The 2026-04-14 retrofit session shipped 5 new top-level keys into `site/disruptions-data.json`:
- `structured_metrics` (with sub-keys: schema_version, methodology_note, metric_definitions, high_feasibility_cases, medium_feasibility_cases_note, low_feasibility_cases_note, feasibility_matrix_appendix)
- `spreadsheets_counterfactual`
- `incumbent_vs_cohort_displacement`
- `capability_vs_adoption_gap`
- `institutional_response_scope_statement`

These are populated and present in the JSON (verified 2026-04-29). But the HTML render scripts were NOT extended to display them. As a result:
- `cases.html` references "20 case studies" but doesn't name them or show structured metrics per case
- `findings.html` doesn't have Spreadsheets Counterfactual, Two Eras of Institutional Response, or Methodological Appendix sections
- Feasibility matrix table is not rendered anywhere on the site

**Task:**
1. Read the current render scripts in `european-disruptions-map/scripts/` — find the script(s) that produce `cases.html` and `findings.html`
2. Extend the render logic to read each of the 5 new JSON keys and emit corresponding HTML
3. For `cases.html`: enumerate the 20 cases by name, show structured metrics inline per case (the 5 metrics: time-to-50%, institutional response lag, reskilling adjacency, geographic concentration, peak annual rate) using the `high_feasibility_cases` data, with confidence flags for medium feasibility per `medium_feasibility_cases_note`, and narrative-only treatment for cases listed in `low_feasibility_cases_note`
4. For `findings.html`: add new sections rendering `spreadsheets_counterfactual` (with the three conditions: elastic output demand + intact skill ladder + complement not substitute), `institutional_response_scope_statement` (Two Eras: pre-state 1440–1880 vs post-state 1930–present), and the feasibility matrix from `feasibility_matrix_appendix`
5. Verify locally before committing; deploy via Netlify
6. After deploy, fetch `disruptions.nexalps.com/cases.html` and `disruptions.nexalps.com/findings.html` to confirm the new sections render

**Acceptance test:** A live-site visitor can read all 20 case studies by name and see structured metrics for the 7 high-feasibility cases. The structural-bias warning (historical calibration is structurally optimistic — Autor 2024 + El-Sahli/Upward counterfactual) is visible in the Methodological Appendix or equivalent.

### Issue 2 (P1, ~2 hours) — L2 missing 2 of 7 regulatory directives

**Repo:** `european-careers-map/`

`site/analysis.html` has a "Regulatory Demand Engine" section covering NIS2, DORA, EU AI Act, EAA, CSRD. Two regulatory directives are missing:
- **Platform Work Directive** — directly affects freelance/platform coverage gap, closes ~2030. Effective December 2026 per VENTURE-SCOPE in `european-ai-exposure-map/`. Affects platform workers + AI transparency requirements.
- **Pay Transparency Directive** — intersects with AI-driven compensation decisions. Effective June 2026 per VENTURE-SCOPE. Affects gender-pay-equity reporting and ISCO groups subject to algorithmic pay-setting.

**Task:**
1. Read the existing Regulatory Demand Engine table on `analysis.html` to understand structure (likely: Directive | Job Impact | Duration columns)
2. Add 2 rows for Platform Work Directive + Pay Transparency Directive
3. Source content from `european-ai-exposure-map/PROJECT-SPEC.md` (or `VENTURE-SCOPE.md` in second-brain) which has the regulatory framework summarised, plus a fresh fetch of EU Commission materials to verify entity counts and effective dates
4. Update sources list (`sources.html`) if new primary sources are cited
5. Deploy via Netlify
6. Verify on live site

**Acceptance test:** All 7 directives in the Regulatory Demand Engine table on `job-market.nexalps.com/analysis.html`. Each row has directive name + scope + job impact + duration.

### Issue 3 (P1, ~1 day) — L1 Gostev Capability Floor panel

**Repo:** `european-ai-exposure-map/`

The 2026-04-28 Gostev ingestion (CHANGELOG entry "Gostev empirical-floor ingestion") planned a Capability Floor panel per occupation but did not ship it. Source data: Peter Gostev (AI Capability Lead, Arena.ai), AIE Europe keynote "What Do Models Still Suck At?" (London, April 10 2026). Three findings:
1. Frontier dissatisfaction floor at ~9% in Q1 2026 (down from ~17% pre-reasoning, ~12% post-o1) — sensitivity bound on every "AI will reliably do X% of task Y" forecast
2. Category gradients are large and persistent — quantitative tasks improve dramatically; gaming, magical, finance, law improve weakly
3. Reasoning often makes pushback worse on the BS benchmark — relevant to legal triage, audit, regulatory advisory, medical occupations

Full reference: `skills/disruption-analysis/SKILL.md` v0.5.2 Takeaway 30 (in second-brain). Cross-references in `knowledge/practitioner/contemporary-claims-registry.md` Source 8.

**Task:**
1. Read the current occupation detail UI in `european-ai-exposure-map/site/` — find the page that renders per-occupation data
2. Add a "Capability Floor" panel that displays:
   - The frontier capability floor (~9% Q1 2026) as a fixed sensitivity bound
   - The Gostev category mapping for the occupation's task profile (quantitative-heavy: capability progressing fast; gaming/magical/finance/law-heavy: capability progressing slowly)
   - Where applicable (legal triage, audit, regulatory advisory, medical), a "Reasoning-Sensitive" flag noting deploying reasoning models reduces deployment value
3. Wire data into the existing data pipeline so the panel populates per ISCO 3-digit group based on its task composition
4. Deploy + verify on live site

**Acceptance test:** Visiting any legal/audit/medical occupation page shows the Capability Floor panel with the Gostev sensitivity bound + reasoning-sensitive flag where applicable. The panel is consistent across all 36 countries.

### Issue 4 (P2, ~30 minutes) — L1 PROJECT-SPEC.md stale

**Repo:** `european-ai-exposure-map/`

`PROJECT-SPEC.md` has Status: "Concept / Pre-Build" dated 2026-03-16. Site is at v2.4.0 with full Risk/Opportunity/Context toggle, 36 countries, and 7 layers deployed.

**Task:**
1. Either (a) update Status field to current version (v2.4.0) and add a brief "What shipped" log paragraph, OR (b) replace the file with a 1-line pointer to README + CHANGELOG as canonical sources of project state
2. Recommend (b) — single source of truth, no drift risk

**Acceptance test:** No file in the repo claims the project is in "Concept / Pre-Build" state.

### Sequencing

Issue 1 (L3 render gap) is P0 because L6 currently has to read `disruptions-data.json` directly to get the structural-bias warning + retrofit findings. Closing this removes long-term coupling and is therefore the priority.

Issues 2 + 3 + 4 can run in parallel with each other. Issue 4 is trivial; can ship in 30 minutes.

### Constraints + reminders

- All 4 affected sites are live on Netlify. Test locally before committing.
- Do NOT modify `projects/layer-6-lens-framework.md` — that's the L6 spec, locked 2026-04-29.
- Do NOT touch L4 README — Phil is handling that separately.
- L5 has no issues — do not touch.
- Match the existing style of each repo (each has its own README, CHANGELOG, code/data licensing). Don't introduce new tooling.
- Phil does all `git commit` and `git push` operations. Stage changes and write commit messages; Phil executes.

### When done

Update `projects/ai-labour-suite-BACKLOG.md` items 23–26 with completion notes (date, commit SHA, verification result). Report back with: which issues fixed, what remains open, and any new issues surfaced during the fix.

## END PROMPT
