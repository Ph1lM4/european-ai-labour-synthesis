# Handover Prompt — Bundle W: Minto + Sources + Locked-Copy Propagation Across Deliverable Docs

Bounded composition session. **Updated 2026-05-08** to absorb Phase 3 + Phase 3.5 outcomes: SM 4 methodology Minto rewritten v5 (Phil-locked 2026-05-08; three-test scenario-completeness audit + Part 7 hook), S2 mechanism-string additive (works-council mediation + procurement-attached social conditionalities, ETUC + IndustriAll Europe), and **5 new primary source-cards** for `sources.html` (54 → **59 primary sources**: Rhodium / MIT Clean Investment Monitor; Bistline et al. NBER WP 32168 / Brookings 2024; OECD Pension Markets in Focus 2025; ETUC press release 2026-03-04; IndustriAll Europe Article 1450).

Propagates site-locked content (S1–S8 codes incl. Polycrisis Drag, 4-SM methodology with three-test ninth-scenario callout, plain-prose Italy block, scenarios phrasing edit, **59 primary sources** incl. Draghi 2024 + Brynjolfsson Li Raymond 2023 + ILO Tier 1 reclassification + the 5 Phase 3.5 additions, banned-phrase scrub) into the 5 existing Layer 6 deliverable docs. Plus rewrites the One-Pager to mirror the landing-page Minto structure. Plus surfaces a Phil-decision on the Einfache deliverables. **Phase 1 (new 2026-05-08): site SOT updates — methodology.html SM 4 swap; SOT JSON S2 mechanism-string additive; sources.html + llms.txt + 7 page bylines + JSON-LD source-count cascade 54 → 59.** Phase 2: existing deliverable-doc propagation. ~10–12 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** This is mostly a markdown / textual session; code-craft applies to any inline code blocks or table edits.

---

## Context

The synthesis site (Phases 1A → 2I) is structurally and editorially clean: 7 pages, **54 primary sources** at start of Bundle W (becomes **59** after Phase 1 cascade), 4-SM methodology with three-test ninth-scenario callout (SM 4 v1 currently on site, swaps to v5 in Phase 1), Polycrisis Drag for S8, plain-prose conventions, consistent typography, 1200 px containers throughout. The site is the canonical source-of-truth post-Phase-1.

The 5 Layer 6 deliverable docs (Executive, Specialist Appendix, One-Pager, Einfache EN, Einfache DE) were last updated during Bundle N (2026-04-30). They still reference pre-Bundle-V scenario codes (S2a/S2b/S4a/S4b/S5), a 3-SM methodology, "load-bearing" framings, the original 15-source bibliography, and an old narrow-container article-format implicit assumption. Bundle W aligns all 5 docs to the current site SOT.

**The One-Pager gets rewritten** to mirror the new landing-page Minto pyramid (hero + stats + 4 SMs with `Go deeper →` references). This makes the One-Pager the print/PDF derivative of the landing page; same body content, different render target. Per Phil's framing 2026-05-06: "the landing IS the one-pager."

**Einfache decision** — site-side Einfache was dropped in Phase 2C. The two Einfache deliverable docs (`-de.md`, `-en.md`) are still in the project. Phil decision needed: archive both, keep both with current scope-mark, or update both with Bundle W changes. Sub-session surfaces.

---

## START PROMPT

I need you to propagate the site-locked content into the 5 Layer 6 deliverable docs, rewrite the One-Pager to mirror the landing-page Minto structure, and surface the Einfache decision for Phil. All copy edits are Phil-locked verbatim from the live site — sub-session does structural insertion + textual replacement, not authoring.

### Read FIRST (absolute paths)

**Deliverable docs (write to these):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document.md` — Specialist Appendix (261 lines)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-executive.md` — Executive Edition (87 lines)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-onepager.md` — One-Pager (30 lines, gets full rewrite)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-einfache-en.md` (109 lines, decision-pending)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-einfache-de.md` (109 lines, decision-pending)

**Site canonical (read for verbatim copy):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` — landing-page hero + stats + 4 SMs (canonical for One-Pager rewrite)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — Italy plain-prose block + Conclusion + 3 within-section Minto SMs
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — Polycrisis Drag prominent block + scenarios phrasing
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — **4-SM methodology Minto** (the new structural pattern; SM 4 is the ninth-scenario)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html` — pan-European Minto open + variation guard + headline pull-quote
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html` — 54 primary source-cards (becomes 59 after Phase 1; Phase 2 propagates the 59 count)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/llms.txt` — canonical source-list summary

**SOT data:**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — current SOT
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — lens spec

### Phil-locked anchors (verbatim — propagate exactly as on the site)

#### S8 rename map (apply across all 5 deliverable docs)

```
"Concurrent-Crisis Cascade" → "Polycrisis Drag"
"concurrent-crisis cascade" → "polycrisis drag"
"concurrent_crisis_cascade" → "polycrisis_drag"
```

Pre-flight grep before editing:
```
grep -in "concurrent.crisis\|concurrent_crisis" layer-6-deliverable-document*.md layer-6-deliverable-onepager.md
```

Verify zero residual after rename. Note: "concurrent-crisis trigger" / "concurrent-crisis tax" are generic adjective uses (not the scenario label) — leave as-is.

#### Pre-Bundle-V scenario code rename map

```
S2a → S5 (Wage Cliff)
S2b → S2 (Climate Adaptation Boom)
S3 (old "Muddle Through") → S4 (Muddle Through)
S4a → S6 (Reinstatement Failure)
S4b → S7 (Bandwidth Fracture)
S5 (old "Concurrent-Crisis Cascade") → S8 (Polycrisis Drag)
NEW S3 → Jobs Transform
```

Plus: every reference to "seven scenarios (six routine + one conditional)" → "eight scenarios (seven routine + one conditional)". Add S3 Jobs Transform to any spectrum / list / probability table that enumerates.

Pre-flight grep:
```
grep -in "S2a\|S2b\|S4a\|S4b\|seven scenarios\|six routine\|S5_cascade" layer-6-deliverable-document*.md layer-6-deliverable-onepager.md
```

Apply via the renumbering map. Note: pre-Bundle-V `S3` (old Muddle Through) needs careful disambiguation from new `S3 Jobs Transform`. Use temporary suffix during the grep-replace pass to avoid collision.

#### Italy plain-prose block (verbatim from `findings.html` lines 442-444)

Replace the existing Italy block in Specialist Appendix + Executive doc + Einfache (if updated) with the locked plain-prose version:

> **Italy — the workforce shrinks before AI displaces a single worker.**
>
> Italy is the only major European economy with negative net migration in 2025. Institutional ageing has crossed from buffer-deficit into accelerating decline — the workforce is contracting on its own, before AI substitutes for any task. Working-age population trajectory: −17.5% to 2050 (sharpest-decline tier). Retirement offset 25.3%, well below the 80% buffer threshold. Migration-dependence is acute but politically constrained, while unfillable shortages in care, trades, and healthcare amplify rather than absorb displacement. Italy sits in Class III, secular-stagnation regime, with the parallel-cascade scenario carrying a 0.10 conditional weight. Net migration 2025: **−485,823**.

Drop any "load-bearing demographic finding" eyebrow. Render as plain prose with bold lead sentence + body paragraph + bold inline number for `−485,823` (no display-size override).

#### 4-SM methodology Minto (verbatim from `methodology.html` SM 1–4)

Replace the existing methodology section in Specialist Appendix + Executive doc with the new 4-SM structure:

**SM 1:** *Five lenses, chosen because earlier parts of the project had already gathered the evidence.*
> We went with the five lenses we already collected evidence on in earlier parts of the project: AI exposure, demographics, disruption pathways, reskilling capacity, and careers data. The constraint was not which lenses might exist in theory — it was which ones we could test rigorously today, with European data, across 36 countries.

**SM 2:** *One calibration choice changes the headline.*
> [Use existing methodology SM 2 support text from `methodology.html` — the threshold-ladder explanation. Sub-session reads + ports.]

**SM 3:** *What we deliberately left open.*
> Three known gaps constrain this analysis:
> 1. **Occupational detail:** capability-floor breach is reported at a coarser job classification (2-digit ISCO) because the finer-grained European Social Survey microdata (3-digit) requires a multi-week application. The count here is a lower bound.
> 2. **Funding allocation:** the EU's adaptation funding through 2030 is not yet broken down by country. We can see the overall envelope, but not its distribution.
> 3. **Employer behaviour:** we cannot observe live signals like hiring, retraining launches, or redundancy plans because they sit behind paywalls or in proprietary HR systems.

**SM 4 (v5, Phil-locked 2026-05-08):** *We tested three candidate additions. None held up on its own.*

> *The EU Industrial Accelerator Act, proposed in March 2026, looked like a candidate ninth scenario. On close inspection, it runs the same absorption pathway as Climate Adaptation Boom: state-coordinated sectoral demand, with workers pivoting into new sectors. The US Inflation Reduction Act, three years post-implementation, confirms the mechanism class.*
>
> *We also tested whether the wealth-fund-rich economies (Norway, Sweden, Denmark, the Netherlands, with Switzerland adjacent) deserved their own regime. The direction is empirically defensible — pension and sovereign-wealth differences are real — but the per-country threshold did not hold cleanly across all five candidates. Switzerland's central-bank reserves do not behave like Norway's sovereign wealth fund, so the line between "wealth-fund rich" and "post-growth" could not be drawn consistently.*
>
> *A third test asked whether startup-driven absorption (Europe's gap relative to the US in venture-scale firm formation) warranted its own scenario. ECB analyses document the gap clearly, and examples from other regions suggest the mechanism is possible. But each existing scenario in this taxonomy rests on something concrete — Cedefop's per-country employment projections, the Net-Zero Industry Act's committed €100 billion, the IRA's three years of realised data — and startup-driven absorption in Europe has no equivalent anchor yet. Without a comparable anchor, it cannot be probability-weighted alongside the others.*
>
> *The three rejections rest on different reasoning, but the takeaway is the same. Going forward, more than one of these mechanisms likely has to work at the same time — climate-led sectoral pivot, industrial-policy demand, wealth-fund buffering, startup formation, and the within-occupation reshape already in the taxonomy. The next part looks at what happens when several of those forces work together, and what that would cost.*

**Note for sub-session:** SM 4 v5 above is the canonical text. The current `methodology.html` carries SM 4 v1 (single-paragraph "Why eight scenarios, not more"); Phase 1 of Bundle W swaps it for v5 verbatim. Do not read v1 from the site as canonical — read this brief as canonical for SM 4 only. SM 1, SM 2, SM 3 remain canonical-from-site.

#### S2 mechanism-string additive (Phil-locked 2026-05-08; Phase 3.5 ETUC + IndustriAll Europe convergence)

The S2 Climate Adaptation Boom mechanism string in `layer-6-deliverable-data.json` (line ~7941) currently ends:

> *"...new sectoral demand absorbs displaced workers (locked spec line 96, 104)."*

Phase 1 of Bundle W appends a conditional clause:

> *"...new sectoral demand absorbs displaced workers, conditional on works-council mediation and procurement-attached social conditionalities (ETUC; IndustriAll Europe) (locked spec line 96, 104)."*

Sources: ETUC press release 2026-03-04 + IndustriAll Europe Article 1450 (both land in `sources.html` per next section). The additive specifies HOW absorption happens (mechanism-component), not just THAT absorption happens (lever-acknowledgment) — see `feedback_mechanism_string_conditionality.md` for the discipline.

Pre-flight grep:
```
grep -n "scenarios.S2\|S2.mechanism\|new sectoral demand absorbs displaced" layer-6-deliverable-data.json site/data.json
```

Apply identical edit to both `layer-6-deliverable-data.json` and `site/data.json` (the site-mirror). Verify md5 checksum changes on both files only on these specific lines (no other drift).

#### Source-cards: 5 new for `sources.html` (54 → 59 primary; Phase 3.5 additions)

Add 5 new primary source-cards to `site/sources.html`, matching the existing source-card schema (Tier indicator + author/year + brief + "How informs" line). Then cascade source-count `54 → 59` across:

- `site/sources.html` — header count
- `site/llms.txt` — Sources line + count summary
- 7 page bylines (`site/index.html`, `findings.html`, `scenarios.html`, `europe.html`, `methodology.html`, `sources.html`, `glossary.html`) — *"Based on N primary sources"*
- 7 JSON-LD blocks — Dataset (data pages) / Article (editorial) — `numberOfItems` / `citation` count if applicable

**The 5 new source-cards:**

| # | Source | Tier | How informs |
|---|---|---|---|
| 55 | Rhodium Group / MIT Clean Investment Monitor — IRA tracker | **Tier 1** | Realised US labour data on state-coordinated industrial buildout; cross-jurisdictional confirmation of Climate Adaptation Boom (S2) mechanism class; Q1 2025 fragility footnote ($8B / 27,000 jobs cancelled) anchors the "mechanism class confirmed, fragility documented" framing in methodology SM 4. |
| 56 | Bistline et al. NBER WP 32168 / Brookings 2024 — IRA labour modelling vs realised | **Tier 1** | Academic anchor for IRA labour-outcome assessment; complements Rhodium tracker; supports the "three years post-implementation confirms the mechanism class" claim in methodology SM 4. |
| 57 | OECD Pension Markets in Focus 2025 | **Tier 1** | Per-country pension-asset operationalisation evidence for the Wealth-Fund Rich regime hypothesis (declined 2026-05-08 on threshold-inconsistency grounds); cited in methodology SM 4 v5 second paragraph. |
| 58 | ETUC press release 2026-03-04 — Industrial Accelerator Act position | **Tier 2** | Labour-side framing of the IAA; convergent with IndustriAll on works-council mediation + procurement-attached social conditionalities; anchors the S2 mechanism-string additive. |
| 59 | IndustriAll Europe Article 1450 — Made in Europe 2.0 labour-side reception | **Tier 2** | Sectoral-union framing complementary to ETUC; second source for the S2 additive convergence. |

**Pre-flight grep for cascade:**
```
grep -rn "54 primary\|54 sources\|Based on 54" site/ layer-6-deliverable-onepager.md llms.txt 2>/dev/null
```

After cascade, verify zero `54` source-count residual; expect to find `59` in 8+ places (sources.html + llms.txt + 7 byline locations + JSON-LD).

#### Scenarios phrasing edit

Page headline (and any mirror in the docs): *"Eight ways the next decade could play out and the most likely one depends on whether the economy is in a growth, secular stagnation, or post-growth stage."*

Replace any "still growing" / "whether the economy is still growing" phrasing with the locked version.

#### Polycrisis Drag prominent block (verbatim from `scenarios.html` §1)

Already absorbed in the rename. Verify the merged framing reads consistently — S8 = Polycrisis Drag; defence rearmament + climate adaptation pressure + global decoupling + Ukraine reconstruction overwhelming institutional capacity simultaneously; carried as conditional outside the routine spectrum.

### Phase 1 — Site SOT updates (new 2026-05-08; do FIRST, before Phase 2 per-doc work)

Phase 1 lands the SM 4 v5 swap, S2 mechanism-string additive, 5 new source-cards, and source-count cascade onto the site SOT. Phase 2 (existing per-doc tasks) reads the updated SOT and propagates.

#### Phase 1 task list

1. **`site/methodology.html` SM 4 swap** — replace SM 4 v1 (single-paragraph "Why eight scenarios, not more") with SM 4 v5 verbatim from this brief. Header changes from *"Why eight scenarios, not more"* to *"We tested three candidate additions. None held up on its own."* Support changes from single paragraph to four paragraphs. Preserve surrounding HTML structure (CSS classes, parent container, sibling SM 1–3 untouched).
2. **`layer-6-deliverable-data.json` + `site/data.json` S2 mechanism-string additive** — append the conditional clause *"...conditional on works-council mediation and procurement-attached social conditionalities (ETUC; IndustriAll Europe)..."* per the spec above. Apply identical edit to both files. Pre-flight grep, post-flight md5 diff verifying only the targeted line changed.
3. **`site/sources.html` add 5 new source-cards** — match existing source-card schema (Tier badge + author/year header + brief + "How informs" line). Insert at appropriate Tier-grouped position (Rhodium + Bistline + OECD PMF in Tier 1 block; ETUC + IndustriAll in Tier 2 block).
4. **Source-count cascade 54 → 59** — apply across `site/sources.html` header, `site/llms.txt` Sources line + count summary, 7 page bylines, 7 JSON-LD blocks. Pre-flight grep returns 54 residual; post-flight grep returns 0 residual `54` count refs and 8+ occurrences of `59`.
5. **Verify Phase 1 clean** — md5 checksum the 6 SOT files post-Phase-1; expect changes on `methodology.html`, `data.json`, `sources.html`, `llms.txt`, `layer-6-deliverable-data.json`, plus the 6 other page-byline files. Other content unchanged.

After Phase 1 verifies clean, proceed to Phase 2.

### Phase 2 — Tasks per doc (existing scope, with count + SM 4 + S2 updates absorbed)

#### 1. Specialist Appendix (`layer-6-deliverable-document.md`, 261 lines) — primary update target

- Apply the S8 + scenario-code renumber map across the full doc
- Rewrite the methodology section using the 4-SM Minto structure (verbatim above)
- Replace the Italy block with the locked plain-prose version
- Update the scenarios spectrum to enumerate S1–S8 (was S1–S5 with letter-suffix variants)
- Update probability tables to use S1–S8 codes; add S3 Jobs Transform row
- Update bibliography section to match the **59 primary sources** in post-Phase-1 `site/sources.html` (Tier 1 = 41, Tier 2 = 18). Use the post-Phase-1 `site/llms.txt` "Sources" line as the canonical comma-separated source list. Add Brynjolfsson Li Raymond 2023 + ILO 2025 reclassified Tier 1 + all Phase 2E additions + the 5 Phase 3.5 additions (Rhodium / MIT CIM, Bistline NBER WP 32168, OECD Pension Markets in Focus 2025, ETUC press release 2026-03-04, IndustriAll Europe Article 1450).
- Banned-phrase scrub: zero residual hits for `load-bearing`, `structurally` (adverb), `structural asymmetry`, `the analysis is built to surface`. Use `read` → `analysis` swap where applicable.
- Italy phrasing: drop any "load-bearing demographic finding" eyebrow.

#### 2. Executive Edition (`layer-6-deliverable-document-executive.md`, 87 lines)

- Same renumber map + S8 rename
- Apply 4-SM methodology Minto in the methodology section (likely a brief summary; abridge to fit Executive register but preserve all 4 SM headers)
- Italy plain-prose block
- Bibliography: short-form citations inline (e.g. "(Draghi 2024)", "(Brynjolfsson Li Raymond 2023)") rather than full source-cards; verify every citation maps to a source in the 59-source canonical list (post-Phase-1)
- Banned-phrase scrub
- Scenarios phrasing alignment

#### 3. One-Pager (`layer-6-deliverable-onepager.md`, 30 lines) — full rewrite

Rewrite to mirror the landing-page Minto pyramid (`site/index.html` structure):

```markdown
# No European labour market is fully safe from AI-driven job displacement.

*We stress-tested 36 markets across five lenses and eight scenarios. Most countries can absorb the disruption only partially, and 15 are likely already beyond that threshold. Under the rules we applied, only nine have the statistical strength to hold up under pressure.*

By Philipp Maul · Nexalps · April 2026 · Part 6 of 7 in the European AI Labour Market suite
Based on 59 primary sources including Autor 2024 (QJE), Cedefop 2025, Draghi 2024, the European Climate Risk Assessment, Eurostat EUROPOP2023, the Rhodium / MIT Clean Investment Monitor, and OECD Pension Markets in Focus 2025.

## Summary statistics

[4-card stats panel content from site/index.html]

## Findings

> *More than three-quarters of European labour markets sit in uncomfortable territory.*

[Locked SM 1 support — Findings, verbatim from site/index.html landing SM 1]

→ Full read: synthesis.nexalps.com/findings.html

## Scenarios

> *Eight ways the next decade could play out and the most likely one depends on whether the economy is in a growth, secular stagnation, or post-growth stage.*

[Locked SM 2 support — Scenarios, verbatim]

→ Full read: synthesis.nexalps.com/scenarios.html

## Europe

> *Europe doesn't have one answer. It has 36.*

[Locked SM 3 support — Europe, verbatim]

→ Full read: synthesis.nexalps.com/europe.html

## Methodology

> *How we tested and what we deliberately left open.*

[Locked SM 4 support — Methodology, verbatim]

→ Full read: synthesis.nexalps.com/methodology.html
```

The One-Pager content is identical to the landing page; the format is markdown-print rather than HTML-web. Same body of work, two render targets.

#### 4. Einfache EN + Einfache DE — Phil-decision pending

Three options:
- **(a) Archive both** — site-side Einfache is dropped (Phase 2C); deliverable docs follow. Move both to `archive/` subdir with a status note.
- **(b) Keep both, mark scope** — flag at the top of each: *"Scope-marked 2026-05-07: not currently aligned with v1.1 site state. Updated as part of an Einfache reactivation push if/when scoped."* No content edits.
- **(c) Update both** — apply the full S8 rename + 4-SM methodology v5 + S2 conditionality additive + Italy plain-prose + 59-source bibliography + banned-phrase scrub to both Einfache docs. Same scope as Specialist Appendix but in B1 / Einfache register.

Sub-session **default:** option (b) — keep both with scope-mark. Recommend in report-back. Phil locks at next turn. If Phil overrides to (a) or (c), Bundle W.1 micro-bundle handles.

#### 5. Banned-phrase scrub — site-wide audit pattern (per `feedback_audit_at_class_at_phase_boundaries.md`)

After per-doc edits, run the full grep across all 5 deliverable docs:
```
grep -in "load-bearing\|load bearing\|structurally\|structural asymmetry\|the analysis is built to surface\|\bthis read\b\|\bthe read\b" layer-6-deliverable-document*.md layer-6-deliverable-onepager.md
```

Zero residual. Apply rewrites per the Phase 2C / 2D pattern (e.g., "load-bearing demographic finding" → "the standout demographic case"; "this read" → "this analysis"; "structurally weaker" → "materially weaker").

### Constraints

- **All copy is Phil-locked verbatim.** Site-locked SMs, headers, supports, Italy block, Polycrisis Drag block, scenarios phrasing edit — propagate exactly as on the site. No re-authoring.
- **No data changes.** `data.json` and `layer-6-deliverable-data.json` unchanged. Bibliography cites sources; doesn't redefine numbers.
- **Source citations match `site/sources.html` canonical.** Use the `site/llms.txt` "Sources" line as the master list. Add Brynjolfsson Li Raymond 2023 + ILO 2025 Tier 1 reclassification per Phase 2F follow-up.
- **No emoji.**
- **Phase 1B/2B/2C/2D/2E/2F/2H/2I site state preserved** — sub-session edits the deliverable docs only; live-site files untouched.
- **Banned-phrase scan applies to all edits** (per the brain rule landed 2026-05-06).
- **Phil does all git commits.**

### Verification (before reporting back)

**Phase 1 — Site SOT updates (verify clean before Phase 2)**

A. **`methodology.html` SM 4 v5** — header reads *"We tested three candidate additions. None held up on its own."*; support is 4 paragraphs verbatim from this brief. SM 1, SM 2, SM 3 unchanged. CSS / surrounding HTML structure intact.
B. **S2 mechanism-string additive** — `layer-6-deliverable-data.json` + `site/data.json` carry the conditional clause *"...conditional on works-council mediation and procurement-attached social conditionalities (ETUC; IndustriAll Europe)..."* in the S2 mechanism string. Both files show the additive on identical lines.
C. **5 new source-cards in `site/sources.html`** — Rhodium / MIT CIM (Tier 1), Bistline NBER WP 32168 (Tier 1), OECD Pension Markets in Focus 2025 (Tier 1), ETUC press release 2026-03-04 (Tier 2), IndustriAll Europe Article 1450 (Tier 2). Each follows existing source-card schema (Tier badge + author/year + brief + "How informs" line).
D. **Source-count cascade 54 → 59 complete** — grep for `\b54\b` in source-count contexts across `site/`, `llms.txt`, all 7 page bylines, all 7 JSON-LD blocks returns 0 residual; grep for `\b59\b` in same contexts returns 8+ occurrences.
E. **Tier split updated** — 41 Tier 1 (was 38) + 18 Tier 2 (was 16) — 41/18 verified in `site/sources.html` header + `site/llms.txt` summary.

**Phase 2 — Deliverable docs propagation (existing checklist, count + SM 4 + S2 absorbed)**

1. **S8 rename complete** across all 5 docs; pre-flight grep for `concurrent.crisis|concurrent_crisis` returns 0 hits (or only the generic adjective uses, flagged).
2. **Pre-Bundle-V scenario codes scrubbed** — `S2a/S2b/S4a/S4b` and pre-V `S5` (Concurrent-Crisis Cascade) all replaced with new codes.
3. **8 scenarios named** in every spectrum / list / probability table; S3 Jobs Transform present.
4. **4-SM methodology Minto v5** present in Specialist Appendix + Executive doc — SM 1–3 verbatim from site, SM 4 v5 (header *"We tested three candidate additions. None held up on its own."* + 4-paragraph support) verbatim from this brief.

4b. **S2 mechanism-string additive** present wherever S2 mechanism is referenced in deliverable docs (Specialist Appendix scenarios section; Executive scenarios summary; One-Pager if applicable). The conditional clause on works-council mediation + procurement-attached social conditionalities lands intact.
5. **Italy plain-prose block** present; "load-bearing demographic finding" eyebrow removed; bold lead sentence + bold inline `−485,823` (no display-size).
6. **One-Pager rewritten** mirroring landing-page Minto: hero + lede + byline + stats + 4 SMs with locked supports + `Go deeper →` references.
7. **Bibliography aligned** — 59 primary sources in Specialist Appendix; short-form citations in Executive; both include Draghi 2024, Brynjolfsson Li Raymond 2023, ILO 2025 Tier 1, and the 5 Phase 3.5 additions (Rhodium/MIT CIM, Bistline NBER, OECD PMF 2025, ETUC, IndustriAll Europe).
8. **Scenarios phrasing** — "growth, secular stagnation, or post-growth stage" verbatim; no "still growing" residual.
9. **Banned-phrase grep across all 5 docs** returns 0 hits.
10. **Einfache decision surfaced** — sub-session's recommendation (default option b: keep + scope-mark) reported with rationale.
11. **Markdown parses** — every doc still valid markdown; tables render; no broken links.
12. **No data file changes** — `data.json` + `layer-6-deliverable-data.json` checksum-verified untouched.

### When done — report back to master session with

**Phase 1 report-back:**

0a. **SM 4 v5 swap audit** — methodology.html before/after diff for SM 4 only; SM 1-3 unchanged confirmed.
0b. **S2 mechanism-string additive audit** — line-level diff on `layer-6-deliverable-data.json` + `site/data.json`; conditional clause landed; no other line changes.
0c. **5 new source-cards** — full rendered HTML of each new card surfaced for sanity-check; Tier-grouping placement noted.
0d. **Source-count cascade 54 → 59** — list of every file touched + count of `54 → 59` replacements per file (expect ≥8 files: sources.html + llms.txt + 7 byline pages + JSON-LD).
0e. **Phase 1 md5 audit** — checksum of every site SOT file pre-/post-Phase-1; only expected files changed.

**Phase 2 report-back:**

1. **Per-doc line count diff.**
2. **Verification checklist (1–12)** — pass/fail per item.
3. **S8 rename audit** — per-file occurrence count + every line touched.
4. **Pre-Bundle-V code-scrub audit** — every old-code → new-code replacement, organised by file.
5. **4-SM methodology audit** — SM 1–4 verbatim verification across Specialist + Executive.
6. **Italy block audit** — present + plain-prose + zero load-bearing eyebrow on every doc that had an Italy section.
7. **One-Pager final state** — full rendered markdown surfaced for Phil sanity-check.
8. **Bibliography diff** — Specialist Appendix old (15 sources) → new (59 sources) + Tier 1/2 split (41/18) + named verification of Draghi 2024 + Brynjolfsson Li Raymond 2023 + ILO 2025 Tier 1 + 5 Phase 3.5 additions.
9. **Banned-phrase grep** — confirm 0 hits across all 5 deliverable docs.
10. **Einfache decision recommendation** — option (b) by default; rationale; Phil-decision flag for override.
11. **Bundle N3 readiness** — anything that surfaced during W that the Specialist Long-Read brief should account for.
12. **Any candidate brain captures** — likely none beyond the audit-at-class-at-phase-boundaries meta-rule already landed.

## END PROMPT
