#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
oaas_directional_transform.py

OAAS-guided constrained directional transformation script.

This script generates positive-directed (POS) and negative-directed (NEG)
candidate variants from an input WAV file, projects each candidate into a
PCA-defined OAAS space, and selects the best candidate according to Euclidean
distance to the corresponding vocal-derived OAAS centroid.

The implementation is intended as a reproducibility resource for the OAAS
operability experiments. It uses the reduced 9-dimensional OAAS feature set:

- spectral entropy mean, SD, and 95th percentile
- spectral flatness mean, SD, and 95th percentile
- RMS temporal entropy
- multiscale envelope entropy
- harmonic ratio

Core constraints:
- target sample rate controlled by --target_sr, default 48000 Hz
- RMS preservation within approximately +/-0.5 dB after transformation
- peak safety with default true-peak ceiling proxy of -1 dBFS
- selection by centroid-distance minimization in OAAS1-OAAS3

Requirements:
    pip install numpy pandas librosa soundfile scipy scikit-learn

Example PowerShell command:
    python ./oaas_directional_transform.py `
        --input_wav "..\audio\W7_01.wav" `
        --out_dir "..\outputs\OAAS_directional_transform\W7_01" `
        --oaas_master_csv "..\data\OAAS_master_projected_with_noise_reference.csv" `
        --target_sr 48000 `
        --n_pos 40 `
        --n_neg 40 `
        --seed 123
"""

from __future__ import annotations

import argparse
import sys
import warnings
from pathlib import Path
from typing import Iterable

import librosa
import numpy as np
import pandas as pd
import soundfile as sf
from scipy import signal
from sklearn.decomposition import PCA

EPS = 1e-12

# ----------------------------- OAAS ANCHOR DEFINITIONS -----------------------------
# Default anchor contexts are aligned with the revised manuscript.
# Matching is performed by substring search in available metadata columns.
DEFAULT_POS_CONTEXTS = [
    "Huddling",
    "Run",
    "Enriched",
    "AfterNursing",
    "BeforeNursing",
]

DEFAULT_NEG_CONTEXTS = [
    "Castration",
    "Crushing",
    "Restrain",
    "LongIsolation",
    "ShortIsolation",
    "MissedNursing",
    "Fighting",
    "Barren",
]

CONTEXT_SEARCH_COLUMNS = [
    "context",
    "category",
    "label",
    "emission_context",
    "SoundWel_context",
    "file",
    "filename",
    "stimulus",
]


# ----------------------------- LEVEL CONTROL -----------------------------
PEAK_TARGET_DBFS = -1.0
PEAK_TARGET = 10 ** (PEAK_TARGET_DBFS / 20.0)
RMS_TOL_DB = 0.5


def _rms_lin(y: np.ndarray) -> float:
    y = y.astype(np.float64, copy=False)
    return float(np.sqrt(np.mean(y * y) + EPS))


def _db_ratio(a: float, b: float) -> float:
    """Return absolute dB difference between two positive linear RMS values."""
    if a < EPS or b < EPS:
        return 0.0
    return abs(20.0 * np.log10((a + EPS) / (b + EPS)))


def _match_rms(y: np.ndarray, target_rms: float) -> np.ndarray:
    cur = _rms_lin(y)
    if cur < 1e-9 or target_rms < 1e-9:
        return y.astype(np.float32)
    return (y * (target_rms / (cur + EPS))).astype(np.float32)


def _peak_limit(y: np.ndarray, peak_target: float = PEAK_TARGET) -> np.ndarray:
    pk = float(np.max(np.abs(y)) + EPS)
    if pk > peak_target:
        y = (y * (peak_target / pk)).astype(np.float32)
    return y.astype(np.float32)


def _apply_level_constraints(y: np.ndarray, ref_rms: float) -> np.ndarray:
    """
    Match RMS to the input reference and enforce peak safety.
    If peak limiting causes RMS drift beyond RMS_TOL_DB, one additional
    RMS-match/peak-limit pass is applied.
    """
    y = _match_rms(y, ref_rms)
    y = _peak_limit(y)

    if _db_ratio(_rms_lin(y), ref_rms) > RMS_TOL_DB:
        y = _match_rms(y, ref_rms)
        y = _peak_limit(y)

    return y.astype(np.float32)


# ----------------------------- CORE FEATURES -----------------------------
def _spectral_entropy_from_mag(mag: np.ndarray, eps: float = EPS) -> float:
    p = mag / (np.sum(mag) + eps)
    return float(-np.sum(p * np.log2(p + eps)))


def _spectral_flatness_from_mag(mag: np.ndarray, eps: float = EPS) -> float:
    gmean = np.exp(np.mean(np.log(mag + eps)))
    amean = np.mean(mag + eps)
    return float(gmean / (amean + eps))


def _frame_audio(y: np.ndarray, frame_length: int = 2048, hop_length: int = 512) -> np.ndarray:
    return librosa.util.frame(y, frame_length=frame_length, hop_length=hop_length)


def compute_core_features(y: np.ndarray, sr: int, n_fft: int = 2048, hop: int = 512) -> dict:
    """Compute the reduced 9-dimensional OAAS feature set."""
    S = np.abs(librosa.stft(y.astype(np.float32), n_fft=n_fft, hop_length=hop, window="hann")) + EPS

    se = np.array([_spectral_entropy_from_mag(S[:, i]) for i in range(S.shape[1])], dtype=np.float64)
    fl = np.array([_spectral_flatness_from_mag(S[:, i]) for i in range(S.shape[1])], dtype=np.float64)

    feats = {
        "se_mean": float(np.mean(se)),
        "se_std": float(np.std(se)),
        "se_p95": float(np.percentile(se, 95)),
        "flatness_mean": float(np.mean(fl)),
        "flatness_std": float(np.std(fl)),
        "flatness_p95": float(np.percentile(fl, 95)),
    }

    frames = _frame_audio(y, frame_length=n_fft, hop_length=hop).astype(np.float64)
    rms = np.sqrt(np.mean(frames**2, axis=0) + EPS)
    rms_db = 20.0 * np.log10(rms + EPS)

    hist, _ = np.histogram(rms_db, bins=64, density=True)
    hist = hist + EPS
    hist = hist / np.sum(hist)
    feats["te_rms"] = float(-np.sum(hist * np.log2(hist)))

    def sampen(x: np.ndarray, m: int = 2, r: float = 0.2) -> float:
        x = np.asarray(x, dtype=np.float64)
        if x.size < (m + 2):
            return 0.0
        sd = np.std(x) + EPS
        r *= sd

        def _phi(mm: int) -> float:
            n_templates = x.size - mm + 1
            if n_templates <= 1:
                return 0.0
            templates = np.array([x[i:i + mm] for i in range(n_templates)])
            counts = (
                np.sum(
                    np.max(np.abs(templates[:, None, :] - templates[None, :, :]), axis=2) <= r,
                    axis=0,
                )
                - 1
            )
            return float(np.sum(counts) / (n_templates * (n_templates - 1) + EPS))

        p_m = _phi(m)
        p_m1 = _phi(m + 1)
        return float(-np.log((p_m1 + EPS) / (p_m + EPS)))

    mse_vals = []
    for scale in [1, 2, 4]:
        xs = rms[::scale] if scale > 1 else rms
        mse_vals.append(sampen(xs, m=2, r=0.2))
    feats["mse_env"] = float(np.mean(mse_vals))

    y_h, y_p = librosa.effects.hpss(y.astype(np.float32))
    eh = float(np.sum(y_h.astype(np.float64) ** 2))
    ep = float(np.sum(y_p.astype(np.float64) ** 2))
    feats["harm_ratio"] = float(eh / (eh + ep + EPS))

    feats["sr"] = int(sr)
    feats["dur_sec"] = float(len(y) / sr)
    return feats


CORE_COLS = [
    "se_mean",
    "se_std",
    "se_p95",
    "flatness_mean",
    "flatness_std",
    "flatness_p95",
    "te_rms",
    "mse_env",
    "harm_ratio",
]


# ----------------------------- OAAS MODEL -----------------------------
def fit_oaas_from_master(master_csv: str):
    """
    Fit z-score normalization and PCA from the canonical OAAS master CSV.

    Required columns:
    - domain
    - file
    - the nine CORE_COLS variables
    """
    df = pd.read_csv(master_csv)

    required = set(CORE_COLS + ["domain", "file"])
    missing = sorted(list(required - set(df.columns)))
    if missing:
        raise ValueError(
            f"{master_csv} is missing required columns: {missing}. "
            "Please verify the canonical OAAS master file."
        )

    X = df[CORE_COLS].astype(float).values
    mu = X.mean(axis=0)
    sd = X.std(axis=0) + EPS
    Xz = (X - mu) / sd

    pca = PCA(n_components=3, random_state=0)
    pca.fit(Xz)

    return df, mu, sd, pca


def project_features_to_oaas(feats_row: dict, mu: np.ndarray, sd: np.ndarray, pca: PCA) -> np.ndarray:
    x = np.array([feats_row[c] for c in CORE_COLS], dtype=np.float64)
    xz = (x - mu) / sd
    return pca.transform(xz.reshape(1, -1))[0]


def _metadata_text(row: pd.Series, columns: Iterable[str]) -> str:
    parts = []
    for col in columns:
        if col in row.index and pd.notna(row[col]):
            parts.append(str(row[col]))
    return " ".join(parts)


def _match_contexts(df: pd.DataFrame, contexts: list[str]) -> pd.Series:
    available_cols = [c for c in CONTEXT_SEARCH_COLUMNS if c in df.columns]
    if not available_cols:
        available_cols = ["file"]

    pattern_contexts = [c.lower() for c in contexts]
    mask_values = []
    for _, row in df.iterrows():
        text = _metadata_text(row, available_cols).lower()
        mask_values.append(any(ctx in text for ctx in pattern_contexts))
    return pd.Series(mask_values, index=df.index)


def compute_poles_from_master(
    df_master: pd.DataFrame,
    mu: np.ndarray,
    sd: np.ndarray,
    pca: PCA,
    pos_contexts: list[str] | None = None,
    neg_contexts: list[str] | None = None,
    allow_median_fallback: bool = False,
):
    """
    Compute POS and NEG vocal centroids from manuscript-aligned context sets.

    By default, POS/NEG centroids are computed from SoundWel context names
    listed in DEFAULT_POS_CONTEXTS and DEFAULT_NEG_CONTEXTS. The function
    searches context metadata fields when present and falls back to file names.

    A median-based fallback can be enabled with --allow_median_fallback, but it
    is disabled by default to avoid silent mismatch with the manuscript anchors.
    """
    pos_contexts = pos_contexts or DEFAULT_POS_CONTEXTS
    neg_contexts = neg_contexts or DEFAULT_NEG_CONTEXTS

    X = df_master[CORE_COLS].astype(float).values
    Xz = (X - mu) / sd
    Z = pca.transform(Xz)

    tmp = df_master.copy()
    tmp["OAAS1"], tmp["OAAS2"], tmp["OAAS3"] = Z[:, 0], Z[:, 1], Z[:, 2]

    voc = tmp[tmp["domain"].astype(str).str.lower().eq("vocalization")].copy()
    if voc.empty:
        raise ValueError(
            "No rows with domain == 'vocalization' were found. "
            "Cannot compute vocal-derived OAAS anchor centroids."
        )

    voc_pos = voc[_match_contexts(voc, pos_contexts)]
    voc_neg = voc[_match_contexts(voc, neg_contexts)]

    if voc_pos.empty or voc_neg.empty:
        message = (
            "Could not identify POS and/or NEG vocal anchors using the default "
            "manuscript context lists.\n"
            f"POS contexts searched: {pos_contexts}\n"
            f"NEG contexts searched: {neg_contexts}\n"
            "Please verify context/file naming in the master CSV or pass "
            "--pos_contexts and --neg_contexts explicitly."
        )
        if not allow_median_fallback:
            raise ValueError(message)
        warnings.warn(message + " Falling back to OAAS1 median split.", RuntimeWarning)
        med = voc["OAAS1"].median()
        voc_pos = voc[voc["OAAS1"] <= med]
        voc_neg = voc[voc["OAAS1"] > med]

    pos_center = voc_pos[["OAAS1", "OAAS2", "OAAS3"]].mean().values
    neg_center = voc_neg[["OAAS1", "OAAS2", "OAAS3"]].mean().values

    return pos_center, neg_center, tmp, voc_pos, voc_neg


# ----------------------------- TRANSFORM OPERATORS -----------------------------
def add_colored_noise(y: np.ndarray, strength: float = 0.02, color: str = "white", rng=None) -> np.ndarray:
    rng = np.random.default_rng() if rng is None else rng
    n = rng.standard_normal(size=y.shape[0]).astype(np.float32)

    if color == "pink":
        N = len(n)
        F = np.fft.rfft(n)
        freqs = np.fft.rfftfreq(N, d=1.0)
        w = 1.0 / np.sqrt(np.maximum(freqs, 1e-6))
        F2 = F * w
        n = np.fft.irfft(F2, n=N).astype(np.float32)
        n /= np.max(np.abs(n)) + EPS
    elif color == "brown":
        n = np.cumsum(n).astype(np.float32)
        n /= np.max(np.abs(n)) + EPS

    return (y + strength * n).astype(np.float32)


def spectral_tilt(y: np.ndarray, sr: int, tilt_db: float = 0.0) -> np.ndarray:
    """Apply a simple frequency-domain tilt around 1 kHz."""
    N = len(y)
    Y = np.fft.rfft(y.astype(np.float32))
    freqs = np.fft.rfftfreq(N, d=1.0 / sr)
    f_ref = 1000.0
    k = tilt_db / 20.0
    w = (np.maximum(freqs, 1.0) / f_ref) ** k
    Y2 = Y * w
    y2 = np.fft.irfft(Y2, n=N).astype(np.float32)
    y2 /= np.max(np.abs(y2)) + EPS
    return y2


def envelope_smooth(y: np.ndarray, win_ms: float = 30, sr: int = 48000) -> np.ndarray:
    win = max(5, int(sr * (win_ms / 1000.0)))
    if win % 2 == 0:
        win += 1
    env = np.abs(signal.hilbert(y.astype(np.float32)))
    env_s = signal.medfilt(env, kernel_size=win)
    gain = env_s / (env + EPS)
    y2 = (y * gain).astype(np.float32)
    y2 /= np.max(np.abs(y2)) + EPS
    return y2


def soft_clip(y: np.ndarray, drive: float = 1.0) -> np.ndarray:
    x = (drive * y).astype(np.float32)
    y2 = np.tanh(x).astype(np.float32)
    y2 /= np.max(np.abs(y2)) + EPS
    return y2


def candidate_to_POS(y: np.ndarray, sr: int, rng) -> np.ndarray:
    """Generate one POS-directed candidate."""
    y2 = y.copy().astype(np.float32)

    # Reduce envelope irregularity.
    y2 = envelope_smooth(y2, win_ms=float(rng.uniform(15, 45)), sr=sr)

    # Reduce broadband energy with a gentle low-pass filter.
    nyq = sr / 2.0
    low = min(3500.0, 0.70 * nyq)
    high = 0.99 * nyq
    if low < 10.0:
        low = 10.0
    if low >= high:
        low = 0.50 * nyq

    cut = float(rng.uniform(low, high))
    wn = cut / nyq
    sos = signal.butter(4, wn, btype="lowpass", output="sos")
    y2 = signal.sosfilt(sos, y2).astype(np.float32)

    # Increase harmonic organization proxy through gentle saturation.
    y2 = soft_clip(y2, drive=float(rng.uniform(1.0, 2.2)))

    # Slightly attenuate high-frequency emphasis.
    y2 = spectral_tilt(y2, sr, tilt_db=float(rng.uniform(-0.6, -0.1)))

    return _apply_level_constraints(y2, _rms_lin(y))


def candidate_to_NEG(y: np.ndarray, sr: int, rng) -> np.ndarray:
    """Generate one NEG-directed candidate."""
    y2 = y.copy().astype(np.float32)

    # Increase flatness and entropy with a low-level colored-noise layer.
    color = rng.choice(["white", "pink", "brown"])
    y2 = add_colored_noise(y2, strength=float(rng.uniform(0.01, 0.06)), color=color, rng=rng)

    # Emphasize broadband/high-frequency edge content.
    cut = float(rng.uniform(120, min(900, 0.45 * sr)))
    sos = signal.butter(3, cut / (sr / 2), btype="highpass", output="sos")
    y2 = signal.sosfilt(sos, y2).astype(np.float32)

    # Apply positive spectral tilt.
    y2 = spectral_tilt(y2, sr, tilt_db=float(rng.uniform(0.15, 0.9)))

    # Add envelope micro-variability.
    hop = max(1, int(sr * 0.05))
    g = rng.uniform(0.6, 1.4, size=int(np.ceil(len(y2) / hop))).astype(np.float32)
    g = np.repeat(g, hop)[: len(y2)]
    y2 = (y2 * g).astype(np.float32)

    return _apply_level_constraints(y2, _rms_lin(y))


# ----------------------------- UTILITY -----------------------------
def _ensure_utf8_stdout() -> None:
    """Prevent UnicodeEncodeError on Windows consoles."""
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def _parse_contexts(value: str | None, default: list[str]) -> list[str]:
    if value is None or not value.strip():
        return default
    return [item.strip() for item in value.split(",") if item.strip()]


# ----------------------------- MAIN -----------------------------
def main() -> None:
    _ensure_utf8_stdout()

    parser = argparse.ArgumentParser(
        description="Generate OAAS-guided POS/NEG directional acoustic transformations."
    )
    parser.add_argument("--input_wav", required=True, help="Input WAV file.")
    parser.add_argument("--out_dir", required=True, help="Output directory.")
    parser.add_argument(
        "--oaas_master_csv",
        required=True,
        help="Canonical OAAS CSV containing domain, file, and the reduced OAAS core features.",
    )
    parser.add_argument("--target_sr", type=int, default=48000, help="Target sample rate.")
    parser.add_argument("--n_pos", type=int, default=40, help="Number of POS candidates.")
    parser.add_argument("--n_neg", type=int, default=40, help="Number of NEG candidates.")
    parser.add_argument("--seed", type=int, default=0, help="Random seed.")
    parser.add_argument(
        "--pos_contexts",
        default=None,
        help="Comma-separated POS context names. Defaults to manuscript POS anchors.",
    )
    parser.add_argument(
        "--neg_contexts",
        default=None,
        help="Comma-separated NEG context names. Defaults to manuscript NEG anchors.",
    )
    parser.add_argument(
        "--allow_median_fallback",
        action="store_true",
        help="Allow OAAS1 median split if manuscript context anchors are not found.",
    )

    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    y, sr = librosa.load(args.input_wav, sr=args.target_sr, mono=True)
    y = _peak_limit(y.astype(np.float32))

    df_master, mu, sd, pca = fit_oaas_from_master(args.oaas_master_csv)

    pos_contexts = _parse_contexts(args.pos_contexts, DEFAULT_POS_CONTEXTS)
    neg_contexts = _parse_contexts(args.neg_contexts, DEFAULT_NEG_CONTEXTS)

    pos_center, neg_center, _master_proj, voc_pos, voc_neg = compute_poles_from_master(
        df_master,
        mu,
        sd,
        pca,
        pos_contexts=pos_contexts,
        neg_contexts=neg_contexts,
        allow_median_fallback=args.allow_median_fallback,
    )

    rng = np.random.default_rng(args.seed)
    rows = []

    f0 = compute_core_features(y, sr)
    c0 = project_features_to_oaas(f0, mu, sd, pca)
    dpos0 = float(np.linalg.norm(c0 - pos_center))
    dneg0 = float(np.linalg.norm(c0 - neg_center))
    aai0 = float((dneg0 - dpos0) / (dneg0 + dpos0 + EPS))

    rows.append(
        {
            "variant": "ORIGINAL",
            "to": "none",
            "d_pos": dpos0,
            "d_neg": dneg0,
            "AAI_OAAS": aai0,
            "OAAS1": c0[0],
            "OAAS2": c0[1],
            "OAAS3": c0[2],
            **{k: f0[k] for k in CORE_COLS},
        }
    )

    best_pos = None
    for i in range(args.n_pos):
        yc = candidate_to_POS(y, sr, rng)
        feats = compute_core_features(yc, sr)
        coords = project_features_to_oaas(feats, mu, sd, pca)
        dpos = float(np.linalg.norm(coords - pos_center))
        dneg = float(np.linalg.norm(coords - neg_center))
        aai = float((dneg - dpos) / (dneg + dpos + EPS))
        row = {
            "variant": f"POS_{i:03d}",
            "to": "POS",
            "d_pos": dpos,
            "d_neg": dneg,
            "AAI_OAAS": aai,
            "OAAS1": coords[0],
            "OAAS2": coords[1],
            "OAAS3": coords[2],
            **{k: feats[k] for k in CORE_COLS},
        }
        rows.append(row)
        if best_pos is None or dpos < best_pos["d_pos"]:
            best_pos = {"row": row, "audio": yc, "d_pos": dpos, "d_neg": dneg}

    best_neg = None
    for i in range(args.n_neg):
        yc = candidate_to_NEG(y, sr, rng)
        feats = compute_core_features(yc, sr)
        coords = project_features_to_oaas(feats, mu, sd, pca)
        dpos = float(np.linalg.norm(coords - pos_center))
        dneg = float(np.linalg.norm(coords - neg_center))
        aai = float((dneg - dpos) / (dneg + dpos + EPS))
        row = {
            "variant": f"NEG_{i:03d}",
            "to": "NEG",
            "d_pos": dpos,
            "d_neg": dneg,
            "AAI_OAAS": aai,
            "OAAS1": coords[0],
            "OAAS2": coords[1],
            "OAAS3": coords[2],
            **{k: feats[k] for k in CORE_COLS},
        }
        rows.append(row)
        if best_neg is None or dneg < best_neg["d_neg"]:
            best_neg = {"row": row, "audio": yc, "d_pos": dpos, "d_neg": dneg}

    log = pd.DataFrame(rows).sort_values(["to", "d_pos", "d_neg"], ascending=[True, True, True])
    log_path = out_dir / "OAAS_directional_transform_log.csv"
    log.to_csv(log_path, index=False, encoding="utf-8")

    in_name = Path(args.input_wav).stem
    best_pos_path = None
    best_neg_path = None

    if best_pos is not None:
        best_pos_path = out_dir / f"{in_name}__toPOS__{best_pos['row']['variant']}.wav"
        sf.write(str(best_pos_path), best_pos["audio"], sr)

    if best_neg is not None:
        best_neg_path = out_dir / f"{in_name}__toNEG__{best_neg['row']['variant']}.wav"
        sf.write(str(best_neg_path), best_neg["audio"], sr)

    summary_path = out_dir / "summary.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("OAAS directional transform summary\n")
        f.write("----------------------------------\n")
        f.write(f"input_wav: {args.input_wav}\n")
        f.write(f"oaas_master_csv: {args.oaas_master_csv}\n")
        f.write(f"target_sr: {sr}\n")
        f.write(f"n_pos: {args.n_pos}\n")
        f.write(f"n_neg: {args.n_neg}\n")
        f.write(f"seed: {args.seed}\n")
        f.write(f"pos_contexts: {', '.join(pos_contexts)}\n")
        f.write(f"neg_contexts: {', '.join(neg_contexts)}\n")
        f.write(f"n_pos_anchor_rows: {len(voc_pos)}\n")
        f.write(f"n_neg_anchor_rows: {len(voc_neg)}\n\n")
        f.write(f"original_d_pos: {dpos0}\n")
        f.write(f"original_d_neg: {dneg0}\n")
        f.write(f"original_AAI_OAAS: {aai0}\n\n")
        if best_pos is not None:
            f.write(f"best_POS_variant: {best_pos['row']['variant']}\n")
            f.write(f"best_POS_d_pos: {best_pos['row']['d_pos']}\n")
            f.write(f"best_POS_d_neg: {best_pos['row']['d_neg']}\n")
            f.write(f"best_POS_AAI_OAAS: {best_pos['row']['AAI_OAAS']}\n")
            f.write(f"best_POS_path: {best_pos_path}\n\n")
        else:
            f.write("best_POS_variant: None\n\n")
        if best_neg is not None:
            f.write(f"best_NEG_variant: {best_neg['row']['variant']}\n")
            f.write(f"best_NEG_d_pos: {best_neg['row']['d_pos']}\n")
            f.write(f"best_NEG_d_neg: {best_neg['row']['d_neg']}\n")
            f.write(f"best_NEG_AAI_OAAS: {best_neg['row']['AAI_OAAS']}\n")
            f.write(f"best_NEG_path: {best_neg_path}\n")
        else:
            f.write("best_NEG_variant: None\n")

    print("[OK] OAAS directional transform finished")
    print("Log CSV:", log_path)
    print("Summary:", summary_path)
    print("Original d_pos/d_neg/AAI:", dpos0, dneg0, aai0)
    if best_pos:
        print(
            "Best POS:",
            best_pos["row"]["variant"],
            "d_pos=",
            best_pos["row"]["d_pos"],
            "AAI=",
            best_pos["row"]["AAI_OAAS"],
        )
    if best_neg:
        print(
            "Best NEG:",
            best_neg["row"]["variant"],
            "d_neg=",
            best_neg["row"]["d_neg"],
            "AAI=",
            best_neg["row"]["AAI_OAAS"],
        )


if __name__ == "__main__":
    main()
