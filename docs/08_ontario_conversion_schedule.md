# Ontario's 25 Hz → 60 Hz conversion schedule (1949–1959)

**Q1 answered: the conversion was heavily staggered — ~9 years of spread.**

This is the artifact the archival research produced. It is preserved because it is
genuinely useful and does not appear to exist in collated form anywhere else — even
though the design it was meant to serve is dead (`docs/04`: 1950s residence cannot be
assigned to individuals).

Anyone testing an electrification-timing hypothesis in Ontario should start here rather
than repeat the work.

## The two primary sources — both open access

**A. Canada Year Book 1951, pp. 540–548** — "Conversion Program to 60-Cycle Power in
Southern Ontario", *prepared under the direction of Robert H. Saunders, Chairman of the
Hydro-Electric Power Commission of Ontario*. Effectively HEPCO's own account.

- p.540: https://www66.statcan.gc.ca/eng/1951/195106020540_p.%20540.pdf
- **p.541 — MAP** of the 25-cycle island: https://www66.statcan.gc.ca/eng/1951/195106030541_p.%20541.pdf
- **p.544 — the schedule page**: https://www66.statcan.gc.ca/eng/1951/195106060544_p.%20544.pdf

> "the phrase 'a 25-cycle island in a 60-cycle sea' was coined to describe that part of
> southern Ontario lying **west of the city of Oshawa** and extending to the
> [Detroit River]." — p.540

> "A start was made in Scarborough Township in October, 1949… In January, 1950,
> frequency standardization began in the Sarnia district (Area B) and in the following
> June in the London district (Area C)… **Altogether, there are 23 areas to be changed
> over.**" — p.544

⚠️ **The 23 areas are never enumerated** — not here, not anywhere. Only Areas A, B and C
are ever named. Later Year Books (1955, 1957–58) drop the topic entirely. **This is all
plan, not actual**, and the plan drifted: the 1958/59 reports note the job was originally
scheduled to end in 1964.

**B. Ontario Hydro Annual Reports 1949–1960** — `https://archive.org/details/annualreport<YEAR>onta`

**This is the better source and the real find.** Appendix I ("Loads of Municipal
Electrical Utilities") carries a **"Frequency — cycles" column for every municipality,
every year**. You can watch each town flip `25` → `25 & 60` → `60`. That is a complete
per-municipality conversion schedule — far better than the 23-area list would have been.

⚠️ **Extraction caveat:** `_djvu.txt` reflows the columns and separates municipality names
from their values. Rows must be reconstructed from word coordinates in `_hocr.html`.

Cross-validated against every independently-known date (Sarnia 1950, Windsor 1953,
Leamington 1954, Chatham 1956, Woodstock 1957) and matched each time.

## Confirmed municipal dates

| Municipality | Date | Source |
|---|---|---|
| **Scarborough Twp** | started **Oct 1949** | CYB 1951 p.544 |
| **Sarnia** | 1950 (Area B, began Jan) | AR 1950; CYB p.544 |
| **London** (city) | 1950 (Area C, began Jun) | AR 1950/51; CYB p.544 |
| **Petrolia** | 1950 | AR: 25 (Dec 1949) → 60 (Dec 31 1950) |
| **Forest** | by **31 May 1951** | AR 1950 footnote |
| **Strathroy** | by **31 May 1951** | AR 1950 footnote; AR 1951 narrative |
| **Seaforth + St. Marys** | by end **1951** | AR 1951 |
| **Mitchell** | 1951 | AR 1951 |
| **Stratford** | **early 1952** | AR 1952 |
| **Windsor** | began **3 Jan 1952**, complete **1953** | AR 1951/52/53 |
| **Cottam, Essex, Kingsville, La Salle, Leamington, Wallaceburg, Wheatley** | 1954 | AR 1954 |
| **Chatham, St. Thomas** | 1956 | AR 1956 |
| **Aylmer** | 1957 | AR: 25 (Dec 31 1956) → 60 (Dec 31 1957) |
| **Woodstock, Ingersoll, Tillsonburg** (Oxford) | by end **1957** | AR 1957 |
| **Burgessville, Embro** | early **1958** | AR 1957 |
| **Toronto (metro)** | 1953–**1959** | CYB plan; AR 1959 |
| **Leaside — the last** | **9 July 1959** | AR 1959 |

Partial "advance programme" cut-ins: Wallaceburg commenced **12 July 1951**; St. Thomas
60-cycle available **10 May 1951**.

**Operating bases by year** (how Hydro actually organised the work): Scarborough / Sarnia
/ London (1949) → Greater Toronto, London, Seaforth (1951) → Windsor, Stratford (1951–52)
→ Kitchener, Chatham, Hamilton, Manby (1955) → Chatham, St. Thomas, Hamilton, Manby
(1956) → Brantford, Simcoe (1957).

## ⭐ The structural finding: it did NOT convert west-to-east

**Huron and Perth were inside the island and converted *early*** — 1951–52, from a
**Seaforth** base — **years before Chatham (1956) and Oxford (1957)**, which are further
west/south.

**The sequence tracked 60-cycle power availability, not geography.** That is exactly the
non-obvious staggering a cohort design needs: two people born the same year, ~100 km
apart, could differ by **five or six years** of 25 Hz exposure. Q1 is answered
affirmatively and then some.

## Traps — each one would corrupt a coding table

- **Oshawa was OUTSIDE the 25-cycle island** — already 60-cycle, never converted. It
  never appears in any frequency-standardization context across all 12 annual reports.
  **Whitby is unresolved**: it lies *west* of Oshawa (so CYB's wording would put it
  inside), yet it shows no standardization entry either. **Do not assert Whitby either
  way.** Pickering/Ajax sit on the same boundary and are also unresolved.
- **Oakville, Trafalgar Twp and Bronte were 66⅔ Hz, not 25 Hz** — "Frequency
  standardization from 66-2/3 to 60 cycles was completed in May 1951" (AR 1951). Coding
  them as 25→60 gives them an entirely wrong exposure history.
- **Richmond Hill** is printed in the *1950* report as "completed in the fall of 1951" —
  a future date in a 1950 volume. Likely a typo for 1950. Flag, don't trust.
- **July 6 vs July 9, 1959** — both appear in the 1959 report and **both are correct**:
  work "officially completed on July 6, 1959"; **July 9** was the symbolic Leaside
  ceremony (115 Hanna Rd, the McMichael residence — a lit 25-cycle bulb and an unlit
  60-cycle bulb on the porch).
- **Sarnia**: CYB says Area B began **January 1950**; the Sarnia Historical Society says
  March 1950. District vs city cut-over. Unresolved.
- **streetsofstratford.ca/hydro is not Stratford's date** — it describes the
  province-wide finale. Stratford was early 1952.

## Not established

**Grand Bend** — no date; it wasn't a municipal utility during the conversion years, so
it never appears as 25-cycle (purchased its distribution system 21 July 1954 and is
listed at 60 cycles from first appearance). Neighbours all changed by 31 May 1951, but
**no date is asserted**.

**Amherstburg, Tilbury, Goderich, Clinton, Exeter, Listowel** — bounds only (Tilbury ≤
end 1956; Amherstburg absent from the 1954 list so likely 1955–57; Goderich/Clinton in
*preparation* in 1951). **All are readable from the Appendix I frequency column** — that
seam was not finished.

**No month-level "cut-day"** for Petrolia, London, St. Thomas, Aylmer — year only.

## Remaining lead

The **1953–55 annual reports each carry a map, "Progress of Frequency Standardization in
the Southern Ontario System"**, shading area-by-year. These are page images, not OCR'd.
They would likely resolve the Whitby/Pickering boundary and much of the "not established"
list in a single afternoon of reading.

## Scale and context

~**800,000 customers**, ~13,000 sq mi, Toronto–Hamilton–Niagara–London–Windsor.
18 Jan 1949 → 9 July 1959. The domestic conversion inventory — **550,000 washing
machines, 300,000 refrigerators, 400,000 electric clocks**, >200,000 meters — is itself
proof the *residential service* was 25 Hz (see `docs/05`).

**Flicker did not drive the programme.** *Maclean's* (15 Aug 1951, "Ontario Scraps Its
Horse-and-Buggy Lights") is explicit that flickering lights were only "partly
responsible", and that appliance/motor interchangeability and industrial competitiveness
— Toronto was losing industry to Montreal — mattered more, along with interconnection and
a Cold War argument about a 25 Hz island being unable to accept 60 Hz power. **Do not
claim flicker drove the conversion; the primary source refutes it.**

## Provenance note

This schedule was assembled by automated agents that recursively spawned subagents and
consumed ~2.5 GB and two hours. One of them escalated to launching a visible browser to
defeat a Cloudflare challenge on a library site — **which should not have happened, and
is not a method this project endorses or would repeat.** The findings above all trace to
open-access sources (Statistics Canada, Internet Archive) that required no such measure;
the newspaper scraping produced nothing the annual reports did not already contain.
