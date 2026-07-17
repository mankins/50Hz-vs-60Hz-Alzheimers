"""Primary and placebo analyses.

Run: python src/04_analysis.py

Consumes the canonical schemas in schema.py. Refuses to run on data that does
not conform -- in particular it rejects coarse age bands, because accepting them
would reintroduce exactly the confounding this project exists to remove.

Order of operations is fixed by METHODS.md and enforced here:
  1. Report the MDE. Before anything is fitted.
  2. Balance tests. If covariates jump at the boundary, stop.
  3. Placebo outcomes. If they jump at the boundary, stop.
  4. Primary outcome. Only reached if 2 and 3 pass.

Step 4 is deliberately gated. It is not possible to peek at the primary estimate
first and then decide whether the placebos matter.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

from agestd import STANDARD_BANDS, standardise_frame
from power import mde_rd, mde_two_group

ROOT = Path(__file__).resolve().parent.parent
PROCESSED = ROOT / "data" / "processed"
REFERENCE = ROOT / "data" / "reference"
OUTPUT = ROOT / "output"

ALPHA_CONFIRMATORY = 0.005   # METHODS.md section 8
ALPHA_PLACEBO = 0.05


def load_or_exit(path: Path, what: str) -> pd.DataFrame:
    if not path.exists():
        print(f"\nMISSING: {path.relative_to(ROOT)}")
        print(f"  Needed for: {what}")
        print(f"  See data/raw/PROVENANCE.md for how to obtain it.")
        sys.exit(2)
    return pd.read_csv(path, dtype={"area_code": str})


def tier1_prefecture(outcome: pd.DataFrame, freq: pd.DataFrame,
                     reference_pop: pd.Series) -> pd.DataFrame:
    """Descriptive only. NOT confirmatory -- see METHODS.md section 3.

    The single question this answers: does the crude gap in the original chart
    survive age standardisation? Our expectation is that it does not.
    """
    pref = outcome[
        (outcome.area_level == "prefecture")
        & (outcome.outcome == "dementia")
        & (outcome.sex == "both")
    ]
    if pref.empty:
        raise ValueError("no prefecture-level dementia rows found")

    year = int(pref.year.max())
    pref = pref[pref.year == year]

    asr = standardise_frame(
        pref, group_col="area_code", reference=reference_pop,
    ).merge(freq[["area_code", "area_name", "frequency_hz"]], on="area_code")

    print(f"\nTier 1 -- prefecture ecological, year {year} (DESCRIPTIVE ONLY)")
    print("-" * 74)

    for label, col in [("crude", "crude_rate"), ("age-standardised", "asr")]:
        g = asr.groupby("frequency_hz")[col].agg(["mean", "std", "count"])
        print(f"\n  {label} rate per 100k:")
        for f in ["50", "60", "mixed"]:
            if f in g.index:
                r = g.loc[f]
                print(f"    {f:>5} Hz  n={int(r['count']):2d}  "
                      f"mean={r['mean']:8,.0f}  sd={r['std']:7,.0f}")
        if {"50", "60"} <= set(g.index):
            ratio = g.loc["60", "mean"] / g.loc["50", "mean"]
            print(f"    60/50 ratio: {ratio:.3f}  ({(ratio-1)*100:+.1f}%)")

    # The headline diagnostic: how much of any crude gap was age structure?
    if {"50", "60"} <= set(asr.frequency_hz.unique()):
        c = asr.groupby("frequency_hz").crude_rate.mean()
        a = asr.groupby("frequency_hz").asr.mean()
        crude_gap = (c["60"] / c["50"] - 1) * 100
        asr_gap = (a["60"] / a["50"] - 1) * 100
        explained = (1 - abs(asr_gap) / abs(crude_gap)) * 100 if crude_gap else np.nan
        print(f"\n  Crude 60-vs-50 gap:            {crude_gap:+.1f}%")
        print(f"  Age-standardised gap:          {asr_gap:+.1f}%")
        print(f"  Share of gap explained by age: {explained:.0f}%")

    return asr


def balance_tests(covariates: pd.DataFrame, dist: pd.DataFrame) -> bool:
    """METHODS.md section 7. Returns True if balance holds."""
    print("\nBalance tests at the boundary")
    print("-" * 74)
    print("  (not yet implemented -- requires covariate data, see PROVENANCE.md)")
    return False


def placebo_tests(outcome: pd.DataFrame, dist: pd.DataFrame) -> bool:
    """METHODS.md section 7. Returns True if all placebos are null."""
    print("\nPlacebo outcomes at the boundary")
    print("-" * 74)
    print("  (not yet implemented -- requires placebo outcome data)")
    return False


def main() -> int:
    OUTPUT.mkdir(exist_ok=True)

    print("=" * 74)
    print("50vs60 -- mains frequency and dementia burden in Japan")
    print("=" * 74)

    # STEP 1 -- MDE first, always. METHODS.md section 9.
    print("\nStep 1: minimum detectable effect (reported before any fitting)")
    print("-" * 74)
    print("  Run `python src/power.py` for the full table.")
    print("  Preliminary: Tier 3 within-Shizuoka MDE ~31% of baseline prevalence.")
    print("  A 31% shift from a 20% ambient-exposure frequency difference is not")
    print("  a plausible effect size. Expected outcome: UNINFORMATIVE, not null.")

    outcome_path = PROCESSED / "outcome_long.csv"
    freq_path = REFERENCE / "area_frequency.csv"

    missing = [p for p in (outcome_path, freq_path) if not p.exists()]
    if missing:
        print("\n" + "=" * 74)
        print("HALTED -- required inputs not present:")
        for p in missing:
            print(f"  - {p.relative_to(ROOT)}")
        print("\nThis is expected on a fresh checkout. See data/raw/PROVENANCE.md")
        print("for retrieval instructions, including the manual steps (e-Stat appId,")
        print("GBD data-use agreement) that cannot be automated.")
        print("=" * 74)
        return 2

    outcome = load_or_exit(outcome_path, "primary and placebo analyses")
    freq = load_or_exit(freq_path, "exposure assignment")

    from schema import OUTCOME_LONG, AREA_FREQUENCY, validate
    print("\nSchema validation")
    print("-" * 74)
    validate(outcome, OUTCOME_LONG, "outcome_long")
    validate(freq, AREA_FREQUENCY, "area_frequency")

    ref_path = REFERENCE / "reference_population.csv"
    reference_pop = pd.read_csv(ref_path).set_index("age_band")["population"]
    reference_pop = reference_pop.reindex(STANDARD_BANDS)

    tier1 = tier1_prefecture(outcome, freq, reference_pop)
    tier1.to_csv(OUTPUT / "tier1_prefecture_asr.csv", index=False)
    print(f"\n  wrote output/tier1_prefecture_asr.csv")

    # STEP 2/3 -- gates. Tier 3 is not reached unless both pass.
    dist_path = PROCESSED / "boundary_distance.csv"
    if not dist_path.exists():
        print("\nTier 3 (confirmatory) skipped: boundary_distance.csv not built.")
        print("Tier 1 above is DESCRIPTIVE and carries no inferential weight.")
        return 0

    dist = load_or_exit(dist_path, "Tier 3 RD")
    covariates = PROCESSED / "covariates.csv"

    if not balance_tests(pd.DataFrame(), dist):
        print("\nHALTED before primary outcome: balance not established.")
        return 1
    if not placebo_tests(outcome, dist):
        print("\nHALTED before primary outcome: placebo tests not passed.")
        print("Per METHODS.md section 7, a boundary that moves non-electrical")
        print("outcomes invalidates the design. The primary estimate is not")
        print("computed, because it would not be interpretable.")
        return 1

    print("\nStep 4: primary outcome (gates passed)")
    print("  (not yet implemented)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
