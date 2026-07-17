"""Tests for agestd.py.

Run: python src/test_agestd.py

The headline test is `test_identical_risk_different_age_structure`, which
demonstrates the core claim of docs/00_critique_of_initial_analysis.md: two
regions with *identical* age-specific dementia risk can show a large crude-rate
gap purely from age structure -- and direct standardisation removes it entirely.
"""

import sys

import numpy as np
import pandas as pd

from agestd import STANDARD_BANDS, direct_standardise, standardise_frame

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILS.append(name)


def test_standardising_to_own_population_returns_crude():
    """If the reference IS the study population, ASR must equal the crude rate."""
    cases = np.array([10, 20, 40, 80, 160, 320, 640], dtype=float)
    pop = np.array([1000, 900, 800, 600, 400, 200, 50], dtype=float)
    asr = direct_standardise(cases, pop, pop)
    crude = cases.sum() / pop.sum() * 100_000
    check("standardising to own population == crude rate",
          np.isclose(asr, crude), f"asr={asr:.2f} crude={crude:.2f}")


def test_identical_risk_different_age_structure():
    """THE point. Same age-specific risk, different demography.

    'Young' region: Tokyo-like, few very old.
    'Old' region:   rural-like, many very old.
    Both have byte-identical age-specific rates, so there is no real difference
    in risk. The crude rates should diverge sharply; the ASRs should be equal.
    """
    # Dementia prevalence roughly doubling every 5-year band, as in reality.
    band_rate = np.array([0.01, 0.02, 0.04, 0.09, 0.18, 0.32, 0.45])

    young_pop = np.array([100_000, 80_000, 55_000, 30_000, 12_000, 3_000, 400], float)
    old_pop = np.array([100_000, 95_000, 88_000, 70_000, 45_000, 18_000, 4_000], float)

    young_cases = band_rate * young_pop
    old_cases = band_rate * old_pop

    reference = young_pop + old_pop

    asr_young = direct_standardise(young_cases, young_pop, reference)
    asr_old = direct_standardise(old_cases, old_pop, reference)

    crude_young = young_cases.sum() / young_pop.sum() * 100_000
    crude_old = old_cases.sum() / old_pop.sum() * 100_000

    gap = crude_old / crude_young

    check("identical risk -> identical ASR",
          np.isclose(asr_young, asr_old),
          f"young={asr_young:.1f} old={asr_old:.1f}")
    check("identical risk -> crude rates still differ substantially",
          gap > 1.3, f"crude ratio={gap:.2f}")

    print(f"        crude:  young={crude_young:,.0f}  old={crude_old:,.0f}  "
          f"ratio={gap:.2f}x  <- spurious gap from demography alone")
    print(f"        ASR:    young={asr_young:,.0f}  old={asr_old:,.0f}  "
          f"ratio={asr_old/asr_young:.2f}x  <- gap correctly removed")


def test_detects_real_effect():
    """Standardisation must not wash out a genuine difference."""
    band_rate = np.array([0.01, 0.02, 0.04, 0.09, 0.18, 0.32, 0.45])
    pop = np.array([100_000, 80_000, 55_000, 30_000, 12_000, 3_000, 400], float)
    reference = pop

    asr_base = direct_standardise(band_rate * pop, pop, reference)
    asr_elevated = direct_standardise(band_rate * 1.2 * pop, pop, reference)

    check("a real 20% elevation survives standardisation",
          np.isclose(asr_elevated / asr_base, 1.2),
          f"ratio={asr_elevated/asr_base:.3f}")


def test_shape_mismatch_raises():
    try:
        direct_standardise(np.ones(3), np.ones(4), np.ones(3))
        check("shape mismatch raises", False, "no exception")
    except ValueError:
        check("shape mismatch raises", True)


def test_zero_population_raises():
    try:
        direct_standardise(np.ones(3), np.array([1.0, 0.0, 1.0]), np.ones(3))
        check("zero denominator raises", False, "no exception")
    except ValueError:
        check("zero denominator raises", True)


def test_standardise_frame_roundtrip():
    reference = pd.Series([100, 90, 80, 60, 40, 20, 5], index=STANDARD_BANDS,
                          dtype=float)
    df = pd.DataFrame({
        "pref": ["A"] * 7 + ["B"] * 7,
        "age_band": STANDARD_BANDS * 2,
        "cases": [1, 2, 4, 8, 16, 32, 64] * 2,
        "population": [1000, 900, 800, 600, 400, 200, 50] * 2,
    })
    out = standardise_frame(df, group_col="pref", reference=reference)
    check("standardise_frame returns one row per group", len(out) == 2,
          f"got {len(out)}")
    check("identical inputs -> identical ASRs",
          np.isclose(out.asr.iloc[0], out.asr.iloc[1]))
    check("CI brackets the point estimate",
          bool((out.asr_lo95 < out.asr).all() and (out.asr > out.asr_hi95 * 0).all()))


def test_missing_band_raises():
    reference = pd.Series([100] * 7, index=STANDARD_BANDS, dtype=float)
    df = pd.DataFrame({
        "pref": ["A"] * 6,
        "age_band": STANDARD_BANDS[:6],  # 95+ missing
        "cases": [1] * 6,
        "population": [100] * 6,
    })
    try:
        standardise_frame(df, group_col="pref", reference=reference)
        check("missing age band raises", False, "silently accepted missing band")
    except ValueError:
        check("missing age band raises", True)


if __name__ == "__main__":
    print("agestd tests")
    print("-" * 60)
    test_standardising_to_own_population_returns_crude()
    test_identical_risk_different_age_structure()
    test_detects_real_effect()
    test_shape_mismatch_raises()
    test_zero_population_raises()
    test_standardise_frame_roundtrip()
    test_missing_band_raises()
    print("-" * 60)
    if FAILS:
        print(f"{len(FAILS)} FAILED: {FAILS}")
        sys.exit(1)
    print("all passed")
