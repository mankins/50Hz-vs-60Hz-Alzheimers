---
title: "Can the mains-frequency hypothesis for Alzheimer's disease be tested?"
subtitle: "A feasibility investigation into 50 Hz vs 60 Hz electricity and dementia"
date: "17 July 2026"
geometry: margin=1in
fontsize: 11pt
linkcolor: black
urlcolor: blue
toc: true
toc-depth: 2
---

\newpage

# Summary

**The hypothesis is that ambient flicker from mains electricity influences Alzheimer's
disease risk.** Japan, uniquely, is split between 50 Hz (east) and 60 Hz (west) by an
accident of 1890s generator procurement, which appears to offer a natural experiment.

**The answer is no — not with data that exists.** Three independent routes were pursued
to exhaustion and each closed for a different reason. This is a stronger and more useful
result than a null: a null would leave "maybe with more data" open. These findings close
specific doors with evidence.

| Route | Status | Why |
|---|---|---|
| International (50/60 Hz by country) | **Closed** | Mains frequency is a proxy for which empire electrified a country. The exposure *is* the confounder. |
| Japan administrative data | **Closed** | Dementia by municipality does not exist. Dementia by prefecture has no age dimension. |
| Japan modelled estimates (GBD) | **Closed** | The dementia surface is measurably flat, and the 50/60 contrast moves a placebo five times harder than the outcome. |
| Japan population cohorts | **Closed** | The only cohort with a frequency contrast has case-finding intensity collinear with frequency. |
| Ontario 25 Hz natural experiment | **Closed** | The exposure was real and large, but 1950s residence was never recorded and cannot be reconstructed. |

**One finding runs the other way and is worth keeping:** the historical exposure in
Ontario was real, measured, and substantial — ~30% luminous modulation at 25 Hz mains,
versus ~12.5% at 60 Hz. The physical premise of the hypothesis is sound. What fails is
measurement, not physics.

**A number that reframes the whole question:** the luminous-flicker contrast between
50 Hz and 60 Hz mains is **1.2×** — a 20% difference in modulation depth of a stimulus
that sits below conscious perception. That is the entire signal the Japan study was ever
chasing.

\newpage

# 1. The question and the mechanism

## 1.1 Origin

Two observations motivate the hypothesis:

1. Clinically recognised Alzheimer's is rare in the historical record before
   electrification.
2. The MIT/Tsai "GENUS" work shows 40 Hz sensory entrainment reduces amyloid burden in
   mouse models — establishing that the brain is, in principle, responsive to flicker in
   this frequency neighbourhood.

**Observation 1 does not survive scrutiny.** Life expectancy at birth in 1900 was ~47;
the 85+ demographic, where prevalence reaches 30–40%, barely existed. Alzheimer's was
described only in 1906, and for seventy years the label meant *presenile* dementia only —
dementia in the old was "senility", considered normal ageing and not counted. Katzman's
1976 reclassification accounts for much of the apparent epidemic. Electrification also
correlates near-perfectly with refrigeration, plumbing, antibiotics, and longevity
itself. Any argument of this shape is nearly uninformative; the same structure supports
aluminium, plastics, seed oils, and WiFi.

**Observation 2 is real but points the other way.** See §1.3.

## 1.2 Two exposures are conflated

"Electrical flicker" hides two distinct physical quantities:

| Exposure | Under 50 Hz mains | Under 60 Hz mains |
|---|---|---|
| **Luminous flicker** (light peaks twice per AC cycle) | 100 Hz | 120 Hz |
| **ELF electromagnetic field** | 50 Hz | 60 Hz |

The ELF-EMF framing has a forty-year occupational literature that is weak and confounded
by co-exposures (solvents in electrical trades), and offers no basis for predicting a
direction. It was set aside as untestable here.

## 1.3 The signed prediction — and it contradicts the original finding

An unsigned hypothesis is unfalsifiable. Taking the 40 Hz mechanism seriously:

- **120 Hz = 3 x 40 Hz** — an exact third harmonic of gamma.
- 100 Hz = 2.5 x 40 Hz — no integer relationship.

If subharmonic entrainment contributes at all, **60 Hz mains should be *protective***.

**The initial analysis showed the opposite** — 60 Hz with *higher* rates. If that pattern
were real it would contradict the mechanism invoked to support it. This was recorded
before any data was examined, so it could not be rationalised later.

## 1.4 The exposure contrast is small and shrinking

Measured, from primary sources (§6): luminous modulation scales as 1/f, so the
**50-vs-60 contrast is 1.2×**. Further, the contrast has been eroding for decades — Japan
adopted high-frequency inverter ballasts early (tens of kHz, erasing the distinction
indoors), LED flicker is set by driver electronics rather than mains, and screens refresh
at 60/120/144 Hz regardless. **Any null result is therefore partly uninformative for
reasons unrelated to the hypothesis's truth.**

\newpage

# 2. Why the initial analysis failed

The starting point was a chart showing mean Alzheimer's rate in Japan by electricity
frequency, 1980–2021, with 60 Hz and "Mixed" above 50 Hz.

**It could not have been built from its stated sources.** Those were country-level (IHME
GBD 2021, World Bank electricity access, Wikipedia mains frequency by country). A chart
split by Japanese prefecture requires subnational data that none of them contain.

**Its 1980–1989 segment does not exist in any cited source.** GBD 2021 begins in 1990.
This exactly explains the ~14x discontinuity at 1990 (~25 → ~350 per 100k) — a data seam,
not biology. The pre-1990 values are plausible as *mortality*; the post-1990 values as
*prevalence*. Two different quantities on one axis.

**The measure was wrong.** GBD "Probability of death" is a mortality measure. People with
Alzheimer's overwhelmingly die *of* pneumonia, sepsis, falls, or cardiac events; whether
"Alzheimer's" is recorded as the underlying cause is an administrative decision varying
by an order of magnitude between countries. **Alzheimer's mortality statistics
substantially measure death-certificate coding practice.**

**The gaps were smaller than the confounder.** The measure was a crude all-ages rate, and
dementia risk roughly doubles every five years after 65 — so a crude all-ages rate is
very nearly a measurement of what fraction of the population is over 75. Simulating two
populations with *byte-identical* age-specific risk but realistic differing age
structures:

| Quantity | Value |
|---|---|
| Spurious crude gap from age structure **alone** | **1.75x (75%)** |
| Observed gap, 60 Hz vs 50 Hz | ~1.04x (~4%) |
| Observed gap, Mixed vs 50 Hz | ~1.13x (~13%) |

Both observed gaps sit **well inside** what demography generates with no effect present.
Direct standardisation removes the simulated gap entirely. *(Reproduce:
`python src/test_agestd.py`.)*

**"Mixed" was Japan.** In a country-level classification, mixed-frequency is a tiny
bucket of which Japan is the canonical member — and Japan has the oldest population on
Earth. The top line was Japanese demography, essentially unmediated. Meanwhile the 50 Hz
bucket contains essentially all of Africa, dragging its unweighted mean down.

# 3. The international comparison is unsalvageable

Not "needs better controls". **The exposure variable is itself the confounder.**

Mains frequency was never assigned by nature. It was assigned by **which industrial power
electrified you**. 50 Hz spread through German (Siemens/AEG) equipment sales and the
British Empire; 60 Hz across the Americas, South Korea, western Japan, and the
Philippines under American influence.

The clinching case: **Liberia runs at 60 Hz** — essentially alone in West Africa — because
it was founded by freed American slaves. There is no physical or geographic account of
why Monrovia differs from Freetown. The variable is a record of 19th-century politics.

| Country | Hz | Reason |
|---|---|---|
| Philippines | 60 | US colonial period |
| Indonesia | 50 | Dutch colonial period |
| India | 50 | British Empire |
| South Korea | 60 | US influence post-1945 |
| Liberia | 60 | Founded from the US |
| Japan | **both** | Tokyo bought AEG; Osaka bought GE |

Geopolitical alignment determines GDP, health-system capacity, **life expectancy** (which
for an age-dependent disease is close to *the* cause), and **death-registration
completeness** (which for a mortality measure is close to *the* measurement). A
cross-country comparison of dementia mortality by mains frequency is a comparison of
empires wearing a hertz costume.

This cannot be adjusted away: the adjustment set is unidentifiable; adjusting on
development means adjusting on the exposure's own cause; and once you condition on
everything colonial history determines, frequency has nothing left to explain.

\newpage

# 4. Japan: the data does not exist

Japan is the one place where frequency is plausibly exogenous — same country, same health
system, same registration practice, boundary set by 1890s procurement. Three data sources
exist. All three fail.

## 4.1 The boundary moved — five times

A finding that invalidates every prior analysis, including the original chart.

**Static 50/60 coding is wrong for 9 of 47 prefectures.**

| Region | Change | When |
|---|---|---|
| Eastern Kyushu — **all of Oita, all of Miyazaki**, E. Fukuoka, E. Kagoshima, Minamata | **50→60** | 1949–1960 |
| Hokkaido west — Sapporo, Otaru, Hakodate | **60→50** | 1943–1946 |
| Joban — N. Ibaraki (Mito, Hitachi), S. Fukushima (Iwaki) | **60→50** | 1961 |
| Sado island | **50→60** | ~1954 (date uncertain) |
| Nagano (Chubu area) | **50→60** | by 1961 |

Oita and Miyazaki were 50 Hz until ~1951–60. **Coding them "60 Hz" for a 1990–2021
dementia analysis assigns the wrong exposure to everyone born before ~1960 — precisely
the cohort now developing dementia.**

Handled correctly this would be an *opportunity*: whole-prefecture, time-varying exposure
running in **both directions**, permitting a birth-cohort design far stronger than the
static spatial contrast. It fails only because the outcome data below does not exist.

*(Corrections to the received map: Yamanashi is not split; Nagano is 60 Hz-dominant with
50 Hz hamlets; Karuizawa's listing as 50 Hz is a Wikipedia fabrication traced to an
unsourced 2011 anonymous edit that has survived fifteen years and is widely mirrored.)*

## 4.2 The outcome does not exist below prefecture level

Japan's LTCI open data (`kaigo DB`) publishes **real, measured** dementia assessments —
actual certification-survey records, not modelling. It has the dementia variable. It has
municipality geography (1,571 insurers, coded). **They are never crossed.**

| Table item | Prefecture | Sex/age | Care level | **Municipality** |
|---|---|---|---|---|
| Application category | yes | yes | yes | yes |
| Care-need judgment | yes | yes | — | yes |
| **Dementia independence level** | yes | yes | yes | **NO** |

Verified by download. The municipality file contains only two tables — application
category and care level. **No dementia.**

Worse, the prefecture and age tables are **separate two-way marginals, not a cross-tab**:
dementia-by-prefecture has no age; dementia-by-age has no prefecture. **So even a
prefecture analysis cannot be age-standardised** — meaning it would reproduce the exact
artefact that discredited the original chart. And the denominator is *certification
applications* (1.6M in 2023), not population — a group selected by who seeks care.

**The tempting workaround must be rejected.** Applying national age/sex-specific dementia
rates to municipality certification counts yields a deterministic rescaling of care-need
counts with **zero independent municipality-level dementia signal**. You would be testing
whether frequency predicts *care-need certification* — dominated by physical frailty and
local administrative practice — while appearing to test dementia.

## 4.3 The modelled estimates are flat — demonstrated, not asserted

GBD 2021 does contain all 47 prefectures with age-standardised prevalence. But IHME's own
Japan paper (Lancet Public Health, 2025) states:

> "Data gaps remain at both the national and prefectural levels. GBD disease models
> compensate by using regional data and covariates, **potentially resulting in minimal
> regional variation** in certain diseases and risk factors due to limited Japanese data
> coverage."

This was tested rather than taken on faith, by comparing dispersion against causes Japan
demonstrably measures well.

**Between-prefecture coefficient of variation, 2021:**

| Cause | CV | Role |
|---|---|---|
| **Alzheimer's & dementias** | **4.3%** | outcome |
| Ischemic heart disease | 4.6% | placebo |
| Colon & rectum cancer | 8.9% | placebo |
| **Stroke** | **9.6%** | real variation (salt gradient) |
| **Stomach cancer** | **12.4%** | real variation |

**Alzheimer's varies about a third as much as stomach cancer**, and less than half as
much as stroke — both of which have large, well-documented Japanese regional variation.
Stable across the entire series: Alzheimer's ranks among the two flattest surfaces in
**32 of 32 years**.

**A surface this flat cannot show an association with anything.** Any 50/60 test on it is
uninformative, not null.

## 4.4 The contrast is east-vs-west Japan — the placebo proves it

**Ratio of age-standardised prevalence, 60 Hz / 50 Hz, 2021** (excluding the 9 prefectures
that changed frequency):

| Cause | Ratio | p | Role |
|---|---|---|---|
| Colon & rectum cancer | **0.895** | **0.000** | **placebo** |
| Stroke | 0.912 | 0.013 | real variation |
| Stomach cancer | 0.945 | 0.196 | real variation |
| **Alzheimer's & dementias** | **0.981** | **0.044** | **outcome** |
| Ischemic heart disease | 1.024 | 0.289 | placebo |

**The placebo separates ~5x harder than the outcome.** Colon cancer — no flicker
mechanism whatsoever — differs by 10.5% at p<0.001, while Alzheimer's differs by 1.9% at
p=0.044. **Stroke behaves exactly as known biology predicts** (higher in the 50 Hz east:
Tohoku, the salt gradient) — a positive control confirming what the 50/60 line actually
measures.

Four of five causes are higher in the east; **Alzheimer's shows the smallest such
gradient of any**. The dementia "difference" is a pale echo of a general east–west
gradient that hits the placebo five times harder.

![**The GBD surface has no signal to test.** Left: between-prefecture dispersion by
cause, 1990–2021 — Alzheimer's sits with the flattest surfaces in all 32 years, at about
a third of stomach cancer's dispersion. Right: the 60-vs-50 Hz contrast — the placebo
(colon cancer, no flicker mechanism) separates five times harder than the outcome, and
stroke reproduces Japan's known east/west salt gradient, confirming what the frequency
line actually measures.](figures/gbd_diagnostic.png)

### The trap that pre-registration avoided

The pre-registered decision rule fixed five criteria before the data was seen.
**Criterion 2 passed**: Alzheimer's is 1.9% lower at 60 Hz, exactly the direction §1.3
predicts. Viewed alone — p=0.044 with the mechanistically predicted sign — **that is the
result that gets written up.**

The placebo is what stops it. **It fails criterion 1** (p=0.044 vs the pre-specified
alpha=0.005) **and criterion 3** (all placebos null). A placebo that moves invalidates the
design. Pre-registering alpha and the placebo set before seeing data is the only reason
this is a clean negative rather than a paper.

## 4.5 The population cohorts have ascertainment collinear with frequency

Japan's multi-site dementia cohorts measure dementia properly — clinical assessment,
population sampling, and JPSC-AD measures *incidence* among the dementia-free, which is
the right measure. It has a genuine contrast: **3 of 8 sites (38% of participants) are
50 Hz**.

**But the three sites with enhanced case-finding — home visits plus nursing-home visits —
are all 60 Hz.** Prevalence at those sites is 16.4% vs 8.5% overall. Meanwhile the
largest 50 Hz site (over half the 50 Hz sample) used **voluntary-response sampling**,
self-selecting toward healthier participants.

Both biases push the same way: **60 Hz ascertained harder, 50 Hz softer.** A naive
contrast manufactures a "60 Hz has more dementia" result of roughly the magnitude one
hopes to detect — **entirely from methodology, and in exactly the direction the original
chart showed.** The effective n is **8 sites**, not 11,410. A null would be interpretable;
a positive result would not.

*(Also: the widely circulated "47-prefecture dementia ranking" tables apply one
prefecture's age-specific rates to every prefecture's population structure. They contain
**zero** prefecture-level information — a map of demography wearing a dementia label.)*

\newpage

# 5. Ontario: the best experiment ever run, and it cannot be read

Southwestern Ontario — Toronto, Hamilton, Niagara, London, Windsor — ran on **25 Hz**
until Ontario Hydro converted the region between **1949 and 1959**. ~800,000 customers,
~13,000 sq mi.

**25 Hz mains produces 50 Hz luminous flicker — in the gamma band.** This is the only
large human population ever to have lived under sustained ambient flicker near 40 Hz:
essentially the GENUS condition, delivered unintentionally, for decades.

## 5.1 The exposure was real — measured, in 1925

| Mains | Luminous flicker | Modulation | Source |
|---|---|---|---|
| **25 Hz** | **50 Hz** | **~23–30%** | Sharp 1906 (22.7%, 40W); Cady 1925 (30%, 25W) |
| 50 Hz | 100 Hz | ~15% | published |
| 60 Hz | 120 Hz | ~6–12.5% | Lehman 2011 (6.6%, 60W) |

Cady & Dates (1925): *"Measurements of the instantaneous candlepower for the 25-watt lamp
on 25-cycle current show a variation in candlepower of 30 per cent above and below the
average… None of the ordinary lamps show visible flicker on 60-cycle current."*

**Triple validation:** two independent measurements 19 years apart agree within 6%; the
1/f scaling law reconciles Sharp (1906) with Lehman (2011) within 10% **across 105
years**.

**The flicker was peripheral and subliminal, not visible** — *"imperceptible when looking
directly at the lamps, but could be observed only through light which is not focused
directly on the fovea"* (Sharp 1906). Which is arguably a *better* exposure construct for
gamma entrainment: the mechanism does not require conscious perception, only that the
retina be driven.

**Two corrections to intuition:** carbon filaments flicker *less* than tungsten (3x less
efficient → thicker filament → longer thermal time constant), so the 1907–11
carbon→tungsten transition **increased** exposure. And lamps were never part of the
conversion programme — motors, clocks and transformers were — so no lamp-replacement
record exists as a proxy.

## 5.2 The conversion was heavily staggered — Q1 answered

Recovered from the Canada Year Book 1951 (prepared under HEPCO's own chairman) and the
Ontario Hydro Annual Reports 1949–60, whose Appendix I carries a **frequency column for
every municipality every year**:

Sarnia and London 1950 · Forest and Strathroy May 1951 · Seaforth and St. Marys end-1951
· Stratford early 1952 · Windsor Jan 1952–1953 · Leamington 1954 · Chatham and St. Thomas
1956 · Oxford 1957 · Toronto 1953–59 · last home 9 July 1959.

**And it did not convert west-to-east.** Huron/Perth converted *early* (1951–52), years
before Chatham (1956), because the sequence tracked 60-cycle power availability, not
geography. Two people born the same year 100 km apart could differ by five or six years
of exposure. **That is exactly the staggering a cohort design needs.**

## 5.3 And it still cannot be done

**1950s residence was never recorded.** Not lost — never observed. OHIP did not exist
until 1966.

| Source | Earliest individual residence | 1955? |
|---|---|---|
| ICES **RPDB** | ~1991, and it is a *lagged current-address snapshot*, not a history | No |
| **CanCHEC** | tax-derived postal codes from ~1981 — the deepest trail in Canada | No — 26 yrs short |
| **StatCan SDLE** | spine from 1964; census linkers from 2001 | No |
| **1951 / 1961 censuses** | sealed 92 years → **2043 / 2053**, then images, not microdata | No |

**The decisive tell:** ONPHEC — Ontario's flagship environmental-dementia cohort, built
by people with every ICES privilege — was inception-dated 1996 *specifically because a
5-year look-back to ~1991 was the maximum residential history obtainable.* If it were
extendable, they would have extended it.

**Two further problems sink it even with perfect exposure data:**

1. **The exposure is nearly collinear with urbanicity.** The 25 Hz zone was the
   Niagara-fed industrial core; the comparison is rural eastern/northern Ontario. Not
   25 vs 60 Hz — urban-industrial vs rural, carrying SES, *education* (the dominant
   dementia confounder), and healthcare access, which also drives differential diagnosis.
2. **Left truncation.** Incident dementia ascertainment starts 1996. The 1930 birth
   cohort carries both the **highest dose** and the **heaviest survival selection**; the
   1955 cohort the least of both. Any predicted dose-gradient could be produced entirely
   by differential survivorship — the confound is collinear with the signal.

The dementia ascertainment is excellent (validated algorithm: Sn 79%, Sp 99%, PPV 80%).
The exposure is not measurable and the contrast is not identifiable.

\newpage

# 6. What would be needed

**The rational order of work is close to the inverse of what was assumed.**

**1. Measure the exposure first.** A photodiode, an FFT, and a few dozen home visits
either side of the Fuji River in Shizuoka. If delivered flicker contrast is ~zero — likely,
given inverter ballasts and LEDs — **no observational design on modern data can test this
hypothesis, and the question is retired for the price of a photodiode.** This is by far
the cheapest decisive step and it was never taken.

**2. Settle the mechanism before the epidemiology.** The signed prediction (§1.3) rests
on a subharmonic-entrainment argument that is plausible but unestablished. Whether 100 Hz
or 120 Hz flicker at ~10% modulation drives 40 Hz gamma at all is answerable on a bench
with an EEG and a signal generator, in weeks, for a tiny fraction of any epidemiological
cost. **If it does not, the hypothesis is dead regardless of any population data.**

**3. Only then consider epidemiology** — and note that even with a formal Japanese
research-database application (institutional affiliation, ethics review, months), the
only identified design detects effects on the order of tens of percent, which no
plausible mechanism produces from a 1.2x exposure contrast.

# 7. What was built

A complete, reproducible pipeline and evidence base, in the project directory:

```
README.md            orientation and state of play
METHODS.md           pre-registration: signed hypothesis, gated pipeline, decision rule
LIMITATIONS.md       written before results, so nothing could be dropped later
REPORT.md/.pdf       this document
docs/00              critique of the initial analysis (8 findings)
docs/01              why the international comparison is unsalvageable
docs/02              the Ontario 25 Hz experiment (verdict revised)
docs/03              Japan data availability - the definitive blocker
docs/04              Ontario/ICES feasibility - the exposure was never recorded
docs/05              Ontario flicker physics - primary sources, 1906-1930
docs/06              Japan population cohorts - ascertainment confound
docs/07              GBD diagnostic results
docs/08              Ontario conversion schedule 1949-59 (reusable artifact)
data/reference/      prefecture->frequency map + the 5 conversions, fully cited
src/                 tested pipeline; agestd.py has 11 passing tests
figures/             gbd_diagnostic.png
```

Two artifacts have value independent of this hypothesis:

- **`data/reference/`** — a **time-varying** Japanese prefecture-frequency map with the
  five documented conversions and full citations, including corrections to errors that
  have propagated through Wikipedia for fifteen years.
- **`docs/08`** — a collated Ontario municipal conversion schedule, which does not appear
  to exist elsewhere.

# 8. Conclusion

**The hypothesis was worth taking seriously, was taken seriously, and cannot be tested
with existing data.**

The Japan idea was genuinely clever — a real natural experiment, in the one place on Earth
where mains frequency is plausibly exogenous to health. It fails not through lack of
imagination or effort but because the outcome data at the required geography does not
exist, the modelled substitute is demonstrably flat, and the contrast that remains is
east-versus-west Japan.

The strongest evidence produced here is not the null. It is that **a placebo outcome with
no conceivable flicker mechanism separates five times harder than dementia does** — and
that the dementia surface is measurably flatter than any cause Japan genuinely measures.
Those two facts together say the instrument is reading its own noise.

The honest position is that this question is not currently answerable by epidemiology,
and that the cheap decisive experiments — measure the exposure, test the entrainment —
have not been done. **They should be done first, and they may well end the question.**

---

*Analysis and documentation produced with Claude (Anthropic). All data sources, retrieval
commands, and manual steps are documented in `data/raw/PROVENANCE.md`. Japanese terms are
romanised in this report; the original orthography is retained in the repository docs for
searchability.*
