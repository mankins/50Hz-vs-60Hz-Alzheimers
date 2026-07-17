"""GBD diagnostic: is there real between-prefecture signal in dementia at all?

Run: python src/05_gbd_diagnostic.py

WHAT THIS TESTS, and why it is not the 50/60 test.

IHME's own Japan subnational paper (Lancet Public Health 2025) says GBD disease
models "compensate by using regional data and covariates, potentially resulting in
MINIMAL REGIONAL VARIATION in certain diseases ... due to limited Japanese data
coverage."

If that applies to dementia, then GBD's between-prefecture variation in Alzheimer's
is model output, and regressing it on ANY prefecture-level variable -- including
mains frequency -- is near-circular.

We can test that claim empirically instead of taking it on faith:

  Compare the between-prefecture coefficient of variation (CV) of age-standardised
  Alzheimer's prevalence against causes where Japan demonstrably HAS good data and
  where large, well-documented regional variation is known to exist:

    - Stroke (494)         : famous east/north-west gradient, driven by salt intake.
                             Tohoku has long had elevated stroke. This is real and
                             well measured in Japanese vital statistics.
    - Stomach cancer (414) : strong, well-documented regional variation in Japan.

  If CV(Alzheimer's) << CV(stroke), the dementia surface is FLATTER than a
  genuinely-measured cause. That is the signature of model smoothing, and it means
  the outcome carries little real prefecture-level information.

  If CV(Alzheimer's) is comparable to CV(stroke), the modelling worry is weaker than
  feared and a prefecture-level analysis is at least looking at something.

Colon/rectum cancer (441) and IHD (493) additionally serve as placebo outcomes for
the 50/60 contrast: no plausible flicker mechanism, so any 50-vs-60 difference in
them indicates the contrast is picking up east/west Japan rather than electricity.

INTERPRETATION GUARD: a null 50-vs-60 result here is NOT evidence of absence. It is
uninformative if the diagnostic shows the surface is flat, because a flat surface
cannot show any association with anything.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
REFERENCE = ROOT / "data" / "reference"
OUTPUT = ROOT / "output"

TARGET = RAW / "gbd2021_japan_prefecture_asr.csv"

CAUSES = {
    543: ("Alzheimer's & dementias", "outcome"),
    494: ("Stroke", "comparator-real-variation"),
    414: ("Stomach cancer", "comparator-real-variation"),
    441: ("Colon & rectum cancer", "placebo"),
    493: ("Ischemic heart disease", "placebo"),
}


def instructions() -> None:
    print("\n" + "=" * 72)
    print("NEED: one browser download (IHME gates the data endpoint behind")
    print("      Cloudflare Turnstile; curl cannot solve it)")
    print("=" * 72)
    print("""
1. Open   https://gbd2021.healthdata.org/gbd-results/
   Sign in (free IHME account; accept the non-commercial user agreement).

   >>> Use gbd2021.healthdata.org, NOT vizhub.healthdata.org <<<
   vizhub now serves GBD 2023, whose location ids differ. Wrong host = wrong data.

2. Set EXACTLY:

     GBD Estimate .... Cause of death or injury
     Measure ......... Prevalence
     Metric .......... Rate
     Age ............. Age-standardized          <-- single option, not the 5-yr bands
     Sex ............. Both
     Year ............ 1990-2021  (select all)

     Cause ........... select these FIVE:
                         Alzheimer's disease and other dementias   (543)
                         Stroke                                    (494)
                         Stomach cancer                            (414)
                         Colon and rectum cancer                   (441)
                         Ischemic heart disease                    (493)

     Location ........ Japan -> expand -> select ALL 47 prefectures
                       (Hokkaido .. Okinawa). Do NOT select "Japan" itself.

   Expected size: 47 x 5 causes x 1 age x 1 sex x 32 years = 7,520 rows.
   Trivially under the 100,000-row cap -> a single download.

3. Download the CSV, unzip if needed, and save it as:

     data/raw/gbd2021_japan_prefecture_asr.csv

4. Re-run:  python src/05_gbd_diagnostic.py
""")
    print("=" * 72)


def load() -> pd.DataFrame:
    df = pd.read_csv(TARGET)
    df.columns = [c.strip().lower() for c in df.columns]

    # IHME exports vary: sometimes *_id + *_name, sometimes names only.
    def pick(*cands):
        for c in cands:
            if c in df.columns:
                return c
        raise ValueError(f"none of {cands} in {list(df.columns)}")

    loc = pick("location_name", "location")
    cause = pick("cause_name", "cause")
    val = pick("val", "value")
    year = pick("year", "year_id")

    out = df.rename(columns={loc: "prefecture", cause: "cause",
                             val: "asr", year: "year"})
    keep = ["prefecture", "cause", "asr", "year"]
    for extra in ("cause_id", "location_id", "upper", "lower"):
        if extra in df.columns:
            out[extra] = df[extra]
            keep.append(extra)

    # Merge on location_id, never on name: IHME romanises with macrons
    # (Hokkaidō, Ōsaka, Tōkyō, Kyōto, Hyōgo, Kōchi, Ōita) and a name join
    # silently drops 7 prefectures.
    if "location_id" in out.columns:
        out = out[out.location_id != 67]  # drop Japan national, keep prefectures
    return out[keep]


def main() -> int:
    if not TARGET.exists():
        print(f"MISSING: {TARGET.relative_to(ROOT)}")
        instructions()
        return 2

    OUTPUT.mkdir(exist_ok=True)
    df = load()
    freq = pd.read_csv(REFERENCE / "prefecture_frequency.csv", dtype={"jis_code": str})

    print("GBD diagnostic: is there real between-prefecture signal in dementia?")
    print("=" * 72)
    print(f"loaded {len(df):,} rows | "
          f"{df.prefecture.nunique()} prefectures | "
          f"{df.cause.nunique()} causes | "
          f"years {int(df.year.min())}-{int(df.year.max())}")

    year = int(df.year.max())
    d = df[df.year == year].copy()

    # ---- Diagnostic 1: between-prefecture CV by cause -----------------------
    print(f"\n{'='*72}\nDIAGNOSTIC 1 -- between-prefecture dispersion, {year}\n{'='*72}")
    print(f"{'cause':<28} {'mean':>10} {'sd':>9} {'CV%':>7} {'min':>9} {'max':>9} {'max/min':>8}")
    print("-" * 72)

    cv = {}
    for cause, g in d.groupby("cause"):
        m, s = g.asr.mean(), g.asr.std()
        c = s / m * 100 if m else np.nan
        cv[cause] = c
        print(f"{cause[:28]:<28} {m:>10,.1f} {s:>9,.1f} {c:>6.1f}% "
              f"{g.asr.min():>9,.1f} {g.asr.max():>9,.1f} "
              f"{g.asr.max()/g.asr.min():>8.2f}")

    alz = next((k for k in cv if "alzheimer" in k.lower()), None)
    stroke = next((k for k in cv if "stroke" in k.lower()), None)

    print("\nVERDICT ON THE MODELLING WORRY")
    print("-" * 72)
    if alz and stroke:
        ratio = cv[alz] / cv[stroke]
        print(f"  CV(Alzheimer's) / CV(Stroke) = {ratio:.2f}")
        if ratio < 0.5:
            print("""
  ** Alzheimer's is MUCH FLATTER across prefectures than stroke. **
  Stroke's regional variation in Japan is real, large, and well measured
  (the salt-intake gradient). Dementia being this much flatter is the
  signature of covariate-driven model smoothing -- consistent with IHME's
  own statement about 'minimal regional variation ... due to limited
  Japanese data coverage'.

  CONSEQUENCE: any 50-vs-60 test on this surface is UNINFORMATIVE, not null.
  A flat surface cannot show an association with anything.""")
        elif ratio < 0.8:
            print("""
  Alzheimer's is somewhat flatter than stroke. Suggestive of smoothing but
  not decisive. Treat any 50/60 result as weak evidence at best.""")
        else:
            print("""
  Alzheimer's dispersion is comparable to stroke's. The modelling worry is
  WEAKER than feared -- the surface does carry prefecture-level variation.
  A 50/60 test is at least looking at something real. Proceed, but the
  circularity caveat still applies: the variation may be covariate-driven
  even if it is not flat.""")

    # ---- Diagnostic 2: the 50 vs 60 contrast + placebos ---------------------
    print(f"\n{'='*72}\nDIAGNOSTIC 2 -- 50 vs 60 Hz contrast, {year}\n{'='*72}")
    print("NOTE: static frequency coding is WRONG for 9/47 prefectures (the boundary")
    print("moved 1943-1961). Prefectures that ever converted are flagged and excluded")
    print("from the strict comparison. See data/reference/frequency_conversions.csv.\n")

    m = d.merge(freq, left_on="location_id", right_on="gbd_location_id", how="left")
    unmatched = m[m.current_hz.isna()].prefecture.unique()
    if len(unmatched):
        print(f"  ERROR unmatched location_ids: {list(unmatched)[:8]}")
        return 1
    print(f"  merged on location_id: {m.prefecture.nunique()}/47 prefectures matched")

    strict = m[(~m.ever_converted.fillna(True)) & (m.current_hz.isin(["50", "60"]))]

    print(f"{'cause':<28} {'50Hz':>9} {'60Hz':>9} {'ratio':>7} {'p':>9}  role")
    print("-" * 72)
    from scipy import stats
    rows = []
    for cause, g in strict.groupby("cause"):
        a = g[g.current_hz == "50"].asr
        b = g[g.current_hz == "60"].asr
        if len(a) < 3 or len(b) < 3:
            continue
        t, p = stats.ttest_ind(a, b, equal_var=False)
        cid = int(g.cause_id.iloc[0]) if "cause_id" in g else None
        role = CAUSES.get(cid, ("", "?"))[1]
        rows.append(dict(cause=cause, mean50=a.mean(), mean60=b.mean(),
                         ratio=b.mean()/a.mean(), p=p, role=role,
                         n50=len(a), n60=len(b)))
        print(f"{cause[:28]:<28} {a.mean():>9,.1f} {b.mean():>9,.1f} "
              f"{b.mean()/a.mean():>7.3f} {p:>9.3f}  {role}")

    if rows:
        out = pd.DataFrame(rows)
        out.to_csv(OUTPUT / "gbd_diagnostic_5060.csv", index=False)
        print(f"\n  wrote output/gbd_diagnostic_5060.csv")

        placebo_hits = out[(out.role == "placebo") & (out.p < 0.05)]
        if len(placebo_hits):
            print(f"""
  ** {len(placebo_hits)} PLACEBO outcome(s) differ between 50 and 60 Hz at p<0.05. **
  Colon cancer and ischaemic heart disease have no flicker mechanism. If they
  separate on frequency, the contrast is capturing EAST vs WEST JAPAN -- diet,
  urbanisation, culture -- not electricity. Any dementia result here is
  uninterpretable.""")
        else:
            print("\n  Placebos do not separate. (Weak reassurance only: with n<=47 and")
            print("  this little power, placebos failing to separate proves little.)")

    print(f"\n{'='*72}")
    print("""REMEMBER: alpha=0.005 was pre-specified for the confirmatory test
(METHODS.md section 8), and this is NOT the confirmatory design -- it is a
prefecture-level ecological comparison with n<=47, no identification, and a
static exposure coding known to be wrong for 9 prefectures. Nothing here can
support a causal claim. It is a diagnostic.""")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
