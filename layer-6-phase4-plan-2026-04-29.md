# Layer 6 Phase 4 Plan — Deliverable Build (2026-04-29)

Phase 3 closed; all corridors, classes, scenarios, probabilities, and folded findings are locked. Phase 4 builds the actual deliverable: the synthesis document + `synthesis.nexalps.com` site rendering Layer 6.

---

## What's locked entering Phase 4

| Lock | Source |
|---|---|
| 36-country corridor map (1.20/2.80 thresholds) | Bundle J |
| Class distribution: **I=9 / II=9 / III=15 / IV=3** | Bundle L + Q1 asymmetric-guard lock |
| Class I = 9 (5 Nordics + BE/FR/NL/LU) | Q1 asymmetric-guard 2026-04-29 |
| Lens 5(c) Klinger 2-digit + 12-country breach scope | Bundle K-2 |
| Regime-conditional probability vectors (3 regimes × 6 routine + S5 cond) with 80% CIs | Bundle L |
| `s2b_dependent` cluster: AT, LU, TR | Bundle L |
| BE/NL squeeze-flag verdict: orthogonal signal | Bundle L |
| SE class_i_confidence: medium | Bundle L |
| Scale tags per country | Bundle L |

## Q2–Q6 decisions baked into Phase 4 scope (locked 2026-04-29)

- **Q2 — Probability CIs in deliverable:** YES. Use corridor-distribution language ("likely in C2 with 60–70% mass") not bare point estimates. Match advisory-track scientific discipline.
- **Q3 — C3 sub-corridor split:** within-corridor analytical tag (Liberal Market 3.33–3.40 vs CEE/Mediterranean weak-ALMP 2.81–2.96). NOT a 4th corridor — would re-litigate Bundle J's 3-corridor lock.
- **Q4 — `s2b_dependent` cluster framing:** load-bearing callout. "The optimism path narrows to Climate Zone-C" pairs with structural-bias warning + S2b dominance under post-growth — strong narrative anchor for the deliverable.
- **Q5 — Breach scope ceiling:** accept 12 (2-digit). 3-digit ESS microdata is multi-week application; document as Phase 5+ enhancement candidate, not Phase 4 blocker.
- **Q6 — Ukraine integration:** separate Class IV reference panel (per spec line 341 — analytical anchor not corridor-mapped). Distinct from the 36-country narrative.

## Phase 4 sub-bundle structure

Phase 4 splits naturally into two parallel tracks:

**Track A — Document (`layer-6-deliverable-document.md`)**
The analytical anchor. Carries: exec summary, methodology, lens-by-lens findings, corridor narrative, fragility-class country profiles, scenario-stack analysis with probabilities + CIs, structural-bias headline, Ukraine reference panel, methodological appendix. Audience: advisory track (Cembra-class engagements, board materials, lecture decks).

**Track B — Site (`synthesis.nexalps.com`)**
The interactive rendering. Carries: corridor map (36 countries colour-coded by Class), 5-trajectory sparkline per country (per locked spec line 418), country-detail pages, scenario toggle, fragility-class distribution panel, lens-finding callouts, methodology page, sources page. Audience: public/policy track + as a citable resource for the document.

Tracks share a **single source-of-truth JSON** (`layer-6-deliverable-data.json`) that both consume — document quotes from it, site renders from it. Build the JSON first, then both tracks in parallel.

## Bundle structure

```
   ┌─────────────────────────────┐
   │ Bundle M — SOT JSON build   │
   │ (single source of truth)    │
   └──────────────┬──────────────┘
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
┌─────────────┐      ┌──────────────────┐
│ Bundle N    │      │ Bundle O         │
│ Document    │      │ Site             │
│ (Track A)   │      │ (Track B)        │
└─────────────┘      └──────────────────┘
```

| Bundle | Goal | Owner |
|---|---|---|
| **M** | Compose `layer-6-deliverable-data.json` from all Phase 1-3 outputs (per-country fields, scenario tensor, probability vectors, folded findings). Schema-locked for Bundles N + O. | Sub-session |
| **N** | Write the deliverable document (`layer-6-deliverable-document.md`) reading from M's JSON. Includes the structural-bias headline, asymmetric-guard methodology trail, Ukraine reference panel. | Sub-session |
| **O** | Site build (HTML/CSS/JS scaffold for `synthesis.nexalps.com`) rendering from M's JSON. Country corridor map + sparklines + class panel. | Sub-session (or Phil-handled if he prefers manual site authorship) |

## Handovers

- **Bundle M:** [`bundle-m-deliverable-sot-json-handover-2026-04-29.md`](bundle-m-deliverable-sot-json-handover-2026-04-29.md) ✅ shipped 2026-04-29 (schema v1.0 locked, 162.7 KB)
- **Bundle N (Specialist Appendix):** [`bundle-n-deliverable-document-handover-2026-04-29.md`](bundle-n-deliverable-document-handover-2026-04-29.md) ✅ shipped 2026-04-30 (5,818 words, 13/13 sentinels). Output to be renamed `layer-6-deliverable-document-appendix.md` after register-fork lock.
- **Bundle N2 (Executive + One-Pager + Einfache companion):** [`bundle-n2-deliverable-executive-handover-2026-04-30.md`](bundle-n2-deliverable-executive-handover-2026-04-30.md) ✅ written 2026-04-30; ready to dispatch
- **Bundle N3 (Specialist Long-Read):** ⏸ pending Phil sign-off on N2 register lock; handover to follow
- **Bundle O:** [`bundle-o-site-build-handover-2026-04-30.md`](bundle-o-site-build-handover-2026-04-30.md) ✅ v3-design-system version written; pending update for executive-register overview, Einfache toggle, glossary page (post-N2)

## Tracking

| Bundle | Handover | Dispatched | Complete |
|---|---|---|---|
| M | ✅ 2026-04-29 | ✅ 2026-04-29 | ✅ 2026-04-29 |
| N (Appendix) | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 |
| N2 (Exec + 1-pager + Einfache) | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 (in editorial review) |
| Cross-layer enrichment audit | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 |
| **P (L4 demographics → Lens 2)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 |
| **Q (L1 regulatory overlay → Lens 1+4)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 |
| **R (L5 reskilling math → Lens 1+§3+Lens 5)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 |
| Squeeze-flag reconciliation (Path 1 lock — 8 countries, 2 sub-clusters) | ✅ 2026-04-30 (master session) | — | ✅ |
| **N2 re-derivation (P/Q/R + editorial pass + squeeze reconciliation)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 (post-edit Partial Absorption rename + plain-language pass) |
| **O v0.1 (site, Executive register, Einfache toggle, glossary page)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 (20/20 PASS; held from deploy pending Phase 1 storytelling rewrite + bundle/phase scrub) |
| **V (scenario reframe — S3 Jobs Transform + S1–S8 renumbering)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 (8/8 sentinels; SOT + lens spec updated; deliverable surface flagged) |
| **O Phase 1A (content rewrite — bundle/phase scrub + S5 Wage Cliff sharpening + axis flip + Italy reframe + S8 climate/decoupling + sidenote on no-historic-S8-analogue + crafted Minto SMs + plain-language discipline)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 (19/19 PASS; 5 site pages + glossary TSV + data.json refresh; cache-busting fetch added; comparator drift caught) |
| **X (pan-European aggregate — EU-27 + 36-market weighted aggregates + variation guard + headline finding string)** | ✅ 2026-04-30 | ✅ 2026-04-30 | ✅ 2026-04-30 (13/13 PASS; both aggregates + Class IV asymmetry finding + 38.5% post-growth share + modal-S2 sentinel held) |
| **Master session handover document** | ✅ 2026-04-30 | — | ✅ ([master-session-handover-2026-04-30.md](master-session-handover-2026-04-30.md)) |
| O Phase 1B (IA restructure — landing summary + rename → `findings.html` + within-section Minto + new `europe.html` + nav + `.closer`→`.conclusion` CSS + global S8 rename to **Polycrisis Drag**) | ✅ 2026-05-05 ([bundle-o-phase-1b-ia-restructure-handover-2026-05-05.md](bundle-o-phase-1b-ia-restructure-handover-2026-05-05.md)) | ✅ 2026-05-05 | ✅ 2026-05-05 (20/20 PASS; 7 HTML pages; 9 V1.1 SMs verbatim; 10 S8 rename occurrences across 5 files; Bundle X aggregates render live; responsive toggle works; 2 Phil-decision items + 7 Phase 2 readiness flags surfaced) |
| O Phase 2A (design exploration — 5 problems × 2-3 alternatives + recommendation per problem; output to `site/phase2-explorations/`; no live-site edits) | ✅ 2026-05-05 ([bundle-o-phase-2a-design-exploration-brief-2026-05-05.md](bundle-o-phase-2a-design-exploration-brief-2026-05-05.md)) | ✅ 2026-05-05 | ✅ 2026-05-05 (9/9 PASS; 12 mockups; locks resolved 2026-05-06: P1 rastered-map (new design via 2A.2), P2 B population-stack, P3 absorbed into P1, P4 A shift-bars (S1+S3 cluster reading), P5 B delta-callout) |
| O Phase 2A.2 (rastered corridor map mini-exploration — single high-fidelity mockup with P3 cross-link + beeswarm toggle baked in) | ✅ 2026-05-06 ([bundle-o-phase-2a2-rastered-map-brief-2026-05-06.md](bundle-o-phase-2a2-rastered-map-brief-2026-05-06.md)) | ✅ 2026-05-06 (4 iterations: 222 → 400 → 762 → 1850 → **1938** equal-area + cleanups) | ✅ 2026-05-06 (final: 96×68 grid, Lambert cylindrical equal-area, 1938 cells, 15.5 KB inline; **33/33 non-microstate countries within ±25% of median**; IS bias resolved; English Channel widened to ≥4 cols; CY at 3 cells; all 5 microstate labels render; mobile cells 3.34 px; `.gitignore` added; Phase 2B build estimate ~14–16 h across 5 problems; awaiting Phil's visual sign-off on equal-area Nordic squash) |
| O Phase 2B (build — implement Phil-locked alternatives into live site; rastered corridor map, fragility-class graphic, §3↔§4 cross-linking, weather-pattern viz, europe aggregate panels + landing-page Minto pyramid + §7 methodology note + nav home-anchor + PostHog re-apply) | ✅ 2026-05-06 ([bundle-o-phase-2b-build-handover-2026-05-06.md](bundle-o-phase-2b-build-handover-2026-05-06.md)) | ✅ 2026-05-06 | ✅ 2026-05-06 (16/16 PASS in single session; +290 lines net across 7 files; 348 KB folder; landing Minto pyramid live; rastered map ported; P5 direction-reversed verbatim; single shared cross-link state machine; PostHog applied; mobile verified; Phil flagged 24 cleanup items on review → Phase 2C) |
| O Phase 2C (editorial + style + IA cleanup pass — 24 items absorbed) | ✅ 2026-05-06 ([bundle-o-phase-2c-cleanup-handover-2026-05-06.md](bundle-o-phase-2c-cleanup-handover-2026-05-06.md)) | ✅ 2026-05-06 | ✅ 2026-05-06 (21/21 PASS; banned-phrase grep 0 hits site-wide; inherited-text scan applied; methodology 4 SMs incl. ninth-scenario; Findings §4 cards above stack; integrated nav + 5 sister-layer cross-links; Einfache fully removed; S8 prominent block; weather-pattern country pills; 520 KB folder; ship-ready audit run 2026-05-07 → Phase 2D) |
| Ship-ready audit (2026-05-07) | — | — | ✅ 24/40 PASS · 9 needs-attention · 7 missing · 3 deploy-blockers (llms.txt stale + banned phrase, netlify.toml missing, sitemap missing 2 pages) |
| O Phase 2D (ship-ready cleanup — 12 items: 3 deploy-blockers, 4 ship-quality, 3 cleanup, 2 Phil-resolved locks (read→analysis, glossary EN/DE strip)) | ✅ 2026-05-07 ([bundle-o-phase-2d-ship-ready-cleanup-handover-2026-05-07.md](bundle-o-phase-2d-ship-ready-cleanup-handover-2026-05-07.md)) | ✅ 2026-05-07 | ✅ 2026-05-07 (15/15 PASS; netlify.toml + sitemap + llms.txt regen; second byline 15 sources proposed; tracking site-wide; D3 dead-load removed; banned-phrase grep clean; Italy number font-size reduced 24→inherit per Phil; sources audit gap surfaced → Phase 2E) |
| O Phase 2E (sources audit — Draghi 2024 added as Tier 1; **exhaustive** cross-layer audit against `DATA-REGISTRY.md` + 5 sister-layer sources.html; "See also" cross-layer footer; byline + llms.txt source-count update) | ✅ 2026-05-07 ([bundle-o-phase-2e-sources-audit-handover-2026-05-07.md](bundle-o-phase-2e-sources-audit-handover-2026-05-07.md)) | ✅ 2026-05-07 | ✅ 2026-05-07 (8/8 PASS; 15 → **53 primary sources** (+38: 25 Tier 1 + 13 Tier 2); ~250 source-line items reviewed; 213 excluded with rationale; Treichl+Klinger cross-reference (option a); banned-phrase grep clean; sources-audit-at-phase-boundary rule surfaced as capture candidate) |
| O Phase 2F (new-sources triage — flag-only review of 25 new Tier 1 sources) | ✅ 2026-05-07 ([bundle-o-phase-2f-source-triage-handover-2026-05-07.md](bundle-o-phase-2f-source-triage-handover-2026-05-07.md)) | ✅ 2026-05-07 | ✅ 2026-05-07 (7/7 PASS; 22 Confirms / 3 Refines / **0 Shifts / 0 Contradicts**; SOT untouched per checksum; Phase 2G NOT needed; 2 source-card copy-edit gaps surfaced + 2 brain captures) |
| O Phase 2G (conditional — re-derivation of SOT fields flagged in 2F) | — | — | ❌ NOT NEEDED (2F triage cleared synthesis as-is) |
| Phase 2F follow-up (inline) — Canaries source-card rewrite to S6/speed-gap; Brynjolfsson Li Raymond 2023 added as Tier 1 (NEW source); ILO 2025 reclassified Tier 2 → Tier 1; count bumped 53 → 54 across sources.html + 7 page bylines + llms.txt + JSON-LD | — | — | ✅ 2026-05-07 (master inline fix; all 8 count references updated; 0 residual) |
| O Phase 2H (typography + style consistency pass — 5 Phil-flagged issues + systematic audit against sister-layer canonical + ship-ready checklist §1 type scale) | ✅ 2026-05-07 ([bundle-o-phase-2h-typography-cleanup-handover-2026-05-07.md](bundle-o-phase-2h-typography-cleanup-handover-2026-05-07.md)) | ✅ 2026-05-07 | ✅ 2026-05-07 (10/10 PASS; 7 Aligning fixes + 4 Decisions surfaced; net −4 lines; methodology audit complete but scenarios + europe not fully audited → Phase 2I) |
| O Phase 2I (typography finish — complete scenarios + europe per-element type-scale audit; widen methodology + sources from .container-narrow to .container 1200px for synthesis-internal visual consistency, override article-format convention) | ✅ 2026-05-07 ([bundle-o-phase-2i-typography-finish-handover-2026-05-07.md](bundle-o-phase-2i-typography-finish-handover-2026-05-07.md)) | ✅ 2026-05-07 | ✅ 2026-05-07 (8/8 PASS; 7 Aligning + 5 fractional-rounded + 8 Necessary kept; methodology + sources containers widened to 1200px with inner max-widths preserved; net −2 lines; sub-session deviated honestly on source-list width with rationale; Phil browser pass pending) |
| W (Minto propagation across deliverable surface — Executive + One-Pager + Einfache + Specialist Appendix; absorbs S8 rename + 4-SM methodology + Italy plain-prose + 54-source bibliography + scenarios phrasing + banned-phrase scrub; One-Pager rewritten to mirror landing Minto) | ✅ 2026-05-07 ([bundle-w-deliverable-doc-propagation-handover-2026-05-07.md](bundle-w-deliverable-doc-propagation-handover-2026-05-07.md)) | ⏸ ready to dispatch | ⏸ |
| N3 (Long-Read with graphics, Minto-aligned at open) | ⏸ post-Phase-2 (parallel with W) | ⏸ | ⏸ |
| Deploy v1 to live `synthesis.nexalps.com` (Phil-managed; single coherent launch) | ⏸ post-N3 + W | ⏸ | ⏸ |

## Out of scope

- Phase 5+ enhancements (3-digit ESS microdata, OECD non-EU comparator panel, Lens 5(a) trade-decoupling refinement using Comext archives)
- L1–L5 layer site changes (those layer sites are live and not Layer 6's concern)
- Brain-level skill enrichment (T34 already landed in Phase 3 closure; further generalisations to disruption-analysis come post-Phase-4 if the Phase 4 build surfaces them)

## Post-Bundle-O candidate work (logged 2026-04-30)

- **Portfolio-wide PostHog audit** across all 6 nexalps subdomains (ai-exposure, demographics, disruptions, reskilling, careers, synthesis): verify tracking is live and consistent; check for leakage; review cookie/consent posture; consider adding cookie banner per ePrivacy / Swiss FADP. Run after Bundle O ships so the audit covers all 6 sites simultaneously.
- **v3 retrofit of `ai-exposure.nexalps.com`** to bring the v1 site up to the v3 layer-site design system (parity with the rest of the layer-site portfolio).
- **Einfache Sprache + glossary retrofit across 5 sister layer-sites** (ai-exposure, demographics, disruptions, reskilling, careers) — port the toggle pattern + glossary page + B1-register variants once Bundle O has the reference implementation. Authoring requires human Einfache Sprache review pass per Netzwerk-Leichte-Sprache / Hurraki style guides.

## Layer 7 (out of scope for Phase 4)

*What can be done* is **Layer 7**, scoped separately. See [`/Users/philippmaul/Documents/projects/european-ai-labour-actions/RATIONALE.md`](../european-ai-labour-actions/RATIONALE.md). The Layer 6 Executive Edition closer references Layer 7; Layer 7 build dispatch waits until Layer 6 ships fully.
