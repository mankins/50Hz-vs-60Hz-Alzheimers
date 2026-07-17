# 50 vs 60 Hz and Alzheimer's Disease

An attempt to test, rigorously, whether mains electricity frequency (50 Hz vs 60 Hz)
is associated with Alzheimer's disease / dementia burden — using Japan's internal
frequency split as a natural experiment.

## Context and Commentary

> [!NOTE]
> I, Matt Mankins (mankins@gmail.com), am not a scientist trained in the fields presented here. Do not take this for anything other than what it is: a single-session journey with Anthropic's Claude Code to investigate a whim I had many decades ago--I wondered if the addition of electricity to modern life had anything to do with the rise of some diseases, such as Alzheimer's, a disease that took my grandmother. (The conclusions here seem to indicate that no, there's nothing here.)
>
> What I find interesting was the use of AI to bring me into domains that I would have previously had no ability to interface with. For example in this report we had to both navigate Japanese as well as the domain-specific jargon, and do that while designing an experimental environment that would isolate variables and be actually testable. In my day-to-day doing web or ai platform programming, that's just not something I do. 
>
> Yet by being curious and asking, I was able to get an answer. Was it the _right_ answer? I think so, but would need to defer to others with more skills to evaluate what was done. This is the AI loop entirely: have a need, collaborate with AI, reach a result, validate with humans. 
>
> To me the excitement of AI is not that it will do my job for me, but that it will help me understand different parts of the world quicker than I otherwise would be able to. With this new understanding, I can then synthesize, create, and combine to make art, tools, and build knowledge.

## → Read [`REPORT.pdf`](./REPORT.pdf) first (14 pp). It is the synthesis of everything below.

**Status: CONCLUDED (2026-07-17). The hypothesis cannot be tested with existing data.**

Three independent routes were pursued to exhaustion; each closed for a different reason.
This is a stronger result than a null — a null would leave "maybe with more data" open.
These findings close specific doors with evidence.

| Route | Status | Why |
|---|---|---|
| International (50/60 by country) | **Closed** | Frequency is a proxy for which empire electrified you. The exposure *is* the confounder. |
| Japan administrative data | **Closed** | Dementia × municipality does not exist. Dementia × prefecture has no age dimension. |
| Japan modelled estimates (GBD) | **Closed** | The dementia surface is measurably flat; a placebo separates 5× harder than the outcome. |
| Japan population cohorts | **Closed** | Case-finding intensity is collinear with frequency. |
| Ontario 25 Hz experiment | **Closed** | Exposure was real and large, but 1950s residence was never recorded. |

**The one finding that runs the other way:** the historical Ontario exposure was real and
measured — ~30% luminous modulation at 25 Hz vs ~12.5% at 60 Hz. **The physics is sound;
the measurement is what fails.**

**The number that reframes it all:** the luminous-flicker contrast between 50 and 60 Hz
mains is **1.2×** — a 20% difference in modulation depth of a stimulus below conscious
perception. That is the entire signal Japan ever offered.

---

## The hypothesis

Ambient flicker from mains electricity influences Alzheimer's disease risk. Motivated by:

1. The observation that clinically recognised Alzheimer's is rare in the historical
   record before electrification.
2. The MIT / Tsai lab "GENUS" work showing 40 Hz sensory entrainment reduces amyloid
   burden in mouse models — establishing that the brain is, in principle, responsive
   to flicker in this frequency neighbourhood.

Japan is the natural test bed: a largely homogeneous population, one health system,
one death-registration practice, split down the middle between 50 Hz (east) and
60 Hz (west) by an accident of 1890s generator procurement.

## Why this repo exists

An initial analysis (see `docs/original_chart_UNRELIABLE.png`) appeared to show a clean
separation: 60 Hz > 50 Hz Alzheimer's rates, with "mixed" regions highest. That chart
does not survive scrutiny — see `docs/00_critique_of_initial_analysis.md`. In short it
used a crude, non-age-standardised **mortality** measure across groups with radically
different age structures, and its pre-1990 segment cannot be produced from the cited
sources at all.

This repo rebuilds the analysis from the ground up with:

- **Prevalence**, not probability of death (Alzheimer's mortality largely measures
  death-certificate coding practice, not disease).
- **Age-standardised** rates using 5-year bands — non-negotiable for a disease whose
  incidence roughly doubles every 5 years after 65.
- **Within-Japan** contrast only. The international 50/60 comparison is abandoned:
  mains frequency at country level is a proxy for 20th-century imperial alignment
  (see `docs/01_why_international_comparison_fails.md`), which is confounded with
  every determinant of both dementia risk and dementia *measurement*.
- A **pre-registered** analysis plan with placebo outcomes and a stated decision rule,
  written before results are examined (`METHODS.md`).

## Repository layout

```
├── REPORT.md / REPORT.pdf   ** THE SYNTHESIS. Start here. **
├── METHODS.md          Pre-registration: signed hypothesis, gated pipeline, decision rule
├── LIMITATIONS.md      Written before results, so nothing could be dropped later
├── docs/
│   ├── 00_critique_of_initial_analysis.md      why the original chart fails (8 findings)
│   ├── 01_why_international_comparison_fails.md   the colonial-history argument
│   ├── 02_the_ontario_25hz_experiment.md       the Ontario design (verdict revised)
│   ├── 03_japan_data_availability.md           THE Japan blocker, verified
│   ├── 04_ontario_ices_feasibility.md          the exposure was never recorded
│   ├── 05_ontario_25hz_flicker_physics.md      primary sources 1906–1930; 30% measured
│   ├── 06_japan_population_surveys.md          JPSC-AD ascertainment confound
│   ├── 07_gbd_diagnostic_results.md            the flat surface + the placebo
│   └── 08_ontario_conversion_schedule.md       reusable artifact: 1949–59 dates
├── data/
│   ├── raw/            Untouched downloads + PROVENANCE.md (every source, every step)
│   ├── reference/      prefecture→frequency map + the 5 conversions, fully cited
│   └── processed/      Derived. Safe to delete and regenerate.
├── src/                Numbered pipeline; agestd.py has 11 passing tests
├── figures/            gbd_diagnostic.png
└── output/             Model results
```

## Two artifacts with value beyond this hypothesis

- **`data/reference/`** — a **time-varying** Japanese prefecture-frequency map covering
  five documented conversions (1943–61), fully cited, including corrections to errors
  that have propagated through Wikipedia for fifteen years.
- **`docs/08`** — a collated Ontario municipal conversion schedule (1949–59), which does
  not appear to exist elsewhere.

## Reproducing

```bash
pip install -r requirements.txt
python src/01_build_frequency_map.py    # builds prefecture→frequency reference table
python src/02_fetch_data.py             # downloads raw data (see PROVENANCE.md for manual steps)
python src/03_age_standardize.py        # direct standardisation to reference population
python src/04_analysis.py               # primary + placebo models
```

Any step requiring manual download (data-use agreements, API keys) is documented in
`data/raw/PROVENANCE.md` with exact instructions rather than being silently skipped.

## Key design decisions, up front

| Decision | Choice | Why |
|---|---|---|
| Outcome measure | Prevalence (and incidence where available) | Mortality ≈ coding practice |
| Standardisation | Direct, 5-year bands to 95+ | Risk doubles every ~5 yrs; coarse bands leave residual confounding |
| Geographic unit | Municipality where possible, prefecture as fallback | n=47 prefectures has near-zero power |
| Primary design | Spatial regression discontinuity at the frequency boundary | The only place frequency is plausibly exogenous |
| Falsification | Placebo outcomes across the same boundary | If colorectal cancer also jumps, the design is broken |

## State of play (2026-07-17)

**0. The Japan study cannot be done with public data — and this is the useful result.**
Not "underpowered." Not assemblable. Japan's 介護DB *does* publish real, measured
dementia assessments (認知症高齢者自立度), and it *does* have municipality geography
(1,571 insurers, coded) — **but never crossed.** The municipality file carries only
application category and care level; dementia stops at prefecture. And dementia ×
prefecture has no age dimension, so it cannot be age-standardised — meaning a prefecture
analysis would reproduce the exact artefact that discredited the original chart.
Verified empirically; files retained in `data/raw/kaigodb/`. See
`docs/03_japan_data_availability.md`. Unblocking needs a formal MHLW 介護DB application
(Japanese institution + ethics, multi-month) for a design already known to detect only a
~31% effect.

Four further findings, in descending order of how much they change the project.

**1. There is a much better experiment than Japan, and it is in Ontario.**
Southwestern Ontario ran at **25 Hz** until a 1949–59 conversion. 25 Hz mains produces
**50 Hz luminous flicker** — visible, and *in the gamma band*. That population is the
only large human group ever to have lived under sustained ambient flicker near 40 Hz,
which is essentially the GENUS condition delivered unintentionally for decades. It gives
a signed prediction, a continuous dose, within-municipality cohort variation, and
individual-level ICES data. See `docs/02_the_ontario_25hz_experiment.md`.

**2. The Japan design cannot detect a plausible effect.** The design with power has no
identification; the design with identification has no power. The confirmatory variant
(RD within Shizuoka) has an MDE of **~31% of baseline prevalence**. Expected outcome is
therefore **uninformative, not null** — a materially different claim. `METHODS.md` §9.

**3. GBD subnational is probably unusable for this question.** GBD 2021 *does* contain
all 47 prefectures (verified live). But IHME's own Japan paper says: *"GBD disease
models compensate by using regional data and covariates, potentially resulting in
minimal regional variation ... due to limited Japanese data coverage."* Our exposure
varies between prefectures; if the outcome's between-prefecture variation is model
output, the test is near-circular. `data/raw/PROVENANCE.md` §4.

**4. The original chart's gaps are smaller than its own uncontrolled confounder.**
Age structure alone, with zero effect present, generates a **1.75×** crude gap in a
realistic Japan-like contrast. The chart's gaps are ~1.04× and ~1.13×. Run
`python src/test_agestd.py`.

## Authors' stance

This is a low-prior hypothesis being given a fair test. We are pre-registering because
the researcher degrees of freedom here are enormous and we would certainly find
*something* if we looked freely.




