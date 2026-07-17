# Sources for the Japan mains-frequency reference tables

Backs `prefecture_frequency.csv` and `frequency_conversions.csv`, built by
`src/01_build_frequency_map.py`.

## ⚠️ Two sourcing warnings, read first

**1. Wikipedia's Japan frequency lists are contaminated and widely mirrored.**

- **軽井沢町 (Karuizawa) is listed as having 50 Hz areas. This is FALSE.** Karuizawa has
  never appeared on Chubu Electric's own frequency page — absent from the 2015 and 2019
  table snapshots, unshaded on Chuden's 2012 and current maps, absent from the current
  map's alt-text. Traced to **revid 37430298, 2011-05-03, anonymous IP 220.219.220.119,
  no source**. It has persisted 15 years. **Code Karuizawa as 60 Hz.**
- **Gunma's 「安中市・吾妻郡の各一部」 is uncited** and unstable across revisions (the same
  2011 IP edit carried a different, larger list, since silently reduced). The Niigata and
  Nagano bullets each carry a `<ref>`; Gunma has none.
- **Aggregator sites that "confirm" these are downstream of Wikipedia, not independent
  corroboration.** Neither are LLM search summaries.

**2. The two best granular sources are dead links.** The Chubu hamlet table and the
Tohoku district list survive only in the Internet Archive. Wayback URLs with snapshot
dates are given below. **Before publication, write to Chubu Electric Power Grid and
Tohoku EPCO for a current authoritative statement.**

## Prefecture-level assignment

- Chubu Electric Power, frequency page —
  https://miraiz.chuden.co.jp/home/electric/contract/structure/frequency/
  Fetched directly. 「長野県は、原則60ヘルツにて供給しております」 — confirms Nagano is
  **60 Hz dominant** with 50 Hz exceptions, not the reverse.
- Hokuriku Electric Power Transmission & Distribution —
  https://www.rikuden.co.jp/nw_qa/hz.html — 「北陸電力送配電管内は６０Ｈｚ」.
  Confirms Hokuriku is 60 Hz despite its northerly latitude; the split follows the
  **Itoigawa–Shizuoka Tectonic Line**, and Hokuriku lies west of it. Latitude is
  irrelevant.
- 商用電源周波数 (ja.wikipedia) — https://ja.wikipedia.org/wiki/商用電源周波数
  Used only where corroborated by a utility source. See warnings above.

**Utility territory does NOT predict frequency.** Four genuine mismatches: Tohoku (a
50 Hz company) supplies 60 Hz in Niigata; Chubu (60 Hz) supplies 50 Hz in Nagano; TEPCO
(50 Hz) supplies 60 Hz in Gunma; Shizuoka splits internally. Do not derive frequency
from utility.

## Shizuoka — the boundary

- 富士市 — https://www.city.fuji.shizuoka.jp/1005330000/p007275.html
  「富士川以東…東京電力エナジーパートナー／富士川以西（旧富士川町）…中部電力パワーグリッド清水営業所」
- 富士宮市 — https://www.city.fujinomiya.lg.jp/1050100000/p003798.html
  「内房(うつぶさ)地区を除く市内全域は、東京電力株式会社の管内です。内房(うつぶさ)地区は、
  中部電力株式会社の管内です。」

**左岸/右岸 trap.** Wikipedia says 「富士川の左岸側が50 Hz、右岸側…が60 Hz」. The Fuji
River flows **north→south**; facing downstream, left hand = **east**. So 左岸 = east =
50 Hz — identical to "east of the Fuji River is 50 Hz." No contradiction. A WebFetch
summary of the 富士川 article got this backwards; it is a real trap.

**Sub-municipal coding is mandatory in 富士市**: 旧富士川町域 (west bank, **16,395** at
2008 merger) is 60 Hz inside a ~250k 50 Hz city. 富士宮市 内房地区 (2,997 at 1955 census)
likewise. The legal line follows **former village boundaries** from a 1956 cross-*gun*
merger — administrative, not hydrological, so it tracks the river closely but not its
centreline.

## Niigata

- Tohoku EPCO district list — live page 404; recovered from
  http://web.archive.org/web/20190915051658/http://www.tohoku-epco.co.jp/dprivate/moving/procedure.html
  「新潟県妙高市、糸魚川市の一部と佐渡市全域が60Hzです」
  — 佐渡市全域 / 妙高市：樽本丙地区（斑尾）/ 糸魚川市：橋立、清水倉、市振、玉ノ木、上路地区
- Corroborated by two **live** Tohoku technical PDFs:
  https://nw.tohoku-epco.co.jp/consignment/system/rule/pdf/rule004.pdf and
  https://nw.tohoku-epco.co.jp/consignment/system/pdf/UFR_henkou_irai.pdf
  (lists Sado as a separate row with no 一部 qualifier → **all of Sado is 60 Hz**).

The boundary here is **not the Himekawa**: western Itoigawa is cut off by 親不知 and fed
across the 境川 from Toyama.

## Nagano — 50 Hz hamlets

Chubu's full hamlet table (live page now shows only a map); recovered from
http://web.archive.org/web/20190820034443/http://www.chuden.co.jp/home/shikumi/shi_keiyaku/hertz/index.html

**9 municipalities**: 栄村, 野沢温泉村, 飯山市, 小諸市 (高峰高原), 佐久市 (田口),
松本市 (奈川地区全域, 上高地, 白骨, 沢渡…), 安曇野市穂高町 (有明中房), 大町市平区 (高瀬入),
小谷村. Mechanism: TEPCO captive-hydro catchments in the North Japan Alps (梓川・高瀬川水系).

## Gunma — real but unlocalized

TEPCO PG 託送供給等約款 附則2 —
https://www.tepco.co.jp/pg/consignment/notification/pdf/takusou_yakkan20240117.pdf
「標準周波数60ヘルツで電気を供給している区域については…**群馬県の一部**」

Legally binding, but **names no municipalities**. TEPCO returns 403 to automated
fetching; read once by a subagent. Chuden's frequency page doesn't mention Gunma. A
journalist field-checked and failed: https://dailyportalz.jp/b/cs/mitekite/detail/121014156669/1.htm
— 「はっきりとした答えが得られませんでした」.

**Do not code Gunma from Wikipedia.** Likely a few border hamlets near 碓氷峠/北軽井沢,
not population-scale. Decisive source would be a direct query to TEPCO PG or Chuden PG's
高崎/佐久 office.

## Historical origin

- 門井龍太郎, 電気学会雑誌 111(12), 1991 — https://doi.org/10.11526/ieejjournal1888.111.1011
  「明治28年9月（1895年）大規模な火力・浅草発電所を建設し、3,000V交流配電方式を始めた」
- 『東京電灯会社史』(1956), p.241 — 浅草火力発電所 着工 1893 → 使用開始 **1895-09-20**.
  Generators: **AEG 3-phase, 265 kW, 3,000 V, 50 Hz × 2**, *plus* 石川島造船所 single-phase
  200 kW × 4 at **100 Hz** — Asakusa was itself a mixed-frequency plant.
- 大阪電燈: founded 1888, AC from 1889 — **but not 60 Hz**. 西道頓堀 used a
  Thomson-Houston single-phase **1,150 V, 125 Hz** lighting-only machine.
  **First 60 Hz = March 1897, 幸町発電所, 150 kW × 2, 2,300 V, monocyclic.** Thomson-Houston
  merged into GE in 1892 and "monocyclic" is Steinmetz/GE proprietary → GE attribution holds.

⚠️ **ja.wikipedia's 「1893年に浅草火力発電所を稼動させた」 is an error contradicting its own
cited source.** 1893 is construction start; operation began 1895.

**Framing caveat for any paper:** neither firm "chose a national standard." 門井 documents
**12+ frequencies (25–133 Hz)** in early Japan. The 50/60 split consolidated later through
mergers. **The tidy AEG-vs-GE story is a retrospective simplification** — true in outline,
misleading if presented as a clean two-way choice.

## The five conversions

| key | source |
|---|---|
| `kyushu1961` | 『九州周波数統一史』(1961). Contains a **national** conversion list. Offline at NDL. Partly accessed via a forum transcription: https://uub.jp/frm/search.cgi?KJNS=28180+28186+28192+28193+28200+28234+28238+28245+28250+28251+28255+28256+28283+28293+28294+28405+28450&TITLE=電力周波数&KJN=1 |
| `ndl1024150` | NDL PID 1024150, p.19 (1940): 「東の半分が五十サイクルで、西の半分が六十サイクル…**北海道でもさうであります**」 |
| `nakagawa1985` | 中川浩一 (1985a), p.89: 「東京電力が茨城県内に残していた60ヘルツ地区を50ヘルツに切り替える方針を受けて、**1961年6月には50ヘルツ用発電所に改められた**」. See also 石岡第一発電所 — https://ja.wikipedia.org/wiki/石岡第一発電所 |
| `itami_note` | https://note.com/itami_k/n/n06960b4bd367 — **single source, low confidence**; era-year conversions internally inconsistent (renders 昭和18年 as both "1943年" and "1943年（昭和43年）"). |
| `kashima2016` | 加島篤 (2016) — https://kitakyushu.repo.nii.ac.jp/records/110 — 博多電灯 was **60 Hz**; the 50 Hz came from **九州電気軌道** (大門発電所, May 1911, BTH 1,000 kW 50 Hz × 3). Reason 「不明」; hypothesises a deliberate 「周波数の壁」. |

**Eastern Kyushu scale:** the Dec 1934 official 「周波數別地域圖」 shows the 50 Hz zone was
**the entire eastern half of Kyushu**. 『九州周波数統一史』: 「福岡県は又九州の縮図で東半は
50サイクル、西半は60サイクル、福岡市は又その縮図で、東半が50サイクル西半は60サイクルであった。」
~590,000 kW of 50 Hz plant in 1949; cost ~¥11 bn; completed June 1960.

**Clean negatives:** Okinawa — 60 Hz throughout, **never converted** (1972 reversion was
institutional only). Chugoku/San'in — 60 Hz on the 1934 map, **no conversion**.
Hokuriku — no documented conversion. Yamanashi — entirely 50 Hz.

**Name trap:** 山梨県南巨摩郡富士川町 ≠ 静岡県庵原郡富士川町. The Yamanashi one is 50 Hz.

## Not verified

- Gunma's 60 Hz municipalities — no utility source names any.
- Sado's conversion year — 1954 vs 1950 disputed. The *fact* is solid; the date is not.
- **Within-year cutover schedules.** No municipality-level timetable survives for
  Hokkaido 1943–46 — that exposure is a **~3-year rolling transition, not a step
  function**. Same for Kyushu Phase 2 (1954–60). This matters for any cohort design.
- Populations of individual Nagano/Niigata hamlets — not published.

## Highest-value untapped sources

- 『九州周波数統一史』(1961) — national conversion list, offline at NDL.
- 『北海道電気事業史』(1978) — https://dl.ndl.go.jp/pid/12108146 (NDL-premises-only).
- 石田隆張「北海道における50 Hzのなかの60 Hz」電気学会誌 145(7), 2025,
  DOI 10.1541/ieejjournal.145.362 (paywalled).

## Frequency converter stations — NOT exposure variables

Sakuma (300 MW, 1965), Shin-Shinano (600 MW, 1977/1992), Higashi-Shimizu (300 MW
installed but capped at 100 MW until Feb 2013), Hida-Shinano HVDC (900 MW, 2021).
East–West interchange: 300 → 600 → 900 → **1,000 usable at 2011-03-11** (not 1,200 —
that was nameplate) → 1,200 (2013) → **2,100 (2021)** → 3,000 target, **slipping to
2030+**.

**南福光 is NOT a frequency converter** — a 60↔60 Hz back-to-back DC link
(Chubu↔Hokuriku), abolished 2026-04-01.

These are grid interties; they **do not set local supply frequency** and are irrelevant
as exposure variables. That Sakuma and Higashi-Shimizu both sit in Shizuoka is a
coincidence of the tectonic boundary, not a confounder.
