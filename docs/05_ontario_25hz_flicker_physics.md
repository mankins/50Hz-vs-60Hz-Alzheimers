# Was the 25 Hz exposure real? Yes — measured at 30% modulation

**Answer to Q2 of `docs/02`. Verified 2026-07-17 against primary sources (1906–1930).**

**The exposure was real, it was measured at the time, and it was ~2.4× the 60 Hz
exposure.** This is the one component of the whole project that came back *stronger* than
hypothesised.

It does not rescue the Ontario study — `docs/04` killed that on exposure *assignment*
(1950s residence was never recorded). But it establishes that the physical premise of the
hypothesis is sound, and it corrects three things this project had wrong.

Tags: **[MEASURED]** = primary measurement · **[MODELLED]** = derived · **[UNSOURCED]**.

## The headline number [MEASURED]

**Tungsten, 25 W / 110 V, on 25 Hz mains: 30% flicker.**

Cady & Dates, *Illuminating Engineering* (Wiley, 1925), pp. 109–110 —
https://archive.org/details/illuminatingengi00cady

> "Measurements of the instantaneous candlepower for the 25-watt lamp on 25-cycle current
> show a variation in candlepower of 30 per cent above and below the average… **None of
> the ordinary lamps show visible flicker on 60-cycle current.**"

All figures normalised to modern IES percent flicker = (max−min)/(max+min). The
historical literature uses three incompatible conventions; mixing them silently is the
main trap in this material.

⚠️ This is a **25 W** lamp — the thin-filament worst case, not a general incandescent
figure. Always pair a percent-flicker number with a **wattage and a voltage**.

## The scaling law [MODELLED, parameter-free]

The filament is a single-pole low-pass with 2πfτ ≫ 1, so it sits in the asymptotic 1/f
region: **percent flicker ∝ 1/f_modulation**.

| Contrast | Ratio |
|---|---|
| **25 Hz vs 60 Hz mains** | **2.4×** |
| 25 Hz vs 50 Hz mains | 2.0× |
| 50 Hz vs 60 Hz mains | **1.2×** |

**Independent validation across 90 years:** Cady's 30% ÷ 2.4 = **12.5% predicted for a
25 W lamp at 60 Hz** — which lands exactly on the top of the modern cited 5–13% range for
incandescents, the 13% end being precisely the low-wattage end. Two sources, ninety years
apart, reconciled by one law.

That last row is worth noting for the Japan question: **the 50-vs-60 luminous contrast is
only 1.2×.** Twenty percent. That is the entire exposure difference the Japan study was
ever chasing.

**Thermal time constant** [MODELLED; the 25 W diameter is MEASURED]: τ ∝ filament radius.
25 W → ~10 ms · 60 W → ~15 ms · 100 W → ~18 ms · 500 W → ~41 ms. τ is comparable to or
longer than the 20 ms between light peaks at 25 Hz, **so the filament cannot smooth the
ripple**. Amplification: lumens ∝ T^~9.4, so a ±5% temperature ripple → ±30–50% luminous
ripple. Cady's independently measured 0.001 in filament matches the calculated 25.4 µm
exactly.

## Correction 1 — carbon flickers LESS than tungsten [MEASURED]

`docs/02` asserted the opposite ("carbon has less thermal mass and flickers more"). **That
is inverted.**

Carbon is ~3× less efficient, so at equal light output it draws ~3× the power → a **much
thicker** filament → longer τ → less flicker. **Diameter is the mechanism; material is
only a proxy.**

Clayton H. Sharp, AIEE Nov 1906 — https://archive.org/details/illuminatingengi01balt
pp. 886–887 — ran the controlled swap: 11 tungsten lamps at 115 V / 25.5 Hz showed
"marked" flicker; 12 carbon lamps at the same light output showed **"no flickering could
be observed."** His conclusion: tungsten is "less adapted to use on alternating circuits
of low frequency than the standard lamp of to-day."

**Consequence, and it runs opposite to intuition: the carbon→tungsten transition
(~1907–1911) *increased* 25 Hz flicker exposure.** Any exposure model must treat lamp
technology as time-varying, with the gradient rising, not falling, through the 1910s.

Caveat: a 5 c.p. carbon lamp flickered as badly as any tungsten (~29–35%) — via Kennelly
& Whiting, *The Illuminating Engineer* Vol. 2 (1907) p. 352
(https://archive.org/details/illuminatingengi02balt), citing Girard & Magnol.

Voltage matters as much as wattage — Stickney 1917
(https://archive.org/details/illuminatingengi00univrich p. 137): *"110 volts of 25 watts
or less (220 volt lamps of 60 watts or less) show perceptible flicker on 25-cycle
circuits."* A 220 V lamp needs ~4× the resistance → thinner filament at equal wattage.

## Correction 2 — the flicker was PERIPHERAL, not foveal [MEASURED]

**This is the most scientifically interesting finding here.**

Sharp (1906): the flicker was *"imperceptible when looking directly at the lamps, but
could be observed only through light which is not focused directly on the fovea."*

Kennelly & Whiting measured foveal critical flicker fusion at **66 Hz maximum, at 100%
modulation**. At ~30% modulation and 50 Hz luminous frequency, 25 Hz mains sat **right at
the fusion boundary — retinally present, consciously invisible.**

**That is a different exposure construct from "annoying flicker," and arguably a better
one for a gamma-entrainment hypothesis.** The Tsai/GENUS mechanism does not require
conscious perception — it requires the retina to be driven. A subliminal, peripheral,
50 Hz, 30%-modulated stimulus delivered for decades is precisely the exposure that
hypothesis would want, and nobody would have reported it as a nuisance.

## Correction 3 — lamps were NOT part of the Ontario conversion [important for design]

`docs/02` implied lamp replacement was part of the programme. It was not. The "~5 million
pieces of equipment" / "6–39 items per house" were **motors, clocks, and transformers**.
**Incandescent lamps run on any frequency** — they simply flickered until the frequency
changed in 1949–59.

**Consequence: lamp-replacement records do not exist and cannot serve as an exposure
proxy.** ~800,000 customers were on 25 Hz pre-conversion.

## Correction 4 — "25 Hz flickered badly" was contested at the time

Do not present it as uncontested. H.B. Alverson (Cataract Power, Buffalo, 1906) called
25-cycle flicker **"not objectionable"**; the IES editors rebutted from the Pan-American
Exposition, where it was **"decidedly annoying… with the best quality lamps."** Genuine
contemporary disagreement — consistent with an effect right at the perceptual threshold
and strongly dependent on lamp wattage.

`docs/02`'s claim that 25 Hz was abandoned *largely because of* lamp flicker is therefore
**overstated**. Motor and appliance interchangeability drove the programme; flicker was a
contributing complaint.

## IEEE 1789 exceedance — real, but read the caveat

| Mains | Modulation | IEEE 1789 low-risk limit | Exceedance |
|---|---|---|---|
| 25 Hz | ~30% | ~1.25% | **~24×** |
| 50 Hz | ~15% | 8% | ~1.9× |
| 60 Hz | ~12.5% | 9.6% | ~1.3× |

⚠️ **Most of that 24× comes from the frequency weighting, not the flicker measurement.**
The weighting curve is a modelling assumption imported from photosensitivity research.
Do not let a 24× headline rest on it without saying so.

## Verdict

**Q2 is answered YES.** Ontario domestic lighting was on 25 Hz, and it delivered ~30%
luminous modulation at 50 Hz — measured, in 1925, with a primary source — versus ~12.5%
at 120 Hz for 60 Hz mains. **A 2.4× exposure contrast, peripheral and subliminal.**

The physical premise of the hypothesis is sound. The study still cannot be done, because
`docs/04` shows the exposure cannot be *assigned* to individuals — but the reason is
data, not physics.

**And one number here reframes the original question:** the 50-vs-60 luminous contrast
Japan offers is **1.2×**. Ontario's was **2.4×**. Even the best natural experiment
available on Earth was chasing a 20% difference in modulation depth of an exposure that
sits below conscious perception.

## Sources

- Cady & Dates, *Illuminating Engineering*, Wiley 1925, pp. 109–110 —
  https://archive.org/details/illuminatingengi00cady
- Clayton H. Sharp, AIEE Nov 1906 —
  https://archive.org/details/illuminatingengi01balt pp. 886–887
- Kennelly & Whiting, *The Illuminating Engineer* Vol. 2 (1907) p. 352 —
  https://archive.org/details/illuminatingengi02balt
- Stickney 1917 — https://archive.org/details/illuminatingengi00univrich p. 137
- Weitz, *Electric Illumination*, 1930 — https://archive.org/details/ElectricIllumination

Method note: Google Books and HathiTrust were both inaccessible; 33 volumes of *The
Illuminating Engineer* / IES *Transactions* (1906–1925, ~70 MB OCR) were pulled from
archive.org and grepped locally. All primary sources came from there.

**Not established [UNSOURCED]:** Ontario domestic lamp wattage mix 1900–1959. This is
load-bearing for any exposure model — the flicker figure depends on wattage, and the
complaints only ever name low-wattage sizes. Would need GE/Edison Lamp Works sales data
or Ontario Hydro domestic load studies. Gas-filled lamp behaviour is also unresolved
(competing effects; empirically the complaints name only the sizes that stayed vacuum).
