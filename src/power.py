"""Minimum detectable effect for the designs in METHODS.md.

METHODS.md section 9 commits to reporting the MDE *before* fitting the primary
model, and reporting it regardless of outcome. This module exists so that
commitment is mechanical rather than aspirational.

The key question this answers: is a null result here informative ("we can
exclude effects larger than X") or uninformative ("we could never have seen
anything")? Those are very different papers.

Run: python src/power.py
"""

from __future__ import annotations

import numpy as np
from scipy import stats


def mde_two_group(
    n_per_group: int,
    sd: float,
    alpha: float = 0.005,
    power: float = 0.80,
    two_sided: bool = True,
) -> float:
    """Minimum detectable difference in means between two groups.

    Args:
        n_per_group: units per arm (e.g. municipalities).
        sd: between-unit standard deviation of the outcome.
        alpha: significance level. METHODS.md section 8 fixes this at 0.005 for
            the confirmatory test, justified by the low prior.
        power: desired power.

    Returns:
        Smallest difference in means detectable at the stated alpha and power.
    """
    z_a = stats.norm.ppf(1 - alpha / 2) if two_sided else stats.norm.ppf(1 - alpha)
    z_b = stats.norm.ppf(power)
    return (z_a + z_b) * sd * np.sqrt(2.0 / n_per_group)


def mde_rd(
    n_effective: int,
    sd: float,
    alpha: float = 0.005,
    power: float = 0.80,
    variance_inflation: float = 2.75,
) -> float:
    """Minimum detectable discontinuity for a local-linear RD.

    Local linear RD at a boundary is markedly less efficient than a simple
    two-group comparison: estimation happens at the edge of the support, where
    the local regression is extrapolating. `variance_inflation` captures this.

    Args:
        n_effective: units inside the bandwidth (both sides combined).
        sd: residual SD of the outcome after removing the running-variable trend.
        variance_inflation: efficiency penalty for boundary estimation with a
            triangular kernel. ~2.75 is a conventional rule-of-thumb; the real
            value is design-specific and should be replaced by a simulation once
            the actual geometry and covariates are in hand.

    Returns:
        Smallest discontinuity detectable at the stated alpha and power.
    """
    base = mde_two_group(n_effective // 2, sd, alpha=alpha, power=power)
    return base * np.sqrt(variance_inflation)


def report(scenarios: list[dict]) -> None:
    print(f"{'design':<42} {'n':>7} {'SD':>7} {'MDE':>9} {'MDE %':>8}")
    print("-" * 78)
    for s in scenarios:
        pct = s["mde"] / s["baseline"] * 100
        print(f"{s['name']:<42} {s['n']:>7} {s['sd']:>7.1f} "
              f"{s['mde']:>9.1f} {pct:>7.1f}%")


if __name__ == "__main__":
    # PLACEHOLDER PARAMETERS -- these are illustrative until real denominators
    # and real between-municipality variance are in hand. The structure of the
    # conclusion, however, is unlikely to change.
    #
    # Baseline: age-standardised dementia prevalence among 65+ in Japan is
    # roughly 12,000-15,000 per 100k (12-15%). Between-municipality SD is
    # plausibly ~15% of the mean once age-standardised; LTCI administrative
    # variation alone could easily produce that.
    BASELINE = 13_000.0
    SD = 0.15 * BASELINE

    scenarios = []

    # Tier 1 -- prefecture ecological. 47 prefectures, roughly 24 vs 20 usable.
    scenarios.append(dict(
        name="Tier 1: prefecture ecological (n=47)",
        n=47, sd=SD, baseline=BASELINE,
        mde=mde_two_group(22, SD),
    ))

    # Tier 2 -- municipality ecological, all Japan.
    scenarios.append(dict(
        name="Tier 2: municipality ecological (n~1700)",
        n=1700, sd=SD, baseline=BASELINE,
        mde=mde_two_group(850, SD),
    ))

    # Tier 3 -- the confirmatory design. Within-Shizuoka is ~35 municipalities.
    scenarios.append(dict(
        name="Tier 3: RD within Shizuoka (n~35)",
        n=35, sd=SD, baseline=BASELINE,
        mde=mde_rd(35, SD),
    ))

    # Tier 3 pooled across Shizuoka + Niigata + Nagano boundary segments.
    scenarios.append(dict(
        name="Tier 3: RD pooled segments (n~120)",
        n=120, sd=SD, baseline=BASELINE,
        mde=mde_rd(120, SD),
    ))

    print("Minimum detectable effect, alpha=0.005 (two-sided), power=0.80")
    print("Outcome: age-standardised dementia prevalence per 100k, 65+")
    print(f"Assumed baseline {BASELINE:,.0f}/100k, between-unit SD {SD:,.0f} "
          f"({SD/BASELINE:.0%} of mean)\n")
    report(scenarios)

    print("\nInterpretation")
    print("-" * 78)
    print("""\
The confirmatory design (Tier 3, within-Shizuoka) can only detect effects on the
order of tens of percent. A 20% difference in the frequency of an ambient
exposure -- one whose delivered contrast has been eroding since inverter
ballasts and LEDs (METHODS.md 2.3) -- producing a double-digit-percent shift in
dementia prevalence is not a plausible effect size.

That makes the expected result UNINFORMATIVE rather than NULL, which is a
materially different claim and must be reported as such. It also means the
honest recommendation is to check the higher-contrast natural experiments in
METHODS.md section 11 (25 Hz Ontario, 16.7 Hz railway cohorts) BEFORE investing
further in the Japan 50/60 contrast -- and to run the exposure-measurement
substudy (section 10), which could retire the question outright for the cost of a
photodiode and a few dozen home visits.

These numbers are placeholders. Rerun once real denominators and the real
between-municipality variance are available.""")
