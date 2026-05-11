# Handover Prompt — Bundle O Phase 2C: Editorial + Style + IA Cleanup Pass

Bounded composition session. Cleanup pass on the Phase 2B live site addressing 24 specific items across editorial (banned phrases + Phil text edits), style (callout-to-plain-text propagation), IA (class-card repositioning + ninth-scenario surfacing), nav restructure (sister-layer cross-links), and removals (Einfache Sprache section). All copy edits are Phil-locked verbatim in this handover. ~6–8 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Phase 2B shipped 16/16 PASS with all five visual locks integrated. Phil reviewed the live build and flagged 24 issues spanning editorial, style, IA, and nav. Recurring failure surfaced: banned phrases ("load-bearing") inherited verbatim from prior-phase copy without re-scan in Phase 2B. This brief absorbs all 24 items into a single coordinated cleanup pass and tightens the banned-phrase scan to cover *inherited* text, not just newly authored.

---

## START PROMPT

I need you to execute 24 specific cleanup items on the Phase 2B live site. All copy edits are Phil-locked verbatim — your job is structural change + textual replacement + style cleanup, not authoring.

Read every section of this handover before starting. Several items interact (e.g., #14 ninth-scenario surfacing changes the methodology Minto count from 3 to 4 SMs, which affects the §7 cleanup in #8).

### Read FIRST (absolute paths)

**Live-site targets (write to these):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/glossary.html`

**Reference (read for nav pattern):**
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/index.html` — established sister-site nav pattern (lines 184–210 + matching CSS). Match this exactly for synthesis nav.

**Reference (read for register):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/master-session-handover-2026-04-30.md` — Phil's editorial register avoid-list

### Phil-locked anchors (verbatim — do NOT rewrite)

#### Methodology Minto restructure (4 SMs total — was 3)

Current Methodology Minto on `methodology.html` has 3 SMs (lenses / calibration / known gaps). Restructure to **4 SMs** with these locked headers + supports:

**SM 1 — Lenses (rewrite):**

Header (verbatim): *"Five lenses, chosen because earlier parts of the project had already gathered the evidence."*

Support (verbatim): We went with the five lenses we already collected evidence on in earlier parts of the project: AI exposure, demographics, disruption pathways, reskilling capacity, and careers data. The constraint was not which lenses might exist in theory — it was which ones we could test rigorously today, with European data, across 36 countries.

**SM 2 — Calibration (keep current):**

Header: *"One calibration choice changes the headline."* (unchanged)

Support: keep the current SM 2 support text verbatim from `methodology.html` (the threshold-ladder explanation).

**SM 3 — Known gaps (rewrite opener):**

Header (verbatim): *"What we deliberately left open."* (unchanged)

Support (verbatim): Three known gaps constrain this read:

1) **Occupational detail:** capability-floor breach is reported at a coarser job classification (2-digit ISCO) because the finer-grained European Social Survey microdata (3-digit) requires a multi-week application. The count here is a lower bound.
2) **Funding allocation:** the EU's adaptation funding through 2030 is not yet broken down by country. We can see the overall envelope, but not its distribution.
3) **Employer behaviour:** we cannot observe live signals like hiring, retraining launches, or redundancy plans because they sit behind paywalls or in proprietary HR systems.

(The numbered list stays plain text per item #5 in the cleanup list — no callout box.)

**SM 4 — Ninth scenario (NEW — promoted from §7 to top Minto):**

Header (verbatim): *"Why eight scenarios, not more."*

Support (verbatim): A ninth scenario — startup-driven absorption as a parallel to Climate Adaptation Boom — was considered but excluded. The absorption mechanism is coherent in principle (new firm formation can absorb displaced workers), but the empirical anchors at country level are thinner than for S1–S8. There is no equivalent of the IPCC / Eurofound climate-demand projections or the Brynjolfsson / Dell'Acqua task-level RCTs that grounded S2 and S3, and the channel is partially captured in Lens 1's absorption-capacity score. The policy-lever version of the question — what it would take to build this mechanism deliberately at supra- or national level — belongs in Part 7.

After this restructure: §7 of `methodology.html` no longer needs the ninth-scenario callout (it's now in SM 4 at the top). §7 keeps its other "what we can't see" content.

#### Phil-text edit — Scenarios SM 1 (or page headline)

Phil flagged: *"...whether the economy is in a growth, secular stagnation, or post-growth stage."*

Apply this swap in **both**:
1. The page headline (`<h1>` at the top of `scenarios.html`) — currently *"Eight ways the next decade could play out and the most likely one depends on whether your economy is still growing."* → keep first half, swap the *"still growing"* tail to the new phrasing: *"Eight ways the next decade could play out and the most likely one depends on whether the economy is in a growth, secular stagnation, or post-growth stage."*
2. The current Scenarios SM 1 support paragraph (which already describes the three regimes) — preserve the substance but make sure the sentence cadence aligns with the new headline phrasing where it overlaps.

#### Landing — "Drill-down" → "Overview"

The landing page currently has a "DRILL DOWN" eyebrow above the 4 SM blocks. Replace with **"OVERVIEW"** (uppercase styling preserved). No other copy changes to the landing.

### Cleanup items (24)

#### A. Editorial (banned phrases + text edits)

**1. Remove all "load-bearing" instances site-wide.**

Pre-flight grep:
```
grep -in "load-bearing\|load bearing" site/*.html
```

Expected hits: Italy callout eyebrow (`findings.html`), scenarios §4 eyebrow (`scenarios.html`), and possibly more. Surface all hits in report-back. For each:
- Remove the eyebrow / label / heading where the phrase appears
- Rewrite the surrounding sentence in plain language if the phrase is part of body prose (e.g., *"Italy is the load-bearing demographic finding"* → *"Italy is the clearest demographic finding"* or just *"Italy"* depending on context — preserve meaning, drop the phrase)

**2. Full banned-phrase grep audit across all 7 pages.**

After removing "load-bearing", grep for the rest of Phil's avoid-list:
```
grep -in "load-bearing\|load bearing\|structurally\|structural asymmetry\|the analysis is built to surface\|the read \|this read" site/*.html
```

(`reads` / `read` as nouns are tricky — flag any mid-sentence noun usage, ignore verb usage. Surface hits in report-back; sub-session may need to consult Phil on edge cases.)

**3. Landing: "Drill-down" → "Overview"** (per locked text above).

**4. Methodology Minto restructure to 4 SMs** (per locked text above).

**5. Scenarios headline + SM 1 phrasing edit** (per locked text above).

#### B. Style (callout-to-plain-text propagation)

The Phase 2B build relied heavily on `.sm-pyramid`, `.callout`, `.editor-note`, and similar styled boxes. Phil sees this as design noise. Replace with plain text + clear hierarchy on every Minto SM block + every callout-style block on every page.

**6. All Minto SM blocks → plain text.**

For every page that carries an `.sm-pyramid` block (landing, findings, scenarios, europe, methodology):
- Drop the `.sm-pyramid` border + soft background
- Keep the italic header (`.sm-header`)
- Keep the support paragraph (`.sm-support`)
- Keep the `Go deeper →` CTA link if present
- Render the block as plain prose with clear typographic hierarchy (e.g., italic h3 + paragraph + linked text), not a styled box

The Minto-pyramid concept stays; the *box-around-it* goes.

**7. Italy callout → plain text** (`findings.html`).

Drop the eyebrow ("ITALY — LOAD-BEARING DEMOGRAPHIC FINDING") + the box + the eyebrow-style heading. Render as plain prose: italic or bold sentence-lead + body paragraph. The dramatic *"−485,823"* number stays inline as bold or large-font, but no decorative box around the whole block.

**8. Conclusion → plain text** (`findings.html`).

Drop the `.conclusion` styled box (orange left-border + dark soft background). Render the 3-paragraph conclusion as plain prose. Keep the `<h3>Conclusion</h3>` heading; drop the wrapper styling.

**9. Methodology §4–6 callouts → plain text** (`methodology.html`).

§4 (Capability-Floor Breach Scope Ceiling), §5 (MFF Per-Country Allocation Gap), §6 (Candidate-Country C2 Sub-Cluster Routing) currently each have callout-styled blocks. Drop the callout styling; render as plain prose subsections with clear h3 + body.

**10. Scenarios §4 two callouts → plain text or differentiated style** (`scenarios.html`).

§4 has two callouts: "CAPACITY-SIDE ANCHOR · CLASS III SPINE" (the reskilling-capacity gap block) and "LOAD-BEARING CALLOUT" (the optimism-path block — also flagged in #1 for "load-bearing" removal). Render both as plain prose subsections. Drop the eyebrows ("CAPACITY-SIDE ANCHOR · CLASS III SPINE", "LOAD-BEARING CALLOUT"). Keep the substance + the bold number callouts (~7.55 M, ~450 K, etc.) as inline emphasis.

**11. Europe variation guard + headline pull-quote — make visible.**

`europe.html` currently has a `.variation-guard` callout and a `.headline-pull-quote` block at the bottom. Phil notes both feel "lost" — design treatment hides them rather than emphasising. Sub-session decides treatment: either render as plain prose paragraphs in the page flow (no box, no left-border accent), OR keep the box treatment but reposition higher up the page so they don't feel orphaned at the bottom. Pick the cleaner option; flag the choice in report-back.

**12. Polycrisis Drag (S8) block + "Note on the eighth scenario" — merge + make prominent** (`scenarios.html` §1).

Currently §1 has the S8 spectrum bullet inline with the other 7 routine scenarios + a separate "A NOTE ON THE EIGHTH SCENARIO" callout below. Merge into a single prominent block:
- Visually distinct from the 7 routine scenario rows (e.g., separated by horizontal rule + slightly different layout — but still plain text, no garish box)
- The merged block contains: scenario name (Polycrisis Drag), the spectrum description (defence rearmament, climate, decoupling, Ukraine — overwhelming institutional capacity), and the historical-no-analogue note in continuous prose, not as separate callout
- Maintains the "outside the spectrum" framing — clear that S8 is not a point on the optimism-pessimism line

#### C. IA (information architecture)

**13. Findings §2 — add subheading after the 3 Minto SMs.**

Currently the 3 Minto SMs sit immediately above the §2 prose ("Only nine countries remain resilient under stress..."). Without a subheading, the §2 prose can read as a continuation of SM 3 ("Stability isn't the same as safety"). Insert a subheading between the 3rd SM and the §2 prose. Suggested: *"What this looks like, country by country"* or *"How the corridors split"* — sub-session picks one that fits the surrounding prose, surfaces choice in report-back. Use `<h3>` styling consistent with other in-section subheadings on findings.html.

**14. Findings §4 — reposition class cards.**

Currently §4 ("Fragility Classes") shows: heading → intro paragraph → population-weighted stack → 4 class cards (below the stack). Phil wants the class cards visible alongside the stack so a desktop full-screen view shows both simultaneously when filtering.

Recommended layout: **class cards above the population-weighted stack, not below.** Maintains §3 → §4 visual flow (map → cards → stack); when a user filters via a class card, both the map (§3) and the stack (§4) update visibly without the user scrolling past the stack to see the cards.

Alternative: move class cards up to §3 (under the corridor map). Phil flagged this option but recommended (a) cards-above-stack. Sub-session implements (a) unless layout reasons override; if (b) seems materially better at desktop, surface for Phil.

**15. Methodology Minto restructure — 4 SMs total** (per locked text above; counted as IA item because it's a structural Minto change).

**16. §7 ninth-scenario callout — remove from §7** (was added in Phase 2B; now lives in SM 4 at the top).

After moving the ninth-scenario content to SM 4 (item #15), remove the §7 callout block. Don't leave a duplicate. §7 keeps its other "Known limits" content (3-digit ESS, MFF allocation, employer behaviour gaps) — those are now also referenced in SM 3 support but the §7 detail is the citable expansion; keep both.

#### D. Nav (cross-layer + integration)

**17. Replace standalone "synthesis · Part 6" wordmark with integrated nav pattern.**

Phase 2B added a `<a class="site-logo">` block leftmost in the nav. Phil notes this feels disconnected from the rest of the nav. Match the established sister-site pattern from `european-demographics-map/site/index.html` (lines 184–210):

```html
<nav class="site-nav" id="site-nav" role="navigation" aria-label="Main navigation">
  <div class="site-nav-links">
    <a href="index.html" aria-current="page">Overview</a>
    <a href="findings.html">Findings</a>
    <a href="scenarios.html">Scenarios</a>
    <a href="europe.html">Europe</a>
    <a href="methodology.html">Methodology</a>
    <a href="sources.html">Sources</a>
    <a href="glossary.html">Glossary</a>
    <span class="nav-sep"></span>
    <a href="https://ai-exposure.nexalps.com/" target="_blank" rel="noopener">AI Exposure ↗</a>
    <a href="https://demographics.nexalps.com/" target="_blank" rel="noopener">Demographics ↗</a>
    <a href="https://disruptions.nexalps.com/" target="_blank" rel="noopener">Disruptions ↗</a>
    <a href="https://reskilling.nexalps.com/" target="_blank" rel="noopener">Reskilling ↗</a>
    <a href="https://job-market.nexalps.com/" target="_blank" rel="noopener">Job Market ↗</a>
  </div>
  <button class="burger" id="burger-btn" aria-label="Toggle navigation menu" aria-expanded="false"><span></span><span></span><span></span></button>
</nav>
<div class="burger-panel" id="burger-panel" role="dialog" aria-label="Navigation menu">
  <!-- mirror the same link set -->
</div>
```

Pattern notes (port from demographics):
- No standalone "synthesis · Part 6" wordmark — page identification happens in the byline ("Part 6 of 7 in the European AI Labour Market suite")
- Internal pages first (Overview = `index.html`, then Findings / Scenarios / Europe / Methodology / Sources / Glossary)
- `<span class="nav-sep">` separator between internal and external links (CSS: small visual gap or vertical rule, match demographics styling)
- External cross-layer links with `↗` (`&#8599;`) opening in new tab via `target="_blank" rel="noopener"`
- Burger panel mirrors the same link set for mobile

Apply on all 7 pages. Update `aria-current="page"` per page (Overview active on index.html, Findings active on findings.html, etc.).

CSS: copy `.site-nav`, `.site-nav-links`, `.nav-sep`, `.burger`, `.burger-panel` styling from `european-demographics-map/site/index.html` if not already present in synthesis (Phase 1A inlined CSS per page; preserve that pattern). Do NOT introduce new color tokens.

**18. Confirm sister-layer URLs.**

The 5 sister-layer URLs to add:
- `https://ai-exposure.nexalps.com/` (Layer 1 — European AI Exposure Map)
- `https://demographics.nexalps.com/` (Layer 4 — European Demographics Map)
- `https://disruptions.nexalps.com/` (Layer 3 — European Disruptions Map)
- `https://reskilling.nexalps.com/` (Layer 5 — European Reskilling Map)
- `https://job-market.nexalps.com/` (Layer 2 — European Careers / Job Market Map; published as job-market.nexalps.com per the demographics nav reference)

Verify by greping `european-demographics-map/site/index.html` for the established URLs; if any differ, use whatever the demographics site uses.

#### E. Removals

**19. Drop Einfache Sprache section site-wide.**

Currently `index.html` and `findings.html` both carry an Einfache Sprache (German) section near the bottom. Remove entirely from both pages. Drop any associated `.einfache` CSS rules that are no longer referenced elsewhere. Do NOT keep an English-only version (Phil clarified: Einfache means German simplified; if it's just English plain language, it's not Einfache).

**20. Audit `index.html` and `findings.html` for any other Einfache scaffolding** (toggle buttons, language switchers, `data-lang` attributes that switched only between standard and Einfache content). Remove cleanly.

#### F. Additions

**21. Scenarios weather-patterns — country pills below each regime card.**

`scenarios.html` §2 currently has 3 regime small-multiples (growth / secular stagnation / post-growth). Add a row of country pills below each card listing the countries assigned to that regime, sourced from `data.json` per-country `regime_tag` field. Pill styling: use existing `.country-pill` or `.country-tag` pattern from elsewhere on the site (e.g., findings.html class cards already render country chips); reuse the same CSS class to maintain visual consistency.

#### G. Validation + meta

**22. Re-run banned-phrase scan after all edits.**

Final post-build grep across all 7 pages:
```
grep -in "load-bearing\|load bearing\|structurally\|structural asymmetry\|the analysis is built to surface" site/*.html
```

Must return 0 hits. If any survive, surface in report-back with line numbers + suggested rewrite.

**23. Re-run banned-phrase scan on inherited text** (per the brain's new working-discipline rule landed 2026-05-06).

Beyond the avoid-list grep, scan all *user-facing* text on the live pages — including text that wasn't modified in Phase 2B but is on the page — for any of Phil's editorial register avoid-list phrases. Flag any survivors that were never scrubbed in prior phases.

**24. Verify Phase 1B / 2B IA still preserved.**

After all the cleanup edits:
- 7 pages still parse and load cleanly
- Cross-link state machine still works on findings.html
- All 5 visualisations still render with live data from data.json
- Mobile responsive at 375 / 768 / 1280 still holds
- PostHog tracking still fires on all interactives
- Cache-busting `{cache:'no-store'}` still on every fetch
- `data.json` and `layer-6-deliverable-data.json` unchanged

### Constraints

- **All copy edits Phil-locked verbatim.** No re-authoring; apply exactly as in this handover.
- **No new design tokens.** Existing `--bg`, `--fg`, `--muted`, `--ring`, `--card`, `--card-border`, `--radius-md`, `--radius-sm`, `--class-i/ii/iii/iv` only.
- **No external libraries.**
- **`data.json` + `layer-6-deliverable-data.json` unchanged.**
- **Phase 1B / 2B IA preserved** (per item #24).
- **No emoji** anywhere.
- **PostHog tracking intact** on all interactives.
- **Mobile responsive at 900 px breakpoint.**
- **Phil does all git commits.**

### Verification (before reporting back)

1. All 24 cleanup items addressed.
2. All 7 pages parse cleanly; zero console errors.
3. Banned-phrase grep returns 0 hits across all 7 pages.
4. Methodology page has 4 SMs with locked headers + supports.
5. Scenarios headline + SM 1 carry the Phil-text edit ("growth, secular stagnation, or post-growth stage").
6. Landing eyebrow reads "OVERVIEW" not "DRILL DOWN".
7. All Minto SM blocks rendered as plain text (no `.sm-pyramid` boxes).
8. Italy callout, Conclusion, methodology §4–6, scenarios §4 callouts, europe variation-guard + pull-quote — all rendered per the cleanup spec (plain text or new treatment per item).
9. Findings §2 has a subheading between Minto block and prose.
10. Findings §4 class cards repositioned above the population-weighted stack.
11. Methodology §7 no longer has the ninth-scenario callout (moved to SM 4 at top).
12. Polycrisis Drag scenario + note merged into one prominent block on scenarios.html §1.
13. All 7 pages use the integrated nav pattern (matching demographics site) with 5 sister-layer cross-links + ↗ markers.
14. `aria-current="page"` correct per page; landing's nav highlights "Overview".
15. Einfache Sprache section removed from index.html and findings.html.
16. Scenarios §2 has country pills under each regime card.
17. Cross-link state machine still works (filter dim, ring, Esc clears).
18. All 5 visualisations still render with live data.
19. Mobile responsive at 375 / 768 / 1280.
20. PostHog tracking fires on all interactives (verify event-tracking audit unchanged).
21. Folder size still < 800 KB excluding `data.json`.

### When done — report back to master session with

1. Per-page line count diff.
2. Verification checklist (1–21) — pass/fail per item.
3. Banned-phrase grep audit — line-by-line list of hits found + rewrites applied.
4. Inherited-text scan audit — any pre-existing avoid-list phrases that were scrubbed in this pass that weren't part of the original 24 items.
5. Static screenshot or rendered-HTML preview of:
   - Landing (Overview eyebrow + plain-text SMs + new nav)
   - Findings (§2 with subheading + §4 with cards above stack + Italy plain text + Conclusion plain text)
   - Scenarios (Phil-text-edit headline + S8 merged block + country pills under regimes + §4 plain text)
   - Europe (variation-guard repositioned)
   - Methodology (4 SMs including ninth-scenario)
6. Nav consistency audit — all 7 pages carry the new integrated nav with 5 sister-layer links.
7. Einfache removal audit — confirm zero Einfache markers left on any page.
8. Bundle W readiness — anything new that surfaced during 2C that Bundle W (Minto propagation across deliverable docs) should account for.
9. Any candidate brain captures (likely none beyond the banned-phrase-propagation rule already landed).

## END PROMPT
