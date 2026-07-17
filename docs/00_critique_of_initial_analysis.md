# Why the initial chart does not support the hypothesis

Concerns `docs/original_chart_UNRELIABLE.png` — "Mean Alzheimer's Rate in Japan by
Electricity Frequency", three series (50 Hz / 60 Hz / Mixed), 1980–2021.

Recorded here because a future paper needs to explain what the naive analysis showed
and why it was discarded. This is not incidental — the failure modes below are the
reason the study design in `METHODS.md` looks the way it does.

## Stated data sources

1. IHME GBD 2021, measure = **Probability of death**, metric = probability of death,
   sex = both, age = all ages, years 1990–2021, cause = Alzheimer's disease and other
   dementias. Country-level.
2. World Bank WDI `EG.ELC.ACCS.ZS` (access to electricity, % of population).
3. Country mains frequency, hand-classified from Wikipedia "Mains electricity by
   country" into 50 Hz / 60 Hz / mixed.

## Finding 1 — the chart cannot be built from these sources

The sources are **country-level**. A chart titled "in Japan" split into 50/60/Mixed
requires **prefecture-level** Japanese data, which none of the three sources contain.

Either the title is wrong and this is actually the international country-level analysis
(consistent with "mixed" being a category in the Wikipedia table), or the data has an
unaccounted origin.

## Finding 2 — the 1980–1989 segment does not exist in any cited source

GBD 2021 begins at **1990**. The chart plots 1980–1989. Those points cannot come from
any listed source.

This exactly explains the ~14× discontinuity at 1990 (≈25 → ≈350 per 100k). No disease
process does that; it is a data seam. The pre-1990 values (≈20/100k) are plausible as a
crude *mortality* rate while the post-1990 values (≈1,200/100k ≈ 1.2%) are plausible as
*prevalence* — suggesting two different quantities were spliced onto one axis.

**Action:** the pre-1990 segment must be treated as unverified and excluded until a
source file can be named. If the analysis was assembled conversationally with an LLM,
this stretch may have been fabricated outright.

## Finding 3 — the series are ordered by age structure, not frequency

The measure is a **crude all-ages rate**. Dementia incidence roughly doubles every five
years after 65, so a crude all-ages rate is very nearly a measurement of *what fraction
of the population is over 75*.

- **"Mixed" highest:** in a country-level classification, "mixed-frequency" is a tiny
  bucket of which **Japan** is the canonical member. Japan has the oldest population on
  Earth. The top line is Japanese demography, essentially unmediated.
- **60 > 50:** the 50 Hz bucket contains essentially all of Africa (~54 countries) —
  the youngest populations on the planet with the least complete death registration,
  hence near-zero *recorded* Alzheimer's mortality. In an unweighted country mean,
  Africa alone drags the 50 Hz line down. The 60 Hz bucket is the Americas plus Korea,
  Taiwan, the Philippines — richer, older, better-registered.

The three lines are ordered by development and median age, in that order.

### Finding 3a — quantified: the observed gaps are smaller than the confounder

Simulating two populations with **byte-identical age-specific dementia risk** but
realistic differing age structures (a Tokyo-like young population vs a rural-west-like
old one), using band rates that double every 5 years:

| Quantity | Value |
|---|---|
| Spurious crude-rate gap from age structure **alone** | **1.75× (75%)** |
| Observed gap in chart, 60 Hz vs 50 Hz | ~1.04× (~4%) |
| Observed gap in chart, Mixed vs 50 Hz | ~1.13× (~13%) |

Both observed gaps sit **well inside** the range that age structure generates unaided,
with no effect present. Direct standardisation removes the simulated gap completely
(1.00×), confirming it is pure demography.

The chart therefore contains no signal exceeding its own uncontrolled confounder.
Reproduce with `python src/test_agestd.py` (test
`test_identical_risk_different_age_structure`).

## Finding 4 — the curves are too smooth to be measurement

Three series running parallel, evenly spaced, never crossing, for thirty years is the
signature of a smooth statistical model — not of noisy epidemiological reality. Real
regional data crosses and jitters.

GBD estimates are produced by a covariate-driven model (DisMod-MR), and cause-of-death
inputs pass through garbage-code redistribution that is itself covariate-driven. An
analysis of these outputs at fine geographic resolution risks **recovering IHME's
covariate structure rather than discovering anything about the world**.

**This is now confirmed by IHME's own authors**, not merely inferred. From the
Limitations section of "Three decades of population health changes in Japan, 1990–2021:
a subnational analysis for GBD 2021" (*Lancet Public Health*, Mar 2025,
https://pmc.ncbi.nlm.nih.gov/articles/PMC11959113/):

> "Data gaps remain at both the national and prefectural levels. **GBD disease models
> compensate by using regional data and covariates, potentially resulting in minimal
> regional variation in certain diseases and risk factors due to limited Japanese data
> coverage.**"

> "Furthermore, incomplete temporal coverage means 2021 estimates relied heavily on GBD
> disease models."

So the smoothness is not a coincidence or an artefact of aggregation. It is what the
model produces where data is thin. The paper reports **no prefecture-level dementia
variation** and identifies **no prefecture-level dementia data source**.

The consequence is severe and general: **any** analysis regressing GBD subnational
dementia estimates on **any** subnational variable risks being near-circular, because
the outcome's regional variation may itself be manufactured from regional covariates.
This applies to the frequency hypothesis and to anything else one might test this way.

## Finding 5 — "Probability of death" is the wrong measure

GBD's "probability of death" is the chance of dying *from a given cause* in an age
period — a mortality measure. For dementia this is close to the worst available choice.

People with Alzheimer's overwhelmingly die *of* pneumonia, sepsis, falls, or cardiac
events. Whether "Alzheimer's" is recorded as the underlying cause is an administrative
and cultural decision varying by an order of magnitude between countries and drifting
over time. **Alzheimer's mortality statistics substantially measure death-certificate
coding practice.**

Use **prevalence** or **incidence**, which GBD publishes for this cause.

Note also that "Alzheimer's disease and other dementias" is a composite folding in
vascular and Lewy body dementia, while the flicker hypothesis concerns AD specifically.

## Finding 6 — electricity access is a confounder, not a control

`EG.ELC.ACCS.ZS` is a development index in disguise, correlating ~0.9 with GDP, life
expectancy, and registration completeness. Because access also correlates with
frequency through colonial history (see `01_why_international_comparison_fails.md`),
stratifying on it carves the data along the contaminated axis rather than cleaning it.

## Finding 7 — the age bands in the newer export are too coarse to rescue it

The age-specific export (<70 / 70–74 / 75–79 / 80+) is the right instinct but
insufficient. `<70` lumps infants with 69-year-olds. `80+` is an open bucket holding
most of the burden, and within-bucket age structure differs sharply between populations
— Japan's 80+ are far older within the bucket than Nigeria's. For a disease doubling
every five years, this leaves large residual confounding.

Five-year bands to 95+ are required.

## Finding 8 — the observed direction contradicts the motivating mechanism

If the 40 Hz gamma-entrainment literature is the motivation, the signed prediction is
that **60 Hz should be protective** (120 Hz = 3 × 40 Hz, an exact third harmonic;
100 Hz has no integer relationship to 40 Hz). The chart shows 60 Hz with *higher*
rates — the opposite. See `METHODS.md` §2.1.

## Disposition

The international analysis is **retired, not patched** — see
`01_why_international_comparison_fails.md`. The Japan subnational design survives and
is specified in `METHODS.md`.
