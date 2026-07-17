# Japan's population dementia surveys: a real contrast, killed by ascertainment

**Verified 2026-07-17.**

This document evaluates the one Japan route that is *not* administrative data: the
population-based dementia cohorts, which measure dementia properly (clinical assessment,
population sampling) rather than counting care applicants.

**The suggestion was a good one and better than earlier notes credited.** The site
geography does *not* kill it — there is a genuine 50/60 Hz contrast. What kills it is an
ascertainment confound that is **perfectly aligned with the exposure**, and which would
manufacture the hypothesised result out of methodology alone.

## JPSC-AD — the only multi-site cohort with a frequency contrast

Japan Prospective Studies Collaboration for Aging and Dementia. Baseline 2016–18,
n=11,410. https://pmc.ncbi.nlm.nih.gov/articles/PMC7603740/

| Site | Prefecture | n | Recruitment | Hz |
|---|---|---|---|---|
| Hirosaki City | Aomori | 2,281 | **voluntary response** | **50** |
| Yahaba Town | Iwate | 962 | full enumeration | **50** |
| Arakawa Ward | Tokyo | 1,099 | simple random | **50** |
| Nakajima Town | Ishikawa | 2,128 | full enumeration | 60 |
| Ama Town | Shimane | 722 | full enumeration | 60 |
| Nakayama Town | Ehime | 927 | full enumeration | 60 |
| Hisayama Town | Fukuoka | 1,714 | full enumeration | 60 |
| Arao City | Kumamoto | 1,577 | full enumeration | 60 |

**3 sites / 4,342 participants (38.1%) at 50 Hz; 5 sites / 7,068 (61.9%) at 60 Hz.**

Note it does **not** include Obu/NCGG (Aichi) or Takashima (Shiga) — a common
misconception. Tohoku University is a collaborating institution (MRI analysis), not a
site. The contrast is real: two Tohoku sites plus central Tokyo on the 50 Hz side.

**It measures incidence** — the primary outcome is incident dementia among the
dementia-free, 8,334 followed 2016–2023 (GeroScience 2026,
https://link.springer.com/article/10.1007/s11357-026-02304-w). That is the right measure.

## ⛔ Why it fails: ascertainment is collinear with frequency

**The three sites with enhanced case-finding — home visits plus nursing-home visits — are
Nakajima, Nakayama, and Hisayama. All three are 60 Hz.** Prevalence at those sites is
**16.4% vs 8.5% overall.**

**Meanwhile the largest 50 Hz site, Hirosaki (n=2,281 — over half the entire 50 Hz
sample), used voluntary-response sampling**, which self-selects toward healthier, more
mobile participants.

Both biases push in the same direction:

> **60 Hz sites are ascertained harder. 50 Hz sites are ascertained softer.**

A naive prevalence contrast on this data will produce a **"60 Hz has more dementia"**
result of roughly the magnitude one would hope to detect — **entirely from methodology**.

**This is exactly the direction the original chart showed.** It is also exactly the
direction that `METHODS.md` §2.1 says the *mechanism* predicts against (120 Hz = 3×40 Hz
implies 60 Hz should be protective). A result that matches your prior here should
therefore be treated as evidence of the confound, not of the hypothesis.

The confound cannot be adjusted away with 8 sites, and cannot be distinguished from a
real effect. **The effective n for a site-level exposure is 8, not 11,410.**

## The other surveys are worse

**Asada 2013** (MHLW; the famous 462万人 / ~15% figure) —
https://www.tsukuba-psychiatry.com/wp-content/uploads/2013/06/H24Report_Part1.pdf

10 sites, but note the attrition pattern: **both dropped sites were 50 Hz** — Kurihara
(Miyagi) excluded after the Tōhoku earthquake, Joetsu (Niigata) dropped for low
physician-interview completion. That leaves **2 of 8 pooled sites at 50 Hz, and both are
in Ibaraki** (Tone Town, Tsukuba) — so **prefecture and frequency are perfectly
collinear**. Age-stratified (5-year bands, 65+, sex-specific); site-level tables
published, though the dementia tables in Part 2 are scanned images.

**MHLW 2024 official estimate** (Ninomiya; basis for the 2040 = 584.2万人 projection) —
https://www.mhlw.go.jp/content/001279920.pdf
Four full-enumeration sites, 2022: Hisayama, Nakajima, Nakayama, Ama. **All four 60 Hz.
Zero contrast.**

**Ninomiya 2015** — not a multi-site survey at all: projections built on **Hisayama
alone** (5 waves, 1985–2012), validated against Asada's other municipalities. The report
concedes it rests on 久山町の1地域. 60 Hz.

**Hisayama Study** — single town (Fukuoka, 60 Hz, ~8,400 people), autopsy-verified,
excellent, and useless for a contrast. Incidence: total dementia 32.3/1,000 person-years
at 65+; AD 14.6, VaD 9.5 (PMID 18977814).

**NILS-LSA, NCGG-SGS** — Obu/Higashiura, Aichi, 60 Hz.

## ⚠️ The 47-prefecture "dementia ranking" tables are an artifact — ignore them

The **Toyama Dementia Survey** publishes 47-prefecture projections
(https://bmcgeriatr.biomedcentral.com/articles/10.1186/s12877-021-02540-z), and these
circulate widely as 「47都道府県 認知症発症率ランキング」.

**They apply *Toyama's* age/sex-specific rates to each prefecture's population
structure.** Every prefecture is assigned **identical age-specific rates by
construction**. The tables therefore contain **exactly zero prefecture-level
information** — they are a pure re-rendering of each prefecture's age structure.

If anyone brings these to the project as evidence of regional variation in dementia, they
are showing you a map of Japan's demography. This is the same failure as the original
chart (`docs/00`, Finding 3), and the same failure as applying national rates to
municipality counts (`docs/03`).

## No prefecture-representative population data exists

Confirmed. Everything prefecture-level is either administrative/care-seeking (患者調査,
NDB, 介護保険) or a projection artifact like the above. The 3.6× Hiroshima-vs-Kanagawa
spread in Patient Survey data is dominated by diagnosis intensity and care supply, not
disease.

Historical surveys (37 prefectures + 10 designated cities, 1970s–80s, pooled into a
12-municipality estimate in 1985) lacked cognitive testing, used non-comparable methods,
and underestimated prevalence. Not usable.

## Access

**JPSC-AD:** *"not publicly available due to restrictions included in the informed
consent… available from the authors upon reasonable request and with the permission of
the Japan Agency for Medical Research and Development."* Plus JPSC-AD steering committee
approval. PI: **Toshiharu Ninomiya, Kyushu University**. Collaboration required.

**Asada 2013** site-level tables are freely downloadable.

## Verdict

**JPSC-AD incidence with site-level random effects is the only defensible Japan analysis
that exists.** Incidence among the dementia-free is the right measure, and baseline
ascertainment differences matter less there than for prevalence.

But: incident case-finding still runs through site-specific follow-up; the effective n is
**8**; and the ascertainment/frequency alignment means **a null is interpretable and a
positive result is not.** That asymmetry is unusual and worth stating plainly — it is a
study that can only disappoint or mislead.

If pursued, the honest framing is: pre-registered, incidence-only, site as the unit of
analysis, ascertainment method as an explicit covariate, requiring Ninomiya's
collaboration and AMED permission — with a stated commitment in advance that a positive
finding will be attributed to ascertainment unless it survives the covariate.
