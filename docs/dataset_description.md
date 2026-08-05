# Data Catalog

This document describes the datasets supporting the KineticAI-AWGC platform.

All datasets are transcribed from the peer-reviewed studies listed in `docs/publications.md` (primarily Workie et al., *Crystals* 13(7):1049, 2023). Provenance notes and the corrections applied during validation are documented in `data/README.md`.

---

# Dataset 1 — Kinetic Blueprint Master Dataset

## Purpose

Integrates processing, phase architecture, transport behavior, and functional response into a single analytical dataset.

## Location

```text
data/kinetic_blueprint_master.csv
```

## Variables

| Variable | Description |
|----------|-------------|
| Temperature_C | Sintering temperature (700–1100 °C) |
| Amorphous_Percent | Residual amorphous phase content (%) |
| Wollastonite_Percent | Wollastonite phase fraction (%) |
| Hydroxyapatite_Percent | Hydroxyapatite phase fraction (%) |
| Whitlockite_Percent | Whitlockite phase fraction (%) |
| Bulk_Density_g_cm3 | Bulk density (g/cm³) |
| MassLoss_21d_Percent | Cumulative mass loss after 21 days SBF immersion (%) |
| Final_pH_21d | Solution pH after 21 days |
| Ca_Release_21d_mM / Si_Release_21d_mM | Cumulative Ca/Si release after 21 days (mM) |
| NBO_BO_Ratio | Network-connectivity descriptor |
| Kinetic_Exponent_n | Korsmeyer–Peppas exponent |
| Transport_Mechanism | Classified transport regime |

## Scientific Role

Supports analysis of processing–structure–transport relationships.

---

# Dataset 2 — pH Evolution Dataset

## Purpose

Tracks microenvironment evolution during SBF immersion.

## Location

```text
data/pH_time_series.csv
```

## Variables

| Variable | Description |
|----------|-------------|
| Time_Days | Immersion time (days) |
| Temperature_C | Processing temperature (°C) |
| pH_Value | Measured pH |
| Interfacial_Classification | Qualitative microenvironment label |

## Derived Copy

`data/processed/ph_evolution.csv` is a reformatted copy used by the results summaries.

## Scientific Role

Links transport behavior to microenvironment regulation.

---

# Dataset 3 — Initial & SBF Phase Composition

## Purpose

Provides the XRD-quantified phase architecture before and during SBF immersion.

## Location

```text
data/raw/initial_phase_composition.csv
data/raw/sbf_phase_evolution.csv
```

## Scientific Role

Primary structural data underpinning crystallization, transport, and bioactivity analyses.

## Scope Note

The raw diffraction spectra and SEM micrographs from which these values were quantified are large instrument files published with the source studies; this repository ships the quantified results, not the raw instrument files.

---

# Dataset 4 — Biological Response

## Purpose

Cell-viability assay results interpreted against ISO 10993-5 thresholds.

## Location

```text
data/biological_response.csv
```

## Scientific Role

Final functional layer of the Kinetic Blueprint framework.
