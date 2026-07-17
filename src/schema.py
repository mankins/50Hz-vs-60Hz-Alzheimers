"""Canonical intermediate schemas.

Fetch scripts conform to these; analysis scripts consume them. Defining the
contract here means a new data source (LTCI vs GBD vs anything else) only needs
a new fetcher, not a new analysis.

Every table is long-format and tidy: one row per (unit, stratum).
"""

from __future__ import annotations

import pandas as pd

# --- data/processed/outcome_long.csv ---------------------------------------
# One row per (area_code, year, age_band, sex, outcome).
OUTCOME_LONG = {
    "area_code": "str",     # JIS municipality/prefecture code, zero-padded
    "area_name": "str",
    "area_level": "str",    # 'prefecture' | 'municipality'
    "year": "int",
    "age_band": "str",      # must be in agestd.STANDARD_BANDS
    "sex": "str",           # 'both' | 'male' | 'female'
    "outcome": "str",       # 'dementia' | 'colorectal_cancer' | 'stroke' | ...
    "cases": "float",
    "population": "float",
    "source": "str",        # 'ltci' | 'gbd2021' | ...
}

# --- data/reference/area_frequency.csv -------------------------------------
# One row per area. THE exposure variable.
AREA_FREQUENCY = {
    "area_code": "str",
    "area_name": "str",
    "area_level": "str",
    "frequency_hz": "str",   # '50' | '60' | 'mixed'
    "utility": "str",        # TEPCO, Chubu, Kansai, ...
    "confidence": "str",     # 'certain' | 'probable' | 'uncertain'
    "source": "str",         # citation key into data/reference/SOURCES.md
    "notes": "str",
}

# --- data/processed/boundary_distance.csv ----------------------------------
# Tier 3 running variable. Only for areas near the boundary.
BOUNDARY_DISTANCE = {
    "area_code": "str",
    "dist_km": "float",      # signed: negative = 50 Hz side, positive = 60 Hz side
    "boundary_segment": "str",  # 'shizuoka' | 'niigata' | 'nagano'
    "centroid_lat": "float",
    "centroid_lon": "float",
}


def validate(df: pd.DataFrame, spec: dict, name: str) -> None:
    """Fail loudly on schema drift rather than silently producing nonsense."""
    missing = set(spec) - set(df.columns)
    if missing:
        raise ValueError(f"{name}: missing columns {sorted(missing)}")

    if "age_band" in df.columns:
        from agestd import STANDARD_BANDS
        bad = set(df.age_band.unique()) - set(STANDARD_BANDS)
        if bad:
            raise ValueError(
                f"{name}: age bands {sorted(bad)} are not in STANDARD_BANDS. "
                "Coarse bands are rejected by design -- see METHODS.md section 6."
            )

    if "frequency_hz" in df.columns:
        bad = set(df.frequency_hz.astype(str).unique()) - {"50", "60", "mixed"}
        if bad:
            raise ValueError(f"{name}: bad frequency values {sorted(bad)}")

    if "area_code" in df.columns and df.area_code.duplicated().any() and \
            "year" not in df.columns:
        dupes = df.area_code[df.area_code.duplicated()].unique()[:5]
        raise ValueError(f"{name}: duplicate area_code, e.g. {list(dupes)}")

    print(f"  {name}: {len(df):,} rows, schema OK")
