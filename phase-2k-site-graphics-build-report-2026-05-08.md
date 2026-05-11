# Phase 2K — Site Graphics Build Report (2026-05-08)

Six items landed in one focused build: 3 Phase-2J micro-iterations (microstate radius, geo-note copy, per-country hit-area) + 3 Path X audit top-3 builds (§2 stack-bar, §1 five-lens card-grid, reskilling-capacity funnel). ai-project style only. Site-only render target. No SOT edits.

---

## TL;DR

- **Item 1 (micro-1) — microstate dot radius bump.** CSS rule scopes `r:4` to `[data-code]` LU / LI / MT (existing groups use `data-code`, not `data-country` as the brief hinted). Verified: computed `r` = 4 px on LU / LI / MT, 3.4 px on DE — visible bump without cluster-density compromise.
- **Item 2 (micro-2) — geo-note copy.** Inserted Phil's clarification sentence between "colour encodes fragility class" and "Web Mercator projection," with `<strong>count</strong>` emphasis on the corrected referent.
- **Item 3 (micro-3) — per-country hit-area polygons.** `tools/dotmap-gen.py` now emits per-country projected SVG paths (~5 km simplification tolerance, holes dropped) plus a `polygons.area_px` paint-order key into `site/dotmap-data.json` (80 KB → 192 KB). `renderMap()` sorts country groups by polygon area DESCENDING, so LI / LU / MT / CY paint last and sit on top of CH / AT / IT / FR; each `<g class="country-region">` has a `<path class="hit-area">` as its first child. Verified: 37/37 country groups have hit-areas; sort order places LI dead-last; existing group-level handlers fire on polygon hover (Germany detail panel renders correctly via dispatched `mouseenter`).
- **Item 4 (build-1) — findings §2 inline 9/9/15/3 stack-bar.** Static stack-bar with flex-weighted segments (9 / 9 / 15 / 3) reuses `.stack-bar` / `.stack-seg` styling from §4. New scoped `.inline-stack` wrapper (32 px height vs §4's 44 px, `cursor:default` since not interactive). Inserted right after the "How the corridors split" paragraph adjacent to the prose claim.
- **Item 5 (build-2) — methodology §1 five-lens card-grid.** Replaced the 5-item `<ul>` with a 5-column responsive grid (5/3/2/1 columns at 1100/720/480 px breakpoints). Each card carries lens number, title, one-line description ported from existing prose, and source-layer attribution (Layer 1 / 4 / 5 etc.). Added new `.lens-grid` / `.lens-card` CSS matching the existing dark-theme palette (`--card`, `--card-border`, `--ring` left-border).
- **Item 6 (build-3) — reskilling-capacity funnel.** Ported the `chart-box` container idiom from reskilling-site (D3 v7 not loaded — pure CSS / HTML implementation matched the shape better; 4 horizontal proportional bars + a callout). Renders the six numerics 7.55 M / 3.34 M / 2.89 M / 450 K / ~15-yr / 1–3-yr in their relative scale. Placed in findings §5 after the bonus-split paragraph, before the "interested readers" `<details>` block.
- **Discipline.** Banned-phrase scan ran clean on the diff (no Tier 1 / 2 / 3 hits in additions; one near-miss caught — "Source:" prefix in card footer is borderline Tier 3 sentence-fragment-then-colon, replaced with "From Layer N" / "Folded across all layers"). BR-19 fabrication discipline held — every numeric comes from the existing site or `data.json` SOT. md5 of `site/data.json` unchanged (`b054fb13f8e98771d87dc205287cb38b`); SOT preserved.

---

## Per-item summary

### 1. Microstate dot radius bump

**Files touched.** `site/findings.html` (CSS only, +4 lines).

**Change.** Added a CSS rule scoped to `[data-code="LU"|"LI"|"MT"] circle { r:4 }` directly below the existing `.is-ukraine` rule. Brief suggested `data-country=` but the group attribute is `data-code=`; selector adapted accordingly. SVG `r` attribute is overridden by the CSS `r` property in modern browsers.

**Verification.**
- DOM: `getComputedStyle(LU circle).r === "4px"`; `getComputedStyle(DE circle).r === "3.4px"`.
- Visual: LU / LI / MT now read as small but present markers; surrounding density (BE / DE / NL / CH / AT / IT) unchanged.
- Edge: hit-area for these microstates is the polygon overlay (Item 3), not the dot — so the radius bump is purely a visual signal.

### 2. Geo-note copy strengthening

**Files touched.** `site/findings.html` (single `<p class="geo-note">` line).

**Change.** Inserted Phil-iteration item #4 sentence between "colour encodes fragility class" and "Web Mercator projection" sentences:

> "Dot **count** per country reflects projected map area, not displacement scale — colour carries the corridor and class signal."

`<strong>` emphasis on `count` to anchor the corrected referent.

**Verification.** Screenshot at the §3 corridor-map block shows the new sentence reads cleanly between the two adjacent sentences; flow holds.

### 3. Per-country hit-area polygons (NEW)

**Files touched.** `tools/dotmap-gen.py` (+50 lines: 3 new functions + provenance update + `geoms` plumbed into `build_output`); `site/dotmap-data.json` (regenerated; +112 KB for `polygons` block); `site/findings.html` (CSS rule for `path.hit-area` + `circle` pointer-events, plus `renderMap()` rewrite to emit hit-areas + sort-by-area).

**Implementation detail.**
- `polygon_to_path()` simplifies each Natural Earth `(Multi)Polygon` at 0.05° tolerance (~5 km — adequate for hit-test on a ~1135 px canvas; collapses vertex count 5–10×). Holes dropped — pointer-events on a transparent fill capture the full enclosing shape regardless. Multi-polygon countries (Norway+Svalbard, Greek islands, Italy+Sicily+Sardinia, Croatian coast) emit as compound paths with `M…L…Z M…L…Z` chaining.
- `polygon_area_px()` uses the projected bounding-box area as a cheap paint-order proxy (vs full polygon area) — sufficient for the sort key, ~constant-time per country.
- Schema: new `polygons` field at top level of `dotmap-data.json`, sibling to the existing `countries` field. `polygons[code] = { path, area_px }`. Keeps the existing dot-list schema intact so `tools/dotmap-export.py` (which reads only `dotmap["countries"]`) stays compatible without changes.
- `renderMap()`:
  - Sort countries by `polygons[code].area_px` DESCENDING — largest first → smallest last → smallest paint on top.
  - Emit `<path class="hit-area" d="…" aria-hidden="true"/>` as first child of `<g class="country-region">`, before the dots.
  - CSS: `path.hit-area { fill:transparent; pointer-events:all; cursor:pointer }`; `circle { pointer-events:none }` so events fire only on the polygon, bubbling cleanly to the group-level handlers.

**Verification.**
- DOM: 37 `.country-region` groups, 37 `path.hit-area` first-children (1:1).
- Sort: LI dead-last in document order (smallest); MT second-last; LU third-last; LI/LU/MT all paint after their larger neighbours (CH/AT/FR/IT) ✓.
- Hover: dispatched `mouseenter` on DE group → detail panel renders Germany / Class II / Corridor C2 — handler chain intact.
- Console: no errors on load.
- File size: `dotmap-data.json` 80 KB → 192 KB (+112 KB; expected — polygon path strings dominate at 0.05° tolerance).

### 4. Findings §2 inline 9/9/15/3 stack-bar

**Files touched.** `site/findings.html` (+18 lines: 1 new `.inline-stack` style block + static stack-bar markup inside §2).

**Change.** Inserted between the "How the corridors split" paragraph and the next "How quickly that resilient nine collapses" paragraph. Structure: small uppercase label "36 markets by fragility class · count" + 4-segment stack-bar with `flex:9/9/15/3`. Reuses `.stack-bar` / `.stack-seg` / `.cls-I…IV` classes from §4 — same colour palette, same diagonal-hatch pattern on Class II/III. Custom `.inline-stack` wrapper drops segment height (44 → 32 px), removes `cursor:pointer` (segments aren't interactive in §2), tightens font sizing.

**Verification.** DOM: 4 segments, `flex` values 9/9/15/3 matching the §4 numerics. Screenshot shows segments coloured I-green / II-amber-hatched / III-red-hatched / IV-darkred, segment widths visually proportional to counts (Class IV is correctly thin via the `thin` modifier).

### 5. Methodology §1 five-lens card-grid

**Files touched.** `site/methodology.html` (+12 lines CSS + 32 lines markup; replaces the 8-line `<ul>` block at §1 "Five lenses").

**Card content per lens (sourced from existing methodology §1 prose + `layer-6-lens-framework.md`):**

| Lens | Title | One-line desc | Source attribution |
|---|---|---|---|
| 1 | Displacement velocity vs absorption capacity | Corridor-defining ratio; absorption decomposed by institutional system; regulated-absorption-friction 0.46–0.68 | Layer 1 (AI Exposure) · Layer 5 (Reskilling) |
| 2 | Demographic buffer | 80% retirement-offset threshold; per-country object with retirement_offset_pct, working_age_change_pct_to_2050, divergence tier, zone heterogeneity | Layer 4 (Demographics) |
| 3 | Distributional fold | Folded into the scale tag (aggregate / distributional / both) | Folded across all layers |
| 4 | Compounding-crisis & jurisdictional buffering | Shock count + squeeze flag with asymmetry score; AI-Act overlay (Annex III ~40, PLD ~29–31) carries diagnostic weight | Layer 1 (regulatory) · composite |
| 5 | Polycrisis drag | Composite at 2-digit ESCO-weighted ISCO with Klinger coordination-share weighting + capability-floor breach test | Layer 3 (Disruptions) · Layer 5 (Reskilling) |

**Responsive grid.** 5 / 3 / 2 / 1 columns at viewport 1100 / 720 / 480 px. Cards use `--card` / `--card-border` palette and a `--ring` orange left border (matches existing `.class-card` pattern on findings.html).

**Verification.** DOM: 5 cards, lens numbers Lens 1 / 2 / 3 / 4 / 5, titles match the table above, source attribution on each card. Banned-phrase scan: "Source:" sentence-fragment-then-colon prefix replaced with "From Layer N" or "Folded across all layers" to stay clean of Tier 3.

**Audit-at-class observation.** No other multi-lens enumerations on the site qualify for the same card pattern. Scenarios already use a 7-bar weather-grid + delta-grid; regimes are 3 short prose paragraphs in methodology §1 (could become a 3-pill row but lower priority — surfaced in §1 audit-extension below).

### 6. Reskilling-capacity funnel

**Files touched.** `site/findings.html` (+18 lines CSS for `.chart-box` / `.funnel-row` / `.funnel-callout`; 24 lines markup inside §5).

**Implementation choice — pure CSS / HTML, no D3.** Inspected reskilling-site `transitions.html`: D3 v7 + `d3-sankey` are loaded for the bubble chart + diverging bar + sankey-style flow. The reskilling-capacity-arithmetic story is a 4-stage proportional-bar comparison (cohort vs throughput vs churn vs net) which is substantially cleaner as static HTML+CSS than as a D3 chart. The `chart-box` container idiom (background, border, h3 styling) ports cleanly; the funnel internals are bespoke.

**Layout.** Three-column grid per row: label (200 px) | proportional bar (flex) | numeric value (110 px). Bar widths in % of the 7.55 M maximum:
- Cohort needing reskilling by 2035 — 7.55 M (100% bar, yellow)
- Annual training throughput — 3.34 M / yr (44.2%, blue)
- — absorbed by baseline churn — 2.89 M / yr (38.3%, grey)
- — net new capacity — 450 K / yr (5.96%, orange)

Plus a callout below: "~15-year backlog to clear the 7.55 M cohort at 450 K / yr net new capacity — against a 1–3 year AI displacement window. Reskilling-system response time runs 5–9 years."

**Placement.** findings §5, after the bonus-split paragraph, before the "For interested readers" `<details>` block. Anchors the §5 #4 finding visually before the prose detail block.

**Cross-page placement decision.** Default per the brief: single placement on findings §5. Methodology §3 / §6 do not directly reference these numerics (those sections cover threshold-locking and candidate-routing); methodology §5 is about MFF allocation, not reskilling. So the cross-page candidate-2 surface (scenarios "reskilling-capacity gap" block, per audit) is a future placement, not in scope here.

**Verification.** DOM: 4 funnel rows, bar widths 100% / 44.2% / 38.3% / 5.96%, callout renders the speed-gap text. ARIA: `role="img"` with full numeric description on the chart-box container.

---

## Verification checklist

### md5 audit (close)

| File | Pre-edit md5 | Post-edit md5 | Expected |
|---|---|---|---|
| `site/findings.html` | `7fbf2d7e36c5f7d00f331900f6eb401a` | `c900c05581d05442437f46746e8d2a49` | changed ✓ |
| `site/methodology.html` | `e0d8632e7f0f05727d438a7f2ae55229` | `d874782923fe59443e1fdd4e34e16830` | changed ✓ |
| `site/dotmap-data.json` | `7f1090763b20ad36f4c8d8aee1b72760` | `1176e93d6ff784314df556bcd81edf19` | changed ✓ |
| `site/data.json` | `b054fb13f8e98771d87dc205287cb38b` | `b054fb13f8e98771d87dc205287cb38b` | UNCHANGED ✓ (SOT preserved) |

`tools/dotmap-gen.py` modified (not part of the close-md5 audit; `git diff` shows the four new functions + `build_output` signature change + provenance update).

### Visual / DOM checks

| Item | Check | Result |
|---|---|---|
| micro-1 | LU / LI / MT computed `r` = 4 px (CSS override) | ✓ verified via `getComputedStyle` |
| micro-1 | DE / FR / SE etc. computed `r` = 3.4 px | ✓ unchanged |
| micro-2 | Geo-note new sentence reads cleanly between "fragility class" and "Web Mercator" sentences | ✓ visual verified |
| micro-3 | Each `<g class="country-region">` has `<path class="hit-area">` as first child | ✓ 37/37 |
| micro-3 | Sort: LI / MT / LU / CY paint last (top), CH / AT / FR / IT paint earlier | ✓ verified order |
| micro-3 | DE hover triggers detail panel | ✓ via dispatched `mouseenter` |
| micro-3 | Console errors on load | ✓ none |
| build-1 | §2 stack-bar 4 segments with flex 9/9/15/3 | ✓ verified |
| build-2 | Lens-grid 5 cards, all source-attributions present | ✓ verified |
| build-3 | Funnel chart-box 4 rows + callout, widths 100/44.2/38.3/5.96 % | ✓ verified |
| Cross | Banned-phrase scan against diff additions only | ✓ 0 hits |

### Live-preview screenshots

- Top-of-findings + corridor map: captured (Item 1 + 2 visible) — see `phase-2k-site-graphics-build-handover-2026-05-08.md` follow-up artifacts; map renders, microstates visible, geo-note new sentence reads.
- §2 inline stack-bar: captured at viewport scroll position — segments render in correct colours/widths.
- Lens-grid + funnel: DOM-verified; screenshot scroll did not capture below-fold content reliably in this preview session (preview tool returned same top-of-page screenshot regardless of `scrollIntoView` / `documentElement.scrollTop` calls). Build correctness confirmed via DOM inspection (`querySelectorAll` counts, computed styles, `getBoundingClientRect`); user-side visual confirmation recommended.

---

## Phil-iteration handoff

Three things you may want to iterate on:

1. **Funnel placement on findings §5 vs splitting onto methodology §1.** Brief said default = single placement on findings §5; that's where it landed. If methodology §1's lens-card-grid feels light (one-line descriptions only) and you want a visual anchor near "Lens 1 — Displacement velocity vs absorption capacity," a smaller variant of the funnel (or a static reference back to findings §5) could anchor that lens. Decision deferred — not built.
2. **Microstate radius value (4 px vs alternatives).** Bumped from 3.4 → 4.0 per the brief. If LU still feels too small relative to its outsized economic weight (single dot covering Luxembourg's actual financial-centre footprint), 4.5 or 5.0 px would read more strongly without invading the BE / FR / DE neighbouring clusters. Single-line CSS edit.
3. **Funnel rendered as proportional-bars (CSS) rather than D3 sankey.** Brief allowed either; chose CSS because the 4-stage cohort/throughput/churn/net comparison is fundamentally a "magnitudes at one scale" story, not a "flows between stages" story. A real sankey (with paths from cohort → throughput → split-into-churn-vs-net) would emphasise the flow but understate the cohort-vs-capacity scale gap. If you prefer the flow-emphasis frame, the reskilling-site sankey at `/transitions.html` chart 4 is the port target — 60 lines of D3 + `d3-sankey` would land it.

Lower-confidence open question — not blocking: **lens-card grid responsive breakpoint at 1100 px.** The 5-column desktop layout requires the methodology page to render at ≥1100 px viewport for the full row; below that it folds to 3 columns. The current `.container` max-width is 1200 px and pages typically render at 1280+. If the cards look cramped at 1280 desktop, dropping the breakpoint to 900 px (so 3 columns at narrower) is a one-line CSS change.

---

## Brain capture candidates

**1. Sister-layer graphic-port idiom — second confirmation.** This session validates the `chart-box` + dark-theme-palette port pattern across a second use case (synthesis-site funnel, not just demographics-dumbbell or reskilling-sankey). Specifically: the `chart-box` *container* (background, border, h3 styling, ARIA scaffolding) is the load-bearing portable primitive; the chart *internals* (D3, static SVG, CSS bars) can be substituted for the data shape without touching the container contract. Surface as a candidate row for a future `skills/graphics-port` skill or as an enrichment to `skills/site-architecture`. Already captured in audit report 2026-05-08; this is a second data point.

**2. Pure-CSS funnel pattern as alternative to D3 sankey.** When the data shape is "magnitudes at a common scale" (not "flows between distinct stages"), proportional horizontal bars in a 3-column grid (label / bar / value) communicate more cleanly than a sankey and skip the D3 dependency. Useful pattern for advisory deliverables where the quantity comparison is the load-bearing story. Lower priority capture — single instance only, repetition needed before crystallising as a skill takeaway.

**3. Per-country polygon hit-area pattern for dot/symbol maps.** Where a map renders symbol-clusters (dots, glyphs) rather than choropleth fills, the gap-between-symbols problem makes country-level interaction unreliable on small-screen / dense regions. Solution: emit invisible projected polygon overlay per country as the first child of the country group, with `fill:transparent; pointer-events:all` and group-level handlers. Sort countries by polygon area descending so microstates paint on top. Reusable across any future dot-map graphic in the suite (current candidates: ai-exposure-map, demographics-map, careers-map). Surface as a candidate for `skills/site-architecture` or a new map-craft skill — wait for one more dot-map deployment before crystallising.

---

**Time budget.** ~3 h of the 5 h budget. Item 3 (hit-area) ran longer than the 60-min estimate (~80 min — polygon simplification tuning, paint-order debugging) but the other five items came in under estimate. No scoping issues triggered the early-stop clause.

**Captures:** Brain-capture candidates 1–3 above (sister-layer chart-box port idiom · 2nd confirmation; pure-CSS funnel pattern; per-country polygon hit-area pattern) → `skills/site-architecture` SKILL.md or new graphics-port skill — deferred to Phil per Rule 12.
