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
