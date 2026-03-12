#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import argparse

import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# --- Anchor sets (los que me confirmaste) ---
POS_ANCHORS = {
    "Huddling",
    "Run",
    "Enriched",
    "AfterNursing",
    "BeforeNursing",
}

NEG_ANCHORS = {
    "Castration",
    "Crushing",
    "Restrain",
    "LongIsolation",
    "ShortIsolation",
    "MissedNursing",
    "Fighting",
    "Barren",
}


def _canon_domain(s: str) -> str:
    """
    Map various domain spellings to the 3 main legend groups used in Figure 5.
    """
    s = str(s).strip().lower()

    # vocalizations
    if "vocal" in s:
        return "vocalization"

    # music
    if "music" in s:
        return "music"

    # challenge references (robusto a variantes)
    if ("challenge" in s) or ("challenger" in s) or ("control_negative" in s) or ("control-negative" in s):
        return "challenge_reference"

    # noise
    if "noise" in s:
        return "noise_reference"

    return s


def _pick_distance_cols(df: pd.DataFrame):
    """
    Accept either:
      - d_neg_euclid / d_pos_euclid
      - dNEG / dPOS
    Return (xcol_for_dNEG, ycol_for_dPOS).
    """
    if {"d_neg_euclid", "d_pos_euclid"}.issubset(df.columns):
        return "d_neg_euclid", "d_pos_euclid"
    if {"dNEG", "dPOS"}.issubset(df.columns):
        return "dNEG", "dPOS"
    raise ValueError(
        "No encuentro columnas de distancia. Esperaba (d_neg_euclid,d_pos_euclid) o (dNEG,dPOS). "
        f"Columnas: {list(df.columns)}"
    )


def load_main(main_csv: Path) -> pd.DataFrame:
    df = pd.read_csv(main_csv)

    # required minimal
    if "file" not in df.columns or "domain" not in df.columns:
        raise ValueError(f"El CSV main debe tener columnas 'file' y 'domain'. Columnas: {list(df.columns)}")

    xcol, ycol = _pick_distance_cols(df)

    df["file"] = df["file"].astype(str).str.strip()
    df["domain_raw"] = df["domain"].astype(str).str.strip()
    df["domain_canon"] = df["domain_raw"].map(_canon_domain)

    df[xcol] = pd.to_numeric(df[xcol], errors="coerce")
    df[ycol] = pd.to_numeric(df[ycol], errors="coerce")
    df = df.dropna(subset=[xcol, ycol]).copy()

    df = df.rename(columns={xcol: "dNEG", ycol: "dPOS"})
    return df


def load_noise(noise_csv: Path) -> pd.DataFrame:
    """
    CSV auxiliar para inset, con columnas:
      file, d_neg_euclid, d_pos_euclid   (o dNEG/dPOS)
    """
    df = pd.read_csv(noise_csv)
    if "file" not in df.columns:
        raise ValueError(f"noise_csv debe tener columna 'file'. Columnas: {list(df.columns)}")

    xcol, ycol = _pick_distance_cols(df)
    df["file"] = df["file"].astype(str).str.strip()
    df[xcol] = pd.to_numeric(df[xcol], errors="coerce")
    df[ycol] = pd.to_numeric(df[ycol], errors="coerce")
    df = df.dropna(subset=[xcol, ycol]).copy()
    df = df.rename(columns={xcol: "dNEG", ycol: "dPOS"})
    return df


def is_pos_anchor(fname: str) -> bool:
    # en tu Figure 5 los anchors vienen como archivos tipo "Huddling__SW__02.wav" etc.
    base = Path(str(fname)).stem
    # toma el token antes del primer separador
    ctx = base.split("__")[0].split("_SW_")[0]
    return ctx in POS_ANCHORS


def is_neg_anchor(fname: str) -> bool:
    base = Path(str(fname)).stem
    ctx = base.split("__")[0].split("_SW_")[0]
    return ctx in NEG_ANCHORS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--main_csv", default="data/Figure5_distances_main.csv")
    ap.add_argument("--noise_csv", default="data/Figure5_noise_inset_distances.csv")
    ap.add_argument("--out_png", default="figures_out/figure5_distance_plane.png")
    ap.add_argument("--out_tiff", default="figures_out/figure5_distance_plane.tiff")
    ap.add_argument("--dpi_png", type=int, default=300)
    ap.add_argument("--dpi_tiff", type=int, default=600)
    ap.add_argument("--label_key", action="store_true", help="Si lo activas, etiqueta W7_07.wav.")
    ap.add_argument("--label_noise", action="store_true", help="Si lo activas, etiqueta los nombres del ruido en el inset.")
    args = ap.parse_args()

    main_csv = Path(args.main_csv)
    noise_csv = Path(args.noise_csv)
    out_png = Path(args.out_png)
    out_tiff = Path(args.out_tiff)

    out_png.parent.mkdir(parents=True, exist_ok=True)

    df = load_main(main_csv)

    # Split domains
    voc = df[df["domain_canon"] == "vocalization"].copy()
    mus = df[df["domain_canon"] == "music"].copy()
    cha = df[df["domain_canon"] == "challenge_reference"].copy()

    # Split vocal anchors into POS/NEG sets (tu lógica)
    voc_pos = voc[voc["file"].map(is_pos_anchor)].copy()
    voc_neg = voc[voc["file"].map(is_neg_anchor)].copy()

    # Si hay vocalizaciones que no caen en ninguno (por nombres raros), no las graficamos
    # (si quieres, las podemos poner como "otros vocal" luego)

    # Noise for inset
    if noise_csv.exists():
        df_noise = load_noise(noise_csv)
        print(f"Noise rows loaded: {len(df_noise)} from {noise_csv}")
    else:
        df_noise = pd.DataFrame(columns=["file", "dNEG", "dPOS"])
        print(f"NOTE: noise_csv no encontrado: {noise_csv} (inset omitido)")

    fig, ax = plt.subplots(figsize=(9.5, 7.5))

    # Limits based on main only (music+challenge+vocal anchors) so inset doesn't crush scale
    main_stack = pd.concat([voc_pos, voc_neg, mus, cha], axis=0)
    x_min, x_max = float(main_stack["dNEG"].min()), float(main_stack["dNEG"].max())
    y_min, y_max = float(main_stack["dPOS"].min()), float(main_stack["dPOS"].max())
    pad_x = (x_max - x_min) * 0.08 if x_max > x_min else 0.5
    pad_y = (y_max - y_min) * 0.08 if y_max > y_min else 0.5

    ax.set_xlim(max(0.0, x_min - pad_x), x_max + pad_x)
    ax.set_ylim(max(0.0, y_min - pad_y), y_max + pad_y)

    # y=x line
    line_min = 0.0
    line_max = max(x_max + pad_x, y_max + pad_y)
    ax.plot([line_min, line_max], [line_min, line_max], linestyle="--", linewidth=1.8, alpha=0.7)

    handles, labels = [], []

    # Vocal NEG
    if len(voc_neg) > 0:
        h = ax.scatter(voc_neg["dNEG"], voc_neg["dPOS"], c="tab:red", marker="x", s=85, linewidths=2.2, label="Vocal anchors (NEG set)")
        handles.append(h); labels.append("Vocal anchors (NEG set)")

    # Vocal POS (mismo marcador, color más claro)
    if len(voc_pos) > 0:
        h = ax.scatter(voc_pos["dNEG"], voc_pos["dPOS"], c="#f4a3a3", marker="x", s=85, linewidths=2.2, label="Vocal anchors (POS set)")
        handles.append(h); labels.append("Vocal anchors (POS set)")

    # Music
    if len(mus) > 0:
        h = ax.scatter(mus["dNEG"], mus["dPOS"], c="tab:blue", marker="o", s=75, alpha=0.9, label="Functional music stimuli")
        handles.append(h); labels.append("Functional music stimuli")

    # Challenge
    if len(cha) > 0:
        h = ax.scatter(cha["dNEG"], cha["dPOS"], c="tab:orange", marker="s", s=75, alpha=0.9, label="Challenge reference stimuli")
        handles.append(h); labels.append("Challenge reference stimuli")

    # Optional key label
    if args.label_key:
        key = main_stack[main_stack["file"].astype(str).str.strip() == "W7_07.wav"]
        for _, r in key.iterrows():
            ax.annotate(r["file"], (r["dNEG"], r["dPOS"]), textcoords="offset points", xytext=(6, 6), fontsize=10)

    ax.set_xlabel("Distance to NEG vocal centroid (OAAS 3D)", fontsize=14)
    ax.set_ylabel("Distance to POS vocal centroid (OAAS 3D)", fontsize=14)
    ax.set_title("Figure 5 — OAAS centroid-distance plane (OAAS 3D)", fontsize=18, pad=12)

    # Inset: noise
    if len(df_noise) > 0:
        inset = ax.inset_axes([0.68, 0.11, 0.27, 0.27])  # [x0,y0,w,h]
        inset.scatter(df_noise["dNEG"], df_noise["dPOS"], c="tab:green", marker="^", s=95, alpha=0.9)

        nx_min, nx_max = float(df_noise["dNEG"].min()), float(df_noise["dNEG"].max())
        ny_min, ny_max = float(df_noise["dPOS"].min()), float(df_noise["dPOS"].max())
        nline_min = min(nx_min, ny_min)
        nline_max = max(nx_max, ny_max)
        inset.plot([nline_min, nline_max], [nline_min, nline_max], linestyle="--", linewidth=1.4, alpha=0.7)

        inset.set_title("Noise reference signals", fontsize=12, pad=6)
        inset.tick_params(labelsize=10)

        if args.label_noise:
            for _, r in df_noise.iterrows():
                inset.annotate(r["file"], (r["dNEG"], r["dPOS"]), textcoords="offset points", xytext=(5, 5), fontsize=9)

        # Dummy legend entry for inset
        dummy = ax.scatter([], [], c="tab:green", marker="^", s=95, label="Noise reference signals (inset)")
        handles.append(dummy); labels.append("Noise reference signals (inset)")

    # Legend (orden fijo)
    desired = [
        "Vocal anchors (NEG set)",
        "Vocal anchors (POS set)",
        "Functional music stimuli",
        "Challenge reference stimuli",
        "Noise reference signals (inset)",
    ]
    order = [labels.index(d) for d in desired if d in labels]
    ax.legend([handles[i] for i in order], [labels[i] for i in order], loc="upper left", frameon=True, fontsize=14)

    fig.tight_layout()
    fig.savefig(out_png, dpi=args.dpi_png)
    plt.close(fig)

    # TIFF (Pillow, uncompressed, Windows-safe)
    if out_tiff.exists() and out_tiff.stat().st_size == 0:
        out_tiff.unlink()

    with Image.open(out_png) as im:
        im = im.convert("RGB")
        im.save(out_tiff, format="TIFF", compression=None, dpi=(args.dpi_tiff, args.dpi_tiff))

    print(f"OK -> {out_png} ({out_png.stat().st_size} bytes)")
    print(f"OK -> {out_tiff} ({out_tiff.stat().st_size} bytes)")


if __name__ == "__main__":
    main()