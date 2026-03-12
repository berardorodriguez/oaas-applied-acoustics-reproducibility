# Operational Acoustic Affective Space (OAAS)

### Applied Acoustics Research Companion Repository

This repository contains the data, scripts, and audio examples
supporting the manuscript:

**Operational Acoustic Affective Space (OAAS):\
An Ethologically Grounded Framework for Functional Acoustic Modulation**

Submitted to **Applied Acoustics**.

------------------------------------------------------------------------

# Authors

**Berardo de Jesús Rodríguez**\
Universidad de Antioquia

**Juliana Zapata‑Cardona**\
Universidad de Antioquia

------------------------------------------------------------------------

# Overview

The **Operational Acoustic Affective Space (OAAS)** is a computational
framework designed to analyze and modulate affective structure in
acoustic environments using biologically grounded vocal reference
systems.

The framework integrates:

-   ethological vocalization anchors\
-   heterogeneous acoustic stimuli\
-   centroid‑distance operational metrics\
-   controlled acoustic transformations

OAAS enables **positioning, diagnosis, and functional modification of
acoustic environments while preserving signal identity**.

This repository contains the materials necessary to reproduce the
analyses and figures presented in the manuscript.

------------------------------------------------------------------------

# Repository Structure

OAAS_Applied_Acoustics_Repository/

audio/\
Example stimuli used for OAAS transformation experiments

data/\
Processed datasets used for figure generation

docs/\
Documentation related to the manuscript

figures/\
Generated manuscript figures

scripts/\
Analysis and figure generation scripts

supplementary/\
Supplementary material used in the journal submission

------------------------------------------------------------------------

# Figures Included in the Repository

## Figure 1 --- OAAS Framework

Conceptual diagram describing the OAAS analytical pipeline.

The diagram illustrates:

-   acoustic inputs\
-   preprocessing and feature extraction\
-   vocal‑only OAAS diagnostic structure\
-   joint acoustic embedding\
-   centroid‑distance metrics\
-   OAAS‑guided acoustic transformation layer\
-   operational outputs

This figure is conceptual and **does not require scripts for
reproduction**.

------------------------------------------------------------------------

## Figure 2 --- OAAS Joint Embedding

Two‑dimensional projections of the OAAS embedding showing:

-   OAAS1 vs OAAS2\
-   OAAS1 vs OAAS3

The embedding integrates four stimulus domains:

-   vocalization anchors (SoundWel)\
-   functional music stimuli\
-   challenge reference stimuli\
-   noise reference signals

These overlays illustrate how heterogeneous acoustic environments are
positioned within the OAAS space.

------------------------------------------------------------------------

## Figure 3 --- Vocal‑only OAAS Protoatlas

Principal component representation derived exclusively from **SoundWel
vocalization ensembles**.

The figure shows:

-   vocalization context centroids\
-   POS and NEG anchor sets\
-   baseline ethological acoustic structure

This protoatlas defines the **operational anchor system** used in OAAS.

------------------------------------------------------------------------

## Figure 4 --- Functional Acoustic Transformation

Example OAAS‑guided transformation applied to stimulus **W7_01**.

Panels include:

A --- Mel‑spectrogram comparison\
B --- Δ spectrograms\
C --- Functional spectral redistribution\
D --- OAAS trajectory

Scripts used:

scripts/analysis/make_fig4_spectrograms_AB.py\
scripts/analysis/make_fig4_panelC_band_redistribution.py\
scripts/analysis/make_fig4_panelD_vectors_W7only_v3.py\
scripts/analysis/assemble_Figure4_master_v3.py

------------------------------------------------------------------------

## Figure 5 --- OAAS Centroid‑Distance Decision Plane

Visualization of stimulus positioning relative to vocal anchor
centroids.

Axes represent:

x‑axis --- distance to NEG vocal centroid\
y‑axis --- distance to POS vocal centroid

Domains shown:

-   vocal anchor sets\
-   functional music stimuli\
-   challenge reference stimuli\
-   noise reference signals (inset)

Script used:

scripts/analysis/scripts_figures_5/make_fig5_distance_plane.py

------------------------------------------------------------------------

# Audio Material

The repository contains example stimuli used in OAAS transformation
demonstrations.

## Challenger Stimuli

Three **challenger stimuli** are included:

-   Challenger_01\
-   Challenger_02\
-   Challenger_03

These stimuli are **synthetic musical soundscape fragments** designed to
challenge the operational behavior of the OAAS framework.

They intentionally incorporate acoustic configurations constructed to
**stress‑test the OAAS embedding**.

------------------------------------------------------------------------

## OAAS Transformation Stimuli

Two stimuli were used for transformation experiments:

-   W7_01\
-   W8_03

Each stimulus includes:

-   original audio\
-   POS transformation\
-   NEG transformation\
-   OAAS_travel_log.csv

The travel log records the displacement trajectory of the stimulus
within OAAS space.

------------------------------------------------------------------------

# Sampling Parameters

Audio duration: **30 seconds**\
Sampling rate: **48 kHz**

------------------------------------------------------------------------

# Reproducibility

All figures presented in the manuscript can be reproduced using the
scripts located in the `/scripts` directory.

Processed datasets required for figure generation are included in
`/data`.

------------------------------------------------------------------------

# Software Requirements

Python **3.10+**

Libraries:

numpy\
pandas\
matplotlib\
scikit‑learn\
scipy\
librosa

------------------------------------------------------------------------

# Quick Reproduction

Run commands from the repository root directory.

### Figure 2

python scripts/analysis/make_fig2_overlay_4groups.py

### Figure 3

python scripts/analysis/make_fig3_vocal_only_oaas.py

### Figure 4

python scripts/analysis/make_fig4_spectrograms_AB.py\
python scripts/analysis/make_fig4_panelC_band_redistribution.py\
python scripts/analysis/make_fig4_panelD_vectors_W7only_v3.py\
python scripts/analysis/assemble_Figure4_master_v3.py

### Figure 5

python scripts/analysis/scripts_figures_5/make_fig5_distance_plane.py

------------------------------------------------------------------------

# Data Availability

This repository distributes:

-   derived acoustic embeddings\
-   centroid‑distance datasets\
-   OAAS transformation logs\
-   example audio stimuli

The proprietary SoundWel recordings are not distributed.

------------------------------------------------------------------------

# License

Code: MIT License\
Data: CC BY 4.0\
Audio: Copyright © Universidad de Antioquia

------------------------------------------------------------------------

# Citation

A `CITATION.cff` file is included for citation metadata.

------------------------------------------------------------------------

# Contact

Berardo de Jesús Rodríguez\
Universidad de Antioquia\
berardo.rodriguez@udea.edu.co

Juliana Zapata‑Cardona\
Universidad de Antioquia\
juliana.zapata9@udea.edu.co
