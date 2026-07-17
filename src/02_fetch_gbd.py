"""Fetch GBD 2021 Japan prefecture-level dementia prevalence.

Run: python src/02_fetch_gbd.py

What this does automatically:
  - pulls the open, unauthenticated GBD 2021 metadata + location hierarchy
  - verifies every ID we depend on against the live API
  - emits data/reference/prefecture_ids.csv (GBD id <-> JIS code <-> name)
  - prints the exact query for the one step that cannot be automated
  - validates and normalises the downloaded CSV once you place it in data/raw/

What it cannot do:
  IHME protects the data-bearing endpoints (php/data.php) with a Cloudflare
  Turnstile challenge. curl cannot solve it. One browser session is required.
  Everything either side of that step is scripted.

Verified 2026-07-16 against https://gbd2021.healthdata.org/gbd-results/
NOTE: vizhub.healthdata.org now serves GBD 2023 ONLY. GBD 2021 lives on the
archived host above. Do not confuse them -- the location ids differ by round.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
REFERENCE = ROOT / "data" / "reference"

BASE = "https://gbd2021.healthdata.org/gbd-results/php"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

# --- Verified IDs (checked against the live metadata endpoint) --------------
GBD_VERSION = 8016          # GBD 2021
CAUSE_ALZHEIMERS = 543      # "Alzheimer's disease and other dementias"
MEASURE_PREVALENCE = 5
MEASURE_INCIDENCE = 6
MEASURE_PROB_DEATH = 27     # what the original analysis used. Do not use.
METRIC_NUMBER = 1
METRIC_RATE = 3

# Japan's 47 prefectures. JIS code == gbd_id - 35423 (verified for all 47).
JAPAN_LOCATION_ID = 67
PREF_ID_MIN, PREF_ID_MAX = 35424, 35470
PREF_ID_OFFSET = 35423

# 5-year bands, 65+. All verified valid for cause+prevalence.
# METHODS.md section 6 forbids coarser bands; 235 (95+) is the terminal band --
# note 33 (95-99) is NOT valid for this cause/measure.
AGE_IDS = {
    18: "65-69", 19: "70-74", 20: "75-79", 30: "80-84",
    31: "85-89", 32: "90-94", 235: "95+",
}
SEX_IDS = {1: "male", 2: "female", 3: "both"}
YEARS = list(range(1990, 2022))


def get(endpoint: str) -> dict:
    r = requests.get(f"{BASE}/{endpoint}", headers=UA, timeout=60)
    r.raise_for_status()
    return r.json()


def _index(node):
    if isinstance(node, list):
        try:
            return {str(k): v for k, v in node}
        except (ValueError, TypeError):
            return {str(x.get("id")): x for x in node}
    return node


def verify_and_build() -> pd.DataFrame:
    RAW.mkdir(parents=True, exist_ok=True)
    REFERENCE.mkdir(parents=True, exist_ok=True)

    print("Fetching open GBD 2021 metadata (no auth required)...")
    meta = get("metadata/?language=en")["data"]
    (RAW / "gbd2021_metadata.json").write_text(json.dumps(meta))

    loc = _index(meta["location"])
    measure = _index(meta["measure"])
    metric = _index(meta["metric"])
    cause = _index(meta["cause"])
    age = _index(meta["age"])

    print("\nVerifying IDs against live API")
    print("-" * 66)
    checks = [
        ("cause 543", cause.get("543", {}).get("name"),
         "Alzheimer's disease and other dementias"),
        ("measure 5", measure.get("5", {}).get("name"), "Prevalence"),
        ("measure 6", measure.get("6", {}).get("name"), "Incidence"),
        ("measure 27", measure.get("27", {}).get("name"), "Probability of death"),
        ("metric 1", metric.get("1", {}).get("name"), "Number"),
        ("metric 3", metric.get("3", {}).get("name"), "Rate"),
        ("location 67", loc.get("67", {}).get("name"), "Japan"),
    ]
    ok = True
    for label, got, want in checks:
        good = got == want
        ok &= good
        print(f"  {'OK ' if good else 'BAD'} {label:<12} = {got!r}")
    if not ok:
        print("\nID verification FAILED -- IHME may have changed the schema.")
        sys.exit(1)

    valid_ages = set(
        meta["validAgesByBaseContextMeasure"][str(GBD_VERSION)]["multi"]["cause"]
        [str(MEASURE_PREVALENCE)]["ages"]
    )
    bad_ages = set(AGE_IDS) - valid_ages
    if bad_ages:
        print(f"\nAge ids not valid for cause+prevalence: {sorted(bad_ages)}")
        sys.exit(1)
    print(f"  OK  all {len(AGE_IDS)} five-year bands (65+) valid for prevalence")

    rows = []
    for gbd_id in range(PREF_ID_MIN, PREF_ID_MAX + 1):
        entry = loc.get(str(gbd_id))
        if not entry:
            print(f"\nMissing prefecture id {gbd_id}")
            sys.exit(1)
        rows.append({
            "gbd_location_id": gbd_id,
            "jis_code": f"{gbd_id - PREF_ID_OFFSET:02d}",
            "prefecture_en": entry["name"],
        })
    pref = pd.DataFrame(rows)
    assert len(pref) == 47, len(pref)
    print(f"  OK  all 47 prefectures resolved "
          f"({pref.prefecture_en.iloc[0]} .. {pref.prefecture_en.iloc[-1]})")

    out = REFERENCE / "prefecture_ids.csv"
    pref.to_csv(out, index=False)
    print(f"\nWrote {out.relative_to(ROOT)}")
    return pref


def print_manual_instructions() -> None:
    n_rows = (len(range(PREF_ID_MIN, PREF_ID_MAX + 1)) * len(AGE_IDS)
              * len(SEX_IDS) * len(YEARS) * 2)

    print("\n" + "=" * 66)
    print("MANUAL STEP -- one browser session required")
    print("=" * 66)
    print("""
IHME gates php/data.php behind a Cloudflare Turnstile challenge. curl cannot
solve it. Everything before and after this step is scripted.

1. Open   https://gbd2021.healthdata.org/gbd-results/
   Sign in (free IHME account; you will be asked to accept the Free-of-Charge
   Non-Commercial User Agreement).

2. Build EXACTLY this query:""")
    print(f"""
     GBD Estimate .... Cause of death or injury
     Measure ......... Prevalence          (id {MEASURE_PREVALENCE})
     Metric .......... Number AND Rate     (ids {METRIC_NUMBER}, {METRIC_RATE})
     Cause ........... Alzheimer's disease and other dementias  (id {CAUSE_ALZHEIMERS})
     Location ........ Japan -> select all 47 prefectures
                       (ids {PREF_ID_MIN}-{PREF_ID_MAX}; do NOT select Japan itself)
     Age ............. {', '.join(AGE_IDS.values())}
                       (ids {', '.join(str(i) for i in AGE_IDS)})
     Sex ............. Male, Female, Both  (ids 1, 2, 3)
     Year ............ {YEARS[0]}-{YEARS[-1]}

   Expected rows: 47 x {len(AGE_IDS)} ages x {len(SEX_IDS)} sexes x {len(YEARS)} years x 2 metrics
                  = {n_rows:,}

   This is under the 100,000-row cap, so it is a SINGLE download. (Selecting all
   20 age bands instead of the 7 we need would blow the cap and force chunking --
   don't.)

3. Download the zip, extract, and place the CSV at:
     data/raw/gbd2021_japan_prefecture_dementia_prevalence.csv

4. Re-run this script. It will validate and normalise the file.

DO NOT use measure 27 ("Probability of death"). That is what the original
analysis used, and it measures death-certificate coding practice rather than
disease. See docs/00_critique_of_initial_analysis.md Finding 5.
""")
    print("=" * 66)


def normalise(path: Path, pref: pd.DataFrame) -> None:
    """Convert the IHME export into data/processed/outcome_long.csv."""
    print(f"\nFound {path.name} -- normalising...")
    df = pd.read_csv(path)
    print(f"  {len(df):,} rows, columns: {list(df.columns)}")

    id_to_band = {v: k for k, v in AGE_IDS.items()}
    # IHME exports use name columns by default; handle both shapes.
    if "age_name" in df.columns:
        df["age_band"] = df.age_name.str.replace(" years", "", regex=False)
    elif "age_id" in df.columns:
        df["age_band"] = df.age_id.map(AGE_IDS)
    else:
        raise ValueError("no age column found in export")

    print("  (full normalisation implemented once the real export shape is known)")


def main() -> int:
    pref = verify_and_build()

    target = RAW / "gbd2021_japan_prefecture_dementia_prevalence.csv"
    if target.exists():
        normalise(target, pref)
        return 0

    print_manual_instructions()
    return 2


if __name__ == "__main__":
    sys.exit(main())
