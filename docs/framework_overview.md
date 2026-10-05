## 🧪 Kinetic Blueprint: Computational Engine

> **Programming ion-release kinetics in apatite-wollastonite glass-ceramics (AWGC).**
> A forward-simulation and analysis toolkit that links sintering temperature → dissolution kinetics → ion-release trajectory → biological safety window.

**Part of the [KineticAI-AWGC](https://github.com/) framework** · Author: Dr. Andualem Belachew Workie · License: MIT · DOI: [10.5281/zenodo.21759552](https://doi.org/10.5281/zenodo.21759552)

---

### What it does

| Module | Purpose |
|---|---|
| `CeramicParameters` | Material descriptor: sintering temperature, reactive amorphous fraction α, intrinsic dissolution rate, Qⁿ connectivity, porosity, strut radius, density |
| `MovingBoundaryDissolutionSolver` | 1D moving-boundary reaction-diffusion-advection solver for strut dissolution (explicit finite differences) |
| `KineticBlueprintAnalyzer` | Dimensionless regime mapping (Da, Pe), Korsmeyer-Peppas fit (k, n, R²), trajectory descriptors (τ, Σ₂₈) |
| `RegenerativeTargetZone` | Checks whether Si, Ca and pH trajectories remain inside a therapeutic, sub-cytotoxic window |
| `generate_framework_figure` | Four-panel publication figure (SVG + 600 DPI PNG) |

---

### Governing model

**Mass conservation (Si and Ca):**

$$\frac{\partial C}{\partial t} + u\,\frac{\partial C}{\partial x} = \frac{\partial}{\partial x}\!\left(D_{\mathrm{eff}}(\varepsilon)\,\frac{\partial C}{\partial x}\right) + S(x,t) - R(x,t)$$

**Moving boundary (porosity evolution):**

$$\frac{\partial \varepsilon}{\partial t} = k_{\mathrm{diss}}\,\alpha\,\beta(t)\,V_m\left(1 - \frac{C}{C_{\mathrm{sat}}}\right)$$

**Closures used in the code**

- Specific surface area: β = 3(1 − ε) / r
- Effective diffusivity (Archie-type): D_eff = D₀ · ε^1.5
- Congruent release: Ca/Si = 3.0 (Ca source = 3 × Si source)
- Ca sink: HCA-type precipitation above 2.5 mM, rate = 0.15 · (C_Ca − 2.5)^1.5
- Numerics: central differences for diffusion, upwind for advection; zero-flux at the strut wall, zero-gradient outflow at the pore exit

---

### Regime map (Damköhler number)

| Region | Condition | Interpretation |
|---|---|---|
| **I** | Da > 2 | Reactive burst: dissolution outpaces transport |
| **II** | 0.5 ≤ Da ≤ 2 | Balanced transport and reaction |
| **III** | Da < 0.5 | Transport-limited: slow, sustained release |

Da = (k_diss · α · β₀ · L²) / (D_eff · C₀) and Pe = (U · L) / D_eff

---

### Kinetic and trajectory descriptors

- **Korsmeyer-Peppas:** M_t / M_∞ = k · tⁿ, fitted on the first ~60% of mass loss, returning *k*, *n* and *R²*
- **Σ₂₈:** cumulative 28-day dose, ∫ C(t) dt (mM·day)
- **τ:** half-dose arrival time, the day when cumulative dose reaches 50% of Σ₂₈

---

### Regenerative Target Zone (RTZ)

| Variable | Admissible range |
|---|---|
| Silicon [Si] | 0.2 – 1.5 mM |
| Calcium [Ca] | 1.0 – 5.0 mM |
| pH | 7.35 – 7.85 |

A trajectory is **admissible** when at least **85%** of time points satisfy all three bounds (pre-registered tolerance).

---

### Built-in test materials

| Label | Sintering T | α (amorphous) | k_diss,0 (mol m⁻² day⁻¹) | Qⁿ | Porosity ε₀ | Density (g cm⁻³) |
|---|---|---|---|---|---|---|
| `700C` | 700 °C | 0.522 | 0.0471 | 1.85 | 0.35 | 2.02 |
| `900C` | 900 °C | 0.360 | 0.0185 | 2.40 | 0.28 | 2.61 |
| `1100C` | 1100 °C | 0.226 | 0.00455 | 3.20 | 0.18 | 2.78 |

All three use a 150 µm strut radius and a 28-day simulation window.

---

### Quick start

```bash
pip install numpy scipy matplotlib
python src/kinetic_blueprint.py
```

**Console output per material:** regime, (Da, Pe), Korsmeyer-Peppas (n, k, R²), (τ, Σ₂₈) and RTZ pass/fail with % in-zone.

**Figures** are saved to `figures/exports/`:

| Panel | Content |
|---|---|
| (a) | Cumulative mass loss and exponent *n* |
| (b) | Microenvironmental pH vs. the RTZ buffer and alkaline-shock bands |
| (c) | Si vs. Ca release against the 3:1 congruent line |
| (d) | (τ, Σ₂₈) trajectory-space map labelled with Da |

---

### Use it on your own material

```python
from src.kinetic_blueprint import (
    CeramicParameters, MovingBoundaryDissolutionSolver,
    KineticBlueprintAnalyzer, RegenerativeTargetZone,
)

mat = CeramicParameters(
    name="custom", temp_c=800.0, alpha=0.45, k_diss_0=0.03,
    q_n_connectivity=2.1, initial_porosity=0.30,
    strut_radius_um=150.0, bulk_density_g_cm3=2.3,
)

sim = MovingBoundaryDissolutionSolver(mat, t_max_days=28.0).run_simulation()
da, pe, regime = KineticBlueprintAnalyzer.compute_dimensionless_numbers(mat)
k, n, r2 = KineticBlueprintAnalyzer.fit_korsmeyer_peppas(
    sim["time_days"], sim["cumulative_mass_loss"])
tau, sigma28 = KineticBlueprintAnalyzer.compute_trajectory_descriptors(
    sim["time_days"], sim["c_si_effluent"])
rtz = RegenerativeTargetZone().check_admissibility(
    sim["time_days"], sim["c_si_effluent"], sim["c_ca_effluent"], sim["ph_effluent"])
```

---

### Citation

If you use this engine, please cite the Zenodo archive: **doi:10.5281/zenodo.21759552**
