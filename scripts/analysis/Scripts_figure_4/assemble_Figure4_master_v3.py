import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from PIL import Image
import matplotlib as mpl

# ============================================================
# Figure 4 (MAIN): W7_01 only — 2×2 layout (two columns)
# Panels:
# A: Mel triplet
# B: Delta
# C: Functional spectral redistribution
# D: OAAS trajectory (PC1–PC3)
# ============================================================

# === Typography (journal legibility) ===
mpl.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
})

# ----------------------------
# Helpers
# ----------------------------
def trim_white_border(img: np.ndarray, tol: int = 245, pad: int = 6) -> np.ndarray:
    """
    Trim near-white borders from an RGB/RGBA image array.
    tol: whiteness threshold (0-255). Higher = more aggressive trimming.
    pad: pixels to keep as padding after trim.
    """
    if img.dtype != np.uint8:
        # mpimg.imread often gives float 0..1; convert to uint8
        if img.max() <= 1.0:
            img8 = (img * 255).astype(np.uint8)
        else:
            img8 = img.astype(np.uint8)
    else:
        img8 = img

    # Handle RGBA by ignoring alpha for border detection
    if img8.ndim == 3 and img8.shape[2] == 4:
        rgb = img8[:, :, :3]
    else:
        rgb = img8

    # Non-white mask: any channel darker than tol
    mask = np.any(rgb < tol, axis=2)
    if not np.any(mask):
        return img  # nothing to trim

    ys, xs = np.where(mask)
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()

    # Add padding and clip
    y0 = max(0, y0 - pad)
    y1 = min(rgb.shape[0] - 1, y1 + pad)
    x0 = max(0, x0 - pad)
    x1 = min(rgb.shape[1] - 1, x1 + pad)

    cropped = img8[y0:y1+1, x0:x1+1]
    # Return in original scale (float) if input was float
    if img.dtype != np.uint8 and img.max() <= 1.0:
        return (cropped.astype(np.float32) / 255.0)
    return cropped

def save_reduction_tests(png_path: Path, out_dir: Path, base_name: str, dpi: int = 300):
    """
    Save simulated reductions at 170 mm (two columns) and 85 mm (one column).
    We resize the raster image to the corresponding pixel widths at given dpi.
    """
    img = Image.open(png_path).convert("RGB")
    w_px, h_px = img.size

    def mm_to_px(mm: float) -> int:
        inches = mm / 25.4
        return int(round(inches * dpi))

    for mm in (170, 85):
        target_w = mm_to_px(mm)
        scale = target_w / w_px
        target_h = int(round(h_px * scale))
        resized = img.resize((target_w, target_h), Image.LANCZOS)
        resized.save(out_dir / f"{base_name}_sim_{mm}mm.png", dpi=(dpi, dpi))

# ----------------------------
# Robust PATHS (no parents[n] guessing)
# ----------------------------
HERE = Path(__file__).resolve().parent
REPO = next(p for p in (HERE, *HERE.parents) if p.name == "OAAS_Applied_Acoustics_Repository")

BASE = REPO / "FIGURES_FINAL" / "READING_PNG" / "Fig4"
OUT  = REPO / "FIGURES_FINAL"
OUT.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Inputs (W7_01 only)
# ----------------------------
img_A = trim_white_border(mpimg.imread(BASE / "Fig4_mels_W7_01.png"), tol=248, pad=8)
img_B = trim_white_border(mpimg.imread(BASE / "Fig4_deltas_W7_01.png"), tol=248, pad=8)
img_C = trim_white_border(mpimg.imread(BASE / "Fig4_band_W7_01.png"), tol=250, pad=8)
img_D = trim_white_border(mpimg.imread(BASE / "Fig4_panelD_vectors_PC1_PC3_W7_01.png"), tol=250, pad=10)

# ----------------------------
# Layout: compact, centered, A/B slightly dominant
# ----------------------------
# Two-column width ~170 mm => ~6.7 in. Height tuned to reduce whitespace.
fig = plt.figure(figsize=(6.70, 5.35))
gs = fig.add_gridspec(
    2, 2,
    width_ratios=[1.25, 0.95],
    height_ratios=[1.00, 1.00],
    wspace=0.16,
    hspace=0.16
)

axA = fig.add_subplot(gs[0, 0])
axC = fig.add_subplot(gs[0, 1])
axB = fig.add_subplot(gs[1, 0])
axD = fig.add_subplot(gs[1, 1])

for ax, im in [(axA, img_A), (axB, img_B), (axC, img_C), (axD, img_D)]:
    ax.imshow(im, aspect="auto")
    ax.axis("off")

# Tight outer margins (reduce "aire")
fig.subplots_adjust(left=0.04, right=0.995, top=0.985, bottom=0.04)

# ----------------------------
# Panel letters: aligned consistently
# ----------------------------
def panel_label(ax, letter: str):
    ax.text(
        -0.10, 1.08, letter,
        transform=ax.transAxes,
        fontsize=12, fontweight="bold",
        va="top", ha="left"
    )

panel_label(axA, "A")
panel_label(axB, "B")
panel_label(axC, "C")
panel_label(axD, "D")

# ----------------------------
# Export
# ----------------------------
out_png = OUT / "Figure_4_MAIN_W7_01.png"
out_tif = OUT / "Figure_4_MAIN_W7_01.tif"

fig.savefig(out_png, dpi=300, bbox_inches="tight", pad_inches=0.01)
fig.savefig(out_tif, dpi=600, bbox_inches="tight", pad_inches=0.01)
plt.close(fig)

print(f"Exported: {out_png}")
print(f"Exported: {out_tif}")

# Reduction tests (journal legibility check)
save_reduction_tests(out_png, OUT, "Figure_4_MAIN_W7_01", dpi=300)
print(f"Saved reduction tests in: {OUT}")