# Scenarios Page Iteration — Report 2026-05-09

Executed against `scenarios-page-iteration-handover-2026-05-09.md`. 9 surgical edits + 1 math fix on `site/scenarios.html`. SOT files untouched. md5 audit clean.

---

## TL;DR — one bullet per edit (file:line pointer)

- **Edit 1 — Hero h1 + lede:** new h1 + lede landed verbatim. [site/scenarios.html:273](site/scenarios.html:273), [site/scenarios.html:274](site/scenarios.html:274).
- **Edit 2 — §1 Spectrum lead:** swapped "it's eight" → "it's at least eight". [site/scenarios.html:292](site/scenarios.html:292).
- **Edit 3 — Polycrisis Drag (S8) prose:** two-paragraph rewrite with "pick-your-poison" framing + full mechanism list + 580-year hyperlink to `https://disruptions.nexalps.com/`. [site/scenarios.html:333](site/scenarios.html:333), [site/scenarios.html:334](site/scenarios.html:334).
- **Edit 4 — Math fix (S1+S3 combined probability):** 25%→5% replaced by 20%→13% at two locations: SM 2 support sentence ([site/scenarios.html:282](site/scenarios.html:282)) + weather-cluster note ([site/scenarios.html:341](site/scenarios.html:341)).
- **Edit 5 — S4 reskilling-capacity gap:** plain-language rewrite (7.55 M / ~3.34 M / ~2.89 M / 450K / 15 yr), dropped the inline "5–9 years" phrase (moved into Edit 9 paragraph). [site/scenarios.html:390](site/scenarios.html:390), anchor [site/scenarios.html:391](site/scenarios.html:391).
- **Edit 6 — S4 optimism path:** rewrote to plain language ("the only realistic 'good outcome' left in the model is the 'Climate Adaptation Boom' scenario..."), removed the second prose paragraph (P(S2 | post-growth) numeric paragraph) so block now reads as one paragraph + AT/LU/TR chip grid. [site/scenarios.html:399](site/scenarios.html:399).
- **Edit 7 — S5 capability-floor breach:** dropped subtitle in `<h2>`, replaced section-sub with two body `<p>` paragraphs verbatim from brief. Old "DK marginal entrant / HIGH=7 MEDIUM=4 LOW=1 / 1-digit→2-digit→11→12" detail removed per Phil-locked text. [site/scenarios.html:409](site/scenarios.html:409)–[site/scenarios.html:411](site/scenarios.html:411).
- **Edit 8 — Four normal-text-size replacements:** swapped all four `<p class="section-sub">` to plain `<p>` body styling.
  - 8.1 Weather-pattern intro (§2): [site/scenarios.html:340](site/scenarios.html:340)
  - 8.2 Trajectory chart caption (§3): [site/scenarios.html:356](site/scenarios.html:356)
  - 8.3 CI explanation (§4): [site/scenarios.html:379](site/scenarios.html:379)
  - 8.4 Squeeze-flag note (§6): [site/scenarios.html:417](site/scenarios.html:417)
- **Edit 9 — 5–9 year speed-gap explanation:** added as a third paragraph inside the reskilling-capacity gap plain-block (the same section that previously contained "5–9 years" inline). [site/scenarios.html:392](site/scenarios.html:392).

---

## Math fix audit

### Pre-flight grep (before any edits)
```
$ grep -n "25%.*probability to about.*5%\|combined probability under growth is around 25" site/scenarios.html
282: ...drops from about <strong>25%</strong> probability to about <strong>5%</strong>...
341: Their combined probability under growth is around 25%; under post-growth, around 5%.
```
2 hits — confirmed both target locations present.

### Post-flight grep
```
$ grep -cn "25%.*probability to about.*5%\|combined probability under growth is around 25" site/scenarios.html
0
```
0 hits.

### New-math landing grep
```
$ grep -n "20%</strong> probability to about <strong>13%\|combined probability under growth is around 20" site/scenarios.html
282: ...drops from about <strong>20%</strong> probability to about <strong>13%</strong>...
341: Their combined probability under growth is around 20%; under post-growth, around 13%.
```
Both new locations verified.

### SOT verification
From `site/data.json`:
- `scenarios.S1.probability_per_regime.growth_baseline = [0.05, 0.10, 0.15]` → mid 0.10
- `scenarios.S3.probability_per_regime.growth_baseline = [0.05, 0.10, 0.15]` → mid 0.10
- Combined growth = **0.20 (20%)** ✓ matches new text
- `scenarios.S1.probability_per_regime.post_growth_empirical = [0.02, 0.05, 0.10]` → mid 0.05
- `scenarios.S3.probability_per_regime.post_growth_empirical = [0.03, 0.08, 0.13]` → mid 0.08
- Combined post-growth = **0.13 (13%)** ✓ matches new text

Note on the "22% → 30%" S2 claim retained verbatim from Phil's locked text: SOT shows S2 mid `growth_baseline = 0.20` and `post_growth_empirical = 0.30`. Phil's "22%" is slightly above SOT mid (0.20) but within the band (0.15–0.25). Retained verbatim per "all copy verbatim from this brief; do not author or paraphrase" — flagging here for awareness.

---

## Verification checklist (1–10)

| # | Item | Result |
|---|---|---|
| 1 | md5 on `site/data.json` + `layer-6-deliverable-data.json` UNCHANGED | **PASS** — data.json `14edf39d0aab065e0db862be440d582b`, layer-6-deliverable-data.json `0ada3d87e06a543e2b805fd2478986b8`, both identical pre/post. |
| 2 | Hero + lede landed verbatim | **PASS** — [site/scenarios.html:273](site/scenarios.html:273), [site/scenarios.html:274](site/scenarios.html:274). |
| 3 | §1 spectrum lead landed verbatim | **PASS** — [site/scenarios.html:292](site/scenarios.html:292). |
| 4 | Polycrisis Drag landed verbatim + part-3 hyperlink resolved | **PASS** — hyperlink target `https://disruptions.nexalps.com/` (same target as nav `Disruptions ↗`). [site/scenarios.html:334](site/scenarios.html:334). |
| 5 | Math fix grep returns 0 hits on old; new locations verified | **PASS** — see Math fix audit above. |
| 6 | S4 reskilling + optimism + S5 capability-floor landed verbatim | **PASS** — [site/scenarios.html:390](site/scenarios.html:390), [site/scenarios.html:399](site/scenarios.html:399), [site/scenarios.html:410](site/scenarios.html:410). |
| 7 | Four "normal text size" sentences in normal body styling (no `.section-sub` / `.italic` / `.note` class) | **PASS** — all four `<p>` tags carry no class; inherit default body `p{font-size:16px;color:#d4d4d8;line-height:1.8}` from base CSS (line 110 of `site/scenarios.html`). |
| 8 | 5–9 year explanation added near existing 5–9 reference, plain language | **PASS** — placed as 3rd paragraph in the reskilling-capacity gap plain-block at [site/scenarios.html:392](site/scenarios.html:392). This is the same section that previously hosted the inline "5–9 years" phrase (now removed as part of Edit 5 rewrite). |
| 9 | Banned-phrase grep across all new copy returns 0 hits | **PASS** — scanned new copy against Tier 1 + Tier 2 + Tier 3 patterns (banned-phrases.md). No matches. Em-dash density on Edit 9 paragraph is 3 in one paragraph (uses Phil's locked text — does not trigger the "3+ in one short post" pattern at page scale). |
| 10 | Visual preview check | **PARTIAL** — running preview server (`synthesis-site`, port 3006) has cwd in a different worktree (`xenodochial-shirley-728acf`), so it does not serve the synthesis project at this path. Editor-side Launch preview confirmed visible on every edit (PostToolUse:Edit hook). HTML structure validated balanced via Python HTMLParser (0 unclosed tags, 0 mismatch errors). Recommend Phil opens the file directly or restarts the dev server with the correct cwd before publish. |

### Numeric BR-19 verification (per brief discipline)

| Claim | SOT location | Status |
|---|---|---|
| 7.55 M deep-reskilling cohort | `cross_cutting_findings.reskilling_capacity_gap.deep_reskilling_need_eu27_uk_m = 7.55` | ✓ |
| ~3.34 M annual training throughput | `…annual_throughput_total_m = 3.34` | ✓ |
| ~2.89 M baseline churn | `…channel_breakdown_per_year.consumed_by_baseline_churn_note` ("≈2.89M of 3.34M consumed by baseline economic churn") | ✓ |
| ~450 K net new annual | `…annual_throughput_net_new_m = 0.45` | ✓ |
| 15-year backlog | `…implied_backlog_years = 15` | ✓ |
| 5–9 year speed gap | `…speed_gap_years = "5-9"` | ✓ |
| AI disrupts in 1–3 yr; system responds 5–9 yr | `…ai_response_lag_years = "AI disrupts in 1–3yr; European VET/university systems respond in 5–9yr; structural lag 3–5yr…"` | ✓ |
| 12-country capability-floor breach | `cross_cutting_findings.capability_floor_breach.list` (12 entries: BE, CH, DE, DK, IE, IS, LI, LU, NL, NO, SE, UK) | ✓ |
| ~40 high-risk EU AI Act Annex III deployer occupations | Not surfaced as a discrete numeric field in `site/data.json` or `layer-6-deliverable-data.json` — Annex III high-risk deployer scope described qualitatively in AI-exposure provenance fields. | ⚠ flag for manual SOT cross-check |
| ~29 Product Liability Directive post-market duty occupations | Not surfaced as a discrete numeric field in either file. | ⚠ flag for manual SOT cross-check |
| 580 years of historical disruptions | Not surfaced as a discrete numeric field; closest hits in data.json are unrelated decimals (e.g. `0.5803`). | ⚠ flag for manual SOT cross-check (likely lives in the disruptions sister-site corpus, not in layer-6 data.json) |

The three ⚠ items are Phil-locked verbatim in the brief (which states they are "all SOT-anchored"). They are likely anchored in the broader project corpus (deliverable docs, sister-site disruptions data, sources page) rather than in the two JSONs in scope. Worth a manual eyeball before publish.

### md5 snapshot

| File | Pre-edit | Post-edit | Changed? |
|---|---|---|---|
| `site/scenarios.html` | `565d60d9ad6d4865722e258c13b9ea06` | `3a3cb062f0261748b4b7c8e723e46207` | yes (intended) |
| `site/data.json` | `14edf39d0aab065e0db862be440d582b` | `14edf39d0aab065e0db862be440d582b` | **no** ✓ |
| `layer-6-deliverable-data.json` | `0ada3d87e06a543e2b805fd2478986b8` | `0ada3d87e06a543e2b805fd2478986b8` | **no** ✓ |

---

## Phil-iteration handoff — least sure (3 items)

1. **Polycrisis Drag link target.** Used `https://disruptions.nexalps.com/` (matches existing nav-bar entry for the Disruptions sister-site). Anchor text rendered as "link to part 3" per Phil's verbatim phrasing. The link opens in a new tab (`target="_blank" rel="noopener"`). Alternative anchor styles to consider: (a) embed "part 3" only (drop the word "link to") for a cleaner reading flow; (b) use a deep link to a specific 580-year-corpus page rather than the site root. Both are minor copy-edit calls — left as written.

2. **Placement of the 5–9 year explanation.** Placed as paragraph 3 of the reskilling-capacity gap plain-block ([site/scenarios.html:392](site/scenarios.html:392)). Rationale: Edit 5's rewrite removed the inline "5–9 years" phrase from paragraph 1; placing Edit 9 immediately after the existing two paragraphs keeps the explanation where a reader expects to find it given the section title. Alternative placement: as a standalone `.plain-block` block between §4 (probability table) and the current reskilling block. Held current placement — easy to move if Phil prefers separation.

3. **§5 capability-floor — old detail removed.** Phil's locked text for Edit 7 did not include the previous prose detail ("DK is the marginal entrant; cascade priority distribution HIGH = 7, MEDIUM = 4, LOW = 1; 1-digit→2-digit lifted count from 11 to 12; 3-digit pass would likely add 1–2 entrants in Continental knowledge-economy band"). I removed it cleanly. Confirm this is intentional — that detail is still authoritative against SOT and may be worth retaining elsewhere (e.g. methodology page) rather than dropped from the project entirely.

Bonus (out of scope but flagged):
- §6 squeeze-cluster body retains a `<p>` mentioning "AT/LU/TR" chips inside the optimism block — preserved unchanged. Edit 6 dropped the post-growth-S2 numeric paragraph (the "P(S2 | post-growth) = 0.30" sentence). If Phil wants that probability detail surfaced elsewhere on the page, it could be appended to the §2 weather-grid card for post-growth or §4 table caption.
- "22% → 30%" S2 claim in Edit 4 SM 2 sentence retained per Phil-locked text; SOT mid is 20% → 30%. Within the 80% CI band, so not strictly incorrect, but worth a precision check on next pass.

---

## Brain capture candidates

None. Iteration was scoped and the brain already absorbed the prior structural patterns (Phil-iterative-locking, banned-phrase scan, SOT md5 audit, BR-19 verification). One pre-existing pattern reaffirmed: when Phil-locked text removes a previously-inline phrase ("5–9 years") and a separate edit re-introduces it as a paragraph, sequence matters — execute the removal-edit before the re-introduce-edit so the grep checkpoints land on the intended terminal state. Already standard practice; not new.
