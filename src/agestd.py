"""Direct age standardisation.

Kept separate from the pipeline scripts so it can be unit-tested in isolation
(`python src/test_agestd.py`). Nothing in here knows about electricity.

The central claim this module exists to support: a crude all-ages rate for an
age-dependent disease is very nearly a measurement of the population's age
structure. Direct standardisation removes that by asking the counterfactual
"what would this region's rate be if it had the reference population's age
distribution?"
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# Five-year bands. An open-ended 80+ bucket is NOT acceptable for dementia --
# see METHODS.md section 6. Risk roughly doubles every 5 years, so within-bucket
# age structure differences leave large residual confounding.
STANDARD_BANDS = [
    "65-69", "70-74", "75-79", "80-84", "85-89", "90-94", "95+",
]


def direct_standardise(
    cases: np.ndarray,
    population: np.ndarray,
    reference_population: np.ndarray,
    per: int = 100_000,
) -> float:
    """Directly age-standardised rate.

    Args:
        cases: observed cases per age band in the study population.
        population: person-years (or population) per age band, study population.
        reference_population: population per age band in the reference/standard.
        per: rate multiplier.

    Returns:
        Age-standardised rate per `per` head of the reference population.

    Raises:
        ValueError: on shape mismatch or non-positive denominators.
    """
    cases = np.asarray(cases, dtype=float)
    population = np.asarray(population, dtype=float)
    reference_population = np.asarray(reference_population, dtype=float)

    if not (cases.shape == population.shape == reference_population.shape):
        raise ValueError(
            f"shape mismatch: cases{cases.shape} population{population.shape} "
            f"reference{reference_population.shape}"
        )
    if np.any(population <= 0):
        raise ValueError("population must be positive in every band")
    if np.any(cases < 0):
        raise ValueError("cases must be non-negative")

    band_rates = cases / population
    weights = reference_population / reference_population.sum()
    return float(np.sum(band_rates * weights) * per)


def standardised_rate_variance(
    cases: np.ndarray,
    population: np.ndarray,
    reference_population: np.ndarray,
    per: int = 100_000,
) -> float:
    """Variance of the directly standardised rate (Poisson approximation).

    Used for confidence intervals. Assumes band counts are Poisson, which is
    standard practice but understates uncertainty when cases are clustered
    (e.g. by household or care facility).
    """
    cases = np.asarray(cases, dtype=float)
    population = np.asarray(population, dtype=float)
    reference_population = np.asarray(reference_population, dtype=float)

    weights = reference_population / reference_population.sum()
    return float(np.sum((weights / population) ** 2 * cases) * per**2)


def standardise_frame(
    df: pd.DataFrame,
    *,
    group_col: str,
    band_col: str = "age_band",
    cases_col: str = "cases",
    pop_col: str = "population",
    reference: pd.Series,
    per: int = 100_000,
) -> pd.DataFrame:
    """Standardise every group in a long-format frame.

    Args:
        df: long format, one row per (group, age_band).
        group_col: column identifying the unit (e.g. 'prefecture').
        reference: Series indexed by age_band giving the standard population.

    Returns:
        One row per group: asr, variance, se, 95% CI, and the crude rate for
        contrast. The crude-vs-standardised gap is the quantity of interest when
        diagnosing whether an apparent regional signal is really age structure.
    """
    bands = list(reference.index)
    rows = []

    for group, g in df.groupby(group_col, sort=True):
        g = g.set_index(band_col).reindex(bands)
        if g[[cases_col, pop_col]].isna().any().any():
            missing = g.index[g[cases_col].isna() | g[pop_col].isna()].tolist()
            raise ValueError(f"{group!r} missing bands: {missing}")

        asr = direct_standardise(g[cases_col], g[pop_col], reference, per=per)
        var = standardised_rate_variance(g[cases_col], g[pop_col], reference, per=per)
        se = float(np.sqrt(var))
        crude = float(g[cases_col].sum() / g[pop_col].sum() * per)

        rows.append({
            group_col: group,
            "asr": asr,
            "asr_se": se,
            "asr_lo95": asr - 1.96 * se,
            "asr_hi95": asr + 1.96 * se,
            "crude_rate": crude,
            # >1 means the crude rate overstates burden because the region is
            # older than the reference. This ratio is the confounder made visible.
            "crude_to_asr_ratio": crude / asr if asr > 0 else np.nan,
            "total_cases": float(g[cases_col].sum()),
            "total_pop": float(g[pop_col].sum()),
        })

    return pd.DataFrame(rows)
