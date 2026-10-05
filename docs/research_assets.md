# Computational Research Assets & Data Manifest

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21759552-1F5AA8)](https://doi.org/10.5281/zenodo.21759552)
[![Data Standard](https://img.shields.io/badge/FAIR-Compliant%20Data-2EA44F)](data/)
[![Pipeline](https://img.shields.io/badge/Pipeline-Verified-0A9EDC)](notebooks/)

This document catalogues the digitized experimental datasets, validation workflows, and computational summaries that operationalize published empirical findings into reproducible research assets within the **Kinetic Blueprint Framework**.

---

## Asset Catalog Overview

| Asset ID | Domain | Physical State Variables | Primary Data Files | Processing Notebook | Output Summary |
|---|---|---|---|---|---|
| **AST-01** | Phase Evolution | $W_{\text{Amorph}}$, $W_{\text{Woll}}$, $W_{\text{Whit}}$, $W_{\text{FA}}$, $\text{NBO/BO}$ | `data/processed/phase_composition.csv` | `notebooks/10_phase_evolution_analysis.ipynb` | `results/phase_evolution_summary.md` |
| **AST-02** | Consolidation | Bulk density ($\rho$), Relative density ($\%$) | `data/processed/density_evolution.csv` | — | `results/density_evolution_summary.md` |
| **AST-03** | Transport Kinetics | Rate constant $k$, Exponent $n$, Mass loss $M_t/M_\infty$ | `data/processed/transport_kinetics.csv`<br>`data/processed/korsmeyer_peppas_parameters.csv` | `notebooks/09_transport_model_validation.ipynb` | `results/transport_model_validation_summary.md` |
| **AST-04** | Microenvironment | Interfacial $\text{pH}(t)$, Ion fluxes $[\text{Ca}^{2+}], [\text{Si}^{4+}]$ | `data/processed/ph_evolution.csv` | — | `results/ph_evolution_summary.md` |

---

## Detailed Asset Specifications

### Asset 1 — Solid-State Phase Evolution & Network Connectivity
- **Physical Scope**: Quantifies the thermal transformation of spray-pyrolyzed amorphous precursor into crystalline pseudowollastonite ($\beta\text{-CaSiO}_3$), whitlockite ($\text{Ca}_3(\text{PO}_4)_2$), and fluorapatite ($\text{Ca}_5(\text{PO}_4)_3\text{F}$) across 700–1100 °C.
- **Key Parameters**:
  - Depletion of reactive amorphous fraction: $52.20\ \text{wt}\% \to 22.60\ \text{wt}\%$
  - Crystallization of wollastonite core: $4.00\ \text{wt}\% \to 21.67\ \text{wt}\%$
  - Network connectivity shift: $\text{NBO/BO}$ ratio decreases from $6.35$ to $2.10$
- **Associated Assets**:
  - `data/processed/phase_composition.csv`
  - `notebooks/10_phase_evolution_analysis.ipynb`
  - `results/phase_evolution_summary.md`

---

### Asset 2 — Matrix Densification & Structural Consolidation
- **Physical Scope**: Captures the viscous-sintering consolidation profile, mapping intergranular pore elimination to bulk skeletal density.
- **Key Parameters**:
  - Initial under-consolidated porous state ($700\ ^\circ\text{C}$): $\rho = 2.02\ \text{g/cm}^3$ (residual porosity: $32.7\%$)
  - Maximum consolidated skeletal limit ($1000\ ^\circ\text{C}$): $\rho = 2.80\ \text{g/cm}^3$ (residual porosity: $6.7\%$)
  - Sintering plateau ($1100\ ^\circ\text{C}$): $\rho = 2.78\ \text{g/cm}^3$
- **Associated Assets**:
  - `data/processed/density_evolution.csv`
  - `results/density_evolution_summary.md`

---

### Asset 3 — Transport Kinetics & Korsmeyer–Peppas Validation
- **Physical Scope**: Multi-model regression identifying the governing mass-attenuation law and classifying the operational transport regime across 21 days of SBF immersion.
- **Governing Equation**:
  $$\frac{M_t}{M_\infty} = k \cdot t^n$$
- **Key Parameters**:
  - **700 °C**: Quasi-Fickian burst release ($n = 0.25$, $k = 4.71 \times 10^{-2}\ \text{day}^{-n}$, $R^2 = 0.993$)
  - **800–1000 °C**: Anomalous non-Fickian transport ($n = 0.38 - 0.49$)
  - **1100 °C**: Diffusion-governed transport ($n = 0.58$, $k = 4.55 \times 10^{-3}\ \text{day}^{-n}$, $R^2 = 0.997$)
- **Associated Assets**:
  - `data/processed/transport_kinetics.csv`
  - `data/processed/korsmeyer_peppas_parameters.csv`
  - `notebooks/09_transport_model_validation.ipynb`
  - `results/transport_model_validation_summary.md`

---

### Asset 4 — Microenvironmental Dynamics & Elemental Stoichiometry
- **Physical Scope**: Time-resolved monitoring of interfacial proton exchange ($\Delta\text{pH}$) and stoichiometric multi-ion release balance.
- **Key Parameters**:
  - **Congruent Dissolution Ratio**: Initial matrix dissolution preserves a strict stoichiometric release ratio of $[\text{Ca}^{2+}]/[\text{Si}^{4+}] \approx 3.00 \pm 0.02$.
  - **Alkaline Burst**: $700\ ^\circ\text{C}$ induces an early pH spike ($\text{pH} > 8.38$), entering the cytotoxic regime ($\text{viability} < 70\%$ at extract doses $\ge 80\%$).
  - **Homeostatic Buffering**: $1100\ ^\circ\text{C}$ stabilizes local proton exchange within the viable osteoblast envelope ($\text{pH} = 7.40 - 7.82$), promoting cellular proliferation up to $\sim 300\%$.
- **Associated Assets**:
  - `data/processed/ph_evolution.csv`
  - `results/ph_evolution_summary.md`

---

## The Kinetic Blueprint Causal Pipeline

These assets collectively form the closed-loop empirical foundation of the Kinetic Blueprint:

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. THERMAL PROCESSING SCHEDULE (700 °C – 1100 °C)           │
└──────────────────────────────┬──────────────────────────────┘
                               │ governs (Asset 1 & 2)
┌──────────────────────────────▼──────────────────────────────┐
│ 2. PHASE ARCHITECTURE & MATRIX DENSITY                      │
│    • Qⁿ network speciation · NBO/BO (6.35 ──► 2.10)         │
│    • Bulk consolidation ρ (2.02 ──► 2.80 g/cm³)             │
└──────────────────────────────┬──────────────────────────────┘
                               │ parameterizes (Asset 3)
┌──────────────────────────────▼──────────────────────────────┐
│ 3. TRANSPORT BEHAVIOR & KINETIC CLOCK                       │
│    • Rate constant k (10-fold attenuation)                  │
│    • Korsmeyer–Peppas exponent n (0.25 ──► 0.58)            │
└──────────────────────────────┬──────────────────────────────┘
                               │ drives (Asset 4)
┌──────────────────────────────▼──────────────────────────────┐
│ 4. MICROENVIRONMENTAL REGULATION                            │
│    • Congruent matrix release: [Ca²⁺]/[Si⁴⁺] ≈ 3.00         │
│    • Interfacial pH trajectory (8.38 ──► 7.82)              │
└──────────────────────────────┬──────────────────────────────┘
                               │ directs
┌──────────────────────────────▼──────────────────────────────┐
│ 5. REGENERATIVE OUTCOME & BIOCOMPATIBILITY                  │
│    • ISO 10993-5 non-cytotoxicity compliance                │
│    • Targeted osteogenic mineralization                     │
└─────────────────────────────────────────────────────────────┘
