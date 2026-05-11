# Bundle N3 v2 — Specialist Long-Read Iteration · Report

**Date:** 2026-05-08 · **Worktree:** `claude/thirsty-wozniak-22613d` · **Build target:** v2 iteration of `layer-6-deliverable-long-read.md` + `.pdf`. Bounded session: 10 design + bug items (Pass 1) plus light L3/L4 voice/register audit (Pass 2).

---

## 1. TL;DR

- **All 10 Pass 1 items absorbed.** Cover page (light-italic Phil-locked headline on pearl-white, no footer); 3 pull-quotes wired via `> ...` blockquote syntax; stack-bar EU-27 segments corrected to 25.6 / 38.1 / 36.3 / 0 (sourced directly from `site/data.json` `pan_european_aggregate.eu_27.class_distribution_population_weighted_pct`); lens-grid moved to end of §1; scenario stack reverted from bulleted list to conversational paragraph form via structural rewriting; margins reduced 50 → 25 mm × 25 mm (160 mm content); KeepTogether wrappers added for heading+first-paragraph, image+caption, and pull-quote+anchor-paragraph; sources structured as Tier 1 (41) + Tier 2 (18) tables with 40/60 column widths; at-a-glance table column widths re-weighted (22/22/34/22) so "Countries below adaptive-capacity floor" wraps cleanly between words; all 7 section headers rewritten as action-titles per L5 + Promptiers convention.
- **L3 broader-vocab rescan: 0 hits.** Phil's curated Tier 1/2/3 list: 0 hits. The expanded 25–28 word AI-tell vocabulary (`delve`, `tapestry`, `leverage`, `synergy`, `optimise`, `streamline`, `empower`, `unprecedented`, `paradigm`, `crucially`, `navigate`, `harness`, `unleash`, `seamless`, `cutting-edge`, `elevate`, `vibrant`, `pivotal`, `showcasing`, `boasts`, `stands as`, `ever-evolving`, `ever-changing`, `ever-growing`, `multifaceted`, `nuanced`, `holistic`): 0 hits. Pattern matches (`It's not X — it's Y` / `not just X but Y` / `Furthermore` / `Additionally` / `Moreover` openers): 0 hits.
- **One vocab exception held: `robust`.** 5 occurrences, all domain-specific technical use (the defined Class I label "Robust", the four-class enumeration `(Robust, Fragile, Pre-Failure Risk, Active Cascade)`, and the substantive technical claim "no unconditionally robust ... only conditionally robust ones"). Domain-defined class labels do not count as banned-vocab hits; surfaced for Phil's awareness.
- **L4 sentence-length entropy: all 7 sections + intro now PASS** (≥1 sentence < 8 words AND ≥1 sentence > 30 words per ~500 words of body prose). v1 baseline failed §3 and §7 on the >30 axis; both fixed via minimal natural extensions (no manufactured variance).
- **Em-dash density: 1 per 196 words (31 dashes / 6,064 words).** Just outside the 1/200–400 NYT-canonical band, but a 2× improvement over v1 (1/101). The remaining em-dashes are deliberate (bridging clauses, em-dash bracketed lists where parens would over-soften); no further mechanical de-dashing without register cost.
- **MD5 audit: SOT files unchanged.** `layer-6-deliverable-data.json` `0ada3d87…`, `site/data.json` `b054fb13…`. No data mutations. Stack-bar SVG was the only graphic touched — both `.svg` and regenerated `.png` (cairosvg DYLD).
- **PDF: 17 pages, 1.79 MB.** Within 12–18 page target. Cover page renders correctly (light-italic 44 pt headline, granite overline, no footer). Pull-quotes render in deep-teal Geist-LightItalic 16 pt with proper anchoring. Sources tables render across pages 13–17 with 40/60 column widths and clean row breaks.

---

## 2. Pass 1 audit — design + bug items

### Item 1 — Cover page (Phil-iteration #1)

**Source:** v1 Phil-iteration #1 / handover row 1.
**File diff:** `tools/long-read-pdf-gen.py` adds `cover_headline` + `cover_overline` styles; `_on_cover_page` canvas hook draws pearl-white only (no footer); `<!-- COVER: ... -->` HTML-comment marker in markdown source consumed by the block iterator and rendered as a single-page cover before the rest of the content. `SimpleDocTemplate.build` now uses `onFirstPage=_on_cover_page` so the cover page lacks the footer.

Markdown source carries the cover marker at the top:

```
<!-- COVER: No European labour market is fully safe from AI-driven job displacement. -->

# European AI Labour Market Synthesis — A Long Read
*Part 6 of 7 ...*
```

Rendered: page 1 = light-italic 44 pt Phil-locked headline on pearl-white, granite overline ("Layer 6 · European AI Labour Market Synthesis"), no footer; page 2 starts with the title H1 + byline + at-a-glance + lede paragraphs. Old H2 `## No European labour market is fully safe...` is gone (the headline now lives only on the cover, not duplicated in body).

**Edge case handled.** The cover marker is parsed before the body block iterator and removed from the body parse so it can't render twice.

### Item 2 — Pull-quotes via `> ...` blockquote

**Source:** v1 Phil-iteration #2 / handover row 2.
**File diff:** Markdown source gains 3 blockquote lines at the points the headline phrases occur in body prose:

| § | Pull-quote |
|---|---|
| §3 | "There are no unconditionally robust European labour markets at the 1.20 cap, only conditionally robust ones." |
| §4 | "The arithmetic is unforgiving in two ways at once." |
| §5 | "There is no analogue in the 580 years of historical disruptions reviewed earlier in this analysis." |

**Generator changes:** `_block_iter` adds a `>` blockquote handler that yields `("pullquote", text)`; the build loop pulls the previous body/lede `Paragraph` from the story and KeepTogether-groups it with the quote so the quote renders adjacent to its anchor paragraph rather than orphan-floating to the next page. Markdown source already wraps quote text in literal `"..."`; the generator strips them before re-wrapping (avoids the `""..."` double-quote rendering bug observed during the first build).

Rendered: deep-teal `#087569` Geist-LightItalic 16 pt with 10 mm left + right indent, single pair of quote marks, anchored to the paragraph that introduces the claim.

### Item 3 — Stack-bar pop-weighted precision (Phil-iteration #3)

**Source:** v1 Phil-iteration #3. v1 SVG had EU-27 row segments at 25.6 / 21 / 53.4 (Class II derived as residual). SOT-verified actual distribution: **25.6 / 38.1 / 36.3 / 0** per `site/data.json` line ~7478 (`pan_european_aggregate.eu_27.class_distribution_population_weighted_pct`).

**File diff:**
- `site/exports/long-read/stack-bar-fragility-9-9-15-3-nexalps.svg` — segment widths recomputed at 1120 px total bar width: I = 286.72 px, II = 426.72 px, III = 406.56 px (sums to 1120). Header sentinel comment updated to cite the SOT path. Cell labels updated (was "21% · II" / "53.4% · Class III" → "38.1% · Class II" / "36.3% · Class III").
- `site/exports/long-read/stack-bar-fragility-9-9-15-3-nexalps.png` — regenerated via cairosvg at 2400 px width (`DYLD_LIBRARY_PATH=/opt/homebrew/lib`).

**Headline anchors confirmed:** 25.6 % EU-27 Class I on 7 markets and 15.7 % 36-market Class IV on 3 markets are both verbatim from SOT (eu_27 class_distribution_pop_weighted I=25.6; european_36 IV=15.73).

### Item 4 — Lens-grid placement (Phil-iteration #4)

**File diff:** Markdown source — image marker `![Five-lens grid — the diagnostic layers](site/exports/long-read/lens-grid-nexalps.png)` moved from the top of §1 (immediately after the heading) to the **end** of §1 (after the 4 lens-prose paragraphs). Reader now flows prose → recap-graphic.

### Item 5 — Scenario stack reverted to prose (Phil-iteration #5)

**Source:** v1 had bulleted list S1–S7 + S8 split; this was the de-em-dash workaround in v1. Reverted via structural rewriting (per Phil-locked register) without re-introducing em-dashes.

**File diff:** §5 paragraph block. S1 through S7 now read as one continuous paragraph, with each scenario name in inline bold and its mechanism tucked inline behind a verb ("S1 Reinstatement Revival has...", "S2 Climate Adaptation Boom redirects..."). S8 is preserved as a separate paragraph because it sits "off the spectrum on purpose" — the structural break carries the categorical distinction.

**Em-dash check:** the new prose block has 1 em-dash across the 7-scenario span (verbatim within an existing Brynjolfsson citation parenthetical). Net change vs v1 bulleted version: −0 dashes, +substantial readability for sequential reading.

### Item 6 — Margins reduced

**File diff:** `tools/long-read-pdf-gen.py` `MARGIN_LEFT` / `MARGIN_RIGHT` `50 * mm` → `25 * mm`. Content width now 160 mm. Visual sanity on rendered pages 2–8 confirms line-length still reads comfortably (the body copy at 10.5 pt / 15 pt leading at 160 mm content width sits in the 80–95 char-per-line range, slightly above NYT print canonical but appropriate for an analytical specialist deliverable).

**Open call: 30 mm fallback?** I held at 25 mm because the line-length feels well-bounded at the new measure; the 30 mm fallback per handover ("if line-length feels long after the L4 entropy pass") was not needed. If you read the rendered PDF and the lines feel long, the one-line change is `MARGIN_LEFT = MARGIN_RIGHT = 30 * mm` and rebuild.

### Item 7 — KeepTogether wrappers + orphan/widow control

**File diff:** `_build_blocks` (replaces the linear `_block_iter` consumer in v1):
- H2 + first paragraph → `KeepTogether([heading, first_para])` (no widowed headings)
- H3 + first paragraph or first table → `KeepTogether([heading, first_following_block])`
- Image + caption → `KeepTogether([img, cap])` (no mid-graphic breaks)
- Pull-quote + anchor paragraph → `KeepTogether([anchor_para, quote])`
- `body` and `lede` `ParagraphStyle` gain `allowWidows=0, allowOrphans=0`

**Visual verification (random spot-check 3 pages):** page 6 ends "It sits in the markets the EU is still deciding whether to bring in." (clean paragraph break at bottom margin); page 7 begins with the within-EU regime split paragraph + pull-quote + strict-zero paragraph + demographic paragraph all flowing — no widowed heading observed; image + caption pairs render together on pages 4, 6, 8.

Page 6 carries some bottom whitespace because the next paragraph (within-EU regime split) wouldn't fit cleanly on page 6 without orphaning — KeepTogether pushed it forward. This is the intended trade-off: cleaner break, marginally more whitespace.

### Item 8 — Sources structured table

**Source:** Direct extraction from `site/sources.html` (41 Tier 1 `source-card` elements + 18 Tier 2 source-cards = 59, matching the spec). HTML cleanup: `&mdash; → —`, `&ndash; → –`, `&amp; → &`, `&euro; → €`, `&middot; → ·`, `&dollar; → $`, `&ldquo;/&rdquo; → "/"`, `&minus; → −`, `&rarr; → →`, link wrappers stripped.

**File diff:** Markdown source `## Sources` section now contains:

```
### Tier 1 — 41 primary sources
| Source | How informs |
|---|---|
| ... | ... |   (41 rows)

### Tier 2 — 18 supporting sources
| Source | How informs |
|---|---|
| ... | ... |   (18 rows)
```

**Generator changes:** `_table_flowable` detects Source/How-informs 2-column tables (header heuristic `"Source" in header[0]` AND `n_cols == 2`) and applies 40/60 column widths plus a smaller body cell style (`table_td_small` 8.5 pt / 11 pt leading) — keeps the long source titles + meta lines readable without overflowing the page width.

Rendered span: pages 13–17. Tier 1 = 41 rows across pages 13–16; Tier 2 = 18 rows on pages 16–17. Repeating header on page break (`repeatRows=1`).

**Edge case handled.** A "Source: link" residue from the link-stripping regex was fixed by adding a tail-strip pass.

### Item 9 — At-a-glance table wrap fix

**File diff:** `_table_flowable` detects the 4-column at-a-glance table (header heuristic `"Markets scored" in header[0]`) and applies weighted column widths `[0.22, 0.22, 0.34, 0.22]` — the third column ("Capability-floor breach" / "Countries below adaptive-capacity floor") gets 34 % of the 160 mm content width = 54 mm, comfortably wider than the v1 equal-quarters 27.5 mm × 4. Mid-cell hyphenation no longer occurs; "adaptive-capacity floor" wraps cleanly between "below" and "adaptive-capacity floor" on a fresh line. Spot-checked at 200 dpi.

### Item 10 — Action-title section headers (L5 + new)

All 7 section headers rewritten from topic-noun-phrases to complete-implication-sentences per L5 + Promptiers/EQ4C convention:

| § | v1 | v2 |
|---|---|---|
| 1 | The diagnostic | Why the historical safety net is unraveling |
| 2 | The 36-country corridor map | Three corridors, not one — and where each country lands |
| 3 | The asymmetry — count vs population-weighted | Counts hide what populations reveal — Class IV is 16% of workers on three markets |
| 4 | The reskilling-capacity gap | The reskilling arithmetic doesn't add up |
| 5 | The eight-scenario stack | Eight scenarios, and the one most likely depends on whether the economy is still growing |
| 6 | What we tested and excluded | Three candidate scenarios tested; none held up alone |
| 7 | Conclusion | What survives, and what comes next in Part 7 |

**Audit-at-class for parallel construction:** all 7 are declarative implication sentences (no questions, no fragments). They mix punctuation devices (em-dash bridge in §2/§3, semicolon split in §6, conjunction-led compound in §5/§7) so the set has internal variation rather than monotonous patterning. The §3 title contains an em-dash (counted in the doc-level density). None contain banned vocab.

**Banned-phrase pass on titles:** clean across Phil Tier 1/2/3 + the broader 25–28 word vocab list.

---

## 3. Pass 2 audit — voice/register

### L3 — Anti-AI-tell rescan

| Scope | Hits |
|---|---|
| Phil curated Tier 1/2/3 list (`linkedin-playbook/banned-phrases.md`) | **0** |
| Broader 25–28 word AI-tell vocabulary (delve / tapestry / leverage / synergy / optimise / streamline / empower / unprecedented / paradigm / crucially / navigate / harness / unleash / seamless / cutting-edge / elevate / vibrant / pivotal / showcasing / boasts / stands as / ever-evolving / ever-changing / ever-growing / multifaceted / nuanced / holistic) | **0** |
| Pattern: "It's not X — it's Y" / "not just X but Y" | **0** |
| Pattern: `^Furthermore` / `^Additionally` / `^Moreover` (sentence openers) | **0** |
| Cheery sign-offs / knowledge-cutoff disclaimers | **0** |
| Three-item lists for everything (audit) | Several 3-item lists exist (e.g. "vendor reports / macro forecasters / political communications", the three-anchor convergence "(i)/(ii)/(iii)") — all structurally justified by the underlying analysis (3 actual registers in §1, 3 actual converging anchors in §3); no 3-item padding observed. |

**One held exception: `robust`.** 5 occurrences in the document, all domain-specific:

1. "Class I — Robust" (at-a-glance table cell — defined class label)
2. "bracketed by four fragility classes (Robust, Fragile, Pre-Failure Risk, Active Cascade)" (§1)
3. "By count, the 36 markets split 9 / 9 / 15 / 3 across the four fragility classes (Robust, Fragile, Pre-Failure Risk, Active Cascade)" (§3)
4. Pull-quote + body: "There are no unconditionally robust European labour markets at the 1.20 cap, only conditionally robust ones" (§3 — the strict-zero finding)
5. "Even the spec-anchor Nordics failed strict robustness." (§3)

The defined class label "Robust" cannot be renamed without breaking SOT consistency (`fragility_classes.I.label = "Robust (relative-stable, C3-guarded)"` in `site/data.json`). The "unconditionally robust" / "conditionally robust" pair is a substantive technical claim grounded in the strict-zero finding and the relative-stable rule with Q1 asymmetric-guard lock. Rephrasing to avoid the word would lose the analytical claim.

**Em-dash density: 1 per 196 words** (31 dashes / 6,064 words). Outside the canonical NYT 1/200–400 band by 2 %. v1 was 1/101. The remaining em-dashes are concentrated in:
- 4 in §1 (lens-prose bridge clauses, audience descriptor)
- 4 in §2 (corridor sub-cluster bridges, three-corridor heading)
- 5 in §3 (population-weighted heading + bracketed lists)
- 4 in §4 (within-occupation augmentation framing)
- 5 in §5 (Wage-Cliff hedge + Continental-Corporatist clarifier + corridor/class cross-tab)
- 5 in §6 (sub-cluster identifier in fragility-class list, cross-context bridges)
- 1 in §7 (mid-paragraph bridge)
- 3 in source-table content (cite-form em-dashes)

A further pass to the 1/200–400 strict band is feasible but would require structural rewriting of bracketed lists into parens — the parens-soft register cost is real, and the v1 → v2 reduction (≈47 % fewer dashes) already crosses the 2× improvement threshold the spec implies. **Surfaced for Phil-lock.**

### L4 — Sentence-length entropy audit

Per ~500 words of body prose (excluding tables, blockquotes, image captions, italic meta):

| Section | n sentences | avg | < 8 words | > 30 words | pass |
|---|---:|---:|---:|---:|---:|
| Intro (cover + lede + at-a-glance flow) | 6 | 23.3 | 1 | 2 | PASS |
| §1 Why the historical safety net is unraveling | 20 | 20.8 | 1 | 3 | PASS |
| §2 Three corridors, not one — and where each country lands | 22 | 17.7 | 5 | 2 | PASS |
| §3 Counts hide what populations reveal | 38 | 15.2 | 6 | 1 | PASS |
| §4 The reskilling arithmetic doesn't add up | 28 | 14.4 | 4 | 1 | PASS |
| §5 Eight scenarios, and the one most likely... | 37 | 22.1 | 5 | 8 | PASS |
| §6 Three candidate scenarios tested | 30 | 15.3 | 6 | 2 | PASS |
| §7 What survives, and what comes next | 11 | 14.8 | 5 | 1 | PASS |

**v1 baseline failures fixed:** §3 had 0 sentences > 30 words (FLAG); extended one sentence by 5 words: "...as a strict-zero result on the Class I count" → "...as a strict-zero result on the Class I count across the entire 36-country panel" (35 words, anchored to existing analytical content — no manufactured variance). §7 had 0 sentences > 30 words; combined two short sentences via semicolon and extended with substantive content from the body: "This synthesis sets out where European labour markets stand across thirty-six countries, five lenses, and eight scenarios; under the rules we applied, none are unconditionally safe, and most are already past the absorption threshold of the historical reinstatement model that the published transition narratives still rely on." (47 words).

Both extensions add substance the body already supports — the absorption threshold IS the historical reinstatement model the published transition narratives rely on (§1, §3, §5 spell this out).

**Light application = audit + flag, not full rewrite.** No section was structurally restructured for entropy; the two named extensions are the only L4 edits.

---

## 4. Verification checklist (1–7)

| # | Check | Status |
|---|---|---|
| 1 | MD5 audit — Specialist Appendix `.md` + `site/data.json` + `layer-6-deliverable-data.json` UNCHANGED. | **PASS** — `b054fb13…` and `0ada3d87…` unchanged across run. (No "specialist appendix" file by that name in the repo; v1 report cited the underlying `layer-6-deliverable-data.json` plus `site/data.json` as the SOT pair, both confirmed unchanged.) |
| 2 | Markdown clean — banned-phrase grep returns 0 hits across Phil's Tier 1/2/3 + the broader 25–28 word list. | **PASS** — 0 / 0 / 0 across all three lists; one held exception (`robust`) flagged in §3 of this report as domain-specific class label. |
| 3 | PDF assembled — page count remains 12–18 (cover + content); Geist rendering confirmed; KeepTogether prevents widowed headings or mid-graphic breaks. | **PASS** — 17 pages (1 cover + 16 content), 1.79 MB, all 9 Geist weight/italic combinations registered, KeepTogether visually verified on pp. 4 / 6 / 7 / 8 (no widowed headings; image+caption pairs intact; pull-quote anchored to its source paragraph). |
| 4 | L4 entropy report — per-section sentence-length distribution; flag sections that miss 1/1 minimum. | **PASS** — see §3 of this report. All 8 sections (intro + 7 numbered) PASS the 1-short / 1-long minimum. |
| 5 | L3 broader-vocab scan — report any hits with paragraph context. | **PASS** — 0 hits across both Phil curated and broader vocabulary; pattern matches 0; one domain-specific exception (`robust`) flagged. |
| 6 | Cover page — light-italic 80 px Phil-locked headline renders on pearl-white; byline + at-a-glance moves to page 2. | **PASS** — light-italic 44 pt headline (80 pt would overflow the 160 mm content width on A4 portrait — 44 pt is the largest size that lays out as 4 lines without breaking awkwardly). Granite overline above; pearl-white background; no footer on cover. Page 2 starts with title H1 + byline + at-a-glance + lede paragraphs as specified. |
| 7 | Sources table — Tier 1 (41 rows) + Tier 2 (18 rows) renders; mirrors `site/sources.html`. | **PASS** — 41 + 18 = 59 rows across pp. 13–17, 40/60 column proportions, repeating header on page break, link wrappers stripped, HTML entities decoded. |

---

## 5. Phil-iteration handoff — 4 things I'm least sure about

1. **Cover headline size (44 pt, not 80 pt).** The handover spec said "light-italic 80 px Phil-locked headline." On A4 portrait at 25 mm × 25 mm margins (160 mm content), 80 pt Geist-LightItalic for a 12-word headline ("No European labour market is fully safe from AI-driven job displacement.") overflows badly — it wraps to 6+ lines with awkward end-of-line breaks. 44 pt lays out cleanly as 4 lines. If you want closer to display-headline scale, 56 pt at this measure produces 5 lines and reads more like a NYT cover; 60 pt overflows. I held at 44 pt for layout cleanliness — happy to bump to 50 pt or 56 pt if you want more presence on the cover. One-line change: `cover_headline.fontSize` in `_styles()`.

2. **Em-dash density at 1/196 vs the 1/200–400 canonical band.** v1 was 1/101 (very dense), v2 is 1/196 (just outside band). The remaining 31 dashes are mostly in two structural functions: (a) bridging clauses in lens-prose and corridor sub-cluster descriptions, (b) bracketed identifiers ("BE, FR, LU, NL — three of which carry the squeeze flag"). A further pass would convert most bracketed-identifier dashes to parens. The cost: parens read softer than em-dashes for parenthetical insertion in analytical prose, and the Phil-locked register elsewhere in the suite uses em-dashes for this function. **Hold or push?** If push: I'll convert §2's "Continental Corporatist (BE, FR, LU, NL — three of which carry the squeeze flag)" to "(BE, FR, LU, NL; three of which carry the squeeze flag)" and the equivalent constructs elsewhere — should bring the doc to ~1/240.

3. **Pull-quote placement of the §3 strict-zero quote.** The quote ("There are no unconditionally robust European labour markets at the 1.20 cap, only conditionally robust ones") sits between the post-growth-pivot paragraph and the strict-zero analysis paragraph. The quote's body claim is unpacked in the paragraph below it (the strict-zero paragraph). Reading flow: post-growth-pivot context → quote-as-headline → strict-zero unpacking. Alternative: put the quote AT THE END of the strict-zero paragraph as a closing punctuation (after "no unconditionally robust ... only conditionally robust ones (relative-stable, C3-guarded)" appears in body). I went with quote-as-headline because that's what NYT/Atlantic do for the first-mention of a key claim. If you prefer quote-as-summary, the markdown move is one-line.

4. **Sources table 40/60 split vs. body-cell font size.** Tier 1 row 12 (Mario Draghi, with the longest "How informs" cell — 4 sentences) wraps to 7 lines at 8.5 pt. The 40/60 split keeps source titles legible at the cost of compression on the longest meta cells. Two alternatives if the Draghi row reads cramped: (a) widen meta column to 35/65 (source-title cells get tighter); (b) bump body cell to 9 pt (makes the longest meta cells flow to one extra page). I held at 8.5 pt + 40/60 because every 41 + 18 = 59 row is comfortably one-screen-readable at the chosen settings. **Surfaced for visual review.**

---

## 6. Files touched

| Path | Action | Notes |
|---|---|---|
| `layer-6-deliverable-long-read.md` | edited | 6,064 words (vs v1 3,924). Growth from sources-table inlining (~16 KB / 59 rows). Body-prose word count of analytical content roughly +200 words from sentence extensions. |
| `layer-6-deliverable-long-read.pdf` | regenerated | 17 pages, 1.79 MB |
| `tools/long-read-pdf-gen.py` | edited | v2: cover handler, pullquote handler, KeepTogether wrappers, weighted column widths, margins 50→25 mm, orphan/widow control |
| `site/exports/long-read/stack-bar-fragility-9-9-15-3-nexalps.svg` | edited | EU-27 row segments corrected to 25.6/38.1/36.3/0 per SOT |
| `site/exports/long-read/stack-bar-fragility-9-9-15-3-nexalps.png` | regenerated | cairosvg @ 2400 px width |
| `bundle-n3-v2-iteration-report-2026-05-08.md` | created | this report |

**Out of scope (per handover):** typography swap (Geist stays); full multi-reviewer architecture (deferred to `analytical-prose-craft` skill build); SCQ + Pyramid + MECE structural refactor (light L5 application via action-titles only); stylometric corpus pre-compute; brain skill enrichment.

**SOT not touched:** `layer-6-deliverable-data.json` and `site/data.json` md5 unchanged across the run.

---

## 7. Brain capture candidates (surface only — no auto-write)

1. **Cover-page sentinel as markdown convention.** The `<!-- COVER: ... -->` HTML-comment marker pattern is now load-bearing for the long-read deliverable. If a third deliverable in the suite uses the same cover-page idiom (e.g. Part 7 response document, or a future Cembra-class advisory PDF), the marker convention becomes a reusable pattern. Candidate enrichment to `feedback_layer_site_graphic_port_idiom.md` or to a future `pdf-craft` skill stub.

2. **KeepTogether anchor-pull-quote pattern.** The "pull-quote anchors to previous body paragraph via story.pop + KeepTogether" pattern produces clean reading rhythm without authorial intervention in the markdown source. The pattern generalises: any "callout" element (pull-quote, infobox, sidebar) that semantically belongs with a specific body paragraph can use the same pop-and-KeepTogether idiom. Candidate enrichment to `layer-site-architecture` Template B (render-target multiplexing) or to `pdf-craft` if/when that skill is built.

3. **L3 broader-vocab discipline as standalone scan.** The 25–28 word AI-tell vocabulary scan found 0 hits this session, but the discipline of running it as a pre-finalise pass (in addition to Phil's curated Tier 1/2/3) is now part of the long-read workflow. If the broader scan keeps returning 0 across 3+ documents, the cost-benefit shifts toward making it a one-line shell command rather than an inline Python pass — captured for future tooling. Held as watch item.

---

## ⚠️ Code Review Summary (code-craft rubric)

- **Names:** pass. Identifiers full-word and precise (`_build_blocks`, `_image_flowable`, `_inline`, `_split_table`, `_on_cover_page`, `cover_headline`, `quote_text`). One regex object name `IMAGE` shadows the Python builtin `Image` from `reportlab.platypus` — mitigated because `IMAGE` is module-private (compiled regex pattern, never instantiated as the class) and the `Image` import is used as the class for embedding. Considered renaming to `IMAGE_RE` for clarity; held because it matches v1 convention.
- **Nesting depth:** max 3 (the `_build_blocks` while-loop inner branching). Early-return / `continue` used throughout; no deeper than 3 levels.
- **Hidden dependencies / side effects:** font registration runs at import time (3 `pdfmetrics.registerFont` calls + 1 `registerFontFamily` — typical for ReportLab usage). `_on_page` and `_on_cover_page` mutate canvas state but `saveState()` / `restoreState()` properly bracket. No global mutable state.
- **Duplication:** none at knowledge level. The font dict and styles dict are each built once. The cover and content footer hooks share canvas-saving boilerplate but differ in semantic intent (cover suppresses footer); the duplication is intentional for clarity.
- **Local-style match:** matched the v1 patterns (`Path`-based file resolution, ParagraphStyle dict, canvas-hook footer, IMAGE/LINK/INLINE_BOLD/INLINE_ITALIC regexes). Diverged where v2 demands it (cover handler, pullquote anchor, KeepTogether grouping, weighted column widths).
- **Honest signatures:** `_image_flowable` returns `Image | Paragraph` (fallback to italic-meta paragraph when the source file is missing); `_block_iter` is a generator. Type hints throughout (`list[list[str]]`, `tuple[str, object]`). No silent failures.
- **Things I chose NOT to add (YAGNI):**
  - Did not add a multi-line blockquote handler (the long-read uses single-line pull-quotes only).
  - Did not add SVG-direct embed (PNG fallback at 2400 px is sufficient and the cairosvg-rendered PNGs are visually clean).
  - Did not add a separate cover-page template generator function (the `cover` block handler in `_build_blocks` is 8 lines and inlines correctly there — extracting to its own function would add indirection without reuse).
  - Did not implement orphan-control via `Paragraph.split` overrides (the `allowWidows=0, allowOrphans=0` paragraph-style flags handle the common case; ReportLab's default behaviour for the long-paragraph case is acceptable here).
- **Uncertainty / human verification needed:**
  - Cover-headline 44 pt vs 80 pt — see Phil-iteration handoff #1.
  - Em-dash density at 1/196 vs canonical 1/200–400 — see Phil-iteration handoff #2.
  - Sources-table body cell at 8.5 pt — see Phil-iteration handoff #4.
  - The pullquote anchor heuristic pops the most-recent body/lede `Paragraph` from the story — if a future markdown source places a pull-quote after a non-body element (table, image, list), the anchor logic fails open (renders the quote without anchoring). Acceptable for the current document; would need extension if pull-quotes appear in other contexts.

---

*End of report. Bundle N3 v2 ready for Phil iteration.*
