# Limitations

Written before results, so that nothing here can be quietly dropped if the numbers turn
out interesting. Ordered roughly by how badly each threatens the enterprise.

## 1. The exposure contrast may not exist

The single most serious problem, and it is not statistical.

The hypothesis needs a real difference in what people's brains are exposed to. But:

- Mains at 50/60 Hz produces **luminous** flicker at 100/120 Hz, not 50/60 Hz.
- Japan adopted high-frequency inverter ballasts (tens of kHz) for fluorescent lighting
  comparatively early, erasing the 100/120 Hz distinction indoors decades ago.
- Post-2010 LED lighting has flicker determined by driver electronics, not mains.
- Screens refresh at 60/120/144 Hz regardless of what is in the wall.

So across precisely the period our outcome data covers, the nominal 50-vs-60 label may
correspond to almost no difference in delivered flicker. **A null result is therefore
substantially uninformative about the hypothesis** — it may only reflect that the
exposure contrast has decayed. Only the measurement substudy (`METHODS.md` §10) can
distinguish "no effect" from "no exposure difference."

## 2. Ecological inference

All tiers are ecological: we observe regional aggregates, not individuals. Regional
association neither implies nor refutes individual-level risk. This design cannot
establish causation at the individual level under any outcome.

## 3. Exposure misclassification from residential mobility

Alzheimer's pathology develops over 20+ years. Current residence is a poor proxy for
the exposure window that matters. Japan has substantial internal migration, especially
toward Tokyo (50 Hz) during working life followed by some return migration. This
misclassification is likely **non-differential**, biasing toward the null — compounding
problem #1 in the same direction.

Fixing this requires individual-level residential histories (e.g. JAGES cohort linkage),
which is a different and much larger project.

## 4. The boundary is not only electrical

The 50/60 divide runs near the Fossa Magna, which is also a genuine geological,
historical, dialectal and culinary divide between eastern and western Japan. Regional
diet (notably salt intake, soy sauce style, stock base) differs across roughly this
line, and diet has plausible vascular-dementia relevance.

This is exactly why placebo outcomes (`METHODS.md` §7) are not optional. If the
boundary shows discontinuities in outcomes with no flicker mechanism, we cannot
attribute anything to electricity. Our expectation is that it may well fail this test.

## 5. Power

Tier 3 restricted to Shizuoka has ~35 municipalities. Even pooling boundary segments,
the effective sample near the cutoff is small. We are likely powered only for large
effects, which are implausible for a 20% difference in an ambient exposure. The MDE
will be reported before fitting; if it exceeds any mechanistically plausible effect,
the honest conclusion is **"uninformative"**, not "null."

## 6. Outcome measurement

- **LTCI dementia assessment** is administrative. It measures *who applied for and was
  assessed for long-term care*, which depends on local service availability, family
  structure, and municipal administrative practice — not purely on dementia prevalence.
  Municipalities differ in LTCI uptake for reasons unrelated to disease.
- **GBD estimates** are modelled. At fine geography they may substantially reflect
  IHME's covariate model rather than local measurement, in which case analysing them
  recovers the model, not the world.

Neither is a clean measurement of dementia. The first is our preference because at
least it is *measured* with a uniform national instrument.

## 7. Composite outcome

Both LTCI assessment and GBD's "Alzheimer's disease and other dementias" fold together
Alzheimer's, vascular, Lewy body and mixed dementias. The flicker hypothesis concerns
AD specifically. Vascular dementia in particular has strong regional dietary
determinants that would load directly onto our East/West contrast.

## 8. Multiple comparisons

Years × sexes × age strata × severity thresholds × outcome definitions × bandwidths
generates hundreds of possible tests. We have pre-specified exactly one primary
outcome (`METHODS.md` §5) for this reason. Any additional analysis is exploratory and
will be labelled so, with no significance claims attached.

## 9. This study cannot confirm the hypothesis

Stated in `METHODS.md` §8.1 and repeated here. Given a strong prior against, a single
ecological study clearing p<0.005 does not move the posterior far. The achievable
outcomes are "bound the effect" or "refute by bounding tightly." A surprising positive
would be a reason to seek individual-level replication and higher-contrast natural
experiments (§11 of METHODS), not a finding in itself.

## 10. Prior literature not yet systematically reviewed

The occupational ELF-EMF and neurodegeneration literature spans forty years and has
not yet been systematically reviewed for this project. It is weak and confounded by
co-exposures, but it exists, and any submission must engage with it rather than
presenting this as a novel question. **Open task.**
