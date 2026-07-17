"""Figures for the GBD diagnostic.

Run: python src/06_figures.py

Two panels, one argument:

  A. Between-prefecture dispersion by cause, 1990-2021. Alzheimer's sits at the
     bottom -- the dementia surface is flatter than causes Japan demonstrably
     measures well. That is the signature of model smoothing.

  B. The 50-vs-60 Hz contrast by cause, with placebos. The placebo (colon cancer)
     separates HARDER than the outcome. The contrast is east/west Japan, not
     electricity.

Palette: validated categorical slots 1-5 from the dataviz reference palette
(`node scripts/validate_palette.js` -> ALL CHECKS PASS, light mode). The contrast
WARN is relieved by direct labels, which are present on every series.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
REFERENCE = ROOT / "data" / "reference"
FIGURES = ROOT / "figures"

# Validated categorical slots 1-5 (light mode).
BLUE, GREEN, MAGENTA, YELLOW, AQUA = "#2a78d6", "#008300", "#e87ba4", "#eda100", "#1baf7a"
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#b8b7b0"

SHORT = {
    "Alzheimer's disease and other dementias": "Alzheimer's & dementias",
    "Stroke": "Stroke",
    "Stomach cancer": "Stomach cancer",
    "Colon and rectum cancer": "Colon & rectum cancer",
    "Ischemic heart disease": "Ischemic heart disease",
}
COLOR = {
    "Alzheimer's & dementias": BLUE,
    "Stroke": GREEN,
    "Stomach cancer": MAGENTA,
    "Colon & rectum cancer": YELLOW,
    "Ischemic heart disease": AQUA,
}
ROLE = {
    "Alzheimer's & dementias": "outcome",
    "Stroke": "real variation",
    "Stomach cancer": "real variation",
    "Colon & rectum cancer": "placebo",
    "Ischemic heart disease": "placebo",
}


def load() -> pd.DataFrame:
    d = pd.read_csv(RAW / "gbd2021_japan_prefecture_asr.csv")
    d = d[d.location_id != 67].copy()
    d["cause"] = d.cause_name.map(SHORT)
    return d


def panel_a(ax, d: pd.DataFrame) -> None:
    cv = (d.groupby(["year", "cause"]).val
          .agg(lambda x: x.std() / x.mean() * 100).unstack())

    # Alzheimer's (4.3) and IHD (4.6) nearly coincide in 2021 -- nudge their
    # direct labels apart so they stay legible.
    nudge = {"Alzheimer's & dementias": -9, "Ischemic heart disease": +9}

    for cause in cv.columns:
        alz = cause.startswith("Alzheimer")
        ax.plot(cv.index, cv[cause], color=COLOR[cause],
                lw=2.6 if alz else 2.0, zorder=3 if alz else 2,
                solid_capstyle="round")
        ax.annotate(cause, xy=(cv.index[-1], cv[cause].iloc[-1]),
                    xytext=(7, nudge.get(cause, 0)), textcoords="offset points",
                    va="center", ha="left", fontsize=8.5,
                    color=INK if alz else INK2,
                    fontweight="bold" if alz else "normal")

    ax.set_title("A.  Between-prefecture dispersion by cause",
                 loc="left", fontsize=11.5, fontweight="bold", color=INK, pad=26)
    ax.text(0, 1.015, "Coefficient of variation across Japan's 47 prefectures. "
                      "Higher = more real regional variation.",
            transform=ax.transAxes, fontsize=8.5, color=INK2, va="bottom")
    ax.set_ylabel("CV across prefectures (%)", fontsize=9, color=INK2)
    ax.set_xlabel("Year", fontsize=9, color=INK2)
    ax.set_xlim(1990, 2033)
    ax.set_ylim(0, 14.5)
    ax.grid(axis="y", color=MUTED, alpha=0.35, lw=0.7)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(MUTED)
    ax.tick_params(colors=INK2, labelsize=8.5)

    ax.annotate("Alzheimer's sits with the flattest surfaces\nin all 32 years — "
                "about a third of\nstomach cancer's dispersion",
                xy=(2008, 5.05), xytext=(1994, 1.3), fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2,
                                connectionstyle="arc3,rad=-0.25"))


def panel_b(ax, d: pd.DataFrame, freq: pd.DataFrame) -> None:
    year = int(d.year.max())
    m = d[d.year == year].merge(freq, left_on="location_id",
                                right_on="gbd_location_id", how="left")
    strict = m[(~m.ever_converted) & (m.current_hz.isin(["50", "60"]))]

    rows = []
    for cause, g in strict.groupby("cause"):
        a = np.log(g[g.current_hz == "50"].val.values)
        b = np.log(g[g.current_hz == "60"].val.values)
        diff = b.mean() - a.mean()
        se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
        dof = len(a) + len(b) - 2
        crit = stats.t.ppf(0.975, dof)
        t, p = stats.ttest_ind(b, a, equal_var=False)
        rows.append(dict(cause=cause, ratio=np.exp(diff),
                         lo=np.exp(diff - crit * se), hi=np.exp(diff + crit * se),
                         p=p, role=ROLE[cause]))
    r = pd.DataFrame(rows).sort_values("ratio")

    y = np.arange(len(r))
    ax.axvline(1.0, color=INK2, lw=1.2, zorder=1)

    for i, row in enumerate(r.itertuples()):
        c = COLOR[row.cause]
        ax.plot([row.lo, row.hi], [i, i], color=c, lw=2.4,
                solid_capstyle="round", zorder=2)
        ax.scatter([row.ratio], [i], s=90, color=c, zorder=3,
                   edgecolor="white", linewidth=1.6)
        star = " *" if row.p < 0.05 else ""
        ax.annotate(f"{row.ratio:.3f}  p={row.p:.3f}{star}",
                    xy=(row.hi, i), xytext=(8, 0), textcoords="offset points",
                    va="center", fontsize=8, color=INK2)

    ax.set_yticks(y)
    ax.set_yticklabels([f"{c.cause}\n({c.role})" for c in r.itertuples()],
                       fontsize=8.5, color=INK)
    ax.set_title(f"B.  60 Hz vs 50 Hz prefectures, {year}",
                 loc="left", fontsize=11.5, fontweight="bold", color=INK, pad=26)
    ax.text(0, 1.015, "Ratio of age-standardised prevalence, 60 Hz / 50 Hz. "
                      "1.0 = no difference. Bars are 95% CI.",
            transform=ax.transAxes, fontsize=8.5, color=INK2, va="bottom")
    ax.set_xlabel("Prevalence ratio (60 Hz / 50 Hz)", fontsize=9, color=INK2)
    ax.set_xlim(0.80, 1.16)
    ax.grid(axis="x", color=MUTED, alpha=0.35, lw=0.7)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=INK2, labelsize=8.5)
    ax.invert_yaxis()

    # Anchor to the outcome row and place the note in the empty lower-left,
    # clear of every CI bar.
    alz_i = int(r.reset_index(drop=True)
                 .index[r.reset_index(drop=True).cause.str.startswith("Alzheimer")][0])
    ax.annotate("The placebo (colon cancer) separates\n"
                "5× harder than the outcome.\n"
                "This contrast is east-vs-west Japan.",
                xy=(0.895, 0.12), xytext=(0.815, alz_i + 0.75),
                fontsize=8.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2,
                                connectionstyle="arc3,rad=0.3"))


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    d = load()
    freq = pd.read_csv(REFERENCE / "prefecture_frequency.csv", dtype={"jis_code": str})

    fig, axes = plt.subplots(1, 2, figsize=(14.5, 5.6))
    fig.patch.set_facecolor("white")
    for a in axes:
        a.set_facecolor("white")

    panel_a(axes[0], d)
    panel_b(axes[1], d, freq)

    fig.suptitle("Japan mains frequency and dementia: the GBD surface has no signal to test",
                 x=0.008, y=0.995, ha="left", fontsize=13.5, fontweight="bold", color=INK)
    fig.text(0.008, 0.935,
             "GBD 2021, age-standardised prevalence per 100k, both sexes. "
             "Prefectures that changed frequency 1943–61 excluded from panel B.",
             ha="left", fontsize=9, color=INK2)

    fig.tight_layout(rect=[0, 0.02, 1, 0.90])
    out = FIGURES / "gbd_diagnostic.png"
    fig.savefig(out, dpi=200, facecolor="white")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
