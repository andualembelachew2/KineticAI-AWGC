# Data

This directory contains the experimental and processed datasets supporting the KineticAI-AWGC platform and the Kinetic Blueprint framework.

The datasets span the complete materials-design workflow from raw characterization data to biological response.

---

## Directory Structure

```text
data/
├── raw/
│   ├── xrd_patterns.csv
│   └── sem_images/
│
├── processed/
│   ├── kinetic_blueprint_master.csv
│   ├── pH_time_series.csv
│   ├── biological_response.csv
│   └── sem_metadata.csv
```

---

## Raw Data

The raw-data layer contains primary experimental observations.

### XRD Dataset

Purpose:

- Crystallization analysis
- Phase identification
- Phase-evolution studies

### SEM Image Archive

Purpose:

- Microstructural characterization
- Surface-degradation analysis
- Mineral-layer evaluation

---

## Processed Data

The processed-data layer contains analysis-ready datasets derived from experimental measurements.

### Kinetic Blueprint Master Dataset

Integrated dataset linking:

- Thermal processing
- Phase architecture
- Network connectivity
- Transport behavior

### pH Time-Series Dataset

Captures microenvironment evolution during SBF immersion.

### Biological Response Dataset

Contains cell-viability measurements and ISO 10993 interpretations.

### SEM Metadata Dataset

Provides structured descriptions of observed microstructural features.

---

## Scientific Workflow

The datasets collectively support the Kinetic Blueprint framework:

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
