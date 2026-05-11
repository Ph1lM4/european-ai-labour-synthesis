# Page Pagination Block — Implementation Report

**Date:** 2026-05-11
**Scope:** 7 synthesis pages — `index.html`, `findings.html`, `scenarios.html`, `europe.html`, `methodology.html`, `sources.html`, `glossary.html`
**Goal:** Add a button-style bottom-of-page pagination block matching the sister-site CTA convention, with per-page back/forward targets per the Phil-locked table.

---

## Step 1 — Captured pattern

### Where the canonical pattern lives

**Source:** `/Users/philippmaul/Documents/projects/european-reskilling-map/site/transitions.html` (and `index.html`) — reskilling.nexalps.com.

**Important caveat:** None of the 5 sister projects ship a dedicated **pagination block** in the strict prev-page / next-page sense. What they ship is a `.cta-bar` container used at section transitions (most consistently on reskilling). I matched its visual primitives — the orange-filled `.btn-primary` + bordered `.btn-outline` pair inside a centered card — and repurposed them as a true pagination block. This is the closest captured pattern. The synthesis site is the first product in the suite to use the `.cta-bar` primitive as cross-page pagination per se; the visual register is identical to reskilling.

Among the 5 sites the `.cta-bar` markup is most cleanly used in reskilling (it ships variants on both `/` and `/transitions`). ai-exposure has a single instance on `/` using a slightly older `.cta-text` / `.cta-sub` shape; the other three sites don't ship a `.cta-bar` at all. The reskilling shape is the most-recently-shipped and the most-replicated, so it wins.

### Captured HTML (verbatim — reskilling transitions.html line 339)

```html
<div class="cta-bar">
  <h3>Why does this matter?</h3>
  <p>...</p>
  <div class="btn-row">
    <a href="lenses.html" class="btn btn-primary">Read the Lenses page &rarr;</a>
    <a href="index.html" class="btn btn-outline">&larr; Back to the gap</a>
  </div>
</div>
```

### Captured CSS (verbatim — reskilling transitions.html lines 89–95)

```css
.cta-bar{max-width:760px;margin:48px auto;padding:32px 24px;background:var(--card);border:1px solid var(--card-border);border-radius:var(--radius-lg);text-align:center}
.cta-bar h3{font-size:20px;font-weight:700;margin-bottom:8px}
.cta-bar p{font-size:14px;color:var(--muted);margin-bottom:20px;line-height:1.6}
.btn{display:inline-block;padding:10px 24px;border-radius:var(--radius-md);font-family:var(--font);font-size:14px;font-weight:600;text-decoration:none;transition:all var(--transition)}
.btn-primary{background:var(--ring);color:#000}.btn-primary:hover{background:#fb923c}
.btn-outline{background:transparent;color:var(--muted);border:1px solid var(--border)}.btn-outline:hover{border-color:rgba(255,255,255,0.25);color:var(--foreground)}
.btn-row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
```

### Captured analytics handler (verbatim — reskilling transitions.html lines 592–596)

```js
document.querySelectorAll('.btn').forEach(btn=>{
  btn.addEventListener('click',()=>{
    if(window.posthog)posthog.capture('cta_clicked',{href:btn.getAttribute('href'),text:btn.textContent.trim(),page:'transitions'});
  });
});
```

Outbound is layered separately (existing pattern on all sites):
```js
document.querySelectorAll('a[target="_blank"]').forEach(function(a){a.addEventListener('click',function(){posthog.capture('outbound_click',{url:a.href,text:a.textContent.trim().slice(0,80),page:'transitions'})})});
```

### Captured visual details

| Aspect | Captured |
|---|---|
| Container | rounded card, `--radius-lg` (12px), `--card-border` 1px, `--card` background, centered, max-width 760px, 48px vertical margin |
| Primary button | filled, `--ring` (orange `#f97316`) bg, black text, hover `#fb923c` |
| Outline button | transparent bg, muted text, 1px `--border`, hover lifts to `--foreground` + brighter border |
| Button shape | radius-md (8px), 10px/24px padding, 14px/600 Geist |
| Glyphs | `&rarr;` (→) **after** primary text; `&larr;` (←) **before** outline text. No ↗ used in reskilling — but ↗ is the suite-wide convention for outbound suite links (used in burger menus across all 5 sites) |
| Mobile stacking | sister sites: only `flex-wrap:wrap` on `.btn-row` (no explicit column switch). Touch targets ~40px on reskilling — below WCAG AA 44px |
| Position | inside content flow, *not* inside `<footer>` |
| Semantic role | `<div>` on reskilling — not `<nav>` |

### Synthesis additions vs the captured pattern (3 explicit deviations, all documented)

1. **DOM order — back-left, forward-right (universal pagination convention).** Reskilling renders **forward-first / back-second** in DOM order (visual: forward → on the left, back ← on the right). Phil's Step 2 table explicitly labels Left = Back, Right = Forward, so I reversed the DOM order on standard pages. The visual register, classes, and styling are identical to reskilling — only the order changed. Hub (index) and tail (glossary) have only one back-relevant slot so the question doesn't arise there.
2. **`<nav>` wrapper with `aria-label`.** Reskilling uses a bare `<div>`. The brief requires "nav with aria-label" — I wrap in `<nav class="cta-bar page-pagination container" aria-label="Page navigation">`. Visually identical because `.cta-bar` styles apply to any block element.
3. **Mobile touch targets ≥44px.** Reskilling buttons are ~40px tall on mobile. The brief requires ≥44px. I added a 640px breakpoint that switches `.btn-row` to `flex-direction:column`, stretches buttons full-width, and pumps padding to 14px/24px with `min-height:44px`. Desktop styling is unchanged from reskilling.

Glyph distinction also added per the brief: `&nearr;` (↗) on the two outbound AI Exposure buttons (index.html, glossary.html). This matches the suite-wide convention for outbound links (the burger-menu pattern on every site).

---

## Step 2 / 3 — Per-page markup deliverable

The pagination nav was inserted **immediately before `</main>`** on every page (inside `<main>`, outside `<footer>`). Footer untouched.

One-line diff per page (the `<nav>` element only, btn-row + closing tags omitted for brevity):

| Page | `<nav>` line + interior buttons (paraphrased) |
|---|---|
| `index.html:266–271` | `<nav class="cta-bar page-pagination container" aria-label="Page navigation">` → **[Findings →]** `btn-primary` → `findings.html` + **[AI Exposure ↗]** `btn-outline` external |
| `findings.html:536–541` | same `<nav>` shell → **[← Overview]** `btn-outline` → `index.html` + **[Scenarios →]** `btn-primary` → `scenarios.html` |
| `scenarios.html:475–480` | same shell → **[← Overview]** + **[Europe →]** → `europe.html` |
| `europe.html:272–277` | same shell → **[← Overview]** + **[Methodology →]** → `methodology.html` |
| `methodology.html:380–385` | same shell → **[← Overview]** + **[Sources →]** → `sources.html` |
| `sources.html:321–326` | same shell → **[← Overview]** + **[Glossary →]** → `glossary.html` |
| `glossary.html:197–202` | same shell → **[← Overview]** + **[AI Exposure ↗]** `btn-primary` external (loop back to suite) |

All anchors carry `data-direction` (`back` / `forward` / `outbound`) and `data-target-page` for analytics. Outbound anchors carry `target="_blank" rel="noopener"`.

Concrete markup (standard 5 pages, exemplified by findings.html lines 536–541):

```html
<nav class="cta-bar page-pagination container" aria-label="Page navigation">
  <div class="btn-row">
    <a href="index.html" class="btn btn-outline" data-direction="back" data-target-page="overview">&larr; Overview</a>
    <a href="scenarios.html" class="btn btn-primary" data-direction="forward" data-target-page="scenarios">Scenarios &rarr;</a>
  </div>
</nav>
```

Hub variant (index.html lines 266–271):

```html
<nav class="cta-bar page-pagination container" aria-label="Page navigation">
  <div class="btn-row">
    <a href="findings.html" class="btn btn-primary" data-direction="forward" data-target-page="findings">Findings &rarr;</a>
    <a href="https://ai-exposure.nexalps.com/" class="btn btn-outline" target="_blank" rel="noopener" data-direction="outbound" data-target-page="ai-exposure">AI Exposure &nearr;</a>
  </div>
</nav>
```

Tail variant (glossary.html lines 197–202):

```html
<nav class="cta-bar page-pagination container" aria-label="Page navigation">
  <div class="btn-row">
    <a href="index.html" class="btn btn-outline" data-direction="back" data-target-page="overview">&larr; Overview</a>
    <a href="https://ai-exposure.nexalps.com/" class="btn btn-primary" target="_blank" rel="noopener" data-direction="outbound" data-target-page="ai-exposure">AI Exposure &nearr;</a>
  </div>
</nav>
```

---

## CSS additions (consolidated — identical on all 7 pages, appended to each `<style>` block)

```css
/* ── Pagination ── */
.cta-bar{max-width:760px;margin:48px auto;padding:32px 24px;background:var(--card);border:1px solid var(--card-border);border-radius:var(--radius-lg);text-align:center}
.btn-row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.btn{display:inline-block;padding:10px 24px;border-radius:var(--radius-md);font-family:var(--font);font-size:14px;font-weight:600;text-decoration:none;transition:all var(--transition);line-height:1.5}
.btn-primary{background:var(--ring);color:#000}.btn-primary:hover{background:#fb923c}
.btn-outline{background:transparent;color:var(--muted);border:1px solid var(--border)}.btn-outline:hover{border-color:rgba(255,255,255,0.25);color:var(--foreground)}
@media(max-width:640px){.btn-row{flex-direction:column;align-items:stretch}.btn{padding:14px 24px;min-height:44px;display:flex;align-items:center;justify-content:center}}
```

Total addition: **7 declarations + 1 media query** per page. Inlined per-page (matching the synthesis project's current style — each page already inlines its full stylesheet; no shared CSS file exists).

CSS variables consumed (`--card`, `--card-border`, `--radius-lg`, `--ring`, `--border`, `--muted`, `--foreground`, `--font`, `--radius-md`, `--transition`) are already defined identically across all 7 synthesis pages and match the reskilling site — no variable drift.

### Analytics handler additions

Each page's existing IIFE got this appended just before `})();` (only the `page:` literal varies):

```js
// ── Pagination ──
document.querySelectorAll('nav.page-pagination a').forEach(a=>{
  a.addEventListener('click',()=>{
    try{posthog.capture('pagination_click',{direction:a.dataset.direction,target_page:a.dataset.targetPage,page:'PAGE'})}catch(e){}
  });
});
```

Per-page `page:` values: `landing` / `findings` / `scenarios` / `europe` / `methodology` / `sources` / `glossary` (matching each page's existing scroll-depth posthog identifier).

**Outbound buttons (index + glossary)** carry `target="_blank"` and are therefore additionally captured by the **pre-existing** `outbound_click` handler that already lives in every page's `<head>` script (no change needed — it auto-binds all `a[target="_blank"]`).

---

## Accessibility checks

| Check | Result |
|---|---|
| Semantic landmark | `<nav>` element used, distinct from main content nav |
| `aria-label` | `"Page navigation"` on the `<nav>` (distinguishes from the main `site-nav` which uses `"Main navigation"`) |
| Keyboard tab order | DOM order = visual order on standard pages (back ← first, forward → second). Hub/tail follow the same DOM-order = visual-order rule |
| Focus styles | Inherited from the existing `:focus-visible{outline:2px solid var(--ring);outline-offset:2px}` rule (line 66 of each page) — already covers `<a>` elements |
| Link semantics | All buttons are `<a href="...">`, not `<button>` — correct for page navigation |
| External link signaling | `target="_blank" rel="noopener"` on outbound; `&nearr;` (↗) glyph as visual cue. No `aria-label` override since the visible text already says "AI Exposure" + arrow |
| Color contrast | `.btn-primary` (black text on `#f97316` orange) and `.btn-outline` (muted-gray text on dark `#0a0a0c` card) both inherit from the reskilling design system — already shipped and validated on a sister product |

Not added (intentionally): `rel="nofollow"`, custom keyboard handlers, role attributes. `<nav>` + `<a>` semantics are already correct without them.

---

## Mobile verification (375px viewport)

**What was verified (by code review of the CSS, not by running a preview):**

- `@media(max-width:640px)` fires at 375px ✓
- `.btn-row{flex-direction:column;align-items:stretch}` → buttons stack vertically ✓
- `.btn{padding:14px 24px;min-height:44px;display:flex;align-items:center;justify-content:center}` → each button is **≥44px tall** at mobile (28px vertical padding + 14px font with line-height ≈ 1.5 → ~49px) ✓
- Buttons full-width inside the `.cta-bar` (max-width:760px, padding 32×24, so on a 375px viewport the card has ~16px page padding via `.container` → buttons fill the ~327px inner width) ✓

**What was NOT verified (honest disclosure):**

- I did not start the synthesis dev server and load the pages in a real 375px viewport. The CSS is a near-clone of the reskilling pattern (already running at scale on a sister site) plus the explicit mobile stack/touch-target additions. The code-craft post-code gate flags this as "uncertainty a human should verify" — recommend Phil opens the preview at 375px and confirms button stack + readable arrow glyphs before pushing.

---

## Audit table — 7 rows

| # | Page | `<nav>` element present | Back (left) target | Forward (right) target | Outbound flag | PostHog event | Phil-lock match |
|---|---|---|---|---|---|---|---|
| 1 | `site/index.html` | line 266 ✓ | — (none, this IS the hub) | `findings.html` + `https://ai-exposure.nexalps.com/` (two forward) | yes (AI Exposure) | `pagination_click` page=`landing` + `outbound_click` (existing) | ✓ |
| 2 | `site/findings.html` | line 536 ✓ | `index.html` | `scenarios.html` | no | `pagination_click` page=`findings` | ✓ |
| 3 | `site/scenarios.html` | line 475 ✓ | `index.html` | `europe.html` | no | `pagination_click` page=`scenarios` | ✓ |
| 4 | `site/europe.html` | line 272 ✓ | `index.html` | `methodology.html` | no | `pagination_click` page=`europe` | ✓ |
| 5 | `site/methodology.html` | line 380 ✓ | `index.html` | `sources.html` | no | `pagination_click` page=`methodology` | ✓ |
| 6 | `site/sources.html` | line 321 ✓ | `index.html` | `glossary.html` | no | `pagination_click` page=`sources` | ✓ |
| 7 | `site/glossary.html` | line 197 ✓ | `index.html` | `https://ai-exposure.nexalps.com/` (loop back to suite) | yes | `pagination_click` page=`glossary` + `outbound_click` (existing) | ✓ |

All 7 rows pass the Phil-locked table from Step 2.

---

## Files changed

- [site/index.html](site/index.html)
- [site/findings.html](site/findings.html)
- [site/scenarios.html](site/scenarios.html)
- [site/europe.html](site/europe.html)
- [site/methodology.html](site/methodology.html)
- [site/sources.html](site/sources.html)
- [site/glossary.html](site/glossary.html)

Each file received 3 inserts: CSS block (before `</style>`), pagination `<nav>` (before `</main>`), posthog handler (before `})();` in IIFE). Footer, hero, body content, existing scripts all untouched.

---

⚠️ **Code Review Summary (code-craft rubric)**

- **Names:** `page-pagination`, `pagination_click`, `data-direction`, `data-target-page` — full-word, precise, honest. No ambiguity about what each button does.
- **Nesting depth:** max 2 (`nav > div > a`). Early-return pattern not applicable (no control flow).
- **Hidden dependencies / side effects:** PostHog handler is wrapped in `try/catch{}` so a missing `window.posthog` won't break navigation. Existing `outbound_click` handler (already in every page) double-fires on the 2 outbound buttons by design (brief explicitly requests this).
- **Duplication:** CSS block + JS handler are duplicated **7×** across files (once per page). This is knowledge-level duplication — but the synthesis project already inlines all CSS and JS per-page (no shared `.css` / `.js` file exists). Following local convention (Principle 9) was the higher-priority rule. Recommend Phil treat shared-stylesheet extraction as a separate refactor across all 7 pages, not this change.
- **Local-style match:** Variable names (`--ring`, `--card`, etc.) inspected on all 7 pages first. CSS minification style (single-line declarations, no extra whitespace) matches the existing inline stylesheets. PostHog handler uses the existing `try{...}catch(e){}` pattern visible in every other handler in the file.
- **Honest signatures:** No new functions introduced. PostHog `.capture` call passes only flat-string properties (`direction`, `target_page`, `page`) — no nested objects, no async.
- **Things I chose NOT to add (YAGNI):**
  - No `<button>` element wrapper or any `role="button"` — `<a href>` is correct for cross-page nav
  - No prefetch hints (`<link rel="prefetch">`) — premature optimization
  - No keyboard shortcut handler (e.g. ← / → arrow keys) — the brief said keyboard-navigable, not keyboard-shortcut. Standard tab order suffices
  - No reduced-motion variant on `.btn` transitions — inherited from existing `--transition` token (already 150ms, well below the 200ms motion-sickness threshold)
  - No icon SVGs — captured pattern uses HTML entities (`&rarr;`, `&larr;`, `&nearr;`); SVG would be a different visual register
  - No `.btn-pagination` modifier class — `.cta-bar` styling fits as-is
- **Uncertainty / assumptions a human should verify:**
  1. **Mobile preview at 375px not run** — code-reviewed only. Open the preview at 375px and confirm stacked buttons + ≥44px tap targets.
  2. **PostHog event name `pagination_click`** is new for this site. Confirm in the PostHog UI it isn't already used for something unrelated. If naming collision, rename across all 7 files in one pass.
  3. **DOM order deviation from reskilling** is intentional (back-left, forward-right per Phil's Step 2 table). If you later decide to backport this block to reskilling/disruptions/etc., you'll need to choose: keep their forward-first DOM order, or switch them to match synthesis.
  4. **The outbound double-fire (pagination_click + outbound_click)** is per spec. If the PostHog dashboard ever shows event-count inflation, this is the reason.
