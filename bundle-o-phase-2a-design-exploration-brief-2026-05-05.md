# Design-Exploration Brief — Bundle O Phase 2A: Visual Alternatives

Bounded design-exploration session. Produces 2-3 visual alternatives per element across five design problems on the Phase 1B site, with a one-paragraph recommendation per problem. Output is rendered HTML mockups in a sibling `site/phase2-explorations/` folder + a single `RECOMMENDATIONS.md`. No edits to live site. Phil locks directions; Phase 2B (separate handover) builds the locked alternatives into the live site. ~150–180 min.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Phase 1B completed 2026-05-05 (20/20 PASS) — site has 7 pages, full Minto-pyramid IA, S8 renamed to Polycrisis Drag, Bundle X aggregate panels live on `europe.html`. Five visual elements remain at Phase 1A treatment (text-or-grid only) and need design-exploration before the single coherent launch:

1. **Corridor map** (`findings.html` §3) — current: 4×9 colour-coded grid of 36 cells. Reads as a heatmap-of-classes, not as a country-by-country narrative.
2. **Fragility-class graphic** (`findings.html` §4) — current: 4-card panel listing classes I/II/III/IV with country names. Reads as an enumeration, not as a distribution.
3. **§3↔§4 cross-linking** (`findings.html`) — current: §3 and §4 are independent blocks; no interaction between them.
4. **Weather-pattern viz** (`scenarios.html` §2) — current: 3-card text panel describing growth / secular-stagnation / post-growth regimes. Reads as a glossary entry, not as a probability-shift visualization.
5. **Europe aggregate panels** (`europe.html`) — current: two side-by-side tabular stat-blocks (EU-27 / 36-market). Reads as a comparison table; misses the "EU-27 is a subset of 36" structural relationship and the asymmetry callouts.

Phase 2A is *exploration only*. The sub-session produces alternatives + recommendations; Phil reviews and locks directions; Phase 2B builds. This separation matters because design exploration generates options most of which won't ship — committing to live-site changes per option would be wasteful.

---

## START PROMPT

I need you to produce visual alternatives for five design problems on the Phase 1B site and recommend one per problem. Output is rendered HTML mockups + a recommendations document. Do NOT modify the live site files; mockups live in a new `site/phase2-explorations/` folder. Phil reviews, locks one direction per problem, and dispatches Phase 2B build separately.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — current corridor map (§3) + fragility-class panel (§4) + Italy callout. Source for problems 1, 2, 3.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — current weather-pattern panel (§2) + spectrum bar + sparkline + probability table. Source for problem 4.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html` — current EU-27 / 36-market tabular panels + variation-guard callout + headline pull-quote. Source for problem 5.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — full SOT (per-country fields + scenario probabilities + Bundle X aggregate block). All visualizations read from this; do not introduce new data.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-o-phase-1b-ia-restructure-handover-2026-05-05.md` — Phase 1B handover for register reference + design-token conventions.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/master-session-handover-2026-04-30.md` — Phil's editorial register (storytelling > methodology paper; plain conversational; no internal jargon).

### Output structure

Create `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/`:

```
phase2-explorations/
├── RECOMMENDATIONS.md           # one-paragraph recommendation per problem (5 paragraphs)
├── 1-corridor-map/
│   ├── A-geographic.html        # alternative A
│   ├── B-beeswarm.html          # alternative B
│   ├── C-sortable-list.html     # alternative C (if ≥3)
│   └── README.md                # what each alternative does + analytical content it surfaces
├── 2-fragility-class-graphic/
│   ├── A-pyramid.html
│   ├── B-population-stack.html
│   ├── C-sankey.html (optional)
│   └── README.md
├── 3-cross-linking/
│   ├── A-hover-highlight.html   # both §3 + §4 in same file with interaction
│   ├── B-click-filter.html
│   └── README.md
├── 4-weather-pattern-viz/
│   ├── A-probability-shift-bars.html
│   ├── B-icon-cards.html
│   ├── C-flow-diagram.html (optional)
│   └── README.md
└── 5-europe-aggregate-panels/
    ├── A-subset-wrapper.html    # 36 wraps EU-27 visually
    ├── B-delta-callout.html     # primary view + delta strip
    ├── C-stacked-comparison.html (optional)
    └── README.md
```

Each mockup is a **standalone HTML file** that:
- Imports the existing site CSS tokens via inline `<style>` block (copy from europe.html)
- Reads from `../data.json` (relative path) using `fetch('./data.json', { cache: 'no-store' })`
- Renders the proposed visual at desktop + verifies mobile collapse via media query
- Carries a top-of-page `<header>` with the problem name + alternative letter (e.g., "Problem 1 / Alternative A — Geographic Map")
- Uses **only existing CSS variables** (--bg, --fg, --muted, --ring, --card, --card-border, --radius-md, --radius-sm). No new colour tokens, no SVG icon libraries beyond inline SVG you author, no external chart libraries (no D3, no Chart.js — D3 acceptable IF a problem genuinely requires it; flag in recommendation).

Each `README.md` in the problem folder explains:
- The analytical content the visual must surface (1-2 sentences)
- What each alternative does differently (1 sentence each)
- Trade-offs (accessibility, mobile, build cost, story clarity)

### The five design problems

#### Problem 1 — Corridor map (`findings.html` §3)

**Analytical content the visual must surface:**
- 36 European labour markets distributed across 3 corridors (C1/C2/C3) and 4 fragility classes (I/II/III/IV)
- Cluster patterns: 5 Nordics + 4 Continental peers in Class I; 15 in Class III; 3 in Class IV (BA/MK/RS/TR — borders/candidates)
- Each country has a corridor placement *and* a fragility class — two dimensions
- Country-level mechanism (hover/tap reveals one-line story)

**Current treatment:** 4×9 grid of cells, colour-coded by Class. Loses the geographic-clustering story; reads as a heatmap of an abstract space.

**Explore:**
- **A — Geographic map.** Inline SVG choropleth of Europe with country shapes filled by Class colour. Pros: clusters legible at a glance (Nordics = green block, Balkans = red); ties to the "borders not within" Europe-page Minto SM 2. Cons: SVG path data is heavyweight; small countries (LU, MT) need callout treatment.
- **B — Beeswarm on Lens 1 ratio.** Horizontal axis = Lens 1 ratio (1.0–3.5); each country = a circle positioned by its ratio, coloured by Class, with corridor-edge vertical lines (1.20 / 2.80). Pros: shows continuous variation + the corridor-edge correction story; small countries don't overflow. Cons: loses geography; readers must know what "Lens 1 ratio" means before the visual lands.
- **C — Sortable / filterable list (optional, if A+B don't bracket the design space).** Table-like with sort by Class / corridor / region; click a country to expand the mechanism line. Pros: accessibility + works on mobile; surface country-level mechanism as primary not secondary. Cons: less emotionally vivid; readers won't remember the cluster shape.

#### Problem 2 — Fragility-class graphic (`findings.html` §4)

**Analytical content the visual must surface:**
- 9 / 9 / 15 / 3 distribution across Classes I / II / III / IV
- Population-weighted distribution differs from country-count distribution (EU-27 Class I = 25.6% of working-age pop vs 33% of country count; 36-market Class IV = 15.7% pop vs 8.3% count)
- Each class has a *rule* (the constraint that lands a country in it) — Class I = stable under softer rule; Class II = fragile under one routine variant; Class III = baseline-C3; Class IV = active cascade signals
- The "softer rule produces 9 robust; strict rule produces 0" finding is a property of Class I specifically

**Current treatment:** 4-card panel listing each class with its countries. Reads as enumeration; misses distribution + population weighting + rule.

**Explore:**
- **A — Pyramid / funnel.** 4-tier funnel widening from Class I (9 markets, narrow top) to Class III (15 markets, widest tier) and back to Class IV (3, narrow bottom — separated visually because cascade is qualitatively different). Pros: distribution legible; the Class III bulge is the visual punchline. Cons: pyramid metaphor implies hierarchy; readers may infer Class I is "best" and Class IV is "worst" linearly when Class IV is qualitatively distinct.
- **B — Population-weighted stack.** Stacked horizontal bar showing % of European working-age population in each class, with country counts as labels. Two bars: EU-27 + 36-market. Pros: surfaces population vs count asymmetry directly (the Phase 2 readiness flag #1 from europe.html); aligns with Bundle X aggregates. Cons: loses class-by-class country list (would need a second row beneath).
- **C — Sankey from corridor to class (optional).** Left side: corridors C1/C2/C3 (ribbon widths = country count); right side: classes I/II/III/IV; ribbons connect baseline corridor to fragility class. Pros: shows that Class III is "in C3 already" and Class II is "in C1/C2 baseline but fractures." Cons: complex; readers without chart literacy will skip it.

#### Problem 3 — §3↔§4 cross-linking (`findings.html`)

**Analytical content the interaction must surface:**
- Every country lives in both a corridor (§3) and a class (§4) — interaction makes the relationship visible without forcing a Sankey
- Hovering a country in the map highlights its class card; clicking a class card highlights its countries on the map
- Reverse direction: hovering/clicking a class filters the map to that class's countries

**Current state:** independent blocks; no interaction.

**Explore:**
- **A — Bidirectional hover-highlight.** Hover a cell in §3 → §4's matching class card gets `--ring` border. Hover a class card in §4 → §3's matching cells get `--ring` outline. Pros: always-on, no clicks required; works on touch via tap. Cons: hover doesn't exist on touch devices; needs tap-fallback.
- **B — Click-to-filter.** Click a class in §4 → §3 dims non-matching cells to 30% opacity; a "showing Class N (n countries)" badge appears with a clear-filter button. Pros: works on touch; intent-driven. Cons: requires explicit user action; first-time readers won't discover it.

Recommend both A + B can coexist (hover for desktop discovery + click for mobile + filter persistence). One recommendation paragraph stating the combined pattern is acceptable.

#### Problem 4 — Weather-pattern viz (`scenarios.html` §2)

**Analytical content the visual must surface:**
- Three regimes (growth / secular stagnation / post-growth) reshape scenario probabilities
- The dramatic shift: tech-led recovery 25% → 5%; Climate Adaptation Boom 22% → 30% under post-growth
- 38.5% of EU-27 working-age population lives under post-growth regime — this isn't a corner case
- Regime is country-level and stable on a multi-year horizon (not a scenario in itself)

**Current treatment:** 3-card text panel. Reads as glossary; misses the probability-shift drama and the population callout.

**Explore:**
- **A — Probability-shift bars.** Three small-multiples (one per regime), each showing 7 scenarios as horizontal bars sorted by probability. The same scenario appears in different positions across the three small-multiples; the visual surfaces "Reinstatement Revival sits at the top under growth, near the bottom under post-growth." Pros: shift is the data; bars are the right form. Cons: requires three-way visual comparison.
- **B — Weather-icon cards (lightweight upgrade).** Keep the 3-card structure; add a single inline-SVG icon per regime (sun / partly-cloudy / overcast or similar) + the modal scenario per regime as a pull-quote inside the card + the population share. Pros: low build cost; survives mobile. Cons: icons are decorative rather than data-bearing; doesn't surface the shift.
- **C — Flow / sankey diagram (optional).** Left side: 7 routine scenarios (with growth-regime probabilities as ribbon widths); right side: same 7 scenarios with post-growth probabilities. Ribbons cross to show how rank changes. Pros: visceral; shift is the visual. Cons: complex; secular-stagnation regime would need a second flow.

#### Problem 5 — Europe aggregate panels (`europe.html`)

**Analytical content the visual must surface:**
- EU-27 is a strict subset of 36-market — geographically and statistically
- Class IV asymmetry: EU-27 = 0 markets, 36-market = 3 markets. The cascade pressure sits at the borders
- Both aggregates produce C2 corridor headline; the difference is the distribution underneath
- Population-weighting: 36-market includes more post-growth pop share (40.2% vs 38.5%)

**Current treatment:** two side-by-side tabular panels (EU-27 left, 36-market right). Reads as a comparison table; misses the subset-superset relationship.

**Explore:**
- **A — Subset-wrapper.** 36-market panel as an outer container; EU-27 panel as an inner panel sitting inside it; the 9-country delta (EFTA-4 + UK + 4 candidates) labelled as the "ring" between them. Pros: dramatises the subset relationship; the Class IV asymmetry sits in the ring (where it analytically belongs). Cons: complex layout; nested cards read as visually heavy.
- **B — Primary view + delta strip.** Primary panel = 36-market (the full read). Above it, a delta strip showing what changes when you restrict to EU-27 (Class IV: 3→0; population share post-growth: 40.2%→38.5%; etc.). Pros: foregrounds the analytical surface (variation IS the read, per the variation-guard); one read, not two. Cons: loses the side-by-side comparison some readers expect.
- **C — Stacked comparison (optional).** Both panels collapsed into a single stat-grid where each stat is a paired EU-27 / 36-market comparison with delta arrow. Pros: compact. Cons: density-heavy; loses narrative.

### Constraints

- **No live-site edits.** All output goes to `site/phase2-explorations/`. Live site stays at Phase 1B state.
- **No new design tokens.** Use only existing `--bg`, `--fg`, `--muted`, `--ring`, `--card`, `--card-border`, `--radius-md`, `--radius-sm` (and the existing fragility-class colour map: I=green / II=amber-light / III=amber / IV=red, used in `findings.html`). If a problem genuinely needs a new token to land, flag in the recommendation; do not introduce it in the mockup.
- **No external libraries.** Inline SVG only. No D3, no Chart.js, no Mapbox, no Leaflet. If Problem 1A (geographic map) needs SVG path data for country shapes, embed a single minimal European-countries SVG (CC0-licensed; flag the source in the README). If a problem genuinely requires a charting library, flag it in the recommendation rather than importing it.
- **Mobile responsive.** Every alternative must collapse cleanly below 900px (matching the existing site breakpoint). Test at 375w / 768w / 1280w.
- **Accessibility.** Every interactive element keyboard-focusable; colour-only signalling supplemented by labels or patterns; ARIA roles where appropriate. The corridor-map alternatives in particular must be navigable without mouse.
- **No new copy.** All mockups use Phil-locked copy from the live site (headlines, callouts, labels). If an alternative requires a new label, surface it as a `// TODO author` comment in the mockup and a flag in the recommendation.
- **Editorial register applies to visuals too.** Storytelling > methodology paper. The corridor map should read as "here is Europe, country by country," not as "here is a heatmap of an analytical space." A visual that requires the reader to learn vocabulary before it lands fails the register.
- **No emoji** anywhere.
- **PostHog tracking unchanged** (mockups don't carry tracking; the build phase 2B reapplies it).
- **Phil does all git commits.**

### Recommendation paragraph structure (per problem)

In `RECOMMENDATIONS.md`, write one paragraph per problem (5 paragraphs total) using this shape:

> **Problem N — [name]:** Recommend Alternative [letter]. [One sentence on what it surfaces best.] [One sentence on what it loses vs the alternatives.] [One sentence on build cost — minor / moderate / heavy.] [If genuinely required, flag any new design token / library / accessibility-non-trivial cost so Phil decides at lock time.]

Keep paragraphs to 4-5 sentences max. Phil reads all 5 paragraphs in one sitting and locks directions — overlong paragraphs slow that.

### Verification (before reporting back)

1. `site/phase2-explorations/` directory created with the 5 problem subfolders + `RECOMMENDATIONS.md`.
2. Each problem has 2 mockups minimum, 3 if the design space genuinely needs the third (per "if A+B don't bracket the design space" guidance).
3. Every mockup is a standalone HTML file that opens cleanly in a browser without external dependencies.
4. Every mockup reads from `../data.json` (cache-busting fetch); no hardcoded scenario probabilities or country lists.
5. Every mockup uses only existing CSS tokens; any new-token need is flagged in `RECOMMENDATIONS.md`.
6. Every mockup collapses to mobile (375w) without horizontal scroll or content overflow.
7. Every interactive element keyboard-focusable; colour-only signal supplemented.
8. `RECOMMENDATIONS.md` has 5 paragraphs (one per problem), each ≤5 sentences, each names a recommended alternative.
9. Live site (`findings.html`, `scenarios.html`, `europe.html`, all other 4 pages) untouched — `git status` shows only new files in `site/phase2-explorations/`.

### When done — report back to master session with

1. Folder structure of `site/phase2-explorations/` (tree).
2. Per-problem summary: alternatives produced + recommended alternative + 1-line rationale.
3. Verification checklist (1–9) — pass/fail per item.
4. Any constraint violations or flags (new token needed, library needed, accessibility cost, etc.).
5. Mockup-file open URLs (relative paths) so Phil can preview each in the browser.
6. Build-cost estimate for Phase 2B per recommended alternative (rough hours; minor / moderate / heavy).
7. Cross-problem dependencies — e.g., if Problem 3 (cross-linking) is locked, does it constrain Problem 1's choice (the corridor map alternative must support hover-highlight + class-filter)? Surface any locks-that-constrain-other-locks.
8. Phase 2B readiness — anything that surfaced during exploration that Phase 2B build should account for.
9. Any candidate brain captures (likely none; bounded exploration).

## END PROMPT
