# Data

This directory contains the experimental and processed datasets supporting the KineticAI-AWGC platform and the Kinetic Blueprint framework.

## Provenance

All datasets are transcribed from the peer-reviewed experimental studies listed in `docs/publications.md` (primarily Workie et al., *Crystals* 13(7):1049, 2023, and the Kinetic Blueprint studies that followed). Derived/curated values are flagged as such in each file's documentation. Raw instrument files (diffraction spectra, SEM micrographs) are available in the source publications; this repository ships the quantified results extracted from them.

## Structure

```text
data/
├── raw/                  # Primary experimental values as reported
├── processed/            # Analysis-ready, derived datasets
├── kinetic_blueprint_master.csv   # Integrated processing–structure–transport dataset
├── pH_time_series.csv             # Solution pH during SBF immersion
├── biological_response.csv        # Cell-viability assay results
└── sem_metadata.csv               # SEM morphology descriptions (images in source paper)
```

### Raw Data

Primary experimental observations:

- Initial phase composition (XRD-quantified) vs sintering temperature
- SBF phase evolution (XRD-quantified) vs immersion time
- 1100 °C degradation summary

### Processed Data

Analysis-ready datasets:

- Kinetic Blueprint Master Dataset
- Machine-learning dataset (`awgc_ml_dataset.csv`)
- pH evolution / transport kinetics / model results / feature importance
- Bioactivity interpretation summary

## Data Corrections (2026-08)

During reproducibility validation the following transcription errors were corrected:

| File | Correction |
|------|------------|
| `raw/initial_phase_composition.csv` | 700 °C row summed to 104.14 %; corrected to the canonical values reported in the master dataset (52.20 / 4.00 / 35.80 / 8.00, sum = 100.00 %). |
| `raw/sbf_phase_evolution.csv` | 900 °C day-3 row summed to 99.76 %; proportionally renormalized to 100.00 %. |
| `kinetic_blueprint_master.csv` | `Final_pH_21d` @ 700 °C set to 8.35, matching the day-21 record in `pH_time_series.csv`. |
| `biological_response.csv` | `ISO_10993_Status` values replaced with the standard ISO 10993-5 categories (`Non-Cytotoxic` / `Cytotoxic (<70%)`). |

## Scientific Workflow

Thermal Processing
↓
Crystallization Pathways
↓
Phase Architecture
↓
Microstructure
↓
Transport Behavior
↓
Microenvironment Evolution
↓
Biological Response
↓
Deterministic Materials Design
