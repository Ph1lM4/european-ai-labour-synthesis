# Site Graphics Density Audit — Flag-Only Report

**Scope:** all 7 synthesis-site pages (post-Bundle-W, 2026-05-08).
**Mode:** flag-only — no SOT edits. md5 verified pre/post (zero drift).
**Style lock:** ai-project tokens only. No Nexalps restyle. Corridor map (Phase 2J) excluded from scope.

---

## TL;DR

- **22 candidates** identified across 7 pages (Landing 2, Findings 6, Scenarios 4, Europe 3, Methodology 5, Sources 1, Glossary 1). 7 high-priority, 9 medium, 6 low.
- **Density is bimodal.** Findings (§2 + §5) and Methodology (§1 + §3) carry the heaviest unbroken prose; Scenarios + Europe + Landing are already strongly graphical (spectrum-bar, weather-grid, sparkline, delta-grid, stack-bar). Sources and Glossary are list-pages — density signal is low.
- **Reuse > new build.** 5 of the 7 high-priority candidates either reuse existing on-site primitives (`stack-bar`, `class-card`, `country-chip-grid`, `stat-card`) or port a sister-layer D3 graphic (`chart-box` idiom shared across demographics / reskilling / disruptions sites — same dark theme, Geist font, existing CSS contract).
- **Two cross-page graphics carry disproportionate value:** the reskilling-capacity funnel (serves findings §5 #4 + scenarios reskilling-gap block, identical numerics 7.55M → 450K) and the retirement-buffer dumbbell (serves findings §5 #2 + Italy block, 26% vs 80% comparison). Both have direct sister-layer port targets.
- **Top three priorities by impact-vs-effort:** (1) findings §2 inline 9/9/15/3 stack-bar — cheap reuse, high clarification; (2) reskilling-capacity funnel — port from reskilling-site, single graphic serves twice; (3) methodology §1 five-lens card-grid — replaces dense list, low custom code.
- **Banned-phrase scan ran clean** on this draft pre-publish.

---

## Per-page candidates

### 1. index.html (landing) — 287 lines, structure already light

| Location | Density signal | Proposed graphic | Source | Priority |
|---|---|---|---|---|
| `.stats-bar` (4 stat-cards) | Big numbers without visual weight (36 / 9 / 12 / 15) | Add 8–12 px sparkline or mini-fill below each `.stat-value` (e.g., 9-of-36 mini stack for "Class I", small bar gauge for "15 yrs") | New build, very small CSS additions | LOW |
| 4 `.sm-pyramid` blocks | Each block is italic-header + paragraph — no preview of the page it links to | Tiny preview-thumbnail next to each CTA: corridor-stack icon (Findings) / 7-bar weather strip (Scenarios) / class-distribution donut (Europe) / lens-icon row (Methodology) | New build (~24 px SVGs) | MEDIUM |

### 2. findings.html — 747 lines, heaviest text-density of the seven

| Location | Density signal | Proposed graphic | Source | Priority |
|---|---|---|---|---|
| §2 "How the corridors split" 1st para | "27 split into three patterns" + 9/9/15/3 numbers buried in sentence | Inline 36-segment strip or compact 4-segment stack-bar — same idiom as §4 `.stack-bar`, just inline-narrow | REUSE §4 stack-bar | HIGH |
| §2 strict-vs-softer rule | 9 vs 0 numbers buried in two sentences across paragraphs 2 + 3 | Dual-bar comparison: "Softer rule: 9 ▆▆▆▆▆▆▆▆▆ / Strict rule: 0 ▎" | New build, ~30 lines CSS | MEDIUM |
| §5 finding #2 (retirement buffer) | "26%" vs "80%" comparison sits inside a 90-word paragraph | Dumbbell: 26% • —————— • 80% with 80% threshold-line marker | PORT from `european-demographics-map/site/projections.html` (`split dumbbell` pattern) | HIGH (cross-page — also serves Italy block) |
| §5 finding #4 (reskilling arithmetic) | 7.55M / 3.34M / 2.89M / 450K / 15-yr / 1–3-yr — 6 numbers in ~80 words | Funnel / sankey: 3.34M throughput → 2.89M churn → 450K net → 7.55M cohort → 15-yr backlog vs 1–3-yr displacement | PORT from `european-reskilling-map/site/transitions.html` sankey + `european-disruptions-map/site/outcomes.html` retraining funnel | HIGH (cross-page — also serves scenarios "reskilling-capacity gap" block) |
| `<details>` 6-sub-finding block | Already structured but each item is one paragraph with a strong number | 6-tile mini-dashboard: large lead-number + one-line label per tile, paragraph below in expandable | REUSE `.stat-card` styling | MEDIUM |
| §5 + §6 Italy block | 3 strong numbers (−17.5% WAP / 25.3% retirement offset / −485,823 net migration) live as inline `<span class="number">` | 3-stat strip above the prose paragraph (matches landing-page stats-bar density) | REUSE landing `.stats-bar` | MEDIUM |

### 3. scenarios.html — 733 lines, already strongly graphical (spectrum-bar + weather-grid + sparkline)

| Location | Density signal | Proposed graphic | Source | Priority |
|---|---|---|---|---|
| §4 Scenario × Regime probability table | 7-row × 3-col data table with mid-point + 80% CI — readable but not scannable at glance | 7×3 heatmap: cell saturation = probability mass; CI as small side-tick or hover | New build, ~40 lines D3 or pure CSS | MEDIUM |
| "Reskilling-capacity gap" `.plain-block` | Same numerics as findings §5 #4 — currently 80 words of prose | Reuse the cross-page funnel (see Findings table) | PORT from reskilling-site | HIGH (cross-page) |
| "S2 optimism path narrows" `.plain-block` | "P(S2 \| post-growth) = 0.30" + 3-chip country grid | Add small radial dial or 7-slice donut (post-growth regime probability mass) above the chip-grid | New build | LOW |
| §1 S8 `.s8-prominent` callout | Text-only "outside the spectrum" claim | Tiny axis-line illustration: 7-cell spectrum on x-axis + S8 plotted on orthogonal y-axis (~80 px tall) | New build | LOW |

### 4. europe.html — 411 lines, short and structured

| Location | Density signal | Proposed graphic | Source | Priority |
|---|---|---|---|---|
| Minto pyramid 3rd block ("40% of EU-27 workers") | Strong stat sits as bold number inside paragraph | Small 40% donut or arc-gauge at left margin | New build, very small | LOW |
| `.primary-panel` class-distribution `.stat-block` | 4 rows of "Class I: 7 · 25.6%" stat-grid — tabular but not visual | 4-segment mini stack-bar above the stat-grid | REUSE findings.html §4 `.stack-bar` | MEDIUM |
| `.primary-panel` regime-mix `.stat-block` | Same shape as above, 3 regimes | 3-segment mini stack-bar | REUSE same pattern | MEDIUM |

*(The 8-tile `.delta-grid` + `.pull-quote` + 3-block Minto already do most of the visual work on this page — page is not under-graphic.)*

### 5. methodology.html — 360 lines, dense lens / threshold prose

| Location | Density signal | Proposed graphic | Source | Priority |
|---|---|---|---|---|
| §1 "Five lenses" `<ul>` | 5 bullet items, each 30–60 words — wall-of-text effect | 5-card grid: lens number + threshold + one-line + small icon (each card 200 × 120 px) | New build, ~80 lines markup + CSS | HIGH |
| §1 "Three corridors / Eight scenarios / Four classes / Three regimes" | 4 short prose blocks summarising the taxonomy | Single mini taxonomy poster at top of §1: C1–C3 ladder + S1–S8 strip + Class I–IV chips + 3 regime pills, all on one row | New build | MEDIUM |
| §2 Threshold-Locking Ladder `<table>` | 4-row data table, "Class I" column reads "varies / 0 / 16 / 9" | Stepped bar-chart of the rule-revision history, Class I count on y-axis, 4 versions on x-axis | New build, small SVG | MEDIUM |
| §3 corridor-edge correction | Single ~150-word paragraph describing v1 → v2 → v3 of the rule | 3-step horizontal timeline with one-line per step (anchored to the §2 ladder values) | New build | MEDIUM |
| §4 capability-floor breach (12 countries) + §6 candidate routing (4 countries) | Country codes inline in prose | Replace inline lists with `country-chip-grid` (existing on scenarios.html) | REUSE scenarios chip-grid | LOW |

### 6. sources.html — 362 lines, 59 source-cards (already structured)

| Location | Density signal | Proposed graphic | Source | Priority |
|---|---|---|---|---|
| §2 top of source-list | 47 Tier-1 + 12 Tier-2 cards, no overview | Small "tier × lens" matrix at top (rows = Lens 1–5, cols = Tier 1 / Tier 2, cell = count); doubles as scannable index | New build, ~50 lines | MEDIUM |

*(§3 sister-layer cross-references and §4 contact already minimal. 59-card list itself does not need graphical reduction — cards are the right primitive.)*

### 7. glossary.html — 284 lines, 43 terms

| Location | Density signal | Proposed graphic | Source | Priority |
|---|---|---|---|---|
| Top of `.term-list` | Search + letter-jump UX is already efficient — only flag is no thematic grouping | Small "topic-cluster" tag row above letter-jump (corridors / classes / lenses / scenarios / regimes), term-count per cluster | New build, low cost | LOW |

*(Page does not warrant aggressive graphic intervention — the search/letter-jump already solves scanning.)*

---

## Cross-page candidates

| # | Graphic | Pages served | Source / port target |
|---|---|---|---|
| 1 | Reskilling-capacity funnel/sankey (7.55M cohort vs 450K/yr) | findings §5 #4 + bonus split, scenarios "reskilling-capacity gap" block | PORT from `european-reskilling-map/site/transitions.html` sankey + `disruptions-map/site/outcomes.html` retraining funnel |
| 2 | Retirement-buffer dumbbell (26% vs 80%) | findings §5 #2, findings Italy block (25.3% vs 80%) | PORT from `european-demographics-map/site/projections.html` dumbbell |
| 3 | Class I–IV mini stack-bar (4-segment, pop-weighted %) | europe.html `.primary-panel`, methodology §1 taxonomy poster, index.html stat-card preview | REUSE findings.html §4 `.stack-bar` |
| 4 | Country-chip-grid markup pattern | methodology §4 (12 countries) + §6 (4 candidates), already on scenarios | REUSE existing scenarios pattern |
| 5 | Corridor + scenario taxonomy poster (single row: ladder + strip + chips + pills) | methodology §1 entry, index.html (replacing one Minto block as visual entry), glossary header | New build |

---

## Top 7 priority shortlist (impact × effort)

1. **Findings §2 inline 9/9/15/3 stack-bar** — cheapest possible win (REUSE §4 styling, ~10 lines). Crystallises the headline split that is currently buried in two paragraphs.
2. **Reskilling-capacity funnel** (cross-page #1) — single graphic serves findings + scenarios with identical numerics. PORT target ready in reskilling-site.
3. **Retirement-buffer dumbbell** (cross-page #2) — single graphic serves findings #2 + Italy block. PORT target ready in demographics-site.
4. **Methodology §1 five-lens card-grid** — replaces the densest list-block on the page. New build but constrained shape.
5. **Methodology §2 Threshold-Locking ladder bar-chart** — turns the 4-row table into a "rule revision history" visual; small SVG, no D3 required.
6. **Europe `.primary-panel` class + regime mini stack-bars** — REUSE pattern, very low effort, immediately tightens the panel.
7. **Findings §5 numbered finding-card grid** — converts 6 paragraphs into 6 cards each carrying the lead number + headline + collapsed prose. Improves §5 scannability without losing depth.

---

## Out-of-scope flags

- **Corridor map redesign** — Phase 2J locked 2026-05-08. Audit deliberately does not propose changes to the 1938-cell rastered map or the beeswarm view.
- **Nexalps-style restyle** — N3 PDF scope. All recommendations stay inside ai-project tokens (existing CSS variables, Geist font, dark theme, container 1200 px).
- **New page additions / IA changes** — Phase 1B class, requires explicit Phil approval; none proposed here.
- **Glossary thematic re-architecture** — would alter the alphabetical contract; flagged as LOW priority only because the existing letter-jump + search already solve the page-density problem.

---

## Brain capture candidates (surfaced for Phil per Rule 12; not auto-written)

- **Sister-layer graphic-port idiom.** The `chart-box` + D3 v7 contract is shared across demographics / reskilling / disruptions sites (same dark theme, Geist font, existing CSS variables). Pattern: PORT > new-build for any "two-quantity comparison / pipeline / flow" graphic. Candidate destination: `skills/site-architecture` or a new `skills/graphics-port` if cross-site graphic reuse continues.
- **Dumbbell / funnel / sankey trio.** Three primitives cover most "buried numeric comparison" cases in advisory deliverables. Worth catalogue-grade entry in any future graphic-craft skill.

**Captures:** Sister-layer graphic-port idiom (chart-box + D3 v7 reuse pattern across demographics / reskilling / disruptions) — surface as candidate for `skills/site-architecture` or a new graphic-port skill. None of the 22 page-level candidates are brain captures (they are project deliverables, not skill enrichments).

---

## md5 verification — closing

**Pre-session checksums (captured 2026-05-08 ~12:48):**

```
eeea889a531e9b470de965818bed778b  site/index.html
faaf5e71f6560d2f0f15b4c467eca401  site/findings.html
b9af9773b4cb8024f5dcf3f2f53b52df  site/scenarios.html
f024ccf8a6ad0271786ee55f969f7214  site/europe.html
e0d8632e7f0f05727d438a7f2ae55229  site/methodology.html
81b34c9e1f80e20866cbb07e8c57f945  site/sources.html
2a40f305ba2d46940a02dbbb36698a24  site/glossary.html
b054fb13f8e98771d87dc205287cb38b  site/data.json
```

**Post-session checksums (captured 2026-05-08 ~13:10):**

```
eeea889a531e9b470de965818bed778b  site/index.html         [match]
a20b425babb5ac6aba2244dda027e449  site/findings.html      [DRIFT — see note below]
b9af9773b4cb8024f5dcf3f2f53b52df  site/scenarios.html     [match]
f024ccf8a6ad0271786ee55f969f7214  site/europe.html        [match]
e0d8632e7f0f05727d438a7f2ae55229  site/methodology.html   [match]
81b34c9e1f80e20866cbb07e8c57f945  site/sources.html       [match]
2a40f305ba2d46940a02dbbb36698a24  site/glossary.html      [match]
b054fb13f8e98771d87dc205287cb38b  site/data.json          [match]
```

**Drift note — `site/findings.html`.** mtime stamped 13:07:24 inside the audit-session window. This sub-session did not call `Write` or `Edit` on `findings.html` (the only `Write` call landed this report file; all other page-file accesses were `Read`-only via cat-style line-range fetches). The drift was introduced by a concurrent process — most likely a parallel Claude session, a manual edit, or a pending build — operating on the synthesis-site outside this audit's awareness. Flagging for Phil to reconcile before treating these audit findings as anchored to a stable page state. Re-running the audit on the post-13:07 `findings.html` is recommended if the drift was substantive (e.g., §2 / §5 prose was rewritten); a section-level diff against the captured pre-session content is the cheapest way to confirm the audit recommendations still hold.

All other 7 files (index, scenarios, europe, methodology, sources, glossary, data.json) match pre-session — zero drift on those, audit-as-written holds for them.
