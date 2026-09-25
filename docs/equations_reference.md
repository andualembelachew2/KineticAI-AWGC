# Equation Reference for Trajectory Engineering

This document collects the primary labeled equations from the manuscript in order of appearance. It is not a replacement for the original LaTeX source; it is a quick reference for the key mathematical statements used throughout the model.

## 1. Chemical trajectory engineering

### Ion exchange reaction
```latex
\begin{equation}
\ce{\equiv Si-O- M+_{(s)} + H3O+_{(aq)} <=> \equiv Si-OH_{(s)} + M+_{(aq)} + H2O},
\label{eq:ion_exchange}
\end{equation}
```

### Siloxane hydrolysis reaction
```latex
\begin{equation}
\ce{\equiv Si-O-Si\equiv{} + OH- \longrightarrow \equiv Si-OH + {}^{-}O-Si\equiv},
\label{eq:hydrolysis}
\end{equation}
```

### Arrhenius-weighted network reactivity
```latex
\begin{equation}
\alpha(Q^n;T) \;=\; \sum_{n=0}^{4} f(Q^n)\,w_n(T),\qquad
w_n(T)\;=\;\nu_n\,e^{-E_{a,n}^{\mathrm{hydr}}/RT},
\label{eq:alpha_arrhenius}
\end{equation}
```

### Dissolution flux boundary condition
```latex
\begin{equation}
k_{\mathrm{diss},i}^{\circ}(T) \;=\; \alpha(Q^n;T)\,k_0\,c_i(\mathrm{network}),
\label{eq:k_diss}
\end{equation}
```

### Gel-layer transport flux
```latex
\begin{equation}
J_i(\mathbf{x},t) \;=\; \frac{D_g}{\delta_g(\mathbf{x},t)}\Bigl(C_{i,s}(\mathbf{x},t)-C_{i,b}(\mathbf{x},t)\Bigr),
\label{eq:gel_flux}
\end{equation}
```

### HCA saturation index and ion activity product
```latex
\begin{equation}
\SIhc \;=\; \log_{10}\Bigl(\frac{\mathit{IAP}}{K_{sp}}\Bigr),\qquad
\mathit{IAP}=a_{\mathrm{Ca}}^{9}\,a_{\mathrm{PO_4}}^{6}\,a_{\mathrm{OH}}^{2},
\label{eq:SI}
\end{equation}
```

### Recession law at the reaction front
```latex
\begin{equation}
\frac{\dd r_s}{\dd t} \;=\; -\frac{\bar{V}_m}{1-\varepsilon}\,\sum_i k_{\mathrm{diss},i}^{\circ},
\label{eq:recession}
\end{equation}
```

### Autocatalytic pH feedback loop
```latex
\begin{equation}
\frac{\dd[\ce{H+}]}{\dd t} = -\mathcal{A}_1\,r_{\mathrm{ex}} \;+\; \mathcal{A}_2\,k_{\mathrm{hydr}}[\ce{OH-}]^{m},\qquad
k_{\mathrm{hydr}}\bigl([\ce{OH-}]\bigr)=k_{\mathrm{hydr}}^{0}\Bigl(1+\chi [\ce{OH-}]^{m}\Bigr),
\label{eq:ph_feedback}
\end{equation}
```

### Surface NBO/BO tracking metric
```latex
\begin{equation}
\Bigl(\frac{\mathrm{NBO}}{\mathrm{BO}}\Bigr)_{\!s}\!(t) \;=\; \frac{A_{\mathrm{NBO}}(t)}{A_{\mathrm{BO}}(t)} \;\propto\; \alpha\bigl(Q^n_{\mathrm{front}}(t)\bigr).
\label{eq:nbo_bo}
\end{equation}
```

## 2. Architectural transport metrics

### Static effective diffusivity law
```latex
\begin{equation}
\Veff \;=\; D_0\,\frac{\varepsilon}{\kappa^{2}}\,g(\varepsilon),
\label{eq:D_eff_static}
\end{equation}
```

### Static scaffold-specific surface scaling
```latex
\begin{equation}
\beta(\mathbf{x},0) \;=\; \frac{SA}{V} \;\simeq\; \frac{n_{\mathrm{struts}}\,\pi\,d_{\mathrm{strut}}\,l_{\mathrm{strut}}}{V_{\mathrm{scaffold}}},
\label{eq:beta_static}
\end{equation}
```

### Dynamic effective diffusivity and tortuosity evolution
```latex
\begin{equation}
\Veff(\mathbf{x},t) \;=\; D_0\,\frac{\bigl[\varepsilon(\mathbf{x},t)\bigr]^{3/2}}{\bigl[\kappa(\mathbf{x},t)\bigr]^{2}},\qquad
\kappa(\mathbf{x},t) \;=\; \kappa_0\Bigl(\frac{\varepsilon(\mathbf{x},0)}{\varepsilon(\mathbf{x},t)}\Bigr)^{q},
\label{eq:D_eff_dynamic}
\end{equation}
```

## 3. Moving-boundary coupled framework

### Porosity evolution law
```latex
\begin{equation}
\pde{\varepsilon(\mathbf{x},t)}{t} \;=\; k^{\circ}_{\mathrm{diss}}\,\alpha(Q^n,t)\;\beta(\mathbf{x},t)\;\bar{V}_m,
\label{eq:eps_evol}
\end{equation}
```

### Dynamic geometric factor for cylindrical struts
```latex
\begin{equation}
\beta(\mathbf{x},t) \;=\; \frac{SA}{V} \;=\; \frac{3\,\bigl(1-\varepsilon(\mathbf{x},t)\bigr)}{r_s(\mathbf{x},t)},
\label{eq:beta_dyn}
\end{equation}
```

### Coupled master equation for ion transport
```latex
\begin{equation}
\pde{C_i}{t} \;+\; \underbrace{\nabla\!\cdot\!\bigl(\mathbf{u}\,C_i\bigr)}_{\text{convection}}
\;=\; \underbrace{\nabla\!\cdot\!\Bigl[\Veff(\mathbf{x},t)\,\nabla C_i\Bigr]}_{\text{diffusion}}
\;+\; \underbrace{k^{\circ}_{\mathrm{diss},i}\,\alpha(Q^n,t)\,\beta(\mathbf{x},t)\,\phi(\SIhc)}_{\text{source: chemistry}\times\text{architecture}}
\;-\; \underbrace{k_{\mathrm{precip},i}\,\gamma(\SIhc)}_{\text{precipitation sink}},
\label{eq:master}
\end{equation}
```

### Reaction-diffusion modifiers
```latex
\begin{equation}
\phi(\SIhc)=1-e^{-\SIhc^{2}},\qquad
\gamma(\SIhc)=\max\!\Bigl(0,\;1-e^{-(\SIhc-\SIhc^{\mathrm{crit}})}\Bigr),
\label{eq:phi_gamma}
\end{equation}
```

### Brinkman formulation for porous-media convection
```latex
\begin{equation}
-\nabla p + \mu_{\mathrm{eff}}\,\nabla^{2}\mathbf{u} - \frac{\mu}{\kappa_m\bigl(\varepsilon(\mathbf{x},t)\bigr)}\,\mathbf{u} = 0,\qquad
\nabla\!\cdot\!\mathbf{u}=0,
\label{eq:brinkman}
\end{equation}
```

### Damk\"ohler and P\'eclet numbers
```latex
\begin{equation}
\mathrm{Da} \;=\; \frac{k^{\circ}_{\mathrm{diss}}\,\alpha\,\beta\,L^{2}}{\Veff}\quad\text{(reaction/diffusion)},\qquad
\mathrm{Pe} \;=\; \frac{U\,L}{\Veff}\quad\text{(convection/diffusion)}.
\label{eq:Da_Pe}
\end{equation}
```

### State-vector ODE form
```latex
\begin{equation}
\mathbf{S}(\mathbf{x},t)=\Bigl[C_{\mathrm{Ca}},\,C_{\mathrm{Si}},\,C_{\mathrm{Mg}},\,\mathrm{pH},\,\varepsilon,\,D_{\mathrm{eff}}\Bigr]^{T}\!\in\mathbb{R}^{6},\qquad
\frac{\dd \mathbf{S}}{\dd t}=\mathcal{F}\bigl(\mathbf{S},\boldsymbol{\theta}\bigr),
\label{eq:state_ode}
\end{equation}
```

## 4. Biological validation and RTZ tube

### Continuous admissibility tube definition
```latex
\begin{equation}
\RZT(t) \;=\; \Bigl\{\, \mathbf{S}(\cdot)\in C^{0}\bigl([0,T];\mathbb{R}^{6}\bigr) \;\Big|\;
C_{i}^{\min}(t)\leq C_{i}(t)\leq C_{i}^{\max}(t),\;\;
[\ce{H+}](t)\in[\ce{H+}]^{\mathrm{lo},\mathrm{hi}},\;\;
\varepsilon(t)\geq\varepsilon^{\mathrm{perc}},\;\;\forall\,t\in(0,T] \Bigr\},
\label{eq:rtz_tube}
\end{equation}
```

### Tube-distance criterion
```latex
\begin{equation}
d_{\RZT}\bigl(\mathbf{S}\bigr) \;=\; \max_{t\in[0,T]}\bigl\Vert\mathbf{S}(t)-\Pi_{\RZT}(\mathbf{S}(t))\bigr\Vert_{2},\qquad
\mathbf{S}\in\RZT \iff d_{\RZT}(\mathbf{S})\leq\delta^{*},
\label{eq:tube_dist}
\end{equation}
```

### Phase-indexed tube decomposition
```latex
\begin{equation}
C_{i}^{\min}(t)=\sum_{k}\Omega_k(t)\,C_{i,k}^{\min},\qquad
C_{i}^{\max}(t)=\sum_{k}\Omega_k(t)\,C_{i,k}^{\max},
\label{eq:tube_phase}
\end{equation}
```

## 5. Functional data analysis and computational model learning

### fPCA eigenequation
```latex
\begin{equation}
\int_{0}^{T}\Sigma(s,t)\,\psi_k(t)\,\dd t \;=\; \lambda_k\,\psi_k(s),
\label{eq:fpca_eig}
\end{equation}
```

### fPCA score definition
```latex
\begin{equation}
\xi_k \;=\; \int_{0}^{T}\bigl(\mathbf{S}(t)-\mu(t)\bigr)\,\psi_k(t)\,\dd t,
\label{eq:fpca_score}
\end{equation}
```

### fPCA reconstruction
```latex
\begin{equation}
\mathbf{S}(t)\;\approx\; \mu(t)+\sum_{k=1}^{K}\xi_k\,\psi_k(t),\qquad K\ll N,
\label{eq:fpca_rec}
\end{equation}
```

### Dynamic time warping cumulative cost
```latex
\begin{equation}
\mathcal{D}(i,j)\;=\;\min\!\bigl\{\mathcal{D}(i-1,j),\;\mathcal{D}(i,j-1),\;\mathcal{D}(i-1,j-1)\bigr\}\;+\;d\bigl(\mathbf{S}_i,\hat{\mathbf{S}}_j\bigr),
\label{eq:dtw}
\end{equation}
```

### Neural ODE state evolution
```latex
\begin{equation}
\frac{\dd\mathbf{S}}{\dd t} \;=\; F_{\boldsymbol{\theta}}\bigl(\mathbf{S}(t),t\bigr),\qquad
\mathbf{S}(t_1)\;=\;\mathbf{S}(t_0)+\int_{t_0}^{t_1}F_{\boldsymbol{\theta}}\,\dd t,
\label{eq:node}
\end{equation}
```

### Adjoint equations for neural ODE training
```latex
\begin{equation}
\frac{\dd\mathbf{a}}{\dd t} \;=\; -\mathbf{a}^{T}\,\frac{\partial F_{\boldsymbol{\theta}}}{\partial \mathbf{S}},\qquad
\frac{\dd \mathcal{L}}{\dd \boldsymbol{\theta}} \;=\; -\int_{t_1}^{t_0}\mathbf{a}^{T}\,\frac{\partial F_{\boldsymbol{\theta}}}{\partial \boldsymbol{\theta}}\,\dd t,
\label{eq:adjoint}
\end{equation}
```

### PINN composite loss
```latex
\begin{equation}
\mathcal{L}(\boldsymbol{\theta}) \;=\; \lambda_D\mathcal{L}_{\mathrm{data}} + \lambda_P\mathcal{L}_{\mathrm{PDE}} + \lambda_B\mathcal{L}_{\mathrm{BC/IC}},
\label{eq:pinn_loss}
\end{equation}
```

### PINN PDE residual loss
```latex
\begin{equation}
\mathcal{L}_{\mathrm{PDE}} \;=\; \Bigl\|\pde{\hat{\mathbf{S}}}{t} + \nabla\!\cdot\!\bigl(\mathbf{u}\hat{\mathbf{S}}\bigr) - \nabla\!\cdot\!\bigl(\Veff(\mathbf{x},t)\nabla\hat{\mathbf{S}}\bigr) - \hat{\mathcal{R}}\Bigr\|^{2},
\label{eq:pinn_pde}
\end{equation}
```

### Hamiltonian used in HMC sampling
```latex
\begin{equation}
H(\boldsymbol{\theta},\mathbf{p}) \;=\; U(\boldsymbol{\theta}) + K(\mathbf{p}),\qquad
U(\boldsymbol{\theta})=-\log p(\mathcal{D}\mid\boldsymbol{\theta})-\log\pi(\boldsymbol{\theta}),
\label{eq:hmc_hamiltonian}
\end{equation}
```

### Posterior RTZ membership probability
```latex
\begin{equation}
\Pr\bigl(\mathbf{S}(t)\in \RZT(t)\mid\mathcal{D}\bigr) \;=\; \int \mathbf{1}_{\RZT}\bigl(\hat{\mathbf{S}}_{\boldsymbol{\theta}}(t)\bigr)\,p(\boldsymbol{\theta}\mid\mathcal{D})\,\dd\boldsymbol{\theta},
\label{eq:rtz_prob}
\end{equation}
```

### UCB acquisition function for active learning
```latex
\begin{equation}
\mathrm{UCB}(\mathbf{x})\;=\;\mu_{GP}(\mathbf{x}) + \beta_t\,\sigma_{GP}(\mathbf{x}),
\label{eq:ucb}
\end{equation}
```

---

## Notes

- The manuscript contains only `equation` environments in this draft; no `align` environments were used in the current source.
- All labels have been preserved as written in the original manuscript.
- The equations remain in the LaTeX source; this file is a reference copy only.
