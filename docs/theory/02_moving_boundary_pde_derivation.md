# 02. Moving-Boundary PDE Derivation

## 2.1 Representative volume element and mass balance

Consider a representative volume element (REV) of the scaffold with both solid and pore phases. The total mass balance for a dissolving network phase is

$$
\frac{\partial}{\partial t}(\rho_s (1-\varepsilon)) + \nabla\cdot \mathbf{J}_s = 0,
$$

where $\rho_s$ is the solid density and $\varepsilon$ is porosity. The dissolution front recedes with a surface-normal velocity $\dd r_s/\dd t$, so as the solid is consumed, the pore volume increases at a rate proportional to the local mass-loss flux.

For a local surface reaction governed by the intrinsic dissolution constant $k_{\mathrm{diss}}^\circ$ and reactive area per unit volume $\beta(\mathbf{x},t)$, the rate of local porosity growth is

$$
\frac{\partial \varepsilon(\mathbf{x},t)}{\partial t}
=
 k_{\mathrm{diss}}^\circ \alpha(Q^n,t)\beta(\mathbf{x},t)\bar V_m.
$$

This expression is dimensionally consistent because

$$
[\mathrm{mol\,m^{-2}\,s^{-1}}]\,[\mathrm{m^{-1}}]\,[\mathrm{m^3\,mol^{-1}}] = [\mathrm{s^{-1}}].
$$

Here $\bar V_m$ is the molar volume of the dissolving phase.

## 2.2 Strut recession velocity

Mass conservation across the solid-gel interface gives the recession law

$$
\frac{\dd r_s}{\dd t} = -\frac{\bar V_m}{1-\varepsilon}\sum_i k_{\mathrm{diss},i}^{\circ}.
$$

The negative sign reflects shrinking solid radius as mass is lost. This is the geometric engine behind degradation: the boundary moves, the pore network opens, and transport properties evolve in lockstep.

## 2.3 Dynamic geometry and specific surface area

For a cylindrical strut, the surface-area-to-volume ratio is

$$
\beta(\mathbf{x},t) = \frac{SA}{V} = \frac{3(1-\varepsilon(\\mathbf{x},t))}{r_s(\mathbf{x},t)}.
$$

This is a crucial closure relation: the specific surface increases as the strut thins and porosity grows.

Because the surface area is itself a function of degradation state, the porosity field and the geometry field are not independent variables. Rather,

$$
\varepsilon = \varepsilon(r_s),\qquad \beta = \beta(\varepsilon,r_s),
$$

so the moving boundary and the transport field are dynamically coupled.

## 2.4 Dynamic tortuosity and effective diffusivity

For a degrading scaffold, the transport coefficients evolve with porosity. A common closure is the dynamic tortuosity law

$$
\kappa(\mathbf{x},t)=\kappa_0\left(\frac{\varepsilon(\mathbf{x},0)}{\varepsilon(\mathbf{x},t)}\right)^q,
$$

with $q \in [0.3,1.0]$ depending on architecture. The corresponding effective diffusivity is

$$
\Veff(\mathbf{x},t)=D_0\frac{\left[\varepsilon(\mathbf{x},t)\right]^{3/2}}{\left[\kappa(\mathbf{x},t)\right]^2},
$$

which is the dynamic Millington-Quirk form. This captures the key phenomenology that porosity opening accelerates transport while increasing paths of least resistance.

## 2.5 Coupled transport equation

The solute concentration satisfies a conservation law:

$$
\frac{\partial C_i}{\partial t} + \nabla\cdot(\mathbf{u} C_i)
=
\nabla\cdot\bigl(\Veff(\mathbf{x},t)\nabla C_i\bigr)
+
 k_{\mathrm{diss},i}^\circ\alpha(Q^n,t)\beta(\mathbf{x},t)\phi(\mathrm{SI}_{\mathrm{HCA}})
-
 k_{\mathrm{precip},i}\gamma(\mathrm{SI}_{\mathrm{HCA}}).
$$

This is the coupled master equation of the moving-boundary reactor. The right-hand side contains the source of ions from dissolution, diffusive spread through the varying pore network, and precipitation loss when the HCA saturation index becomes sufficiently large.

## 2.6 Brinkman porous-medium momentum balance

In vivo, interstitial fluid perfuses the degradable scaffold. The momentum balance is not free Stokes flow but porous-medium flow. The monophasic Brinkman extension reads

$$
-\nabla p + \mu_{\mathrm{eff}} \nabla^2 \mathbf{u} - \frac{\mu}{\kappa_m(\varepsilon(\mathbf{x},t))}\mathbf{u}=0,
\qquad\nabla\cdot\mathbf{u}=0.
$$

Here:
- $p$ is pore-fluid pressure,
- $\mathbf{u}$ is superficial pore velocity,
- $\mu$ is the fluid viscosity,
- $\mu_{\mathrm{eff}}$ is the effective viscosity,
- $\kappa_m$ is permeability.

As degradation proceeds, $\varepsilon$ increases, which raises both $\kappa_m$ and $\Veff$, coupling the flow field to the state variables of the scaffold.

## 2.7 Closing statement

The moving-boundary problem is therefore closed by a coupled set of state equations:

$$
\varepsilon = \varepsilon(\mathbf{x},t),\quad
\kappa = \kappa(\varepsilon),\quad
\Veff = \Veff(\varepsilon,\kappa),\quad
\mathbf{u} = \mathbf{u}(\varepsilon,p),\quad
C_i = C_i(\mathbf{x},t). 
$$

The architecture, chemistry, and transport fields are not independent design variables; they are coordinates of one evolving trajectory.
