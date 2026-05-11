# Handover Prompt — Bundle O Phase 2B: Build Phil-Locked Visuals into Live Site

Bounded composition session. Builds five Phil-locked visual treatments + a Minto-pyramid landing-page rebuild + a methodology-note addition into the Phase 1B live site. All copy is Phil-locked verbatim (mockups, drill-down headlines, landing SM supports, methodology note). Sub-session does structural insertion + interaction wiring + PostHog tracking re-apply, no authoring. ~14–18 h; if context tight, sub-session may report back mid-way after Phase 2B.1 (landing + P1 + P3) and resume in Phase 2B.2 (P2 + P4 + P5 + methodology note + PostHog).

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Phase 2A produced 12 mockups across 5 design problems. Phase 2A.2 produced the final rastered corridor map (`D-rastered.html`, 96×68 Lambert cylindrical equal-area, 1938 cells, full P3 interaction baked in, iframe beeswarm toggle). Phil locked all 5 directions plus a landing-page rebuild and a §7 methodology note. Phase 2B integrates all of it into the live site at `synthesis.nexalps.com`.

Locked direction set:

| # | Lock | Mockup source |
|---|---|---|
| Landing page | Rebuild as Minto pyramid (hero + stats + 4 SM blocks → 4 drill-downs) | new build, locked SM supports verbatim in this handover |
| P1 — Corridor map (`findings.html` §3) | Rastered map (96×68 equal-area, 1938 cells) | port verbatim from `phase2-explorations/1-corridor-map/D-rastered.html` |
| P2 — Fragility-class graphic (`findings.html` §4) | Population-weighted stack | port from `phase2-explorations/2-fragility-class-graphic/B-population-stack.html` |
| P3 — §3↔§4 cross-linking (`findings.html`) | Hover-highlight + click-filter (combined; absorbed into P1) | use country-region API contract from D-rastered.html |
| P4 — Weather-pattern viz (`scenarios.html` §2) | Probability-shift bars with S1+S3 cluster caption | port from `phase2-explorations/4-weather-pattern-viz/A-probability-shift-bars.html` |
| P5 — Europe panels (`europe.html`) | Primary view + delta strip with direction reversed (36-market → EU-27, the restriction-to-EU-27 read) | port from `phase2-explorations/5-europe-aggregate-panels/B-delta-callout.html` with direction fix |
| Header / nav | Wordmark/logo home anchor on all 7 pages | structural CSS + HTML pattern |
| §7 methodology note | "Why eight scenarios, not more" — Phil-locked verbatim in this handover | structural insertion |

---

## START PROMPT

I need you to build five Phil-locked visual treatments into the live `synthesis.nexalps.com` site, rebuild the landing page as a Minto pyramid, and add a methodology note. All copy is Phil-locked verbatim — your job is structural insertion + interaction wiring + PostHog tracking re-apply, not authoring.

### Read FIRST (absolute paths)

**Live-site targets (write to these):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` — landing rebuild
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — §3 corridor map + §4 fragility-class graphic + §3↔§4 cross-link
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — §2 weather-pattern viz
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html` — aggregate panels rebuild
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — §7 note addition
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html` + `glossary.html` — nav update only

**Mockup sources (read to port from):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/1-corridor-map/D-rastered.html` — P1 rastered map (final state)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/1-corridor-map/B-beeswarm.html` — beeswarm iframe target
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/2-fragility-class-graphic/B-population-stack.html` — P2 source
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/4-weather-pattern-viz/A-probability-shift-bars.html` — P4 source
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/5-europe-aggregate-panels/B-delta-callout.html` — P5 source

**Reference docs:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-o-phase-1b-ia-restructure-handover-2026-05-05.md` — Phase 1B reference for IA + token conventions
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — SOT; never modify; both visualisations + landing reference it
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/tools/cellmap-gen.py` — generator for the rastered cellMap (offline; don't run in this session unless cells need regen)

### Phil-locked anchors (verbatim — do NOT rewrite)

#### Landing page Minto pyramid (`index.html`)

The landing rebuild keeps the existing hero + stats panel + footer, REPLACES the Phase 1B "Read-more cards" with a 4-SM Minto pyramid. Each SM block uses the same `.sm-pyramid` / `.sm-header` / `.sm-support` styling already on findings/scenarios/methodology, plus a `Go deeper →` CTA link.

**Hero (already in place — do not modify):**

> **No European labour market is fully safe from AI-driven job displacement.**
>
> *We stress-tested 36 markets across five lenses and eight scenarios. Most countries can absorb the disruption only partially, and 15 are likely already beyond that threshold. Under the rules we applied, only nine have the statistical strength to hold up under pressure.*

**Stats panel** — keep current 4-card panel as-is.

**SM 1 — Findings**

Header (verbatim): *"More than three-quarters of European labour markets sit in uncomfortable territory."*

Support (verbatim): Most countries can absorb only part of the disruption, and 15 are likely already past that threshold. Nine countries qualify under our softer rule (drift one corridor either way, never the worst); under a strict reading, the count drops to zero. Even Norway and Sweden fail the strict rule. The two buffers that were supposed to soften this — retirement and retraining — don't move at the speed required.

CTA: `Go deeper →` linked to `/findings.html`

**SM 2 — Scenarios**

Header (verbatim): *"Eight ways the next decade could play out and the most likely one depends on whether your economy is still growing."*

Support (verbatim): We tested seven routine futures plus one parallel cascade scenario (Polycrisis Drag). The same shock translates into different odds depending on whether the economy is in growth, secular stagnation, or post-growth. Under post-growth, the standard tech-led-recovery story collapses from about 25% probability to about 5%, while Climate Adaptation Boom rises to take its place.

CTA: `Go deeper →` linked to `/scenarios.html`

**SM 3 — Europe**

Header (verbatim): *"Europe doesn't have one answer. It has 36."*

Support (verbatim): On a population-weighted average, the EU-27 looks like it is coping. The country-by-country view tells a different story. The cascade pressure sits at the EU's borders, not within them, and for nearly 40% of EU-27 workers, the optimism path runs through climate, not conventional tech.

CTA: `Go deeper →` linked to `/europe.html`

**SM 4 — Methodology**

Header (verbatim): *"How we tested and what we deliberately left open."*

Support (verbatim): Five lenses chosen because earlier parts of the project had already gathered the evidence. One calibration choice changed the headline. Three known gaps bound this read, and one ninth scenario was considered but excluded for empirical-anchor reasons.

CTA: `Go deeper →` linked to `/methodology.html`

#### §7 methodology note (`methodology.html`)

Append to §7 ("Known limits — what this synthesis cannot see") as a new sub-section. Phil-locked verbatim:

> **Why eight scenarios, not more.** E.g. a ninth scenario — startup-driven absorption as a parallel to Climate Adaptation Boom — was considered but excluded. The absorption mechanism is coherent in principle (new firm formation can absorb displaced workers), but the empirical anchors at country level are thinner than for S1–S8. There is no equivalent of the IPCC / Eurofound climate-demand projections or the Brynjolfsson / Dell'Acqua task-level RCTs that grounded S2 and S3, and the channel is partially captured in Lens 1's absorption-capacity score. The policy-lever version of the question — what it would take to build this mechanism deliberately at supra- or national level — belongs in Part 7.

#### P5 delta-strip direction (verbatim labels)

The P5 mockup currently reads "EU-27 → 36-market" (e.g., `Class IV count: 0 → 3`). Phil flagged this as backward. The delta strip's narrative is *"what changes if you restrict to EU-27"*, so the direction must read **36-market → EU-27** (full set on the left, restricted set on the right):

| Stat | Was (mockup) | Fix (verbatim) |
|---|---|---|
| Class IV (count) | `0 → 3` | `3 → 0` |
| Class IV (% pop) | `0.0% → 15.7%` | `15.7% → 0.0%` |
| Post-growth pop share | `38.5% → 40.2%` | `40.2% → 38.5%` |
| Capability-floor breach | `7 mkts → 12 mkts` | `12 mkts → 7 mkts` |
| Class I (count) | `7 → 9` | `9 → 7` |
| Headline corridor | `C2 → C2` | `C2 → C2` (unchanged either way) |
| Squeeze cluster | `7 mkts → 8 mkts` | `8 mkts → 7 mkts` |
| Weighted Lens 1 ratio | `2.40 → 2.50` | `2.50 → 2.40` |

Also reverse the per-stat one-liner narratives accordingly (e.g., *"5 additional markets breach when the lens widens"* becomes *"5 markets drop out of the breach list when restricted to EU-27"*).

### Header / logo home anchor (all 7 pages)

Add to the existing nav strip on all 7 pages (`index.html`, `findings.html`, `scenarios.html`, `europe.html`, `methodology.html`, `sources.html`, `glossary.html`):

```html
<a href="/" class="site-logo" aria-label="synthesis.nexalps.com home">
  <span class="site-logo-mark">synthesis</span>
  <span class="site-logo-suffix">· Part 6</span>
</a>
```

Position: leftmost in the header bar, before the 6-item nav. Style: same font as nav items; muted colour for the suffix; hover state matches existing nav hover convention. The `index.html` landing page does NOT highlight the logo as active (logo is a home anchor, not a nav item).

### Tasks per problem

#### 1. Landing page rebuild (`index.html`)

- Keep: header + hero + stats panel + footer
- Remove: the existing Read-more 4-card block (added in Phase 1B as a structural placeholder)
- Add: 4 SM blocks under the stats panel using the locked headers + supports above. Use the existing `.sm-pyramid` / `.sm-header` / `.sm-support` CSS pattern; add a `.sm-cta` style (e.g., `font-size: 14px; color: var(--ring); text-decoration: none; &:hover { text-decoration: underline; }`) for the `Go deeper →` link. Each SM block is its own `.sm-pyramid` container (4 separate pyramids, not one with 4 SMs inside — keeps the visual rhythm consistent and lets each block link cleanly to its destination).
- Update meta-description if needed; it should remain the locked hero headline + lede.

#### 2. P1 corridor map (`findings.html` §3)

- Open `D-rastered.html` and copy the SVG render block + inline `CELL_MAP` JSON + interaction code (hover, focus, click, keyboard) into a new `<section>` replacing the current §3 grid markup in `findings.html`.
- Wrap in the existing `findings.html` section template (`<section class="container" role="region" aria-label="Corridor map">` + `<h2><span class="num">3.</span> ...</h2>` + intro paragraph if appropriate).
- Reuse the existing §3 explanatory paragraph: *"The map below sorts 36 European labour markets into three corridors based on how well their training and re-employment systems can keep up with AI-driven displacement..."*
- Add the toggle button (`Map view ↔ Beeswarm view`) and the iframe target — beeswarm view loads `B-beeswarm.html` from the explorations folder via iframe, OR (better) port the beeswarm render too into a sibling block within the same section that shows/hides on toggle. Pick whichever produces the smoother UX; the iframe approach worked in the mockup but may feel clunky inside the live page. If switching to inline beeswarm, keep the toggle state confined to the single section (don't carry filter state across views).
- Update CSS to use existing tokens; the mockup already uses `var(--class-i/ii/iii/iv)` so this should drop in cleanly.
- Mobile responsive: the mockup ships with `@media (max-width:480px)` padding tightening; preserve.
- Re-apply PostHog tracking: every country-region click + class-card click + toggle button = a tracked event. Use the existing event-naming convention from Phase 1A (e.g., `corridor_country_click`, `class_card_filter`, `view_toggle`).

#### 3. P2 fragility-class graphic (`findings.html` §4)

- Open `B-population-stack.html`, port the population-weighted stack render block into a new `<section>` replacing the current §4 4-card panel.
- Section heading: keep the existing *"Fragility Classes"* h2.
- Render two stacked bars (EU-27 + 36-market) with class-segment widths proportional to population share + count labels. Same CSS tokens as everywhere else.
- Mobile: bars stack vertically; segment widths scale.
- Each class segment is keyboard-focusable + hover/tap reveals the country list for that class (tooltip or inline panel).
- Re-apply PostHog tracking on segment-click + segment-hover (if hoverable).

#### 4. P3 cross-linking (`findings.html` §3 ↔ §4)

The country-region API contract is already documented inline in `D-rastered.html`:

- Each country = `<g class="country-region" data-code="..." data-class="..." tabindex="0" role="button" aria-label="...">`
- Class cards in §4 dispatch a custom event `class:filter` with `detail: { class: 'I'|'II'|'III'|'IV'|null }` on click
- The map listens for this event and applies/clears the `.dimmed` state on non-matching country regions
- Hover on a class segment in the §4 stack adds `.ringed` to matching country regions in §3 (transient ring)
- Esc clears any sticky filter state
- Click an active class segment again clears its filter

Wire one shared state machine module (suggested: `findings-cross-link.js` or inline IIFE at the bottom of `findings.html`) that owns:
- `activeFilter: null | 'I' | 'II' | 'III' | 'IV'`
- `applyFilter(cls)` — null clears
- `ringClass(cls, on)` — transient ring management
- `clearAll()` — Esc handler
- Event listeners on §3 country regions + §4 class segments

The mockups `phase2-explorations/3-cross-linking/A-hover-highlight.html` + `B-click-filter.html` are reference patterns; the `D-rastered.html` already implements both modes inline. Carry that implementation forward; do NOT rebuild.

#### 5. P4 weather-pattern viz (`scenarios.html` §2)

- Open `A-probability-shift-bars.html`, port the small-multiples block (3 regimes, 7 scenarios as horizontal bars per regime) into `scenarios.html` §2 replacing the current 3-card text panel.
- Section heading: keep existing *"Three Weather Patterns"* h2.
- The locked V1.1 SM 1 supporting paragraph (already in place from Phase 1B at the top of scenarios.html) frames the "tech-led recovery cluster" reading; do not duplicate that text inside §2. §2 is the visual; the V1.1 SM is the narrative.
- Add a single explanatory caption above the 3 small multiples that notes the cluster reading: *"Note: 'tech-led recovery' here refers to S1 Reinstatement Revival + S3 Jobs Transform, both tech-led optimistic scenarios. Their combined probability under growth is around 25%; under post-growth, around 5%."*
- Mobile: the 3 small multiples stack vertically; bar widths scale.
- Re-apply PostHog tracking on regime-card hover + scenario-bar hover.

#### 6. P5 europe panels (`europe.html`)

- Open `B-delta-callout.html`, port the primary view + delta strip into `europe.html` REPLACING the current side-by-side EU-27 / 36-market panels.
- Apply the **direction fix** (36-market → EU-27) per the table in "Phil-locked anchors" above.
- Primary panel = 36-market (the full read).
- Delta strip = "WHAT CHANGES IF YOU RESTRICT TO EU-27" with 8 stat tiles, each showing `36-market_value → EU-27_value` and a one-liner narrative reframed for the restriction direction.
- Variation-guard callout + headline-finding pull-quote stay (already on `europe.html`).
- Phil-locked Europe Minto open at the top of the page (headline + sub-paragraph + 3 SMs) stays exactly as-is from Phase 1B.
- Mobile: primary panel stays, delta strip stacks tile-by-tile vertically.
- Re-apply PostHog tracking on delta-tile hover.

#### 7. §7 methodology note (`methodology.html`)

- Append the Phil-locked "Why eight scenarios, not more" paragraph to §7 as a new sub-section. Use a `<details>` collapsible if the §7 layout already uses that pattern; otherwise inline as a `<div class="callout">` or sub-section heading + body.

#### 8. Header / logo home anchor (all 7 pages)

- Insert the `<a class="site-logo" href="/">` block at the leftmost position of the existing nav strip on all 7 pages (incl. `index.html`).
- Add `.site-logo`, `.site-logo-mark`, `.site-logo-suffix` styles to the inline `<style>` block on each page (Phase 1A inlined CSS per page; preserve that pattern).
- The logo carries no `aria-current="page"` anywhere; it's a navigational anchor, not a page label.

#### 9. PostHog tracking re-apply

- Phase 2A mockups deliberately omitted PostHog (per Phase 2A brief constraint).
- Every new interactive in Phase 2B must carry tracking. Use the existing event-naming convention from Phase 1A (verb_object pattern: `corridor_country_click`, `class_segment_filter`, `regime_card_hover`, `delta_tile_hover`, `view_toggle`, `landing_sm_click`).
- Verify the PostHog token (`phc_bjax6jdRxYJAaExodvALjRru8AQzUSbYFNlWlXiJM8A`) appears once per page on all 7 pages post-build.

### Constraints

- **All copy is Phil-locked verbatim.** No authoring; structural insertion only. If a phrase looks awkward to you, surface in report-back; do NOT edit.
- **No new design tokens.** Use existing `--bg`, `--fg`, `--muted`, `--ring`, `--card`, `--card-border`, `--radius-md`, `--radius-sm`, `--class-i/ii/iii/iv`. New CSS classes are fine; new tokens are not.
- **Existing SOT.** All visualisations read from `site/data.json` with cache-busting fetch (`{cache:'no-store'}`). Do not modify `data.json`. Do not modify `layer-6-deliverable-data.json` (the master SOT).
- **No external libraries.** Inline SVG / CSS only.
- **Phase 1B IA preserved.** 7 pages, 6-item nav (Findings | Scenarios | Europe | Methodology | Sources | Glossary), `.closer`→`.conclusion` rename held, cache-busting fetches everywhere.
- **No emoji** anywhere.
- **PostHog tracking** on every interactive (per task 9).
- **Mobile responsive at 900 px breakpoint** for all new visuals; test at 375 / 768 / 1280.
- **Accessibility.** Every interactive keyboard-focusable; colour-only signal supplemented by labels; ARIA roles where appropriate; Esc clears any sticky state.
- **Phil does all git commits.**

### Verification (before reporting back)

1. All 7 HTML pages parse cleanly; zero console errors on each.
2. **Landing page**: hero + stats + 4 SM blocks present, each SM has locked header + locked support + `Go deeper →` CTA linked to the correct page; no Read-more cards remaining.
3. **`findings.html` §3**: rastered map renders with 1938 cells, all 36 country regions present with class-colour fills; hover/tap detail panel works; toggle to beeswarm works; click on a class card in §4 dims non-matching regions in §3; Esc clears.
4. **`findings.html` §4**: population-weighted stack renders with EU-27 + 36-market bars; segment widths reflect class %; segment hover/click cross-links to §3.
5. **`scenarios.html` §2**: 3-regime small multiples render with 7 horizontal bars each, bar widths reflect probabilities; cluster-caption sentence present.
6. **`europe.html`**: primary 36-market panel renders + delta strip with 8 stat tiles + direction reversed (36-market → EU-27 per the locked table); variation-guard + headline pull-quote retained.
7. **`methodology.html` §7**: "Why eight scenarios, not more" paragraph appended verbatim.
8. **All 7 pages**: site-logo anchor leftmost in nav, links to `/`; nav unchanged otherwise (still 6-item: Findings | Scenarios | Europe | Methodology | Sources | Glossary).
9. **All interactives carry PostHog event tracking** with verb_object naming.
10. **Mobile responsive**: every new visual collapses cleanly at 375 / 768 / 1280; no horizontal scroll; cells/bars/tiles scale as designed.
11. **Accessibility**: every interactive keyboard-focusable; tab order sensible; Esc clears sticky filter state; colour-only signals supplemented (e.g., class-segment widths supplemented by count labels).
12. **No new design tokens** introduced anywhere; all colours/spacings/radii via existing variables.
13. **`data.json` + `layer-6-deliverable-data.json` unchanged**; cache-busting fetch on every consumer page.
14. **Phase 1B IA preserved**: 7 pages, 6-item nav, `.closer`→`.conclusion` held, no `.closer` residual.
15. **No emoji** anywhere in HTML body.
16. **Folder size** check: `< 800 KB` excluding `data.json` (Phase 1B was 273.5 KB; +5 visuals + cellMap inline JSON adds ~20–30 KB; reasonable budget).

### When done — report back to master session with

1. File-by-file line count diff (additions / removals).
2. Verification checklist (1–16) — pass/fail per item.
3. Static screenshot or rendered-HTML preview of:
   - Landing page (desktop + mobile)
   - findings.html §3 + §4 with cross-link active state
   - scenarios.html §2
   - europe.html (delta strip showing the direction fix)
4. PostHog event-tracking audit — list every new tracked event + the page it fires on.
5. Cross-link state-machine summary — confirm shared state across §3 + §4 with `applyFilter / ringClass / clearAll` API.
6. Any constraint violations or design decisions that needed flagging (e.g., did inline beeswarm work better than iframe? if so, document).
7. Bundle W readiness — anything that surfaced during 2B that Bundle W (Minto propagation across deliverable docs) should account for. Specifically: the landing-page Minto pyramid is now the canonical executive-summary structure; Bundle W's one-pager rewrite mirrors this shape (same hero + 4 SMs).
8. Phase 3 / deploy readiness flags — anything that needs Phil's attention before the single coherent launch.
9. Any candidate brain captures (likely none; bounded execution).

If context fills before all 9 tasks are complete, report back at the natural midpoint (after tasks 1, 2, 4, 8 — landing + findings + nav) and resume in Phase 2B.2 covering tasks 3, 5, 6, 7, 9 (P2 + P4 + P5 + methodology + PostHog).

## END PROMPT
