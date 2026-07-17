# Data provenance

Every raw input must be recorded here **before** it is used: what it is, where it came
from, when it was retrieved, and how to retrieve it again. Files in `data/raw/` are
never edited — all cleaning happens in `src/` and lands in `data/processed/`.

Status key: ✅ obtained · ⏳ in progress · 🔒 requires manual step · ❌ unavailable

---

## Inputs required

| # | Dataset | Purpose | Status |
|---|---|---|---|
| 1 | LTCI dementia assessment (認知症高齢者の日常生活自立度), municipality × year | Primary outcome | ⏳ |
| 2 | Census / population estimates, municipality & prefecture × 5-yr age band | Denominator for standardisation | ⏳ |
| 3 | Prefecture → mains frequency mapping | Exposure | ⏳ |
| 4 | Municipality → mains frequency, for split prefectures | Exposure (Tier 3) | ⏳ |
| 5 | Frequency boundary geometry (polyline) | RD running variable | ⏳ |
| 6 | Placebo outcomes (colorectal cancer, stroke, IHD, hip fracture) | Falsification | ⏳ |
| 7 | Balance covariates (income, density, education, physician density) | Balance tests | ⏳ |
| 8 | GBD Japan subnational prevalence | Fallback/secondary outcome | ⏳ |

---

## 1. Original chart under critique

- **File:** `docs/original_chart_UNRELIABLE.png`
- **Provenance:** supplied by the project originator; analysis performed elsewhere.
- **Forensics:** PNG metadata records `Matplotlib version 3.6.3`. This machine runs
  matplotlib 3.10.8, so the chart was generated in a different environment. 3.6.3 is
  consistent with a hosted code-interpreter sandbox of that era.
- **Unresolved:** the chart plots 1980–1989, but its stated source (GBD 2021) begins at
  1990. **Action required from the originator:** identify the file containing the 1980s
  rows, or confirm that no such file exists. Until then those points are treated as
  unverified. See `docs/00_critique_of_initial_analysis.md` Finding 2.
- **Disposition:** not used as an input. Retained only as the object of the critique.

## 2. Stated sources of the original analysis (for the record)

Not used going forward — see `docs/01_why_international_comparison_fails.md`.

- IHME GBD 2021, measure "Probability of death", cause "Alzheimer's disease and other
  dementias", all ages, both sexes, 1990–2021, country level.
  Retrieved via https://vizhub.healthdata.org/gbd-results/ (date unknown).
- World Bank WDI `EG.ELC.ACCS.ZS`, https://data.worldbank.org (date unknown).
- Mains frequency by country, hand-classified from
  https://en.wikipedia.org/wiki/Mains_electricity_by_country (date unknown).

## 3. e-Stat (政府統計の総合窓口) — Japanese government statistics

- **Portal:** https://www.e-stat.go.jp
- **API:** https://api.e-stat.go.jp — requires a free `appId`.

### Obtaining an appId (verified 2026-07-16)

**The registration form is NOT on the `/api/` documentation page.** This is the single
most confusing part of the process — `/api/` only links to user registration and login,
never to ID issuance. The form lives inside My Page.

1. Create an e-Stat account (if needed):
   https://www.e-stat.go.jp/mypage/user/preregister
   (email → 仮登録 → confirm link → set password → 本登録)
2. Log in: https://www.e-stat.go.jp/mypage/login
3. **Go directly to: https://www.e-stat.go.jp/mypage/view/api**
   Equivalently: マイページ → **「API機能(アプリケーションID発行)」**
   (Both `/mypage/view/api` and `/api/apiuser/php/index.php` resolve to the same place;
   unauthenticated they redirect to an identical login page.)
4. The page offers **three slots** (for managing up to three apps). Fill **row 1** only:
   | Field | Value |
   |---|---|
   | \*名称 (Name) | required — e.g. `50vs60-dementia-study` |
   | \*URL | required — **must be a real public URL you control** |
   | 概要 (Description) | optional |
5. Click **発行** (Issue). The appId populates in the `appId` row immediately — no
   approval queue. Buttons: 発行 = issue, 変更 = change, 廃止 = revoke.

**⚠️ localhost is REJECTED.** The form states:
> ※http://localhostやプライベートIPアドレス（127.0.0.1等）は登録できません
> *(localhost and private IP addresses such as 127.0.0.1 cannot be registered)*

Older guides (incl. several blog walkthroughs) still recommend `http://test.localhost/`
— **that advice is stale and will fail.** Use a domain you own or a GitHub repo URL.
The URL is bookkeeping only; e-Stat does not fetch it. Do not use `example.com`.

**Gotcha:** if browsing in English, the My Page menu may not expose the API item. Switch
the site to 日本語 and retry; parts of the API registration UI are Japanese-only.

**Storage:** place in `.estat_appid` (git-ignored) or export as `ESTAT_APPID`.
Never commit it.

- **Retrieved:** _pending_

## 4. IHME GBD 2021 — Japan prefecture-level dementia prevalence 🔒

**Resolved 2026-07-16. GBD 2021 DOES include all 47 Japan prefectures.**

- **Host:** `https://gbd2021.healthdata.org/gbd-results/`
  ⚠️ **Not** `vizhub.healthdata.org` — that now serves **GBD 2023 only**. Location ids
  differ between rounds; using the wrong host silently gives you the wrong data.
- **Supporting publication:** "Three decades of population health changes in Japan,
  1990–2021: a subnational analysis for GBD 2021", *Lancet Public Health*, Mar 2025.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC11959113/

### Verified IDs (checked live against the metadata API, `src/02_fetch_gbd.py`)

| Field | Value |
|---|---|
| GBD version | 8016 (GBD 2021) |
| Cause | **543** — Alzheimer's disease and other dementias |
| Measure | **5** = Prevalence, **6** = Incidence |
| Measure to AVOID | **27** = Probability of death — what the original analysis used |
| Metric | **1** = Number, **3** = Rate |
| Japan | location id 67 |
| Prefectures | ids **35424–35470** (47). **JIS code = gbd_id − 35423**, verified all 47 |
| Age bands (65+) | ids **18, 19, 20, 30, 31, 32, 235** = 65-69 … 95+ |
| Terminal band | **235** (95+). Note id 33 (95-99) is *not* valid for this cause+measure |
| Years | 1990–2021 |

### Access status

- **Metadata + hierarchy endpoints: open, unauthenticated.** Scripted, working:
  - `GET https://gbd2021.healthdata.org/gbd-results/php/hierarchy/`
  - `GET https://gbd2021.healthdata.org/gbd-results/php/metadata/?language=en`
  - Requires a browser `User-Agent`. Saved to `data/raw/gbd2021_*.json`.
- **Data endpoint (`php/data.php`): Cloudflare Turnstile challenge (403
  `cf-mitigated: challenge`).** curl cannot solve it. **One browser session required.**
- Useful lever: `php/get_download_result.php?taskID=<id>` is **not** Turnstile-gated,
  so once a taskID exists, polling/fetching the zip can be scripted.
- No prefecture-level flat file exists on GHDx. The nearest record
  (`gbd-2021-nervous-system-disorders-1990-2021`, DOI `10.6069/728K-CK32`) is a
  2021-only summary XLSX with no prefectures. No usable mirrors (`s3.healthdata.org`
  no longer resolves; `ddf_utils`' IHME loader is dead).

### Manual step

Run `python src/02_fetch_gbd.py` — it verifies all IDs live and prints the exact query.
Summary: sign in (free IHME account + non-commercial user agreement), select the query
above, download, and place the CSV at
`data/raw/gbd2021_japan_prefecture_dementia_prevalence.csv`.

**Row budget:** 47 × 7 ages × 3 sexes × 32 years × 2 metrics = **63,168 rows**, under
the 100,000 cap → **single download**. Selecting all 20 age bands would exceed the cap
and force chunking; only the 7 bands at 65+ are needed.

- **Retrieved:** _pending manual browser step_

### ⛔ Caveat that survives acquisition — read before using this data

**IHME's own Japan subnational paper says the prefecture-level estimates may contain
little real regional signal.** Verbatim, from the Limitations section of the Lancet
Public Health 2025 paper (https://pmc.ncbi.nlm.nih.gov/articles/PMC11959113/):

> "Limitations from Japan's GBD 2015 study persist, despite methodological
> improvements. **Data gaps remain at both the national and prefectural levels. GBD
> disease models compensate by using regional data and covariates, potentially
> resulting in minimal regional variation in certain diseases and risk factors due to
> limited Japanese data coverage.**"

and:

> "Furthermore, incomplete temporal coverage means 2021 estimates relied heavily on GBD
> disease models."

This is close to fatal for a GBD-based test of this hypothesis. Our exposure varies
**between prefectures**; if between-prefecture variation in the outcome is substantially
**model output** rather than measurement, then regressing it on any prefecture-level
variable recovers IHME's covariate structure, not Japan. The test would be near-circular.

It also independently explains Finding 4 in `docs/00_critique_of_initial_analysis.md`
(the original chart's implausibly smooth, parallel, never-crossing series) — that is
what a covariate-driven model looks like.

Note further: the paper reports **no prefecture-level dementia variation** at all, and
does not identify any prefecture-level dementia data source.

**Consequence:** GBD is demoted from "fallback outcome" to "not fit for this purpose
unless the methods appendix demonstrates real prefecture-level dementia inputs."
**LTCI (§3) is not merely preferred — it is the only candidate that measures anything.**
Verifying this against appendix 1 (`mmc1.pdf`, 13.4 MB) is an open task.

## 5. Mains frequency mapping

- **Output:** `data/reference/prefecture_frequency.csv`
- **Sources:** documented in `data/reference/SOURCES.md`
- **Built by:** `src/01_build_frequency_map.py`
- **Retrieved:** _pending_

---

## Retrieval log

| Date | Dataset | By | Notes |
|---|---|---|---|
| 2026-07-16 | (repo initialised) | — | Scaffolding, pre-registration, critique docs |
