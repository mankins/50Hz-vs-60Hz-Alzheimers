# Japan data availability: the study cannot be done with public data

**Status: definitive. Verified empirically 2026-07-17 against downloaded files.**

This document records the single most important practical finding of the project:
**every design in `METHODS.md` is blocked, not by power, but by data that does not
exist.** This is a stronger and more useful result than a null.

## The question

To test whether mains frequency affects dementia, we need dementia counts by
**geography** (finer than prefecture, to exploit the boundary) crossed with **age**
(to standardise), on a **population denominator**.

## What actually exists

Three candidate sources. All three fail, for three different reasons.

### 1. IHME GBD 2021 — exists, but is modelled

Contains all 47 prefectures (ids 35424–35470), prevalence and incidence, 5-year bands
to 95+, 1990–2021. Obtainable (one browser session; see `PROVENANCE.md` §4).

**Disqualified by IHME's own authors.** From the Limitations of the Lancet Public Health
2025 Japan subnational paper:

> "Data gaps remain at both the national and prefectural levels. GBD disease models
> compensate by using regional data and covariates, **potentially resulting in minimal
> regional variation** in certain diseases and risk factors due to limited Japanese data
> coverage."

Our exposure varies between prefectures. If the outcome's between-prefecture variation
is model output, regressing one on the other is near-circular.

### 2. 介護保険事業状況報告 (LTCI Business Status Report) — no dementia variable

File-only on e-Stat (`toukei=00450351`); **not in the API** — which is why
`statsCode=00450351` returns zero from `getStatsList`. Files download fine with plain
curl, no appId:

```bash
curl -L "https://www.e-stat.go.jp/stat-search/file-download?statInfId=<id>&fileKind=0"
```

Contains 要介護（要支援）認定者数, 保険給付費 etc. by 都道府県 and 保険者.
**Contains no dementia variable of any kind.** Verified against the full annual-report
table listing: no 認知症, no 認知症高齢者の日常生活自立度.

### 3. 介護DBオープンデータ — real measurement, but the two axes never meet

**This is the important one.** MHLW publishes aggregated 要介護認定 records — actual
certification-survey data, *measured*, not modelled. Four rounds covering 2017–2023.
https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/kaigo_koureisha/nintei/index_00009.html

It **does** contain 認知症高齢者自立度 (table item 15). And it **does** have
municipality (保険者) geography. But not together:

| Table item | 都道府県 (表1) | 性・年齢階級 (表2) | 要介護度 (表3) | **保険者 (表4)** |
|---|---|---|---|---|
| 1 申請区分 | ● | ● | ● | ● |
| 5 二次判定結果 | ● | ● | – | ● |
| **15 認知症高齢者自立度** | ● | ● | ● | **–** |

Verified empirically by downloading the files (`data/raw/kaigodb/`):

- `001716234.xlsx` — 保険者別. Contains **only** 表4-1 and 表4-5. 1,585 rows: every
  insurer with its code (`011007 札幌市` …). Columns are **care levels**. No dementia.
- `001716226.xlsx` — 都道府県別. Contains 表1-15 = dementia × prefecture. 58 rows,
  columns 自立/Ⅰ/Ⅱa/Ⅱb/Ⅲa/Ⅲb/Ⅳ/M. **No age dimension.**
- `001716227.xlsx` — 性・年齢階級別. Contains 表2-15 = dementia × age/sex.
  **No prefecture dimension.**

These are **two-way marginal tables, not a three-way cross-tab.**

### 4. e-Stat — independent confirmation, and it is worse than §3 suggested

A separate research pass over e-Stat reached the same conclusion by a different route, and
added two facts:

**認知症高齢者の日常生活自立度 exists nowhere on e-Stat at any subnational level.**
It appears in exactly one survey — 介護サービス施設・事業所調査 (`toukei=00450042`) — and:

- it covers **facility residents only** (在所者数, ~934k people), not the
  community-dwelling population — a profoundly selected group, since entering a care
  facility is itself partly caused by dementia;
- its metadata states 集計地域区分: **該当なし** — *no regional breakdown at all*. National
  totals only.

Verified by download, e.g. table 第61表 (`statInfId=000040149364`, `fileKind=1`) giving
施設種類 × 性 × 年齢階級 × 認知症自立度.

**地域包括ケア「見える化」システム** (mieruka.mhlw.go.jp) does hold municipality 認定
data, but is **registration-gated and interactive — no bulk download, no API.**

**The municipality-level 「自立度Ⅱ以上」 figures one sees cited are MHLW ad-hoc estimates**
derived from raw 認定調査 records, not a standing statistical table.

### ⛔ Why the obvious workaround does not work

The tempting move — and one a collaborator will propose — is to **apply national
age/sex/care-level-specific dementia rates to municipality 要介護認定 counts**.

**Reject this.** If the dementia rates come from national tables, the resulting
municipality "dementia count" is a deterministic rescaling of 要介護認定者数. It contains
**zero independent municipality-level dementia signal**. Regressing it on mains frequency
would test whether frequency predicts *care-need certification* — which is dominated by
physical frailty, and by local administrative and service-availability practice — while
appearing to test dementia.

This is structurally identical to the GBD problem in §1: a covariate-driven derived
quantity wearing the costume of a measurement. It is also, note, exactly the formula the
見える化 system uses (「割合を要介護認定者数に乗じて算出」).

### What Japan *does* offer (for the record, and for other questions)

Solved and downloadable with **no appId** — the file-download endpoint is unauthenticated:

```bash
curl -L "https://www.e-stat.go.jp/stat-search/file-download?statInfId=<id>&fileKind=0"
```

- **要介護認定 by care level, municipality (保険者) level, FY2001–FY2023** — 23 complete
  years, ~1,350–1,570 insurers. (FY2000 has no 保険者別 table.) FY2001–2017 are `.xls`
  (need `xlrd`); FY2018–2023 are `.xlsx`.
- **Prefecture × age band × care level**, monthly, 2015+ — via MHLW static files, not
  e-Stat: `https://www.mhlw.go.jp/topics/kaigo/osirase/jigyo/m{YY}/xls/{YYMM}-t2-1.xlsx`
  (age bands 65-70/70-75/75-80/80-85/85-90/90+).
- **Population by age** — census and estimates. Caveats: 人口推計 annual files are in
  **千人** and cap at 80+ (1991–2006) or 85+ (2007–2021); only per-census 基本集計 tables
  carry single-year age to 100+. **1990 is not on e-Stat at all** (no 平成2年 tstat —
  the list jumps 昭和55年 → 平成7年). 2015 has **1.45M (1.1%) age-不詳**; use the 不詳補完
  tables or denominators drift.

None of this contains dementia. It is the denominator and the wrong numerator.

## The three blocking facts

**1. Municipality × dementia does not exist publicly.**
The municipality geography is there (1,571 insurers, coded). The dementia variable is
there. They are never crossed. So **Tier 3 — the spatial RD, the only design in which
frequency is plausibly exogenous — is impossible.** Not underpowered. Impossible.

**2. Prefecture × age × dementia does not exist publicly.**
表1-15 gives dementia by prefecture with no age. 表2-15 gives dementia by age with no
prefecture. Direct standardisation needs both at once. **So Tier 1 cannot be
age-standardised** — meaning the exact confounder that produced the artefact in the
original chart (`docs/00_critique_of_initial_analysis.md`, Finding 3) cannot be removed.
An unstandardised prefecture analysis would reproduce the original error.

**3. The denominator is applicants, not population.**
表1-15's 総数 for 2023 is 1,624,300 — the number of **certification applications**, not
the population. So any rate computed from it is "dementia among people who applied for
long-term care," a heavily selected group whose selection varies by municipality with
service availability, family structure and administrative practice. This is not
population prevalence and cannot be made into it.

## Verdict

| Design | Blocked by |
|---|---|
| Tier 1 — prefecture ecological | no age cross-tab → cannot standardise → reproduces the original artefact |
| Tier 2 — municipality ecological | municipality × dementia does not exist |
| Tier 3 — spatial RD *(confirmatory)* | municipality × dementia does not exist |

**Every design in `METHODS.md` is blocked by data availability.** This supersedes the
power analysis in §9: we no longer reach the question of whether the study is powered,
because it cannot be assembled at all from public sources.

## What would unblock it

1. **介護DB research access.** The underlying database holds raw 認定調査 records, which
   *do* carry 保険者 code, 認知症高齢者の日常生活自立度, sex and age together. The
   published open data are marginal tables of exactly this. A research application to
   MHLW would yield the cross-tab we need.
   **Cost:** formal application, Japanese institutional affiliation, ethics review.
   Realistically a multi-month process requiring a Japanese collaborator.
   Contact listed for the open data: `opendata-kaigo-db@ml.mri.co.jp`
2. **JAGES cohort.** Individual-level, multi-municipality, with cognitive measures.
   Collaboration required.
3. **Go to Ontario instead** — see `docs/02_the_ontario_25hz_experiment.md`.

## Recommendation

The Japan route now requires a formal MHLW data application *before* any analysis can
begin — and even if granted, `METHODS.md` §9.2 says the resulting design detects only a
~31% effect. **That is a large, slow bet on a design already known to be underpowered.**

Ontario needs no such application to *start*: the exposure history is archival and
public, and the outcome data (ICES) is a well-trodden application path in English with
a far better design attached to it.

## Reproducing these findings

```bash
# LTCI Business Status Report: file-only, no appId needed
curl -L "https://www.e-stat.go.jp/stat-search/file-download?statInfId=000040309318&fileKind=0" -o ltci.xlsx

# 介護DB open data, round 4 (2023): table index + the three key files
curl -L https://www.mhlw.go.jp/content/001716207.xlsx -o r4_table_list.xlsx  # index
curl -L https://www.mhlw.go.jp/content/001716226.xlsx -o r4_prefecture.xlsx  # 表1-*, has 表1-15
curl -L https://www.mhlw.go.jp/content/001716227.xlsx -o r4_age_sex.xlsx     # 表2-*, has 表2-15
curl -L https://www.mhlw.go.jp/content/001716234.xlsx -o r4_insurer.xlsx     # 表4-1, 表4-5 ONLY
```

Open `r4_table_list.xlsx`, sheet `ファイルと集計表の対応`, and confirm that the
保険者別 row lists only 表4-1 and 表4-5.
