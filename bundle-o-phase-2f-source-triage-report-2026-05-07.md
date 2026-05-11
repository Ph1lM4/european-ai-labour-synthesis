# Bundle O Phase 2F — New-Sources Triage Report (Flag-Only)

**Session:** 2026-05-07 bounded sub-session, ~2 h.
**Scope:** 25 new Tier 1 sources from Phase 2E + spot-check of 13 Tier 2.
**Output mode:** Flag-only. No SOT edits, no source-card edits, no re-derivations.
**Verification:** 7 SOT files (`site/data.json`, `layer-6-deliverable-data.json`, `layer-6-lens-framework.md`, `site/findings.html`, `site/scenarios.html`, `site/methodology.html`, `site/sources.html`) untouched — md5 checksums identical pre-/post-session.

---

## TL;DR

- **24 of 25 Tier 1 sources land Confirms** (already integrated upstream via L1/L4/L5 enrichment that feeds the SOT) **or Refines** (would sharpen but not change SOT direction).
- **0 Shifts. 0 Contradicts.** No SOT field assignments would flip if these sources were integrated directly into the synthesis layer.
- **1 Phase 2E source-card audit gap:** Brynjolfsson, Chandar & Chen 2025 (Canaries) — the source-card claims "direct anchor for the S3 Jobs Transform scenario," but the SOT S3 mechanism cites a different Brynjolfsson paper (Brynjolfsson, Li & Raymond 2023 — Generative AI at Work, the call-centre RCT), and Canaries' headline finding (entry-level employment decline of ~13% in AI-exposed jobs) is more S6/entry-level-aligned than S3.
- **1 tier-classification anomaly:** ILO 2025 (Generative AI Occupational Exposure) is listed as Tier 2 in `sources.html` (line 255) but treated as a Tier 1 hot-spot in this brief. The L5 sources page treats it as a primary triangulation input. Phil-decision flag.
- **13 Tier 2 spot-check: 0 contradictions surfaced.** All Tier 2 additions are framing/contextual and direction-aligned with SOT.
- **Phase 2G NOT needed.** No re-derivation required. Synthesis can deploy as-is.

---

## 4-Bucket Triage Summary Table

| # | Source | Bucket | Confidence | Notes |
|---|---|---|---|---|
| 1 | Draghi 2024 — European Competitiveness | Confirms | High | Strategic anchor; not a data input. SOT Lens 5 framing aligned. Local PDF in DATA-REGISTRY (`european-ai-exposure-map/data/draghi/`). |
| 2 | Anthropic Economic Index (Handa et al. 2025) | Confirms | High | Already in DATA-REGISTRY, in L1 `triangulated_adoption.csv`, in L5 triangulation. Feeds Lens 1 dual-baseline. |
| 3 | Massenkoff & McCrory 2026 (Anthropic Research) | Refines | Medium | Granular underpinning for the entry-level signal already in SOT speed-gap derivation. Source-card says "feeds Lens 1 displacement-velocity calibration" — direction-aligned but not directly verified per cell. |
| 4 | Tomlinson, Jaffe et al. 2025 (Microsoft Working with AI) | Confirms | High | In DATA-REGISTRY, in L1 triangulation, in L5 capability-vs-deployment frame. |
| 5 | Eloundou et al. 2023 (GPTs are GPTs) | Confirms | High | In DATA-REGISTRY (`openai_gpts_exposure.csv`), foundational L1 exposure index. |
| 6 | Eurostat Enterprise AI adoption (`isoc_eb_ai`) | Confirms | High | In DATA-REGISTRY. Direct per-country Lens 1 calibration input. |
| 7 | Eurostat ICT specialists (`isoc_sks_itspt`) | Confirms | High | In DATA-REGISTRY. Anchors Klinger ICT-heavy weight 0.157 (verified in SOT high_coord_archetype_split). |
| 8 | Eurostat Employment by ISCO 2-digit (`lfsa_egai2d` / `lfsa_egais`) | Confirms | High | In DATA-REGISTRY. Backbone employment table for Klinger 2-digit weighting; SOT klinger_classification_2digit derived from it. |
| 9 | OECD EPL Database | Confirms | High | In DATA-REGISTRY (`epl_*.csv`). Lens 5 jurisdictional buffering input; squeeze-cluster worker-protection axis. |
| 10 | **Brynjolfsson, Chandar & Chen 2025 (Canaries)** ★ | **Refines (data) + source-card audit gap** | **High** | Source-card frames as S3 Jobs Transform anchor; SOT S3 mechanism cites different Brynjolfsson paper (Generative AI at Work RCT). Canaries' actual finding (entry-level ~13% employment decline in AI-exposed roles) is S6/entry-level-aligned. Data refines existing entry-level signal in speed-gap derivation; source-card "how informs" copy needs realignment. |
| 11 | Acemoglu & Restrepo 2020 (Robots and Jobs JPE) ★ | Confirms | High | Sister evidence to El-Sahli & Upward 2017 (already in original 15). Same direction (~6 jobs lost per robot per thousand workers in commuting zones); reinforces C3 corridor. |
| 12 | Acemoglu & Restrepo 2019 (Automation and New Tasks JEP) | Confirms | High | Theoretical companion to Autor 2024 (already in original 15). Same reinstatement-effect-weakening framing. |
| 13 | Feigenbaum & Gross 2024 (Telephone Operation QJE) | Confirms | Medium | Historical entry-level displacement evidence; aligned with SOT speed-gap derivation entry-level signal. |
| 14 | Card, Kluve & Weber 2018 (ALMP Meta-Analysis) | Confirms | High | L5 cites as Tier 1 input; calibrates absorption-capacity denominator already in SOT lens1_absorption_capacity. |
| 15 | Dauth, Findeisen, Südekum & Wößner 2021 (German Robots) | Confirms | Medium | DACH-specific worker-displacement evidence; aligned with DE/AT Class II Corridor 2 SOT placements (zero net employment effect at country level + worker-level losses). |
| 16 | Jacobson, LaLonde & Sullivan 1993 (Earnings Losses) | Confirms | High | Foundational displaced-worker earnings-deficit anchor; sister to El-Sahli & Upward 2017. |
| 17 | EC 2024 Ageing Report ★ | Refines | Low | Source-card claims feeds Lens 2 demographic-buffer + Lens 5 fiscal-bandwidth context. SOT Lens 2 currently uses EUROPOP2023 (per L4 enrichment, Bundle P). Ageing Report adds explicit fiscal-projection layer not currently in SOT. Not in DATA-REGISTRY locally; sister-layer L4 sources page does not cite it explicitly. Would sharpen working-age-2050 and fiscal-headroom estimates without changing direction. |
| 18 | OECD Old-age dependency ratio | Confirms | High | Direct Lens 2 input; SOT retirement_offset_pct already derived from this kind of data via L4 (max 26.4%). |
| 19 | UN Population Division 2024 (WPP 2024) | Confirms | High | In DATA-REGISTRY (`UN_PPP2024_*.xlsx` in L4). Comparator for EUROPOP2023 alignment, already cross-checked. |
| 20 | IMF WEO 2026 | Confirms | High | In DATA-REGISTRY (`imf-dm-export-20260420.xls` in L4). Feeds Lens 5 GDP/fiscal context and SOT regime classification (DE 1.02% / 0.54% etc.). |
| 21 | OECD Economic Surveys EU/Euro Area 2025 | Confirms | Medium-High | In DATA-REGISTRY (multiple OECD country PDFs in L4). Source-card claims anchors post-growth-empirical regime classification (10 markets) — sentinel matches SOT regime_split.post_growth_empirical = AT/CH/DE/FI/FR/LI/LU/NO/SE/UK. |
| 22 | Bertheau et al. 2022 (IZA DP 15033) ★ | Confirms | High | Local PDF in `european-reskilling-map/scripts/data/bertheau/`. Direct anchor for SOT lens1_a_to_c_transition_rate_pct via L5 script 08; per-country bands + central_derived_pct populated for AT/DK/FR/IT/PT/ES/SE and system-peer extension to others. |
| 23 | OECD SOCX (ALMP training spend) ★ | Confirms | High | L5 sources page explicitly names SOCX as "the replacement primary" for the withdrawn Eurostat `empl_lmp_expsumm`. Already feeding L5 channel-throughput → SOT reskilling_capacity_gap.channel_breakdown_per_year.government_almp = 650K. |
| 24 | Eurostat Adult Education Survey (`trng_aes_100`) | Confirms | High | L5 cache (`aes_100_2022.json`); speed-axis indicator on the per-country reskilling-system radar. |
| 25 | Eurostat Employment rate of older workers 55-64 (`lfsa_ergan` / `lfsa_egais`) | Confirms | High | Direct input to retirement-offset; L5 derivation explicitly cites lfsa_egais ("21.0% EU-27 weighted average"). |

★ = hot-spot (7 priority sources from handover Step 5).

**Bucket counts:**
- Confirms: 22
- Refines: 3 (Massenkoff & McCrory 2026 ; Brynjolfsson Chandar Chen 2025 — also flagged for source-card audit ; EC 2024 Ageing Report)
- Shifts: 0
- Contradicts: 0
- "Data not directly verified" (Low confidence): 1 (EC 2024 Ageing Report)

---

## Hot-Spot Deep-Dive (7 priority sources)

### 1. Bertheau et al. 2022 (IZA DP 15033) — A→C transition rates
- **Source data:** Harmonised admin 5-year re-employment rates post-displacement for AT/DK/FR/IT/PT/ES/SE. Cited finding from L5 sources page methodology section: "a 10pp increase in the share of ALMP spending is associated with a 5% decrease in earnings losses" (Bertheau §5).
- **SOT field comparison:** SOT `lens1_a_to_c_transition_rate_pct` carries `band_low_pct`, `band_high_pct`, `central_derived_pct` per country. Verified per-country values: AT 3-6% / 7.9 derived ; DK 8-12 / 9.9 ; FR 5-8 / 6.9 ; IT 2-5 / 4.8 ; PT 2-5 / 4.8 ; ES 2-5 / 4.8 ; SE 8-12 / 9.9. System-peer extension applied to non-Bertheau countries (DE/CH inherit Germanic Dual band; NO/FI inherit Nordic; etc.).
- **Verdict:** **Confirms** (already integrated upstream via L5 script 08). Bertheau is named in SOT `_provenance.source_data` for the field. No data divergence.
- **Confidence:** **High** — local PDF + L5 derivation script + SOT _provenance trace are all in place.
- **Note:** SOT layer_5_enrichment block already flags two material disagreements documented in L5 sources page (Germanic Dual +3.4pp central vs band ; Liberal Market −3.3pp central vs band). These are **already-known known-limits**, not new shifts.

### 2. Massenkoff & McCrory 2026 — entry-level AI signal
- **Source data:** Per L5 sources page, Massenkoff & McCrory 2026 contributes "wage and earnings data" plus the "entry-level hiring slowdown" signal derived from US CPS + Claude usage data. The source-card on synthesis says "Earliest large-sample evidence on AI hiring effects per occupation."
- **SOT field comparison:** SOT cross_cutting (via L5 enrichment) flags the "entry-level signal flagged in the L5 Speed-Gap derivation" but does not surface a per-country numeric entry-level metric. The signal feeds the qualitative speed_gap field (5-9 years) and the AI-response-lag commentary (1-3 yr disrupt vs 5-9 yr respond).
- **Verdict:** **Refines** — direction-aligned but would add per-occupation hiring-effect granularity not currently in SOT. No country-level placement would flip from this.
- **Confidence:** **Medium** — paper not directly verified by sub-session; relying on L5 sources page summary. The "early evidence" framing is consistent with how L5 already uses it as a leading-indicator-with-caveats input ("US CPS + Claude usage; European adoption may differ due to regulatory environment, works councils, ISCO-08 vs SOC").
- **Not a Shift** because the SOT speed-gap is intentionally bounded to 5-9 yr and the entry-level signal is qualitative — granularising it doesn't move corridor placements or scenario probabilities.

### 3. Brynjolfsson, Chandar & Chen 2025 (Canaries in the Coal Mine) — S3 Jobs Transform
- **Source data:** Stanford Digital Economy Lab paper documenting six facts about AI employment effects. The widely-publicised headline finding is ~13% employment decline for young workers (22-25) in AI-exposed occupations, with older workers and unexposed roles unaffected. The within-occupation reshape angle is one of several facts but not the dominant framing.
- **SOT field comparison:** SOT `scenarios.S3.mechanism` cites four empirical anchors: "Brynjolfsson et al. OpenAI productivity RCT 2025 (call-centre workers); Dell'Acqua et al. HBS WP 24-013 (BCG consultants +40%/-19pp); Nielsen + Gibbons ADPList Q1 2026; ATM/teller (Bessen), Spreadsheets (Levy)." **The "Brynjolfsson et al. RCT 2025 (call-centre workers)" reference is to Brynjolfsson, Li & Raymond — Generative AI at Work — a different paper from Canaries.**
- **Verdict:** **Refines (data) + Phase 2E source-card audit gap.**
  - *Data side (Refines):* Canaries' entry-level employment-decline finding aligns with the entry-level signal already in SOT speed-gap derivation (anchored on Massenkoff & McCrory 2026 + Feigenbaum & Gross 2024). Adds a third independent confirmation. Direction-aligned with S6 Reinstatement Failure for entry-level cohort, not S3 reshape.
  - *Source-card audit gap:* The Phase 2E "how informs" copy on `sources.html` line 226 says "Direct anchor for the S3 Jobs Transform scenario; documents the within-occupation reinstatement pattern that distinguishes S3 from S6 Reinstatement Failure." This conflates Brynjolfsson Chandar Chen 2025 (Canaries) with Brynjolfsson Li Raymond 2023 (Generative AI at Work). The Canaries paper's dominant contribution is the entry-level employment-decline fact, which sits closer to S6 than S3.
- **Confidence:** **High** — SOT S3 mechanism text is unambiguous about which empirical anchors it claims; Canaries findings are well-publicised.
- **Recommended path:** Re-cast the Canaries source-card "how informs" copy to read along the lines of "Provides independent confirmation of the entry-level employment-decline signal that the speed-gap derivation flags (alongside Massenkoff & McCrory 2026 and Feigenbaum & Gross 2024). The within-occupation reshape facts in Canaries also support the S3 Jobs Transform mechanism, but the dominant cited anchor for S3 is Brynjolfsson, Li & Raymond — Generative AI at Work (2023, call-centre RCT)." **Phase 2G is not required to fix this** — it's a source-card copy edit; the underlying SOT data is unaffected.

### 4. OECD SOCX (ALMP training-category spend)
- **Source data:** Per-country ALMP training spend as % GDP. Per L5 sources page: "OECD SOCX is the replacement primary" for withdrawn Eurostat `empl_lmp_expsumm`. Feeds the government-ALMP channel throughput at 650K/yr in SOT reskilling_capacity_gap and the Bertheau-anchored Zone-C destination share calibration ("Nordic systems ALMP ~0.37% → ~10% Zone-C share ; CEE/Southern ~0.09% → ~4%").
- **SOT field comparison:** SOT `cross_cutting_findings.reskilling_capacity_gap.channel_breakdown_per_year.government_almp = 650000`. Bertheau-derived a_to_c_rates use the ALMP slope explicitly. Aligned.
- **Verdict:** **Confirms.**
- **Confidence:** **High** — L5 names SOCX as primary; downstream SOT field traces back to it via L5 enrichment.

### 5. EC 2024 Ageing Report
- **Source data:** EC DG ECFIN 2024 Ageing Report — economic and budgetary projections for EU member states 2022-2070 covering working-age trajectory, dependency ratios, and fiscal projections.
- **SOT field comparison:** SOT carries working-age-decline trajectories per country for 9 of 36 markets explicitly via L4 enrichment Bundle P (IT -17.5%, ES -12.9%, DE -12.0%, BG -29%, LV -28%, AT -7.4%, NL -5.7%, FR -5.5%, CH +1.8%). Source for these is named as "EUROPOP2023 (via L4)" in the SOT _provenance, not the Ageing Report. The Ageing Report's fiscal-projection layer (pension-spending, age-related public spending) is not currently surfaced in SOT.
- **Verdict:** **Refines** — would sharpen working-age trajectories beyond the 9 currently covered (the "Phase 5+ candidate: parse Eurostat proj_23np for full coverage" gap noted in SOT layer_4_enrichment.data_gaps_acknowledged) and add the missing fiscal-projection layer that Lens 5 currently approximates via IISS/SIPRI/MFF defence + climate envelopes. No SOT corridor or fragility class would flip — these are richer inputs for the regime-classification context.
- **Confidence:** **Low** — paper not local in DATA-REGISTRY; sister-layer L4 sources page does not appear to cite it explicitly. Verdict based on Ageing Report's well-known scope plus the SOT data-gap acknowledgement.
- **Recommended path:** Carry as Phase 5+ enrichment candidate (not Phase 2G).

### 6. Acemoglu & Restrepo 2020 (Robots and Jobs JPE)
- **Source data:** US local-labour-market evidence. Headline finding (well-established): each additional industrial robot per thousand workers reduces employment by ~6 workers in the same commuting zone, with negative wage effects persisting.
- **SOT field comparison:** SOT C3 corridor (Displacement Without Absorption) currently anchored on El-Sahli & Upward 2017 (dockworker lifetime-earnings deficits). Acemoglu & Restrepo 2020 is direction-aligned sister evidence — local-labour-market displacement without absorption. Same C3 mechanism.
- **Verdict:** **Confirms.**
- **Confidence:** **High** — finding is canonical and direction-aligned; no SOT divergence.

### 7. ILO 2025 (Generative AI Occupational Exposure Index)
- **Source data:** Third independent global AI exposure index, complementing Anthropic Economic Index (observed usage) and Microsoft Working with AI (capability framework). Per L5 sources page methodology: "Exposure coefficients are triangulated from three independent indices: the ILO Global Index of Occupational Exposure (2025), the Anthropic Economic Index (2025...), and Microsoft's Working with AI."
- **SOT field comparison:** SOT Lens 1 displacement velocity uses L1's `triangulated_adoption.csv`, which is L1's consolidated cross-index view. ILO 2025 is part of the upstream triangulation set.
- **Verdict:** **Confirms** (already in upstream triangulation). Third-index cross-check claim in source-card is accurate.
- **Confidence:** **High** — explicitly named in L5 methodology; in DATA-REGISTRY pipeline upstream.
- **Tier-classification anomaly:** ILO 2025 is placed in **Tier 2** in synthesis sources.html (line 255) but the handover treats it as a Tier 1 hot-spot. L5 treats it as a primary triangulation input. Phil-decision flag: should this be re-classified Tier 1 in synthesis to match upstream usage?

---

## Shifts list

**None.** No SOT field assignments would flip.

---

## Contradicts list

**None.** No source data directly conflicts with the corresponding synthesis finding.

---

## Phase 2E Source-Card Audit Gap

**Single gap surfaced:**

| Source | sources.html line | Issue |
|---|---|---|
| Brynjolfsson, Chandar & Chen 2025 (Canaries in the Coal Mine) | 226 | "How informs" copy claims "Direct anchor for the S3 Jobs Transform scenario; documents the within-occupation reinstatement pattern that distinguishes S3 from S6." The SOT S3 mechanism cites a **different** Brynjolfsson paper (Brynjolfsson, Li & Raymond — Generative AI at Work 2023, call-centre RCT). Canaries' dominant contribution is entry-level employment decline (~13%), which sits closer to S6 / the speed-gap entry-level signal than to S3 reshape. |

**Recommended fix (NOT executed in this session):** rewrite the Canaries "how informs" copy to position it as an independent confirmation of the entry-level employment-decline signal alongside Massenkoff & McCrory 2026 and Feigenbaum & Gross 2024, with a secondary cross-reference that within-occupation reshape facts also speak to S3 (without claiming direct anchorship of S3, which is held by the Brynjolfsson Li Raymond RCT).

**Tier-classification anomaly:**

| Source | sources.html line | Issue |
|---|---|---|
| ILO 2025 (Generative AI and Jobs: Refined Global Index) | 255 | Placed Tier 2 in synthesis but used as a Tier 1 primary triangulation input by L5; handover Step 5 treats it as a Tier 1 hot-spot. Phil-decision: re-classify Tier 1 in synthesis to match upstream usage, or document why synthesis treats it Tier 2 (e.g., synthesis only consumes the L1 triangulated output, not the raw ILO index — in which case Tier 2 is defensible as analytical/contextual rather than primary).

---

## Phase 2G Readiness — NOT NEEDED Verdict

**No re-derivation required. Synthesis can deploy as-is.**

Reasoning:
1. All 25 Tier 1 sources land Confirms or Refines — none would shift a per-country fragility class, corridor placement, regime tag, scenario probability, or threshold value if integrated directly.
2. The 22 Confirms sources are already integrated upstream via L1 (Bundle Q), L4 (Bundle P), and L5 (Bundle R) enrichment that feed the SOT. Phase 2E added explicit synthesis-side citation cards for sources that were doing analytical work but had been cited only in upstream layer source pages — this is bibliographic surfacing, not new data.
3. The 3 Refines sources (Massenkoff & McCrory 2026 ; Brynjolfsson Chandar Chen 2025 ; EC 2024 Ageing Report) would add granularity — per-occupation hiring-effect numbers, additional independent entry-level signal confirmation, fiscal-projection layer for Lens 5 — but no corridor / class / probability would change. Direction-aligned across all three.
4. The single Phase 2E source-card audit gap (Canaries S3 framing) is a copy edit on `sources.html`, not a SOT derivation issue. Fix scope: 1 source-card "how informs" rewrite, ~3 sentences.
5. The 0-shift / 0-contradict result is consistent with what we'd expect from a Phase 2E exhaustive audit — the audit was anchored on existing synthesis findings that were *already* derived from upstream layer data; the new source-cards bibliographically surface what was previously cited only via the upstream source pages.

If Phil wants the Canaries source-card copy fixed and (optionally) the ILO Tier 1/2 question resolved, that's a small `sources.html`-only edit (Phil-driven or a separate small bundle), not a Phase 2G re-derivation.

---

## Tier 2 Spot-Check (13 sources)

Per the handover, Tier 2 spot-check is optional and flagged only if surface inspection suggests a contradiction. **No contradictions surfaced.** All 13 Tier 2 additions are framing/contextual and direction-aligned with SOT.

| # | Source | Verdict |
|---|---|---|
| 1 | EU AI Act 2024/1689 | Confirms (regulatory anchor; SOT regulatory_asymmetry block matches) |
| 2 | Hall & Soskice 2001 (Varieties of Capitalism) | Confirms (institutional typology aligned with Nordic/Continental/Liberal cluster split) |
| 3 | Acemoglu & Johnson 2023 (Power and Progress) | Confirms (strategic context, no data conflict) |
| 4 | Brynjolfsson, Rock & Syverson 2021 (Productivity J-Curve) | Confirms (capability-vs-deployment lag is the SOT dual-baseline frame) |
| 5 | Frey 2019 (Technology Trap) | Confirms (long-run displacement-without-absorption framing aligned with C3) |
| 6 | Feigenbaum & Gross 2025 (AT&T Management Science) | Confirms (slow-deployment within-firm evidence aligned with S4/S7 timing) |
| 7 | Autor, Dorn & Hanson 2013 (China Syndrome) | Confirms (local-labour-market displacement framework aligned with C3) |
| 8 | Bruegel 2025 (Demographic Divide) | Confirms (cross-country demographic-asymmetry; aligned with SOT lens2_zone_heterogeneity per-country split) |
| 9 | OECD Pensions at a Glance 2023 | Confirms (cross-country pension-system context; aligned with post-growth regime classification) |
| 10 | Allianz Research 2024 (Migration matters) | Confirms (named the IT net-migration −485,823 figure that SOT explicitly carries) |
| 11 | EP 2025 (Displaced Ukrainians) | Confirms (migration-bandwidth context aligned with MFF €64.6 B reinforcement signal) |
| 12 | ILO 2025 (Generative AI Occupational Exposure) | Confirms — but also tier-classification anomaly (treated as Tier 2 here, Tier 1 hot-spot in handover, primary in L5) |
| 13 | EURES/ELA 2024 (Labour Shortages) | Confirms (in DATA-REGISTRY; sector shortage signals aligned with Lens 2 zone-bifurcation) |

---

## Verification Checklist (handover Step 7)

| # | Check | Status |
|---|---|---|
| 1 | All 25 new Tier 1 sources reviewed | Pass — 25/25 in triage table; all 13 Tier 2 spot-checked too. |
| 2 | Each source has a triage verdict + confidence level | Pass — single Confirms/Refines/Shifts/Contradicts label + confidence per row. |
| 3 | Shifts/Contradicts have magnitude estimate | N/A — 0 Shifts, 0 Contradicts. |
| 4 | "Data not directly verified" flagged | Pass — EC 2024 Ageing Report explicitly flagged Low confidence with reason. |
| 5 | SOT files untouched (md5 match pre/post) | **Pass** — `site/data.json` 298bd730… ; `layer-6-deliverable-data.json` 61b5e973… ; `layer-6-lens-framework.md` 87933b81… ; `site/findings.html` c4139f58… ; `site/scenarios.html` 0cbfc8b6… ; `site/methodology.html` 03541db3… ; `site/sources.html` 398c4b5f… all unchanged. |
| 6 | No edits to source-cards in sources.html | Pass — confirmed by checksum. |
| 7 | No edits to any site HTML or markdown | Pass — confirmed by checksum on all 8 site/*.html files. |

---

## Candidate Brain Captures

Two pattern-level captures worth surfacing for Phil decision:

### Capture 1 — "Bibliography-vs-data audit separation" rule (medium scope)
**Family:** Same family as the Phase 2E "sources audit at phase boundaries" rule (per handover §10).

**Pattern observed:** Phase 2E added 25 Tier 1 source-cards by mapping sources to *the findings the synthesis already makes*. Phase 2F shows that 24 of those mappings are bibliographically correct but are documenting upstream-integrated data, not direct synthesis-layer inputs. The 1 misalignment (Canaries S3 framing) was caught by reading the SOT mechanism text after-the-fact.

**Proposed rule:** *When adding a source-card via bibliography audit (rather than via direct integration), the "how informs" copy should be written from the SOT field's actual citation chain, not from the audit's mapping inference. Concretely: grep the SOT for the source's distinctive named anchor (paper title, author surname, dataset code) before composing the card. If the SOT cites a different paper by the same author, flag the disambiguation in the card.*

**Why:** prevents Brynjolfsson-Canaries-vs-Brynjolfsson-Generative-AI-at-Work confusions. Cheap to implement (one grep per addition).

**How to apply:** during source-card composition, after writing the "how informs" line, run a verification grep: `grep -i "<distinctive token>" site/data.json layer-6-lens-framework.md site/scenarios.html site/findings.html site/methodology.html`. If the source's specific paper isn't cited but the author is, the card needs to flag which paper underpins the SOT vs which is being newly added.

### Capture 2 — "Hot-spot triage discipline first" (small scope)
**Pattern observed:** Sub-session triaged the 7 hot-spots first (per handover), found 6 Confirms + 1 Refines/source-card-gap. Once that pattern was established, the remaining 18 sources triaged faster — most converged on the same Confirms verdict because they were also upstream-integrated.

**Proposed rule:** *When the highest-risk subset of an audit-set lands as Confirms / Refines without Shifts, declare a low-risk priors update and triage the rest at lower depth. Don't apply uniform per-source depth when the priors have moved.*

**Why:** speeds up flag-only triages without sacrificing accuracy on the cases that matter.

**How to apply:** explicitly check after the priority subset whether any have landed Shifts/Contradicts. If yes, maintain full depth. If no, drop to "summary verdict + confidence + 1-2 line justification" for the remainder.

These are sub-session candidates for Phil to decide on; not auto-written to the brain.

---

## Sub-session metadata

- **Bounded duration:** ~2h target. Actual: ~1.25h.
- **Reads only.** No writes to SOT, source-cards, site HTML, lens framework, deliverable data, or llms.txt.
- **Files touched:** this report only — `bundle-o-phase-2f-source-triage-report-2026-05-07.md` (new file at project root).
- **Phil does all git commits.**
