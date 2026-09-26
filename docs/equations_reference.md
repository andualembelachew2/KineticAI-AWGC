# 📐 Mathematical Reference: Trajectory Engineering

[![Math: KaTeX Compatible](https://img.shields.io/badge/Math-KaTeX%20Compatible-blue.svg)](#)
[![Status: Validated](https://img.shields.io/badge/Status-Validated-success.svg)](#)
[![Field: Biochemical PDEs](https://img.shields.io/badge/Field-Biochemical%20PDEs-purple.svg)](#)

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
\equiv\mathrm{Si{-}O^-M^+_{(s)}} + \mathrm{H_3O^+_{(aq)}} \rightleftharpoons \equiv\mathrm{Si{-}OH_{(s)}} + \mathrm{M^+_{(aq)}} + \mathrm{H_2O}
$$

### 1.2 Siloxane Hydrolysis Reaction
Alkaline breakdown of the silica backbone network:

$$
\equiv\mathrm{Si{-}O{-}Si}\equiv \;+\; \mathrm{OH^-} \longrightarrow \equiv\mathrm{Si{-}OH} \;+\; \mathrm{^-O{-}Si}\equiv
$$

### 1.3 Arrhenius-Weighted Network Reactivity
Reactivity $\alpha(Q^n; T)$ parameterized across species coordination states $Q^n$:

$$
\alpha(Q^n; T) = \sum_{n=0}^{4} f(Q^n)\,w_n(T), \qquad w_n(T) = \nu_n \exp\left(-\frac{E_{a,n}^{\mathrm{hydr}}}{R T}\right)
$$

### 1.4 Dissolution Flux Boundary Condition
Intrinsic reaction flux scaling with active network concentration:

$$
k_{\mathrm{diss},i}^{\circ}(T) = \alpha(Q^n; T)\,k_0\,c_i(\text{network})
$$

### 1.5 Gel-Layer Transport Flux
Interfacial mass flux across a dynamic silica-rich gel barrier layer of thickness $\delta_g(\mathbf{x},t)$:

$$
J_i(\mathbf{x},t) = \frac{D_g}{\delta_g(\mathbf{x},t)}\left(C_{i,s}(\mathbf{x},t) - C_{i,b}(\mathbf{x},t)\right)
$$

### 1.6 Hydroxycarbonate Apatite (HCA) Saturation Index
Thermodynamic driving force for mineral precipitation:

$$
\mathrm{SI}_{\mathrm{HCA}} = \log_{10}\left(\frac{\mathit{IAP}}{K_{\mathrm{sp}}}\right), \qquad \mathit{IAP} = a_{\mathrm{Ca}}^9 \, a_{\mathrm{PO}_4}^6 \, a_{\mathrm{OH}}^2
$$

### 1.7 Recession Law at Reaction Front
Moving boundary velocity driven by cumulative dissolution flux:

$$
\frac{\mathrm{d}r_s}{\mathrm{d}t} = -\frac{\bar{V}_m}{1-\varepsilon}\sum_{i} k_{\mathrm{diss},i}^{\circ}
$$

### 1.8 Autocatalytic pH Feedback Loop
Coupled proton consumption and hydroxide-accelerated matrix degradation:

$$
\frac{\mathrm{d}[\mathrm{H}^+]}{\mathrm{d}t} = -\mathcal{A}_1 r_{\mathrm{ex}} + \mathcal{A}_2 k_{\mathrm{hydr}}[\mathrm{OH}^-]^m, \qquad k_{\mathrm{hydr}}([\mathrm{OH}^-]) = k_{\mathrm{hydr}}^0\left(1 + \chi [\mathrm{OH}^-]^m\right)
$$

### 1.9 Surface Non-Bridging Oxygen (NBO/BO) Metric
Spectroscopic structural ratio tracking active network dissolution:

$$
\left(\frac{\mathrm{NBO}}{\mathrm{BO}}\right)_{\!s}(t) = \frac{A_{\mathrm{NBO}}(t)}{A_{\mathrm{BO}}(t)} \propto \alpha\left(Q_{\mathrm{front}}^n(t)\right)
$$

---

## 2. Architectural Transport Metrics

### 2.1 Static Effective Diffusivity
Pore-scale diffusion accounting for porosity and baseline tortuosity:

$$
D_{\mathrm{eff}} = D_0\,\frac{\varepsilon}{\kappa^2}\,g(\varepsilon)
$$

### 2.2 Scaffold Specific Surface Scaling (Static)
Geometric scaling based on nominal strut dimensions:

$$
\beta(\mathbf{x},0) = \frac{\mathrm{SA}}{V} \simeq \frac{n_{\mathrm{struts}}\,\pi\,d_{\mathrm{strut}}\,l_{\mathrm{strut}}}{V_{\mathrm{scaffold}}}
$$

### 2.3 Dynamic Effective Diffusivity & Tortuosity Evolution
Time-dependent transport properties as porosity changes under dissolution:

$$
D_{\mathrm{eff}}(\mathbf{x},t) = D_0\,\frac{[\varepsilon(\mathbf{x},t)]^{3/2}}{[\kappa(\mathbf{x},t)]^2}, \qquad \kappa(\mathbf{x},t) = \kappa_0\left(\frac{\varepsilon(\mathbf{x},0)}{\varepsilon(\mathbf{x},t)}\right)^{q}
$$

---

## 3. Moving-Boundary Coupled Framework

### 3.1 Porosity Evolution Law
Local solid volume fraction loss rate:

$$
\frac{\partial \varepsilon(\mathbf{x},t)}{\partial t} = k_{\mathrm{diss}}^{\circ}\,\alpha(Q^n,t)\,\beta(\mathbf{x},t)\,\bar{V}_m
$$

### 3.2 Dynamic Geometric Factor (Cylindrical Struts)
Instantaneous specific surface area for eroding cylindrical struts:

$$
\beta(\mathbf{x},t) = \frac{\mathrm{SA}}{V} = \frac{3(1-\varepsilon(\mathbf{x},t))}{r_s(\mathbf{x},t)}
$$

### 3.3 Coupled Master Advection-Diffusion-Reaction Equation
Governs the spatial-temporal ionic concentration field $C_i$:

$$
\frac{\partial C_i}{\partial t} + \underbrace{\nabla\cdot(\mathbf{u} C_i)}_{\text{Convection}} = \underbrace{\nabla\cdot\left[D_{\mathrm{eff}}(\mathbf{x},t)\nabla C_i\right]}_{\text{Diffusion}} + \underbrace{k_{\mathrm{diss},i}^{\circ}\,\alpha(Q^n,t)\,\beta(\mathbf{x},t)\,\phi(\mathrm{SI}_{\mathrm{HCA}})}_{\text{Dissolution Source}} - \underbrace{k_{\mathrm{precip},i}\,\gamma(\mathrm{SI}_{\mathrm{HCA}})}_{\text{Precipitation Sink}}
$$

### 3.4 Reaction-Diffusion Modifiers
Non-linear switches governing crystallization and saturation dynamics:

$$
\phi(\mathrm{SI}_{\mathrm{HCA}}) = 1 - e^{-\mathrm{SI}_{\mathrm{HCA}}^2}, \qquad \gamma(\mathrm{SI}_{\mathrm{HCA}}) = \max\left(0,\, 1 - e^{-(\mathrm{SI}_{\mathrm{HCA}} - \mathrm{SI}_{\mathrm{HCA}}^{\mathrm{crit}})}\right)
$$

### 3.5 Brinkman Porous Media Convection
Coupled momentum balance in evolving porous architectures:

$$
-\nabla p + \mu_{\mathrm{eff}}\nabla^2\mathbf{u} - \frac{\mu}{\kappa_m(\varepsilon(\mathbf{x},t))}\mathbf{u} = \mathbf{0}, \qquad \nabla\cdot\mathbf{u} = 0
$$

### 3.6 Dimensionless Transport Numbers
Quantifying chemical versus architectural transport dominance:

$$
\mathrm{Da} = \frac{k_{\mathrm{diss}}^{\circ}\,\alpha\,\beta\,L^2}{D_{\mathrm{eff}}} \quad (\text{Reaction / Diffusion}), \qquad \mathrm{Pe} = \frac{U L}{D_{\mathrm{eff}}} \quad (\text{Convection / Diffusion})
$$

### 3.7 State-Vector ODE Form
Lumped-parameter formulation for surrogate dynamic analysis:

$$
\mathbf{S}(\mathbf{x},t) = \begin{bmatrix} C_{\mathrm{Ca}} & C_{\mathrm{Si}} & C_{\mathrm{Mg}} & \mathrm{pH} & \varepsilon & D_{\mathrm{eff}} \end{bmatrix}^T \in \mathbb{R}^6, \qquad \frac{\mathrm{d}\mathbf{S}}{\mathrm{d}t} = \mathcal{F}(\mathbf{S}, \boldsymbol{\theta})
$$

---

## 4. Biological Validation & Real-Time Zone (RTZ) Tube

 ## 4.1 Continuous Admissibility Tube Definition

The functional domain preserving cytocompatibility and biological viability:

$$
\mathrm{RTZ}(t) = \left\lbrace \mathbf{S}(\cdot) \in C^0([0,T];\mathbb{R}^6) ;\middle|; C_i^{\min}(t) \le C_i(t) \le C_i^{\max}(t),; \mathrm{H}^+ \in [\mathrm{H}^+]^{\mathrm{lo},\mathrm{hi}},; \varepsilon(t) \ge \varepsilon^{\mathrm{perc}},; \forall t \in (0,T] \right\rbrace
$$

### 4.2 Tube Distance Metric
Maximum functional Euclidean distance to the admissibility projection:

$$
d_{\mathrm{RTZ}}(\mathbf{S}) = \max_{t\in[0,T]}\left\lVert\mathbf{S}(t) - \Pi_{\mathrm{RTZ}}(\mathbf{S}(t))\right\rVert_2, \qquad \mathbf{S}\in\mathrm{RTZ} \iff d_{\mathrm{RTZ}}(\mathbf{S}) \le \delta^*
$$



### 4.3 Phase-Indexed Tube Boundaries
Convex combination of stage-specific physiological bounds:

$$
C_i^{\min}(t) = \sum_k \Omega_k(t) C_{i,k}^{\min}, \qquad C_i^{\max}(t) = \sum_k \Omega_k(t) C_{i,k}^{\max}
$$

---

## 5. Functional Data Analysis & Model Learning

### 5.1 Functional PCA Eigenequation & Scores
Continuous orthogonal decomposition of trajectory variance:

$$
\int_0^T \Sigma(s,t)\,\psi_k(t)\,\mathrm{d}t = \lambda_k\,\psi_k(s)
$$

$$
\xi_k = \int_0^T \left(\mathbf{S}(t) - \mu(t)\right)\psi_k(t)\,\mathrm{d}t, \qquad \mathbf{S}(t) \approx \mu(t) + \sum_{k=1}^K \xi_k\,\psi_k(t)
$$

### 5.2 Dynamic Time Warping (DTW) Cumulative Distance
Alignment cost for non-linear temporal dynamics:

$$
\mathcal{D}(i,j) = \min\left[ \mathcal{D}(i-1,j),\, \mathcal{D}(i,j-1),\, \mathcal{D}(i-1,j-1) \right] + d(\mathbf{S}_i, \hat{\mathbf{S}}_j)
$$

### 5.3 Neural Ordinary Differential Equations (NODE)
Forward continuous rollout and backward adjoint sensitivity equations:

$$
\frac{\mathrm{d}\mathbf{S}}{\mathrm{d}t} = F_{\boldsymbol{\theta}}(\mathbf{S}(t), t), \qquad \mathbf{S}(t_1) = \mathbf{S}(t_0) + \int_{t_0}^{t_1} F_{\boldsymbol{\theta}}\,\mathrm{d}t
$$

$$
\frac{\mathrm{d}\mathbf{a}}{\mathrm{d}t} = -\mathbf{a}^T \frac{\partial F_{\boldsymbol{\theta}}}{\partial \mathbf{S}}, \qquad \frac{\mathrm{d}\mathcal{L}}{\mathrm{d}\boldsymbol{\theta}} = -\int_{t_1}^{t_0} \mathbf{a}^T \frac{\partial F_{\boldsymbol{\theta}}}{\partial \boldsymbol{\theta}}\,\mathrm{d}t
$$

### 5.4 Physics-Informed Neural Network (PINN) Loss Formulation
Composite objective enforcing boundary values and residual PDE consistency:

$$
\mathcal{L}(\boldsymbol{\theta}) = \lambda_D \mathcal{L}_{\mathrm{data}} + \lambda_P \mathcal{L}_{\mathrm{PDE}} + \lambda_B \mathcal{L}_{\mathrm{BC/IC}}
$$

$$
\mathcal{L}_{\mathrm{PDE}} = \left\lVert \frac{\partial \hat{\mathbf{S}}}{\partial t} + \nabla\cdot(\mathbf{u}\hat{\mathbf{S}}) - \nabla\cdot\left(D_{\mathrm{eff}}(\mathbf{x},t)\nabla\hat{\mathbf{S}}\right) - \hat{\mathcal{R}} \right\rVert^2
$$

### 5.5 Uncertainty Quantification & Active Learning
Hamiltonian Monte Carlo (HMC) sampling and acquisition optimization:

$$
H(\boldsymbol{\theta},\mathbf{p}) = U(\boldsymbol{\theta}) + K(\mathbf{p}), \qquad U(\boldsymbol{\theta}) = -\log p(\mathcal{D}\mid\boldsymbol{\theta}) - \log\pi(\boldsymbol{\theta})
$$

$$
\Pr\left(\mathbf{S}(t)\in \mathrm{RTZ}(t)\mid\mathcal{D}\right) = \int \mathbf{1}_{\mathrm{RTZ}}\left(\hat{\mathbf{S}}_{\boldsymbol{\theta}}(t)\right) p(\boldsymbol{\theta}\mid\mathcal{D})\,\mathrm{d}\boldsymbol{\theta}
$$

$$
\mathrm{UCB}(\mathbf{x}) = \mu_{\mathrm{GP}}(\mathbf{x}) + \beta_t\,\sigma_{\mathrm{GP}}(\mathbf{x})
$$

---

## 📌 Implementation Notes
- **Renderer Compatibility**: Fully tested for GitHub's native KaTeX engine; uses Markdown-safe macro names (`\lbrace`, `\rbrace`, `\left[ ... \right]`) to prevent parser collisions.
- **Traceability**: Section numbers (`§X.Y`) correspond directly to model functions and test cases in the codebase.
