# Damkohler--Peclet Scaling

## Non-dimensionalization

Use $\mathbf{x}=L\hat{\mathbf{x}}$, $t=(L^2/D_{\mathrm{eff}})\hat{t}$, $C_i=C_0\hat{C}_i$, and $\mathbf{u}=U\hat{\mathbf{u}}$. Starting from

$$
\frac{\partial C_i}{\partial t}+\nabla\cdot(\mathbf{u}C_i)=\nabla\cdot(D_{\mathrm{eff}}\nabla C_i)+k_{\mathrm{diss}}^\circ\alpha\beta_0\Phi(C_i),
$$

substitution and multiplication by $L^2/(D_{\mathrm{eff}}C_0)$ gives

$$
\boxed{\frac{\partial\hat{C}_i}{\partial\hat{t}}+\mathrm{Pe}\,\hat{\nabla}\cdot(\hat{\mathbf{u}}\hat{C}_i)=\hat{\nabla}^2\hat{C}_i+\mathrm{Da}\,\hat{\Phi}(\hat{C}_i)}.
$$

The exact dimensionless groups are

$$
\boxed{\mathrm{Da}=\frac{k_{\mathrm{diss}}^\circ\alpha\beta_0L^2}{D_{\mathrm{eff}}C_0}},
\qquad
\boxed{\mathrm{Pe}=\frac{UL}{D_{\mathrm{eff}}}}.
$$

## Physical interpretation and regimes

The Damk\"ohler number measures how quickly the material reacts relative to how fast species diffuse away:

- $\mathrm{Da} \ll 1$: reaction is slow relative to diffusion
- $\mathrm{Da} \gg 1$: reaction is fast relative to diffusion

In the context of bioactive silicate degradation, large $\mathrm{Da}$ corresponds to rapid surface dissolution and possible local supersaturation or HCA precipitation spikes.

The P\'eclet number compares convection to diffusion:

$$
\mathrm{Pe} = \frac{UL}{D_{\mathrm{eff}}}.
$$

It reveals whether solutes are transported largely by advective washout or by local diffusive equilibration.

- $\mathrm{Pe} \ll 1$: diffusion-dominated transport
- $\mathrm{Pe} \gg 1$: convection-dominated transport

## Quadrant analysis

The $(\log_{10}\mathrm{Pe},\log_{10}\mathrm{Da})$ plane splits into four asymptotic regimes.

### Q1: reaction-limited, diffusion-dominated

$$
\mathrm{Da}\ll 1, \qquad \mathrm{Pe}\ll 1.
$$

This is a slow, relatively uniform release regime, typically associated with gentle plateaus and underdosing risk.

### Q2: diffusion-limited burst regime

$$
\mathrm{Da}\gg 1, \qquad \mathrm{Pe}\ll 1.
$$

Reaction is fast but local diffusion cannot remove the generated ions efficiently, producing boundary-layer supersaturation and burst/passivation behavior.

### Q3: convective washout regime

$$
\mathrm{Da}\ll 1, \qquad \mathrm{Pe}\gg 1.
$$

Transport is dominated by advection; ions are swept away before accumulation, leading to low local exposure and a weak osteogenic signal.

### Q4: convection-amplified localized dosing

$$
\mathrm{Da}\gg 1, \qquad \mathrm{Pe}\gg 1.
$$

This is a highly dynamic regime with steep gradients and aggressive local dosing, often associated with erosion-driven instability and possible overshoot.

## Design corridor

The central design corridor is the coupled regime

$$
\mathrm{Da}\sim 1,\qquad \mathrm{Pe}\sim 1.
$$

This is the regime in which reaction and transport neither dominate independently. It is here that the trajectory can be deliberately tuned to sit inside the biological admissibility tube. The engineering problem reduces to:

$$
\text{choose } (\alpha, \beta_0, \varepsilon_0, U) \text{ such that } (\mathrm{Da},\mathrm{Pe}) \in \text{design corridor}.
$$

The source reactivity $\alpha$, specific area $\beta_0$, and dynamic diffusivity $D_{\mathrm{eff}}$ are therefore inseparable design variables. Static composition or architecture optimization cannot determine whether a full trajectory remains inside the biological admissibility tube.
