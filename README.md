Open Science Resources

- Zenodo Archive: https://doi.org/10.5281/zenodo.21759552

# KineticAI-AWGC

![Kinetic Blueprint Framework](figures/kinetic_blueprint_framework.png)

## Overview

KineticAI: An open computational research platform for predictive materials design through physics-informed modeling, kinetic analysis, multiscale characterization, and data-driven materials engineering.

The platform integrates experimental observations, mechanistic understanding, and computational workflows to establish predictive processing–structure–property relationships across complex materials systems.

## Research Context

While developed using bioactive glass-ceramic systems, the computational principles demonstrated in KineticAI-AWGC are broadly applicable to predictive materials research involving:

- Structure evolution
- Transport phenomena
- Reaction kinetics
- Property evolution
- Data-driven materials design
  
## Scientific Workflow

The framework follows a sequential pipeline to achieve deterministic design:

```text
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
```

## Repository Structure

```text
docs/        Scientific documentation
data/        Experimental and processed datasets
figures/     Framework and analysis figures
notebooks/   Analytical workflows
```
## Quick Start

Clone the repository:

```bash
git clone https://github.com/<username>/KineticAI-AWGC.git
cd KineticAI-AWGC
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter:

```bash
jupyter notebook
```

Recommended workflow:

1. Start with `07_xrd_pattern_analysis.ipynb`
2. Continue to `08_microstructure_analysis.ipynb`
3. Explore `02_exploratory_analysis.ipynb`
4. Review `05_microenvironment_evolution.ipynb`
5. Finish with `06_biological_response.ipynb`
## Datasets

The repository currently contains the following datasets within the `data/` directory:

- Kinetic Blueprint Master Dataset
- pH Time-Series Dataset
- Biological Response Dataset
- Raw XRD Pattern Dataset
- SEM Metadata Dataset
- SEM Image Archive
## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

Core dependencies:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
- jupyter

## Analytical Notebooks

The `notebooks/` directory contains analytical workflows broken down into the following stages:

- **01** Data Cleaning
- **02** Exploratory Analysis
- **03** Phase Prediction Model
- **04** Bioactivity Interpretation
- **05** Microenvironment Evolution
- **06** Biological Response
- **07** XRD Pattern Analysis
- **08** Microstructure Analysis

## Model Validation

The repository includes transport-model validation workflows based on experimentally measured mass attenuation data.

The Korsmeyer-Peppas model provided the highest goodness-of-fit (R² > 0.99) and revealed a transition from quasi-Fickian burst transport (700°C) to controlled anomalous transport (1100°C).

See:

- `docs/model_validation.md`
- `data/processed/transport_kinetics.csv`

## Reproducible Research

The repository contains reproducible computational workflows that transform raw experimental measurements into published analytical figures.

Example:

transport_kinetics.csv
        ↓
09_transport_model_validation.ipynb
        ↓
mass_loss_profiles.png
  
## Research Vision

KineticAI-AWGC serves as a demonstration platform for the Kinetic Blueprint Framework and contributes toward the broader goal of predictive computational materials research.

The long-term vision is to integrate experimental characterization, physics-informed modeling, quantitative analysis, and machine learning into reproducible frameworks capable of connecting processing history, structure evolution, and performance prediction across complex materials systems.

## Documentation & Publications

Additional project documentation and publication information are available in the `docs/` directory:

- **Publications:** `docs/publications.md`
- **Project Summary:** `docs/project_summary.md`
- **Scientific Background:** `docs/scientific_background.md`
- **Framework Overview:** `docs/framework_overview.md`
- **Dataset Description:** `docs/dataset_description.md`
- **Materials Informatics Relevance:** `docs/materials_informatics_relevance.md`
