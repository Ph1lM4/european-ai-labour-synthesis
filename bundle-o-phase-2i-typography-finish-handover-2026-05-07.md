# Handover Prompt — Bundle O Phase 2I: Typography Finish + Container Width Normalisation

Bounded composition session. Two scopes Phase 2H didn't fully resolve: (1) complete the systematic type-scale audit on `scenarios.html` + `europe.html` (Phase 2H built the full audit table for `methodology.html` only, patched scenarios + europe at the two Phil-flagged spots); (2) widen `methodology.html` + `sources.html` from narrow article container to wide container (1200px) for synthesis-internal visual consistency, overriding the ship-ready checklist §3 article-format convention specifically for this layer. ~2 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Phase 2H ran a systematic type-scale audit on methodology.html (full per-element table in the report), patched scenarios.html + europe.html at two Phil-flagged spots (reskilling-gap inline numbers; europe pull-quote bold), and fixed `.plain-block h3` 17→16 across both. But the full per-element audit didn't extend to scenarios + europe. Phil reports both pages still have inconsistent font sizes section-to-section.

Container width is a separate issue: 5 pages use `.container { max-width: 1200px }` (wide); methodology + sources use `.container-narrow { max-width: 780px / 760px }` (narrow article format per checklist §3). The narrow centering reads visually inconsistent against the wide pages, and synthesis-specific content density (4-SM methodology, 54 source-cards) doesn't benefit from the article-format constraint. Phil locks: widen to match.

---

## START PROMPT

I need you to (1) complete the systematic type-scale audit on `scenarios.html` and `europe.html` that Phase 2H started, applying every Aligning fix and surfacing every Decision; and (2) widen the methodology + sources containers from narrow to wide (1200px) for synthesis-internal consistency.

### Read FIRST (absolute paths)

**Synthesis live-site (write to these):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html`

**Reference (Phase 2H output + canonical):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-o-phase-2h-typography-cleanup-handover-2026-05-07.md` — Phase 2H's audit method (the §6 methodology table is the template to apply to scenarios + europe)
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/index.html` — canonical type-scale + colour reference
- `/Users/philippmaul/Documents/second-brain/knowledge/practitioner/ship-ready-checklist.md` §1 (type scale)

### Scope 1 — Type-scale audit completion (scenarios + europe)

Apply the same audit method Phase 2H used on methodology.html, but on `scenarios.html` and `europe.html`:

**Step 1 — Build the per-element table** for each page. Grep all `font-size:` declarations. Map each to canonical slot:

| Slot | Size |
|---|---|
| labels (uppercase eyebrows) | 10–11 px |
| meta / footer | 12 px |
| notes | 13 px |
| body small | 14 px |
| body | 15 px |
| lead | 16 px |
| section headings narrow | 18 px |
| stat values / burger links | 20 px |
| section headings wide | 22 px |
| page headings mobile | 24–28 px |
| h1 desktop | 36 px |

**Step 2 — Categorise every declaration** as:
- **Necessary** — synthesis-specific component (delta-tile, scenario-row, weather-card pop, country-pill, etc.) that genuinely needs a custom size. Keep + document why.
- **Aligning** — straightforward port from canonical. Apply silently.
- **Decision** — synthesis has deliberately diverged for a layout reason. Surface for Phil.

**Step 3 — Fractional sizes** (10.5 / 11.5 / 12.5 / 13.5 px) Phase 2H kept in europe + scenarios as Decision items. Re-evaluate: are these still necessary, or can they round to canonical slots without breaking layout? If a fractional size sits inside a `font-size: clamp()` or `font-size: calc()`, document as intentional. Otherwise round to nearest slot.

**Step 4 — Apply** all Aligning fixes silently. Surface Decisions.

### Scope 2 — Container width normalisation

**Currently:**
- `.container { max-width: 1200px; margin: 0 auto; padding: 0 32px }` — used by index, findings, scenarios, europe, glossary
- `.container-narrow { max-width: 780px; margin: 0 auto; padding: 0 32px }` — methodology
- `.container-narrow { max-width: 760px; margin: 0 auto; padding: 0 32px }` — sources

**Phil-locked target:**
- All 7 pages use `.container` with `max-width: 1200px`.
- The `.container-narrow` rule is removed (or kept as an unused alias) on methodology + sources.
- Methodology + sources content layout works at 1200px — sub-session verifies sections + tables + source-cards still render cleanly without forced edge-to-edge stretching.

**Procedure:**

1. On `methodology.html`: every `<section class="container-narrow ...">` and `<header class="container-narrow ...">` → change to `<section class="container ...">` / `<header class="container ...">`. Remove the `.container-narrow` CSS rule from the inline `<style>` block.
2. On `sources.html`: same. Plus remove the 760 / 780 inconsistency.
3. **Inner content max-widths** — the prose readability concern (line length too long at 1200px) is real. Mitigate by setting per-element max-width on prose containers where appropriate:
   - `<p>` paragraphs in dense prose sections: `max-width: 760px` (or whatever reads cleanly) so reading line-length stays comfortable while the section container is wide.
   - `<h2>` / `<h3>` headings: no inner max-width needed (short enough to read at any width).
   - Tables, code blocks, source-card grids: take the full 1200px.
   - Sub-session decides per-section whether to apply inner max-width or let content breathe.
4. **Verify methodology page reads well at 1200px desktop** — no orphan whitespace pockets, no sections that visually fall apart at the wider width.
5. **Verify sources page reads well at 1200px** — source-card grid likely fits wider naturally; the cross-layer footer cards too.

### Constraints

- **No Phil-locked copy edits.**
- **No new design tokens.** Existing tokens only.
- **No IA changes.** Same 7 pages, same nav, same JSON-LD, same byline.
- **`data.json` + `layer-6-deliverable-data.json` unchanged.**
- **Cross-link state machine + 5 visualisations + PostHog interactives all still work.**
- **Mobile responsive at 375 / 768 / 1280** preserved. Narrow→wide container change is a desktop-feel change; mobile already collapses to single-column at the 480/768 breakpoints regardless.
- **Banned-phrase grep at the end** as confirmation.
- **Phil does all git commits.**

### Verification (before reporting back)

1. **Scenarios + Europe per-element audit tables** complete. Every `font-size:` declaration mapped to canonical slot with verdict (Necessary / Aligning / Decision). All Aligning fixes applied.
2. **Fractional sizes** re-evaluated — if rounded, document; if kept, document why.
3. **Methodology + Sources containers widened** to 1200px (`.container`, not `.container-narrow`). `.container-narrow` rule removed from both pages' inline `<style>` blocks.
4. **Prose inner max-widths** applied where appropriate (long prose paragraphs constrained for readability at the wider container).
5. **All 7 pages** parse cleanly; zero console errors.
6. **Mobile responsive** at 375 / 768 / 1280 preserved (visual check via browser preview if available; static check via `@media` rule preservation if not).
7. **Cross-link state machine + 5 visualisations + PostHog** preserved on all pages.
8. **Banned-phrase grep** clean.

### When done — report back to master session with

1. **Per-page line-count diff.**
2. **Verification checklist (1–8)** — pass/fail per item.
3. **Scenarios.html type-scale table** — full per-element listing with canonical slot mapping + Aligning fixes applied + Decision items.
4. **Europe.html type-scale table** — same shape.
5. **Container widening summary** — methodology + sources before/after; inner max-width policy applied (which elements got constrained, which didn't, why).
6. **Reading-line-length verification** — sample paragraph rendered at 1200px; line length per em (target ~60–80 chars per line for prose, narrower for compact data callouts).
7. **Decision items surfaced** — anywhere scenarios + europe have intentional divergence from canonical that warrants Phil's lock.
8. **Bundle W readiness** — anything new this session that Bundle W needs to absorb (likely: methodology + sources deliverable docs may inherit container conventions if site CSS is referenced).
9. **Any candidate brain captures** — likely "container width as visual-rhythm signal" or "type-scale completion at the section level beats spot-fixing".

## END PROMPT
