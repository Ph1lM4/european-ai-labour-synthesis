"""
Bundle R: Layer 5 Reskilling Math enrichment of Layer 6 SOT JSON.

Surgical edits to layer-6-deliverable-data.json:
  1) Add per-country `lens1_a_to_c_transition_rate_pct` keyed off `_system_p1`
     - DACH (DE/AT/CH) gets country-specific reform-velocity composite augment
  2) Add top-level `cross_cutting_findings.reskilling_capacity_gap`
     (7.55M / 450K / 15-year math + diagnostic framework)
  3) Add per-country `lens5_internal_transition_diagnostic` (null + Phase-5+ flag —
     L5 carries the framework but no country-level data)
  4) Add `metadata.layer_5_enrichment` block

All numbers traced to L5 sources (reskilling-data.json + a_to_c_rates.csv + dach.html
+ README + lenses.html). No fabrication; all _provenance recorded.
"""
import json
from collections import OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOT_PATH = ROOT / "layer-6-deliverable-data.json"
L5_DATA = Path("/Users/philippmaul/Documents/projects/european-reskilling-map/site/reskilling-data.json")
L5_AC_CSV = Path("/Users/philippmaul/Documents/projects/european-reskilling-map/scripts/output/a_to_c_rates.csv")

# ---------------------------------------------------------------------------
# L5 system bands per `systems` array in reskilling-data.json (headline) +
# central derived per a_to_c_rates.csv (Bertheau-anchored). Where headline ≠
# derived, we surface both so Lens 1 readers see the divergence.
# ---------------------------------------------------------------------------
SYSTEM_BANDS = {
    "Nordic flexicurity": {
        "low": 8, "high": 12, "central_derived": 9.9,
        "delta_central_vs_mid": -0.1,
        "source_alignment": "headline ~= derived",
    },
    "Germanic Dual": {
        "low": 3, "high": 6, "central_derived": 7.9,
        "delta_central_vs_mid": 3.4,
        "source_alignment": "derived above headline mid-band by 3.4pp (L5-flagged review delta)",
    },
    "Continental Corporatist": {
        "low": 5, "high": 8, "central_derived": 6.9,
        "delta_central_vs_mid": 0.4,
        "source_alignment": "headline ~= derived",
    },
    "Liberal Market": {
        "low": 5, "high": 8, "central_derived": 3.2,
        "delta_central_vs_mid": -3.3,
        "source_alignment": "derived below headline mid-band by 3.3pp (L5-flagged review delta; README key-findings publishes derived 2.8–3.6 as canonical for UK)",
    },
    "Central/Eastern European": {
        "low": 2, "high": 5, "central_derived": 3.3,
        "delta_central_vs_mid": -0.2,
        "source_alignment": "headline ~= derived",
    },
    "Southern European": {
        "low": 2, "high": 5, "central_derived": 4.8,
        "delta_central_vs_mid": 1.3,
        "source_alignment": "derived above headline mid-band by 1.3pp",
    },
    # The L6 _system_p1 tag for BA/MK/RS/TR contains the encoded definition
    "candidate-baseline (CEE+SE weighted avg, both 2–5%/yr midpoint 3.5%)": {
        "low": 2, "high": 5, "central_derived": 3.5,
        "delta_central_vs_mid": 0.0,
        "source_alignment": "weighted avg of CEE + Southern European bands per _system_p1 tag definition",
    },
}

# DACH per-country reform-velocity composite per dach.html caption + README
# (0–10 scale: veto-player 0–5 + recent-reform 0–5)
DACH_REFORM_VELOCITY = {
    "DE": {"composite": 5, "veto_player": 2, "recent_reform": 3,
           "note": "federal + 16 Länder + Sozialpartner ≈ 3 effective blocks; Qualifizierungsgeld 2024 passed and operational"},
    "AT": {"composite": 3, "veto_player": 3, "recent_reform": 0,
           "note": "federal + 9 Länder + Sozialpartner ≈ 2 effective blocks; Bildungskarenz operational but 2026 tightening reads as regression, not reform"},
    "CH": {"composite": 1, "veto_player": 1, "recent_reform": 0,
           "note": "26 cantonal autonomies + WeBiG subsidiarity caps federal action; no major reskilling-system reform 2017–2026"},
    # LI tagged Germanic Dual but not in DACH composite; flag.
    "LI": {"composite": None, "veto_player": None, "recent_reform": None,
           "note": "Liechtenstein tagged Germanic Dual via _system_p1 but L5 dach.html composite covers DE/AT/CH only — Phase 5+ acquisition"},
}

# DACH: L5 dach.html S2 (Time × cost × reform velocity) augments
DACH_TIME_COST = {
    "DE": {"time_to_first_graduate_yr": 4.5, "cost_per_transition_eur_k": 38,
           "note": "Neuordnung 3–5yr + 24mo Umschulung; full Umschulung + income support"},
    "AT": {"time_to_first_graduate_yr": 3.5, "cost_per_transition_eur_k": 28,
           "note": "Bildungskarenz 12mo + FH 2–3yr; AlV + training"},
    "CH": {"time_to_first_graduate_yr": 3.0, "cost_per_transition_eur_k": 18,
           "note": "24mo EFZ adult + cantonal assessment; individual/employer bear most under WeBiG"},
}


def build_lens1_field(country_code: str, system_p1: str) -> dict:
    bands = SYSTEM_BANDS.get(system_p1)
    if bands is None:
        raise ValueError(f"Unmapped _system_p1 for {country_code}: {system_p1!r}")
    out = OrderedDict()
    out["band_low_pct"] = bands["low"]
    out["band_high_pct"] = bands["high"]
    out["central_derived_pct"] = bands["central_derived"]
    out["system_p1_match"] = system_p1
    out["delta_central_vs_mid_pp"] = bands["delta_central_vs_mid"]
    out["source_alignment"] = bands["source_alignment"]

    if country_code in DACH_REFORM_VELOCITY:
        rv = DACH_REFORM_VELOCITY[country_code]
        out["country_specific"] = True
        out["reform_velocity_composite_0_10"] = rv["composite"]
        out["reform_velocity_decomposition"] = {
            "veto_player_factor_0_5": rv["veto_player"],
            "recent_reform_factor_0_5": rv["recent_reform"],
            "rationale": rv["note"],
        }
        if country_code in DACH_TIME_COST:
            tc = DACH_TIME_COST[country_code]
            out["time_to_first_graduate_yr"] = tc["time_to_first_graduate_yr"]
            out["public_cost_per_transition_eur_k"] = tc["cost_per_transition_eur_k"]
            out["dach_time_cost_note"] = tc["note"]
    else:
        out["country_specific"] = False
        out["reform_velocity_composite_0_10"] = None

    out["_provenance"] = {
        "source_layer": "L5",
        "source_data": [
            "reskilling-data.json#systems (headline bands)",
            "scripts/output/a_to_c_rates.csv (derived central, Bertheau IZA DP 15033 anchor)",
        ] + (["site/dach.html (DACH reform-velocity composite + time/cost)"] if country_code in DACH_REFORM_VELOCITY else []),
        "bundle": "R",
        "ingestion_date": "2026-04-30",
    }
    return out


def build_capacity_gap_block() -> dict:
    return OrderedDict([
        ("deep_reskilling_need_eu27_uk_m", 7.55),
        ("upskilling_need_eu27_m", 15.0),
        ("partial_change_need_eu27_m", 7.5),
        ("net_total_need_eu27_2035_m", 30.05),
        ("gross_high_exposure_eu27_m", 38.72),
        ("retirement_offset_eu27_2035_m", 8.67),
        ("annual_throughput_total_m", 3.34),
        ("annual_throughput_net_new_m", 0.45),
        ("implied_backlog_years", 15),
        ("speed_gap_years", "5-9"),
        ("channel_breakdown_per_year", {
            "university_adults_30plus": 380000,
            "vet_apprenticeships_adult": 880000,
            "corporate_l_and_d": 1250000,
            "government_almp": 650000,
            "bootcamps_microcredentials": 180000,
            "total": 3340000,
            "consumed_by_baseline_churn_note": "≈2.89M of 3.34M consumed by baseline economic churn (Eurostat lfsa_etpgan tenure-under-1yr proxy); ~450K net new available for AI transitions",
        }),
        ("class_iii_implication", "Reskilling pathway is structurally insufficient for Class III countries: baseline ALMP + VET capacity already saturated by churn, leaving ~450K/yr against a 7.55M deep-reskilling need. Even allocating disproportionately to Class III absorbs only marginal share without channel expansion. Anchors §4 'reskilling pathway is structurally insufficient' framing in Executive deliverable."),
        ("ai_response_lag_years", "AI disrupts in 1–3yr; European VET/university systems respond in 5–9yr; structural lag 3–5yr for admin clerks, customer service, writers/translators"),
        ("mooc_completion_rate_pct", "3-15"),
        ("mooc_caveat", "MOOC channel cannot serve as a primary reskilling channel at observed completion rates"),
        ("context", "These are the load-bearing capacity numbers behind the 'absorption is structurally bounded' claim. The ~450K net new annual capacity divided into the 7.55M deep cohort yields the 15-year backlog. The 5–9yr speed gap is between AI-side disruption velocity and reskilling-system response velocity. Both inputs anchor Class III §3 in the Executive doc."),
        ("_provenance", {
            "source_layer": "L5",
            "source_data": [
                "reskilling-data.json#reskilling_gap (7.55M / 15M / 7.5M / 30.05M / 38.72M / 8.67M)",
                "reskilling-data.json#capacity (3.34M / 0.45M / 15yr)",
                "reskilling-data.json#speed_gap (5–9yr lag)",
                "scripts/output/channel_throughput.csv (channel breakdown)",
                "scripts/output/net_new_capacity.csv (450K net new derivation)",
                "scripts/output/speed_gap.csv (occupational lag detail)",
                "README.md Methodology §1–§3 + sources.html Derivation Appendix A–H",
            ],
            "bundle": "R",
            "ingestion_date": "2026-04-30",
        }),
    ])


def build_internal_transition_diagnostic() -> dict:
    """Country-level — null for all 36 since L5 carries the FRAMEWORK, not country-level data."""
    return OrderedDict([
        ("value", None),
        ("acquisition_status", "L5-framework-only; no country-level data; Phase 5+ acquisition target"),
        ("framework_citation", "L5 lenses.html §4 'Candidate diagnostic metric — internal transition speed vs external turnover'"),
        ("operational_definition", "internal transition speed = elapsed time from capability formation (training completion / certification) to internal role change using that capability; external turnover = rate at which newly-capable workers leave the firm before internal translation. Where external turnover materially exceeds internal transition speed, transition architecture is broken (firm pays to produce capability; market captures it)."),
        ("data_collection_blocker", "Requires firm-level linked HR data (training completion + internal posting outcomes + tenure-at-exit, joined on worker identity). Most firms track separately; most aggregate studies have no line of sight."),
    ])


def build_diagnostic_framework_block() -> dict:
    """Top-level cross_cutting addition — the BR-22-validated diagnostic that
    Layer 6 currently misses entirely (per Bundle R rationale)."""
    return OrderedDict([
        ("metric_name", "Internal transition speed vs external turnover"),
        ("scope", "firm-level, not country-level — sits orthogonal to aggregate Lens 1 absorption"),
        ("framework_citation", "L5 lenses.html §4 (candidate diagnostic) + L5 systems.html (referenced as the constraint that actually binds)"),
        ("squeeze_flag_relevance", "Firms whose internal-transition speed is materially slower than external turnover are at higher squeeze risk regardless of programme participation. Aggregate reskilling KPIs (completion rates, participation %) do not capture this; two firms with identical programme metrics can produce opposite ROIs if their internal-transition-to-external-turnover ratios differ by an order of magnitude."),
        ("br_22_provenance", {
            "validation_event": "Stefanie Haslauer LinkedIn thread, 2026-04-15",
            "validation_pattern": "BR-22 external-human variant (5-round adversarial pushback from external domain expert with coherent thesis arc)",
            "outcome": "Metric crystallised at round 5 as the testable diagnostic that solo-brain and claude.ai rounds had not surfaced. Confirms BR-22 generalises beyond Claude-Claude critique cycles.",
            "memory_anchor": "MEMORY.md → 'BR-22 external-human variant (Apr 15)'",
        }),
        ("layer_5_acquisition_status", "framework-only; country-level data is Phase 5+ acquisition target. L5 README contributing-section explicitly invites firm-level data on this metric."),
        ("layer_6_application_note", "Use as squeeze-flag interpretive lens for Class III countries even where country-level data is absent: the metric explains why programme-design comparisons in §3 explain less variance than they appear to. Carry as caveat in §4 reskilling-pathway framing."),
        ("_provenance", {
            "source_layer": "L5",
            "source_data": [
                "site/lenses.html §4 (candidate diagnostic metric definition)",
                "site/systems.html (constraint-that-binds reference)",
                "README.md Contributing section (firm-sample acquisition invite)",
            ],
            "br_22_anchor": "Second Brain MEMORY.md / contexts/behavioral-rules-scoped.md TF-A → BR-22 (adversarial-iteration validation)",
            "bundle": "R",
            "ingestion_date": "2026-04-30",
        }),
    ])


def build_metadata_block() -> dict:
    return OrderedDict([
        ("source_layer", "L5"),
        ("source_paths", [
            "/Users/philippmaul/Documents/projects/european-reskilling-map/site/reskilling-data.json",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/scripts/output/a_to_c_rates.csv",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/scripts/output/channel_throughput.csv",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/scripts/output/net_new_capacity.csv",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/scripts/output/speed_gap.csv",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/site/dach.html",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/site/lenses.html",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/site/systems.html",
            "/Users/philippmaul/Documents/projects/european-reskilling-map/README.md",
        ]),
        ("ingestion_date", "2026-04-30"),
        ("bundle_version", "R-v1"),
        ("modification_surface", [
            "countries[*].lens_findings.lens1_a_to_c_transition_rate_pct (added)",
            "countries[*].lens_findings.lens5_internal_transition_diagnostic (added; null + framework-only for all 36)",
            "cross_cutting_findings.reskilling_capacity_gap (added)",
            "cross_cutting_findings.internal_transition_diagnostic_framework (added)",
            "metadata.layer_5_enrichment (added; this block)",
        ]),
        ("composition_gaps_surfaced", [
            "Liberal Market (UK/IE): L5 systems.json carries 5–8 headline; L5 a_to_c_rates.csv derives 2.8–3.6 (Δ=−3.3pp); README key-findings publishes derived as canonical for UK. SOT carries both; Lens 1 readers should treat 5–8 as upper bound and 2.8–3.6 as the L5-recommended central.",
            "Germanic Dual (DE/AT/CH/LI): L5 derives 7.9 central vs 3–6 headline (Δ=+3.4pp); reform-velocity composite (DE 5 / AT 3 / CH 1) is a country-specific override but on a different dimension (reform velocity 0–10, not transition rate). LI tagged Germanic Dual but not in DACH composite — Phase 5+ acquisition.",
            "Internal-transition diagnostic: L5 carries framework only (lenses.html §4). No country-level data. All 36 countries flagged null with Phase 5+ acquisition pointer.",
            "Western Balkans + Turkey (BA/MK/RS/TR): L6 _system_p1 tag = 'candidate-baseline (CEE+SE weighted avg)'. Treated as 2–5 band / 3.5 central per tag definition. L5 has no first-principles derivation for these — Phase 5+ acquisition recommended.",
            "Bertheau IZA DP 15033 base rate is 5y re-employment (not 5y A→C). Cross-zone fraction layered on top. Headline bands are Bertheau base × system-model adjustment; derived central is direct (re-employment × ALMP-spend × Zone-C share).",
        ]),
    ])


def main():
    with open(SOT_PATH) as f:
        sot = json.load(f)

    # 1) Per-country Lens 1 + Lens 5 fields
    countries_modified = 0
    transition_summary = []
    diagnostic_coverage = []
    for code in sorted(sot["countries"].keys()):
        country = sot["countries"][code]
        sys_p1 = country.get("_system_p1")
        lens1 = build_lens1_field(code, sys_p1)
        diag = build_internal_transition_diagnostic()

        if "lens_findings" not in country:
            country["lens_findings"] = {}
        country["lens_findings"]["lens1_a_to_c_transition_rate_pct"] = lens1
        country["lens_findings"]["lens5_internal_transition_diagnostic"] = diag

        # provenance pointers
        country.setdefault("_provenance", {})
        country["_provenance"]["lens1_a_to_c_transition_rate_pct"] = {
            "source_bundle": "Bundle R",
            "source_field": "L5 reskilling-data.json#systems + a_to_c_rates.csv",
        }
        country["_provenance"]["lens5_internal_transition_diagnostic"] = {
            "source_bundle": "Bundle R",
            "source_field": "L5 lenses.html §4 (framework-only; country-level data is Phase 5+ target)",
        }

        countries_modified += 1
        transition_summary.append((code, sys_p1, lens1["band_low_pct"], lens1["band_high_pct"], lens1["central_derived_pct"]))
        diagnostic_coverage.append((code, diag["acquisition_status"]))

    # 2) Top-level cross-cutting blocks
    sot["cross_cutting_findings"]["reskilling_capacity_gap"] = build_capacity_gap_block()
    sot["cross_cutting_findings"]["internal_transition_diagnostic_framework"] = build_diagnostic_framework_block()

    # 3) Metadata block
    sot["metadata"]["layer_5_enrichment"] = build_metadata_block()

    # Write
    with open(SOT_PATH, "w") as f:
        json.dump(sot, f, indent=2, ensure_ascii=False)

    print(f"OK: {countries_modified} countries enriched")
    print(f"OK: cross_cutting_findings.reskilling_capacity_gap added")
    print(f"OK: cross_cutting_findings.internal_transition_diagnostic_framework added")
    print(f"OK: metadata.layer_5_enrichment added")
    return transition_summary, diagnostic_coverage


if __name__ == "__main__":
    main()
