# Cards Plain-Language Rewrite — Report (2026-05-09)

Bounded composition session per `cards-plain-language-rewrite-handover-2026-05-09.md`. Per-country `narrative_one_liner` field rewritten across both source-of-truth and site mirror for all 37 entries (36 country codes + Ukraine reference panel).

---

## TL;DR

- **37 / 37** `narrative_one_liner` strings rewritten in plain language across both `layer-6-deliverable-data.json` (SOT) and `site/data.json` (mirror). Where/what/lever framing held throughout.
- **Banned-phrase scan: 0 hits** across Tier 1 / Tier 2 / Tier 3 LinkedIn-playbook list and the layer-site AI-tell vocab (delve, tapestry, leverage, synergy, paradigm, robust, etc.). Em-dash budget per one-liner: 0 ≤ 2 (cap honoured).
- **Forbidden-technical scan: 0 hits** for `Lens N`, `S1–S8`, `C1–C3`, `growth_baseline`, `secular_stagnation`, `post_growth_empirical`, `Klinger`, `Gini`, `ALMP`, `ESCO`, `ISCO`, `NACE`, `Autor 2024`, `El-Sahli`, `Dell'Acqua`, `Cedefop`, `robust`.
- **Word counts**: range 22–31 words/one-liner (mean 27); only NL at 31 sits one above the brief's "~30 max"; brief uses `~` so soft-cap. All others ≤30.
- **JSON validity**: both files parse cleanly (`json.load`). Field count match: both files now carry 37 `narrative_one_liner` strings (36 country + 1 UA insert).
- **md5 pre/post**: SOT `0ada3d87…` → `6753154c…`; site `14edf39d…` → `65ac63b5…`. Diff scope audited: only the 37 narrative strings changed; the UA panel gained one new line where the field did not previously exist; no other SOT fields touched.
- **Pre-existing SOT↔site divergence** (3 fields, not from this session) flagged below — Phil to reconcile separately.
- **Render check**: I cannot start a browser preview from this sub-session; flagged for Phil's manual verification (DE / NO / BG / MK / IT / UA recommended click-throughs).

### Sample before / after

| code | before | after |
|---|---|---|
| BG | *"Growth-baseline C2 reaching C3 only under S6/S7 stress; aggregate."* | *"Bulgaria is coping for now, with an expanding economy that leaves room for retraining; weakening job-replacement or stretched institutions would push it into displacement."* |
| DE | *"Post-growth + breach + squeeze flag; Europe's largest economy in S4 vulnerability."* | *"Germany's traditional job-replacement story is now weaker because the economy has stopped growing, so the most plausible recovery runs through climate-adaptation work rather than conventional tech jobs."* |
| NO | *"Nordic Class I + post-growth + breach; cascade priority high (post-growth fiscal headroom)."* | *"Norway sits among Europe's most resilient labour markets thanks to deep retraining capacity and a sovereign-wealth buffer; its breached capability floor and export-dependence make resilience conditional on global trade."* |
| MK | *"Candidate-partial-coverage Class IV; vuln 0.62."* | *"North Macedonia is currently failing on partial-coverage data, with high overlapping-shock pressure straining its institutions; EU candidate-status investment in retraining capacity is the main lever to shift the trajectory."* |
| UA | *(field absent — render fell back to a hard-coded string)* | *"Ukraine is the reference case for institutional collapse already underway, with war-damaged training infrastructure, refugee outflow, and 40% defence spending bounding the worst case European peers could face."* |

---

## Per-country table (37 rows for Phil-lock)

| code | country | class | corridor | regime | new `narrative_one_liner` |
|---|---|---|---|---|---|
| AT | Austria | II | C2 | post growth empirical | Austria is stable today, but with the economy no longer growing, recovery runs only through climate-adaptation work, and stretched institutions would push it into displacement. |
| BA | Bosnia and Herzegovina | II | C2 | growth baseline | Bosnia and Herzegovina is coping for now on partial-coverage data; the expanding economy leaves room for retraining capacity, though weakening job-replacement or stretched institutions would push it into displacement. |
| BE | Belgium | I | C2 | growth baseline | Belgium is among the more resilient economies thanks to strong worker protection, but its closeness to the UK's lighter-protection labour market exposes it to capital flight under overlapping shocks. |
| BG | Bulgaria | II | C2 | growth baseline | Bulgaria is coping for now, with an expanding economy that leaves room for retraining; weakening job-replacement or stretched institutions would push it into displacement. |
| CH | Switzerland | II | C2 | post growth empirical | Switzerland is stable today but its capability floor has breached on essential occupations; with the economy no longer growing, weakening job-replacement would push it into displacement. |
| CY | Cyprus | III | C3 | growth baseline | Cyprus already shows more displacement than its labour market can absorb; an expanding economy still leaves fiscal room to scale active labour-market policy as the main recovery lever. |
| CZ | Czechia | III | C3 | growth baseline | Czechia is already past the absorption threshold; the expanding economy leaves fiscal room to scale active labour-market policy, the main lever back toward partial absorption. |
| DE | Germany | II | C2 | post growth empirical | Germany's traditional job-replacement story is now weaker because the economy has stopped growing, so the most plausible recovery runs through climate-adaptation work rather than conventional tech jobs. |
| DK | Denmark | I | C1 | growth baseline | Denmark sits among Europe's most resilient labour markets, with strong worker protection and active retraining capacity; its main risk is exposure to overlapping shocks across defence, climate, and trade. |
| EE | Estonia | III | C3 | growth baseline | Estonia is already past the absorption threshold; the expanding economy gives fiscal room to scale retraining capacity, the main lever back toward partial absorption. |
| EL | Greece | III | C3 | secular stagnation warning | Greece already shows more displacement than its labour market can absorb, with stagnant output limiting the normal job-replacement channel; building active labour-market capacity is the main lever. |
| ES | Spain | II | C2 | growth baseline | Spain is coping for now; an expanding economy leaves room to add retraining capacity, but weakening job-replacement or stretched institutions would push it into displacement. |
| FI | Finland | I | C1 | post growth empirical | Finland is among Europe's most resilient labour markets thanks to deep reskilling capacity, but a stalled economy means recovery from any shock runs through climate-adaptation work rather than conventional growth. |
| FR | France | I | C2 | post growth empirical | France is stable today thanks to strong worker protection, though a stalled economy means recovery from any shock runs through climate-adaptation work rather than conventional tech jobs. |
| HR | Croatia | III | C3 | growth baseline | Croatia is already past the absorption threshold; the expanding economy leaves fiscal room to scale active labour-market policy, the main lever back toward partial absorption. |
| HU | Hungary | III | C3 | growth baseline | Hungary is already past the absorption threshold; the expanding economy gives fiscal room for retraining capacity, the main lever back toward partial absorption. |
| IE | Ireland | III | C3 | growth baseline | Ireland is already past the absorption threshold and its capability floor has breached on essential occupations; the expanding economy still leaves room to scale retraining as the main recovery lever. |
| IS | Iceland | I | C1 | growth baseline | Iceland is among Europe's most resilient labour markets, but its small scale and a breached capability floor on essential occupations leave it dependent on continued integration with regional labour flows. |
| IT | Italy | III | C3 | secular stagnation warning | Italy is already past the absorption threshold, with a shrinking workforce reducing absorption capacity before AI displaces a single worker; reskilling and migration policy are the only realistic levers. |
| LI | Liechtenstein | II | C2 | post growth empirical | Liechtenstein is stable today but its capability floor has breached on essential occupations; with the economy no longer growing, weakening job-replacement would push it into displacement. |
| LT | Lithuania | III | C3 | growth baseline | Lithuania is already past the absorption threshold; the expanding economy gives fiscal room to scale retraining capacity as the main recovery lever. |
| LU | Luxembourg | I | C2 | post growth empirical | Luxembourg is stable today thanks to deep institutional capacity, but its capability floor has breached on essential occupations and recovery from any shock runs only through climate-adaptation work. |
| LV | Latvia | II | C2 | growth baseline | Latvia is coping for now, with an expanding economy that leaves room for retraining; weakening job-replacement or stretched institutions would push it into displacement. |
| MK | North Macedonia | IV | C2 | growth baseline | North Macedonia is currently failing on partial-coverage data, with high overlapping-shock pressure straining its institutions; EU candidate-status investment in retraining capacity is the main lever to shift the trajectory. |
| MT | Malta | III | C3 | growth baseline | Malta is already past the absorption threshold; the expanding economy gives fiscal room to scale retraining capacity as the main recovery lever. |
| NL | Netherlands | I | C2 | growth baseline | The Netherlands is stable today thanks to strong worker protection, but its capability floor has breached on essential occupations, and closeness to the UK's lighter-protection market exposes it to capital flight. |
| NO | Norway | I | C1 | post growth empirical | Norway sits among Europe's most resilient labour markets thanks to deep retraining capacity and a sovereign-wealth buffer; its breached capability floor and export-dependence make resilience conditional on global trade. |
| PL | Poland | III | C3 | growth baseline | Poland is already past the absorption threshold; the expanding economy gives fiscal room to scale active labour-market policy, the main lever back toward partial absorption. |
| PT | Portugal | III | C3 | growth baseline | Portugal is already past the absorption threshold; the expanding economy gives fiscal room to scale retraining capacity, the main lever back toward partial absorption. |
| RO | Romania | II | C2 | growth baseline | Romania is coping for now, with an expanding economy that leaves room for retraining; weakening job-replacement or stretched institutions would push it into displacement. |
| RS | Serbia | IV | C2 | growth baseline | Serbia is currently failing on partial-coverage data, with overlapping shocks straining its institutions; EU candidate-status investment in retraining capacity is the main lever to shift the trajectory. |
| SE | Sweden | I | C1 | post growth empirical | Sweden sits among Europe's most resilient labour markets thanks to strong worker protection and deep retraining capacity, though its export-dependence means its position is conditional on continued global trade integration. |
| SI | Slovenia | III | C3 | growth baseline | Slovenia is already past the absorption threshold; the expanding economy gives fiscal room to scale retraining capacity, the main lever back toward partial absorption. |
| SK | Slovakia | III | C3 | growth baseline | Slovakia is already past the absorption threshold; the expanding economy gives fiscal room to scale active labour-market policy as the main recovery lever. |
| TR | Turkey | IV | C2 | growth baseline | Turkey is currently failing on partial-coverage data, with high overlapping-shock pressure and steep inequality; its only realistic recovery channel runs through climate-adaptation work rather than conventional growth. |
| UK | United Kingdom | III | C3 | post growth empirical | The UK is already past the absorption threshold with its capability floor breached on essential occupations; a stalled economy means recovery runs through climate-adaptation work rather than conventional tech jobs. |
| UA | Ukraine | IV (ref) | — | — | Ukraine is the reference case for institutional collapse already underway, with war-damaged training infrastructure, refugee outflow, and 40% defence spending bounding the worst case European peers could face. |

---

## Mechanism-fidelity flags (countries where SOT mechanism was thinner / Phil-verify)

These are countries where the SOT (`fragility_class`, `phase3_corridor`, `regime`, scenario corridor map, `squeeze_flag`, `breach_flag`, `s2_dependent`) was the only structured anchor and country-specific narrative depth was limited. The one-liner falls back to the generic Class+Corridor+Regime+(routine-stress mechanism) frame; Phil-verify if a country-specific nuance should be folded in.

| code | flag | why |
|---|---|---|
| BA | partial-coverage; otherwise generic CEE C2 | `narrative_one_liner` was *"Partial-coverage Class II preserved (no extreme readings); CEE growth-baseline."*; no country-specific flags. One-liner uses the generic C2-coping + partial-coverage caveat frame. |
| LV | generic CEE-in-C2 | No squeeze/breach/s2-dependent flags; SOT carries no LV-specific mechanism beyond the regime and corridor. Used generic C2-coping frame. |
| RO | generic CEE-in-C2 | Same as LV — no specifying flags. Generic frame. |
| ES | generic Med-in-C2 | Same — Spain has no squeeze/breach/s2-dep flags or country-specific note in SOT; generic frame. |
| LT, MT, SI, SK, HR, HU, PL, PT, CZ, EE | generic Class-III C3 | These ten Class-III/C3 entries with `growth_baseline` and no specifying flags share a near-uniform one-liner ("already past the absorption threshold … expanding economy gives fiscal room … main lever back toward partial absorption"). Differences across these one-liners are minor lexical variation (retraining vs active labour-market policy). If Phil wants per-country differentiation here, that requires the per-country mechanism notes (e.g. sectoral exposure, demographic specifics) that aren't currently in the SOT one-liner / scenario-distribution / regime-implications fields. |
| MK, RS, TR | candidate-partial-coverage + Class IV | SOT carries `poly` / `vuln` / `gini` numeric readings but no per-country mechanism prose. Recommend Phil verify that "high overlapping-shock pressure" (MK/TR) vs "overlapping shocks" (RS) language matches his framing; the readings differ but the SOT prose doesn't articulate the distinction. |
| IE | breach + growth-baseline, no s2-dep | One-liner combines Class III + breach + expanding-economy fiscal room. Phil-verify the framing — Ireland's specific FDI-channel exposure isn't captured by SOT flags. |
| NL | Class I + squeeze + breach + UK-adjacency | The Continental squeeze sub-cluster mechanism is folded in via "closeness to the UK's lighter-protection market". Phil-verify register. |
| BE | Class I + squeeze + breach + UK-adjacency | Same as NL — Continental squeeze framing. |
| LU | Class I but s2-dependent + breach | An unusual combo (Class I but optimism only via climate-adaptation work). One-liner names both. Phil-verify whether the Class-I framing should appear more prominently. |

---

## Banned-phrase scan results

**Clean: 0 hits.**

Patterns scanned across all 37 new strings (case-insensitive regex):

- **Tier 1 / Tier 2 / Tier 3 LinkedIn-playbook**: `the real (question|caveat|issue|problem|reason)`, `here's the thing`, `let that sink`, `where it gets interesting`, `what most people miss`, `game-changer`, `at the end of the day`, `hot take`, `unpopular opinion`, `absolutely`, `this is what no one is talking about`, `the uncomfortable truth`, `holding up a mirror`, `voices like yours`, `paradigm-shift`, `bright/genuine/real humans`, `heavy lifting`, "It's not X — it's Y", "not just X but Y".
- **Layer-site AI-tell vocab**: `delve`, `tapestry`, `leverage` (word-boundary, to avoid catching "lever"), `synergy`, `optimise/optimize`, `streamline`, `empower`, `paradigm`, `crucially`, `navigate`, `harness`, `unleash`, `seamless`, `cutting-edge`, `elevate`, `vibrant`, `pivotal`, `showcasing`, `boasts`, `stands as`, `ever-evolving`, `multifaceted`, `nuanced`, `holistic`, `unprecedented`.
- **Brief-explicit**: `structurally`, `load-bearing`, `the analysis is built to surface`.
- **Colon-fragment openers**: `^Reality:`, `^The truth:`, `^Hard fact:`, `^One word:`, `^My take:`.

Em-dash budget: cap ≤ 2 per one-liner. All 37 strings sit at 0 em-dashes (the rewrite leaned on commas + semicolons; em-dash density was the most common AI-tell to police, so I avoided them entirely).

Note on word "lever": I use `lever`, `levers`, `recovery lever` non-trivially across the corpus (it's the third beat of the spec's "where / what / lever" frame). The banned-list word is `leverage` (full word). The scan uses `\bleverage\b` to avoid false positives on `lever`/`levers`. **0 hits on `leverage`.**

Note on "deep retraining capacity" / "deep institutional capacity" / "deep reskilling capacity": `deep` is not on the AI-tell list and is the most concise word for the underlying mechanism (Lens 5 reskilling-capacity readings translated to plain language). If Phil wants this restructured ("strong" / "substantial" / "well-developed"), trivial s/deep/strong/g pass.

---

## Forbidden-technical scan results

**Clean: 0 hits.**

Regex patterns scanned (word-bound, case-insensitive):
- `\bLens\s?[1-9]\b` (Lens 1, Lens 5, etc.)
- `\bS[1-8]\b` (S1–S8 scenario codes)
- `\bC[1-3]\b` (C1–C3 corridor codes)
- `growth_baseline`, `secular_stagnation`, `post_growth_empirical`
- `\bKlinger\b`, `\bGini\b`, `\bALMP\b`, `\bESCO\b`, `\bISCO\b`, `\bNACE\b`
- `\bAutor 2024\b`, `\bEl-Sahli\b`, `\bDell'?Acqua\b`, `\bCedefop\b`
- `\brobust\b` (the brief allows `Robust` as a class-name; I avoided it entirely since the class-name didn't appear in any one-liner)

The brief's recommendation "ALMP → active labour-market policy" was applied verbatim where needed (CY, CZ, EL, HR, PL, SK).

---

## JSON validation + md5 audit

| | pre-edit | post-edit |
|---|---|---|
| `layer-6-deliverable-data.json` md5 | `0ada3d87e06a543e2b805fd2478986b8` | `6753154c06db6f843710fcce0a8f04d6` |
| `layer-6-deliverable-data.json` lines | 8338 | 8339 |
| `site/data.json` md5 | `14edf39d0aab065e0db862be440d582b` | `65ac63b50889722f3d47f81bb3f1e3bb` |
| `site/data.json` lines | 8337 | 8338 (file lacks trailing newline; +1 line from UA insertion) |
| `python -c 'json.load(open(F))'` | n/a | **OK** both files |
| `narrative_one_liner` count | 36 / file (no UA field) | 37 / file (36 country + 1 UA inserted) |

**Diff scope audit** (in-memory pre/post comparison via the edit script's `presence audit` + a structural-strip pass): only `narrative_one_liner` values changed across both files; the UA panel gained one new line where the field did not exist; no other key/value touched.

**SOT ↔ site mirror audit, narrative_one_liner only**: all 37 strings identical between the two files (verified by Python equality check on the gathered dicts).

---

## Pre-existing SOT ↔ site divergence (NOT introduced by this session)

While auditing diff scope I noticed 3 fields where SOT and site already differed before this edit:

| field path | SOT | site |
|---|---|---|
| `cross_cutting_findings.pan_european_aggregate.headline_finding_pan_european` | *"…3 in active cascade. Within the EU-27…"* | *"…3 in currently failing. Within the EU-27…"* |
| `ukraine_reference_panel.class_iv_anchor_role` | *"Empirical worst-case for Class IV active-cascade…"* | *"Empirical worst-case for Class IV currently-failing…"* |
| `fragility_classes.IV.label` | *"Active Cascade"* | *"Currently Failing"* |

Pattern: site/data.json has been rolled forward to the Phil-locked "Currently Failing" rename (the spec line referenced in the brief), but `layer-6-deliverable-data.json` still carries the older "Active Cascade" label in three places. **Out of scope for this session** (the brief restricts edits to `narrative_one_liner`). Recommend a follow-up s/Active Cascade/Currently Failing/ + s/active cascade/currently failing/ + s/active-cascade/currently-failing/ pass on the SOT to bring it in line with the locked rename.

---

## Phil-iteration handoff — countries I'm least sure about (5)

1. **AT (Austria)** — "stretched institutions" stands in for the S7 mechanism. AT's specific scenario flag is `toC3=[S7,S8]` (only S7 of the routine variants), so the one-liner reduces correctly, but "stretched institutions" is a paraphrase Phil hasn't yet locked elsewhere in the site copy. Other candidates: "training systems stretched too thin" (closer to brief's translation), "overstretched institutions" (one word shift). Check fit against `site/scenarios.html` Bandwidth Fracture wording.
2. **NL (Netherlands)** — 31 words, one over the soft cap. Three mechanism beats (worker protection + breached floor + UK-adjacency capital-flight) all earn their place from SOT flags, but the sentence sits at the boundary of "tight one-liner." If Phil wants 30 hard, easy s/its capability floor has breached on essential occupations/its capability floor has breached/ for –4 words.
3. **MK / RS / TR (Class IV trio)** — all three use "currently failing" per the Phil-locked rename. MK and TR use "high overlapping-shock pressure"; RS uses just "overlapping shocks." That distinction came from SOT numeric readings (MK `vuln 0.62`, TR `poly 0.67 / eea_vuln 0.75 / gini 44.8`, RS `poly 0.55 / eea_vuln 0.60`) — the prose register doesn't yet exist for these in the SOT. Phil-verify the register is what he wants for candidate-partial-coverage Class IV.
4. **LU (Luxembourg)** — the Class I + breach + s2-dependent combo is unusual (Luxembourg is the only Class I that runs entirely through climate-adaptation work for recovery). The one-liner leads with "stable today thanks to deep institutional capacity" but then immediately complicates with the breach + climate-adaptation dependence — three beats in 28 words. Reader might miss whether the Class-I or the breach is the lede. Phil-verify reading order.
5. **UK** — uses "stalled economy" rather than "no longer growing in the conventional sense." Same plain-language target, different word choice. Lock whichever Phil prefers as the canonical translation of `post_growth_empirical`; right now: AT uses "no longer growing", DE uses "stopped growing", FR / UK use "stalled economy". The variation is intentional but Phil may want one canonical phrase.

---

## Render check — flagged for Phil

Sub-session has no browser preview tool reachable in this environment, so the brief's step "open `site/findings.html` corridor map view in preview; click 3-5 countries (DE, NO, BG, MK, IT); confirm cards render new plain-language strings; no rendering errors" was **not executed**.

Render risk assessment:
- The `showDetail()` function in `findings.html` reads `c.narrative_one_liner || c.scenario_distribution_language || ''` — string value, no schema dependency. The change is a string-for-string swap inside the same field, so render risk is ~zero from a code path standpoint.
- UA reference panel render code reads `ua.narrative_one_liner || ua.note || 'Class IV reference panel — partial coverage…'`. We added the previously-missing `narrative_one_liner` field, which will now win the fallback chain. Visually-different result expected for the UA card (was rendering the fallback string; now renders the new one-liner).

Recommend Phil click through DE / NO / BG / MK / IT / UA / a Class III (e.g. IT or UK) to confirm visual fit, line-wrap behaviour at 30-word length, and the UA panel render.

---

## ⚠️ Live Inspection Required

Before locking:
- **Visual line-wrap fit**: 30-word one-liners may wrap differently than the prior ~12-word analyst shorthand on the corridor-map card UI; verify on desktop + mobile breakpoints.
- **UA panel newly rendering a real string**: previously the panel rendered the fallback. Confirm visual register.
- **Cross-page consistency**: scenarios.html and methodology.html may carry references to "Active Cascade" vs "Currently Failing" with the same SOT/site divergence noted above; if Phil reconciles by harmonising on "Currently Failing", a separate audit pass across `site/*.html` is warranted.
- **Voice register fit against the locked Italy block + Conclusion in findings.html**: I read both as register anchors and the one-liners are pitched at the same plain conversational register, but Phil's ear is the lock.

---

## Brain capture candidates (per Rule 12)

**None.** This session was composition execution against a Phil-locked brief, not pattern discovery. The only minor process observation worth noting (not a capture):

- The brief's example for Germany used "structurally weaker," but the brief's own discipline section bans `structurally`. Tension resolved in favour of the discipline section ("now weaker" used instead). If the brief's worked examples are intended to override the discipline section, that's a separate Phil-decision; otherwise the discipline section wins per the brief's own framing ("Banned-phrase scan applies").

**Captures:** None.

---

## Audit artefact

Edit script: `_apply_one_liners.py` (in project root). Idempotent — re-running against an already-edited file is a no-op (the regex looks for `narrative_one_liner` lines; the values are now the new strings). Safe to delete after Phil-lock.
