# Handover Prompt — Bundle N3 v2: Specialist Long-Read Iteration

Bounded iteration session. v1 landed clean (3,728 words / 14 pages / 4 SVG+PNG graphics / banned-phrase clean). v2 absorbs Phil-flagged design items + light application of voice/register patterns from the 2026-05-08 elite-longform-writing research. **Output:** updated `layer-6-deliverable-long-read.md` + `.pdf` + iteration report. Single render target — Nexalps style for PDF; markdown source register matches Phil-locked rest-of-suite voice. ~3–4 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** Mostly editorial + page-layout work; code-craft applies to the PDF generator changes (KeepTogether wrappers, margin defaults, action-title parser).

---

## Research scope

**Corpus-only.** All v2 changes draw from existing v1 state + post-Phase-2K SOT + Phil-locked decisions surfaced in conversation. Light application of L3/L4/L5 takeaways from `skills/layer-site-architecture/SKILL.md` v0.2.0 (sourced from `/Users/philippmaul/Documents/second-brain/sources/ai-writing/`); full operational templates deferred to a separate `analytical-prose-craft` skill build.

---

## Context

Bundle N3 v1 (2026-05-08) landed with 5 Phil-iteration items + 3 net-new design observations + 1 small bug. v2 absorbs all of them in one iteration round plus light application of 3 voice/register patterns (anti-AI-tell rescan, sentence-length entropy, action-title rewrite). NYT-style typography research returned: no off-the-shelf solution exists; **typography stays Geist (research is about voice, not type)**; voice patterns apply lightly here, full skill build deferred post-deploy.

---

## START PROMPT

Iterate the long-read markdown + Nexalps PDF in two passes: (1) absorb the 10 design + bug items per the table below; (2) apply L3/L4/L5 light voice/register pass.

### Read FIRST (absolute paths)

**v1 state:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-long-read.md` — current markdown (3,728 words)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-long-read.pdf` — current PDF (14 pages, 1.69 MB)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/tools/long-read-pdf-gen.py` — generator (320 lines)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-n3-specialist-long-read-report-2026-05-08.md` — v1 report incl. Phil-iteration handoff section

**Voice/register research (light application, source for L3/L4/L5):**
- `/Users/philippmaul/Documents/second-brain/sources/ai-writing/The longform-AI tooling gap and how to fill it_claude.md` — synthesis of 4-document research sweep
- `/Users/philippmaul/Documents/second-brain/.claude/worktrees/xenodochial-shirley-728acf/skills/layer-site-architecture/SKILL.md` — L1–L5 takeaways (only L3 / L4 / L5 light application in scope here)
- `/Users/philippmaul/Documents/second-brain/.claude/worktrees/xenodochial-shirley-728acf/skills/linkedin-playbook/references/banned-phrases.md` — Phil's curated Tier 1/2/3 list

**Nexalps style reference (unchanged):**
- `/Users/philippmaul/Documents/Other/My projects/Nexalps/nexalps-website/tailwind.config.ts`

### Pass 1 — Design + bug items (10 items, Phil-locked)

| # | Item | Source | Surface |
|---|---|---|---|
| 1 | **Cover page** — light-italic Phil-locked headline ("No European labour market is fully safe from AI-driven job displacement") on pearl-white, content starts page 2 | v1 Phil-iteration #1 | `tools/long-read-pdf-gen.py` (cover-page template) |
| 2 | **Pull-quotes invocation** — slot 3 candidates from v1 report into markdown source via `> ...` blockquote syntax: §3 "There are no unconditionally robust European labour markets at the 1.20 cap, only conditionally robust ones"; §4 "The arithmetic is unforgiving in two ways at once"; §5 "There is no analogue in the 580 years of historical disruptions reviewed earlier in this analysis" | v1 Phil-iteration #2 | Markdown source + generator (pull-quote style is registered, needs `> ...` parser handler) |
| 3 | **Stack-bar pop-weighted precision** — verify Class II = 21% (residual derivation) against `layer-6-deliverable-data.json` SOT or specialist appendix §3 cross-tab. If SOT carries different splits, update the SVG segment widths. Headline 25.6% Class I + 15.7% Class IV in 36-market view stays anchored. | v1 Phil-iteration #3 | `site/exports/long-read/stack-bar-fragility-9-9-15-3-nexalps.svg` |
| 4 | **Lens-grid placement** — move from §1 (currently before lens-prose) to **end of §1** (after the lens-prose paragraph that introduces them). Reader gets prose → recap-graphic flow. | v1 Phil-iteration #4 | Markdown source + image embedding pipeline |
| 5 | **Scenario stack — revert to prose** — current is bulleted list (was an em-dash-density workaround); revert to conversational paragraph form via structural rewriting (per Phil-locked register elsewhere in the suite). | v1 Phil-iteration #5 | Markdown source §6 |
| 6 | **Margins** — 50mm × 50mm → 25mm × 25mm default (160mm content on A4); +5mm to 30mm × 30mm if line-length feels long after the L4 entropy pass | New | `tools/long-read-pdf-gen.py` |
| 7 | **Page breaks** — `KeepTogether([heading, first_paragraph])` (no widowed headings); `KeepTogether([image, caption])` (no mid-graphic breaks; no separated graphic/header pairs); orphan/widow control (min 2 lines on continuation page); pull-quote anchored to surrounding paragraph | New | `tools/long-read-pdf-gen.py` (ReportLab `KeepTogether` + `Paragraph` style options) |
| 8 | **Sources structured table** — convert inline prose ("Based on 59 primary sources including Autor 2024 (QJE)…") to **Tier 1 + Tier 2 table** structure. Columns: Source / Tier / How informs (one-liner). Mirrors `site/sources.html` schema. Tier 1 = 41 entries; Tier 2 = 18 entries. | New | Markdown source (sources section) + generator (table parser) |
| 9 | **At-a-glance table wrap fix** — page 2 currently wraps "Countries below adaptive-capacity floor" as `"adaptiv e-capacity floor"` (mid-cell hyphenation broken). Increase column width or use `<nobr>`-equivalent flowable; verify all 4 cells render without mid-word break | New (visual catch) | `tools/long-read-pdf-gen.py` (table cell sizing) |
| 10 | **Section-header action-title rewrite** — current section headers are topic noun phrases ("1. The diagnostic", "2. The 36-country corridor map", "3. The asymmetry", etc.). Rewrite each as a complete implication sentence per L5 + Promptiers/EQ4C convention. Suggestions: §1 *"Why the historical safety net is unraveling"*; §2 *"Three corridors, not one — and where each country lands"*; §3 *"Counts hide what populations reveal — Class IV is 16% of workers on 3 markets"*; §4 *"The reskilling arithmetic doesn't add up"*; §5 *"Eight scenarios, and the one most likely depends on whether the economy is still growing"*; §6 *"Three candidate scenarios tested; none held up alone"*; §7 *"What survives, and what comes next in Part 7"*. Sub-session iterates these for register fit, surfaces for Phil-lock. | L5 + new | Markdown source (all section headers) |

### Pass 2 — Light voice/register application (L3 + L4)

After Pass 1 lands, run two voice-fidelity passes against the updated markdown source:

#### L3 — Anti-AI-tell rescan (broader vocabulary list)

Existing v1 ran banned-phrase scan against Phil's `linkedin-playbook/references/banned-phrases.md` Tier 1/2/3 (clean — 0 hits). Extend to the broader 2025–26 AI-tell vocabulary surfaced by the research:

```
delve, tapestry, leverage, synergy, optimise, streamline, empower,
unprecedented, paradigm, robust, crucially, navigate, harness, unleash,
seamless, cutting-edge, elevate, vibrant, pivotal, showcasing, boasts,
stands as, ever-evolving, ever-changing, ever-growing, multifaceted,
nuanced, holistic
```

Plus pattern-matching:
- "It's not X — it's Y" / "not just X but Y" formulas
- "Furthermore" / "Additionally" / "Moreover" sentence openers
- Cheery sign-offs (e.g. "Stay curious!", "Onwards!", "Let's go.")
- Knowledge-cutoff disclaimers
- Three-item lists for everything (audit: are 3-item lists structurally justified or padding?)

**Don't strip em-dashes wholesale.** Match human density (~1 per 200–400 words is canonical NYT/New Yorker/Atlantic). Current density check: report em-dash count + words ratio in v1; flag if outside 1/200–400 range.

#### L4 — Sentence-length entropy check

Per ~500 words of body prose (excluding table cells, source-card captions, callouts):
- ≥1 sentence under 8 words
- ≥1 sentence over 30 words

Audit each section. If a section runs all 12–25 word sentences, restructure to introduce one short and one long. Don't manufacture variance — find natural sentences that should be shorter (a punchline, a transition) or longer (a clarification, a chained logical step).

**This is the single most-underexploited move in the field per the synthesis research.** Light application = audit + flag, not full rewrite.

### Pass 3 — Verification

1. **md5 audit** — Specialist Appendix `.md` + `site/data.json` + `layer-6-deliverable-data.json` UNCHANGED.
2. **Markdown clean** — banned-phrase grep returns 0 hits across Phil's Tier 1/2/3 + the broader 25–28 word list above.
3. **PDF assembled** — page count remains 12–18 (cover + content); Geist rendering confirmed; KeepTogether prevents widowed headings or mid-graphic breaks (visual check on 3 random pages).
4. **L4 entropy report** — per-section sentence-length distribution: report short (<8 words) count, long (>30 words) count, average. Flag sections that miss the 1/1 minimum.
5. **L3 broader-vocab scan** — report any hits with paragraph context for Phil-lock.
6. **Cover page** — light-italic 80 px Phil-locked headline renders on pearl-white; byline + at-a-glance moves to page 2.
7. **Sources table** — Tier 1 (41 rows) + Tier 2 (18 rows) renders; mirrors `site/sources.html`.

### Discipline (carry forward)

- **Style lock — long-read PDF in Nexalps; markdown source matches Phil-locked rest-of-suite voice.** Typography stays Geist (research is about voice, not type).
- **Banned-phrase scan against both lists** (Phil's curated + broader 25–28 word AI-tell vocab).
- **BR-19 fabrication discipline** — every numeric, citation, per-country claim traces to SOT or 59-source bibliography. Action-title rewrites must stay anchored to actual section content.
- **Audit-at-class** — when one action-title rewrite lands, audit all 7 section headers for parallel construction.
- **Two-layer chart-port idiom** — graphics geometry shared across web + print; only style swaps.
- **Time budget: 3–4 h.** If Pass 1 stretches (sources table parser, cover-page template), surface scoping issue. L3/L4 light passes should not balloon — they're audit-and-flag, not full rewrite.
- **Banned-phrase scan on own draft + commit messages** before report-back.

### Report-back format

Single markdown file: `bundle-n3-v2-iteration-report-2026-05-08.md`. Same directory.

1. **TL;DR** — 6–8 bullets covering the 10 Pass 1 items + L3/L4 findings
2. **Pass 1 audit** — per-item: file diff summary, before/after screenshot pointer where visual, edge cases handled
3. **Pass 2 audit** — L3 broader-vocab grep results (hits + paragraph context); L4 sentence-length entropy table per section
4. **Verification checklist (1–7)** — pass/fail per item
5. **Phil-iteration handoff** — flag 2–4 things you're least sure about (action-title fit, pull-quote placement, sources table column widths, etc.)
6. **Brain capture candidates** (if any) — likely none beyond what v1 surfaced

---

## Out of scope

- **Typography swap** (Geist → serif) — research returned no off-the-shelf alternative; defer indefinitely
- **Full multi-reviewer architecture** (L2) — deferred to separate `analytical-prose-craft` skill build (handover at `/Users/philippmaul/Documents/second-brain/.claude/worktrees/xenodochial-shirley-728acf/docs/analytical-prose-craft-skill-build-handover-2026-05-08.md`)
- **SCQ + Pyramid + MECE structural refactor** (full L5) — light application via action-title rewrite only; full whitepaper-engine refactor is post-deploy work
- **Stylometric corpus pre-compute** for NYT/Atlantic/Economist — flagged in research as the most-underexploited move; out of scope here
- **Brain skill enrichment** — capture candidates surface for Phil per Rule 12

---

*This brief is the dispatch prompt for Bundle N3 v2. Sub-session iterates the long-read in 2 passes (10 design items + light L3/L4/L5 voice pass), surfaces report. ~3–4 h. Output: updated long-read .md + .pdf + report.*
