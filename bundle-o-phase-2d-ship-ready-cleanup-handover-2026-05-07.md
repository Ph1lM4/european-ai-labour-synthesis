# Handover Prompt — Bundle O Phase 2D: Ship-Ready Cleanup

Bounded composition session. Closes 12 items surfaced by the 2026-05-07 ship-ready audit on the synthesis site. Three deploy-blockers (llms.txt regen, netlify.toml, sitemap), four ship-quality (second byline, twitter:description, JSON-LD, scroll/outbound tracking), three cleanup (D3 dead-load, touch target, stale data.json key), two Phil-resolved locks ("read" → "analysis" swap, glossary EN/DE strip). ~3–4 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

The 2026-05-07 ship-ready audit surfaced 24/40 binary checks passing with 9 needs-attention + 7 missing items. Phil resolved two earlier-deferred decisions in the same turn ("read" as noun → "this analysis"; glossary EN/DE machinery → strip). This brief absorbs all of it into a single coordinated cleanup pass before deploy.

Three items are deploy-blockers (without them, deploy is unsafe or LLM/SEO indexing breaks). The rest are ship-quality / cleanup / Phil-locked.

---

## START PROMPT

I need you to execute 12 cleanup items on the synthesis site to clear the 2026-05-07 ship-ready audit. All copy edits + structural changes are spec'd verbatim or formula-driven; no authoring beyond Phil-confirmation items.

### Read FIRST (absolute paths)

**Live-site targets (write to these):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/glossary.html`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/llms.txt` — full regen
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sitemap.xml` — refresh
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — single key rename + variation_guard text edit
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — single key rename + variation_guard text edit (mirror SOT)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/netlify.toml` — new file at project root

**Reference:**
- `/Users/philippmaul/Documents/second-brain/knowledge/practitioner/ship-ready-checklist.md` — full checklist; sections §5 (SEO), §6 (LLM), §7 (PostHog), §8 (netlify.toml template) are direct sources for items below
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/llms.txt` — sister-site llms.txt structure to mirror
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/sitemap.xml` — sitemap pattern reference
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html` — read for primary-source count + tier ranking (drives item 4)

### Items (12)

#### A. Deploy-blockers (3)

**1. Regenerate `llms.txt` from current SOT + Phase 2C site copy.**

Current llms.txt is stale: pre-Bundle-V scenario codes (S2a / S2b / S4a / S4b / S5 = Concurrent-Crisis Cascade), missing S3 Jobs Transform, missing Polycrisis Drag, claims 5 Class I countries (was right pre-Bundle-V, now 9), contains "load-bearing demographic finding" (Phase 2C banned phrase).

Full regen using the structure from sister-site `european-demographics-map/site/llms.txt` as a template, with content sourced from:
- `data.json` (SOT) — 36 countries, scenario codes S1–S8, fragility class distribution, lens framework, regime tags
- `site/findings.html` — narrative for the five mechanism findings
- `site/scenarios.html` — eight scenarios + three regimes
- `site/europe.html` — pan-European aggregate findings (Bundle X)
- `site/methodology.html` — five lenses + three corridors + four classes + three regimes + ninth-scenario-considered-but-excluded note (SM 4)

Required content (per checklist §6):
- Title + one-line description
- Author + publication date
- Key findings (8–10 bullets; one specific number per bullet)
- Per-section: 8 scenarios, 3 corridors, 4 fragility classes, 3 regimes
- Reskilling capacity anchor (~7.55 M cohort, ~450 K throughput, 15-year backlog)
- Class distributions (9 / 9 / 15 / 3 across the 36-market scope; 7 / 6 / 14 / 0 across EU-27 — from Bundle X aggregate)
- Pan-European aggregate read (from `cross_cutting_findings.pan_european_aggregate`)
- Sources count (from item 4 below)
- Pages (all 7 with full URLs)
- Data file URL (`https://synthesis.nexalps.com/data.json`)
- Contact (Phil LinkedIn + Nexalps URL)

**Banned-phrase scan on the regenerated llms.txt:** zero hits for `load-bearing`, `structurally`, `structural asymmetry`, `the analysis is built to surface`. Use "this analysis" not "this read" / "the read".

**2. Add `netlify.toml` at project root.**

Path: `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/netlify.toml` (NOT inside `site/`).

Use the checklist §8 template verbatim:

```toml
[build]
  publish = "site"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"

[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=3600"

[[headers]]
  for = "/*.json"
  [headers.values]
    Cache-Control = "public, max-age=86400"
    Access-Control-Allow-Origin = "*"

[[headers]]
  for = "/*.svg"
  [headers.values]
    Cache-Control = "public, max-age=604800"

[[headers]]
  for = "/*.png"
  [headers.values]
    Cache-Control = "public, max-age=604800"

[[redirects]]
  from = "/index.html"
  to = "/"
  status = 301
```

No customisation. Verbatim copy.

**3. Refresh `sitemap.xml`.**

Current state: 5 entries (index, scenarios, methodology, sources, glossary), all `lastmod: 2026-04-30`. Missing `findings.html` + `europe.html`.

Replace with all 7 pages, all `lastmod: 2026-05-07`. Priorities by checklist §3 hub-and-spoke pattern:

| Page | Priority |
|---|---|
| `/` | 1.0 |
| `/findings.html` | 0.9 |
| `/scenarios.html` | 0.9 |
| `/europe.html` | 0.85 |
| `/methodology.html` | 0.8 |
| `/sources.html` | 0.7 |
| `/glossary.html` | 0.7 |

Standard XML format per existing file.

#### B. Ship-quality (4)

**4. Author + propagate second byline on all 7 pages.**

Phil locked option (b): sub-session counts primary sources from `sources.html` and proposes the top 4–5 named by tier ranking; Phil confirms at report-back.

Procedure:
- Parse `site/sources.html` for the source list. Count total primary sources (the file uses a tier system; primary sources are typically Tier 1 + Tier 2 — verify against the file's tier definition).
- Identify the top 4–5 by either: (a) frequency of citation in the synthesis findings, or (b) source-importance tier as defined in sources.html. Pick (a) if citation frequency is reachable from the data; otherwise (b).
- Propose the byline format:

  ```
  Based on <a href="sources.html">N primary sources</a> including X, Y, Z, A, B.
  ```

- Add as a second `<p class="byline">` immediately after the existing first byline on each of the 7 pages.

**Constraint:** the byline copy is Phil-confirmation-pending until report-back. Surface the proposed N + 4–5 names in the report; Phil locks the exact text in a follow-up turn before final deploy. For now, place the proposed text in all 7 pages so Phil can review live.

CSS pattern (per checklist §2 Byline):
```css
.hero .byline { font-size: 12px; color: var(--muted-foreground); line-height: 1.6; }
.hero .byline a { color: var(--muted); text-decoration: underline; text-underline-offset: 2px; }
.hero .byline a:hover { color: var(--foreground); }
.hero .byline + .byline { margin-top: 4px; }
```

If these CSS rules already exist in the per-page inline style block (inherited from sister-site pattern), skip; otherwise add.

**5. Add `twitter:description` on 6 missing pages.**

Currently `index.html` has it; `findings.html`, `scenarios.html`, `europe.html`, `methodology.html`, `sources.html`, `glossary.html` are missing. Add a single line per page mirroring the `og:description` content from the same page:

```html
<meta name="twitter:description" content="<same as og:description>">
```

**6. Add JSON-LD structured data on 6 missing pages** (per checklist §5).

Schema selection per checklist §5:
- `findings.html` + `europe.html` + `scenarios.html` → `Dataset` (data pages)
- `methodology.html` + `sources.html` + `glossary.html` → `Article` (editorial pages)

Use `index.html` existing JSON-LD as the structural template. Each `Dataset` includes `variableMeasured`, `spatialCoverage`, `temporalCoverage`, `keywords`, `license: CC BY 4.0`, `isPartOf` linking to the main synthesis dataset URL. Each `Article` includes `headline`, `author` (Person + LinkedIn), `publisher` (Nexalps), `datePublished` (2026-04-30 or current page lastmod).

Inline `<script type="application/ld+json">` block in `<head>` of each page. Validate with `python3 -c "import json; json.loads(open('test').read())"` per file.

**7. Add `scroll_depth` + `outbound_click` PostHog tracking site-wide.**

Currently every page has `posthog.init` but only some have `posthog.capture` calls (none have scroll_depth or outbound_click). Add the standard IIFE pattern from checklist §7 to every page.

For every page, append after the existing PostHog init block:

```javascript
setTimeout(function(){
  if(typeof posthog==='undefined') return;
  // Scroll depth
  var thresholds=[25,50,75,100], fired={};
  window.addEventListener('scroll', function(){
    var pct=Math.round((window.scrollY/(document.body.scrollHeight-window.innerHeight))*100);
    thresholds.forEach(function(t){
      if(pct>=t && !fired[t]){ fired[t]=true; posthog.capture('scroll_depth',{percent:t,page:'<page_name>'}); }
    });
  }, {passive:true});
  // Outbound clicks
  document.querySelectorAll('a[target="_blank"]').forEach(function(a){
    a.addEventListener('click', function(){ posthog.capture('outbound_click',{url:a.href, page:'<page_name>'}); });
  });
}, 500);
```

Per-page `<page_name>`: `landing`, `findings`, `scenarios`, `europe`, `methodology`, `sources`, `glossary`.

#### C. Cleanup (3)

**8. Remove unused D3 from `index.html` + `findings.html`.**

Phase 2C ports replaced D3 visualisations with inline SVG, but the D3 `<script>` tag was not pruned. Verify with `grep -c "d3\." <file>` — both pages should have 0 method calls. Remove the D3 import line + any associated `<link>` preconnects if D3-specific.

**Don't touch `scenarios.html`** — that page still uses D3 (5 method calls). Verify before removing anywhere.

**9. Bump `stack-seg` mobile `min-height: 36px → 44px`** in `findings.html`.

The `@media (max-width: 480px)` block on `findings.html` sets `.stack-seg { min-height: 36px; }` — below the 44×44 px touch-target spec. Update to `min-height: 44px`. No other changes needed.

**10. Rename stale `s2b_only_optimism` key.**

In `data.json` (site copy) and `layer-6-deliverable-data.json` (master SOT), rename:

```
cross_cutting_findings.s2b_only_optimism → cross_cutting_findings.s2_only_optimism
```

Also grep for any JS consumers referencing `s2b_only_optimism` across all 7 HTML files and rename to `s2_only_optimism`. Verify with:

```
grep -rn "s2b_only_optimism\|s2b-only-optimism" site/*.html site/data.json layer-6-deliverable-data.json
```

Should return 0 hits post-rename.

#### D. Phil-resolved locks (2)

**11. "read" → "this analysis" site-wide swap.**

Pre-flight grep:
```
grep -in '\bthis read\b\|\bthe read\b' site/*.html site/data.json site/llms.txt layer-6-deliverable-data.json
```

Apply per-instance:

| Location | Original | Replacement |
|---|---|---|
| `index.html` (landing SM 4) | "Three known gaps bound this read" | "Three known gaps bound this analysis" |
| `methodology.html` SM 3 | "Three known gaps constrain this read:" | "Three known gaps constrain this analysis:" |
| `methodology.html` §7 subtitle | "Five gaps that bound the read" | "Five gaps that bound the analysis" |
| `europe.html` variation guard | "the variation underneath is the read" | "the variation underneath is the analysis" |
| `data.json` + `layer-6-deliverable-data.json` `variation_guard_note` | (same string) | (same edit) |

**Plural usage on `findings.html` §5 subtitle:** "Five reads beneath the headline" → **"Five findings beneath the headline"** (Phil-locked).

After all swaps, re-grep returns 0 hits.

**12. Strip glossary EN/DE machinery entirely.**

`glossary.html` currently carries `getLangMode()` / `getSubLang()` runtime machinery for switching definition language between EN and DE. Phil locked: remove entirely. Glossary is English-only.

Procedure:
- Delete the `getLangMode()` and `getSubLang()` JS functions
- Delete any `data-lang-de` / `data-sub-lang` attributes from glossary content blocks (or, if every glossary entry has both EN and DE versions in HTML, keep the EN-only path and delete the DE blocks; sub-session decides based on actual structure)
- Delete any `<button>` UI affordances that triggered the language switch (Phase 2C already removed the nav-level toggle; verify no in-page toggle remains)
- Verify no JS console errors on `glossary.html` post-strip

### Constraints

- **No new design tokens.** Use existing `--bg`, `--fg`, `--muted`, `--ring`, `--card`, `--card-border`, `--radius-md`, `--radius-sm`, `--class-i/ii/iii/iv` only.
- **No external libraries.**
- **`data.json` + `layer-6-deliverable-data.json` only modified for items 10 + 11** (key rename + variation_guard text edit). All other content untouched.
- **Phase 1B / 2B / 2C IA preserved** (cross-link state machine, all 5 visualisations, mobile responsive, PostHog interactives all still work post-edit).
- **No emoji.**
- **Banned-phrase scan applies to all changes** (per the brain rule landed 2026-05-06): every public-facing edit re-greps the avoid-list against the modified files before reporting done.
- **Phil does all git commits.**

### Verification (before reporting back)

1. **All 12 items addressed.**
2. **`llms.txt` regenerated** with: zero pre-Bundle-V codes (S2a/S2b/S4a/S4b/S5), zero banned phrases (`load-bearing`, `structurally`, etc.), 8 scenarios named including S3 Jobs Transform + S8 Polycrisis Drag, Class I = 9 countries, all 7 page URLs, data file URL.
3. **`netlify.toml`** present at project root, parses as valid TOML.
4. **`sitemap.xml`** has 7 entries + `lastmod: 2026-05-07` on all + correct priorities + valid XML.
5. **Second byline** present on all 7 pages with the proposed N + 4–5 names; sub-session surfaces N + names in report-back for Phil lock.
6. **`twitter:description`** present on all 7 pages.
7. **JSON-LD** present on all 7 pages; correct schema (`Dataset` on data pages, `Article` on editorial pages); valid JSON.
8. **`scroll_depth` + `outbound_click`** tracking present on all 7 pages with correct page-name parameter.
9. **D3 `<script>` removed** from `index.html` + `findings.html`; remains on `scenarios.html`.
10. **`stack-seg` min-height = 44px** on `findings.html` mobile.
11. **`s2b_only_optimism` → `s2_only_optimism`** in both JSONs + 0 residual references in HTML.
12. **"read" → "analysis" + "Five reads" → "Five findings"** swaps applied; 0 residual `\bthis read\b` or `\bthe read\b` hits.
13. **Glossary EN/DE machinery stripped**; `glossary.html` console-error-free.
14. **Banned-phrase grep** returns 0 hits across all 7 pages + llms.txt.
15. **Cross-link state machine + all 5 visualisations + mobile responsive + PostHog** all still work post-edit.

### When done — report back to master session with

1. Per-page line-count diff.
2. Verification checklist (1–15) — pass/fail per item.
3. **Proposed second byline (item 4):** N count + top 4–5 named sources + final byline text. Phil locks at next turn.
4. **`llms.txt` content audit** — confirm Polycrisis Drag named, Class I = 9, S3 Jobs Transform present, source count matches item 4, banned-phrase grep clean.
5. **`netlify.toml` content** — paste verbatim for Phil sanity-check.
6. **`sitemap.xml` final state** — 7 URLs + lastmod + priorities.
7. **JSON-LD audit** — schema selected per page + sample `@type` + validation result.
8. **Tracking audit** — sample of `posthog.capture` calls per page.
9. **Banned-phrase grep audit** — confirmation of 0 hits site-wide.
10. **Bundle W readiness** — anything new this session that Bundle W should account for (unlikely — this is contained cleanup).
11. **Any candidate brain captures** (likely none beyond what's already landed).

## END PROMPT
