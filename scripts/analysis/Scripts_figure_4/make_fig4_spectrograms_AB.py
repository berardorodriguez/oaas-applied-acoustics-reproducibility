#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

try:
    import soundfile as sf
except Exception as e:
    raise SystemExit("Missing dependency: soundfile. Install with: pip install soundfile") from e

try:
    import librosa
    import librosa.display
except Exception as e:
    raise SystemExit("Missing dependency: librosa. Install with: pip install librosa") from e


def load_mono(path: Path):
    y, sr = sf.read(str(path), always_2d=False)
    if y.ndim == 2:
        y = y.mean(axis=1)
    y = y.astype(np.float32)
    return y, int(sr)


def mel_db(y: np.ndarray, sr: int, n_fft: int, hop: int, n_mels: int, fmax: float):
    S = librosa.feature.melspectrogram(
        y=y, sr=sr, n_fft=n_fft, hop_length=hop, n_mels=n_mels,
        fmin=0.0, fmax=fmax, power=2.0
    )
    # Convert to dB using a consistent reference per stimulus (set later)
    return S


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def plot_mels_triplet(So_db, Sp_db, Sn_db, sr, hop, fmax, out_png: Path, title: str,
                      vmin=-80, vmax=0):
    fig = plt.figure(figsize=(11.2, 3.4))
    gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 0.05], wspace=0.12)

    axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[0, 2])]
    cax = fig.add_subplot(gs[0, 3])

    imgs = []
    for ax, Sdb, lab in zip(axes, [So_db, Sp_db, Sn_db], ["Original", "POS", "NEG"]):
        img = librosa.display.specshow(
            Sdb, sr=sr, hop_length=hop, x_axis=None, y_axis="mel",
            fmax=fmax, ax=ax, vmin=vmin, vmax=vmax
        )
        ax.set_title(lab, fontsize=10)
        ax.set_xlabel("")
        ax.set_ylabel("")
        imgs.append(img)

    # Leftmost keeps y ticks; others hide
    axes[1].set_yticks([])
    axes[2].set_yticks([])

    cb = fig.colorbar(imgs[0], cax=cax)
    cb.set_label("dB", rotation=90)

    fig.suptitle(title, y=0.98, fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.subplots_adjust(top=0.88)
    fig.savefig(out_png, dpi=300)
    plt.close(fig)


def plot_deltas(Sp_db, Sn_db, So_db, sr, hop, fmax, out_png: Path, title: str,
                delta_lim=6.0):
    dpos = Sp_db - So_db
    dneg = Sn_db - So_db

    fig = plt.figure(figsize=(7.6, 3.4))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 0.06], wspace=0.15)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    cax = fig.add_subplot(gs[0, 2])

    img1 = librosa.display.specshow(
        dpos, sr=sr, hop_length=hop, y_axis="mel", fmax=fmax,
        ax=ax1, vmin=-delta_lim, vmax=delta_lim
    )
    img2 = librosa.display.specshow(
        dneg, sr=sr, hop_length=hop, y_axis="mel", fmax=fmax,
        ax=ax2, vmin=-delta_lim, vmax=delta_lim
    )

    ax1.set_title("ΔPOS (POS − Original)", fontsize=10)
    ax2.set_title("ΔNEG (NEG − Original)", fontsize=10)

    ax2.set_yticks([])

    cb = fig.colorbar(img1, cax=cax)
    cb.set_label("Δ dB", rotation=90)

    fig.suptitle(title, y=0.98, fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(out_png, dpi=300)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True, help="Root folder containing W7_01/ and W8_03/ with wavs.")
    ap.add_argument("--outdir", type=Path, required=True, help="Output directory for PNGs.")
    ap.add_argument("--fmax", type=float, default=8000.0)
    ap.add_argument("--n_mels", type=int, default=128)
    ap.add_argument("--n_fft", type=int, default=2048)
    ap.add_argument("--hop", type=int, default=512)
    ap.add_argument("--mel_vmin", type=float, default=-80.0)
    ap.add_argument("--mel_vmax", type=float, default=0.0)
    ap.add_argument("--delta_lim", type=float, default=6.0)
    args = ap.parse_args()

    ensure_dir(args.outdir)

    stims = ["W7_01", "W8_03"]
    for stim in stims:
        folder = args.root / stim
        if not folder.exists():
            raise SystemExit(f"Missing stimulus folder: {folder}")

        p_orig = next(folder.glob(f"{stim}_original_30s.wav"), None)
        p_pos  = next(folder.glob(f"{stim}_POS_30s.wav"), None)
        p_neg  = next(folder.glob(f"{stim}_NEG_30s.wav"), None)

        if not (p_orig and p_pos and p_neg):
            raise SystemExit(f"Missing one of the WAVs in {folder}. Expected *_original_30s.wav, *_POS_30s.wav, *_NEG_30s.wav")

        y0, sr0 = load_mono(p_orig)
        yp, srp = load_mono(p_pos)
        yn, srn = load_mono(p_neg)

        if not (sr0 == srp == srn):
            raise SystemExit(f"Sample rate mismatch in {stim}: {sr0}, {srp}, {srn}")

        # Compute mel power
        S0 = mel_db(y0, sr0, args.n_fft, args.hop, args.n_mels, args.fmax)
        Sp = mel_db(yp, sr0, args.n_fft, args.hop, args.n_mels, args.fmax)
        Sn = mel_db(yn, sr0, args.n_fft, args.hop, args.n_mels, args.fmax)

        # Convert to dB with a CONSISTENT reference per stimulus:
        # Use max of ORIGINAL mel power as reference so all three share the same scale.
        ref = float(np.max(S0))
        S0_db = librosa.power_to_db(S0, ref=ref)
        Sp_db = librosa.power_to_db(Sp, ref=ref)
        Sn_db = librosa.power_to_db(Sn, ref=ref)

        out_mels = args.outdir / f"Fig4_mels_{stim}.png"
        out_dlt  = args.outdir / f"Fig4_deltas_{stim}.png"

        plot_mels_triplet(
            S0_db, Sp_db, Sn_db, sr0, args.hop, args.fmax, out_mels,
            title=f"{stim} — Mel-spectrograms (30 s, 48 kHz)",
            vmin=args.mel_vmin, vmax=args.mel_vmax
        )
        plot_deltas(
            Sp_db, Sn_db, S0_db, sr0, args.hop, args.fmax, out_dlt,
            title=f"{stim} — Δ Mel-spectrograms (relative to Original)",
            delta_lim=args.delta_lim
        )

        print("Saved:", out_mels)
        print("Saved:", out_dlt)


if __name__ == "__main__":
    main()