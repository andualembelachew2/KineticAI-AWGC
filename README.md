# KineticAI-AWGC

Computational platform linking processing, structure, and performance in apatite-wollastonite glass-ceramics (AWGC).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21759552.svg)](https://doi.org/10.5281/zenodo.21759552)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Contents

- [About](#about)
- [Kinetic Blueprint Framework](#kinetic-blueprint-framework)
- [Highlights](#highlights)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Reproducibility](#reproducibility)
- [Publications](#publications)
- [Citation](#citation)
- [Contact](#contact)
- [License](#license)

## About

This repository combines experimental datasets, kinetic analysis, and machine learning methods to study apatite-wollastonite glass-ceramics, a bioactive materials family relevant to bone-regeneration research. It supports the Kinetic Blueprint Framework described below and documents the analysis workflow, datasets, and results behind the associated research.

## Kinetic Blueprint Framework

![Kinetic Blueprint Framework](figures/kinetic_blueprint_framework.png)

The framework structures material performance as a connected processing-to-response chain:

```text
Thermal processing -> Crystallization pathways -> Phase architecture
    -> Microstructure -> Transport behavior -> Microenvironment evolution
    -> Biological response
```

## Highlights

- Experimental and processed datasets for phase composition, degradation, transport, and biological response
- Ten Jupyter notebooks covering the full analysis workflow
- Python modules for data preparation, baseline modeling, evaluation, and visualization
- Transport-model summaries in [results](results/)
- Archived release via [Zenodo](https://doi.org/10.5281/zenodo.21759552)

## Installation

Requires Python 3.9.

```bash
git clone https://github.com/andualembelachew2/KineticAI-AWGC.git
cd KineticAI-AWGC

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Dependencies are listed in [requirements.txt](requirements.txt) as package names rather than a locked environment; exact numerical results may vary slightly across dependency versions.

## Usage

### Build the ML dataset

Merges [data/raw/initial_phase_composition.csv](data/raw/initial_phase_composition.csv) and [data/raw/sbf_phase_evolution.csv](data/raw/sbf_phase_evolution.csv) by temperature, engineers phase features, and writes [data/processed/awgc_ml_dataset.csv](data/processed/awgc_ml_dataset.csv):

```bash
python src/data_processing.py
```

### Train baseline models

Loads the processed dataset and reports MAE, MSE, and R² for linear regression and random forest regression (metrics printed to terminal only):

```bash
python src/models.py
```

### Generate figures

Reads the raw phase datasets and saves three PNG figures to [figures](figures/):

```bash
python src/visualization.py
```

### Notebooks

Follow the numbered workflow from [01_data_cleaning.ipynb](notebooks/01_data_cleaning.ipynb) through [10_phase_evolution_analysis.ipynb](notebooks/10_phase_evolution_analysis.ipynb):

```bash
jupyter notebook notebooks
```

See [notebooks/README.md](notebooks/README.md) for descriptions and intended order.

## Architecture

```text
data/raw/*.csv
      |
      v
src/data_processing.py
      |
      v
data/processed/awgc_ml_dataset.csv
      |
      v
src/models.py -> metrics printed to terminal

data/raw/*.csv -> src/visualization.py -> figures/*.png
```

- [src/data_processing.py](src/data_processing.py) — loads raw phase datasets, engineers features, builds the processed dataset
- [src/models.py](src/models.py) — trains linear regression and random forest baselines on a reproducible train/test split
- [src/metrics.py](src/metrics.py) — reusable metric and evaluation-table helpers
- [src/visualization.py](src/visualization.py) — generates phase-composition and SBF evolution plots
- [notebooks](notebooks/) — exploratory and scientific analysis workflow
- [docs](docs/) — framework, dataset, and research context

## Repository Structure

```text
KineticAI-AWGC/
├── data/                # Raw and processed experimental datasets
├── notebooks/           # Numbered analysis workflow (01–10)
├── src/                 # Data processing, models, metrics, visualization
├── docs/                # Framework, dataset, and validation notes
├── results/             # Markdown result summaries
├── figures/             # Framework and generated figures
├── requirements.txt     # Python dependencies
├── LICENSE
└── README.md
```

Further detail: [data/README.md](data/README.md), [docs/README.md](docs/README.md), [figures/README.md](figures/README.md), [src/README.md](src/README.md).

## Reproducibility

The command-line pipeline is reproducible from repository-relative paths. Dependencies are not pinned, and model evaluation currently uses a random train/test split; results based on leave-one-temperature-out validation are not yet available. The current transport-model summary, including Korsmeyer-Peppas fits for the 700 °C and 1100 °C samples, is documented in [docs/model_validation.md](docs/model_validation.md).

## Publications

See [docs/publications.md](docs/publications.md) for associated peer-reviewed work.

## Citation

```text
KineticAI-AWGC. Zenodo. https://doi.org/10.5281/zenodo.21759552
```

## Contact

- GitHub: [andualembelachew2](https://github.com/andualembelachew2)
- ORCID: [0000-0003-3162-4257](https://orcid.org/0000-0003-3162-4257)

For questions, please use the repository's issue tracker.

## License

MIT — see [LICENSE](LICENSE).
