# Handover Prompt — Bundle V: Scenario Reframe (S3 Jobs Transform addition + S1–S8 linear renumbering)

Bounded analytical session. Adds an 8th scenario (Jobs Transform, slightly-optimistic steady-state) + renumbers all scenarios linearly in spectrum order. Re-scores regime-conditional probability vectors. Updates SOT JSON + flags downstream re-derivation. ~90–110 min.

---

## Context

Phil-locked decision (2026-04-30 evening, master session): the existing scenario set conflated two analytical readings into S2a (Wage Cliff). Both readings are defensible and likely under different conditions:
1. AI substitutes for mid-skill labour → wages compress → fewer or lower-paid reinstatement jobs (the existing S2a Wage Cliff)
2. AI substitutes for routine tasks → wages stable; jobs reshape around the rest (Brynjolfsson jagged-frontier / Nielsen forklift / BCG +40%/-19pp territory) — currently absent from the framework

Bundle V adds the missing reading as a separate scenario and renumbers the full set linearly in spectrum order for executive register clarity. The S2-family naming convention (a/b/c) is retired in favour of S1–S8 sequential codes.

---

## START PROMPT

I need you to add a new scenario (S3 Jobs Transform) and renumber the full scenario set linearly in spectrum order. This is analytical work + structural rename. Re-score regime-conditional probability vectors and update per-country scenario corridor mappings. Modify SOT JSON + lens framework spec only; flag downstream re-derivation for the deliverable surface (Executive, One-Pager, Einfache, Specialist Appendix, glossary).

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON, schema v1.0. Current `scenarios` block has S1, S2a, S2b, S3, S4a, S4b, S5. Per-country `scenarios.{S}` references throughout 36 country blocks.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec. Update scenario taxonomy section.
- `/Users/philippmaul/Documents/second-brain/skills/disruption-analysis/references/takeaways.md` — read T31 (Nielsen cognitive-forklift / seniority-tier redistribution as within-occupation Class C mechanism) + T32 (pancaking as Class C terminal state) for the empirical grounding of S3 Jobs Transform.
- `/Users/philippmaul/Documents/projects/european-disruptions-map/site/findings.html` — Layer 3 historical-precedents reference: ATM/teller (Bessen), Spreadsheets (Levy), telephone-operator displacement (Feigenbaum & Gross 2024) — these are S3 Jobs Transform analogues at the historical case base.

### The renumbering map (spectrum order)

```
OLD CODE → NEW CODE — Scenario name (spectrum position)
─────────────────────────────────────────────────────────────
S1       → S1 — Reinstatement Revival         (uber-optimistic)
S2b      → S2 — Climate Adaptation Boom       (optimistic)
NEW      → S3 — Jobs Transform                (slightly optimistic) ← ADDED
S3       → S4 — Muddle Through                (middle)
S2a      → S5 — Wage Cliff                    (slightly pessimistic)
S4a      → S6 — Reinstatement Failure         (pessimistic)
S4b      → S7 — Bandwidth Fracture            (pessimistic)
S5       → S8 — Concurrent-Crisis Cascade     (parallel cascade, conditional)
```

**Rename sequencing matters** — execute in an order that avoids collision. Recommended:
1. First add S3 Jobs Transform as a NEW key (no collision)
2. Then rename in ascending NEW-code order, but use a temporary suffix (`_tmp`) where collisions threaten:
   - S2b → S2_tmp
   - S3 → S4 (now-empty S3 keeps the new entry safe)
   - S2_tmp → S2
   - S2a → S5
   - S4a → S6
   - S4b → S7
   - S5 → S8
3. Verify no collision artifacts remain before serialising.

OR: read the entire SOT JSON into memory, build a fresh scenarios block + a key-rename map, transform every per-country `scenarios.{old}` reference via the map, write atomically. Probably cleaner.

### S3 Jobs Transform — semantic definition

Author the scenario block following the same shape as existing scenarios (S1/S2/S4 etc):

**Label:** Jobs Transform
**Spectrum position:** slightly optimistic (between S2 Climate Adaptation Boom and S4 Muddle Through)
**Mechanism:** AI substitutes for routine tasks within existing occupations. Wages stay stable or rise modestly. The reinstatement effect operates within-occupation (jobs reshape) rather than cross-occupation (new occupations created). Workers spend less time on routine sub-tasks and more on judgment / coordination / non-routine cognitive-social work. Empirically grounded by:
- Brynjolfsson et al. OpenAI productivity RCT 2025 — call-centre workers
- Dell'Acqua et al. HBS WP 24-013 — BCG consultants +40% on within-frontier tasks, -19pp on out-of-frontier
- Nielsen + Gibbons ADPList Q1 2026 — "forklift for the mind" + seniority-tier redistribution (T31)
- Historical analogues: ATM/teller (Bessen), Spreadsheets (Levy)

**Conditions under which S3 dominates:** countries with strong within-firm transition infrastructure, high human-capital intensity, sector mix favouring cognitive-social complementarity (Deming).

**Distinct from neighbours:**
- Distinct from S2 Climate Adaptation Boom — S2 requires *new sectoral demand*; S3 reshapes *existing occupations* without sectoral redirection.
- Distinct from S5 Wage Cliff — S5 has mid-skill wage compression; S3 has wages stable or up.

### Probability re-scoring rules

Routine variants (S1–S7) sum to 1.0 per regime. S8 (Concurrent-Crisis Cascade) is conditional/orthogonal — keep its existing probability values.

**Re-score guidance:**
- Total routine probability mass = 1.0 across S1–S7 per regime.
- S3 Jobs Transform takes mass primarily from S2 (some optimism that was unattributed to climate-specific) and S4 (some Muddle-Through mass that's actually steady-state job-transformation).
- Maintain pre-existing key findings:
  - **S2 must remain modal under post-growth** (the load-bearing finding: optimism path narrows to Climate Zone-C). After re-score, P(S2 | post_growth_empirical) ≥ P(S4 | post_growth_empirical).
  - **S5 Wage Cliff probability stays moderate-to-high** under secular_stagnation_warning + post_growth_empirical regimes (preserves the existing Wage Cliff scoring under stress).
  - **Total optimistic mass (S1+S2+S3) and total pessimistic mass (S5+S6+S7) shift modestly** — the old framework underweighted optimistic probability by treating S2a as pessimistic (which it was when called Wage Cliff). The new framework lets S3 carry the legitimate slightly-optimistic mass that was suppressed.

**Suggested probability re-score (sub-session refines based on the rules above):**

| Regime | S1 | S2 | **S3** | S4 | S5 | S6 | S7 | (S8 cond.) |
|---|---|---|---|---|---|---|---|---|
| growth_baseline | 0.10 | 0.20 | **0.10** | 0.25 | 0.15 | 0.12 | 0.08 | 0.05 |
| secular_stagnation_warning | 0.07 | 0.25 | **0.05** | 0.23 | 0.15 | 0.13 | 0.12 | 0.10 |
| post_growth_empirical | 0.05 | 0.30 | **0.08** | 0.22 | 0.13 | 0.13 | 0.09 | 0.15 |

Rationale (sub-session validates):
- S3 takes ~10% mass from old S3 Muddle Through (now S4) which was over-loaded as a residual category.
- S3 mass higher under growth_baseline (where steady-state job transformation is most plausible) than secular_stagnation (where the breakdown vector dominates) or post_growth (where S2 climate dominates).
- 80% CI bands per cell at ±0.05–0.07 (sub-session establishes via structured-elicitation reasoning).

If sub-session's analytical judgement produces different distributions, document the reasoning in metadata.

### Per-country S3 corridor mapping

For each of 36 countries, score where S3 Jobs Transform lands the country: C1 (Managed Transition), C2 (Partial Absorption), or C3 (Displacement Without Absorption).

**Heuristic:** S3 corridor = country's institutional capacity to support within-occupation job reshaping under stable wages. Approximate via:
- High institutional capacity (Nordic flexicurity 8–12% A→C transition, Continental Corporatist 5–8%) → C1 likely under S3
- Mid institutional capacity (Germanic Dual 3–6%, Southern European 2–5%) → C2 likely
- Low institutional capacity (CEE 2–5%, Liberal Market high IE/UK with 3.2% derived) → C2 or C3
- Class III countries with weak ALMP (Mediterranean weak-ALMP cluster) → C2 (S3 is better than S6/S7 but not great)
- Class IV countries (MK, RS, TR) → C2 (S3 doesn't escape baseline class)
- s2b-dependent set (AT, LU, TR) — S3 can be a secondary path to C1 if institutional capacity is high enough; AT and LU likely C1 under S3 (high institutional capacity); TR stays C2.

Sub-session refines per-country with the country's `_system_p1` tag + `lens1_a_to_c_transition_rate_pct.central_derived_pct` as primary inputs.

### Goal — modify SOT JSON only, flag downstream

**Modify:**
- `layer-6-deliverable-data.json` — add S3, renumber to S1–S8, re-score probabilities, add per-country S3 corridor mappings
- `layer-6-lens-framework.md` — update scenario taxonomy section (find it, replace S1–S5 codes with S1–S8 + add S3 Jobs Transform definition)

**Do NOT modify** (flag for post-Bundle-V re-derivation):
- `layer-6-deliverable-document-executive.md` — Executive §3 spectrum + scenario probability table
- `layer-6-deliverable-onepager.md` — finding 3 (s2b-dependent → S2-dependent under new code)
- `layer-6-deliverable-document-einfache-en.md` and `-de.md`
- `layer-6-deliverable-document.md` — Specialist Appendix §3 + §6
- `layer-6-glossary-draft.tsv` — scenario entries

These get updated in a unified pass alongside Phase 1 (Bundle O storytelling rewrite) — Bundle V flags the changes; doesn't make them.

### Composition rules

1. **Read-only against everything except SOT JSON + lens framework spec.**
2. **BR-19 no fabrication.** Probability re-score grounds in the rules above + structured reasoning; per-country S3 corridor placements ground in `_system_p1` + L5 transition rates. Document reasoning in metadata.
3. **Preserve key findings:**
   - S2 modal under post_growth (was S2b dominance — locked spec line 104)
   - S5 (Wage Cliff) pessimistic mass holds under stress regimes
   - S8 (Cascade) conditional probabilities unchanged (0.05 / 0.10 / 0.15 across regimes)
4. **Atomic SOT JSON write** — verify round-trip cleanly before persist.
5. Phil does all git commits.

### Verification (before reporting back)

1. SOT JSON loads round-trip cleanly via `json.load → dumps → load`.
2. `scenarios` block has exactly 8 entries: S1, S2, S3, S4, S5, S6, S7, S8.
3. No remaining `S2a`, `S2b`, or `S2c` keys anywhere in the SOT JSON.
4. All 36 country blocks have `scenarios.S3` populated with corridor (1, 2, or 3) + label "Jobs Transform" (or country-specific narrative line).
5. Probability vectors per regime sum to 1.0 across S1–S7 (within ±0.001).
6. S2 ≥ S4 under post_growth_empirical (preserves load-bearing finding).
7. S8 conditional probabilities = 0.05 / 0.10 / 0.15 (unchanged).
8. Top-level `metadata.bundle_v_scenario_reframe` block records: rationale, renumbering map, probability re-score reasoning, per-country S3 mapping methodology, ingestion date.
9. Lens framework spec scenario taxonomy section updated to S1–S8 + S3 Jobs Transform definition added.

### When done — report back to master session with

1. Renumbering audit: confirm 0 instances of S2a/S2b/S2c/old-S3/old-S4a/old-S4b/old-S5 in the SOT.
2. New probability table (regime × scenario, central + 80% CI).
3. Per-country S3 corridor distribution (count of countries per C1/C2/C3 under S3).
4. Sentinel checks: S2 modal under post-growth ✓ ; S5 pessimistic mass under stress ✓ ; S8 conditional unchanged ✓ .
5. Knock-on flag list — every deliverable file that needs re-derivation against the renumbering, with line-level grep results showing where each old code lives.
6. Composition gaps — places where the existing framework didn't carry data needed for S3 corridor mapping (likely candidate countries where transition rate is band-proxied not derived).
7. Any candidate brain captures — likely none (this is mechanical scenario addition + re-score, not novel methodology).

## END PROMPT
