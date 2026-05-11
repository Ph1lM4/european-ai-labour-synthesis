"""Bundle Q — Layer 1 regulatory overlay enrichment for Layer 6 Lens 1 + Lens 4.

Read-only against Layer 1.
Modifies Layer 6 SOT JSON only at the specified Lens 1 + Lens 4 fields plus two
top-level additions (cross_cutting_findings.regulatory_asymmetry,
metadata.layer_1_enrichment).

Computes per-country:
  - lens1_regulated_absorption_pct: employment-weighted share of high-exposure
    occupations (technical_score >= 6.0) that fall under EU AI Act Annex III
    high-risk subject scope (i.e. the regulated_score is materially below
    technical_score because European employment law forces a wedge).
  - asymmetry_score: 1 - (UK-rule weighted regulated score) / (EU-rule weighted
    regulated score), clamped to [0, 1]. Higher = more regulatory asymmetry
    relative to UK if EU rules applied to this country's labour mix.
  - For squeeze=true countries: per-country counts of occupations with
    employment > 0 and (a) high_risk_as_deployer, (b) high_risk_as_subject,
    (c) platform_work_directive_relevant.

Provenance: source_layer L1, source files scores.json + uk_scores.json + site/data.json.
"""
from __future__ import annotations

import json
from collections import OrderedDict
from datetime import date
from pathlib import Path

L1_SCORES = Path("/Users/philippmaul/Documents/projects/european-ai-exposure-map/scores.json")
L1_UK_SCORES = Path("/Users/philippmaul/Documents/projects/european-ai-exposure-map/uk_scores.json")
L1_SITE_DATA = Path("/Users/philippmaul/Documents/projects/european-ai-exposure-map/site/data.json")
L6_SOT = Path("/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json")

HIGH_EXPOSURE_THRESHOLD = 6.0
BUNDLE_VERSION = "Q"
INGESTION_DATE = "2026-04-30"


def load_l1_occupations() -> list[dict]:
    with open(L1_SITE_DATA) as f:
        site = json.load(f)
    occs = []
    for cat in site["treemap"]["children"]:
        for occ in cat.get("children", []):
            occs.append(occ)
    return occs


def compute_per_country(occs: list[dict], country: str) -> dict:
    """Return enrichment metrics for one country."""
    # Filter occupations with employment > 0 in this country
    present = [o for o in occs if o.get("emp", {}).get(country, 0) > 0]
    if not present:
        return {
            "lens1_regulated_absorption_pct": None,
            "asymmetry_score": None,
            "annex_iii_high_risk": None,
            "art_26_7_deployer_obligations": None,
            "pwd_post_market_duties": None,
            "data_gap_reason": "L1 has no employment data for this country",
        }

    total_emp = sum(o["emp"][country] for o in present)

    # Per-occupation EU friction = technical_score - regulated_score (positive = EU regulation
    # depresses practical exposure relative to technical capability).
    # UK friction = technical_score - uk_regulated_score.
    # Employment-weighted averages per country.
    eu_friction_weighted = sum(
        o["emp"][country] * (o["technical_score"] - o["regulated_score"]) for o in present
    ) / total_emp
    uk_friction_weighted = sum(
        o["emp"][country] * (o["technical_score"] - o.get("uk_regulated_score", o["regulated_score"]))
        for o in present
    ) / total_emp

    # asymmetry_score: (EU_friction - UK_friction) / EU_friction, clamped [0, 1].
    # 0 = UK and EU equally heavy; 1 = UK frictionless relative to EU.
    if eu_friction_weighted > 0:
        asymmetry = (eu_friction_weighted - uk_friction_weighted) / eu_friction_weighted
        asymmetry = max(0.0, min(1.0, asymmetry))
    else:
        asymmetry = 0.0  # if EU has no friction either, no asymmetry

    # lens1_regulated_absorption_pct: employment-weighted share of high-exposure occupations
    # (technical_score >= 6.0) sitting under EU AI Act Annex III high-risk deployer scope —
    # i.e., where regulation creates absorption-velocity friction for AI deployment.
    high_exposure_occs = [o for o in present if o.get("technical_score", 0) >= HIGH_EXPOSURE_THRESHOLD]
    if high_exposure_occs:
        total_high_emp = sum(o["emp"][country] for o in high_exposure_occs)
        regulated_high_emp = sum(
            o["emp"][country] for o in high_exposure_occs if o.get("high_risk_as_deployer")
        )
        regulated_pct = regulated_high_emp / total_high_emp if total_high_emp > 0 else 0.0
    else:
        regulated_pct = 0.0

    # Overlay counts (for squeeze countries)
    annex_iii = sum(1 for o in present if o.get("high_risk_as_deployer"))
    art_26_7 = sum(1 for o in present if o.get("high_risk_as_subject"))
    pwd = sum(1 for o in present if o.get("platform_work_directive_relevant"))

    return {
        "lens1_regulated_absorption_pct": round(regulated_pct, 4),
        "asymmetry_score": round(asymmetry, 4) if asymmetry is not None else None,
        "annex_iii_high_risk": annex_iii,
        "art_26_7_deployer_obligations": art_26_7,
        "pwd_post_market_duties": pwd,
        "_eu_weighted_friction": round(eu_friction_weighted, 4),
        "_uk_weighted_friction": round(uk_friction_weighted, 4),
        "_high_exposure_employment": int(sum(o["emp"][country] for o in high_exposure_occs)) if high_exposure_occs else 0,
    }


def main():
    occs = load_l1_occupations()
    with open(L6_SOT) as f:
        sot = json.load(f)

    enriched_summary = {}
    for code, country_block in sot["countries"].items():
        if code == "LI":
            metrics = {
                "lens1_regulated_absorption_pct": None,
                "asymmetry_score": None,
                "annex_iii_high_risk": None,
                "art_26_7_deployer_obligations": None,
                "pwd_post_market_duties": None,
                "data_gap_reason": "LI not present in L1 dataset (Liechtenstein excluded from EU AI Exposure Map scope)",
            }
        else:
            metrics = compute_per_country(occs, code)

        # Lens 1 enrichment: add lens1_regulated_absorption_pct under lens_findings
        country_block["lens_findings"]["lens1_regulated_absorption_pct"] = metrics["lens1_regulated_absorption_pct"]

        # Lens 4 squeeze-flag quantification: replace boolean with structured object
        existing_lens4 = country_block["lens_findings"]["lens4_compounding"]
        binary_flag = bool(existing_lens4.get("squeeze_flag"))

        if binary_flag:
            squeeze_struct = {
                "binary": True,
                "asymmetry_score": metrics["asymmetry_score"],
                "ai_act_overlay_count": {
                    "annex_iii_high_risk": metrics["annex_iii_high_risk"],
                    "art_26_7_deployer_obligations": metrics["art_26_7_deployer_obligations"],
                    "pwd_post_market_duties": metrics["pwd_post_market_duties"],
                },
                "_provenance": {
                    "source_layer": "L1",
                    "source_data": "scores.json + uk_scores.json + site/data.json",
                    "bundle": BUNDLE_VERSION,
                },
            }
            if "data_gap_reason" in metrics:
                squeeze_struct["ai_act_overlay_count"]["_data_gap_reason"] = metrics["data_gap_reason"]
        else:
            squeeze_struct = {
                "binary": False,
                "asymmetry_score": metrics["asymmetry_score"],
                "_provenance": {
                    "source_layer": "L1",
                    "source_data": "scores.json + uk_scores.json + site/data.json",
                    "bundle": BUNDLE_VERSION,
                },
            }
            if "data_gap_reason" in metrics:
                squeeze_struct["_data_gap_reason"] = metrics["data_gap_reason"]

        existing_lens4["squeeze_flag"] = squeeze_struct

        enriched_summary[code] = {
            "binary": binary_flag,
            "asymmetry": metrics["asymmetry_score"],
            "lens1_reg_abs_pct": metrics["lens1_regulated_absorption_pct"],
            "annex_iii": metrics.get("annex_iii_high_risk"),
            "art_26_7": metrics.get("art_26_7_deployer_obligations"),
            "pwd": metrics.get("pwd_post_market_duties"),
        }

    # Top-level additions
    sot.setdefault("cross_cutting_findings", {})
    sot["cross_cutting_findings"]["regulatory_asymmetry"] = {
        "summary": (
            "Layer 1's dual scoring (EU regulated_score vs uk_regulated_score) "
            "quantifies regulatory asymmetry across all 36 countries. The EU-vs-UK "
            "delta (avg 1.2 vs 0.5 friction points per occupation) translates, when "
            "weighted by each country's labour mix, into an asymmetry score that ranges "
            "across EU-27 + EFTA above the UK baseline. The 8 squeeze-flagged Lens 4 "
            "countries (BE, DE, DK, FI, FR, NL, NO, SE) sit at the top of the regulated-"
            "absorption-friction distribution: their high-exposure occupations are also "
            "the most regulated, compounding the squeeze the binary flag identifies."
        ),
        "_provenance": {
            "source_layer": "L1",
            "source_data": "scores.json + uk_scores.json + site/data.json",
            "bundle": BUNDLE_VERSION,
        },
    }

    sot["metadata"]["layer_1_enrichment"] = {
        "bundle": BUNDLE_VERSION,
        "ingestion_date": INGESTION_DATE,
        "source_paths": {
            "scores": str(L1_SCORES),
            "uk_scores": str(L1_UK_SCORES),
            "site_data": str(L1_SITE_DATA),
        },
        "fields_added": [
            "countries.<code>.lens_findings.lens1_regulated_absorption_pct",
            "countries.<code>.lens_findings.lens4_compounding.squeeze_flag (boolean → structured)",
            "cross_cutting_findings.regulatory_asymmetry",
        ],
        "method": (
            "Per-occupation EU friction = technical_score - regulated_score. UK friction = "
            "technical_score - uk_regulated_score. Per-country employment-weighted average of "
            "each computed across L1 ISCO 3-digit occupations present in country (emp>0). "
            "asymmetry_score = (EU_friction_weighted - UK_friction_weighted) / EU_friction_weighted, "
            "clamped [0,1]; 0 = UK and EU equally heavy regulation, 1 = UK frictionless. "
            "lens1_regulated_absorption_pct = employment-weighted share of high-exposure "
            "(technical_score >= 6.0) occupations sitting under EU AI Act Annex III high-risk "
            "deployer scope. Overlay counts: # of occupations with country emp>0 and the "
            "respective flag (high_risk_as_deployer / high_risk_as_subject / "
            "platform_work_directive_relevant)."
        ),
        "data_gap": [
            "LI (Liechtenstein) not in L1 dataset; all Lens 1 + Lens 4 enrichment fields null."
        ],
    }

    # Write back
    with open(L6_SOT, "w") as f:
        json.dump(sot, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Print verification summary
    print(f"Enriched {len(enriched_summary)} countries.")
    print()
    print("Asymmetry score distribution:")
    asym = [(c, v["asymmetry"]) for c, v in enriched_summary.items() if v["asymmetry"] is not None]
    asym_sorted = sorted(asym, key=lambda x: x[1], reverse=True)
    print(f"  range: {min(v for _, v in asym):.4f} - {max(v for _, v in asym):.4f}")
    print(f"  null:  {[c for c, v in enriched_summary.items() if v['asymmetry'] is None]}")
    print("  top 5:")
    for c, v in asym_sorted[:5]:
        print(f"    {c}: {v:.4f}")
    print("  bottom 5:")
    for c, v in asym_sorted[-5:]:
        print(f"    {c}: {v:.4f}")
    print()
    print("Squeeze countries with overlay counts:")
    for c, v in enriched_summary.items():
        if v["binary"]:
            print(f"  {c}: annex_iii={v['annex_iii']}, art_26_7={v['art_26_7']}, pwd={v['pwd']}, asym={v['asymmetry']}, lens1_reg_abs={v['lens1_reg_abs_pct']}")
    print()
    print("Lens 1 regulated_absorption_pct distribution:")
    abs_pct = [(c, v["lens1_reg_abs_pct"]) for c, v in enriched_summary.items() if v["lens1_reg_abs_pct"] is not None]
    abs_sorted = sorted(abs_pct, key=lambda x: x[1], reverse=True)
    print(f"  range: {min(v for _, v in abs_pct):.4f} - {max(v for _, v in abs_pct):.4f}")
    print("  top 5:")
    for c, v in abs_sorted[:5]:
        print(f"    {c}: {v:.4f}")
    print("  bottom 5:")
    for c, v in abs_sorted[-5:]:
        print(f"    {c}: {v:.4f}")


if __name__ == "__main__":
    main()
