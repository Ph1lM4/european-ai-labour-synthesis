# Bundle N3 — Specialist Long-Read · Report

**Date:** 2026-05-08 · **Worktree:** `claude/romantic-rubin-128691` · **Build target:** Long-read derivative of post-Phase-2K Specialist Appendix.

---

## 1. TL;DR

- **Three phases delivered, all verification gates pass.** Markdown long-read at 3,728 words (target 3,500–5,000); 4 Nexalps graphics rendered (corridor-map copied; stack-bar, reskilling-funnel, lens-grid new); A4 PDF assembled at 14 pages, 1.69 MB (target 12–18).
- **Banned-phrase scan returns zero hits.** Tier 1, 2, and 3 patterns all clean against `skills/linkedin-playbook/references/banned-phrases.md`.
- **Em-dash density compliant.** No paragraph exceeds 3 em-dashes after structural rewrites of three offending sections (anchor list converted to numbered inline, scenario list converted to bullet list, parenthetical fence dropped on AT/LU/TR sentence).
- **MD5 audit:** Specialist Appendix `.md` and both data JSONs unchanged. No SOT mutation.
- **Style locks held.** Long-read PDF in Nexalps (pearl-white background, Geist 300/400/500/600/700, deep-teal-text accent #087569, granite-gray secondary). Markdown source register matches the rest-of-suite Phil-locked voice.
- **PDF generator** at `tools/long-read-pdf-gen.py` extends the `projects/job-scout-agent/generate_pdf_generic.py` pattern: same Geist family registration, same Platypus story-based composition, page-background canvas hook draws pearl-white, custom markdown-to-flowable parser tuned to this single document.
- **Five Phil-iteration items flagged below** — register tone in Section 4 stretch paragraph, lens-grid placement decision, pull-quote presence vs. absence, scenario-stack list-vs-prose tradeoff, pop-weighted bar precision.

---

## 2. Phase 1 audit — markdown long-read

**File:** [`layer-6-deliverable-long-read.md`](layer-6-deliverable-long-read.md) · **Words:** 3,728 · **Sections:** 7 (numbered) plus hero + at-a-glance + sources.

### Section-by-section

| § | Title | Words (approx.) | Phil-locked anchors lifted verbatim |
|---|---|---|---|
| Hero | "No European labour market is fully safe…" | ~150 | Hero H1 + lede + byline (verbatim from `site/index.html` lines 195–198) |
| At a glance | 4-card stats | ~30 | 36 / 9 / 12 / 15 yrs (verbatim from `site/index.html` lines 202–223) |
| §1 | The diagnostic | ~590 | "Five lenses, chosen because earlier parts of the project had already gathered the evidence" (methodology SM 1) |
| §2 | The 36-country corridor map | ~430 | Italy block verbatim from `site/findings.html` lines 508–510 (working-age trajectory, retirement offset 25.3%, net migration −485,823) |
| §3 | The asymmetry — count vs population-weighted | ~600 | Europe Minto blocks 1–3 from `site/europe.html` ("There is no single European corridor → variation is the answer", "The cascade pressure sits at the EU's borders, not within them", "For nearly 40% of EU-27 workers, the optimism path runs through climate, not tech") |
| §4 | The reskilling-capacity gap | ~440 | 7.55 M / 3.34 M / 2.89 M / 450 K / 15-year backlog / 1–3 year disruption / 5–9 year response (verbatim numerics from Specialist Appendix §5.3 and `site/findings.html` §5 funnel) |
| §5 | The eight-scenario stack | ~720 | S1–S8 spectrum names + S8 prominence ("S8 sits outside the spectrum on purpose", "no analogue in the 580 years of historical disruptions"); P(S2 \| post-growth) = 0.30; modal-finding sentence; AT/LU/TR S2-dependent block |
| §6 | What we tested and excluded | ~445 | Methodology SM 4 verbatim — Industrial Accelerator Act, wealth-fund-rich regime test, startup-driven absorption (from `site/methodology.html` lines 215–218) |
| §7 | Conclusion | ~205 | Phil-locked Layer 7 closer verbatim from `site/findings.html` lines 516–518 |
| Sources | Tier 1 + Tier 2 anchors list | ~140 | From Specialist Appendix §9 + `site/sources.html` |

### Banned-phrase scan

```
Tier 1: 0 hits  (heavy lifting / real work / real X / sink in / interesting / most miss / hot take / game-changer)
Tier 2: 0 hits  (it's not X it's Y / dressed as / quiet part / paradigm-shift / quietly / new oil / holding mirror / voices like yours / bright humans)
Tier 3: 0 hits  (fragment-then-colon openers, "load-bearing", "structurally", "the analysis is built to surface")
Em-dash density: max 3 per paragraph (compliant)
```

The em-dash audit caught three early offenders. Each was structurally rewritten rather than mechanically de-dashed:
1. Three-anchor list in §3 (Phase 1 sub-cluster boundaries / Autor 2024 / El-Sahli & Upward) converted from "Anchor — description" repetition to numbered inline `(i) (ii) (iii)`.
2. Seven-scenario sequence in §5 converted from inline em-dash list to bulleted list — also clearer on the page.
3. AT / LU / Turkey parenthetical fence in §5 changed from `— —` to `(...)`.

### Two corrections caught during composition

- **Lens 4 / Lens 5 ordering.** First draft listed lenses as "displacement velocity, demographic buffer, distributional fold, polycrisis drag, jurisdictional buffering" — that swaps L4 and L5 against the Specialist Appendix §2 spec (L4 = jurisdictional buffering, L5 = polycrisis drag). Fixed before the PDF render.
- **Lens-grid graphic placement.** First draft put the lens grid in §6 ("What we tested and excluded") because the visual is "five-lens." Moved to §1 (the diagnostic) where the lenses are introduced — semantically correct placement.

---

## 3. Phase 2 audit — Nexalps graphics

**Output directory:** `site/exports/long-read/` · **4 SVG + 4 PNG** (PNG fallback at 2400 px wide, rendered via cairosvg with `DYLD_LIBRARY_PATH` set to the homebrew cairo lib).

| Graphic | SVG | PNG | Palette | Two-layer port |
|---|---|---|---|---|
| `corridor-map-nexalps.svg` (copied from Phase 2J) | 247 KB | 1349 KB | pearl-white bg, Mercator dot-encoding | already nexalps-styled, copy-only |
| `stack-bar-fragility-9-9-15-3-nexalps.svg` | 4.0 KB | 101 KB | bg `#F8F9FA`, segments `#087569`/`#F59E0B`/`#C41E3A`/`#4A5568` | chart-box ported (pearl-white container, Geist labels); internals = two stacked bars (count 9/9/15/3 + EU-27 population-weighted 25.6/21/53.4) for the asymmetry story |
| `reskilling-funnel-nexalps.svg` | 3.4 KB | 111 KB | bg `#F8F9FA`, monochrome greys `#4A5568`/`#718096`/`#A0AEC0`, deep-teal accent `#087569` on net-new | chart-box ported; internals = 4 proportional bars (7.55 M / 3.34 M / 2.89 M / 450 K) plus 15-year-backlog callout |
| `lens-grid-nexalps.svg` | 5.9 KB | 200 KB | bg `#F8F9FA`, white cards with deep-teal `#087569` left border | new layout, 5 cards + synthesis box (chart-box container ported, internals = ReportLab-friendly card grid for static SVG embed) |

**Palette confirmation:** every SVG includes `<style>` block with explicit Nexalps tokens. `grep -l "F8F9FA"` returns all four files; spot-check confirms `#087569`, `#4A5568`, `#F59E0B`, `#C41E3A` distributed per the chart-internal tokens.

**Two-layer thinking applied** per `feedback_layer_site_graphic_port_idiom.md`. Chart-box container (pearl-white background, Geist label, overline + title) ported from Nexalps. Internals chosen per story:
- Stack-bar got two stacked rows (count + pop-weighted) because §3 of the long-read carries the asymmetry as the headline; a single-row count bar would have under-served the section.
- Funnel got the same 4-bar proportional structure as the site, with the deep-teal accent moved exclusively to the 450 K net-new bar (the bottleneck).
- Lens-grid was synthesised from scratch — there is no equivalent on the existing site.

---

## 4. Phase 3 audit — PDF assembly

**File:** [`layer-6-deliverable-long-read.pdf`](layer-6-deliverable-long-read.pdf) · **Pages:** 14 · **Size:** 1.69 MB · **Generator:** [`tools/long-read-pdf-gen.py`](tools/long-read-pdf-gen.py).

### Generator changes vs. `generate_pdf_generic.py`

| Element | Generic brief | Long-read |
|---|---|---|
| Page size | A4 | A4 |
| Margins | 25 mm × 25 mm | **50 mm × 50 mm** (110 mm content per spec) |
| Background | none (white) | **pearl-white #F8F9FA, drawn on every page via canvas hook** |
| Fonts | Geist Regular/Bold/Light/Italic/Medium/SemiBold | + **Geist-LightItalic** (pull-quote signature) + **Geist-MediumItalic** + **Geist-BoldItalic** |
| Pipeline | hard-coded story | **markdown → block iterator → Platypus story** with H1/H2/H3, p, bullet list, image, italic-meta, hr, pipe-table |
| Footer | "Executive Positioning Brief" | "Layer 6 — Long Read · Nexalps · Part 6 of 7 · Page N" |
| Color tokens | `#1a1a1a` / `#4a4a4a` / `#666666` | **`#000000` / `#087569` (deep-teal-text) / `#4A5568` (granite) / `#CBD5E0` (hairline)** |

### Style sheets

```
h1:        Geist-Medium 26 pt / 30 pt leading (slightly tighter than handover spec to fit hero on one column)
h2:        Geist-Medium 18 pt / 23 pt — section titles
h3:        Geist-Medium 14 pt / 18 pt — sub-headings (post-hero callout, in-section H3)
overline:  Geist-Bold 8 pt — small labels
lede:      Geist-Light 14 pt / 20 pt, granite — auto-applied to first paragraph after H1
body:      Geist 10.5 pt / 15 pt
bullet:    Geist 10.5 pt / 15 pt, indent 5 mm
pullquote: Geist-LightItalic 15 pt / 22 pt — registered but not currently invoked (see Phil-iteration §6)
table_th:  Geist-Bold 8 pt, granite (header)
table_td_bold: Geist-Bold 14 pt — auto-applied to numeric "at-a-glance" rows
```

### Image embedding

PNG-via-`Image` flowable rather than SVG-via-`svg2rlg` (svglib not installed; PNG fallback render is robust at 2400 px and the print-safe ratio is preserved). The generator falls back from `.svg` to `.png` automatically if a markdown reference points at `.svg`. All four graphic embeds resolved cleanly on first build.

### Font-registration confirmation

```
Geist, Geist-Bold, Geist-Italic, Geist-BoldItalic         — registered via registerFontFamily
Geist-Light, Geist-LightItalic, Geist-Medium, Geist-MediumItalic, Geist-SemiBold  — registered as standalone TTFs
```

---

## 5. Verification checklist

| # | Check | Status |
|---|---|---|
| 1 | Markdown source clean (valid markdown, banned-phrase grep returns 0, word count 3,500–5,000) | **PASS** — 3,728 words, 0 hits |
| 2 | Graphics exported (4 SVG/PNG in `site/exports/long-read/`, pearl-white bg confirmed, Nexalps palette confirmed) | **PASS** — 4/4 SVGs carry `#F8F9FA`, palette tokens verified inline |
| 3 | PDF assembled (12–18 pages, Geist rendering, image embedding, pull-quote light-italic available where applicable) | **PASS** — 14 pages, 1.69 MB; Geist family registered with all 9 weight/italic combinations; PNG embed at content-width preserves aspect |
| 4 | MD5 audit (Specialist Appendix `.md`, `site/data.json`, `layer-6-deliverable-data.json` unchanged) | **PASS** — `e99eb460…` / `b054fb13…` / `0ada3d87…` (unchanged across run) |
| 5 | Visual sanity (page 1 + corridor-map page + funnel page + methodology + conclusion render legibly) | **PASS** — page 1 thumbnail rendered via `qlmanage`; hero + at-a-glance table + lede styling all reading correctly; footer non-overlapping after one fix iteration (initial draft had "European AI Labour Market Synthesis — Long Read" colliding with center+right at 110 mm content width; shortened to "Layer 6 — Long Read") |

---

## 6. Phil-iteration handoff — five things I'm least sure about

1. **Hero H1 size (26 pt).** I deliberately ran below the 80 / 56 / 40 Nexalps desktop ladder because A4 portrait at 110 mm content width can't carry an 80 px headline without breaking awkwardly. 26 pt with a 14 pt H3 callout under it gives a cleaner first-page read at this measure. If you want the full Nexalps display feel (light-italic 80 px on a near-full-bleed first page) the generator needs a separate "cover" first-page template — call out and I'll add it.
2. **Pull-quote style is registered but never invoked.** I held back from injecting Phil-locked pull-quotes mid-text because the markdown source has no explicit pull-quote markers and adding them as authorial decisions feels like scope creep on a corpus-only composition session. Three candidate pull-quotes if you want them: "There are no unconditionally robust European labour markets at the 1.20 cap, only conditionally robust ones" (§3); "The arithmetic is unforgiving in two ways at once" (§4); "There is no analogue in the 580 years of historical disruptions reviewed earlier in this analysis" (§5). I can wire the pull-quote style in the markdown via `> ...` syntax if you confirm.
3. **Stack-bar second row precision.** The pop-weighted EU-27 segment widths (25.6 / 21 / 53.4) are an estimate composed from the Specialist Appendix §3 cross-tab and the Bundle X aggregate language. The 25.6% Class I figure is anchored. The 21% Class II figure I derived assuming Class II ≈ EU-27 minus C1 minus C3-IV and recombining; the 53.4% Class III is the residual. If the canonical SOT carries different exact splits for the EU-27 pop-weighted view, the SVG segment widths need a tweak. The headline finding (Class I = 25.6% on 7 markets, Class IV = 15.7% on 3 markets in the 36-market view) is verbatim from the existing site copy.
4. **Lens-grid placement in §1.** Originally placed in §6 because it shows "five lenses." Moved to §1 (the diagnostic) where the lenses are introduced. The risk: the grid now sits *before* the prose introduces the lenses, which can make the reader work to map the visual to the text. If the read flows better with the grid at the *end* of §1, swap order; if better as a §6 "what we measured, recap" graphic, swap back.
5. **Scenario stack as bulleted list.** In the de-em-dash pass I converted the seven-scenario inline sequence to a bulleted list. It reads cleaner on the page but breaks the prose flow of §5. Phil-locked register elsewhere prefers conversational paragraphs over lists. If the §5 scenario block should be prose (period-separated rather than bulleted), one revert.

---

## 7. Brain capture candidates (surface only — no auto-write)

1. **Two-layer chart-port idiom — n=3 confirmation.** This session ports three new chart-box containers (stack-bar, funnel, lens-grid) using the same idiom. The pattern — port the container, pick the internals to match the section's story — held cleanly across all three. Candidate: promote `feedback_layer_site_graphic_port_idiom.md` from n=2 to n=3 if you agree the lens-grid (which had no site equivalent and is synthesised) still counts as an instance of the idiom rather than a new pattern.
2. **PDF-generator skill candidate — `pdf-craft` or extension to `code-craft`.** The job-scout-agent → long-read PDF generator path now repeats: Geist registration, Platypus, page-background canvas hook, custom markdown parser tuned to one document. If a third deliverable lands on the same generator pattern (e.g. a Part 7 response document), a dedicated skill stub becomes load-bearing. Held as a watch item.
3. **Em-dash structural-rewrite as the right fix.** Three separate mechanical de-dash candidates this session (anchor list, scenario list, parenthetical fence) each resolved cleanest by rewriting structure (numbered inline, bulleted list, parentheses) rather than searching for a different em-dash-free phrasing. Pattern: when the rule fires, the fix is usually a structural change rather than a synonym swap. Possible enrichment to `linkedin-playbook/banned-phrases.md` Tier 3 row.

⚠️ **Code Review Summary (code-craft rubric)**

- **Names:** pass. Identifiers full-word and precise (`_block_iter`, `_image_flowable`, `_inline`, `_split_table`, `MARGIN_LEFT`). One regex object name `IMAGE` shadows builtin in narrow scope but is module-private and unambiguous in context.
- **Nesting depth:** max 3 (the `_block_iter` while loop with branching). Early-return / continue used throughout to flatten.
- **Hidden dependencies / side effects:** font registration runs at import time (3 `pdfmetrics.registerFont` + 1 `registerFontFamily`) — typical for ReportLab usage. `_on_page` mutates the canvas state but saves/restores. No global mutable state.
- **Duplication:** none at knowledge level. The font dict is the single source for font registration. The styles dict is built once per build call.
- **Local-style match:** matched `generate_pdf_generic.py` patterns (Path-based file resolution, Geist family registration, ParagraphStyle dict, canvas-hook footer). Diverged where the long-read demands it (markdown-to-flowable parser is new; pearl-white background hook is new).
- **Honest signatures:** `_image_flowable` returns `Image | Paragraph` (fallback to italic-meta paragraph when the source file is missing). Type hints throughout. No silent failures.
- **Things I chose NOT to add (YAGNI):**
  - Did not install svglib for SVG embed; PNG fallback is sufficient and the cairosvg-rendered PNGs are 2400 px wide.
  - Did not implement a full markdown parser (no support for nested lists, code blocks, blockquotes, footnotes); the long-read markdown is hand-controlled and uses only the subset I parse.
  - Did not implement a cover-page template (see Phil-iteration item 1) — held until Phil signals the hero needs to grow.
  - Did not register an unused `KeepTogether` flowable wrapper; the page breaks fall reasonably without it.
- **Uncertainty / human verification needed:**
  - Does the 50 mm × 50 mm margin spec actually mean total 50 mm or 50 mm-each-side? I read it as each-side (110 mm content). If that's wrong, the renders re-flow at narrower margins.
  - The `is_numeric_row` heuristic in `_table_flowable` triggers Geist-Bold 14 pt rows for the at-a-glance table. If a future markdown table uses bold-numeric formatting and *doesn't* want the bigger rendering, the heuristic needs tightening.
  - Pull-quote style is registered but never matched by the parser (no `> ...` blockquote handler currently). Trivial to add when the markdown source uses one.

---

## 8. Files touched / written

| Path | Action | Notes |
|---|---|---|
| `layer-6-deliverable-long-read.md` | created | 3,728 words |
| `layer-6-deliverable-long-read.pdf` | created | 14 pages, 1.69 MB |
| `tools/long-read-pdf-gen.py` | created | 320 lines |
| `site/exports/long-read/corridor-map-nexalps.svg` + `.png` | copied from Phase 2J | unchanged |
| `site/exports/long-read/stack-bar-fragility-9-9-15-3-nexalps.svg` + `.png` | created | 4 KB SVG / 101 KB PNG |
| `site/exports/long-read/reskilling-funnel-nexalps.svg` + `.png` | created | 3.4 KB SVG / 111 KB PNG |
| `site/exports/long-read/lens-grid-nexalps.svg` + `.png` | created | 5.9 KB SVG / 200 KB PNG |

**Out-of-scope (per handover):** no IA changes to existing site files; no SOT data changes; no re-derivation of Phase 1–3 outputs; no brain skill enrichment (capture candidates surfaced in §7); deploy v1 left for Phil after report-back.

---

*End of report. Bundle N3 ready for Phil iteration.*
