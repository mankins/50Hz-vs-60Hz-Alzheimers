# Ontario / ICES feasibility: the exposure was never recorded

**Status: definitive on the exposure question. Verified 2026-07-17.**

Companion to `docs/02_the_ontario_25hz_experiment.md`, whose recommendation this
document withdraws for the individual-level design.

## The finding

**Individual-level residential history for 1900–1959 does not exist in Canada.** Not
lost, not restricted, not expensive — **never observed**. OHIP did not exist until 1966.
No registry ever recorded a 1955 Ontario address in a form linkable to a person alive
today. This is not a data-retention gap an archival request could fill.

| Source | Earliest individual residence | Verdict for 1955 |
|---|---|---|
| ICES **RPDB** | ~1991 annual snapshots of a *lagged current-address field* | **No** |
| **ONPHEC** | inception 1996, 5-yr look-back → ~1991 | **No** |
| **CanCHEC** | census linkage 1991; tax-derived postal codes from ~1981 | **No** — still 26 yrs short |
| **StatCan SDLE / DRD** | spine = Social Insurance Registry 1964; census linkers from 2001 | **No** |
| **1951 / 1961 censuses** | sealed 92 yrs → unseal **2043 / 2053**; then scanned images at LAC, not linkable microdata | **No** |

**RPDB is not an address history.** Postal code comes from the health-card record,
refreshed at renewal (~5 yrs) or opportunistically. ICES retains annual snapshots of that
*current* field, which creates a trail going forward — but the trail starts when the
snapshots start. The OCHPP methods note is explicit that the field lags reality: "The
majority of people who move do not change or update their health card until renewal
time…"

**The cohort timing makes it hopeless even as a proxy.** The 1930–60 birth cohorts were
aged 6–29 during the 1949–59 conversion. The earliest address ICES can show is ~1991,
when they were 31–61 — **30 to 60 years and several moves after the exposure window**,
spanning exactly the highest-mobility stage of the life course.

### The decisive tell

**ONPHEC** — Ontario's flagship environmental-dementia cohort, built by people with every
ICES privilege — was inception-dated 1 Apr 1996 *specifically because a 5-year look-back
to ~1991 was the maximum residential history obtainable*, and excluded anyone resident in
Ontario under 5 years for that reason.

**If a 1991 look-back were extendable, they would have extended it.** That is the ceiling,
set by the people who built the infrastructure. Chen/Kwong's celebrated air-pollution and
dementia study (Environ Int 2017, PMID 28917207) inherits exactly that ceiling: exposure
back to ~1996–2001, no further.

## Two problems that sink it even with perfect exposure data

**1. The exposure is nearly collinear with urbanicity.** The 25 Hz zone was the
Niagara-fed industrial core — Toronto, Hamilton, Niagara, London, Windsor. The comparison
region is rural eastern and northern Ontario. This is not 25 Hz vs 60 Hz; it is **urban
industrial Ontario vs rural Ontario**, carrying SES, education (*the* dominant modifiable
dementia confounder), occupational exposure, air pollution, and healthcare access — the
last of which drives **differential ascertainment**, since diagnosis rates track
specialist access.

**2. Left truncation destroys the cohort — including the dose-gradient fix.** ODD incident
dementia starts **1996**. Anyone born 1930–60 who died before then — disproportionately
the urban, industrial, exposed group — is invisible.

This is fatal to the gradient design proposed in `02`, and it is worth being precise about
why: that design predicted the SW-vs-rest gap would **attenuate across birth cohorts**,
tracking dose. But the 1930 cohort carries both the *highest dose* and the *heaviest
survival selection*; the 1955 cohort the least of both. **The predicted attenuation could
be produced entirely by differential survivorship.** The confound is collinear with the
signal. The fix does not survive.

## What IS excellent: dementia ascertainment

The one component that is genuinely well-supported. ICES maintains the **Ontario Dementia
Database (ODD)** on a validated algorithm:

> ≥1 hospitalisation with a dementia diagnosis (CIHI-DAD) **OR** ≥3 physician claims ≥30
> days apart within 2 years (OHIP) **OR** ≥1 dispensing of a dementia-specific medication
> (ODB — cholinesterase inhibitors or memantine)

| Metric (age 65+) | Value |
|---|---|
| Sensitivity | 79.3% |
| Specificity | 99.1% |
| PPV | 80.4% |
| NPV | 99.0% |

Jaakkimainen RL et al., *J Alzheimers Dis* 2016;54(1):337–49, DOI 10.3233/JAD-160105
(PMID 27567819). Validated against EMRALD family-physician EMRs.

- **Coverage: prevalence from Apr 1991; incidence from Apr 1996** (the 5-yr offset is the
  washout to call a case incident). **1996 is the operative start for a cohort study.**
- **Early-onset caveat (45–64):** same algorithm gives **PPV only 23.7%** (Jaakkimainen
  2022, PMC9661344) — largely because the ODB drug arm only captures 65+. Relevant since
  the 1960 birth cohort reaches 65 only in 2025.

## Access pathway (for the record)

**Internal — ICES Scientist/Adjunct.** Requires appointment at one of seven ICES
sites/satellites. Row-level access. **No separate REB needed** — ICES is a "prescribed
entity" under PHIPA s.45. Requires an Ontario academic host.

**External — ICES Data & Analytic Services (DAS).** No ICES affiliation required, but:
- Eligibility is "publicly funded, not-for-profit researcher, student, organization,
  policy maker or decision maker." **A non-academic, unaffiliated private individual does
  not qualify for row-level data.**
- **Private-sector requestors cannot get row-level datasets at all** — ICES performs the
  analysis and returns summary reports only. No iterating on model specification.
- **REB approval required** (this is the trade-off vs the internal route), then ICES
  Privacy Office review.
- **Timeline:** ICES advertises a median 37 days from services-agreement signing to data
  availability. That excludes REB (2–6 months), privacy review, and the Dataset Creation
  Plan. **Realistic end-to-end: 9–18 months.**
- **Cost:** unpublished; expect five figures CAD for a custom cohort, more with bespoke
  linkage.

https://www.ices.on.ca/services-for-researchers/public-sector-researchers/access-to-ices-data/

## The one surviving door: the NDR pattern

The structurally relevant precedent is **not** the air-pollution work. It is the **Ontario
nuclear power plant worker dementia study** (PMC12591044):

- 60,874 workers drawn from the **Canadian National Dose Registry**, which has recorded
  individual occupational radiation doses **since the 1950s**.
- Historical exposure came **entirely from the external registry** — not from any
  health-system residential field.
- The roster was **probabilistically linked into ICES** using full names, birthdates,
  place of birth, and sex.
- Dementia outcomes from the **ODD, 1996–2022** (867,028 person-years).

**This proves the pattern: a historical exposure roster built outside the health system,
carried on identifiers, linked to ICES for modern dementia ascertainment. ICES will do
this. The exposure does not have to come from RPDB.**

For the 25 Hz question, the roster would have to be **Ontario Hydro's Frequency
Standardization Program customer records** (~800,000 accounts, 1949–59), if they survive
with names and addresses. Two problems even then:

1. They name the **account holder** — the parent — not the child in the birth cohort.
2. Survivorship to 1996+ selects hard on the exposed cohort (see left truncation above).

Whether those records survive is the subject of the archival inquiry
(`docs/05_ontario_hydro_archives.md`, pending).

## Verdict

**The individual-level Ontario cohort cannot be done.** The dementia ascertainment is
excellent and the access pathway is real and navigable — but the exposure is not
measurable and the contrast is not identifiable.

An **ecological** design (region-level dementia rates against conversion-zone boundaries)
needs no ICES application and is cheap, but will be inconclusive for the urbanicity and
ascertainment reasons above.

That inconclusiveness is a property of the question, not of the effort applied to it.
