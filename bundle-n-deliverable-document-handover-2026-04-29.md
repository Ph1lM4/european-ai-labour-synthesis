# Handover Prompt — Bundle N: Layer 6 Deliverable Document (Phase 4 Track A)

Bounded write session. Composes the analytical document (`layer-6-deliverable-document.md`) by reading from the Bundle M SOT JSON. No re-computation. ~75–90 min.

---

## START PROMPT

I need you to write the Layer 6 deliverable document. This is Track A of Phase 4: the analytical anchor that the advisory track (Cembra-class engagements, board materials, lecture decks) reads. Track B (the `synthesis.nexalps.com` site, Bundle O) renders from the same data; both tracks share the locked SOT JSON.

This is NOT a re-computation session. All locks are in place from Phases 1–3 and Bundle M. Bundle N's job is composition + narrative — turning the structured data into a readable, citable document.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — **canonical input**. Schema v1.0 locked by Bundle M (162.7 KB). Every factual claim in the document must trace to a field in this JSON. Do NOT read Phase 1–3 outputs directly except for tone calibration.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec. Reference for lens definitions, corridor labels, scenario taxonomy, Ukraine line 341, sparkline spec line 418.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase4-plan-2026-04-29.md` — Phase 4 plan + Q2-Q6 deliverable scoping decisions.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-m-deliverable-sot-json-handover-2026-04-29.md` — Bundle M handover for schema reference + the two narrative callouts M flagged (MFF per-country gap; candidate-country C2 sub-cluster routing).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-probability-findings.md` — Bundle L findings (TONE CALIBRATION ONLY — for register/voice. Do NOT copy-paste; re-compose from SOT JSON.)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-corridor-findings.md` + `layer-6-phase3-klinger-findings.md` — same purpose (tone calibration; do not duplicate).

### Goal — output `layer-6-deliverable-document.md`

A single markdown document. Audience: senior policy/advisory readers — board members, executive-search principals, lecture-room participants. Tone: scientific, declarative, no hedging beyond what the probability bands already encode. Length: **4,500–6,500 words** (hard ceiling 7,000). Structured for both linear reading and section-jump.

### Required document structure

```
# Layer 6 — European AI Labour Market Synthesis

## TL;DR — Five Findings (≤500 words, bullet-grouped)
## 1. Why this synthesis exists (≤400 words)
## 2. Methodology in one page (≤700 words)
## 3. The 36-country corridor map (≤900 words + table)
## 4. The five folded findings (≤1,800 words, ~360 words each)
   4.1 Structural-bias validation
   4.2 Demographic orthogonality
   4.3 The optimism path narrows to Climate Zone-C (s2b-dependent)
   4.4 High-coord archetype split (T34: aggregation hides bifurcation)
   4.5 BE/NL squeeze-flag — orthogonal jurisdictional buffering signal
## 5. Fragility-class country profiles (≤1,400 words)
   5.1 Class I — Robust (9): 5 Nordics + BE/FR/NL/LU
   5.2 Class II — Fragile (9)
   5.3 Class III — Pre-Failure Risk (15)
   5.4 Class IV — Active Cascade (3)
## 6. Scenario probability stack (≤600 words + table)
## 7. Ukraine reference panel (≤250 words)
## 8. Methodological appendix (≤900 words)
   8.1 Threshold-locking ladder (Phase 1 → Phase 3)
   8.2 Class I rule trail (3-stage: S5-orthogonal → relative-stable → asymmetric-guard)
   8.3 Capability-floor breach scope ceiling (12 countries / 2-digit)
   8.4 MFF per-country allocation gap
   8.5 Candidate-country C2 sub-cluster routing (BA/MK/RS/TR)
   8.6 Phase 5+ enhancement candidates
## 9. Sources + provenance
```

### Composition rules

1. **Read-only against the SOT JSON.** Every numeric claim, country list, classification, and probability quote sources from a JSON field. If a number isn't in the SOT JSON, do not invent it; flag the gap inline.
2. **Quote `narrative_one_liner` for each country profile.** The one-liner is the load-bearing sentence per country; build the profile around it. Don't paraphrase.
3. **Quote `scenario_distribution_language` for probability framing.** Use the IPCC AR6 likelihood-scale band wording from the JSON; do not bare-publish point estimates. Where you need a number, frame as range ("60–70% mass") not "0.65".
4. **Reference `metadata.amendments_trail` in §8.2.** The 3-stage Class I rule ladder (S5-orthogonal → relative-stable → asymmetric-guard) is the methodological transparency anchor. Render each stage with its empirical trigger.
5. **§4.4 must invoke T34** (`disruption-analysis` skill takeaway). The high-coord archetype split (NO/IS/DK/LU LIFT vs CH/DE/IE/UK DRAG) is the in-suite manifestation of T34 ("aggregation/granularity flips findings"). Name T34 explicitly; this is the cross-skill bridge that earns the document its pedagogical depth.
6. **§4.3 (s2b-dependent) must use Phil's chosen framing:** "The optimism path narrows to Climate Zone-C." Q4 lock — load-bearing callout. AT, LU, TR are the only three countries where S2b is the *exclusive* C1 path among 6 routine variants.
7. **§5 country profiles**: name + corridor + scale_tag + one-liner + 1–2 sentences of mechanism. Aim for ~30–40 words per country average. Cluster by class; within a class, order by alphabetical code.
8. **§8.4 MFF gap callout** (per Bundle M note): explicitly state that lens5a_eu_mff_allocation per-country share is null in the SOT JSON because the €64.6B aggregate is not disaggregated per Member State in public sources. Site Lens 5 panel renders aggregate only. This is a known gap, not an error.
9. **§8.5 candidate-country C2 sub-cluster routing** (per Bundle M note): explicitly state that BA/MK/RS/TR are routed to `central_eastern_european_in_c2` for sub-cluster purposes with `_system_p1: candidate-baseline (CEE+SE weighted avg)` preserved. Readers should not conflate candidate-baseline-proxied sub-clustering with confirmed institutional similarity. ~80–120 words.
10. **TL;DR (§TL;DR) is the most important section.** Five bullet-grouped findings (use the cross_cutting_findings keys as anchors). The reader who stops after TL;DR should still know the headline.
11. **No fabrication.** BR-19 strict. If a country mechanism isn't in the JSON, write "mechanism per Phase 1/2 lens findings (see provenance block)" rather than invent.
12. **No emoji** in the deliverable document. (Tables are fine; bullet markers fine; emoji not.)
13. **Markdown rendering targets**: GitHub-flavoured markdown. Tables with header row + separator. Code-fence blocks for any structured callouts. Anchor links between sections (§4.3 → §8.5 etc.).

### Constraints

- Read-only against `layer-6-deliverable-data.json` and the locked spec. Do not modify either.
- Do not modify any Phase 1–3 outputs.
- Do not commit. Phil does all git commits.
- Do not invoke web search; this is a closed-loop composition session.
- Word budget is real — over-shoot risks deliverable bloat. Cut before submitting.

### Verification (run before reporting back)

1. Word count between 4,500 and 7,000 (`wc -w`).
2. Every country in §5 traces to a country block in the SOT JSON (36 + Ukraine = 37 in the country profile section if Ukraine included; Ukraine actually goes in §7 reference panel, so §5 has 36).
3. Class distribution in §5 matches **9 / 9 / 15 / 3** (Class I count = 9, Class II = 9, Class III = 15, Class IV = 3).
4. T34 named in §4.4.
5. "Optimism path narrows to Climate Zone-C" framing present in §4.3.
6. AT / LU / TR named in §4.3 as the s2b-dependent set.
7. 12-country breach list named or referenced in §4.4 or §8.3.
8. Asymmetric-guard methodology trail rendered in §8.2 with all 3 stages.
9. Ukraine reference panel present and tagged not-corridor-mapped per spec line 341.
10. MFF gap callout present in §8.4.
11. Candidate-country C2 sub-cluster routing callout present in §8.5.
12. No emoji in the document body.
13. No probability point estimates outside the §6 probability table — narrative uses band language.

### When done — report back to master session with

1. Final word count + section-by-section word distribution.
2. Verification checklist (1–13 above) — pass/fail per item.
3. Any narrative gaps surfaced (places where SOT JSON didn't carry a needed field).
4. Top 3 framing choices made (where multiple legitimate phrasings existed and the choice affects emphasis).
5. Recommended next step:
   - Bundle O dispatch now (parallel render, since N stress-tested the schema and any gaps are documented)?
   - Or pause for Phil to review N before O builds?
6. Any candidate brain captures (T34 generalisations, advisory-track skill enrichments, BR triggers fired during composition).

## END PROMPT
