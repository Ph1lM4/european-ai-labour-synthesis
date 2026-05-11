# Handover Prompt — Bundle O Phase 1B: IA Restructure + Polycrisis Drag Rename

Bounded composition session. Restructures the Phase 1A site (5 HTML pages) into a Minto-pyramid information architecture (split landing/findings, new europe.html, within-section Minto on every drill-down), applies the global S8 rename (Concurrent-Crisis Cascade → Polycrisis Drag) across SOT + lens spec + all site files, and bundles trivial cleanups (`.closer` → `.conclusion` CSS rename, cache-busting fetch on new pages). Pure structure + locked-text injection; no copy authoring (V1.1 SMs are Phil-locked verbatim). ~120–150 min.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Phase 1A completed 2026-04-30 (19/19 PASS) — site copy rewritten, scenario codes reset to S1–S8, plain-language discipline applied, bundle/phase scaffolding scrubbed. Bundle X completed same-day (13/13 PASS) — pan-European EU-27 + 36-market aggregates added to the SOT under `cross_cutting_findings.pan_european_aggregate`.

Phase 1B is the structural step that turns the Phase 1A content site into the Minto-pyramid public site. Three structural changes:

1. **Split landing/findings.** Current `index.html` carries both the headline summary and the full findings drill-down. Split into a short landing summary (still `index.html`) + full drill-down (renamed `findings.html`).
2. **New `europe.html` page.** Renders the Bundle X EU-27 + 36-market aggregates side-by-side at desktop, toggle at mobile. Phil-locked Minto open verbatim (in this handover).
3. **Within-section Minto on every drill-down page.** Findings, Scenarios, Methodology each get a 3-SM block under their locked headline using V1.1 supports (all 9 Phil-locked verbatim, in this handover).

Bundled with the IA restructure: a global S8 rename (Concurrent-Crisis Cascade → Polycrisis Drag) across SOT + lens spec + all site files. The deliverable-doc-side rename (Executive, Appendix, One-Pager, Einfache) defers to Bundle W when it propagates Minto across docs.

---

## START PROMPT

I need you to restructure the Phase 1A site into a Minto-pyramid information architecture (split landing/findings + new europe.html + within-section Minto on three drill-down pages), apply the global S8 rename to Polycrisis Drag, and bundle two trivial cleanups (CSS class rename + cache-busting fetch on new pages). All copy is Phil-locked verbatim — your job is structural insertion, not authoring.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` — current Phase 1A overview page; will be split.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — within-section Minto target (3 SMs to insert).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — within-section Minto target (3 SMs to insert).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/glossary.html` + `site/sources.html` — nav update only.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/glossary.tsv` — S8 rename target.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — frontend-consumed copy of SOT; europe.html reads from this; verify it carries `cross_cutting_findings.pan_european_aggregate`.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON; S8 rename target. Bundle X aggregate block lives at `cross_cutting_findings.pan_european_aggregate` with sub-blocks `eu_27`, `european_36`, `variation_guard_note`, `headline_finding_pan_european`.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec; S8 rename target (4 occurrences).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-o-phase-1a-content-rewrite-handover-2026-04-30.md` — Phase 1A handover for register reference.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-x-pan-european-aggregate-handover-2026-04-30.md` — Bundle X handover for aggregate-block schema.

### Phil-locked copy (verbatim — do NOT rewrite)

#### Landing page (`index.html` after split)

Strip everything currently between `<section role="region" aria-label="Prelude">` and the end of the page; keep the hero (h1 + lede + byline) and the summary stats panel. Add a short "Read more" block after the stats panel pointing to the four drill-downs (Findings, Scenarios, Europe, Methodology). Stats-panel content stays as-is from Phase 1A.

The hero block stays Phil-locked verbatim:

> **No European labour market is fully safe from AI-driven job displacement.**
>
> *We stress-tested 36 markets across five lenses and eight scenarios. Most countries can absorb the disruption only partially, and 15 are likely already beyond that threshold. Under the rules we applied, only nine have the statistical strength to hold up under pressure.*

#### Findings page (`findings.html` — renamed from `index.html` content)

Carries the full drill-down content currently in `index.html` §1–§6 + Italy callout + Conclusion. Insert the within-section Minto block after the existing §2 headline (`<h2><span class="num">2.</span> More than three-quarters of European labour markets sit in uncomfortable territory.</h2>`) and before the existing §2 prose paragraphs. The headline stays as the Minto-pyramid open; the three SMs are children of it.

**Findings within-section Minto (verbatim):**

**SM 1 header:** *"Even the safe nine aren't unconditionally safe."*
**SM 1 support:** Nine countries look safe under a *lenient* rule: a country may drift one corridor either way, as long as it never lands in the worst. Those nine are the five Nordics plus Belgium, France, Luxembourg, and the Netherlands. Under a *strict* rule (no drift at all), the safe count drops to zero — even Norway and Sweden fail. "Safe" here is a feature of the rule, not a permanent property of the labour market.

**SM 2 header:** *"The two hopes that were supposed to soften this don't hold."*
**SM 2 support:** Two "buffers" are often assumed to make AI displacement manageable: **retirement** and **retraining**. The retirement buffer is smaller than the story suggests: across 32 countries it covers about **26%** of displaceable employment, versus roughly **80%** that would be needed to "catch the fall." The retraining buffer is too slow for the timing: Europe needs to deeply reskill about **7.55 million** workers by 2035, but current throughput is about **450,000/year** — a **~15-year backlog** against a **1–3 year** displacement window.

**SM 3 header:** *"Stability isn't the same as safety."*
**SM 3 support:** Eight worker-protection economies look stable on the corridor map under the lenient rule: Belgium, Germany, Denmark, Finland, France, the Netherlands, Norway, and Sweden. But "stable" can mean the risk moved, not disappeared. The Nordics are more exposed to trade decoupling; the Continental group sits next to a large neighbour (the UK) with weaker worker protections. The bigger danger is not immediate job losses at home, but **AI investment and jobs relocating** to jurisdictions with thinner protections — stability at the price of capital-flight risk.

#### Scenarios page (`scenarios.html` — within-section Minto inserted)

Insert the within-section Minto block immediately after the page h1 (`<h1>Eight ways the next decade could play out and the most likely one depends on whether your economy is still growing.</h1>`) + lede paragraph, and before the existing §1 spectrum section. The headline stays as the Minto-pyramid open; the three SMs are children of it.

**Scenarios within-section Minto (verbatim):**

**SM 1 header:** *"Three economic regimes, three different sets of odds."*
**SM 1 support:** The same seven "routine" futures exist for every country, but the probabilities attached to them change by economic regime — because what's plausible in a growing economy is often not plausible when output isn't expanding. We separate *growth*, *secular stagnation*, and *post-growth*. In post-growth, the standard tech-led recovery path drops from about **25%** probability to about **5%**, while **Climate Adaptation Boom** rises from about **22%** to about **30%**. Same menu of futures; different odds.

**SM 2 header:** *"The optimism path narrows the further you push the regime."*
**SM 2 support:** For Austria, Luxembourg, and Turkey, only one of the routine futures consistently lands them in the safe corridor — and it is not the one most policy speeches assume. A tech-led reinstatement path is effectively closed off. Their best routine outcome runs through redirecting workers into climate-adaptation demand: healthcare, trades, and the green economy. Optimism remains possible. It just runs through climate, not conventional tech.

**SM 3 header:** *"S8 sits outside the spectrum on purpose."*
**SM 3 support:** Seven scenarios sit on an optimism↔pessimism spectrum, and their probabilities sum to **100%** within each regime. The eighth — **Polycrisis Drag** — is intentionally different: it assumes overlapping shocks (AI displacement plus decoupling pressure, demographic decline, climate stress, and fiscal strain), not a single dominant driver. Because there is no clean historical analogue for that combination, we treat it as a conditional "parallel risk," not simply the worst point on the routine spectrum.

#### Methodology page (`methodology.html` — within-section Minto inserted)

Insert the within-section Minto block immediately after the page h1 (`<h1>How we tested and what we deliberately left open.</h1>`) + lede paragraph, and before the existing §1 Methodology Overview section. Headline as Minto open; three SMs as children.

**Methodology within-section Minto (verbatim):**

**SM 1 header:** *"Five lenses, chosen because earlier parts of the project had already gathered the evidence."*
**SM 1 support:** This is a synthesis layer, not a new data-collection study. The five lenses map directly to evidence already assembled earlier in the project: AI exposure, demographics, disruption pathways, reskilling capacity, and careers data. The constraint was not "what lenses could exist in theory," but "what we can test rigorously today, with European data, across 36 countries."

**SM 2 header:** *"One calibration choice changes the headline."*
**SM 2 support:** This result hinges on one "dial" setting: where we draw the corridor cut-offs. Earlier drafts used cut-offs fitted to past literature (1.50 / 3.00). The published version uses theory-anchored cut-offs (1.20 / 2.80). With the strict rule (no wiggle room), the literature cut-offs produce three "Robust" markets; the theory cut-offs produce zero. That's why we show the choice clearly and keep it reversible: readers can recreate the earlier count from the threshold ladder. We chose the theory anchor because it matches the Lens 1 framework.

**SM 3 header:** *"What we deliberately left open."*
**SM 3 support:** Three known gaps bound this read:

1) **Occupational detail:** capability-floor breach is reported at a coarser job classification (2-digit ISCO) because the finer-grained European Social Survey microdata (3-digit) requires a multi-week application. The count here is a lower bound.
2) **Funding allocation:** the EU's adaptation funding through 2030 is not yet broken down by country. We can see the overall envelope, but not its distribution.
3) **Employer behaviour:** we cannot observe live signals like hiring, retraining launches, or redundancy plans because they sit behind paywalls or in proprietary HR systems.

#### Europe page (`europe.html` — NEW)

New page. Phil-locked Minto open verbatim:

> **Headline:** *Europe doesn't have one answer. It has 36.*
>
> **Sub-paragraph:** *We ran the same analysis at three scales: the EU-27, the full set of 36 European markets, and where the two diverge.*
>
> **SM 1 header:** *"There is no single European corridor → variation is the answer."*
> **SM 1 support:** On a population-weighted average, the EU-27 looks like it is coping. But that average spans a wide range. More than a third of EU-27 workers live in markets that are already past coping. The average tells you something about Europe. Only the country-by-country view shows the true shape of its parts, and therefore Europe as a whole.
>
> **SM 2 header:** *"The cascade pressure sits at the EU's borders, not within them."*
> **SM 2 support:** Look only at EU-27 member states and you will see no markets in active crisis. Add the four EU candidate countries and three appear — North Macedonia, Serbia, Turkey. That shifts the frame: cascade risk is not really an internal EU problem. It sits at the borders, in the markets the EU is still deciding whether to bring in.
>
> **SM 3 header:** *"For nearly 40% of EU-27 workers, the optimism path runs through climate, not tech."*
> **SM 3 support:** Almost 40% of EU-27 workers live in countries whose economies have stopped growing in the conventional sense — Germany, France, Austria, Sweden, Finland, Luxembourg. In those countries, the comforting story *"old jobs disappear, new ones appear at the same rate"* breaks down. Output is not expanding to make room for new jobs. What can work is redirecting workers into, for example, climate-adaptation jobs that grow as Europe decarbonises. For 40% of EU workers, the optimism path runs through climate, not conventional tech.

Below the Minto open, render two side-by-side aggregate panels (EU-27 and 36-market) reading from `data.json`'s `cross_cutting_findings.pan_european_aggregate.eu_27` and `.european_36`. Each panel surfaces: weighted Lens 1 ratio, headline corridor + label, class distribution (count + population-weighted %), regime mix (count + %), capability-floor breach count, squeeze cluster count. Render the `variation_guard_note` as a callout below the two panels. Render `headline_finding_pan_european` as a closing pull-quote.

**Responsive:** at viewport ≥ 900px render side-by-side; below 900px collapse to a primary-with-toggle (default to EU-27, toggle to 36-market). Match the corridor-map breakpoint already in `index.html`.

### S8 global rename map

Apply across SOT JSON + lens spec + all site files (excluding deliverable docs — those defer to Bundle W).

```
"Concurrent-Crisis Cascade" → "Polycrisis Drag"
"concurrent-crisis cascade" → "polycrisis drag"
"concurrent_crisis_cascade" → "polycrisis_drag"
```

Files in scope (10 occurrences across 5 files per pre-flight grep):

- `layer-6-deliverable-data.json` — 2 occurrences
- `layer-6-lens-framework.md` — 4 occurrences
- `site/scenarios.html` — 2 occurrences (spectrum bullet + sidenote)
- `site/methodology.html` — 1 occurrence
- `site/glossary.tsv` — 1 occurrence

**Pre-flight grep** to confirm scope before cutting:
```
grep -in "concurrent.crisis\|concurrent_crisis" \
  layer-6-deliverable-data.json \
  layer-6-lens-framework.md \
  site/*.html \
  site/glossary.tsv
```

**Verify zero residual after rename:** same grep returns 0 results.

**Glossary update:** the `site/glossary.tsv` entry for the scenario term needs both the term column and the definition column updated. If a separate `Concurrent-Crisis Cascade` row exists, rename the term row to `Polycrisis Drag`. If the term is referenced inside a multi-row scenario definition, update inline.

**Sidenote update on scenarios.html §1:** the sentence currently reads *"The eighth scenario — Concurrent-Crisis Cascade — has no analogue in the 580 years of historical disruptions covered in Part 3."* After rename: *"The eighth scenario — Polycrisis Drag — has no analogue in the 580 years of historical disruptions covered in Part 3."*

**Tooze attribution check:** if any prose attributes "polycrisis" to Adam Tooze or any other named author, drop the attribution. Use "polycrisis" as plain term-of-art for overlapping crises; the term pre-dates Tooze (originated with Edgar Morin) and does not require attribution in this context. Pre-flight grep:
```
grep -in "tooze\|morin\|adam tooze" \
  layer-6-deliverable-data.json \
  layer-6-lens-framework.md \
  site/*.html \
  site/glossary.tsv
```
Surface any hits in the report-back; rename target only if the rename itself surfaces a Tooze reference.

### Information-architecture restructure tasks

#### 1. Split `index.html` → `index.html` + `findings.html`

- **`findings.html` (NEW file, copy from current `index.html`):**
  - Copy current `index.html` verbatim.
  - Update page `<title>` to *"Findings — European AI Labour Map"*.
  - Update meta-description to the locked landing headline + sub-paragraph (same as index.html — landing headline is shared across all pages per Phase 1A convention).
  - Insert the Findings within-section Minto block (3 SMs above) immediately after the §2 headline `<h2>` and before its `<p class="section-sub">` line.
  - Keep all other sections (§1 Prelude, §3 Corridor Map, §4 Fragility Classes, §5 storytelling + `<details>` appendix, Italy callout, Conclusion) verbatim.
  - Update breadcrumb / nav: highlight "Findings" as active.

- **`index.html` (REWRITE as landing summary):**
  - Keep: header bar, hero (`<h1>` + `.lede` + `.byline`), summary statistics panel.
  - Drop: §1 Prelude, §2 Headline finding, §3 Corridor Map, §4 Fragility Classes, §5 folded findings + appendix, Italy callout, Conclusion. (All move to `findings.html`.)
  - Add (after stats panel): a short "Read more" block with four call-out cards or links pointing to **Findings**, **Scenarios**, **Europe**, and **Methodology**. Plain-text card pattern; no new visual elements (Phase 2 owns visual design).
  - Update meta-description to remain the locked landing headline + sub-paragraph.

#### 2. Build `europe.html` (NEW)

- Copy structural skeleton from `methodology.html` (closest match: short page with section blocks + Minto open).
- Insert the Phil-locked Europe Minto open verbatim (above).
- Add the two side-by-side aggregate panels (EU-27 + 36-market) reading from `data.json`.
- Add the variation-guard callout.
- Add the headline-finding pull-quote.
- Use the existing site CSS variables; no new colour tokens.
- Cache-busting fetch: `fetch('./data.json', { cache: 'no-store' })` (Phase 1A convention).
- Add to nav across all pages (see step 4).

**Responsive logic:**
```js
const breakpoint = 900;  // matches existing site convention
const isDesktop = window.matchMedia(`(min-width: ${breakpoint}px)`).matches;
// desktop: render both panels in a flex grid
// mobile: render one panel + toggle button defaulting to EU-27
```

#### 3. Within-section Minto promotion

For `findings.html`, `scenarios.html`, `methodology.html`, insert the locked V1.1 SM blocks (above) under each page's existing locked headline. SM blocks render as a structured pyramid: each SM-header becomes an `<h3>` with `class="sm-header"` and italic styling; each SM-support becomes a `<p>` with `class="sm-support"` directly below it.

Add CSS:
```css
.sm-pyramid { margin: 24px 0 32px; padding: 20px 24px; border-left: 3px solid var(--accent); background: var(--surface-soft); }
.sm-header { font-style: italic; font-size: 18px; margin: 16px 0 8px; }
.sm-header:first-child { margin-top: 0; }
.sm-support { font-size: 16px; line-height: 1.55; margin: 0 0 12px; max-width: 760px; }
```

Adjust `--accent` and `--surface-soft` to match existing tokens; if those names don't exist, use the closest existing ones.

#### 4. Nav update across all pages

Current nav (per Phase 1A): probably some subset of `index | scenarios | methodology | sources | glossary`. New nav (all 6 pages):

```
Findings (findings.html) | Scenarios | Europe | Methodology | Sources | Glossary
```

The `index.html` landing page is the implicit default (reached at `/` or via the site logo / title); it does NOT appear in the top nav as a separate item.

**Apply consistently across:** `index.html`, `findings.html`, `scenarios.html`, `europe.html`, `methodology.html`, `sources.html`, `glossary.html`. Mark active page with `aria-current="page"` + a CSS class (use existing convention).

#### 5. `.closer` → `.conclusion` CSS class rename

Phase 1A renamed the H3 from "Closer" to "Conclusion" but kept the CSS class as `.closer`. Trivial cleanup:

- In every CSS block (across all HTML files — Phase 1A inlined the CSS per page), rename `.closer` → `.conclusion`.
- In every `<div class="closer">` instance, rename → `<div class="conclusion">`.
- Verify no other code references `.closer` (no external CSS file per Phase 1A; if one exists, rename there too).

Pre-flight grep:
```
grep -in '\.closer\|class="closer"' site/*.html site/*.css 2>/dev/null
```
Verify zero residual after rename.

#### 6. Cache-busting fetch on new pages

Phase 1A added `{ cache: 'no-store' }` to `fetch('./data.json')`. Apply same convention to any new `fetch()` calls in `europe.html`. Existing pages already have it; no change to those.

### Constraints

- **All copy is Phil-locked verbatim.** No authoring; structural insertion only. If a phrase looks awkward to you, do NOT rewrite — surface it in the report-back.
- **No new visual design.** Phase 2 owns visual exploration. Use existing tokens, existing grid, existing colour palette. The Europe page two-panel layout uses the existing flex/grid utility classes.
- **No emoji** in any HTML body. Same as Phase 1A.
- **No internal vocabulary in public-facing copy.** Same as Phase 1A — "Bundle X / Phase Y / SOT" all stay scrubbed. The S8 rename touches the SOT JSON's data fields but should NOT introduce any new public-facing internal vocabulary.
- **No information loss.** Splitting `index.html` → `index.html` + `findings.html` must preserve every paragraph, table, callout, and `<details>` appendix from Phase 1A. Diff-check before and after.
- **Single SOT.** Both `layer-6-deliverable-data.json` and `site/data.json` get the S8 rename. Verify both are in sync after the rename (the `site/data.json` is a copy of the SOT for frontend consumption per existing convention; if they're symlinked or built from a script, follow that pattern).
- **PostHog config unchanged.**
- **Phil does all git commits.**

### Verification (before reporting back)

1. All 7 HTML pages parse as valid HTML5: `index.html`, `findings.html`, `scenarios.html`, `europe.html`, `methodology.html`, `sources.html`, `glossary.html`.
2. `grep -in "concurrent.crisis\|concurrent_crisis" layer-6-deliverable-data.json layer-6-lens-framework.md site/*.html site/glossary.tsv` returns 0 results.
3. `grep -in '\.closer\|class="closer"' site/*.html` returns 0 results.
4. `findings.html` is a verbatim superset of pre-1B `index.html` content + the Findings within-section Minto block. Diff confirms every section, paragraph, callout, and `<details>` block preserved.
5. `index.html` is a strict subset: hero + stats panel + new "Read more" block only. No drill-down content remaining.
6. All 9 V1.1 SM headers + supports present verbatim in their target pages (3 in findings.html §2, 3 in scenarios.html top, 3 in methodology.html top).
7. Phil-locked Europe Minto open present verbatim in `europe.html` (1 headline + 1 sub-paragraph + 3 SM blocks).
8. `europe.html` renders both EU-27 and 36-market aggregate panels reading from `data.json.cross_cutting_findings.pan_european_aggregate`. Both panels surface: weighted Lens 1 ratio, headline corridor, class distribution, regime mix, breach count, squeeze count.
9. Variation-guard callout + headline-finding pull-quote present on `europe.html`.
10. Responsive logic on `europe.html`: side-by-side at ≥ 900px, primary-with-toggle below.
11. Nav consistent across all 7 pages: `Findings | Scenarios | Europe | Methodology | Sources | Glossary` with `aria-current="page"` on the active item. The landing `index.html` is reached via site logo / title only.
12. Page `<title>` and meta-description updated correctly per page.
13. Cache-busting `{ cache: 'no-store' }` present on every `fetch('./data.json')` call across all pages including `europe.html`.
14. Both `layer-6-deliverable-data.json` and `site/data.json` post-rename JSON loads round-trip cleanly.
15. Bundle X aggregate block (`cross_cutting_findings.pan_european_aggregate`) untouched apart from the S8 rename inside any nested scenario references; structure unchanged.
16. Lens spec (`layer-6-lens-framework.md`) post-rename markdown still parses (no broken table cells / list items).
17. PostHog token unchanged in every page.
18. No emoji present anywhere in HTML body.
19. Total folder size still < 700 KB excluding `data.json`.
20. Tooze / Morin attribution audit: report any hits found by the pre-flight grep, even if zero.

### When done — report back to master session with

1. File-by-file line count diff (additions / removals / new files).
2. Verification checklist (1–20) — pass/fail per item.
3. S8 rename audit — 10 occurrences expected; report each line touched (file + line number + before/after).
4. Information-loss audit on the index.html → findings.html split — confirm zero content lost; flag any section that was structurally shifted.
5. Within-section Minto integration audit — confirm each of the 9 SM blocks renders correctly in context (no broken h3 nesting, no styling collision with existing section-num pattern).
6. Europe page screenshot or rendered HTML preview — surface the rendered aggregate panels for Phil sanity-check (the live Bundle X data should produce: EU-27 weighted Lens 1 ratio, 36-market ratio, both class distributions, regime mixes, breach counts).
7. Responsive behaviour audit on `europe.html` — describe how the side-by-side → toggle transition works at the 900px breakpoint.
8. Nav consistency audit — confirm all 7 pages carry the new 6-item nav with active-state highlighting.
9. Tooze / Morin attribution audit result.
10. Phase 2 readiness — anything that surfaced during 1B that Phase 2 (visual exploration) should account for (e.g., the two-panel layout on europe.html may want a different visual treatment in Phase 2; flag for design exploration).
11. Any candidate brain captures (likely none; bounded execution).

## END PROMPT
