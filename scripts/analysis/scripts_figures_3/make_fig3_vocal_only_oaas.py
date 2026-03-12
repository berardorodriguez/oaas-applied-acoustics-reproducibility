#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# Grupos tal como aparecen en la Figura 3
POS_ANCHOR = {
    "AfterNursing",
    "ShortReunion",
    "Huddling",
    "PositiveConditioning",
    "Enriched",
}

NEG_ANCHOR = {
    "Castration",
    "Restrain",
    "Crushing",
    "Fighting",
    "LongIsolation",
    "ShortIsolation",
    "NegativeConditioning",
}


def assign_group(ctx: str) -> str:
    ctx = str(ctx).strip()
    if ctx in NEG_ANCHOR:
        return "NEG-anchor set"
    if ctx in POS_ANCHOR:
        return "POS-anchor set"
    return "Non-anchor"


def main():
    in_csv = Path("data/Table_S5_vocal_only_OAAS_bias_by_context.csv")
    out_dir = Path("figures_out")
    out_png = out_dir / "figure3_vocal_only_oaas.png"
    out_tiff = out_dir / "figure3_vocal_only_oaas.tiff"

    df = pd.read_csv(in_csv)

    required = {"context", "vOAAS1", "vOAAS2"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(
            f"Faltan columnas {missing} en {in_csv}. Columnas: {list(df.columns)}"
        )

    df["context"] = df["context"].astype(str).str.strip()
    df["group"] = df["context"].map(assign_group)

    # Dibujar Non-anchor primero, luego anchors encima
    zorder_map = {"Non-anchor": 0, "NEG-anchor set": 1, "POS-anchor set": 2}
    df = df.sort_values("group", key=lambda s: s.map(zorder_map))

    fig, ax = plt.subplots(figsize=(12, 8))

    for grp, sub in df.groupby("group", sort=False):
        ax.scatter(sub["vOAAS1"], sub["vOAAS2"], label=grp, s=90)
        for _, r in sub.iterrows():
            ax.text(r["vOAAS1"], r["vOAAS2"], r["context"], fontsize=11)

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlabel("vOAAS1", fontsize=14)
    ax.set_ylabel("vOAAS2", fontsize=14)
    ax.set_title(
        "Vocal-only OAAS (PCA fit on SoundWel vocalization ensembles) — context centroids",
        fontsize=18,
        pad=14,
    )

    # Leyenda con orden fijo
    handles, labels = ax.get_legend_handles_labels()
    desired = ["NEG-anchor set", "Non-anchor", "POS-anchor set"]
    legend_order = [labels.index(d) for d in desired if d in labels]
    ax.legend(
        [handles[i] for i in legend_order],
        [labels[i] for i in legend_order],
        loc="upper left",
        frameon=True,
        fontsize=14,
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()

    # Guardar PNG con Matplotlib
    fig.savefig(out_png, dpi=300)
    plt.close(fig)

    # Guardar TIFF con Pillow (SIN compresión) — esto ya te funcionó en test_uncompressed.tif
    if out_tiff.exists() and out_tiff.stat().st_size == 0:
        out_tiff.unlink()

    with Image.open(out_png) as im:
        im = im.convert("RGB")
        im.save(out_tiff, format="TIFF", compression=None, dpi=(600, 600))

    print(f"OK -> {out_png} ({out_png.stat().st_size} bytes)")
    print(f"OK -> {out_tiff} ({out_tiff.stat().st_size} bytes)")


if __name__ == "__main__":
    main()