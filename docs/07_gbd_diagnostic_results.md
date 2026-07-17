# GBD diagnostic results: the surface is too flat to test, and the contrast is east/west

**Run 2026-07-17.** Data: GBD 2021, age-standardised prevalence per 100k, both sexes,
47 Japan prefectures, 1990–2021, five causes. `data/raw/gbd2021_japan_prefecture_asr.csv`
(7,680 rows; location_ids 35424–35470 verified as GBD 2021, plus Japan national).

Reproduce: `python src/05_gbd_diagnostic.py` · figure: `python src/06_figures.py`

**Two independent findings, either of which is fatal. Together they close the GBD route.**

---

## Finding 1 — the dementia surface is flat, as IHME implied

Between-prefecture coefficient of variation, 2021:

| Cause | CV | max/min | role |
|---|---|---|---|
| **Alzheimer's & dementias** | **4.3%** | 1.39 | outcome |
| Ischemic heart disease | 4.6% | 1.25 | placebo |
| Colon & rectum cancer | 8.9% | 1.60 | placebo |
| **Stroke** | **9.6%** | 1.47 | comparator, real variation |
| **Stomach cancer** | **12.4%** | 2.06 | comparator, real variation |

**CV(Alzheimer's) / CV(Stroke) = 0.44. CV(Alzheimer's) / CV(Stomach cancer) = 0.34.**

Stroke and stomach cancer have large, real, well-documented regional variation in Japan —
the stroke gradient tracks salt intake (Tohoku elevated); stomach cancer tracks
*H. pylori* and diet. Japan measures both well. **Dementia varies about a third as much.**

**Stable across the entire series.** Alzheimer's CV runs 4.3–5.7% for 32 years while
stomach cancer runs 12.2–13.0%. Alzheimer's ranks among the two flattest surfaces in
**32 of 32 years**.

This is the empirical version of IHME's own statement — *"GBD disease models compensate by
using regional data and covariates, potentially resulting in minimal regional variation…
due to limited Japanese data coverage."* We no longer take it on faith; the numbers show
it.

**Consequence: any 50-vs-60 test on this surface is UNINFORMATIVE, not null.** A surface
this flat cannot show an association with anything. Failure to find an effect here is not
evidence of absence.

---

## Finding 2 — the 50/60 contrast is east-vs-west Japan, and the placebo proves it

Excluding the 9 prefectures whose frequency changed 1943–61
(`data/reference/frequency_conversions.csv`). Ratio = 60 Hz / 50 Hz, 2021:

| Cause | 50 Hz | 60 Hz | ratio | p | role |
|---|---|---|---|---|---|
| Colon & rectum cancer | 332.0 | 296.8 | **0.895** | **0.000** | **placebo** |
| Stroke | 1,237.3 | 1,124.5 | 0.912 | 0.013 | real variation |
| Stomach cancer | 86.1 | 81.1 | 0.945 | 0.196 | real variation |
| **Alzheimer's & dementias** | 675.5 | 663.0 | **0.981** | **0.044** | **outcome** |
| Ischemic heart disease | 773.0 | 789.9 | 1.024 | 0.289 | placebo |

**The placebo separates ~5× harder than the outcome.** Colon and rectum cancer — which
has no flicker mechanism whatsoever — differs by **10.5% at p<0.001**, while Alzheimer's
differs by 1.9% at p=0.044.

**Stroke behaves exactly as known biology predicts** (50 Hz east = Tohoku = more stroke,
the salt gradient, p=0.013). That is not a nuisance result — it is a **positive control
that confirms what the contrast is actually measuring**: the 50/60 line is a proxy for
eastern vs western Japan.

Note the systematic pattern: **four of five causes are higher in the east**, and
Alzheimer's shows the *smallest* east/west gradient of any of them. The dementia
"difference" is a pale echo of a general east–west gradient that hits the placebo five
times harder.

---

## Against the pre-registered decision rule

`METHODS.md` §8 fixed five criteria in advance. Scoring honestly:

| # | Criterion | Result |
|---|---|---|
| 1 | Primary significant at **α = 0.005** | ❌ **p = 0.044** — fails by an order of magnitude |
| 2 | Sign matches §2.1 prediction (60 Hz protective) | ✅ ratio 0.981 — 60 Hz *is* lower |
| 3 | **All** placebos null at α = 0.05 | ❌ **colon cancer p < 0.001** |
| 4 | Covariate balance | — not applicable to this design |
| 5 | Stable across bandwidths | — not applicable to this design |

**Fails 1 and 3. Per §7, a placebo that moves invalidates the design** — we report that
and stop, rather than presenting the primary estimate as though it were interpretable.

### The trap this avoided, stated plainly

Criterion 2 **passed**. Alzheimer's is 1.9% lower at 60 Hz, and that is the direction the
gamma-harmonic argument predicts (120 Hz = 3 × 40 Hz → 60 Hz protective). Looked at
alone, p=0.044 with the mechanistically-predicted sign is exactly the result that gets
written up.

The placebo is what stops it. Colon cancer moves in the same direction, five times
harder, at p<0.001. **The mechanism did not produce the dementia difference; eastern
Japan did.** Pre-registering α=0.005 and the placebo set before seeing the data is the
only reason this is a clean negative instead of a paper.

---

## Verdict

**The GBD route is closed, twice over.**

1. The surface is too flat to carry a signal (Finding 1) — so the test is uninformative
   regardless of outcome.
2. The contrast is east/west Japan, not electricity (Finding 2) — so any signal it did
   carry would be uninterpretable.

Combined with `docs/03` (municipality × dementia does not exist; prefecture × age ×
dementia does not exist) and `docs/06` (the population cohorts have ascertainment
collinear with frequency), **every Japan route is now closed.**

## What would a real signal have looked like?

Worth stating, so the null is falsifiable rather than rhetorical:

- Alzheimer's CV comparable to stroke's (~10%), showing the surface carries real
  prefecture-level information;
- an Alzheimer's ratio clearing p<0.005;
- **and placebos flat**, showing the boundary does nothing to causes without a mechanism.

None of the three holds. That is not a marginal miss.

## Figure

`figures/gbd_diagnostic.png` — panel A: dispersion by cause over 32 years; panel B: the
50/60 contrast with placebos.
