# KineticAI-AWGC

**Open computational infrastructure for studying processing-structure-property relationships in spray-pyrolyzed apatite-wollastonite glass-ceramics.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21759552.svg)](https://doi.org/10.5281/zenodo.21759552)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Contents

- [About](#about)
- [The Kinetic Blueprint Framework](#the-kinetic-blueprint-framework)
- [Highlights](#highlights)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Reproducibility and Validation](#reproducibility-and-validation)
- [Publications](#publications)
- [Citation](#citation)
- [Author and Contact](#author-and-contact)
- [License](#license)

## About

KineticAI-AWGC combines experimental datasets, kinetic analysis, and machine learning to study apatite-wollastonite glass-ceramics (AWGCs), a bioactive materials family relevant to bone-regeneration research.

The repository supports the **Kinetic Blueprint Framework**, which organizes material performance as a connected chain:

```text
Thermal processing -> Crystallization pathways -> Phase architecture
    -> Microstructure -> Transport behavior -> Microenvironment evolution
    -> Biological response
```

The project is led by [Dr. Andualem](https://github.com/andualembelachew2). Research context and related publications are documented in [docs/publications.md](docs/publications.md).

## The Kinetic Blueprint Framework

![Kinetic Blueprint Framework](figures/kinetic_blueprint_framework.png)

The framework connects thermal processing to phase evolution, transport behavior, and biological response. The repository contains both the scientific documentation and computational assets used to investigate those relationships.

## Highlights

- Experimental and processed datasets for phase composition, degradation, transport, and biological response.
- Ten Jupyter notebooks covering the documented analysis workflow.
- Reusable Python modules for data preparation, baseline modeling, evaluation metrics, and visualization.
- Transport-model results and scientific summaries in [results](results/).
- A persistent research release through [Zenodo](https://doi.org/10.5281/zenodo.21759552).

## Installation

The source scripts are written for Python 3.9. Create an isolated environment, then install the dependencies:

```bash
git clone https://github.com/andualembelachew2/KineticAI-AWGC.git
cd KineticAI-AWGC

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The dependencies are listed in [requirements.txt](requirements.txt). The repository currently provides package names rather than a locked environment, so exact numerical reproduction may vary across dependency versions.

## Usage

### Build the machine-learning dataset

This reads [data/raw/initial_phase_composition.csv](data/raw/initial_phase_composition.csv) and [data/raw/sbf_phase_evolution.csv](data/raw/sbf_phase_evolution.csv), merges them by temperature, creates engineered phase features, and writes [data/processed/awgc_ml_dataset.csv](data/processed/awgc_ml_dataset.csv).

```bash
python src/data_processing.py
```

### Train baseline models

The modeling script loads the processed dataset and prints MAE, MSE, and R2 metrics for linear regression and random forest regression. It does not write model files or metric tables.

```bash
python src/models.py
```

### Generate figures

The visualization script reads the two raw phase datasets and saves three PNG files under [figures](figures/):

```bash
python src/visualization.py
```

### Explore the notebooks

Open the notebook directory with Jupyter, then follow the numbered workflow from [01_data_cleaning.ipynb](notebooks/01_data_cleaning.ipynb) through [10_phase_evolution_analysis.ipynb](notebooks/10_phase_evolution_analysis.ipynb):

```bash
jupyter notebook notebooks
```

The notebook descriptions and intended order are maintained in [notebooks/README.md](notebooks/README.md).

## Architecture

The executable source layer is intentionally small and file-oriented:

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
src/models.py -> metrics printed to the terminal

data/raw/*.csv -> src/visualization.py -> figures/*.png
```

- [src/data_processing.py](src/data_processing.py) loads the raw phase datasets, engineers features, and creates the processed ML dataset.
- [src/models.py](src/models.py) trains linear regression and random forest baseline models using a reproducible random train/test split.
- [src/metrics.py](src/metrics.py) provides reusable metric and evaluation-table helpers.
- [src/visualization.py](src/visualization.py) generates phase-composition and simulated-body-fluid evolution plots.
- [notebooks](notebooks/) contain the broader exploratory and scientific analysis workflow; [docs](docs/) explains the framework, datasets, and research context.

## Repository Structure

```text
KineticAI-AWGC/
├── data/                # Raw and processed experimental datasets
├── notebooks/           # Numbered Jupyter analysis workflow (01 through 10)
├── src/                 # Data processing, models, metrics, and visualization
├── docs/                # Framework, dataset, validation, and publication notes
├── results/             # Markdown summaries of analysis results
├── figures/             # Framework and generated figures
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT license
└── README.md            # Project overview and usage guide
```

More detailed indexes are available in [data/README.md](data/README.md), [docs/README.md](docs/README.md), [figures/README.md](figures/README.md), and [src/README.md](src/README.md).

## Reproducibility and Validation

The repository includes committed notebooks, source code, input data, generated figures, and result summaries. The current command-line source pipeline is reproducible from repository-relative paths, but dependencies are not pinned and the model evaluation currently uses a random train/test split. Claims about leave-one-temperature-out validation should not be made until that protocol is implemented and its results are documented.

The existing transport-model summary is available in [docs/model_validation.md](docs/model_validation.md). It reports Korsmeyer-Peppas fits for the 700 C and 1100 C samples.

## Publications

See [docs/publications.md](docs/publications.md) for the peer-reviewed research associated with this repository.

## Citation

Please cite the repository release through its Zenodo record:

```text
KineticAI-AWGC. Zenodo. https://doi.org/10.5281/zenodo.21759552
```

## Author and Contact

**Dr. Andualem Belachew Workie**

- GitHub: [andualembelachew2](https://github.com/andualembelachew2)
- ORCID: [0000-0003-3162-4257](https://orcid.org/0000-0003-3162-4257)

For project questions, please use the repository's GitHub issue tracker.

## License

This project is available under the [MIT License](LICENSE).
