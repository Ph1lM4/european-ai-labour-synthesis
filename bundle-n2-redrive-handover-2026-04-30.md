# Handover Prompt — N2 Re-Derivation: Unified Editorial Pass + P/Q/R Enrichment + Squeeze Reconciliation

Bounded composition session. Re-derives all N2 outputs (Executive + One-Pager + Einfache EN/DE + Glossary) + Specialist Appendix targeted edits + Lens framework spec light updates, absorbing three SOT enrichments (Bundles P/Q/R) + a Phil-locked editorial-pass batch + the squeeze-flag reconciliation. ~150–180 min.

---

## Context

Phase 4 deliverable surface needs unified re-derivation. Three SOT enrichments shipped (Bundles P/Q/R, all reported back, all 7/7 verifications passed). One reconciliation locked (squeeze-flag 8-country set with Nordic + Continental two-sub-cluster decomposition). One editorial-pass batch locked (multiple Phil-iterated drafts, Phil-corrected register, "Part 7" public-facing convention, ESCO/ISCO fix, terminology consistency, framing-assumption disclaimers).

This is composition, not analysis. All locks are upstream; the sub-session integrates them into the deliverable surface.

---

## START PROMPT

I need you to re-derive the Layer 6 N2 deliverable surface (Executive + One-Pager + Einfache EN/DE + Glossary) plus targeted edits to the Specialist Appendix and Lens framework spec, integrating three SOT enrichments + an editorial-pass batch + a squeeze-flag reconciliation.

This is NOT re-computation. The SOT JSON is the authoritative state; every numeric claim traces to it.

### Read FIRST (absolute paths)

**Authoritative state:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON post-P/Q/R enrichment. Schema v1.0 still locked; sub-fields enriched per Bundles P/Q/R.

**Existing N2 outputs to update:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-executive.md` — Executive Edition (current 1,869 words; will grow ~200–400 words)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-onepager.md` — One-Pager (current 600 words; target ~700)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-einfache-en.md` and `-de.md` — Einfache versions (~1,000 words each)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-glossary-draft.tsv` — glossary (33 terms; will add ~10)

**Existing artefacts to lightly update:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document.md` — Specialist Appendix; targeted edits to §4.5 (squeeze reconciliation), §2 Lens 1 + Lens 4 + Lens 5 (enrichment integration), §4 Class III (7.55M math)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — Lens spec; add Lens 1 `lens1_a_to_c_transition_rate_pct` + `lens1_regulated_absorption_pct` schema; Lens 5 `lens5_internal_transition_diagnostic` schema

**Bundle reports for context:**
- `bundle-p-l4-demographics-enrichment-handover-2026-04-30.md` + report-back in master-session conversation
- `bundle-q-l1-regulatory-overlay-handover-2026-04-30.md` + report-back
- `bundle-r-l5-reskilling-math-handover-2026-04-30.md` + report-back

**Anti-slop reference:**
- `/Users/philippmaul/Documents/second-brain/skills/linkedin-playbook/references/banned-phrases.md` — Tier 1, 2, 3 scan as sentinel.

### What's changing — three sources

#### Source 1: SOT enrichment from Bundles P/Q/R

**Bundle P (Layer 4 demographics → Lens 2):**
- Per-country `lens2_demographic_buffer` object (32/36 with retirement_offset_pct; 4 candidate countries null)
- Retirement-offset range: 20.4% (IE/SE) to 26.4% (BG/EL/HR/LT/LV/MT/PL/PT/RO)
- Working-age decline 2050: 8 explicit values (BG −29%, LV −28%, IT −17.5%, ES −12.9%, DE −12.0%, AT −7.4%, NL −5.7%, FR −5.5%, CH +1.8%)
- **Italy load-bearing finding: −485,823 net migration in 2025 (negative)** — only major EU economy with negative net migration
- Net-migration explicit for 7 countries (DE +517K, AT +50K, CH +83K, FR +201K, IT −486K, ES +593K, NL +107K), 29 gap-flagged for Phase 5+
- Top-level `cross_cutting_findings.lens2_zone_heterogeneity` summarises Zone A (clerical, AI substitutes well, retirement low → compounding mismatch) vs Zone C (healthcare/trades/care, AI doesn't substitute, retirement high → unfillable shortage / negative buffer)
- DACH-specific: 163 Engpassberufe, 82% Austrian shortage rate, 34.4% Swiss foreign workforce

**Bundle Q (Layer 1 regulatory overlay → Lens 1 + Lens 4):**
- Per-country `lens1_regulated_absorption_pct` (range 0.46–0.68; **stronger Lens 1 differentiator than asymmetry**)
- Per-country `squeeze_flag.asymmetry_score` (range 0.6333–0.6650; tight 0.0317 span; weak differentiator)
- Per-country `squeeze_flag` upgraded boolean → object
- AI Act overlay counts for the 8 squeeze countries (Annex III: 40, Art 26(7): 121–124, PWD: 29–31)
- **Caveat: Art 26(7) is universal scope in L1 data → collapses to country employment-coverage, not a differentiated overlay surface.** Use Annex III + PWD as the load-bearing two-axis quantification; relegate Art 26(7) to a methodology footnote.
- Top-level `cross_cutting_findings.regulatory_asymmetry` summary
- LI null with documented `data_gap_reason` (excluded from L1 dataset)

**Bundle R (Layer 5 reskilling → Lens 1 + §3 + Lens 5):**
- Per-country `lens1_a_to_c_transition_rate_pct` keyed off `_system_p1`:
  - Nordic flexicurity (5 countries): 8–12% headline / 9.9% derived central
  - Continental Corporatist (4): 5–8% / 6.9%
  - Liberal Market (2 — IE/UK): 5–8% headline / **3.2% derived central** (L5 publishes derived as canonical for UK; Δ=−3.3pp)
  - Germanic Dual (4): 3–6% headline / 7.9% derived (Δ=+3.4pp; reform-velocity composite is country-specific; DE rv=5, AT rv=3, CH rv=1)
  - Southern European (6): 2–5% / 4.8%
  - Central/Eastern European (11): 2–5% / 3.3%
  - Candidate-baseline (4 — BA/MK/RS/TR): 2–5% / 3.5%
- DACH country-specific: time-to-first-graduate years (DE 4.5 / AT 3.5 / CH 3.0); public-cost-per-transition €k (DE 38 / AT 28 / CH 18)
- **Top-level `cross_cutting_findings.reskilling_capacity_gap`: 7.55M deep-reskilling need / 3.34M annual throughput / ~450K net new / 15-year backlog / 5–9-year speed gap**
- Internal-transition diagnostic: framework only at L5 (no country data); all 36 countries `value: null` with framework citation + BR-22 Haslauer thread provenance + Phase 5+ acquisition pointer. **Top-level `cross_cutting_findings.internal_transition_diagnostic_framework`** carries the framework for downstream use as interpretive lens.

#### Source 2: Editorial-pass batch (Phil-locked)

**§Prelude — light polish (already locked):**

```markdown
**Europe's AI Labour Map Experiment — What Survives the Stress Test**

**Prelude**

Forecasts of how AI will reshape European jobs come in three flavours: vendor reports tied to compute spending (often US-centric), macro projections that assume yesterday's patterns repeat, and political messaging anchored to promises that land unevenly. Few ask what happens if the "old jobs disappear, new jobs appear" mechanism weakens, ageing fails to absorb displacement, and institutions are stretched by defence, decoupling, climate, and the war in Ukraine.

So we ran an experiment. We scored 36 labour markets — the EU-27 plus EFTA, the United Kingdom, and four candidate countries — across five lenses, and stress-tested them under seven *what-if* scenarios. The results group into three corridors and four fragility classes. This brief walks through the headline map, lens findings, regime-weighted scenario probabilities, country profiles, and what the framework cannot see.
```

**§What Survives — terminology consistency + drop trailing Part 7 pointer (Option A locked):**

The silver-lining paragraph: replace `ALMP🛈 capacity, reskilling investment, EU budget allocation, regulatory choices, and fiscal headroom` with `job-training capacity, reskilling, (EU) funding choices, regulation, and fiscal headroom`. Drop the ALMP🛈 tooltip from this section (it stays in the glossary entry; first-occurrence in §2 is enough).

End §What Survives with: *"This sets the frame. The remainder of the brief explains where each country lands and why."* Drop the trailing *"What can be done comes in a separate document — Layer 7 of this project, scoped separately."* — §6 carries the Part 7 closer at full weight.

**§2 The Five Lenses — full register pass + framing-assumption disclaimer (locked v3):**

```markdown
## §2 The Five Lenses, Briefly

We chose these five lenses because they capture the main forces at play, and Parts 1–4 of this project provide most of the underlying evidence. Other framings would also work.

Lens 1 asks how fast jobs get disrupted versus how well the country can help displaced workers find new work. The ratio defines corridor placement. Below 1.20: *Managed Transition* (C1). Above 2.80: *Displacement Without Absorption* (C3). Between: *Bifurcated Absorption* (C2) — partial coping, uneven across sectors. Five Nordic markets clear the lower threshold. Fifteen sit above the upper one. *[INTEGRATE: A→C transition rate per institutional system from R; lens1_regulated_absorption_pct from Q as the stronger differentiator — range 0.46–0.68 is the Lens 1 signal that makes corridor placement quantitatively defensible per country.]*

Lens 2 asks whether retirements create enough openings to absorb workers displaced by AI. The threshold: retirement offset above 80 % of the displaceable cohort. Across 32 scored countries, the highest reading was about 26 %. Zero countries cleared the threshold. The "silver-lining ageing" argument fails empirically across all 36 markets, with strikingly little variance between regimes. *[INTEGRATE: Zone A vs Zone C heterogeneity — buffer fails worst in Zone C (healthcare/trades) where AI doesn't substitute, creating a compounding labour shortage rather than offsetting one. Italy −485K net migration as the load-bearing dramatic finding. 8 deep-dive countries with explicit working-age 2050 trajectories.]*

Lens 3 asks whether AI exposure registers as a jobs-volume problem, an inequality problem, or both. Each country is tagged accordingly: *aggregate*, *distributional*, or *both*. The tag points to which kind of policy response fits.

Lens 4 asks whether overlapping crises — defence, climate, decoupling, Ukraine — could cause extra strain on top of the AI exposure base. It also flags a separate signal: a jurisdictional squeeze. *[REPLACE: was "Five countries (BE/DE/FR/LU/NL)..." → 8-country two-sub-cluster framing — see Squeeze Reconciliation below.]*

Lens 5 asks whether the country's industry mix makes coordination harder when AI displaces workers — and tests where institutional capacity starts to break. Twelve countries fail this test: BE, CH, DE, DK, IE, IS, LI, LU, NL, NO, SE, UK. This is the cluster where the bifurcation finding in §4 bites hardest. (Methodology: Klinger coordination-share weighting at 2-digit ISCO, with ESCO occupation counts for the aggregation — see Specialist Appendix.) *[INTEGRATE: Internal-transition-vs-external-turnover diagnostic framework from R as a Lens 5 interpretive lens; country-data gap-flagged for Phase 5+.]*
```

**§3 Seven Scenarios — spectrum framing + framing-assumption disclaimer (locked v3):**

```markdown
## §3 Seven Scenarios, Three Economic Regimes

We tested seven *what-if* futures, arranged along an optimism-pessimism spectrum — our framing assumption, not a definitive taxonomy. These are five chosen views of how the next decade could unfold; other plausible futures would land between these positions, or outside the spectrum entirely.

- **Uber-optimistic — Reinstatement Revival** (S1). The historical "old jobs disappear, new jobs appear" pattern fully holds; new jobs replace old at the historical rate.
- **Optimistic — Climate Adaptation Boom** (S2b). Sectoral activity redirects into climate-adaptation work; new demand absorbs displacement.
- **Middle — Muddle Through** (S3). Only attrition and partial reabsorption; no sharp pattern either way.
- **Pessimistic — Wage Cliff** (S2a). AI substitutes for mid-skill labour; wages compress.
- **Pessimistic — Breakdown** (S4, two flavours): *Reinstatement Failure* (S4a) — the historical pattern weakens further, per Autor et al. 2024; *Bandwidth Fracture* (S4b) — training and re-employment systems collapse under parallel-crisis overstretch.

The orthogonal seventh — **Concurrent-Crisis Cascade** (S5) — sits outside the spectrum: defence, EU-budget strain, and migration combine to overwhelm institutional capacity simultaneously.

Three economic *weather patterns* group countries differently. **Growth-baseline** — 24 markets, including the four candidate countries — treats Reinstatement Revival as the central recovery channel; the historical pattern still holds. **Secular-stagnation-warning** — Greece and Italy — assigns more mass to Muddle Through and to Breakdown; the historical pattern is already faltering. **Post-growth-empirical** — Austria, Switzerland, Germany, Finland, France, Liechtenstein, Luxembourg, Norway, Sweden, the United Kingdom — treats Reinstatement Revival as structurally weaker because aggregate output is no longer expanding to support reinstatement.

The weather pattern changes which *what-if* future is most likely. Under post-growth, the most probable routine path is not Muddle Through but **Climate Adaptation Boom**: probability 0.30 against 0.25 for Muddle Through and 0.05 for Reinstatement Revival. The optimism path runs through climate-adaptation work, not tech-led job creation. The Concurrent-Crisis Cascade probability also rises with weather-pattern severity: from 0.05 in growth-baseline to 0.10 in stagnation to 0.15 in post-growth. Probability bands use IPCC AR6 likelihood-scale language. Per-country distribution sentences quote corridor mass ranges rather than single point estimates — the precision stays honest.

*[INTEGRATE from Bundle R: 7.55M deep-reskilling need / ~450K annual net new / 15-year backlog / 5–9-year AI-vs-system speed gap as the load-bearing empirical anchor for Class III "reskilling pathway is structurally insufficient" framing — render as a short paragraph or sidebar after the regime overlay.]*
```

**§4 Country Profiles — full register pass + traffic-light opener + squeeze reconciliation + T34 reference removal (locked v3 + reconciliation):**

```markdown
## §4 Country Profiles by Class

Think of this as a traffic-light reading of 36 countries. Nine look relatively sturdy — but only under a softer rule. Nine are one shock away from breaking. Fifteen are already in bad shape under business-as-usual. Three show warning signs of cascading institutional overload. Each class profile below names the countries, the mechanism, and the load-bearing scenario sensitivity.

**Class I — Robust (9 countries).** Five Nordic markets (Denmark, Finland, Iceland, Norway, Sweden) and four Continental peers (Belgium, France, Luxembourg, Netherlands). The Nordics anchor the cluster on Lens 1: their training and re-employment capacity absorbs displacement at ratios where the corridor edge sits — Nordic A→C transition rates land at 9.9% derived central (8–12% institutional band), well above any other system. The four Continental markets reach the *Managed Transition* corridor under three of the six routine variants and never land in the worst corridor under routine perturbation. Sweden is flagged knife-edge (medium confidence). One caveat: Class I is conditional on the rule applied. Under a literal-strict reading — no scenario produces a worse outcome — the count drops to zero. Robustness is conditional, not unconditional.

**Class II — Fragile (9 countries).** Austria, Bosnia and Herzegovina, Bulgaria, Switzerland, Germany, Spain, Liechtenstein, Latvia, Romania. Baselines sit in C2 (*Bifurcated Absorption*); one or more routine variants push them to C3 (typically S4a or S4b). Seven of these — BG, CH, DE, ES, LI, LV, RO — were reclassified out of Class I when the rule tightened: their baseline is stable but a single routine variant pushes them into the worst corridor, which is inconsistent with "Robust." Austria carries an additional flag — *Climate Adaptation Boom-dependent* (S2b in the technical schema) — alongside Luxembourg (Class I) and Turkey (Class IV). For these three, the only routine path to *Managed Transition* runs through S2b. All other routine variants yield C2 or worse.

**Class III — Pre-Failure Risk (15 countries).** Cyprus, Czechia, Estonia, Greece, Croatia, Hungary, Ireland, Italy, Lithuania, Malta, Poland, Portugal, Slovenia, Slovakia, United Kingdom. The Muddle-Through baseline puts these markets in C3 (*Displacement Without Absorption*). Two within-corridor sub-clusters: Ireland and the UK form a *Liberal Market high* group at ratios 3.33–3.40 — high knowledge-economy concentration plus weak training capacity (derived A→C transition central 3.2%, against an 8% Nordic benchmark). The remaining 13 form a *CEE / Mediterranean weak-ALMP* group at ratios 2.81–2.96. The headline read: displacement velocity exceeds absorption capacity, and the reskilling pathway is structurally insufficient — anchored empirically by a 7.55M deep-reskilling need across EU-27+UK by 2035, against ~450K net new annual transitions, implying a 15-year backlog and a 5–9-year speed gap between AI displacement and reskilling system response.

A finding worth surfacing: **aggregation hides bifurcation.** Within the high-coordination cluster (across Class I and Class III), the 1-digit average concealed a 3.7× internal spread — teaching-heavy professionals carry coordination weight 0.582; ICT 0.157. Splitting at 2-digit produces two archetypes moving in opposite directions: *EDUCATION / ADMIN LIFT* (Denmark, Iceland, Luxembourg, Norway) and *FINANCE / TECH DRAG* (Switzerland, Germany, Ireland, UK). The cluster isn't one archetype; it's two.

**Class IV — Active Cascade (3 countries).** North Macedonia, Serbia, Turkey. The cascade signal arrives via Lens 4 and Lens 5 extremes — their corridor baselines sit in C2, but the polycrisis and EEA-vulnerability readings push them outside the routine-perturbation envelope. Turkey carries the *Climate Adaptation Boom-dependent* flag in addition to Class IV, narrowing its optimism path further.

**The squeeze cluster — eight worker-protection economies, two distinct mechanisms.** Lens 4 flags eight countries whose institutional structure produces a jurisdictional squeeze: BE, DE, DK, FI, FR, NL, NO, SE — Continental + Nordic worker-protection economies. They split into two mechanistically distinct sub-clusters. The *Nordic sub-cluster* (DK, FI, NO, SE) carries the squeeze via worker-protection plus trade-decoupling exposure. The *Continental sub-cluster* (BE, DE, FR, NL) carries it via worker-protection plus UK adjacency — high domestic protection sitting next to weaker UK protection, with Mode 1 capital-flight risk on top. The squeeze is a capital-flight signal, not a labour-displacement signal — quantified in the SOT by Annex III high-risk deployer counts (~40 per country) and PWD post-market duty counts (~29 per country). The conflation worth resisting: squeeze and active cascade are separate signals through separate institutional channels. (Note: an earlier draft of this brief named only five squeeze countries — that draft drifted from the SOT data, which records the eight-country pattern Phase 2 methodology computed.)

Read across the four classes. Nine markets in Class I are conditionally robust under the softer rule — and zero are robust under the strict rule. Nine sit one routine variant away from C3. Fifteen are already there at baseline. Three carry active-cascade signals. The distribution itself encodes the structural-bias reading from §1: the centre of gravity of the European map sits inside C2 and C3, not inside C1. The advisory implication is that the policy debate cannot be framed as "how do we keep the Nordic model." It has to be framed as "how do we get the other 27 markets to the Nordic conditional position."
```

**§5 What the Framework Cannot See — trim:**

```markdown
## §5 What the Framework Cannot See

Five honest limits frame this read. The framework draws on structured artefacts (CSVs, JSON, methodology notes) but does not pull live external intelligence. Recent moves on Draghi-track competitiveness funding, the latest national budget rounds, and the most recent ALMP reform announcements are out of scope. The MFF mid-cycle reinforcement is treated as an EU-aggregate signal because publicly available Council documentation does not disaggregate the €64.6 B by Member State. That gap is a known limit. The four candidate, partial-coverage markets (BA, MK, RS, TR) are routed to a "central-eastern-European-in-C2" sub-cluster as an analytical convention, not as a confirmed institutional similarity. The capability-floor breach scope is bounded above by the 2-digit ISCO ceiling.
```

(Note: drop the "Lens 2 was rendered as a single-string field..." sentence — Bundle P enrichment removed that limit; per-country variance is now surfaced.)

**§6 Closer (Phil-drafted, "ecological" applied):**

```markdown
## §6 Closer

This brief diagnoses the challenges. It does not prescribe a response. A country's "risk class" reflects current policy choices, not a fixed destiny. Job-training capacity, reskilling, (EU) funding choices, regulation, and fiscal headroom can shift corridor placement, and more importantly, social, economic, and ecological realities.

- Class I markets can largely focus on preservation.
- Class II markets face conditional fragilities that can harden or soften depending on the scenario.
- Class III markets need step-change responses.
- Class IV markets need containment.

The strict-zero finding demands a response, not just a diagnosis. *What to do comes in a separate document: Part 7 of this project, scoped separately.*
```

**Global replacements:**
- All "Layer 7" → "Part 7" in Executive, One-Pager, Einfache, Specialist Appendix
- "harderst" → "hardest" (typo fix in §2 Lens 5)
- "ESCO" → "ISCO with ESCO weighting" (or "occupational classification" at executive register) wherever the technical-vs-executive distinction matters

#### Source 3: Squeeze-flag reconciliation (Phil-locked Path 1)

The SOT records 8 squeeze-true countries: BE/DE/DK/FI/FR/NL/NO/SE. LU is `false`. The earlier Specialist Appendix narrative (5 countries: BE/DE/FR/LU/NL) drifted from the SOT — it was a focused subset mislabeled as the squeeze set. **Path 1 lock: trust SOT (8 countries) with the two-sub-cluster reframe.**

| Squeeze sub-cluster | Countries | Mechanism |
|---|---|---|
| Nordic | DK, FI, NO, SE | Worker-protection + trade-decoupling exposure (no UK adjacency) |
| Continental | BE, DE, FR, NL | Worker-protection + UK adjacency + Mode 1 capital-flight risk |
| LU correction | — | Not squeeze-flagged in SOT (earlier narrative was wrong) |

This answers the Phase 2 open question: the squeeze pattern is genuine extension, not methodology over-fitting — it decomposes cleanly into two mechanistically distinct sub-clusters.

The Specialist Appendix §4.5 needs a rewrite to reflect the 8-country headline + two-sub-cluster decomposition; the LU correction noted explicitly. The Executive §4 paragraph above already reflects the locked reframe.

### Output files

| File | Action |
|---|---|
| `layer-6-deliverable-document-executive.md` | Substantial rewrite per locked drafts above + bundle integration markers |
| `layer-6-deliverable-onepager.md` | Targeted edits — finding 2 absorbs zone-heterogeneity + Italy −485K; finding on squeeze updates to 8-country two-sub-cluster; add 7.55M / 15-year backlog one-liner; "Part 7" globally |
| `layer-6-deliverable-document-einfache-en.md` and `-de.md` | Targeted edits — capacity-gap math at B1 ("15 years to retrain enough workers"); zone-heterogeneity at B1; squeeze 8-country at B1; "Part 7" / "Teil 7" globally |
| `layer-6-glossary-draft.tsv` | Add ~10 terms: A→C transition rate, reform-velocity composite, internal-transition diagnostic, deep-reskilling need, regulatory asymmetry, Annex III, PWD, Zone A/B/C/D, retirement offset |
| `layer-6-deliverable-document.md` (Specialist Appendix) | Targeted edits — §4.5 squeeze rewrite (8-country two-sub-cluster + LU correction + Phase 2 open-question resolution); §2 Lens 1+4+5 enrichment integration; §4 Class III 7.55M anchor; "Part 7" globally |
| `layer-6-lens-framework.md` | Light updates — Lens 1 schema additions (`lens1_a_to_c_transition_rate_pct`, `lens1_regulated_absorption_pct`); Lens 5 (`lens5_internal_transition_diagnostic`) |

### Constraints

- **Read-only against the SOT JSON.** Do not modify it. All numeric claims trace to specific SOT fields.
- **Locked drafts above are verbatim.** Do not rewrite §2/§3/§4/§5/§6 register; integrate the bundle data into the structures shown.
- **Phil-voice silver-lining + Phil-voice §6 closer are locked verbatim.**
- **No emoji** in any deliverable body (🛈 tooltip markers preserved in Executive — they're UI hooks, not display glyphs).
- **BR-19 no fabrication.** Every numeric claim traces to SOT JSON.
- **Banned-phrase scan as sentinel.** Tier 1, 2, 3 — 0 hits required across all updated files.
- **Em-dash discipline.** Executive ≤0.7/para; One-Pager ≤0.3/para; Einfache ≤0.3/para.
- **"Part 7" globally** in all public-facing artefacts (Executive, One-Pager, Einfache, Specialist Appendix). Internal master-session vocabulary stays "Layer."
- **Squeeze-set is 8 countries** everywhere it's named: BE/DE/DK/FI/FR/NL/NO/SE. Two sub-clusters (Nordic + Continental). LU explicitly NOT squeeze-flagged.
- **Italy −485,823 net migration** is load-bearing for §2 Lens 2 — surface as a sharp finding, not a buried number.
- **The 7.55M / ~450K / 15-year / 5–9-year speed gap math** is the empirical anchor for Class III "structurally insufficient" framing; surface in §3 + §4 Class III explicitly.
- Phil does all git commits.

### Verification (run before reporting back)

**Per-file structural:**
1. Executive: word count 1,950–2,400 (was 1,869; expect ~200–400 word growth from bundle integration). All section headers present. §Prelude + locked silver-lining + §6 Phil-draft preserved verbatim.
2. One-Pager: word count 600–800. 5-finding slate preserved. Squeeze update lands in finding 5.
3. Einfache EN/DE: word count under 1,200 each. Status header present. Sentence-length scan: ≤15 words average.
4. Glossary TSV: ≥40 entries.
5. Specialist Appendix: §4.5 rewrite reflects 8-country two-sub-cluster.

**Cross-file consistency:**
6. Squeeze countries identical across all files: BE/DE/DK/FI/FR/NL/NO/SE (8). LU named explicitly as NOT squeeze in Executive §4 + Specialist Appendix §4.5.
7. Class distribution unchanged: 9 / 9 / 15 / 3.
8. s2b-dependent countries (AT, LU, TR) consistent across §3, §4 Class II, §4 Class IV.
9. Italy −485,823 named identically wherever surfaced.
10. 7.55M / 450K / 15-year / 5–9-year speed gap consistent across §3 + §4 Class III + One-Pager.
11. "Part 7" globally — 0 instances of "Layer 7" in any public-facing deliverable.

**Anti-slop / banned-phrase scan:**
12. Tier 1, 2, 3 banned phrases: 0 hits across all updated files.
13. Em-dash density: Executive ≤0.7/para; One-Pager ≤0.3/para; Einfache ≤0.3/para.
14. No sentence-fragment-then-colon openers; no closing CTA; no emoji-as-bullet-marker.

**Numeric provenance:**
15. Random-sample 8 numbers across the updated files (2 Executive + 2 One-Pager + 2 Einfache + 2 Specialist Appendix); each traces to a specific SOT JSON field path via grep.

### When done — report back to master session with

1. Per-file word counts + diff size (lines added / lines removed).
2. Verification checklist (1–15) — pass/fail per item.
3. Banned-phrase scan results.
4. Em-dash density per file.
5. Squeeze-set audit: confirm 8 countries everywhere; LU correction present where surfaced.
6. Bundle integration audit: confirm each P/Q/R bundle's load-bearing finding is surfaced in at least one of Executive/One-Pager/Einfache.
7. Any composition gaps — places where the locked drafts didn't quite fit the bundle data, or where bundle data turned out thinner than expected.
8. Recommendation for Bundle N3 dispatch sequencing (parallel with Bundle O update, or sequential).
9. Any candidate brain captures (T36-adjacent observations during integration; BR triggers fired).

## END PROMPT
