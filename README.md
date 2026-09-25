# Spatiotemporal Trajectory Engineering in Bioactive Silicate Ceramics

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](requirements.txt)
[![Tests](https://img.shields.io/badge/pytest-6%20passing-0A9EDC?logo=pytest&logoColor=white)](tests/)
[![License](https://img.shields.io/badge/License-MIT-2EA44F.svg)](LICENSE)
[![Moving-boundary PDE](https://img.shields.io/badge/model-moving--boundary%20PDE-6B4FA8)](docs/theory/02_moving_boundary_pde.md)
[![PINN/SciML](https://img.shields.io/badge/method-PINN%20%2F%20SciML-A91D33)](docs/theory/05_sciml_bayesian_pipeline.md)
[![ChemRxiv DOI](https://img.shields.io/badge/ChemRxiv-DOI%20not%20assigned-lightgrey)](https://chemrxiv.org/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21759552-1F5AA8)](https://doi.org/10.5281/zenodo.21759552)

## Scientific overview

Bioactive silicate ceramics are commonly compared through static composition, porosity, or endpoint bioactivity measurements. This repository formulates a different question: can chemistry and architecture be designed as an open-loop dynamic program for the evolving microenvironment?

The framework couples solid-state speciation, moving-boundary dissolution, dynamic pore transport, Damkohler--Peclet regime analysis, and a continuous regenerative target zone (RTZ). The object of optimization is therefore the trajectory

$$
\text{network chemistry}\rightarrow\text{ion release}\rightarrow\text{transport}\rightarrow\text{pH and supersaturation}\rightarrow\text{mineralization}.
$$

| Design paradigm | Primary object | Typical limitation |
|---|---|---|
| Static optimization | A composition or endpoint property | Misses temporal overshoot and passivation |
| Stimuli-responsive material | A response triggered by an external cue | Often requires a separate activation event or controller |
| Spatiotemporal trajectory engineering | The complete chemistry--transport path through an admissibility tube | Requires coupled models and time-resolved validation |

## Research program and background

KineticAI-AWGC is an open computational research platform for predictive materials design through physics-informed modeling, kinetic analysis, multiscale characterization, and data-driven materials engineering. It was developed around apatite-wollastonite glass-ceramics, a bioactive materials family relevant to bone-regeneration research, and connects experimental observations with mechanistic processing--structure--property relationships.

The broader Kinetic Blueprint Framework follows the material system from synthesis to biological response:

```text
Thermal processing -> Crystallization pathways -> Phase architecture
  -> Microstructure -> Transport behavior -> Microenvironment evolution
  -> Biological response -> Predictive materials design
```

The computational principles are applicable to materials systems involving structure evolution, transport phenomena, reaction kinetics, property evolution, and data-driven design.

## Research assets

The repository contains reproducible assets derived from experimental studies and their computational interpretation:

- **Experimental datasets:** phase composition, density evolution, degradation, transport kinetics, pH evolution, biological response, and raw XRD patterns.
- **Computational workflows:** XRD pattern analysis, phase evolution analysis, transport-model validation, and biological-response interpretation.
- **Scientific outputs:** parameter identification, transport-regime classification, crystallization evolution analysis, and trajectory-engineering figures.

The original numbered workflow remains available in [notebooks/README.md](notebooks/README.md), from [01_data_cleaning.ipynb](notebooks/01_data_cleaning.ipynb) through [10_phase_evolution_analysis.ipynb](notebooks/10_phase_evolution_analysis.ipynb). The two trajectory-engineering demonstrations are linked below.

The exact historical portfolio README is preserved in [docs/archive/README_legacy_full.md](docs/archive/README_legacy_full.md). Historical visual assets recovered from Git are catalogued with their source commits in [docs/assets/legacy_figures/MANIFEST.tsv](docs/assets/legacy_figures/MANIFEST.tsv).

### Legacy research figures

The original Kinetic Blueprint framework diagram remains available alongside the modern trajectory-engineering gallery:

<p align="center">
  <img src="docs/assets/legacy_figures/figures__kinetic_blueprint_framework.png" alt="Legacy Kinetic Blueprint Framework" width="85%"/>
</p>

Additional recovered figures are preserved as direct assets: [phase evolution](docs/assets/legacy_figures/figures__characterization__xrd_phase_evolution.png), [feature importance](docs/assets/legacy_figures/figures__feature_importance.png), [hydroxyapatite gain](docs/assets/legacy_figures/figures__hydroxyapatite_gain_day21.png), [initial phase composition](docs/assets/legacy_figures/figures__initial_phase_composition.png), [mass-loss profiles](docs/assets/legacy_figures/figures__mass_loss_profiles.png), [predicted versus experimental phases](docs/assets/legacy_figures/figures__predicted_vs_experimental_phase_fractions.png), [SBF hydroxyapatite evolution](docs/assets/legacy_figures/figures__sbf_hydroxyapatite_evolution.png), and [SBF wollastonite evolution](docs/assets/legacy_figures/figures__sbf_wollastonite_evolution.png).

## Visual architecture gallery

<p align="center">
  <img src="figures/exports/fig1_chemical_trajectory.svg" alt="Chemical trajectory families" width="85%"/>
</p>

<p align="center">
  <img src="figures/exports/fig2_moving_boundary_erosion.svg" alt="Moving-boundary strut erosion and dynamic transport" width="85%"/>
</p>

<p align="center">
  <img src="figures/exports/fig3_regime_map.svg" alt="Damkohler-Peclet regime map" width="75%"/>
</p>

<p align="center">
  <img src="figures/exports/fig4_rtz_tube.svg" alt="Continuous regenerative target zone tube" width="85%"/>
</p>

## Governing equations

The coupled concentration field is modeled by

$$
\frac{\partial C_i}{\partial t}+\nabla\cdot(\mathbf u C_i)
=\nabla\cdot\left(D_{\mathrm{eff}}(t)\nabla C_i\right)+S_i-R_i.
$$

Dissolution changes the accessible pore volume according to

$$
\frac{\partial\varepsilon}{\partial t}
=k_{\mathrm{diss}}^{\circ}\alpha\beta\bar V_m,
\qquad
\beta(t)=\frac{3[1-\varepsilon(t)]}{r_s(t)}.
$$

The dimensionless regime coordinates are

$$
\mathrm{Da}=\frac{k_{\mathrm{diss}}^{\circ}\alpha\beta_0L^2}{D_{\mathrm{eff}} C_0},
\qquad
\mathrm{Pe}=\frac{UL}{D_{\mathrm{eff}}}.
$$

The balanced design corridor is $\mathrm{Da}\sim1$ and $\mathrm{Pe}\sim1$, where source generation and transport remain comparable.

## Quickstart

Install the scientific stack and run the validated example:

```bash
python -m pip install -r requirements.txt
python scripts/generate_figures.py
pytest -q
```

A minimal forward solve and RTZ check is:

```python
import numpy as np
from kineticai import admissible_tube, simulate_moving_boundary_1d

material = {"alpha": 0.38, "k_diss": 0.016}
result = simulate_moving_boundary_1d(
    tmax=28.0,
    dt=0.05,
    nx=96,
    alpha=material["alpha"],
    k_diss=material["k_diss"],
    diffusivity=0.004,
)

trajectory = np.column_stack([
    np.full(len(result["time_grid"]), 0.55),
    np.full(len(result["time_grid"]), 0.50),
    np.full(len(result["time_grid"]), 0.25),
    np.full(len(result["time_grid"]), 7.70),
    result["porosity_history"].mean(axis=1),
])
lower = np.tile([0.15, 0.10, 0.05, 7.35, 0.20], (len(trajectory), 1))
upper = np.tile([1.10, 1.00, 0.60, 8.20, 0.85], (len(trajectory), 1))
print("RTZ admissible:", admissible_tube(trajectory, lower, upper))
```

Interactive demonstrations are available in [notebooks/01_moving_boundary_simulation.ipynb](notebooks/01_moving_boundary_simulation.ipynb) and [notebooks/02_da_pe_regime_and_rtz_optimization.ipynb](notebooks/02_da_pe_regime_and_rtz_optimization.ipynb).

## Existing analysis workflow

The experimental-data pipeline can be reproduced from repository-relative paths:

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
src/models.py -> baseline metrics

data/raw/*.csv -> src/visualization.py -> figures/*.png
```

For the original analysis modules:

```bash
python src/data_processing.py
python src/models.py
python src/visualization.py
jupyter notebook notebooks
```

The current transport-model fits, including Korsmeyer--Peppas analysis for the 700 and 1100 C samples, are summarized in [docs/model_validation.md](docs/model_validation.md).

## Documentation

| Topic | Document |
|---|---|
| Solid-state chemistry and Arrhenius reactivity | [01_solid_state_chemistry.md](docs/theory/01_solid_state_chemistry.md) |
| Moving-boundary PDE and dynamic transport | [02_moving_boundary_pde.md](docs/theory/02_moving_boundary_pde.md) |
| Damkohler--Peclet scaling | [03_damkohler_peclet_scaling.md](docs/theory/03_damkohler_peclet_scaling.md) |
| Regenerative target zone | [04_regenerative_target_zone.md](docs/theory/04_regenerative_target_zone.md) |
| SciML and Bayesian validation | [05_sciml_bayesian_pipeline.md](docs/theory/05_sciml_bayesian_pipeline.md) |
| Manuscript source | [docs/trajectory_engineering.tex](docs/trajectory_engineering.tex) |
| Equation inventory | [docs/equations_reference.md](docs/equations_reference.md) |

## Publication collection

The publication record documents the progression from experimental bioactivity and cytotoxicity to phase programming, crystallization pathways, mass-transport kinetics, and surface reactivity:

- Workie, Ningsih, Yeh, and Shih, “An Investigation of In Vitro Bioactivities and Cytotoxicities of Spray Pyrolyzed Apatite--Wollastonite Glass-Ceramics,” *Crystals* (2023). [DOI](https://doi.org/10.3390/cryst13071049)
- Workie and Shih, “A Kinetic Blueprint for Bioactive Ceramics: Programming the Bio-interface through Thermal Processing,” *Ceramics International* (2025). [DOI](https://doi.org/10.1016/j.ceramint.2025.11.191)
- Workie and Taye, “Sequential Crystallization Pathways in Apatite--Wollastonite Glass-Ceramics via Spray Pyrolysis,” *RSC Advances* (2026). [DOI](https://doi.org/10.1039/d5ra08885b)
- Workie, Taye, Melchels, and Mamo, “Predictive Mass-Transport Kinetics in Phase-Programmed Silicate Glass-Ceramics for Controlled Microenvironmental Engineering,” *Biomaterials Science* (2026). [DOI](https://doi.org/10.1039/D6BM00997B)
- Taye, Workie, and Shih, “Rational Engineering of Mesoporous Bioactive Glass Surface Reactivity: NBO/BO Ratio Control via Synergistic Ag and Ce Co-Doping by Spray Pyrolysis,” *Ceramics International* (2026). [DOI](https://doi.org/10.1016/j.ceramint.2026.01.486)

The complete publication context and repository relevance notes are maintained in [docs/publications.md](docs/publications.md).

## Repository structure

```text
KineticAI-AWGC/
├── data/                # Raw and processed experimental datasets
├── notebooks/           # Numbered analysis workflow and demonstrations
├── src/                 # Data, chemistry, transport, and analysis modules
├── docs/                # Manuscript, theory, equations, and publications
├── results/             # Model-validation and trajectory summaries
├── figures/             # Generated PNG and SVG figures
├── scripts/             # Reproducible figure-generation utilities
├── tests/               # Physics and mathematical regression tests
├── requirements.txt     # Python dependencies
├── CITATION.cff
└── LICENSE
```

## Citation

```bibtex
@software{workie_kineticai_awgc,
  author  = {Workie, Andualem Belachew},
  title   = {KineticAI-AWGC: Spatiotemporal Trajectory Engineering in Bioactive Silicate Ceramics},
  year    = {2025},
  doi     = {10.5281/zenodo.21759552},
  url     = {https://github.com/andualembelachew2/KineticAI-AWGC}
}
```

The machine-readable citation record is [CITATION.cff](CITATION.cff). The project is released under the [MIT License](LICENSE).

<details>
<summary>Legacy portfolio (verbatim historical README)</summary>

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
    -> Biological response -> Predictive materials design
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

</details>
