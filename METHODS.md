# Pre-registration: Mains frequency and dementia burden in Japan

**Version:** 0.2 (draft)
**Status:** written before any outcome data has been examined. Any analysis run before
this document is finalised is exploratory and labelled as such.
**Deviations:** all departures from this plan must be logged in `docs/DEVIATIONS.md`
with a date and reason. Do not silently edit this file after data inspection.

---

> ## ⛔ SUPERSEDED BY DATA AVAILABILITY (2026-07-17)
>
> **Every design below is blocked — not by power, but by data that does not exist
> publicly.** See `docs/03_japan_data_availability.md` for the verified evidence.
>
> - **Municipality × dementia does not exist.** Japan's 介護DB open data publishes
>   dementia (認知症高齢者自立度) by prefecture and by age — but the 保険者
>   (municipality) file contains *only* application category and care level. The
>   geography and the outcome are never crossed. **Tier 3, the only identified design,
>   is impossible.**
> - **Prefecture × age × dementia does not exist.** 表1-15 is dementia × prefecture with
>   no age; 表2-15 is dementia × age with no prefecture. They are marginal tables, not a
>   cross-tab. **Tier 1 cannot be age-standardised**, so it would reproduce the exact
>   artefact this project exists to correct.
> - **The denominator is applicants, not population** (1,624,300 certification
>   applications in 2023), a selected group.
>
> This supersedes the power analysis in §9 — we never reach the question of whether the
> study is powered, because it cannot be assembled.
>
> **Unblocking requires a formal 介護DB research application to MHLW** (Japanese
> institutional affiliation + ethics review, multi-month), and even then §9.2 says the
> design detects only a ~31% effect.
>
> **Recommendation: go to Ontario instead** — `docs/02_the_ontario_25hz_experiment.md`.
>
> The material below is retained because the design reasoning remains correct and would
> apply if 介護DB access were obtained.

---

> ## ⭐ AMENDMENT (2026-07-17): the boundary MOVED — a better Japan design exists
>
> The spatial-boundary framing of §3 is **not the strongest Japan design**, and the
> static 50/60 map every prior analysis has used (including the original chart) is
> **wrong for 9 of 47 prefectures**.
>
> **Five documented conversions, 1943–1961** (`data/reference/frequency_conversions.csv`,
> sourced in `data/reference/SOURCES.md`):
>
> | Region | Change | When | Confidence |
> |---|---|---|---|
> | Eastern Kyushu — **all of Ōita, all of Miyazaki**, E. Fukuoka, E. Kagoshima, Minamata | **50→60** | 1949-12 → 1960-06 | confirmed |
> | Hokkaido west — Sapporo, Otaru, Hakodate | **60→50** | 1943-06 → 1946 | confirmed |
> | Jōban — N. Ibaraki (Mito, Hitachi), S. Fukushima (Iwaki) | **60→50** | 1961 | confirmed |
> | Sado island | **50→60** | ~1954 (date uncertain) | fact solid, date not |
> | Nagano (Chubu area) | **50→60** | by 1961-03 | strong |
>
> **Why this is a better design than §3.1:**
>
> - **Ōita and Miyazaki converted at whole-prefecture scale.** That matches the *only*
>   granularity Japan's public dementia data offers (prefecture), instead of requiring
>   the municipality data that does not exist.
> - **It runs in both directions** (Kyushu 50→60; Hokkaido and Jōban 60→50), permitting
>   a dose-response symmetry test rather than a single-direction contrast.
> - **It is temporal**, giving within-prefecture, across-birth-cohort dose variation —
>   which strips out the fixed East/West confounding (diet, urbanisation, culture) that
>   cripples the cross-sectional design. This is the same structural advantage that
>   makes the Ontario experiment strong.
> - **Exposure lands in early/mid life**, the aetiologically relevant window, rather
>   than at current residence.
>
> **Why it is still blocked:** it needs dementia × prefecture × **age** (to construct
> birth cohorts). 表1-15 has dementia × prefecture with no age; 表2-15 has dementia × age
> with no prefecture. Same wall as everything else — see §Data availability above.
>
> **Consequence for the original chart:** coding Ōita and Miyazaki as "60 Hz" for a
> 1990–2021 analysis assigns the wrong exposure to everyone born before ~1960 — i.e.
> precisely the cohort now developing dementia. This is an *additional*, independent
> error beyond the age-structure confounding of Finding 3.
>
> **Caveats:** the Hokkaido conversion is confounded by the war years. No
> municipality-level cutover timetable survives for Hokkaido 1943–46 or Kyushu Phase 2
> (1954–60), so those are **~3-year rolling transitions, not step functions**. Sado is
> an islanded grid, so its 60 Hz is confounded with insularity.

---

## 1. Background and motivation

Japan's electricity grid is split between 50 Hz (east) and 60 Hz (west). The boundary
originates in an 1890s procurement accident: Tokyo Electric Light purchased German
AEG 50 Hz generators, Osaka Electric Lamp purchased American General Electric 60 Hz
generators. The line has been essentially fixed since, and runs through Shizuoka
Prefecture along the Fuji River.

This makes frequency **plausibly exogenous to health** within Japan — the identifying
assumption of this study, and the reason the design is worth running at all. The same
cannot be said internationally, where mains frequency is a proxy for which empire
electrified a country (see `docs/01_why_international_comparison_fails.md`).

## 2. The mechanistic hypothesis, and its direction

This is the part the motivating intuition leaves dangerously vague, so we pin it down
here. **An unsigned hypothesis is unfalsifiable and we will not test one.**

Two distinct exposures are conflated in casual statements of "electrical flicker":

| Exposure | Frequency under 50 Hz mains | Under 60 Hz mains |
|---|---|---|
| **Luminous flicker** (light output peaks twice per AC cycle) | 100 Hz | 120 Hz |
| **ELF electromagnetic field** | 50 Hz | 60 Hz |

### 2.1 Signed prediction under the gamma-entrainment mechanism

If the motivation is the Tsai/GENUS 40 Hz work, then the relevant quantity is how well
ambient flicker could drive 40 Hz gamma. Note:

- 120 Hz = **3 × 40 Hz** — an exact third harmonic of gamma.
- 100 Hz = 2.5 × 40 Hz — no integer relationship.

If subharmonic entrainment contributes at all, **60 Hz mains should be *protective***,
producing *less* dementia than 50 Hz. This is the a priori signed prediction of H1.

**This is the opposite of what the initial chart appeared to show.** That chart showed
60 Hz with *higher* rates. If that pattern were real, it would contradict the mechanism
it was invoked to support. We flag this now so it cannot be rationalised later.

### 2.2 Signed prediction under the ELF-EMF mechanism

None available. The occupational ELF-EMF and neurodegeneration literature is weak,
confounded by co-exposures (solvents in electrical trades), and offers no basis for
predicting 60 > 50 or 50 > 60. **We therefore do not treat ELF-EMF as a testable
mechanism here** and confine confirmatory testing to §2.1.

### 2.3 Exposure-contrast decay — a threat to the whole enterprise

The 100/120 Hz luminous contrast has been eroding for decades:

- High-frequency inverter ballasts (tens of kHz) displaced magnetic-ballast
  fluorescents in Japan comparatively early.
- LED lighting (post ~2010) has flicker set by driver electronics, not mains.
- Screens refresh at 60/120/144 Hz irrespective of mains frequency.

So the true exposure contrast is likely far smaller than the nominal 50-vs-60 label,
and shrinking across exactly the period our outcome data covers. **This biases the
study toward the null for reasons unrelated to the truth of the hypothesis**, and must
be stated in any report. An exposure-measurement substudy (§10) is the only fix.

## 3. Design

Three tiers, in ascending order of credibility. **Tier 3 is the confirmatory design.**
Tiers 1–2 are descriptive and will be reported as such.

- **Tier 1 — Prefecture ecological (descriptive only).** n=47. Reported to demonstrate
  whether the crude gap in the initial chart survives age standardisation. Not
  confirmatory: n=47 with spatial autocorrelation and East/West confounding has
  negligible power and no credible identification.
- **Tier 2 — Municipality ecological (descriptive only).** n≈1,700. Better resolution,
  same identification problem.
- **Tier 3 — Spatial regression discontinuity at the frequency boundary (confirmatory).**

### 3.1 Tier 3 specification

**Estimand:** the local average treatment effect of 60 Hz vs 50 Hz supply on
age-standardised dementia prevalence, at the frequency boundary.

**Running variable:** signed geodesic distance from municipality population centroid to
the frequency boundary polyline. Negative = 50 Hz side, positive = 60 Hz side.

**Model:** local linear regression, triangular kernel, MSE-optimal bandwidth
(Calonico–Cattaneo–Titiunik), robust bias-corrected confidence intervals.

```
Y_m = α + τ·1[dist_m > 0] + f(dist_m) + ε_m
```

**Preferred variant — within-Shizuoka.** Restricting to Shizuoka municipalities holds
prefecture constant: same prefectural health policy, same LTCI administration, same
climate, same regional diet, same registration practice. This is the cleanest contrast
available anywhere on Earth for this question. It is also small (~35 municipalities),
so it will be underpowered; we report it regardless, as a bound.

**Secondary variant — 2D geographic RD.** Latitude/longitude polynomial with boundary
segment fixed effects (Dell 2010 style), pooling the Shizuoka, Niigata and Nagano
boundary segments.

## 4. Data sources

See `data/raw/PROVENANCE.md` for exact retrieval instructions and dates.

**Outcome (preferred):** Japan Long-Term Care Insurance (介護保険事業状況報告).
Since 2000 every applicant receives a standardised nationwide dementia assessment
(認知症高齢者の日常生活自立度). Municipality-level, uniform national instrument,
*measured* rather than modelled. Retrieved via e-Stat.

**Outcome (~~fallback~~ — DEMOTED, likely unusable):** IHME GBD Japan subnational
prevalence. GBD 2021 does contain all 47 prefectures (ids 35424–35470, prevalence and
incidence, 5-year bands to 95+, 1990–2021), so the data exists and is obtainable.

**But IHME's own Japan subnational paper states the regional variation may not be real:**

> "Data gaps remain at both the national and prefectural levels. GBD disease models
> compensate by using regional data and covariates, potentially resulting in **minimal
> regional variation** in certain diseases and risk factors due to limited Japanese data
> coverage." — *Lancet Public Health*, Mar 2025, Limitations

Our exposure varies between prefectures. If the outcome's between-prefecture variation
is model output rather than measurement, regressing one on the other is near-circular.
**GBD is therefore not fit for this purpose** unless the methods appendix demonstrates
genuine prefecture-level dementia inputs — an open task. See `data/raw/PROVENANCE.md` §4.

This is not a minor caveat. It removes the fallback and makes LTCI load-bearing.

**Denominator:** Census (国勢調査) / population estimates, prefecture and municipality
× 5-year age bands, via e-Stat.

**Exposure:** `data/reference/prefecture_frequency.csv` — built and cited in
`data/reference/SOURCES.md`.

## 5. Outcome definitions

**Primary outcome (ONE, pre-specified):** age-standardised prevalence of dementia
(LTCI independence level II or above), both sexes, ages 65+, most recent year with
complete municipality coverage.

Everything else — other years, sex strata, age strata, severity thresholds — is
**secondary and exploratory**. This is stated to prevent the multiple-comparisons
disaster that years × sexes × ages × severities × outcomes would otherwise produce.

## 6. Age standardisation

Direct standardisation, 5-year bands: 65–69, 70–74, 75–79, 80–84, 85–89, 90–94, 95+.
Reference population: Japan 2015 Census (sensitivity: WHO World Standard).

**Coarse bands are not acceptable.** An open-ended 80+ bucket leaves large residual
confounding, because the within-bucket age distribution differs substantially between
regions. If only coarse bands prove obtainable, that is a reason to report the analysis
as inconclusive, not a reason to proceed with them.

## 7. Falsification and balance

**Placebo outcomes** (no plausible flicker mechanism; should show no discontinuity):
colorectal cancer incidence, stroke, ischaemic heart disease, hip fracture,
all-cause mortality.

If any placebo outcome shows a discontinuity at the boundary, the design is
**invalid** — the boundary is capturing a cultural, economic or geographic
discontinuity (the Fossa Magna is a real East/West divide in Japan, not only an
electrical one). We will report this and stop, rather than reporting the primary
result alongside it.

**Balance tests** (should be continuous at the boundary): median income, urbanicity /
population density, educational attainment, physician density, % over 75.

## 8. Statistical decision rule

Fixed in advance:

We will report the primary estimate as **"consistent with a real effect"** only if
**all** of the following hold:

1. Tier 3 primary RD estimate significant at **α = 0.005** (not 0.05 — justified by
   the low prior; cf. Benjamin et al. 2018).
2. Sign matches the §2.1 prediction (60 Hz protective).
3. **All** placebo outcomes null at α = 0.05.
4. Covariate balance holds at the boundary.
5. Estimate stable across bandwidths (½×, 1×, 2× the MSE-optimal bandwidth).

Failing any of these, we report **an upper bound on the effect size** and a null.

### 8.1 Honest Bayesian framing

Our prior against the hypothesis is strong — call it somewhere in the region of 1:1000.
A single ecological study clearing p<0.005 yields a Bayes factor nowhere near enough to
overturn that. **This design cannot confirm the hypothesis.** It can only:

- fail to refute it, and place a bound; or
- refute it, by placing a bound tight enough to exclude effects worth caring about.

We state this so that a positive result is not oversold if one appears. A surprising
positive here is a reason to seek individual-level replication, not a finding.

## 9. Power

The minimum detectable effect will be reported **before** the primary model is fitted,
and reported in the paper regardless of outcome. Computed by `src/power.py`.

### 9.1 Preliminary MDE (placeholder parameters)

Assuming baseline age-standardised dementia prevalence of 13,000/100k among 65+ and a
between-municipality SD of 15% of the mean, at α=0.005 and 80% power:

| Design | n | MDE | MDE as % of baseline |
|---|---|---|---|
| Tier 1: prefecture ecological | 47 | 2,145/100k | **16.5%** |
| Tier 2: municipality ecological | ~1,700 | 345/100k | **2.7%** |
| Tier 3: RD within Shizuoka *(confirmatory)* | ~35 | 4,047/100k | **31.1%** |
| Tier 3: RD pooled segments | ~120 | 2,154/100k | **16.6%** |

These are placeholders pending real denominators and real variance. Rerun before
fitting.

### 9.2 The central tension — read this before running anything

**The design with power has no identification; the design with identification has no
power.**

- Tier 2 can detect a 2.7% difference — but its contrast is East vs West Japan, which
  is confounded by diet, urbanisation, migration and culture. A 2.7% signal there means
  nothing.
- Tier 3 is the only design where frequency is plausibly exogenous — but it can only
  detect a **~31% shift in dementia prevalence**.

A 20% difference in the frequency of an ambient exposure — whose *delivered* contrast
has been eroding since inverter ballasts and LEDs (§2.3) — producing a 31% shift in
dementia prevalence is not a plausible effect size by any mechanism we can articulate.

**Therefore the expected outcome of this study is "uninformative", not "null".** That
distinction is not pedantry: a null bounds the effect, an uninformative result bounds
nothing. We commit to reporting it as uninformative if the MDE exceeds the plausible
effect range, rather than presenting a failure to detect as evidence of absence.

### 9.3 Consequence for project sequencing

If §9.2 holds after real parameters are substituted, the rational order of work is:

1. **Exposure-measurement substudy first** (§10). If measured flicker/ELF contrast
   across the boundary is near zero, no observational design on modern Japanese data
   can test this hypothesis, and the question is retired for the price of a photodiode.
2. **Higher-contrast natural experiments** (§11) — 25 Hz Ontario, 16.7 Hz railway
   cohorts — which offer far more signal per unit of effort.
3. **Japan 50/60 epidemiology last**, and only if 1 and 2 leave the hypothesis alive.

Running the epidemiology first, as originally contemplated, spends the most effort on
the least informative step.

## 10. Exposure-measurement substudy (proposed, not yet funded)

The single highest-value addition. Measure, in dwellings on both sides of the Fuji
River boundary: luminous flicker spectra and modulation depth (photodiode + FFT), and
ELF magnetic field strength. If measured exposure contrast is near zero — which §2.3
suggests is likely for the LED era — then **no observational design on modern data can
test this hypothesis**, and that finding retires the question more efficiently than any
amount of epidemiology.

## 11. Higher-contrast natural experiments (recommended before investing further)

50-vs-60 is a 20% contrast in an ambient exposure. Far larger contrasts exist and
should be checked first, as cheap falsification:

- **25 Hz Southwestern Ontario — now the recommended primary study.** See
  `docs/02_the_ontario_25hz_experiment.md` for the full design. Toronto/Niagara/Windsor
  ran at 25 Hz until an Ontario Hydro conversion programme in **1949–1959**.
  25 Hz mains → **50 Hz luminous flicker** → *visible*, and **in the gamma band**.
  This is the only large human population ever to live under sustained ambient flicker
  near 40 Hz — essentially the GENUS condition, delivered unintentionally, for decades.
  The 1949–59 conversion gives within-municipality, across-birth-cohort dose variation,
  and Ontario's ICES holds individual-level linkable dementia data with residential
  history. Bigger contrast, signed prediction, dose-response, individual-level data,
  exposure in the aetiologically relevant window, and no exposure-decay problem.
- **16.7 Hz railway electrification** (Germany, Austria, Switzerland, Sweden, Norway).
  Swiss railway worker cohorts have already been assembled for EMF and
  neurodegenerative endpoints; reanalysis may be possible without new data collection.
- **Frequency conversions.** Any region historically converted between frequencies
  provides a within-region temporal contrast, which is stronger than any cross-section.

## 12. What will be reported regardless of outcome

The null, the bound, the MDE, all placebo results, all balance tests, the exposure-decay
argument of §2.3, and this document unedited. Pre-registration is worthless if only the
interesting branch is published.
