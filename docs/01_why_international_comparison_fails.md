# Why the international 50 Hz vs 60 Hz comparison is unsalvageable

This document argues that no amount of covariate adjustment can rescue a cross-country
comparison of dementia burden by mains frequency. The problem is not residual
confounding. The problem is that **the exposure variable is a confounder**.

## The claim

Mains frequency was never assigned by anything resembling nature, geography, or chance.
It was assigned by **which industrial power electrified you**.

- **50 Hz** spread through German (Siemens/AEG) equipment sales and the British Empire.
  Early Siemens generators were designed around 50 Hz, and British engineering practice
  carried it across the colonies — hence Europe, Africa, India, Australia, much of Asia.
- **60 Hz** was Westinghouse's choice in the United States, and spread across the
  Americas, South Korea, western Japan, and the Philippines under U.S. technological
  leadership.

The industry's own histories describe it in precisely these terms — this is not a
reconstruction, it is the standard account.

## The clinching case: Liberia

**Liberia runs at 60 Hz.** It is essentially alone in West Africa in doing so; its
neighbours run at 50 Hz. The reason is that Liberia was founded by freed American
slaves and took American electrical equipment and standards.

There is no physical, climatic, or geographic account of why the mains frequency in
Monrovia differs from the mains frequency in Freetown. The variable is a record of
19th-century political history and nothing else.

Related cases making the same point:

| Country | Frequency | Reason |
|---|---|---|
| Philippines | 60 Hz | U.S. colonial period |
| Indonesia | 50 Hz | Dutch colonial period |
| India | 50 Hz | British Empire |
| South Korea | 60 Hz | U.S. influence post-1945 |
| Liberia | 60 Hz | Founded from the U.S. |
| Japan | **both** | Tokyo bought AEG (German); Osaka bought GE (American) |

## Why this is fatal rather than merely inconvenient

If mains frequency is a proxy for 20th-century geopolitical alignment, then it is
correlated with:

- GDP per capita and every downstream determinant of health
- Health system capacity and diagnostic access
- **Life expectancy** — which, for an age-dependent disease, is close to *the* cause
- **Death registration completeness and coding practice** — which, for a mortality
  measure, is close to *the* measurement

That last pair is the killer. A cross-country comparison of dementia *mortality* by
mains frequency is a comparison of empires wearing a hertz costume: it measures how
long people live and how carefully their deaths are recorded, sorted by which country
sold them generators in 1900.

This is not a confounder one adjusts away, because:

1. **The adjustment set is not identifiable.** Colonial history affects the outcome
   through an unbounded number of paths (nutrition, education, war, migration,
   institutions, healthcare, registration). You cannot enumerate them.
2. **Adjusting on development is adjusting on the exposure's own cause.** Electricity
   access, GDP, and life expectancy are all downstream of the same colonial variable.
   Conditioning on them does not isolate frequency; it slices the confounder.
3. **There is no residual variation left.** Once you condition on everything colonial
   history determines, frequency has nothing left to explain — and if it appears to,
   that is a sign of model misspecification, not of signal.

## What survives

Only **within-country** contrasts where frequency was assigned by an accident
uncorrelated with health determinants. In practice this means **Japan**, where the
50/60 boundary sits inside a single country, single health system, single registration
practice, and single broad culture, placed by a procurement decision in the 1890s.

That is the design specified in `METHODS.md`. It is the reason the Japan idea is worth
pursuing and the international one is not.

## Sources

- Utility frequency — https://en.wikipedia.org/wiki/Utility_frequency
- Mains electricity by country — https://en.wikipedia.org/wiki/Mains_electricity_by_country
- The Evolution of Power Grid Frequencies —
  https://strongpowerelectric.com/the-evolution-of-power-grid-frequencies-why-50hz-and-60hz-dominate-global-electricity-systems/
- Guide to International Power Frequencies —
  https://powersystemsinternational.com/guide-to-international-power-frequencies/
- Voltage & Frequency by Country —
  https://generatorsource.com/tools-info/voltages-frequencies-hz-around-the-world/

*(Citations to be upgraded to peer-reviewed / primary historical sources before any
submission. The Liberia and Korea cases in particular deserve a proper history-of-
technology citation rather than a reference site.)*
