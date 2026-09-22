# KineticAI-AWGC

Open research repository documenting the analysis of processing-structure-performance 
relationships in apatite-wollastonite glass-ceramics (AWGC).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21759552.svg)](https://doi.org/10.5281/zenodo.21759552)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## About

This repository contains experimental datasets and Python analysis scripts 
supporting my published research on apatite-wollastonite glass-ceramics, 
a bioactive materials family for bone-regeneration applications. It documents 
the data processing, kinetic modeling, and statistical analysis behind my 
peer-reviewed publications, ensuring full reproducibility of the reported results.

## Kinetic Blueprint Analysis Workflow

![Kinetic Blueprint Workflow](figures/kinetic_blueprint_framework.png)

The analysis follows a processing-to-response chain:

    Thermal processing → Crystallization pathways → Phase architecture
        → Microstructure → Transport behavior → Microenvironment evolution
        → Biological response

## Contents

- Raw and processed experimental datasets (phase composition, degradation, transport, biological response)
- Ten Jupyter notebooks documenting the analysis steps in sequence
- Python scripts for data preparation, baseline modeling, and visualization
- Model fitting results in [results](results/)
- Archived release via [Zenodo](https://doi.org/10.5281/zenodo.21759552)

## Setup

Requires Python 3.9.

    git clone https://github.com/andualembelachew2/KineticAI-AWGC.git
    cd KineticAI-AWGC

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt

Note: Dependencies are listed as package names without version pinning; 
numerical results may vary slightly across versions.

## Usage

### Reproduce the processed dataset

    python src/data_processing.py

### Run baseline models

Reports MAE, MSE, and R² for linear regression and random forest:

    python src/models.py

### Generate figures

    python src/visualization.py

### Notebooks

Follow the numbered workflow from [01_data_cleaning.ipynb](notebooks/01_data_cleaning.ipynb) 
through [10_phase_evolution_analysis.ipynb](notebooks/10_phase_evolution_analysis.ipynb):

    jupyter notebook notebooks

See [notebooks/README.md](notebooks/README.md) for descriptions and intended order.

## Analysis Pipeline

    data/raw/*.csv
          |
          v
    src/data_processing.py
          |
          v
    data/processed/awgc_ml_dataset.csv
          |
          v
    src/models.py → metrics printed to terminal

    data/raw/*.csv → src/visualization.py → figures/*.png

## Repository Structure

    KineticAI-AWGC/
    ├── data/                # Raw and processed experimental datasets
    ├── notebooks/           # Numbered analysis notebooks (01–10)
    ├── src/                 # Data processing, models, metrics, visualization
    ├── docs/                # Analysis notes and research context
    ├── results/             # Model fitting results
    ├── figures/             # Generated figures
    ├── requirements.txt     # Python dependencies
    ├── LICENSE
    └── README.md

## Reproducibility Notes

The command-line pipeline is reproducible from repository-relative paths. 
Dependencies are not pinned, and model evaluation uses a random train/test split; 
results based on leave-one-temperature-out validation are not yet available. 
Current transport-model fitting, including Korsmeyer-Peppas fits for the 700 °C 
and 1100 °C samples, is documented in [docs/model_validation.md](docs/model_validation.md).

## Publications

See [docs/publications.md](docs/publications.md) for associated peer-reviewed work.

## Citation

    KineticAI-AWGC. Zenodo. https://doi.org/10.5281/zenodo.21759552

## Contact

- GitHub: [andualembelachew2](https://github.com/andualembelachew2)
- ORCID: [0000-0003-3162-4257](https://orcid.org/0000-0003-3162-4257)

For questions, please use the repository's issue tracker.

## License

MIT — see [LICENSE](LICENSE).
