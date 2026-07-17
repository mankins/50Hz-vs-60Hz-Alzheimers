"""Build the Japan mains-frequency reference tables.

Run: python src/01_build_frequency_map.py

Emits:
  data/reference/prefecture_frequency.csv    47 prefectures, CURRENT frequency
  data/reference/frequency_conversions.csv   historical conversions (the important one)

THE HEADLINE: the boundary is not static. Five documented conversions between 1943
and 1961 moved whole prefectures between frequencies. Any analysis that assigns a
prefecture a single fixed frequency -- as the original chart did -- misclassifies
exposure for exactly the birth cohorts who are developing dementia now.

Ōita and Miyazaki were 50 Hz until ~1951-60. Coding them "60 Hz" for a 1990-2021
dementia analysis assigns the wrong exposure to everyone born before ~1960.

Sourcing warnings, carried from the research pass:
  - Wikipedia's Japan frequency lists are CONTAMINATED. 軽井沢町 (Karuizawa) is listed
    as having 50 Hz areas; this is FALSE, traced to an unsourced 2011 anonymous edit
    (revid 37430298) that persisted 15 years and is widely mirrored. Aggregator sites
    "confirming" it are downstream of Wikipedia, not independent.
  - The two best granular sources (Chuden's hamlet table, Tohoku's district list) are
    DEAD LINKS surviving only in the Internet Archive. Wayback URLs are cited below.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "data" / "reference"

# jis_code, name_en, name_ja, current_hz, split?, utility, confidence, notes
PREFECTURES = [
    ("01", "Hokkaido",  "北海道",   "50", False, "Hokkaido EPCO", "certain",  "CONVERTED 60->50 west 1943-46"),
    ("02", "Aomori",    "青森県",   "50", False, "Tohoku EPCO",   "certain",  ""),
    ("03", "Iwate",     "岩手県",   "50", False, "Tohoku EPCO",   "certain",  ""),
    ("04", "Miyagi",    "宮城県",   "50", False, "Tohoku EPCO",   "certain",  ""),
    ("05", "Akita",     "秋田県",   "50", False, "Tohoku EPCO",   "certain",  ""),
    ("06", "Yamagata",  "山形県",   "50", False, "Tohoku EPCO",   "certain",  ""),
    ("07", "Fukushima", "福島県",   "50", False, "Tohoku/TEPCO",  "certain",  "CONVERTED 60->50 Hamadori/Iwaki 1961"),
    ("08", "Ibaraki",   "茨城県",   "50", False, "TEPCO/Tohoku",  "certain",  "CONVERTED 60->50 north (Mito, Hitachi) 1961"),
    ("09", "Tochigi",   "栃木県",   "50", False, "TEPCO",         "certain",  ""),
    ("10", "Gunma",     "群馬県",   "50", True,  "TEPCO",         "uncertain","60 Hz area exists per TEPCO tariff but NO source names the municipalities. DO NOT code from Wikipedia."),
    ("11", "Saitama",   "埼玉県",   "50", False, "TEPCO",         "certain",  ""),
    ("12", "Chiba",     "千葉県",   "50", False, "TEPCO",         "certain",  ""),
    ("13", "Tokyo",     "東京都",   "50", False, "TEPCO",         "certain",  ""),
    ("14", "Kanagawa",  "神奈川県", "50", False, "TEPCO",         "certain",  ""),
    ("15", "Niigata",   "新潟県",   "50", True,  "Tohoku EPCO",   "certain",  "Sado city ALL 60 Hz; parts of Myoko & Itoigawa 60 Hz"),
    ("16", "Toyama",    "富山県",   "60", False, "Hokuriku",      "certain",  ""),
    ("17", "Ishikawa",  "石川県",   "60", False, "Hokuriku",      "certain",  ""),
    ("18", "Fukui",     "福井県",   "60", False, "Hokuriku/Kansai","certain", "Tsuruga=Hokuriku, Wakasa=Kansai; both 60 Hz, no freq consequence"),
    ("19", "Yamanashi", "山梨県",   "50", False, "TEPCO",         "certain",  "NOT split. Fuji River rule does NOT apply here -- both banks 50 Hz."),
    ("20", "Nagano",    "長野県",   "60", True,  "Chubu",         "certain",  "60 Hz DOMINANT with 50 Hz hamlets in 9 municipalities. CONVERTED 50->60 by Mar 1961."),
    ("21", "Gifu",      "岐阜県",   "60", False, "Chubu",         "certain",  ""),
    ("22", "Shizuoka",  "静岡県",   "mixed", True, "TEPCO/Chubu", "certain",  "THE boundary. East of Fuji River=50, west=60."),
    ("23", "Aichi",     "愛知県",   "60", False, "Chubu",         "certain",  ""),
    ("24", "Mie",       "三重県",   "60", False, "Chubu/Kansai",  "certain",  ""),
    ("25", "Shiga",     "滋賀県",   "60", False, "Kansai",        "certain",  ""),
    ("26", "Kyoto",     "京都府",   "60", False, "Kansai",        "certain",  ""),
    ("27", "Osaka",     "大阪府",   "60", False, "Kansai",        "certain",  ""),
    ("28", "Hyogo",     "兵庫県",   "60", False, "Kansai/Chugoku","certain",  ""),
    ("29", "Nara",      "奈良県",   "60", False, "Kansai",        "certain",  ""),
    ("30", "Wakayama",  "和歌山県", "60", False, "Kansai",        "certain",  ""),
    ("31", "Tottori",   "鳥取県",   "60", False, "Chugoku",       "certain",  ""),
    ("32", "Shimane",   "島根県",   "60", False, "Chugoku",       "certain",  ""),
    ("33", "Okayama",   "岡山県",   "60", False, "Chugoku",       "certain",  ""),
    ("34", "Hiroshima", "広島県",   "60", False, "Chugoku",       "certain",  ""),
    ("35", "Yamaguchi", "山口県",   "60", False, "Chugoku",       "certain",  ""),
    ("36", "Tokushima", "徳島県",   "60", False, "Shikoku",       "certain",  ""),
    ("37", "Kagawa",    "香川県",   "60", False, "Shikoku",       "certain",  ""),
    ("38", "Ehime",     "愛媛県",   "60", False, "Shikoku",       "certain",  ""),
    ("39", "Kochi",     "高知県",   "60", False, "Shikoku",       "certain",  ""),
    ("40", "Fukuoka",   "福岡県",   "60", False, "Kyushu",        "certain",  "CONVERTED 50->60 EAST HALF 1949-1960"),
    ("41", "Saga",      "佐賀県",   "60", False, "Kyushu",        "certain",  ""),
    ("42", "Nagasaki",  "長崎県",   "60", False, "Kyushu",        "certain",  ""),
    ("43", "Kumamoto",  "熊本県",   "60", False, "Kyushu",        "certain",  "CONVERTED 50->60 Minamata area 1949-1960"),
    ("44", "Oita",      "大分県",   "60", False, "Kyushu",        "certain",  "CONVERTED 50->60 WHOLE PREFECTURE 1949-1960"),
    ("45", "Miyazaki",  "宮崎県",   "60", False, "Kyushu",        "certain",  "CONVERTED 50->60 WHOLE PREFECTURE 1949-1960"),
    ("46", "Kagoshima", "鹿児島県", "60", False, "Kyushu",        "certain",  "CONVERTED 50->60 EAST 1949-1960"),
    ("47", "Okinawa",   "沖縄県",   "60", False, "Okinawa EPCO",  "certain",  "NEVER converted. 1972 reversion was institutional only."),
]

# The five documented conversions. THIS is the research contribution.
# region, jis_codes, from_hz, to_hz, start, end, confidence, source_key, notes
CONVERSIONS = [
    ("Eastern Kyushu", "40;43;44;45;46", "50", "60", "1949-12", "1960-06", "confirmed",
     "kyushu1961",
     "Cabinet decision 1949-12-13. Ph1 1949-12 to 1951-06; interruption; Ph2 1954 to 1960-06. "
     "~590,000 kW of 50 Hz plant in 1949, cost ~JPY 11bn. Completed Jun 1960 (Onnabata #6, the 'shingari'). "
     "Whole of Oita and Miyazaki; east half of Fukuoka; east Kagoshima; Minamata (Kumamoto). "
     "WHOLE-PREFECTURE scale for Oita and Miyazaki -- usable with prefecture-level data."),
    ("Hokkaido west", "01", "60", "50", "1943-06", "1946", "confirmed",
     "ndl1024150",
     "Plan Dec 1942, began Jun 1943, completed 1946. Hakodate, Sapporo, Otaru, Shiribeshi, Tomakomai. "
     "Sapporo ran 60 cycles from 1900; Hakodate 60 Hz unbroken 1908-1942. "
     "ABSENT FROM WIKIPEDIA ENTIRELY. Confounded by the war years. "
     "No municipality-level timetable survives -- a ~3-year rolling transition, not a step."),
    ("Joban", "07;08", "60", "50", "1961-02", "1961-06", "confirmed",
     "nakagawa1985",
     "North Ibaraki (Mito, Hitachi) and south Fukushima Hamadori/Iwaki. Tohoku side by Feb 1961, "
     "TEPCO side Jun 1961. Mechanism: Hitachi Mining's Ishioka No.1 plant used a GE 1,000 kW 60 Hz "
     "generator (1910) -- an American-equipment island, the same pattern as Osaka."),
    ("Sado island", "15", "50", "60", "1954", "1954", "uncertain",
     "itami_note",
     "YEAR UNCERTAIN -- single source (a journalist's blog with sloppy era-year conversions); "
     "another agent reported 1950. The FACT of a 50->60 conversion is solid; the date is not. "
     "Sado is an ISLANDED grid, so 60 Hz is confounded with insularity (ageing, rural, access)."),
    ("Nagano (Chubu area)", "20", "50", "60", "", "1961-03", "strong",
     "kyushu1961",
     "By Mar 1961. Rests partly on a forum transcription of the Kyushu history volume, "
     "not independently confirmed."),
]


def main() -> None:
    REFERENCE.mkdir(parents=True, exist_ok=True)

    pref = pd.DataFrame(PREFECTURES, columns=[
        "jis_code", "prefecture_en", "prefecture_ja", "current_hz",
        "has_internal_split", "utility", "confidence", "notes",
    ])
    assert len(pref) == 47, len(pref)
    pref["gbd_location_id"] = pref.jis_code.astype(int) + 35423
    pref["ever_converted"] = pref.notes.str.contains("CONVERTED")

    conv = pd.DataFrame(CONVERSIONS, columns=[
        "region", "jis_codes", "from_hz", "to_hz",
        "start", "end", "confidence", "source_key", "notes",
    ])

    pref.to_csv(REFERENCE / "prefecture_frequency.csv", index=False)
    conv.to_csv(REFERENCE / "frequency_conversions.csv", index=False)

    print("Japan mains frequency reference")
    print("=" * 70)
    print(f"\nprefecture_frequency.csv  : {len(pref)} rows")
    print(f"frequency_conversions.csv : {len(conv)} rows\n")

    print("Current frequency:")
    for hz, n in pref.current_hz.value_counts().items():
        print(f"  {hz:>5} Hz : {n}")

    print(f"\nPrefectures with an internal split: "
          f"{', '.join(pref[pref.has_internal_split].prefecture_en)}")
    print(f"Prefectures EVER converted: "
          f"{', '.join(pref[pref.ever_converted].prefecture_en)}")

    print("\n" + "=" * 70)
    print("THE BOUNDARY MOVED -- five conversions, 1943-1961")
    print("=" * 70)
    for _, r in conv.iterrows():
        span = f"{r.start}..{r.end}" if r.start else f"..{r.end}"
        print(f"\n  {r.region:<22} {r.from_hz}->{r.to_hz} Hz  {span:<18} [{r.confidence}]")
        print(f"    JIS: {r.jis_codes}")

    print("\n" + "=" * 70)
    print("""IMPLICATION FOR ANY ANALYSIS

A static 50/60 assignment -- as used in the original chart -- is WRONG for
8 prefectures. Oita and Miyazaki were 50 Hz until roughly 1951-1960. Coding
them as "60 Hz" for a 1990-2021 dementia analysis assigns the wrong exposure
to everyone born before ~1960, i.e. precisely the cohort now developing
dementia.

Correctly handled, this is an OPPORTUNITY, not just an error: the conversions
give TIME-VARYING, prefecture-scale exposure running in BOTH directions
(Kyushu 50->60; Hokkaido and Joban 60->50). That permits a birth-cohort /
difference-in-differences design far stronger than the static spatial contrast
-- and Oita/Miyazaki operate at whole-prefecture scale, which is the only
granularity Japan's public dementia data actually offers.

BLOCKER: it still needs dementia x prefecture x AGE, which is not public.
See docs/03_japan_data_availability.md.""")


if __name__ == "__main__":
    main()
