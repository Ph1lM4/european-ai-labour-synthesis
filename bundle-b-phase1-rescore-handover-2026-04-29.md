# Handover Prompt — Bundle B: Phase 1 Re-Score with Candidates Added (2026-04-29)

Self-contained prompt for a fresh session. Does not require prior conversation context.

---

## START PROMPT

I need you to re-run Layer 6 Phase 1 country scoring with 4 candidate countries added that the original Phase 1 session inadvertently dropped. The original Phase 1 produced 32 country rows; the locked spec says 36. The missing 4 are EU candidate countries (Bosnia and Herzegovina, North Macedonia, Serbia, Turkey) which ARE present in L1 data but were not scored.

Read the locked spec at `projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — particularly the "Locked Decisions" block (note country scope: 36 with composition) and the "Headline Finding" section (orthogonality result is now confirmed; do NOT re-derive). Do NOT modify the spec.

Read the original Phase 1 outputs at `projects/european-ai-labour-synthesis/`:
- `layer-6-phase1-scoring.csv` (32 rows)
- `layer-6-phase1-scoring.json`
- `layer-6-phase1-methodology-notes.md`
- `layer-6-phase1-findings.md`

These are the canonical methodology + thresholds. Replicate exactly for the 4 added countries; do NOT change scoring methodology or thresholds for the existing 32 (those are locked).

### Goal

Produce updated Phase 1 outputs covering 36 countries:
- EU-27 (27)
- EEA non-EU: NO, IS, LI (3) — LI carried with proxy-data flag (already in original)
- CH (1)
- UK (1)
- **Candidates: BA, MK, RS, TR (4) — NEWLY ADDED**

Total: 36 countries. EU27 aggregate is excluded from per-country output (it's an aggregate, not a country).

### Treatment of candidate countries

Candidates have **L1 exposure data** but lack **L4 demographic** + **L5 reskilling** data (these are EU-27 + EEA + CH + UK only). Treatment:

- `lens1_displacement_velocity` — score normally from L1 `data.json`
- `lens1_absorption_capacity` — use a candidate-baseline proxy. Suggest: weighted average of CEE rate (2–5%) + Southern European rate (2–5%), since Western Balkans + Turkey have institutional patterns most similar to those clusters. **Document the proxy choice in methodology notes.** Confidence flag = "partial-coverage" (new flag value, distinct from low / medium / high).
- `lens1_ratio` — computed normally
- `lens1_corridor` — assigned normally per ratio thresholds (1.5 / 3)
- `lens2_demographic_load` — N/A (no L4 data); use `null` or empty string in CSV
- `lens2_retirement_offset` — N/A
- `lens2_overlap_score` — N/A
- `combined_corridor_v1` — equal to `lens1_corridor` (no Lens 2 modifier possible)
- `confidence` — "partial-coverage"
- `notes` — "candidate-status partial-coverage; L1 only; L2/L4/L5 data not available; absorption capacity proxied as candidate-baseline"

### What to verify

Before declaring complete:
1. **36 rows** in CSV (no EU27 aggregate)
2. **Candidate row sanity check:** TR (Turkey, large population, high coordination-layer share, mixed institutional pattern) — Lens 1 ratio likely puts it in C2 or C3. Document which.
3. **All existing 32 countries unchanged** from original Phase 1 — corridor assignments, confidence flags, all numbers identical
4. **Orthogonality finding restated** in findings.md but NOT re-tested — it's already confirmed for the 32 with European demographic data; candidates don't have demographic data so the finding doesn't apply to them in the same way (note this caveat explicitly)
5. **PL at 2.96 still flagged** as Phase 3 sentinel test case for structural-bias re-calibration

### Outputs

Update (NOT replace) the 4 Phase 1 output files:
- `projects/european-ai-labour-synthesis/layer-6-phase1-scoring.csv` — 36 rows
- `projects/european-ai-labour-synthesis/layer-6-phase1-scoring.json` — 36 entries
- `projects/european-ai-labour-synthesis/layer-6-phase1-methodology-notes.md` — append a new section "Candidate Country Treatment (added 2026-04-29)" documenting the proxy choice for absorption capacity + the partial-coverage confidence flag
- `projects/european-ai-labour-synthesis/layer-6-phase1-findings.md` — update country-count claim from 32 → 36; append a new section "Candidate Country Findings" with the 4 candidates' Lens 1 readings + caveats; confirm orthogonality finding only applies to the 32 with demographic data

### Constraints

- Do NOT modify `projects/european-ai-labour-synthesis/layer-6-lens-framework.md` (locked spec)
- Do NOT change scoring methodology or thresholds for the existing 32 countries
- Do NOT touch any layer repo (L1–L5)
- Do NOT score Lens 4 or Lens 5 — that's Phase 2
- Do NOT assign fragility classes — Phase 3
- Phil does all git commit + push. Stage outputs; Phil executes.

### When done

Report back with:
- 4 candidate corridor assignments (BA, MK, RS, TR — which corridor each lands in)
- Confidence sanity check (all 4 should be partial-coverage; existing 32 unchanged)
- Any data gaps surfaced during candidate scoring
- Whether the absorption-capacity proxy choice produces defensible corridor assignments (do TR's known Eastern-Mediterranean labour-market characteristics match the corridor it lands in?)

## END PROMPT
