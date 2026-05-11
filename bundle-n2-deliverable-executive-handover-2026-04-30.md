# Handover Prompt — Bundle N2: Layer 6 Executive Edition + One-Pager + Einfache Sprache Companion (Phase 4 Track A)

Bounded write session. Three deliverables, one composition pass. All read from the locked SOT JSON. ~90–120 min.

---

## Context (read this section before the START PROMPT)

Phase 4 deliverable surface forks across three audience registers:

```
Specialist Appendix    →  layer-6-deliverable-document-appendix.md   (existing N, will be renamed)
Specialist Long-Read   →  layer-6-deliverable-document-long.md       (Bundle N3, separate handover)
Executive Edition      →  layer-6-deliverable-document-executive.md  (THIS BUNDLE)
McKinsey One-Pager     →  layer-6-deliverable-onepager.md            (THIS BUNDLE — extract from Executive)
Einfache Sprache       →  layer-6-deliverable-document-einfache.md   (THIS BUNDLE — B1 companion)
```

Bundle N2 ships the three lower-tier-audience artifacts. Specialist content (Appendix, Long-Read) is not this bundle's concern.

---

## START PROMPT

I need you to compose three deliverables for Layer 6: an Executive Edition (BCG-style brief, ~1,800–2,200 words), a McKinsey-style One-Pager (~600–800 words, downloadable extract), and an Einfache Sprache (B1-register) companion to the Executive (~1,000 words, draft pending human review).

This is NOT a re-computation or analytical session. All locks come from Phases 1–3 + Bundle M (data) + Bundle N (which becomes the Specialist Appendix). Bundle N2's job is **register translation** — turning the locked findings into three audience-tiered formats.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — **canonical input.** Schema v1.0 locked by Bundle M. Every numeric claim and country list traces to a JSON field.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document.md` — Specialist Appendix (former Bundle N). **Source for analytical content + tone calibration for the OPPOSITE register.** The executive edition is what this document is *not* — denser-than-needed for the executive reader; full appendix detail; specialist vocabulary. Read it to know what to translate, not to copy.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase4-plan-2026-04-29.md` — Phase 4 plan + Q-decisions baked in.
- `/Users/philippmaul/Documents/projects/european-ai-labour-actions/RATIONALE.md` — **Layer 7 rationale.** The Executive Edition closer references Layer 7 explicitly. Read this to get the Layer 7 framing right ("what can be done").
- `/Users/philippmaul/Documents/second-brain/skills/linkedin-playbook/references/banned-phrases.md` — **anti-slop discipline.** Run the same banned-phrase scan on all three outputs as part of verification.

### Locked register — Executive Edition v4 sample

The opening of the Executive Edition is locked (composed in the master session, polished by Phil). Use it verbatim as §0 + the opening of §1. Do NOT rewrite this opening — it carries Phil-voice and was iterated to lock through 4 rounds.

```markdown
**Europe's AI Labour Map Experiment — What Survives the Stress Test**

**Prelude**

Forecasts of how artificial intelligence will reshape European jobs come in three flavours: vendor reports tied to compute spending (mostly US-centric), macro projections built on past patterns (often only one), and political communications anchored to promises that materialize differently than advertised. None takes seriously what happens when the historical "old jobs disappear, new jobs appear" pattern weakens, when ageing populations fail to absorb displacement, and when institutions are stretched by parallel crises in defence, global decoupling, climate, and the war in Ukraine.

So we ran an experiment. We scored 36 European labour markets — the EU-27 plus Iceland, Liechtenstein, Norway, Switzerland, the United Kingdom, and four candidate countries — across five lenses, stress-tested them under seven economic scenarios, and grouped the results into three corridors and four fragility classes. The brief below walks through the headline map, lens-by-lens findings, scenario probabilities by economic regime, country profiles, and what the framework cannot see.

**What Survives the Stress Test**

The headline result is uncomfortable. Only nine countries remain resilient under stress: the five Nordics (Denmark, Finland, Iceland, Norway, Sweden) and four Continental peers (Belgium, France, Luxembourg, Netherlands). All others either:

- **Fracture under at least one of six macro shocks** (nine countries), or
- **Already sit in the worst corridor under business-as-usual conditions** (15 countries).

Three more markets — North Macedonia, Serbia, Turkey — show **active cascade**🛈 signals, with institutional capacity already close to saturation.

How quickly **robustness**🛈 disappears as thresholds tighten is the second uncomfortable finding. Under a strict definition — no scenario produces a worse outcome — even Norway and Sweden fail. Policy briefings typically apply a softer rule: performance stays within ±1 corridor and never lands in the worst corridor under any standard variant. Under the softer rule, nine countries qualify. Under the strict rule, none do. There is no unconditionally safe European labour market at the corrected threshold.

That said, no fate is written in stone. Every country — and especially Europe as a whole — has a chance to make the (sometimes) hard decisions needed to improve its population's situation. The fragility class a country sits in today is a read-out of present conditions, not a forecast of inevitability — **ALMP**🛈 capacity, reskilling investment, EU budget allocation, regulatory choices, and fiscal headroom are levers, not constants.

This sets the frame. The remainder of the brief explains where each country lands and why. What can be done comes in a separate document — Layer 7 of this project, scoped separately.
```

This opening is ~470 words. The remaining ~1,330–1,730 words extend the brief along the structure already promised in the prelude: lens-by-lens findings, scenario probabilities by regime, country profiles, framework's known limits.

### Executive Edition (`layer-6-deliverable-document-executive.md`) — required structure

| Section | Words | Content |
|---|---:|---|
| Prelude (locked v4) | ~300 | The Phil-voice opening above |
| §1 What Survives the Stress Test (locked v4) | ~470 | The headline + robustness paradox + silver lining |
| §2 The Five Lenses, Briefly | ~280 | One short paragraph per lens (~55 words each). Each lens names what it tests + the headline finding + one concrete number. Tooltips on first occurrence of each lens-specific term. |
| §3 Seven Scenarios, Three Economic Regimes | ~280 | What the scenarios are (one-line each, plain language); the three regimes (growth-baseline, secular-stagnation-warning, post-growth-empirical); the regime-conditional finding (S2b dominates under post-growth). Tooltip on first regime mention. |
| §4 Country Profiles by Class | ~480 | Four short paragraphs, one per class (I/II/III/IV). Names the countries; one mechanism sentence; carries the load-bearing callouts (s2b-dependent set; high-coord archetype split; BE/NL squeeze-flag). T34 referenced explicitly but plain-language ("aggregation hides bifurcation — the high-coord cluster splits into two archetypes"). |
| §5 What the Framework Cannot See | ~180 | Honest limits: live intelligence, MFF per-country gap, candidate-country C2 sub-cluster proxy, Lens 2 single-string compression, capability-floor 2-digit ceiling. Plain language. |
| §6 Closer + Layer 7 teaser | ~120 | One short paragraph: brief closing thought; Layer 7 teaser. Voice-led, not consultancy boilerplate. |

**Total target: 1,800–2,200 words.** Hard ceiling 2,400.

### One-Pager (`layer-6-deliverable-onepager.md`) — McKinsey-style structural extract

Intended for download as a 1-page PDF (typeset later by Phil). Markdown source needs to render to ~1 page A4 when typeset at 11pt body / 14pt heading.

| Element | Words / Format |
|---|---|
| Title | "Europe's AI Labour Map — At a Glance" |
| Sub-title | One-sentence framing (e.g., "Of 36 European labour markets, 9 remain resilient under stress.") |
| Headline finding box | 1 sentence: the strict-zero structural-bias finding. Highlighted (bold or callout). |
| 5-finding section | The 5 folded findings as 5 bullets, each 1–2 sentences in plain language. Each bullet leads with the country count or named country group. |
| What we tested | 1 paragraph (~80 words): 36 countries, 5 lenses, 7 scenarios, 3 regimes, 4 fragility classes. Plain naming. |
| Country distribution | 4 mini-bullets: Class I (9), Class II (9), Class III (15), Class IV (3). Names the countries in I + IV (small lists); aggregates II + III. |
| Closer | 1 sentence Layer 7 teaser. |

**Total target: 600–800 words.** Hard ceiling 900. Designed as visual one-page extract; assumes the reader will see this *before or instead of* the full Executive.

### Einfache Sprache Companion (`layer-6-deliverable-document-einfache.md`) — B1 register, draft pending human review

**Status header (mandatory, must appear at top of file):**

```markdown
> **Status: Erstentwurf — vor Veröffentlichung muss eine Einfache-Sprache-Fachperson den Text prüfen.**
> First draft. Before public release this text needs review by a certified Einfache-Sprache editor.
> Reference style guides: Hurraki Wörterbuch (https://hurraki.de) and Netzwerk Leichte Sprache (https://www.leichte-sprache.org).
```

**Register rules (B1 / Einfache Sprache, NOT Leichte Sprache A1-A2):**
- Sentence length cap: ~15 words average, 20 hard maximum.
- Active voice. Present tense where natural.
- One main idea per sentence.
- Define every specialist term inline at first occurrence (no tooltip dependency — this version is text-first).
- No nested clauses. Use full stops instead of commas + clauses.
- No metaphors that depend on cultural reference (e.g. "fate written in stone" → "the situation is not fixed forever").
- Numbers in figures (9, 36) not words for clarity.
- No English jargon untranslated. ALMP → "Active Labour Market Policies" (define) / "Aktive Arbeitsmarktpolitik" if German output desired.

**Output language:** German Einfache Sprache OR English plain-B1, depending on Phil's pre-dispatch instruction. Default if not specified: produce both as separate sub-files (`-einfache-de.md` and `-einfache-en.md`) and report back asking which Phil wants public.

| Section | Words | Content |
|---|---:|---|
| Status header | — | Mandatory review-flag block (above) |
| Title | — | Plain: "Europe's AI Labour Map — easy version" / "Europas Arbeitsmarkt und KI — einfache Version" |
| What we did | ~150 | Short sentences. We looked at 36 countries. We asked: which can handle AI changes to work? We tested 5 things and 7 scenarios. |
| What we found | ~200 | 9 countries are stable (name them). 9 are at risk under shocks. 15 are already in trouble. 3 are in active crisis. |
| What "stable" means | ~150 | Plain explanation of the robustness paradox. With strict rules, 0 countries are stable. With softer rules, 9 are. So no European country is fully safe. |
| What can change things | ~250 | The levers, in plain language: government training programs, EU money, school + university programs, rules. Layer 7 teaser. |
| Glossary box | ~250 | 8–10 key terms with B1 definitions (cascade, robust, ALMP, corridor, lens, scenario, fragility, displacement, regime, MFF). One term + one short sentence definition each. |

**Total target: ~1,000 words.** Hard ceiling 1,200.

### Glossary input — for the executive site (Bundle O dependency)

Bundle N2 also produces a glossary draft inline as a side-output. This goes to Bundle O for the `/glossary.html` page. **Format: tab-separated lines** (`term \t standard_definition \t einfache_definition`). Aim for 25–40 terms covering all jargon used in the Executive Edition + One-Pager + Einfache version. Save as `layer-6-glossary-draft.tsv`.

Required terms (minimum set):
ALMP · cascade · corridor · displacement · fragility class · lens · MFF · NDLS · post-growth empirical · regime · reinstatement effect · robustness · scenario · scale (aggregate / distributional / both) · secular stagnation · squeeze flag · structural bias · TAA · ESCO · ISCO · Klinger coordination share

### Constraints

- **Read-only against the SOT JSON, the Specialist Appendix, and the Layer 7 RATIONALE.** Do not modify any of these.
- **Locked v4 opening is verbatim.** Do not rewrite §Prelude or §1.
- **Phil-voice in two specific lines is locked verbatim** (with the apostrophe fix on "population's"):
  - The silver-lining sentence: *"That said, no fate is written in stone. Every country — and especially Europe as a whole — has a chance to make the (sometimes) hard decisions needed to improve its population's situation."*
  - The closer: *"What can be done comes in a separate document — Layer 7 of this project, scoped separately."*
- **No emoji** in any output (the 🛈 tooltip markers are the exception — they map to a UI affordance in Bundle O, not display glyphs in print).
- **No fabrication (BR-19).** Every numeric claim and country list traces to the SOT JSON.
- **Banned-phrase scan is a sentinel** (see verification block below). Run on all three outputs.
- **Tier-3 anti-slop discipline:** no sentence-fragment-then-colon openers ("Reality:", "The truth:"), no closing CTA, no AI-generated headshot patterns. The Executive Edition is consultancy register, not LinkedIn.
- **Em-dash discipline:** the Specialist Appendix runs at ~1.3 em-dashes per paragraph (defensible at that register). Executive Edition target: ≤0.7 per paragraph average. One-Pager and Einfache version: ≤0.3 per paragraph (em-dashes are friction at lower-prerequisite registers).
- Phil does all git commits.

### Verification (run before reporting back)

**Per-deliverable structural checks:**

1. Executive: word count 1,800–2,400. §Prelude + §1 verbatim from locked v4 (diff returns nothing). All section headings present.
2. One-Pager: word count 600–900. Renders to ~1 page A4 when typeset (rough check: under 60 lines at standard markdown rendering).
3. Einfache: word count under 1,200. Status header present at top. Sentence-length scan: ≤15 words average, ≤20 max.

**Cross-deliverable consistency:**

4. Country counts match across all three: Class I=9, Class II=9, Class III=15, Class IV=3.
5. s2b-dependent set named identically (AT, LU, TR) across Executive §4 + One-Pager.
6. 12-country breach list named identically across Executive §4 + One-Pager (or omitted from One-Pager if word budget tight; flag in report-back).
7. Layer 7 closer language identical across Executive §6 + One-Pager closer + Einfache §What can change things.

**Anti-slop / banned-phrase scan:**

8. Tier 1 banned phrases: 0 hits across all three files.
9. Tier 2 banned phrases: 0 hits across all three files.
10. Tier 3 patterns: 0 sentence-fragment-then-colon openers; 0 closing CTAs; 0 emoji-as-bullet-marker.
11. Em-dash density: Executive ≤0.7/paragraph, One-Pager ≤0.3/paragraph, Einfache ≤0.3/paragraph.

**Numeric claims:**

12. Every number in every output traces to a SOT JSON field (random-sample 5 numbers per file; verify by grep against `layer-6-deliverable-data.json`).

**Glossary side-output:**

13. `layer-6-glossary-draft.tsv` written with ≥25 terms, each with both standard and Einfache definitions.

### When done — report back to master session with

1. Per-deliverable word count + section distribution.
2. Verification checklist (1–13) — pass/fail per item.
3. Banned-phrase scan results: number of hits per tier per file (expect 0 across the board; report any near-misses).
4. Em-dash density per file (Executive / One-Pager / Einfache).
5. Glossary draft term count + 3 example entries.
6. Any composition gaps surfaced (places where the SOT JSON or Specialist Appendix didn't carry a register-translatable field — e.g. mechanism sentences too thin for §4 plain-language rendering).
7. Einfache version: language decision — German, English, or both produced? If both, which is recommended for first publish?
8. Recommendation for Bundle N3 dispatch sequencing — parallel with Bundle O, or sequential after Bundle N2 review?
9. Any candidate brain captures (T34-shape patterns surfaced during register translation; BR triggers fired; new methodology observations).

## END PROMPT
