from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# ==========================================
# Panel D — W7_01 only (clean stable v3)
# ==========================================

mpl.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
})


def find_col_contains(columns, tokens):
    for c in columns:
        cl = c.lower()
        if any(t.lower() in cl for t in tokens):
            return c
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--stem", default="W7_01")
    args = parser.parse_args()

    log_path = Path(args.log)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(log_path)

    # Detect columns robustly
    text_col = find_col_contains(df.columns, ["label", "stim", "name", "id"])
    if text_col is None:
        text_col = df.columns[0]  # fallback

    xcol = find_col_contains(df.columns, ["oaas1", "pc1"])
    ycol = find_col_contains(df.columns, ["oaas3", "pc3"])

    if xcol is None or ycol is None:
        raise ValueError(f"No pude detectar columnas OAAS1/PC1 y OAAS3/PC3. Columnas: {df.columns}")

    s = df[text_col].astype(str)

    row_original = df[s.str.contains("original", case=False)].iloc[0]
    row_pos = df[s.str.contains("pos", case=False)].iloc[0]
    row_neg = df[s.str.contains("neg", case=False)].iloc[0]

    x0, y0 = float(row_original[xcol]), float(row_original[ycol])
    x_pos, y_pos = float(row_pos[xcol]), float(row_pos[ycol])
    x_neg, y_neg = float(row_neg[xcol]), float(row_neg[ycol])

    orig_name = str(row_original[text_col])
    pos_name = str(row_pos[text_col])
    neg_name = str(row_neg[text_col])

    # ===============================
    # Plot
    # ===============================
    fig, ax = plt.subplots(figsize=(4.0, 3.6))
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.18)

    # Arrows
    ax.annotate("", xy=(x_pos, y_pos), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", linewidth=2.2))
    ax.annotate("", xy=(x_neg, y_neg), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", linewidth=2.2))

    # Points
    h0 = ax.scatter(x0, y0, s=80, edgecolor="black", linewidth=0.5, zorder=3)
    h1 = ax.scatter(x_pos, y_pos, s=110, marker="^",
                    edgecolor="black", linewidth=0.5, zorder=3)
    h2 = ax.scatter(x_neg, y_neg, s=110, marker="s",
                    edgecolor="black", linewidth=0.5, zorder=3)

    ax.set_xlabel("OAAS1 (PC1)")
    ax.set_ylabel("OAAS3 (PC3)")
    ax.set_title(args.stem)

    ax.legend(
        [h0, h1, h2],
        ["Original", f"POS ({pos_name})", f"NEG ({neg_name})"],
        loc="lower right",
        frameon=False,
        fontsize=8,
        handlelength=1.2,
        handletextpad=0.5
    )

    ax.margins(x=0.15, y=0.15)
    plt.tight_layout()

    png_path = outdir / f"Fig4_panelD_vectors_PC1_PC3_{args.stem}.png"
    tif_path = outdir / f"Fig4_panelD_vectors_PC1_PC3_{args.stem}.tiff"

    fig.savefig(png_path, dpi=300, bbox_inches="tight", pad_inches=0.02)
    fig.savefig(tif_path, dpi=600, bbox_inches="tight", pad_inches=0.02)

    plt.close(fig)

    print(f"Saved: {png_path}")
    print(f"Saved: {tif_path}")


if __name__ == "__main__":
    main()
