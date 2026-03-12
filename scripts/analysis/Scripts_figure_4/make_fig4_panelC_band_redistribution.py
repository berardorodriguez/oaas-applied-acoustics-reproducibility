#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import argparse
from pathlib import Path
import math

import numpy as np
import matplotlib.pyplot as plt

try:
    import soundfile as sf
except Exception as e:
    raise SystemExit("Missing dependency: soundfile. Install with: pip install soundfile") from e

try:
    import librosa
except Exception as e:
    raise SystemExit("Missing dependency: librosa. Install with: pip install librosa") from e


def load_mono(path: Path):
    y, sr = sf.read(str(path), always_2d=False)
    if y.ndim == 2:
        y = y.mean(axis=1)
    y = y.astype(np.float32)
    return y, int(sr)


def band_energies(y: np.ndarray, sr: int, n_fft: int, hop: int, bands_hz: list[tuple[float, float]]):
    """
    Compute mean power per frequency band using STFT power spectrogram.
    Returns energies per band (linear power, not dB).
    """
    # power spectrogram
    S = np.abs(librosa.stft(y=y, n_fft=n_fft, hop_length=hop, center=True)) ** 2
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

    energies = []
    for lo, hi in bands_hz:
        mask = (freqs >= lo) & (freqs < hi)
        if not np.any(mask):
            energies.append(np.nan)
            continue
        # average over time then sum over freq bins (power)
        e = float(np.mean(np.sum(S[mask, :], axis=0)))
        energies.append(e)
    return np.array(energies, dtype=float)


def delta_db(e_var: np.ndarray, e_ref: np.ndarray):
    eps = 1e-12
    return 10.0 * np.log10((e_var + eps) / (e_ref + eps))


def make_panelC_for_stim(stim: str, folder: Path, outdir: Path,
                         bands_hz: list[tuple[float, float]], band_labels: list[str],
                         n_fft: int, hop: int, ylim: float):
    p0 = folder / f"{stim}_original_30s.wav"
    pp = folder / f"{stim}_POS_30s.wav"
    pn = folder / f"{stim}_NEG_30s.wav"

    for p in (p0, pp, pn):
        if not p.exists():
            raise SystemExit(f"Missing WAV: {p}")

    y0, sr0 = load_mono(p0)
    yp, srp = load_mono(pp)
    yn, srn = load_mono(pn)

    if not (sr0 == srp == srn):
        raise SystemExit(f"Sample rate mismatch in {stim}: {sr0}, {srp}, {srn}")

    e0 = band_energies(y0, sr0, n_fft, hop, bands_hz)
    ep = band_energies(yp, sr0, n_fft, hop, bands_hz)
    en = band_energies(yn, sr0, n_fft, hop, bands_hz)

    dp = delta_db(ep, e0)
    dn = delta_db(en, e0)

    # Plot: grouped bars (POS and NEG) across bands
    fig = plt.figure(figsize=(5.4, 3.3))
    ax = fig.add_subplot(1, 1, 1)

    x = np.arange(len(band_labels))
    w = 0.36

    ax.bar(x - w/2, dp, width=w, label="POS − Original")
    ax.bar(x + w/2, dn, width=w, label="NEG − Original")

    ax.axhline(0, linewidth=1.0)
    ax.set_xticks(x)
    ax.set_xticklabels(band_labels)
    ax.set_ylabel("Δ band energy (dB)")
    ax.set_title(f"{stim} — Functional spectral redistribution")
    ax.set_ylim(-ylim, ylim)
    ax.legend(frameon=False, fontsize=8, loc="upper right")

    fig.tight_layout()
    out_png = outdir / f"Fig4_band_{stim}.png"
    fig.savefig(out_png, dpi=300)
    plt.close(fig)
    print("Saved:", out_png)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True, help="Root folder with W7_01/ and W8_03/ WAVs.")
    ap.add_argument("--outdir", type=Path, required=True, help="Output directory for panel C PNGs.")
    ap.add_argument("--fmax", type=float, default=8000.0, help="Upper freq used for high band (Hz).")
    ap.add_argument("--low_hi", type=float, default=500.0, help="Low band upper bound (Hz).")
    ap.add_argument("--mid_hi", type=float, default=2000.0, help="Mid band upper bound (Hz).")
    ap.add_argument("--n_fft", type=int, default=4096)
    ap.add_argument("--hop", type=int, default=512)
    ap.add_argument("--ylim", type=float, default=20.0, help="Symmetric Y limit in dB.")
    args = ap.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    bands = [(0.0, args.low_hi), (args.low_hi, args.mid_hi), (args.mid_hi, args.fmax)]
    labels = ["Low", "Mid", "High"]

    for stim in ["W7_01", "W8_03"]:
        make_panelC_for_stim(
            stim=stim,
            folder=args.root / stim,
            outdir=args.outdir,
            bands_hz=bands,
            band_labels=labels,
            n_fft=args.n_fft,
            hop=args.hop,
            ylim=args.ylim
        )


if __name__ == "__main__":
    main()