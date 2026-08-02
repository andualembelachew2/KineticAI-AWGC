# KineticAI-AWGC

![Kinetic Blueprint Framework](figures/kinetic_blueprint_framework.png)

## Overview

**KineticAI-AWGC** is an open computational materials-science platform integrating experimental characterization, data analytics, machine learning, and mechanistic interpretation to investigate advanced glass-ceramic systems.

The platform serves as the computational foundation of the **Kinetic Blueprint Framework**, which links thermal processing, crystallization pathways, phase architecture, microstructure, transport behavior, microenvironment evolution, and biological response into a deterministic materials-design strategy.

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

## Documentation & Publications

Additional project documentation and publication information are available in the `docs/` directory:

- **Publications:** `docs/publications.md`
- **Project Summary:** `docs/project_summary.md`
- **Scientific Background:** `docs/scientific_background.md`
- **Framework Overview:** `docs/framework_overview.md`
- **Dataset Description:** `docs/dataset_description.md`
- **Materials Informatics Relevance:** `docs/materials_informatics_relevance.md`
