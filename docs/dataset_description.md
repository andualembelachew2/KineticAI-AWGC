# Data Catalog

This document describes the datasets supporting the KineticAI-AWGC platform.

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
| Temperature_C | Sintering temperature |
| Amorphous_Percent | Residual amorphous phase content |
| ... | ... |

## Scientific Role

Supports analysis of processing–structure–transport relationships.

---

# Dataset 2 — pH Evolution Dataset

## Purpose

Tracks microenvironment evolution during SBF immersion.

## Location

```text
data/processed/ph_evolution.csv
```

## Variables

| Variable | Description |
|----------|-------------|
| Time_Days | Immersion time |
| Temperature_C | Processing temperature |
| pH_Value | Measured pH |

## Scientific Role

Links transport behavior to microenvironment regulation.

---

# Dataset 3 — Raw XRD Pattern Dataset

## Purpose

Provides primary crystallographic evidence of phase evolution.

## Location

```text
data/raw/xrd_patterns.csv
```

## Scientific Role

Supports crystallization and phase-fraction analysis.

---

# Dataset 4 — SEM Image Dataset

## Purpose

Provides microstructural evidence of morphology evolution when microscopy images are available.

## Location

```text
SEM image files are not currently included in this repository.
```

## Associated Metadata

```text
data/sem_metadata.csv
```

## Scientific Role

Supports interpretation of phase architecture and transport behavior.
