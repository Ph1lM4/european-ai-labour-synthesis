# Handover Prompt — Bundle M: Layer 6 Deliverable Single-Source-of-Truth JSON (Phase 4 Foundation)

Bounded build session. Composes the single JSON that downstream document (Bundle N) and site (Bundle O) both consume. Schema-locks the deliverable data structure so document and site can build in parallel. ~45–60 min.

---

## START PROMPT

I need you to build the Layer 6 deliverable's single-source-of-truth (SOT) JSON file. This is the data foundation for Phase 4: both the analytical document (Bundle N) and the `synthesis.nexalps.com` site (Bundle O) will consume this JSON. Schema-lock the structure so the two downstream bundles can build in parallel without coupling.

This is NOT a re-computation session. All locks are already in place from Phase 1–3. Bundle M's job is composition, not analysis.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec (corridors, fragility classes, scenarios, scale tags, regime taxonomy)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase4-plan-2026-04-29.md` — Phase 4 plan + Q2-Q6 deliverable scoping decisions
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-scenario-probability.csv` + `.json` — Bundle L outputs (final fragility classes; expected corridor; class_i_confidence; s2b_dependent; squeeze_flag; breach_flag; s5_cascade_priority; scale_tag; narrative_one_liner; per-country probability-weighted corridor + CIs)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-corridor-rescaled.csv` + `.json` — Bundle J outputs (re-calibrated corridors at 1.20/2.80; sub-cluster annotations; PL sentinel result)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-klinger-rescaled.csv` + `.json` — Bundle K-2 outputs (Lens 5(c) 2-digit; capability-floor breach scope; archetype split — education/admin LIFT vs finance/tech DRAG)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase1-scoring.csv` + `.json` — Phase 1 baseline corridors + lens1_ratio + sub-cluster classification
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-data.json` — Lens 4/5 input cells (Gini, geopolitical, climate shocks, MFF allocation, trade decoupling, Klinger reference, EEA vulnerability, Munich Re, adaptation budget, regime stability, MSC narratives)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-scoring.csv` + `.json` — Bundle D outputs (per-scenario corridors per country; Lens 4 squeeze-flag; Lens 5 composite drag) — kept for traceability
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-probability-findings.md` — Bundle L narrative findings (TL;DR + 5 folded-finding paragraphs)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-corridor-findings.md` + `layer-6-phase3-klinger-findings.md` — Bundle J + K-2 narrative findings

### Goal — output `layer-6-deliverable-data.json`

Single JSON file composing all per-country deliverable fields + cross-cutting metadata + folded findings. Schema must be:
- **Stable** — Bundles N (document) and O (site) lock against this schema; schema changes after Bundle M complete trigger both downstream bundles to re-read.
- **Hierarchical** — country-level data nested under per-country keys; cross-cutting findings at top level; metadata block at top.
- **Self-describing** — every field includes `description` + `source_bundle` + `source_field` so downstream readers can audit without re-reading inputs.
- **Renderable** — site (Bundle O) reads this JSON via fetch; format must be web-renderable JSON (no Python pickle artifacts, no NaN, no Infinity, all floats finite).

### Schema (locked by this bundle)

```json
{
  "metadata": {
    "deliverable": "Layer 6 — European AI Labour Market Synthesis",
    "phase": 4,
    "schema_version": "1.0",
    "build_date": "2026-04-29",
    "country_scope_count": 36,
    "lens_count": 5,
    "scenario_count": 7,
    "fragility_class_count": 4,
    "corridor_count": 3,
    "regime_count": 3,
    "thresholds": { "C1_cap": 1.20, "C3_floor": 2.80 },
    "class_distribution": { "I": 9, "II": 9, "III": 15, "IV": 3 },
    "amendments_trail": [
      { "stage": "Phase 2 S5-orthogonal", "rule": "Class I scope restricted to S1-S4b" },
      { "stage": "Phase 3 Bundle J relative-stable", "rule": "Class I = ±1 of baseline" },
      { "stage": "Phase 3 Bundle L Q1 asymmetric-guard", "rule": "Class I = ±1 AND no routine variant reaches C3" }
    ],
    "source_bundles": ["Phase 1", "Bundle D", "Bundle H", "Bundle I", "Bundle J", "Bundle K-2", "Bundle L"]
  },
  "countries": {
    "AT": {
      "code": "AT",
      "name": "Austria",
      "phase1_lens1_ratio": 2.41,
      "phase3_corridor": 2,
      "regime": "post_growth_empirical",
      "fragility_class": "II",
      "class_i_confidence": null,
      "scale_tag": "both",
      "scenarios": {
        "S1": { "corridor": 2, "label": "Reinstatement Revival" },
        "S2a": { "corridor": 2 }, "S2b": { "corridor": 1 }, "S3": { "corridor": 2 }, "S4a": { "corridor": 2 }, "S4b": { "corridor": 3 }, "S5_cascade": { "corridor": 3 }
      },
      "expected_corridor": 2.10,
      "expected_corridor_rounded": 2,
      "corridor_uncertainty_band": 0.92,
      "dominant_corridor": 2,
      "p_dominant": 0.65,
      "lens_findings": {
        "lens1_displacement_velocity": "...",
        "lens2_demographic_buffer": "refuted at scale",
        "lens4_compounding": { "shock_count": 3, "squeeze_flag": false, "buffering_squeeze": null },
        "lens5_polycrisis_drag": { "composite": 0.512, "klinger_2digit": "...", "breach_flag": false, "s5_cascade_priority": "MEDIUM" }
      },
      "s2b_dependent": true,
      "squeeze_flag": false,
      "breach_flag": false,
      "narrative_one_liner": "...",
      "scenario_distribution_language": "Likely in C2 with ~65% mass; reaches C1 only under S2b; reaches C3 under S4b only",
      "regime_implications_note": "..."
    },
    "BE": { ... },
    ...
  },
  "cross_cutting_findings": {
    "structural_bias_validation": "Phase 3 corrected thresholds (C1<1.20, C3≥2.80) revealed strict-stable Class I = 0; relative-stable + C3-guarded definition produces 9 Class I. The strict-zero finding under literal-strict ±0 is itself the strongest validation of the structural-bias warning: even spec-anchor countries fail strict robustness under tight C1.",
    "demographic_orthogonality": "Phase 1 finding: max retirement offset ~26%; spec threshold 80%. No country meets buffer_holds. Refuted decisively at 32-country scope; 4 candidates (BA/MK/RS/TR) restated, not re-tested.",
    "s2b_only_optimism": {
      "framing": "Optimism path narrows to Climate Zone-C",
      "s2b_dependent_countries": ["AT", "LU", "TR"],
      "implication": "..."
    },
    "high_coord_archetype_split": {
      "framing": "Aggregation hides bifurcation (T34): the high-coord cluster splits into two archetypes",
      "education_admin_lift": ["NO", "IS", "DK", "LU"],
      "finance_tech_drag": ["CH", "DE", "IE", "UK"],
      "mechanism": "..."
    },
    "be_nl_squeeze_extension": "orthogonal signal confirmed (jurisdictional buffering, mechanistically independent from coordination-share displacement velocity)",
    "regime_split": {
      "growth_baseline": [...],
      "secular_stagnation_warning": [...],
      "post_growth_empirical": [...]
    },
    "capability_floor_breach": {
      "n_countries": 12,
      "list": ["DK", "DE", "SE", "NO", "BE", "UK", "IE", "NL", "LU", "IS", "CH", "LI"],
      "ceiling_reason": "ISCO 2-digit limit; 3-digit gated at Eurostat (ESS microdata path required)"
    }
  },
  "ukraine_reference_panel": {
    "status": "analytical anchor only; not corridor-mapped per spec line 341",
    "lens5_inputs_at_maxima": "...",
    "class_iv_anchor_role": "..."
  },
  "scenarios": {
    "S1": { "label": "Reinstatement Revival", "mechanism": "...", "probability_per_regime": { "growth_baseline": [0.05, 0.10, 0.18], "secular_stagnation_warning": [...], "post_growth_empirical": [...] } },
    "S2a": { ... }, "S2b": { ... }, "S3": { ... }, "S4a": { ... }, "S4b": { ... }, "S5_cascade": { ... }
  },
  "corridors": {
    "C1": { "label": "Managed Transition", "ratio_range": "<1.20", "n_countries": "..." },
    "C2": { "label": "Bifurcated Absorption", "ratio_range": "1.20–2.80", "subclusters": { "continental_corporatist": [...], "germanic_dual": [...] } },
    "C3": { "label": "Displacement Without Absorption", "ratio_range": "≥2.80", "subclusters": { "liberal_market_high": [...], "ce_med_weak_almp": [...] } }
  },
  "fragility_classes": {
    "I": { "label": "Robust (relative-stable, C3-guarded)", "rule": "...", "countries": [...] },
    "II": { ... }, "III": { ... }, "IV": { ... }
  }
}
```

This is illustrative; actual schema may evolve during composition. **Lock the final schema in `metadata.schema_version` = "1.0" once Bundle M is complete.** Document any deviations from this draft schema in the metadata block as `schema_deviations_from_draft`.

### Composition tasks

1. **Per-country composition (36 countries):** for each country, compose the full block by reading from Bundle L, J, K-2, D, Phase 1, and Phase 2 data. The Bundle L output is the canonical source for fragility_class, expected_corridor, scale_tag, etc.; Bundle J for phase3_corridor + sub-cluster; K-2 for Lens 5(c) details + breach. Phase 2 data for Lens 4/5 raw inputs (Gini, etc.). Phase 1 for lens1_ratio.
2. **Scenario distribution language** per country (Q2 baked in): for each country, generate the corridor-distribution sentence ("Likely in C2 with 60–70% mass; reaches C1 only under S2b") from the per-scenario corridor mapping + regime-conditional probabilities + 80% CIs from Bundle L. Use natural-language probability bands; do not bare-publish point estimates.
3. **Cross-cutting findings** composition (5 paragraphs): structural-bias validation, demographic orthogonality, s2b-only-optimism, high-coord archetype split, BE/NL squeeze extension. Each one references its source bundle + key data points. Length: 80–120 words each.
4. **Ukraine reference panel** (Q6 baked in): pull from Bundle D handover lines + spec line 341 + Lens 5 maxima reading. ~60 words.
5. **Scenario probability vectors** with CIs (Q2): all 7 scenarios × 3 regimes × [low_ci, mid, high_ci]. Source: Bundle L metadata.probability_vectors.
6. **Corridor sub-cluster annotations** (Q3 baked in): C2 sub-clusters from Bundle J methodology; C3 sub-clusters split into liberal_market_high (3.33–3.40) and ce_med_weak_almp (2.81–2.96).
7. **Fragility class blocks**: rule + countries + count per class (under Q1 asymmetric-guard lock).

### Constraints

- BR-19 no fabrication: every field traces to a source bundle + source field. If a field cannot be sourced cleanly, flag with `null` + `data_gap_reason`.
- BR-21 per-cell provenance: every metric has `source_bundle` + `source_field` adjacent or in a sibling `_provenance` block.
- JSON must validate cleanly (no NaN, no Infinity, all floats finite, all strings UTF-8). Test with `json.load()` round-trip.
- **Web-renderability**: Bundle O will fetch this JSON via HTTPS from the site; keep it under 2MB total to avoid loading-perf issues. If approaching cap, split into `layer-6-deliverable-data.json` (lean public version, country basics + cross-cutting + scenarios) + `layer-6-deliverable-data-detail.json` (full lens findings + provenance). Document which fields are in which file.
- Do NOT modify any Phase 1–3 outputs. Bundle M is read-only against them.
- Do NOT touch the locked spec.
- Phil does all git commits.

### Verification

Before declaring complete:
1. Class distribution in JSON matches `9 / 9 / 15 / 3`.
2. All 36 countries present in `countries` block; no nulls in `code`, `name`, `phase3_corridor`, `fragility_class`, `regime`, `scale_tag`.
3. JSON loads round-trip cleanly via `json.load()` then `json.dumps()` then `json.load()` again.
4. File size < 2MB (or if split, both files load + cross-reference correctly).
5. `scenario_distribution_language` per country uses probability-band language, not point estimates (Q2 verification).
6. `s2b_dependent` is TRUE for exactly AT/LU/TR (sentinel test).
7. Capability-floor breach list has exactly 12 countries (sentinel test).
8. Fragility-class table sums to 36 (no country missed).
9. `ukraine_reference_panel` present and tagged `not_corridor_mapped`.
10. C3 sub-clusters present (Q3 verification — sub-cluster within corridor, not 4th corridor).

### When done — report back to master session with

1. Schema version locked (1.0) + any schema_deviations_from_draft logged
2. File size (and split decision if applicable)
3. Sentinel verifications (class distribution, s2b_dependent count, breach list count, country count)
4. Top 5 fields where multiple sources had to be reconciled (and which source won + why)
5. Any composition gaps surfaced (data fields that were in spec but not in any Phase 1–3 output)
6. Recommendation for Bundle N + O readiness — both can dispatch in parallel, or one needs to wait?
7. Phase 4 next-step: which sub-bundle to dispatch first

## END PROMPT
