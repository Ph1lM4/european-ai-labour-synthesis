# Handover Prompt — Bundle O Phase 1A: Content Rewrite

Bounded composition session. Rewrites the existing Bundle O v0.1 site (5 HTML pages) to absorb Bundle V scenario reframe (S1–S8 + S3 Jobs Transform), apply Phil's storytelling + plain-language feedback, scrub bundle/phase scaffolding from public-facing copy, and craft Minto-aligned headlines. Pure text + structure work; no information-architecture restructure (Phase 1B handles split landing/findings + within-section Minto). ~120–150 min.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Bundle V completed 2026-04-30 — SOT JSON now uses S1–S8 linear codes; S3 (Jobs Transform) added; `s2b_dependent` field renamed to `s2_dependent`. The existing Bundle O v0.1 site uses old codes (S1/S2a/S2b/S3/S4a/S4b/S5) + carries bundle/phase scaffolding visible in Methodology + Sources pages + has storytelling structure Phil flagged as too technical.

Phil's feedback (master session, 2026-04-30 evening) consolidated:
1. Audience doesn't know the analytical constructs (C1/C2/C3 / Partial Absorption / etc.). Plain-language discipline: introduce a label only after its meaning has been established.
2. Bundle/phase IDs (Bundle J, Phase 2, etc.) are internal vocabulary, not for public.
3. Storytelling spine — Minto/message-map structure with crafted story-arc headers.
4. Specific structural fixes: Italy callout reframe, Closer → Conclusion rename, §5 → storytelling-only with `<details>` appendix, sparkline C1-C3 axis flip, S5 Wage Cliff pessimistic-frame sharpening, S8 (was S5) climate-decoupling addition + sidenote on no-historic-Layer-3-analogue.

Phase 1A executes all of this on the existing site HTML. Phase 1B (post-1A) restructures information architecture — splits `index.html` into landing-summary + `findings.html` drill-down, applies within-section Minto on every drill-down page.

---

## START PROMPT

I need you to rewrite the Bundle O v0.1 site (5 HTML pages) to absorb Bundle V's S1–S8 renumbering + add S3 Jobs Transform + apply Phil's storytelling + plain-language + bundle-phase-scrub feedback. Do NOT restructure the information architecture — that's Phase 1B. This is content rewrite within the existing 5-page structure.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` + `scenarios.html` + `methodology.html` + `sources.html` + `glossary.html` — the existing v0.1 site to update in place.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — post-Bundle-V SOT JSON. Schema unchanged; scenario codes now S1–S8.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-v-scenario-reframe-handover-2026-04-30.md` — Bundle V handover for renumbering map + S3 semantic + new probability table.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-executive.md` — Executive doc (still has old codes; will be updated in Bundle W, but reference for tone + crafted prose).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-glossary-draft.tsv` — glossary (still has old codes; will update as part of Phase 1A scope).
- `/Users/philippmaul/Documents/second-brain/skills/disruption-analysis/references/takeaways.md` — T31 (Nielsen forklift), T32 (pancaking) for the S3 Jobs Transform empirical anchor in scenarios.html.

### Phil-locked anchors (verbatim — do NOT rewrite)

**Landing-page headline (used in index.html overview + every page meta-description; Phase 1B will surface it as the formal Minto pyramid open):**

> **No European labour market is fully safe from AI-driven job displacement.**
>
> *We stress-tested 36 markets across five lenses and eight scenarios. Most countries can absorb the disruption only partially, and 15 are likely already beyond that threshold. Under the rules we applied, only nine have the statistical strength to hold up under pressure.*

**Within-page Minto headlines (Phase 1A introduces them in the existing pages; Phase 1B promotes them to formal Minto opens):**

| Page | Headline (verbatim) |
|---|---|
| Findings (currently `index.html`) | *"More than three-quarters of European labour markets sit in uncomfortable territory."* |
| Scenarios | *"Eight ways the next decade could play out and the most likely one depends on whether your economy is still growing."* |
| Methodology | *"How we tested and what we deliberately left open."* |

### Renumbering map (apply across all 5 site pages + glossary TSV)

```
OLD CODE → NEW CODE — Scenario name (spectrum position)
─────────────────────────────────────────────────────────────
S1       → S1 — Reinstatement Revival         (uber-optimistic)
S2b      → S2 — Climate Adaptation Boom       (optimistic)
NEW      → S3 — Jobs Transform                (slightly optimistic)
S3       → S4 — Muddle Through                (middle)
S2a      → S5 — Wage Cliff                    (slightly pessimistic)
S4a      → S6 — Reinstatement Failure         (pessimistic)
S4b      → S7 — Bandwidth Fracture            (pessimistic)
S5       → S8 — Concurrent-Crisis Cascade     (parallel cascade, conditional)
```

Field rename also: `s2b_dependent` → `s2_dependent` (already done in SOT; site copy needs the same rename — references to "s2b-dependent countries (AT, LU, TR)" become "s2-dependent countries").

**Sequencing for site rename:** read each HTML file, do find-replace in ascending NEW-code order with temporary suffixes to avoid collision (or read entire file content, build a key-rename map, transform via map, write atomically — same approach as Bundle V).

### S3 Jobs Transform — site copy

Add S3 Jobs Transform across the site:

- **scenarios.html** spectrum section: insert S3 between S2 and S4 in the spectrum bullets; new bullet text:
  > **Slightly optimistic — Jobs Transform** (S3). AI substitutes for routine *tasks* within existing occupations. Wages stay stable or rise modestly. Jobs reshape — workers spend less time on routine sub-tasks, more on judgment, coordination, and non-routine cognitive-social work. Empirical anchors: Brynjolfsson 2025 (call-centre productivity RCT), Dell'Acqua 2023 (BCG consultants +40% inside the frontier), Nielsen forklift framing.
- **scenarios.html** weather-pattern probability paragraph: update with new S2 = 0.30 vs S4 = 0.22 under post-growth (was S2b vs S3 muddle-through).
- **scenarios.html** sparkline: now renders 7 routine variants (S1, S2, S3, S4, S5, S6, S7) instead of 6; legend updates accordingly. **Also flip the y-axis: C1 at top, C3 at bottom** (Phil's feedback — the current rendering has C1 at bottom which is counterintuitive since C1 is the "good" outcome).
- **scenarios.html** capacity anchor + s2-dependent callout: rename to s2-dependent (was s2b-dependent) — countries are still AT, LU, TR.
- **scenarios.html** breach panel + squeeze cluster panel: unchanged (not scenario-coded).
- **glossary.html** scenario term + s2_dependent term: update definitions to S1–S8 + new s2_dependent code.
- **index.html** within Lens 4 + 5 mentions: same s2b → s2 rename applied.
- **methodology.html** reference to scenarios: update enumerations to S1–S8.

### Bundle/phase scrub (public-facing readability)

**Find every reference to internal vocabulary across all 5 site pages and replace with public-readable equivalents.**

Patterns to search (use grep-i across `site/*.html` + `glossary.tsv`):

| Internal pattern | Public-readable replacement |
|---|---|
| "Bundle J" / "Bundle K-2" / "Bundle L" / "Bundle M" / "Bundle N" / "Bundle P" / "Bundle Q" / "Bundle R" / "Bundle V" | Either remove entirely or replace with "this analysis" / "our scoring" — no specific bundle reference |
| "Phase 1" / "Phase 2" / "Phase 3" / "Phase 4" / "Phase 5+" | "earlier in the analysis" / "the next stage" / generic "the analysis" |
| "Sentinel" / "sentinel test" | "a check we ran" / "a test condition" |
| "Q1 lock" / "Q2 lock" / etc. | Either remove or replace with what the lock is ("we decided that ...") |
| "Schema v1.0" / "schema_version" | Drop (technical metadata, not for public) |
| "SOT JSON" / "SOT" | "the underlying data" |
| "locked spec line N" | Drop (internal spec reference) |
| "asymmetric guard" / "Q1 asymmetric-guard" | "the rule we applied" or "the corrected rule" |
| "stage 1 → 2 → 3 amendments trail" | Replace the code-fence with a single paragraph: "The corridor edges were tightened during the analysis when the original literature-fitted thresholds returned a count of zero under strict robustness — the published rule is the corrected one." (Sub-session's earlier suggestion, locked.) |
| "Bundle N composition over Bundle M SOT JSON" header strapline | Replace with: *"Version 1.0 · Last updated 2026-04-30"* |
| "Source Bundles" section in sources.html | Drop the entire 13-bundle section; the external citations stay; add a brief "How we built this" replacement (2 sentences naming the data-build pattern: lens scoring → corridor placement → scenario stress-test) without bundle vocabulary |
| "Phase 5+ candidates" header | Rename to *"Known limits"* or *"What this synthesis cannot see"* — keep the substantive content (3-digit ESS, MFF disaggregation, Ukraine backporting, live external intel, internal-transition diagnostic) but strip "Phase 5+", "Q5 lock", "candidate" framing |

**Run grep audit before cutting:** `grep -in "bundle\|phase [0-9]\|schema v\|q[0-9]\|locked spec\|sentinel\|sot json" site/*.html glossary.tsv` to see every line that needs review. Surface the line-by-line list to the master session in the report-back so Phil can sanity-check the cuts.

### Storytelling rewrites (Phil's specific feedback per page)

#### index.html (current overview; will become Findings in Phase 1B)

- **Subheader replaced** with locked landing headline + sub-paragraph (above).
- **Page reads like a story**, not a fact-list. Transitional sentences between sections; section openers that pull the reader forward.
- **§2 (lenses)** uses the bullet pattern from `layer-6-deliverable-document-executive.md` §2 (each lens opens with a plain-language question, then finding, then number).
- **§3 (corridor map)** — add a 2-sentence explanatory paragraph above the map. Plain-language. Example: *"The map below sorts 36 European labour markets into three corridors based on how well their training and re-employment systems can keep up with AI-driven displacement. Green markets are coping; amber markets are at risk; red markets are already behind."* Visual exploration of better representations is Phase 2 — for Phase 1A keep the existing 4×9 grid.
- **§4 (fragility classes)** — add a 2-sentence explanatory paragraph above the class panel. Plain-language. Example: *"We grouped countries into four fragility classes based on how their corridor placement holds up under stress. The classes are a traffic-light reading: which countries can keep going, which are one shock away, which are already in trouble."*
- **§5 (currently lens-by-lens recap)** — rewrite as storytelling-only. Move the data details (numbers, ratios, technical breakdowns) into a `<details>` collapsible appendix labelled "For interested readers — the numbers behind these findings" or similar.
- **Italy callout reframe** — currently lead with the number "−485,823." Reframe to lead with **what it tells us**: *"Italy is the only major European economy with negative net migration in 2025. Institutional ageing has crossed from buffer-deficit into accelerating decline — the workforce shrinks before AI displaces a single worker. Net migration: −485,823."* (Number lands at the end as the proof, not the headline.)
- **Closer → Conclusion** — rename section header from "Closer" to "Conclusion." Style: same register as Prelude (author-note pattern) or reframe to fit the author-note pattern. Phil flagged stylistic consistency between Prelude open and Conclusion close.

#### scenarios.html

- **§1 (scenario list)** — restructure with the 8-scenario spectrum (above).
- **§1 sidenote** (NEW) — add a short callout box: *"The eighth scenario — Concurrent-Crisis Cascade — has no analogue in the 580 years of historical disruptions covered in Part 3. The combination of defence rearmament, climate adaptation, global decoupling, and Ukraine reconstruction creating simultaneous institutional stress is unprecedented. This adds an additional layer of uncertainty no historical case base can ground."* (Sub-session refines wording.)
- **§1 S5 Wage Cliff sharpening** — current framing is ambiguous (could read optimistic). Sharpen to clearly pessimistic: *"AI substitutes for mid-skill labour. Wages compress because reinstatement creates fewer or lower-paid jobs."*
- **§1 S8 Concurrent-Crisis Cascade — climate adaptation + global decoupling addition** — current framing names "defence, EU-budget strain, and migration." Add climate adaptation + global decoupling explicitly: *"defence rearmament, EU-budget strain, climate adaptation pressure, global decoupling, and Ukraine reconstruction combine to overwhelm institutional capacity simultaneously."*
- **§2 (weather patterns)** — add storytelling text. Each weather pattern gets 1–2 sentences explaining what living in that economy means for AI-displacement absorption.
- **§3 (sparkline)** — flip y-axis (C1 top, C3 bottom). Add explanatory caption.
- **§4 (probability table)** — update to S1–S8 with new probability vectors per regime (from Bundle V). Add a single explanatory sentence above the table: *"These probabilities are our best estimate of how likely each scenario is, given the country's economic regime. Bands cover an 80% confidence interval."*
- **§5/§6** — light storytelling pass; keep substantive content.

#### methodology.html

- Already running the bundle/phase scrub above; this page is the densest.
- Add Methodology page Minto headline at top: *"How we tested and what we deliberately left open."*
- Replace the "amendments trail" code-fence with the single-paragraph public-readable equivalent (see scrub table above).
- Rename "Phase 5+ candidates" → "Known limits" or "What this synthesis cannot see."
- Drop "schema_deviations_from_draft" reference.

#### sources.html

- Drop the entire "Source Bundles" 13-bundle section.
- Replace with a brief "How we built this" — 2 sentences naming the data-build pattern without bundle vocabulary.
- External citations + license + cite-as + LinkedIn contact stay.

#### glossary.html

- Apply S1–S8 renumbering to scenario term + s2_dependent term.
- Add a glossary entry for **Jobs Transform** (S3) — definition + Einfache definition.
- Light copy-edit pass.

### Constraints

- **Read-only against the SOT JSON, lens framework spec, deliverable docs.** Phase 1A modifies the site HTML + glossary TSV only. Deliverable docs get updated in Bundle W (post-Phase-2).
- **Plain-language discipline.** Introduce a label (C1, Class I, S2, etc.) only AFTER its meaning has been established in surrounding prose. First-occurrence pattern: "*managed transition* — meaning markets that can absorb almost all displacement (C1 in our coding)..."
- **No internal vocabulary in public-facing copy.** "Bundle X / Phase Y / Q-lock / sentinel / SOT / schema-version" all gone.
- **Locked headlines verbatim** — landing headline + within-section Minto headlines.
- **No information architecture changes.** Same 5 pages; same nav; same file paths. Phase 1B handles IA.
- **No new visual elements.** Same corridor grid, same sparkline, same fragility class panel — just axis flip on sparkline. Phase 2 handles new visuals.
- **No emoji** in any HTML body. Same as v0.1.
- **PostHog config unchanged.**
- Phil does all git commits.

### Verification (before reporting back)

1. All 5 HTML pages parse as valid HTML5.
2. `grep -in "S2a\|S2b\|S2c\|S5_cascade\|s2b" site/*.html site/glossary.tsv` returns 0 results.
3. `grep -in "bundle [a-z]\|phase [0-9]\|q[0-9] lock\|sentinel\|sot json\|schema v\|locked spec" site/*.html site/glossary.tsv` returns 0 results (or only non-load-bearing residuals — surface the list).
4. Locked landing headline present verbatim in index.html (or as meta-description).
5. Within-section Minto headlines present at the top of `index.html`, `scenarios.html`, `methodology.html`.
6. Sparkline y-axis flipped: C1 at top, C3 at bottom.
7. S3 Jobs Transform present in scenarios.html spectrum + sparkline + glossary.
8. S8 framing includes climate adaptation + global decoupling explicitly.
9. S8 sidenote present on scenarios.html.
10. S5 Wage Cliff sharpened to clear pessimistic frame.
11. Italy callout leads with what-it-tells-us, not the number.
12. Conclusion section header replaces "Closer."
13. §5 on index.html uses storytelling-only + `<details>` appendix for data details.
14. Methodology amendments-trail code-fence replaced with single-paragraph plain-language equivalent.
15. Sources page "Source Bundles" section removed; "How we built this" replacement present.
16. "Known limits" / "What this synthesis cannot see" replaces "Phase 5+ candidates" framing.
17. Header strapline replaced with version + date (no Bundle/SOT references).
18. PostHog token unchanged.
19. Total folder size still < 600 KB excluding data.json.

### When done — report back to master session with

1. Per-page line count diff (additions / removals).
2. Verification checklist (1–19) — pass/fail per item.
3. Bundle/phase scrub audit — line-by-line list of every cut, surfaced for Phil sanity-check.
4. Renumbering audit — confirm 0 instances of old codes anywhere in site.
5. Plain-language discipline audit — list any term first-introduced without prior definition (label-on-first-use violations).
6. New numerical claim drift caught (e.g., One-Pager-style 0.30 vs 0.25 → 0.30 vs 0.22) — list of every numerical-comparator update.
7. Storytelling pass observations — any paragraphs where the storytelling rewrite turned out structurally different from the original (intentional or otherwise).
8. Phase 1B readiness — anything that surfaced during 1A that Phase 1B's IA restructure should account for.
9. Any candidate brain captures (likely none; this is bounded execution).

## END PROMPT
