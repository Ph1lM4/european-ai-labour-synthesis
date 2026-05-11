# Layer 6 Data Fetch List — 2026-04-29

Tracks what's secured for Lens 5 + scenario stack scoring vs what's still open.

---

## ✅ Secured (cite-ready, 2025-vintage where possible)

### Lens 5(a) — Polycrisis cluster

| Source | URL | Key data |
|---|---|---|
| SIPRI Trends in World Military Expenditure 2025 | https://www.sipri.org/publications/2026/sipri-fact-sheets/trends-world-military-expenditure-2025 | 29 European NATO members $559B combined; Germany $114B (2.3% GDP, first since 1990); Spain $40.2B (first above 2% since 1994); Ukraine $84.1B (40% GDP); Russia 7.5% GDP |
| NATO Hague Summit Declaration June 2025 | https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2025/06/25/the-hague-summit-declaration | 5% GDP by 2035 (3.5% core defence + 1.5% security-related); Spain excluded; 2029 review |
| ReArm Europe / Readiness 2030 | https://www.consilium.europa.eu/en/policies/european-defence-readiness/ | €800B target; €150B SAFE loan adopted 27 May 2025; national escape clause activated for 17 member states (Feb 2026); 2025 EU defence expenditure €381B (+11% YoY, +62.8% vs 2020) |
| EU MFF Mid-Term Review 2024 | https://www.consilium.europa.eu/en/policies/eu-long-term-budget/timeline-mid-term-revision-of-the-long-term-budget-2021-2027/ | €64.6B reinforcement: Ukraine Facility €50B (€33B loans + €17B grants), migration €2B, emergency €1.5B. Bandwidth-tax proxy. Next MFF 2028–2034 proposal expected July 2025 |

### Lens 5(d) — Climate net position

| Source | URL | Key data |
|---|---|---|
| EEA European Climate Risk Assessment 2024 | https://www.eea.europa.eu/en/about/who-we-are/projects-and-cooperation-agreements/european-climate-risk-assessment | 36 climate risks identified, 8 particularly urgent; agriculture/food most-affected sector 2025; geographic classification (N/E/S/W Europe). 2nd assessment due 2028 |
| Munich Re NatCat 2025 Europe | https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/natural-disaster-figures-2025.html | Europe 2025 losses US$11B (low year vs $35B 10-yr average). **Spain wildfires: 400,000 hectares — 5x annual average.** Hailstorms FR/AT/DE $1.2B. 2024 Valencia floods: $31B Europe-wide |
| Cedefop 2025 Skills Forecast | https://www.cedefop.europa.eu/en/tools/skills-forecast | Country-level employment projections to 2035 by sector. Coal mining largest decrease; electricity jobs increase; engineering + administration service sectors increase. Direct input for net-climate-position adaptation-capacity scoring |
| Net-Zero Industry Act + Clean Industrial Deal Feb 2025 | https://commission.europa.eu/topics/competitiveness/green-deal-industrial-plan/net-zero-industry-act_en | €100B clean manufacturing allocation; 40% strategic net-zero technologies manufacturing capacity target by 2030; Net-Zero Industry Academies for upskilling/reskilling |
| IEA via NZIA reporting | https://www.europarl.europa.eu/topics/en/article/20231031STO08721/net-zero-industry-act-boosting-clean-technologies-in-europe | Clean energy jobs 6M → 14M by 2030 if global pledges met (global, not EU-direct — needs European triangulation) |

### Tooze framing context (parallel only, not load-bearing)

| Source | URL | Verdict |
|---|---|---|
| Tooze Chartbook 130 — Defining polycrisis (2022) | https://adamtooze.substack.com/p/chartbook-130-defining-polycrisis | Original definition: "the whole is even more dangerous than the sum of the parts." Mechanism = escalatory feedback loops + amplification. **Does NOT address institutional bandwidth.** Confirms Lens 5 mechanism is novel. |
| Tooze Chartbook 407 — Polycrisis revisited (Sep 2025) | https://adamtooze.substack.com/p/chartbook-407-polycrisis-revisited | "Polycrisis no longer seems so apt" as general descriptor. Pivoted to personal-agency framing (Trump, Netanyahu, MAGA as named actors). Distinct scale of analysis from Lens 5. |

---

## ❌ Still open

### Phil to surface (his existing access / institutional)

| Item | Why needed | Priority |
|---|---|---|
| **IISS Military Balance 2025** | Force-structure reading (not just budget) for Lens 5(a) | P1 — sharpens claims |
| **Tooze, *Shutdown* (2021), Ch on COVID institutional response** | Closest adjacent literature to bandwidth-saturation thesis | P2 — supports framing |
| **Freedman, *Command* (2022), Ch on bandwidth saturation** | Adjacent literature; closest direct treatment of crisis-decision-making bandwidth | P2 — supports framing |
| **Levinson, *The Box* 2nd Ed (2016), Ch 7 (container penetration tables)** | Retrofit v0.3 verification — already surfaced, not yet processed | P0 — blocks Lens 1 two-horizon spec |
| **Bessen, *Learning by Doing* (2015), banking chapter** | Retrofit v0.3 verification — already surfaced, not yet processed | P0 — blocks Lens 1 two-horizon spec |

### Brain to fetch (next session)

| Item | Why needed | Status |
|---|---|---|
| **Cedefop 2025 country-report PDFs** at country granularity | Net climate position adaptation-capacity scoring per country | Index page found; per-country PDFs need direct fetch |
| **L3 deeper page render verification** (`/cases.html`, `/findings.html` rendered output) | Confirm render gap scope before patching | Partially verified 2026-04-29; full sub-page audit pending |
| **Lieven Quincy Institute "Future of European Security" essay** | Multi-front conflict framing for Lens 5(a) | Located at quincyinst.org; specific essay needs direct fetch |
| **Anthropic Economic Index full dataset** via HuggingFace (`Anthropic/EconomicIndex`) | Per-occupation observed-exposure scores for Lens 1(c) calibration | Already verified top-line; raw dataset is v0.4 refinement |
| **ILO European green-jobs employment estimates** at country level | Climate Adaptation Boom (Scenario 2) bounding constraint | Framework located; specific country numbers not surfaced |

### Closed by deprioritisation

| Item | Why deprioritised | Date |
|---|---|---|
| BLS OES pre-1999 historical series | US data for European-focused project | 2026-04-14 |
| Cedefop Skills Forecast at ISCO 3-digit granularity | Cedefop public dataset only goes to 2-digit; solution is ESCO structural-weights distribution at L1 build time | 2026-04-14 |

---

## Sequencing

**Blocks Lens 1 two-horizon spec (P0):** Levinson Ch 7 + Bessen banking chapter.
**Blocks nothing else** — Lens 1 v1 (single-horizon), Lens 2, Lens 4, Lens 5 can all proceed with secured data.

**Lens 5 v1 ready to score** with secured data (a + b + c + d). v2 refinement when IISS + Cedefop country PDFs land.

---

## Bundle E session 1 captures (2026-04-29)

**Munich Re factsheets — design-level note for Phase 2 readers:**
Munich Re NatCAT-Stats factsheets publish **top-3 events per continent per year**, NOT systematic per-country totals. Smaller-loss events (below the top-3 threshold) are not enumerated and the country dropouts are by-design, not by missing-data. Joint-country events report joint figures only with no per-country split — treat joint figures as upper bounds for any single country. Confidence H only for sole-country events; M for joint; "no entry" ≠ "no event" — likely just below top-3 threshold.

**Munich Re Spain Valencia DANA 2024 — correction:**
Original fetch-list note "$31B Europe-wide" was the **2024 Europe AGGREGATE** (verified from 2024 factsheet continent-overview table: $31B overall / $14B insured / 400 fatalities Europe-wide). The Spain Valencia DANA event-specific figure is **$11B overall / $4.2B insured / 229 fatalities** (sole-country, 28-30.10.2024). Phase 2 readers: use $11B for ES Valencia, not $31B.

**IISS Military Balance 2025 — secured (P1 unblocked 2026-04-29):**
Three IISS Military Balance 2025 PDFs supplied by Phil and read directly: (a) launch-event editor's remarks, (b) Defence Spending and Procurement Trends chapter, (c) Russia and Eurasia chapter. Verbatim extracts compiled in `layer-6-iiss-military-balance-2025-extracts.md` covering: top-15 defence budgets 2024 USD figures (DE 86.0, UK 81.1, FR 64.0, IT 35.2, UA 28.4, PL 28.4); 2024 real-terms growth rates (Russia +41.9%, Europe +11.7%, DE +23.2%, China +7.4%); European procurement contracts (South Korea $18.03bn, Israel $6.85bn+, Embraer $4.18bn); Rheinmetall ammo capacity 70k→700k→1M by 2026; EU 2M rounds/yr target end-2025; nitrocellulose-supply dependency on China (direct Task 4 input); EPF disbursements (AM €10m, GE €30m frozen, MD €50m); Anduril Arsenal-2 abroad-optionality (direct Lens 4 jurisdictional-buffering input). Bandwidth-tax mechanism quoted directly by IISS analysts (Giegerich, McGerty) — independent attestation of Lens 5(a) mechanism without Tooze.
