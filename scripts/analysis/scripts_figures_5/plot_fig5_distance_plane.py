#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import argparse

import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def _canon_domain(s: str) -> str:
    s = str(s).strip().lower()
    if "challenge" in s:
        return "Challenge reference stimuli"
    if "vocal" in s:
        return "Vocalization anchors"
    if "music" in s:
        return "Functional music stimuli"
    if "noise" in s:
        return "Noise reference signals"
    return f"Other: {s}"


def load_main(main_csv: Path) -> pd.DataFrame:
    df = pd.read_csv(main_csv)

    required = {"file", "domain", "d_pos_euclid", "d_neg_euclid"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas {missing} en {main_csv}. Columnas: {list(df.columns)}")

    df["file"] = df["file"].astype(str).str.strip()
    df["domain_raw"] = df["domain"].astype(str).str.strip()
    df["domain"] = df["domain_raw"].map(_canon_domain)

    df["d_pos_euclid"] = pd.to_numeric(df["d_pos_euclid"], errors="coerce")
    df["d_neg_euclid"] = pd.to_numeric(df["d_neg_euclid"], errors="coerce")
    df = df.dropna(subset=["d_pos_euclid", "d_neg_euclid"]).copy()
    return df


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--main_csv", default="data/Figure5_distances_main.csv")
    ap.add_argument("--out_png", default="figures_out/figure5_distance_plane.png")
    ap.add_argument("--out_tiff", default="figures_out/figure5_distance_plane.tiff")
    ap.add_argument("--show_noise_inset", action="store_true", default=True)
    args = ap.parse_args()

    main_csv = Path(args.main_csv)
    out_png = Path(args.out_png)
    out_tiff = Path(args.out_tiff)

    out_png.parent.mkdir(parents=True, exist_ok=True)

    df = load_main(main_csv)

    # Split noise to inset
    df_noise = df[df["domain"] == "Noise reference signals"].copy()
    df_main = df[df["domain"] != "Noise reference signals"].copy()

    style = {
        "Vocalization anchors": dict(marker="x", s=85, linewidths=2.2),
        "Functional music stimuli": dict(marker="o", s=70),
        "Challenge reference stimuli": dict(marker="s", s=70),
    }
    colors = {
        "Vocalization anchors": "tab:red",
        "Functional music stimuli": "tab:blue",
        "Challenge reference stimuli": "tab:orange",
        "Noise reference signals": "tab:green",
    }

    fig, ax = plt.subplots(figsize=(9.5, 7.5))

    # limits based on main only
    x = df_main["d_neg_euclid"]
    y = df_main["d_pos_euclid"]
    x_min, x_max = float(x.min()), float(x.max())
    y_min, y_max = float(y.min()), float(y.max())
    pad_x = (x_max - x_min) * 0.08 if x_max > x_min else 0.5
    pad_y = (y_max - y_min) * 0.08 if y_max > y_min else 0.5

    ax.set_xlim(max(0.0, x_min - pad_x), x_max + pad_x)
    ax.set_ylim(max(0.0, y_min - pad_y), y_max + pad_y)

    # identity line y=x
    line_min = 0.0
    line_max = max(x_max + pad_x, y_max + pad_y)
    ax.plot([line_min, line_max], [line_min, line_max], linestyle="--", linewidth=1.6, alpha=0.7)

    handles, labels = [], []
    legend_order = ["Vocalization anchors", "Functional music stimuli", "Challenge reference stimuli"]

    for grp in legend_order:
        sub = df_main[df_main["domain"] == grp]
        if len(sub) == 0:
            continue
        sc = ax.scatter(
            sub["d_neg_euclid"],
            sub["d_pos_euclid"],
            c=colors[grp],
            label=grp,
            alpha=0.9,
            **style[grp],
        )
        handles.append(sc)
        labels.append(grp)

    ax.set_xlabel("Distance to NEG vocal centroid (OAAS 3D)", fontsize=14)
    ax.set_ylabel("Distance to POS vocal centroid (OAAS 3D)", fontsize=14)
    ax.set_title("Figure 5 — OAAS centroid-distance plane (OAAS 3D)", fontsize=18, pad=12)

    # inset for noise
    if args.show_noise_inset and len(df_noise) > 0:
        inset = ax.inset_axes([0.68, 0.11, 0.27, 0.27])  # [x0,y0,w,h]
        inset.scatter(
            df_noise["d_neg_euclid"],
            df_noise["d_pos_euclid"],
            c=colors["Noise reference signals"],
            marker="^",
            s=85,
            alpha=0.9,
        )

        nx_min, nx_max = float(df_noise["d_neg_euclid"].min()), float(df_noise["d_neg_euclid"].max())
        ny_min, ny_max = float(df_noise["d_pos_euclid"].min()), float(df_noise["d_pos_euclid"].max())
        nline_min = min(nx_min, ny_min)
        nline_max = max(nx_max, ny_max)
        inset.plot([nline_min, nline_max], [nline_min, nline_max], linestyle="--", linewidth=1.4, alpha=0.7)

        inset.set_title("Noise reference signals", fontsize=12, pad=6)
        inset.tick_params(labelsize=10)

        # legend dummy
        dummy = ax.scatter([], [], c=colors["Noise reference signals"], marker="^", s=85,
                           label="Noise reference signals (inset)")
        handles.append(dummy)
        labels.append("Noise reference signals (inset)")

    ax.legend(handles, labels, loc="upper left", frameon=True, fontsize=14)

    fig.tight_layout()
    fig.savefig(out_png, dpi=300)
    plt.close(fig)

    # TIFF (Pillow, uncompressed, Windows-safe)
    if out_tiff.exists() and out_tiff.stat().st_size == 0:
        out_tiff.unlink()

    with Image.open(out_png) as im:
        im = im.convert("RGB")
        im.save(out_tiff, format="TIFF", compression=None, dpi=(600, 600))

    print(f"OK -> {out_png} ({out_png.stat().st_size} bytes)")
    print(f"OK -> {out_tiff} ({out_tiff.stat().st_size} bytes)")


if __name__ == "__main__":
    main()