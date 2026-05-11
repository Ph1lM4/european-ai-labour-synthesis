# Handover Prompt — Bundle O Phase 2H: Typography + Style Consistency Pass

Bounded composition session. Five Phil-flagged typography/style issues + a systematic audit of all 7 synthesis pages against the sister-layer canonical (demographics) + ship-ready checklist §1 type scale. Output is consistent typography/styling across the synthesis site, matching the rest of the nexalps portfolio. ~2–3 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Phil reviewed the 2026-05-07 ship-ready / 2D / 2E / 2F / canaries-fix state of the synthesis site and flagged 5 typography/style issues:

1. **Conclusion header on findings.html** — different style from the orange numbered section headers; should match.
2. **Reskilling-capacity gap number on scenarios.html** — same too-large inline number issue Italy had (fixed earlier from 24px to inherit). Needs the same fix here.
3. **Link colour is off** — somewhere on the site, link colour deviates from the canonical orange/muted convention.
4. **Methodology page text sizes are a wild mix** — multiple deviations from the canonical type scale visible on a single page.
5. **Europe pull-quote is italic + bold** — questioning the bold treatment (italic alone may be sufficient; or italic + accent colour, but not bold + italic which reads as visual noise).

Underlying pattern: synthesis CSS evolved across Phase 1A → 1B → 2A → 2B → 2C → 2D → 2E with iterative additions but never a systematic alignment to sister-layer convention. This brief is the systematic alignment.

---

## START PROMPT

I need you to fix five specific Phil-flagged typography/style issues and run a systematic audit of all 7 synthesis pages against the sister-layer canonical (demographics) + ship-ready checklist type scale, applying any other deviations surfaced.

### Read FIRST (absolute paths)

**Synthesis live-site (write to these):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/glossary.html`

**Canonical references:**
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/index.html` — sister-layer canonical for typography + colour conventions. Read its `<style>` block end-to-end as the reference style guide.
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/methodology.html` — secondary reference, same project.
- `/Users/philippmaul/Documents/second-brain/knowledge/practitioner/ship-ready-checklist.md` §1 (Design System) — canonical type scale, colour usage, letter-spacing rules, line-height rules, font-weight rules.

### Phil-flagged issues (5)

#### 1. Conclusion header on findings.html

Currently the Conclusion section uses `<h3>Conclusion</h3>` with the `.conclusion` class wrapper (Phase 2C plain-text conversion). The header reads as a plain h3, not matching the orange-numbered section header style used by §1 Prelude / §2 / §3 / etc. on the same page.

Fix: render the Conclusion as a section with the same header pattern. Likely:
```html
<h2><span class="num">8.</span> Conclusion</h2>
```
(or whatever the next sequential number is at that point in the page).

Verify the section-num + h2 pattern matches the prevailing style on findings.html exactly. If "Conclusion" doesn't take a section number for narrative reasons, surface that decision and propose a section h2 without the numeric prefix that still matches the visual h2 weight + size + letter-spacing.

#### 2. Reskilling-capacity gap number on scenarios.html

Same pattern as the Italy fix on findings.html (resolved earlier — `.italy-block .number` font-size dropped from `24px` to inherit). The reskilling-capacity gap block on scenarios.html has at least one inline number rendered at display size that should be inline body bold + accent colour.

Pre-flight grep:
```
grep -n "font-size:[ ]*\(20\|22\|24\|28\|32\)px" site/scenarios.html
```

Find every instance where an inline number/stat is rendered at display size inside body prose, and inherit body size (or at most lead size at 18px) with `font-weight:700` and accent colour for emphasis. Apply the same pattern as `.italy-block .number` post-Italy-fix.

#### 3. Link colour audit

Pre-flight grep across all 7 pages for any `color:` declaration on `a`, `a:link`, or `a:visited` selectors. The canonical link colour is the muted body-link convention (not orange/`--ring`, which is reserved for the active nav item). Sister-layer pattern (demographics):
```css
a { color: var(--muted); text-decoration: underline; text-underline-offset: 2px; }
a:hover { color: var(--foreground); }
```

(or whatever demographics actually uses — verify by reading demographics CSS).

Identify any synthesis page where link colour deviates (e.g. orange where it should be muted, or a non-token hex value). Apply the canonical convention site-wide.

Distinct cases to preserve:
- Active nav link (`aria-current="page"`) — keep `color: var(--ring)` (orange)
- Source-card title links inside `sources.html` — may have a deliberate styling; preserve unless inconsistent with the rest of the site

#### 4. Methodology page font-size mix

Pre-flight: grep all `font-size:` declarations in `methodology.html` inline `<style>` block. Compare against the ship-ready checklist §1 type scale:

| Use | Size |
|---|---|
| labels (uppercase eyebrows) | 10 px |
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

Any methodology size that doesn't fit one of these slots is a deviation. Fix to the closest canonical slot. Surface the diff in report-back.

Also verify: no body text smaller than 10 px anywhere on mobile (per checklist mobile rule).

#### 5. Europe pull-quote — italic + bold

The europe.html headline pull-quote (sourced from data.json `headline_finding_pan_european`) is currently rendered in italic + bold. Phil flagged the bold as visual noise.

Fix: drop `font-weight:700` (or whatever weight is applied); keep italic; consider increasing size slightly (to lead 16px or section-heading 18px) or adding accent-colour border-left to compensate for the lost emphasis. Sub-session picks the cleanest treatment that matches the sister-layer pull-quote / blockquote convention on demographics. Surface the choice.

### Systematic audit (all 7 pages)

After fixing the 5 specific issues, run a systematic typography audit:

**Step 1 — Build the canonical type-scale map** from demographics index.html + ship-ready checklist §1. Document every CSS variable, every `font-size`/`font-weight`/`letter-spacing`/`line-height`/`color` declaration that constitutes the canonical style.

**Step 2 — Diff each synthesis page** against the canonical. Identify every CSS declaration on a class/element that deviates from the canonical (without reasonable cause).

**Step 3 — Categorise deviations:**
- **Necessary** — synthesis-specific component (rastered map cells, weather-pattern bars, fragility-class colour pills) needing custom CSS that has no demographics analogue. Keep as-is.
- **Aligning** — straightforward port from canonical (h2/h3 sizes, body line-height, link colour). Apply.
- **Decision** — synthesis has deliberately diverged for a layout reason (e.g., narrower max-width on a specific section). Surface for Phil decision in report-back.

**Step 4 — Apply all "Aligning" fixes** without surfacing. Surface the "Decision" set with rationale.

### Constraints

- **No Phil-locked copy edits.** Typography only; no rewrites of locked text (Minto SMs, hero, etc.).
- **No new design tokens.** Use existing `--bg`, `--fg`, `--muted`, `--ring`, `--card`, `--card-border`, `--radius-md`, `--radius-sm`, `--class-i/ii/iii/iv` only. If a clearly-needed token is missing, propose for Phil decision rather than introduce silently.
- **`data.json` + `layer-6-deliverable-data.json` unchanged.**
- **Phase 1B / 2B / 2C / 2D / 2E / 2F IA preserved** (cross-link state machine, all 5 visualisations, mobile responsive, PostHog interactives, sources page structure all still work).
- **No emoji.**
- **Banned-phrase scan applies to any minor copy edits** that surface (per the brain rule landed 2026-05-06). Most of this session is CSS-only; banned-phrase risk is low. Run the grep at the end as confirmation.
- **Phil does all git commits.**

### Verification (before reporting back)

1. **Conclusion header on findings.html** matches the section-h2 + `.num` pattern of §1–§N on the same page (or surfaces an explicit reason why it doesn't take a number).
2. **Reskilling-capacity gap inline numbers** on scenarios.html are body-size + bold + accent colour, not display size.
3. **Link colour** is canonical (muted with hover-to-foreground) on every page where it deviated; active nav + source-card title links preserved per their existing intent.
4. **Methodology page font sizes** all fit the canonical type-scale slots; no deviations except documented Decision items.
5. **Europe pull-quote** is italic-only (no bold); cleanest treatment chosen per demographics convention.
6. **Systematic audit** completed across all 7 pages. Aligning fixes applied. Decision items surfaced with rationale.
7. **All 7 pages parse cleanly; zero console errors.**
8. **Mobile responsive at 375 / 768 / 1280** still holds.
9. **Cross-link state machine + all 5 visualisations + PostHog interactives** all still work.
10. **Banned-phrase grep** clean across any text edits.

### When done — report back to master session with

1. Per-page line-count diff (additions / removals).
2. Verification checklist (1–10) — pass/fail per item.
3. **Conclusion section** — final markup + any Phil-decision surfaces (number or no number).
4. **Reskilling-capacity gap fix** — before/after CSS diff.
5. **Link colour audit** — every deviation found + the canonical fix applied + which pages were affected.
6. **Methodology type-scale audit** — full table of every `font-size` declaration on the page, mapped to canonical slot, with the fix applied.
7. **Europe pull-quote** — final styling + reasoning (italic-only / italic + size bump / italic + border-left).
8. **Systematic audit summary** — total deviations found, count of Aligning fixes applied, count of Decision items surfaced.
9. **Decision items** — any places where synthesis deliberately diverges from canonical with rationale, for Phil's lock.
10. **Bundle W readiness** — anything new this session that Bundle W needs to absorb (e.g., if methodology page now has different h3 weights than Specialist Appendix, flag for alignment).
11. **Any candidate brain captures** — likely a process pattern around typography-audit-against-canonical at phase boundaries.

## END PROMPT
