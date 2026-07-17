# The Ontario 25 Hz experiment

> ## ⛔ VERDICT REVISED (2026-07-17): the individual-level design is dead
>
> This document recommended Ontario as "a far better test than Japan." **That
> recommendation was over-optimistic and is withdrawn** for the individual-level cohort.
> Q3 below — can 1950s residence be reconstructed? — came back **no**, and two further
> problems sink it even with perfect data. Full evidence in
> `docs/04_ontario_ices_feasibility.md`. Summary:
>
> **1. The exposure was never recorded.** Not "lost" — never observed. OHIP did not exist
> until 1966. ICES's RPDB holds a *lagged current-address snapshot* starting ~1991, not
> an address history. Canada's deepest individual residential trail is CanCHEC's
> tax-derived postal codes from ~1981 — still 26 years short. The 1951 and 1961 censuses
> are sealed under the *Statistics Act* 92-year rule until **2043 and 2053**, and even
> then arrive as scanned images, not linkable microdata, by which time the 1930–60
> cohorts are dead.
>
> **The decisive tell:** ONPHEC — Ontario's flagship environmental-dementia cohort, built
> by people with every ICES privilege — was inception-dated 1996 *specifically because a
> 5-year look-back to ~1991 was the maximum residential history obtainable*, and excluded
> anyone resident under 5 years for that reason. **If a 1991 look-back were extendable,
> they would have extended it.** That is the ceiling, set by the people who built the
> infrastructure.
>
> **2. The exposure is nearly collinear with urbanicity.** The 25 Hz zone was the
> Niagara-fed industrial core — Toronto, Hamilton, Niagara, London, Windsor. The
> comparison region is rural eastern and northern Ontario. This is not 25 Hz vs 60 Hz;
> it is **urban industrial Ontario vs rural Ontario**, carrying SES, education (the
> dominant dementia confounder), occupational exposure, air pollution, and healthcare
> access — which also drives **differential ascertainment**, since diagnosis rates track
> specialist access.
>
> **3. Left truncation destroys the cohort — including the gradient fix below.** Incident
> dementia in the ODD starts **1996**. Anyone born 1930–60 who died before then —
> disproportionately the urban, industrial, exposed group — is invisible. Worse for the
> dose-gradient design specifically: the 1930 cohort has both the *highest dose* and the
> *heaviest survival selection*, and the 1955 cohort the least. **The predicted
> attenuation across cohorts could be produced entirely by differential survivorship.**
> The fix proposed below does not survive this.
>
> **What is still true:** the physics (§ below) and the historical fact of the
> conversion. And **the dementia ascertainment is excellent** — see
> `docs/04_ontario_ices_feasibility.md`.
>
> **The one surviving door** is the NDR pattern: an external historical roster linked
> into ICES. Ontario Hydro's Frequency Standardization Program customer records
> (~800,000 accounts, 1949–59) would be that roster **if they survive**. That is what the
> archival question below is now for — and even then, the records name the *account
> holder* (the parent), not the child in the birth cohort. Do not bet on it.
>
> The material below is retained: the physics is sound, the historical claim is sound,
> and the design reasoning is correct in the world where the exposure roster exists.

The Japan design is elegant but underpowered (`METHODS.md` §9.2: the only identified
variant detects a ~31% shift, which no plausible mechanism produces). Southwestern
Ontario offers an order of magnitude more exposure contrast, a sharper mechanistic
prediction, and better data.

## The history

Southwestern Ontario — Toronto, Niagara Falls, Hamilton, Windsor — ran on **25 Hz**
electricity as a large island until the 1950s. Ontario Hydro then converted the entire
region to 60 Hz in a ten-year, ~$400M programme running roughly **1949–1959**. The last
25 Hz generating plant (Rankine, Niagara Falls) ran until 2005.

25 Hz was abandoned largely *because of visible lamp flicker*. That fact is the whole
point of what follows.

## Why the physics makes this decisive

Light output peaks twice per AC cycle, so luminous flicker sits at 2× mains:

| Mains | Luminous flicker | Visible? | Relation to 40 Hz gamma |
|---|---|---|---|
| **25 Hz** | **50 Hz** | **Yes** — at/below flicker fusion | **In the gamma band** |
| 50 Hz | 100 Hz | No | 2.5× — no integer relation |
| 60 Hz | 120 Hz | No | 3× — third harmonic |

**Southwestern Ontario before 1959 is the only large human population known to have
lived under sustained ambient flicker in the gamma band.**

That is essentially the Tsai/GENUS condition — 40 Hz visual entrainment — delivered to
millions of people, in their homes and workplaces, for decades, unintentionally.

Compare the contrast on offer:

- Japan: 100 Hz vs 120 Hz. Both far above fusion, neither in the gamma band, and the
  delivered difference has been eroding since inverter ballasts and LEDs.
- Ontario: 50 Hz vs 120 Hz. One visible and in-band, one not. **No decay problem** —
  the exposure ended in 1959, before LEDs existed, and everything was incandescent.

## The signed prediction

Sharp, and opposite to the intuition that started this project:

> If the 40 Hz gamma-entrainment mechanism is real, the cohort exposed to 25 Hz mains
> in Southwestern Ontario should have **LESS** dementia than comparable 60 Hz cohorts.

If instead one believes ambient flicker is *harmful*, the prediction reverses — and this
population had by far the most flicker exposure of anyone. **Either way the hypothesis
makes a strong, testable, falsifiable claim here.** That is exactly what the Japan
50-vs-60 contrast fails to deliver.

## Why the cohort timing works

This is the part that makes it feasible rather than merely interesting:

- Exposure window: 25 Hz present until ~1949–59.
- Someone born 1930–1955 spent childhood and/or early adulthood under 25 Hz.
- That cohort reaches 65 between roughly **1995 and 2020**.
- Alzheimer's has a 20+ year prodrome, so early- and mid-life exposure is the
  aetiologically relevant window — which is precisely what this cohort has and what a
  cross-sectional Japan analysis of *current* residence does not.

Ontario ascertains dementia in health administrative data from around 1991 onward. **The
exposed cohort's dementia is inside the data window.**

## The data

**ICES** (Institute for Clinical Evaluative Sciences, Ontario) holds population-level,
individually linkable health administrative data for essentially every Ontarian:

- Validated dementia case ascertainment (the Ontario Dementia Cohort algorithm, using
  linked physician billings, hospitalisations, and drug claims).
- Postal-code-level residential history via OHIP registration, enabling exposure
  assignment by where someone actually lived and when.
- Individual-level — so this escapes the ecological-inference problem that caps the
  Japan design entirely (`LIMITATIONS.md` §2).

Access is by application, with a named Ontario-based collaborator. That is a real
barrier but a well-trodden one.

## Three questions that decide feasibility

Answer these before anything else. Each can kill the study outright.

### Q1 — Was the conversion STAGGERED across municipalities? *(load-bearing)*

If every municipality converted at once, then "years of 25 Hz exposure" is a pure linear
function of birth year — **perfectly collinear with cohort effects**, and the design
collapses. If Windsor converted in 1950 and Toronto in 1957, then two people born the
same year got different doses depending on where they lived. **That municipality × cohort
variation is the entire identifying strategy.**

So the archival conversion schedule is not a nice-to-have. It is the study.

### Q2 — Was domestic lighting actually on 25 Hz?

Some 25 Hz systems fed lighting through separate circuits or motor-generator sets
*specifically to avoid flicker*, reserving 25 Hz for industrial motors and traction. If
Ontario homes lit on 60 Hz while only industry ran 25 Hz, **there is no exposure and the
hypothesis has nothing to bite on.**

### Q3 — Can 1950s residence be reconstructed at the individual level?

**Probably not, and this is the most likely killer.** OHIP did not exist until 1966.
ICES's Registered Persons Database address history is unlikely to reach before ~1990.
Canada's historical census microdata is released on a 92-year rule — the 1951 census
becomes available in **2043**. So individual residential history for the exposure window
may simply be unobtainable, forcing an ecological design.

## The cohort-timing problem, and the fix

A naive within-place design fails on timing, and it is worth seeing why before proposing
one:

- Exposure ended 1959. To compare exposed vs unexposed *within* Southwestern Ontario, the
  unexposed are those born after ~1960 — who reach 65 only in **2025–2040**. They are
  barely into dementia age. There are almost no unexposed cases yet.

**The fix: use the spatial contrast within birth cohort, and test the dose gradient
across cohorts.** Everyone in the analysis is currently 70–95, so all of them are
ascertainable now.

| Birth cohort | 25 Hz years (SW Ontario) | 25 Hz years (rest of Ontario) |
|---|---|---|
| 1930 | ~19–29 | 0 |
| 1940 | ~9–19 | 0 |
| 1950 | ~0–9 | 0 |
| 1955 | ~0–4 | 0 |

Within Southwestern Ontario the dose **declines monotonically** across the 1930→1955
cohorts. Outside it, dose is zero for every cohort. So the prediction is sharp:

> **The SW-Ontario-vs-rest-of-Ontario dementia gap should attenuate across successive
> birth cohorts, tracking the dose gradient — and vanish for cohorts born after ~1960.**

This is a difference-in-differences on the cohort × region interaction. Cohort effects
(secular dementia trends, diagnostic drift) difference out against the rest-of-Ontario
comparison. It needs no unexposed elderly cohort, because the identifying variation is
the *gradient*, not a binary.

**The residual threat** is any SW-Ontario × cohort interaction unrelated to electricity —
wartime industrial exposure concentrated in the Toronto–Hamilton–Windsor corridor,
post-war immigration waves, or occupational hazards that also vary by cohort and region.
These are real and must be addressed with placebo outcomes, not waved at.

**Migration is the other threat, and it is severe.** Post-war immigration to Toronto was
enormous; a large fraction of Toronto residents born in 1940 were born in Italy,
Portugal, or the Caribbean and arrived after the conversion. Current residence badly
misclassifies 1950s exposure. Partial fix: restrict to the Ontario-born using census
place-of-birth, at the cost of sample and generalisability.

## Design sketch

**Exposure:** years of residence in the 25 Hz service area before conversion,
constructed from birth year, residential history, and the municipality-level conversion
schedule. This yields a **continuous dose**, not a binary — far better than Japan's
binary contrast.

**Two sources of variation, which is the real advantage:**

1. **Spatial** — 25 Hz island vs the rest of Ontario (always 60 Hz).
2. **Temporal** — the 1949–59 conversion means adjacent birth cohorts *within the same
   municipality* got different doses.

The second is the valuable one: it identifies off within-place, across-cohort variation,
which strips out the urban/rural confounding that wrecks a bare Toronto-vs-rural
comparison. A difference-in-differences or cohort-discontinuity design falls out
naturally, because only the 25 Hz region experienced a change.

**Placebo outcomes and balance tests** as in `METHODS.md` §7 — the same discipline
applies; conversion timing correlated with urbanisation and wealth, so this is not
automatically clean.

## Honest problems

- **The conversion schedule must be reconstructed** municipality by municipality from
  Ontario Hydro records. This is archival work and may be the binding constraint.
- **Survivor bias** is serious: the exposed cohort is old, and differential mortality
  before dementia onset could manufacture or mask an association.
- **Selective migration** into and out of Toronto over 70 years.
- **Confounding with urbanisation** — the 25 Hz island was the industrial heartland.
  The within-place cohort variation is what defends against this; the spatial contrast
  alone would not.
- Incandescent lamps have thermal inertia, which damps modulation depth. Visible 25 Hz
  flicker is well attested historically, but the actual **modulation depth** delivered
  by period lamps should be measured or modelled — a surviving 25 Hz lamp on a variable
  frequency supply would settle it in an afternoon.

## Verdict

Bigger exposure contrast, a sharper and genuinely signed prediction, individual-level
data, dose-response rather than binary, exposure in the aetiologically relevant window,
and no exposure-decay problem. Every axis on which the Japan design is weak, this one is
strong.

The main cost is archival (the conversion schedule) rather than statistical. That is a
better problem to have than an MDE of 31%.

## Sources

- The rise and fall of 25-cycle electricity in Ontario —
  https://www.lifebynumbers.ca/history/the-rise-and-fall-of-25-cycle-hz-electricity-in-ontario/
- Hydro conversion from 25 Hz to 60 Hz —
  https://www.streetsofstratford.ca/hydro
- Utility frequency — https://en.wikipedia.org/wiki/Utility_frequency
- Rankine Generating Station — https://en.wikipedia.org/wiki/Rankine_Generating_Station
- Niagara-on-the-Lake Hydro, "Frequency" — https://www.notlhydro.com/frequency-blog/
- IEEE Power & Energy Magazine, History —
  https://magazine.ieee-pes.org/novemberdecember-2012/history-5/

*(To be upgraded to Ontario Hydro primary records and a history-of-technology citation
before any submission. The municipality-level conversion schedule is the key missing
artefact and does not appear to exist in digitised form.)*
