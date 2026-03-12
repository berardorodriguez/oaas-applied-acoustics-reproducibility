from __future__ import annotations

import argparse
from pathlib import Path
import re

import pandas as pd
import matplotlib.pyplot as plt


# -------------------------
# Grouping (robust)
# -------------------------
def classify_4groups(file_id: str, domain: str | None) -> str:
    f = (file_id or "").strip()
    d = (domain or "").strip().lower()

    # 1) Vocalization anchors (SoundWel)
    if any(tok in d for tok in ["vocal", "soundwel", "anchor"]):
        return "Vocalization anchors (SoundWel)"

    # 2) Noise reference signals
    # domain labels like: noise, noise_reference, noise-reference
    # filename patterns: brown_noise / pink_noise / white_noise
    if ("noise" in d) or re.search(r"(brown|pink|white)_noise", f, flags=re.IGNORECASE):
        return "Noise reference signals"

    # 3) Challenge reference stimuli (challengers / negative controls)
    # domain labels + filename patterns (Challenger_* or Negative_*)
    if any(tok in d for tok in ["chall", "challenge", "control", "negative"]):
        return "Challenge reference stimuli"

    if re.search(r"(?i)\bchallenger\b", f) or re.match(r"(?i)^challenger[_\-]", f):
        return "Challenge reference stimuli"

    # IMPORTANT: capture your "Negative_01.wav", "Negative_02_part1.wav", etc.
    if re.match(r"(?i)^nega?ti?ve[_\-\s]*\d+", f) or re.search(r"(?i)\bnegative\b", f):
        return "Challenge reference stimuli"

    # 4) Functional music stimuli (W1_01.wav, etc.)
    if ("music" in d) or re.match(r"(?i)^w\d+_\d+(\.wav)?$", f):
        return "Functional music stimuli"

    return "Other/Unclassified"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--projected",
        required=True,
        help="CSV with OAAS1/OAAS2/OAAS3 + file + domain "
             "(use: data/OAAS_master_projected_with_noise_reference.csv)",
    )
    ap.add_argument("--out_dir", required=True, help="Output directory (e.g., figures)")
    ap.add_argument("--out_name", default="Figure_2.png", help="Output filename (default: Figure_2.png)")
    ap.add_argument("--include_other", action="store_true", help="If set, plot Other/Unclassified as gray x")
    args = ap.parse_args()

    projected_path = Path(args.projected)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(projected_path)

    # Required columns
    id_col = "file"
    domain_col = "domain"
    xcol, y2col, y3col = "OAAS1", "OAAS2", "OAAS3"

    for col in [id_col, xcol, y2col, y3col]:
        if col not in df.columns:
            raise ValueError(f"Missing required column '{col}'. Columns found: {list(df.columns)}")

    if domain_col not in df.columns:
        df[domain_col] = ""

    df["group4"] = [
        classify_4groups(str(f), str(d))
        for f, d in zip(df[id_col].astype(str), df[domain_col].astype(str))
    ]

    # Diagnostics
    print("=== domain counts ===")
    print(df[domain_col].value_counts(dropna=False))
    print("\n=== group4 counts ===")
    print(df["group4"].value_counts(dropna=False))

    # --- Styling (stable & journal-friendly) ---
    style = {
        "Challenge reference stimuli": dict(marker="s", s=55, linewidths=0.5, edgecolors="black"),
        "Functional music stimuli": dict(marker="o", s=55, linewidths=0.5, edgecolors="black"),
        "Noise reference signals": dict(marker="^", s=70, linewidths=0.8, edgecolors="black"),
        "Vocalization anchors (SoundWel)": dict(marker="x", s=70, linewidths=1.8),
        "Other/Unclassified": dict(marker="x", s=70, linewidths=1.4),
    }

    colors = {
        "Challenge reference stimuli": "tab:blue",
        "Functional music stimuli": "tab:orange",
        "Noise reference signals": "tab:green",
        "Vocalization anchors (SoundWel)": "tab:red",
        "Other/Unclassified": "0.5",
    }

    order = [
        "Challenge reference stimuli",
        "Functional music stimuli",
        "Noise reference signals",
        "Vocalization anchors (SoundWel)",
    ]
    if args.include_other:
        order.append("Other/Unclassified")

    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.2), dpi=150)

    # Left: OAAS1 vs OAAS2
    ax = axes[0]
    ax.set_title("OAAS overlay: OAAS1 vs OAAS2")
    ax.set_xlabel("OAAS1 (PC1)")
    ax.set_ylabel("OAAS2 (PC2)")
    ax.grid(True, alpha=0.25)

    handles, labels = [], []
    for g in order:
        sub = df[df["group4"] == g]
        if sub.empty:
            continue
        sc = ax.scatter(sub[xcol], sub[y2col], c=colors[g], label=g, **style[g])
        handles.append(sc)
        labels.append(g)

    ax.legend(handles, labels, loc="upper right", frameon=True)

    # Right: OAAS1 vs OAAS3
    ax = axes[1]
    ax.set_title("OAAS overlay: OAAS1 vs OAAS3")
    ax.set_xlabel("OAAS1 (PC1)")
    ax.set_ylabel("OAAS3 (PC3)")
    ax.grid(True, alpha=0.25)

    handles, labels = [], []
    for g in order:
        sub = df[df["group4"] == g]
        if sub.empty:
            continue
        sc = ax.scatter(sub[xcol], sub[y3col], c=colors[g], label=g, **style[g])
        handles.append(sc)
        labels.append(g)

    ax.legend(handles, labels, loc="upper right", frameon=True)

    fig.tight_layout()

    # --- outputs ---
    out_png = out_dir / args.out_name
    # create a matching TIFF name
    out_tif = out_png.with_suffix(".tif")

    fig.savefig(out_png, dpi=300, bbox_inches="tight")
    fig.savefig(out_tif, dpi=600, bbox_inches="tight")
    plt.close(fig)

    print(f"\nSaved: {out_png}")
    print(f"Saved: {out_tif}")


if __name__ == "__main__":
    main()