# Handover Prompt — Layer 6 Phase 1: Country × Lens Scoring v1 (2026-04-29)

Use this as the opening prompt for a new session. Self-contained — does not require prior conversation context.

---

## START PROMPT

I need you to execute **Layer 6 Phase 1** of the European AI Labour Market suite — first-pass country-level corridor assignment using Lens 1 (Displacement Velocity × Absorption Capacity) and Lens 2 (Demographic Buffer or Accelerant) only. Lens 4 (Compounding Shocks) and Lens 5 (Polycrisis Drag) are Phase 2 — do NOT touch them in this session.

The Layer 6 spec is at `projects/layer-6-lens-framework.md` — read it FIRST, especially the "Locked Decisions" block at the top, the Lens 1 + Lens 2 sections, and the Corridors section. The spec was locked 2026-04-29; do NOT modify it. This session writes scoring outputs only.

### Goal

Produce a country-level scoring table (36 countries: EU-27 + EEA + CH + UK) with these columns per country:
- `country_code` (ISO-2)
- `lens1_displacement_velocity` (employment-weighted exposure score across ISCO 3-digit groups)
- `lens1_absorption_capacity` (cross-zone Zone A→C transition rate; uses L5 system-model assignment)
- `lens1_ratio` (displacement / absorption)
- `lens1_corridor` (preliminary corridor 1/2/3 from Lens 1 alone)
- `lens2_demographic_load` (working-age population shrinkage rate per year through 2035)
- `lens2_retirement_offset` (% of high-exposure roles absorbed by retirement by 2035)
- `lens2_overlap_score` (does demographic shortage overlap with displaced occupations? 0–1 scale)
- `combined_corridor_v1` (Lens 1 + Lens 2 combined assignment)
- `confidence` (high / medium / low based on data density)
- `notes` (any country-specific caveats)

Output as both `projects/layer-6-phase1-scoring.csv` AND `projects/layer-6-phase1-scoring.json` (CSV for human review, JSON for downstream Phase 2 + site rendering).

### Inputs (canonical data sources)

**Layer 1 — AI exposure scores per ISCO × country:**
- File: `/Users/philippmaul/Documents/projects/european-ai-exposure-map/site/data.json`
- Use: technical exposure score per ISCO 3-digit group, employment counts per country × ISCO
- Aggregate to country-level displacement velocity using employment-weighted average exposure across all ISCO groups in that country
- Apply Gostev sensitivity floor (~9%) as a noise band — do NOT score below this floor as confidently displaced
- Apply Klinger coordination-share weighting if data permits; if not, flag as Phase 2 refinement

**Layer 4 — Demographic projections per country:**
- File: `/Users/philippmaul/Documents/projects/european-demographics-map/site/demographics-data.json`
- Use: working-age population trajectory per country 2025→2035; retirement cohort size; dependency ratio shift
- Lens 2 demographic load = annual shrinkage rate of working-age population per country
- Lens 2 retirement offset = retirement cohort as % of high-exposure roles (use L1 for "high-exposure" definition)

**Layer 5 — Reskilling absorption capacity per country:**
- File: `/Users/philippmaul/Documents/projects/european-reskilling-map/site/reskilling-data.json`
- Use: cross-zone Zone A→C transition rate per country, mapped via system model (Nordic flexicurity 8–12%, Germanic Dual 3–6%, Continental Corporatist 5–8%, Liberal Market 2.8–3.6%, Southern European 2–5%, Central/Eastern European 2–5%)
- Country → system model mapping is in the L5 reskilling-data.json under the systems comparison section

**Layer 3 — historical disruption metrics (read-only context):**
- File: `/Users/philippmaul/Documents/projects/european-disruptions-map/site/disruptions-data.json`
- Use: structural-bias warning (historical calibration overstates protective power of buffering institutions — Autor 2024 + El-Sahli/Upward counterfactual). Apply this as a CALIBRATION NOTE in the output: corridor 1 (Managed Transition) is narrower than historical base rates suggest.
- The L3 site has a render gap (data is in JSON, HTML doesn't display it). Read the JSON directly. Another session is fixing the render gap; do not touch L3 in this session.

### Methodology

**Lens 1 v1 (single-horizon — task→employment lag retrofit is Phase 2):**
1. For each country, compute employment-weighted average exposure across all ISCO 3-digit groups
2. For each country, look up the cross-zone transition rate from L5 system-model assignment
3. Compute ratio = (employment-weighted exposure) / (transition rate × time-horizon adjustment)
4. Time-horizon adjustment: AI disrupts 1–3 years; reskilling responds 5–9 years; use 5x for the "speed gap" coefficient documented in L5
5. Assign preliminary corridor:
   - **Corridor 1 (Managed Transition):** ratio < 1.5
   - **Corridor 2 (Bifurcated Absorption):** ratio between 1.5 and 3, AND middle-skill share of high-exposure cohort > 60%
   - **Corridor 3 (Displacement Without Absorption):** ratio > 3, OR ratio between 1.5–3 with non-bifurcated profile

These thresholds are *first-pass anchors*, not validated. Document the threshold-selection rationale in `projects/layer-6-phase1-methodology-notes.md`. They must be re-tested in Phase 3 (corridor reduction + structural-bias surfacing).

**Lens 2 (demographic overlay):**
1. For each country, compute annual working-age shrinkage rate (Layer 4 data)
2. For each country, compute retirement cohort overlap with displaced cohort using ISCO occupation-by-age data if available; if not, use country-level retirement projections as a proxy and flag confidence
3. Lens 2 modifier:
   - If retirement offset ≥ 80% of displaced cohort AND demographic shortage occupations overlap with displaced occupations → demographic buffer thesis HOLDS for this country (corridor shifts toward 1)
   - If retirement offset < 50% OR no occupation overlap → demographic buffer thesis FAILS for this country (corridor stays or shifts toward 3)
   - Intermediate cases → no modifier
4. The non-obvious hypothesis from the spec: "default assumption is demographic decline softens AI's blow. If data shows displacement and shortage are structurally orthogonal, that's the most important finding in the project." Test this explicitly. Report which countries show structural orthogonality.

**Combined corridor v1:** apply Lens 2 modifier to Lens 1 preliminary corridor → output `combined_corridor_v1`.

**Confidence flag:** high if all 3 inputs (L1, L4, L5) have country-level data; medium if 1 is proxy; low if 2+ are proxy. Flag any countries where Layer 4 or Layer 5 data is sparse (likely Malta, Cyprus, Luxembourg, Iceland, Liechtenstein).

### Output

1. `projects/layer-6-phase1-scoring.csv` — 36 rows + header, all columns above
2. `projects/layer-6-phase1-scoring.json` — same data, JSON-structured
3. `projects/layer-6-phase1-methodology-notes.md` — threshold-selection rationale, data-source caveats, decisions made during scoring (e.g., proxy choices), countries with low confidence
4. `projects/layer-6-phase1-findings.md` — first-pass observations:
   - Which countries land in which preliminary corridor under Lens 1 alone
   - Which countries shift corridor under Lens 2 overlay
   - Which countries (if any) show structural orthogonality between displaced occupations and demographic-shortage occupations (the non-obvious hypothesis)
   - Which countries are confidence-flagged and why
   - Open questions for Phase 2 (Lens 4 + 5)

### Constraints

- **Do NOT modify** `projects/layer-6-lens-framework.md` (locked spec)
- **Do NOT touch** Layers 1–5 repos — another session is fixing L1–L5 issues
- **Do NOT score** Lens 4 or Lens 5 — that's Phase 2
- **Do NOT assign fragility classes** (I–IV) — those need the full 5-scenario stack from Phase 2
- **Do NOT pre-fit findings to the corridor count.** The spec says "let the lenses produce findings first; do not pre-fit to a triad." If your Lens 1 + Lens 2 scoring produces a clean 4-cluster result instead of 3, report that honestly.
- **Apply the structural-bias warning** as a calibration note, not a footnote: corridor 1 is narrower than historical base rates suggest, corridor 3 is correspondingly broader.
- **Phil does all `git commit` and `git push`** operations. Stage outputs; Phil executes.

### Verification

Before declaring Phase 1 complete:
1. Sanity-check 5 countries by hand: DE, FR, IT, ES, PL. Their corridor assignments should be defensible against the data — if any feel wrong, the methodology is likely wrong, not the country.
2. Verify the Nordic countries (DK, NO, SE, FI) cluster together (likely Corridor 1, high confidence).
3. Verify Ukraine is NOT in the output — it's a Lens 5 reference case in Phase 2, not a Phase 1 corridor case.
4. Verify total country count is 36 (EU-27 + EEA-3 [NO, IS, LI] + CH + UK).

### What this session does NOT do

- L6 site build (Phase 5)
- Synthesis document draft (Phase 4)
- Lens 4 or Lens 5 scoring (Phase 2)
- Scenario stack application (Phase 2/3)
- Fragility class assignment (Phase 3)
- Corridor reduction validation (Phase 3)

### When done

Report back with:
- Phase 1 outputs shipped (4 files)
- First-pass corridor distribution (how many countries in each corridor)
- Whether the structural-orthogonality finding holds (Lens 2 non-obvious hypothesis)
- Any data gaps that block Phase 2
- Any methodology decisions that need Phil's review before Phase 2 starts

## END PROMPT
