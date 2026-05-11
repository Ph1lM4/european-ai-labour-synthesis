# Handover Prompt — Phase 2K: Site Graphics Build (2J Micro-Iterations + Audit Path X Top 3)

Bounded build session. Combines three 2J micro-iterations (post-Phil-review) with the Path X top-3 audit candidates from `site-graphics-density-audit-report-2026-05-08.md`. **Output mode: live build + verification.** Single render target — site (ai-project style, no Nexalps). PDF parity for any cross-page graphic deferred to Bundle N3. ~5 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** Five small builds; code-craft applies to each.

---

## Research scope

**Corpus-only.** Inputs: synthesis-site post-2J state + audit report + sister-layer site at `reskilling-site` (port 3005) for funnel-pattern port. No external WebSearch.

---

## Context

Phase 2J landed 2026-05-08 (corridor map redraw, Web Mercator, ESRA-style dots, headers simplified to *"Lens 1 absorption ratio · 36 markets, theory-anchored corridor edges 1.20 / 2.80"* / *"Lens 1 absorption ratio · 36 markets"*). Phil's review surfaced 2 micro-iterations. The site graphics density audit (parallel sub-session) surfaced 22 candidates with a top-3 priority shortlist. This phase consolidates both into one focused build.

**Style lock — site stays in ai-project style.** No Nexalps restyle. PDF deliverables (Bundle N3) handle Nexalps style separately. Cross-page graphics that would benefit from PDF parity (e.g., reskilling-capacity funnel) ship in ai-project style on the site here; Bundle N3 builds the Nexalps PDF version separately.

---

## START PROMPT

Build six items into the synthesis site: three 2J micro-iterations + three audit candidates from the Path X shortlist. ai-project style only. Single sub-session.

### Read FIRST (absolute paths)

**Phase 2J context:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/phase-2j-corridor-map-redraw-report-2026-05-08.md` — particularly the "Phil-iteration handoff" section (items 2 + 4) and section-header simplification context
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — current post-2J state (corridor map block, geo-note paragraph)

**Audit context:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site-graphics-density-audit-report-2026-05-08.md` — per-page candidate table + top-3 priority shortlist + chart-box / D3 v7 sister-layer port idiom notes

**Sister-layer reference (for funnel port):**
- `reskilling-site` (port 3005, http://localhost:3005) — locate the reskilling-capacity funnel / sankey on `transitions.html` (per audit). Inspect implementation: `chart-box` CSS class, D3 v7 idiom, data-binding pattern.

**Synthesis-site files touched:**
- `site/findings.html` — micro-1 (microstate radius), micro-2 (geo-note copy), micro-3 (hit-area `<path>` rendering in `renderMap()` + CSS), build-1 (§2 stack-bar), build-3 (reskilling funnel §5)
- `site/methodology.html` — build-2 (§1 five-lens card-grid)
- `site/dotmap-data.json` — extended schema: `polygon_path` field per country (micro-3)
- `tools/dotmap-gen.py` — extended to emit `polygon_path` per country (micro-3)
- `site/data.json` — read-only (no edits expected)

### The six items

#### 1. 2J micro-1 — Microstate dot radius bump (~5 min)

LU / LI / MT render at 1–2 dots and visually disappear at default 3.4 px. Bump those countries to 4.0 px so they read as a slightly larger marker without breaking the no-labels lock.

CSS-only edit in `site/findings.html`. Add a rule scoped to `.country-region` groups for those ISO-2 codes:

```css
#map-svg .country-region[data-country="LU"] circle,
#map-svg .country-region[data-country="LI"] circle,
#map-svg .country-region[data-country="MT"] circle { r: 4 !important; }
```

(or equivalent — sub-session picks the cleanest selector that matches the existing CSS conventions in the file).

Verify: visual screenshot of the corridor map post-edit; LU / LI / MT visible without compromising surrounding country density.

#### 2. 2J micro-2 — Geo-note copy strengthening

Current geo-note (under the corridor map) reads: *"Each cluster of dots is one country. Dot size encodes outline fidelity (smaller dots feather coastlines and narrow regions, larger dots fill country interiors); colour encodes fragility class. Web Mercator projection, with country geometry from Natural Earth 1:50m. No labels — identification via hover or click. Ukraine appears as a Class IV reference panel at reduced opacity."*

Add one sentence to clarify dot **count** under Mercator (per Phil-iteration item #4): *"Dot **count** per country reflects projected map area, not displacement scale — colour carries the corridor and class signal."*

Suggested insertion point: between the "colour encodes fragility class" sentence and the "Web Mercator projection" sentence. Sub-session picks placement.

Verify: visual screenshot of the geo-note block post-edit; sentence reads cleanly.

#### 3. 2J micro-3 — Per-country hit-area for hover/click (NEW — ~60 min)

**Problem:** Hover/click on the corridor map currently fires only when the pointer lands on a dot fill. Gaps between dots are non-interactive. With smaller dots / smaller graphic / mobile viewports, hitting a country precisely is hard.

**Fix:** Emit an invisible projected country polygon as a hit-area overlay per country. Pointer events on the polygon trigger the same country-region handlers that currently fire on dots.

**Implementation:**

1. **Extend `tools/dotmap-gen.py`** to also emit per-country projected polygon SVG path:
   - Reuse the same Natural Earth 1:50m source loaded for dot generation
   - Apply the same Web Mercator projection (with same canvas bounds + transforms) to each country's polygon
   - Convert projected polygon to SVG `d` attribute string (M/L commands; multi-polygon countries become compound paths with `M ... L ... Z M ... L ... Z`)
   - Emit per-country in `dotmap-data.json` as `polygon_path: "<d-string>"`
   - Skip Ukraine (reference panel) — UA polygon optional, sub-session decides whether to include based on whether UA reference panel needs hit-area too (recommend yes for consistency)
2. **Update `site/dotmap-data.json` schema** — add `polygon_path` field per country in the `countries` object
3. **Update `findings.html` `renderMap()`** — for each country group, emit `<path class="hit-area" d="..." aria-hidden="true">` as the first child of `<g class="country-region">`, BEFORE the dots. The path renders behind the dots due to SVG paint order.
4. **CSS in `findings.html`:**
   ```css
   #map-svg .country-region path.hit-area {
     fill: transparent;
     pointer-events: all;
     cursor: pointer;
   }
   #map-svg .country-region:hover path.hit-area,
   #map-svg .country-region:focus-within path.hit-area { /* no visible change; handler-driven highlight on dots */ }
   ```
5. **Event handlers** — existing handlers on `.country-region` (group level) should already capture pointer events from any descendant including the polygon. Verify no regression.
6. **Edge cases:**
   - Microstates (LU/LI/MT): polygon is small, hit-area still small. After micro-1 bump (radius 4.0 px), the hit-area should be ≥ the visible cluster. Verify visually.
   - Overlapping countries (LI inside CH/AT region): SVG paint order is document order. LI polygon must render AFTER CH/AT to receive events. Sub-session sorts country groups by polygon area descending so smaller countries land on top.
   - Multi-polygon countries (Greek islands, Croatian coast, Italian Sicily/Sardinia, Norway with Svalbard): emit as compound path or as multiple `<path>` siblings within the group.

**Verify:**
- Visual: SVG looks identical to pre-edit (no visible change from invisible polygon)
- DOM: each `<g class="country-region">` has at least one `<path class="hit-area">` as first child
- Hover: moving pointer anywhere within DE / FR / ES / NO / SE country shape (not just on dots) triggers the detail panel
- Click: clicking anywhere within country shape sticky-toggles the detail panel
- Microstate hover: LU / LI / MT respond to hover within their polygon
- Keyboard: tab through country groups; focus order matches existing flow
- Console: no errors

#### 4. Audit build-1 — Findings §2 inline 9/9/15/3 stack-bar (~45 min)

Per audit: §2 currently presents the 9/9/15/3 fragility-class distribution in prose. Same numerics already render as a stack-bar in §4 of findings.html. Reuse §4 styling for an inline stack-bar in §2. No new D3, no new CSS class — port the existing pattern.

Sub-session reads §2 prose, identifies the exact insertion point, ports §4's stack-bar markup with §2-context labels (audit recommends inline placement adjacent to the prose claim).

Verify: visual screenshot of §2 post-edit; stack-bar renders correctly; numerics match §4.

#### 5. Audit build-2 — Methodology §1 five-lens card-grid (~60 min)

Per audit: methodology §1 (the "Five lenses" SM 1 support paragraph) currently lists the five lenses inline in prose: *"AI exposure, demographics, disruption pathways, reskilling capacity, and careers data."* Build a 5-card grid showing each lens with: lens name (bold), one-line description, source-layer reference (e.g., "Layer 1: AI Exposure", "Layer 4: Demographics", etc.).

Source content for each lens card from the SOT (`site/data.json` — Lens 1–5 metadata) or from the Specialist Appendix (`layer-6-deliverable-document.md` §2 specialist data anchors). Sub-session picks the source that has cleanest per-lens content.

Card design: minimal, ai-project style (matches existing card patterns on findings / scenarios pages). Responsive grid (5 columns desktop, 2-3 mobile, 1 narrow).

Verify: visual screenshot of methodology §1 post-edit; cards render correctly; content matches SOT.

#### 6. Audit build-3 — Reskilling-capacity funnel (port from reskilling-site) (~90 min)

Per audit: cross-page candidate; high priority because (a) serves findings + methodology with identical numerics (26% retirement / 80% needed / 7.55M reskill / 450K throughput / 15-yr backlog / 1–3 yr window), (b) direct port target exists in reskilling-site `transitions.html` sankey/funnel, (c) `chart-box` + D3 v7 idiom is portable across sister sites.

**Approach:**
1. Inspect reskilling-site `transitions.html` via local preview at port 3005 — locate the funnel/sankey block, identify CSS / data structure / D3 entry point.
2. Port the funnel structure to synthesis-site, adapting:
   - CSS: use synthesis-site dark-theme palette (NOT reskilling-site palette if it differs; check both)
   - Data: bind to synthesis-site values from `data.json` or hardcode the 6 numerics if not in the data layer
   - D3: load D3 v7 from CDN if not already loaded (check existing `<script>` tags)
3. Place on findings.html §5 (the "Stability isn't safety" / reskilling section — currently text-heavy with the 26% / 80% / 450K-year / 15-year-backlog prose).
4. Audit specifies cross-page; if methodology §3 also references the same numerics, consider a smaller variant or static reference there. Sub-session decides; default = single placement on findings §5.

**Important — site-version-only.** PDF/Nexalps version of the funnel is Bundle N3 territory; do NOT build a Nexalps-style export here. The site version uses synthesis-site palette + container conventions.

Verify: visual screenshot of findings §5 post-edit; funnel renders correctly; data binding works; no console errors.

### Discipline (carry forward)

- **Style lock — ai-project only.** All five items render in synthesis-site current dark-theme palette. No Nexalps tokens.
- **Banned-phrase scan on own draft + commit messages.** Tier 1/2/3 reference: `skills/linkedin-playbook/references/banned-phrases.md`.
- **BR-19 fabrication discipline** — port real numerics from SOT / sister-layer site; do not invent values for cards / funnel labels.
- **Sister-layer graphic-port idiom** — `chart-box` + D3 v7 reuse pattern (per audit report capture candidate). Port the CSS class + D3 framework, adapt data binding only. Do not re-invent the funnel from scratch.
- **Audit-at-class** — for the methodology card-grid, if you find five cards working well, scan whether other multi-lens enumerations on the site (e.g., scenario list, regime list) would benefit from the same card pattern. Surface as audit-flag, do not auto-build.
- **No SOT edits.** `site/data.json` + `layer-6-deliverable-data.json` md5-verified pre/post. The five items are CSS / HTML / JS only.
- **File coordination** — three of the five items touch `findings.html`. Edit sequentially, verify each works before moving to the next; don't batch all three edits then test.
- **Time budget: 3–4 h.** If the funnel port balloons (chart-box framework conflicts with synthesis-site, D3 v7 not loaded, etc.), surface scoping issue and stop. Funnel is the single most complex item; the other four are small.

### Verification (close with this)

```
md5 site/findings.html site/methodology.html site/dotmap-data.json site/data.json
```

`findings.html` + `methodology.html` + `dotmap-data.json` change. `data.json` md5 unchanged.

Visual checks via preview:
- Map: LU/LI/MT visible (micro-1)
- Geo-note: new sentence reads clean (micro-2)
- Map hit-area: hover anywhere within DE / FR / NO country shape triggers detail panel; click anywhere within country sticky-toggles (micro-3)
- §2: stack-bar inline (build-1)
- §1 methodology: 5-card grid renders (build-2)
- §5: funnel renders (build-3)

DOM checks via `preview_eval`:
- Each `<g class="country-region">` has `<path class="hit-area">` as first child (micro-3)
- No console errors
- No missing data bindings (funnel)
- Card-grid responsive at narrow viewport
- Microstate hit-areas (LU/LI/MT) match dot extent or larger

Banned-phrase grep across edited files: 0 hits.

### Report-back format

Single markdown file: `phase-2k-site-graphics-build-report-2026-05-08.md`. Same directory. Mirror Phase 2J report structure:

1. **TL;DR** — 6–8 bullets covering the 6 items
2. **Per-item summary** — what changed, before/after screenshot pointer, edge cases handled
3. **Verification checklist** — md5 audit + visual + DOM checks per item
4. **Phil-iteration handoff** — flag 2–3 things you're least sure about (e.g., funnel placement on findings vs methodology, card-grid responsive breakpoint, microstate radius value)
5. **Brain capture candidates** (if any) — likely the chart-box port idiom validation as additional data point

---

## Out of scope

- Nexalps-style PDF versions of any graphic (Bundle N3)
- Other audit candidates beyond top 3 (defer to N3 or later batch)
- Phase 2J corridor-map further iterations beyond microstate radius + geo-note copy
- IA changes / new pages
- `site/data.json` edits — graphics consume the data layer, don't redefine it
- Brain skill enrichment — capture candidates surface for Phil per Rule 12

---

*This brief is the dispatch prompt for Phase 2K. Sub-session lands 3 micro-iterations + 3 audit-build items in one focused session. ai-project style. ~5 h. Output: live changes on findings.html + methodology.html + dotmap-data.json + tools/dotmap-gen.py, plus report.*
