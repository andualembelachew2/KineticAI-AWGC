# 📐 Mathematical Reference: Trajectory Engineering

[![Math: LaTeX / KaTeX](https://img.shields.io/badge/Math-KaTeX%20Compatible-blue.svg)](#)
[![Status: Reference Draft](https://img.shields.io/badge/Status-Validated-success.svg)](#)
[![Domain: Biomaterials & Transport](https://img.shields.io/badge/Field-Biochemical%20PDEs-purple.svg)](#)

> **Overview**: This document provides a mathematical reference for the forward models, transport equations, moving-boundary frameworks, and data-driven learning modules used across the repository.

---

## 📑 Table of Contents
1. [Chemical Trajectory Engineering](#1-chemical-trajectory-engineering)
2. [Architectural Transport Metrics](#2-architectural-transport-metrics)
3. [Moving-Boundary Coupled Framework](#3-moving-boundary-coupled-framework)
4. [Biological Validation & Real-Time Zone (RTZ) Tube](#4-biological-validation--real-time-zone-rtz-tube)
5. [Functional Data Analysis & Model Learning](#5-functional-data-analysis--model-learning)

---

## 1. Chemical Trajectory Engineering

### 1.1 Ion Exchange Reaction
Exchange of network-modifying cations with hydronium ions at the solid-liquid interface:
$$
\equiv\mathrm{Si\text{--}O^-M^+_{(s)}} + \mathrm{H_3O^+_{(aq)}} \rightleftharpoons \equiv\mathrm{Si\text{--}OH_{(s)}} + \mathrm{M^+_{(aq)}} + \mathrm{H_2O}
\tag{1.1}
$$

### 1.2 Siloxane Hydrolysis Reaction
Alkaline breakdown of the silica backbone network:
$$
\equiv\mathrm{Si\text{--}O\text{--}Si}\equiv + \;\mathrm{OH^-} \longrightarrow \equiv\mathrm{Si\text{--}OH} + \mathrm{^-O\text{--}Si}\equiv
\tag{1.2}
$$

### 1.3 Arrhenius-Weighted Network Reactivity
Reactivity $\alpha(Q^n; T)$ parameterized across species coordination states $Q^n$:
$$
\alpha(Q^n; T) = \sum_{n=0}^{4} f(Q^n)\,w_n(T), \qquad w_n(T) = \nu_n \exp\left(-\frac{E_{a,n}^{\mathrm{hydr}}}{R T}\right)
\tag{1.3}
$$

### 1.4 Dissolution Flux Boundary Condition
$$
k_{\mathrm{diss},i}^{\circ}(T) = \alpha(Q^n; T)\,k_0\,c_i(\text{network})
\tag{1.4}
$$

### 1.5 Gel-Layer Transport Flux
Interfacial mass flux across a dynamic silica-rich gel barrier layer of thickness $\delta_g(\mathbf{x},t)$:
$$
J_i(\mathbf{x},t) = \frac{D_g}{\delta_g(\mathbf{x},t)}\Big(C_{i,s}(\mathbf{x},t) - C_{i,b}(\mathbf{x},t)\Big)
\tag{1.5}
$$

### 1.6 Hydroxycarbonate Apatite (HCA) Saturation Index
Thermodynamic driving force for mineral precipitation:
$$
\mathrm{SI}_{\mathrm{HCA}} = \log_{10}\left(\frac{\mathit{IAP}}{K_{\mathrm{sp}}}\right), \qquad \mathit{IAP} = a_{\mathrm{Ca}}^9 \, a_{\mathrm{PO}_4}^6 \, a_{\mathrm{OH}}^2
\tag{1.6}
$$

### 1.7 Recession Law at Reaction Front
Moving boundary velocity driven by cumulative dissolution flux:
$$
\frac{\mathrm{d}r_s}{\mathrm{d}t} = -\frac{\bar{V}_m}{1-\varepsilon}\sum_{i} k_{\mathrm{diss},i}^{\circ}
\tag{1.7}
$$

### 1.8 Autocatalytic pH Feedback Loop
$$
\frac{\mathrm{d}[\mathrm{H}^+]}{\mathrm{d}t} = -\mathcal{A}_1 r_{\mathrm{ex}} + \mathcal{A}_2 k_{\mathrm{hydr}}[\mathrm{OH}^-]^m, \qquad k_{\mathrm{hydr}}\big([\mathrm{OH}^-]\big) = k_{\mathrm{hydr}}^0\Big(1 + \chi [\mathrm{OH}^-]^m\Big)
\tag{1.8}
$$

### 1.9 Surface Non-Bridging Oxygen (NBO/BO) Metric
$$
\left(\frac{\mathrm{NBO}}{\mathrm{BO}}\right)_{\!s}(t) = \frac{A_{\mathrm{NBO}}(t)}{A_{\mathrm{BO}}(t)} \propto \alpha\big(Q_{\mathrm{front}}^n(t)\big)
\tag{1.9}
$$

---

## 2. Architectural Transport Metrics

### 2.1 Static Effective Diffusivity
$$
D_{\mathrm{eff}} = D_0\,\frac{\varepsilon}{\kappa^2}\,g(\varepsilon)
\tag{2.1}
$$

### 2.2 Scaffold Specific Surface Scaling (Static)
Geometric scaling based on strut dimensions:
$$
\beta(\mathbf{x},0) = \frac{\mathrm{SA}}{V} \simeq \frac{n_{\mathrm{struts}}\,\pi\,d_{\mathrm{strut}}\,l_{\mathrm{strut}}}{V_{\mathrm{scaffold}}}
\tag{2.2}
$$

### 2.3 Dynamic Effective Diffusivity & Tortuosity Evolution
Time-dependent transport properties as porosity changes:
$$
D_{\mathrm{eff}}(\mathbf{x},t) = D_0\,\frac{\big[\varepsilon(\mathbf{x},t)\big]^{3/2}}{\big[\kappa(\mathbf{x},t)\big]^{2}}, \qquad \kappa(\mathbf{x},t) = \kappa_0\left(\frac{\varepsilon(\mathbf{x},0)}{\varepsilon(\mathbf{x},t)}\right)^{q}
\tag{2.3}
$$

---

## 3. Moving-Boundary Coupled Framework

### 3.1 Porosity Evolution Law
$$
\frac{\partial \varepsilon(\mathbf{x},t)}{\partial t} = k_{\mathrm{diss}}^{\circ}\,\alpha(Q^n,t)\,\beta(\mathbf{x},t)\,\bar{V}_m
\tag{3.1}
$$

### 3.2 Dynamic Geometric Factor (Cylindrical Struts)
$$
\beta(\mathbf{x},t) = \frac{\mathrm{SA}}{V} = \frac{3\big(1-\varepsilon(\mathbf{x},t)\big)}{r_s(\mathbf{x},t)}
\tag{3.2}
$$

### 3.3 Coupled Master Advection-Diffusion-Reaction Equation
Governs the spatial-temporal concentration field $C_i$:
$$
\frac{\partial C_i}{\partial t} + \underbrace{\nabla\cdot(\mathbf{u} C_i)}_{\text{Convection}} = \underbrace{\nabla\cdot\Big[D_{\mathrm{eff}}(\mathbf{x},t)\nabla C_i\Big]}_{\text{Diffusion}} + \underbrace{k_{\mathrm{diss},i}^{\circ}\,\alpha(Q^n,t)\,\beta(\mathbf{x},t)\,\phi(\mathrm{SI}_{\mathrm{HCA}})}_{\text{Dissolution Source}} - \underbrace{k_{\mathrm{precip},i}\,\gamma(\mathrm{SI}_{\mathrm{HCA}})}_{\text{Precipitation Sink}}
\tag{3.3}
$$

### 3.4 Reaction-Diffusion Modifiers
Non-linear switches governing crystallization and saturation dynamics:
$$
\phi(\mathrm{SI}_{\mathrm{HCA}}) = 1 - e^{-\mathrm{SI}_{\mathrm{HCA}}^2}, \qquad \gamma(\mathrm{SI}_{\mathrm{HCA}}) = \max\Big(0,\, 1 - e^{-(\mathrm{SI}_{\mathrm{HCA}} - \mathrm{SI}_{\mathrm{HCA}}^{\mathrm{crit}})}\Big)
\tag{3.4}
$$

### 3.5 Brinkman Porous Media Convection
Coupled momentum balance in evolving porous architectures:
$$
-\nabla p + \mu_{\mathrm{eff}}\nabla^2\mathbf{u} - \frac{\mu}{\kappa_m\big(\varepsilon(\mathbf{x},t)\big)}\mathbf{u} = \mathbf{0}, \qquad \nabla\cdot\mathbf{u} = 0
\tag{3.5}
$$

### 3.6 Dimensionless Transport Numbers
$$
\mathrm{Da} = \frac{k_{\mathrm{diss}}^{\circ}\,\alpha\,\beta\,L^2}{D_{\mathrm{eff}}} \quad (\text{Reaction / Diffusion}), \qquad \mathrm{Pe} = \frac{U L}{D_{\mathrm{eff}}} \quad (\text{Convection / Diffusion})
\tag{3.6}
$$

### 3.7 State-Vector ODE Form
Lumped-parameter formulation for surrogate and dynamical analysis:
$$
\mathbf{S}(\mathbf{x},t) = \Big[C_{\mathrm{Ca}},\, C_{\mathrm{Si}},\, C_{\mathrm{Mg}},\, \mathrm{pH},\, \varepsilon,\, D_{\mathrm{eff}}\Big]^T \in \mathbb{R}^6, \qquad \frac{\mathrm{d}\mathbf{S}}{\mathrm{d}t} = \mathcal{F}(\mathbf{S}, \boldsymbol{\theta})
\tag{3.7}
$$

---

## 4. Biological Validation & Real-Time Zone (RTZ) Tube

### 4.1 Continuous Admissibility Tube Definition
The functional domain preserving cytocompatibility and biological viability:
$$
\mathrm{RTZ}(t) = \left\{ \mathbf{S}(\cdot) \in C^0\big([0,T];\mathbb{R}^6\big) \;\middle|\; C_i^{\min}(t) \le C_i(t) \le C_i^{\max}(t),\; [\mathrm{H}^+](t) \in [\mathrm{H}^+]^{\mathrm{lo},\mathrm{hi}},\; \varepsilon(t) \ge \varepsilon^{\mathrm{perc}},\; \forall t \in (0,T] \right\}
\tag{4.1}
$$

### 4.2 Tube Distance Metric
$$
d_{\mathrm{RTZ}}(\mathbf{S}) = \max_{t\in[0,T]}\big\lVert\mathbf{S}(t) - \Pi_{\mathrm{RTZ}}(\mathbf{S}(t))\big\rVert_2, \qquad \mathbf{S}\in\mathrm{RTZ} \iff d_{\mathrm{RTZ}}(\mathbf{S}) \le \delta^*
\tag{4.2}
$$

### 4.3 Phase-Indexed Tube Boundaries
$$
C_i^{\min}(t) = \sum_k \Omega_k(t) C_{i,k}^{\min}, \qquad C_i^{\max}(t) = \sum_k \Omega_k(t) C_{i,k}^{\max}
\tag{4.3}
$$

---

## 5. Functional Data Analysis & Model Learning

### 5.1 Functional PCA Eigenequation & Scores
$$
\int_0^T \Sigma(s,t)\,\psi_k(t)\,\mathrm{d}t = \lambda_k\,\psi_k(s)
\tag{5.1}
$$
$$
\xi_k = \int_0^T \big(\mathbf{S}(t) - \mu(t)\big)\,\psi_k(t)\,\mathrm{d}t, \qquad \mathbf{S}(t) \approx \mu(t) + \sum_{k=1}^K \xi_k\,\psi_k(t)
\tag{5.2}
$$

### 5.2 Dynamic Time Warping (DTW) Cumulative Distance
$$
\mathcal{D}(i,j) = \min\Big\{\mathcal{D}(i-1,j),\, \mathcal{D}(i,j-1),\, \mathcal{D}(i-1,j-1)\Big\} + d(\mathbf{S}_i, \hat{\mathbf{S}}_j)
\tag{5.3}
$$

### 5.3 Neural Ordinary Differential Equations (NODE)
Forward rollout and adjoint sensitivity backpropagation:
$$
\frac{\mathrm{d}\mathbf{S}}{\mathrm{d}t} = F_{\boldsymbol{\theta}}(\mathbf{S}(t), t), \qquad \mathbf{S}(t_1) = \mathbf{S}(t_0) + \int_{t_0}^{t_1} F_{\boldsymbol{\theta}}\,\mathrm{d}t
\tag{5.4}
$$
$$
\frac{\mathrm{d}\mathbf{a}}{\mathrm{d}t} = -\mathbf{a}^T \frac{\partial F_{\boldsymbol{\theta}}}{\partial \mathbf{S}}, \qquad \frac{\mathrm{d}\mathcal{L}}{\mathrm{d}\boldsymbol{\theta}} = -\int_{t_1}^{t_0} \mathbf{a}^T \frac{\partial F_{\boldsymbol{\theta}}}{\partial \boldsymbol{\theta}}\,\mathrm{d}t
\tag{5.5}
$$

### 5.4 Physics-Informed Neural Network (PINN) Loss Formulation
$$
\mathcal{L}(\boldsymbol{\theta}) = \lambda_D \mathcal{L}_{\mathrm{data}} + \lambda_P \mathcal{L}_{\mathrm{PDE}} + \lambda_B \mathcal{L}_{\mathrm{BC/IC}}
\tag{5.6}
$$
$$
\mathcal{L}_{\mathrm{PDE}} = \left\lVert \frac{\partial \hat{\mathbf{S}}}{\partial t} + \nabla\cdot(\mathbf{u}\hat{\mathbf{S}}) - \nabla\cdot\big(D_{\mathrm{eff}}(\mathbf{x},t)\nabla\hat{\mathbf{S}}\big) - \hat{\mathcal{R}} \right\rVert^2
\tag{5.7}
$$

### 5.5 Uncertainty Quantification & Active Learning
Hamiltonian Monte Carlo (HMC) posterior sampling with Upper Confidence Bound (UCB) selection:
$$
H(\boldsymbol{\theta},\mathbf{p}) = U(\boldsymbol{\theta}) + K(\mathbf{p}), \qquad U(\boldsymbol{\theta}) = -\log p(\mathcal{D}\mid\boldsymbol{\theta}) - \log\pi(\boldsymbol{\theta})
\tag{5.8}
$$
$$
\Pr\big(\mathbf{S}(t)\in \mathrm{RTZ}(t)\mid\mathcal{D}\big) = \int \mathbf{1}_{\mathrm{RTZ}}\big(\hat{\mathbf{S}}_{\boldsymbol{\theta}}(t)\big)\,p(\boldsymbol{\theta}\mid\mathcal{D})\,\mathrm{d}\boldsymbol{\theta}
\tag{5.9}
$$
$$
\mathrm{UCB}(\mathbf{x}) = \mu_{\mathrm{GP}}(\mathbf{x}) + \beta_t\,\sigma_{\mathrm{GP}}(\mathbf{x})
\tag{5.10}
$$

---

## 📌 Implementation Notes
- **Renderer Compatibility**: Formatted strictly for GitHub's native MathJax/KaTeX backend.
- **Traceability**: Equation tags match section indices (`§X.Y`) for explicit cross-referencing across source code comments and test suites.
