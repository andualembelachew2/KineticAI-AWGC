# Moving-Boundary Reaction--Diffusion Derivation

## Porosity evolution

Let $V_s$ be solid volume in a representative volume $V$, so $V_s/V=1-\varepsilon$. A surface source $r_{\mathrm{diss}}$ over specific area $\beta=A_s/V$ removes solid volume at rate $\bar V_m r_{\mathrm{diss}}\beta$. Hence

$$
\frac{\partial[(1-\varepsilon)V]}{\partial t}=-V\bar V_m r_{\mathrm{diss}}\beta.
$$

Divide by $V$ and use $r_{\mathrm{diss}}=k_{\mathrm{diss}}^{\circ}\alpha$:

$$
\boxed{\frac{\partial\varepsilon}{\partial t}=k_{\mathrm{diss}}^{\circ}\alpha\beta\bar V_m}.
$$

For a cylindrical or isotropic strut with radius $r_s$,

$$
\beta(t)=\frac{3[1-\varepsilon(t)]}{r_s(t)}.
$$

## Receding boundary

The molar volume flux normal to the solid interface is $\bar V_m\sum_i k_{\mathrm{diss},i}^{\circ}\alpha_i$. Dividing by the remaining solid fraction gives

$$
\boxed{\frac{dr_s}{dt}=-\frac{\bar V_m}{1-\varepsilon}\sum_i k_{\mathrm{diss},i}^{\circ}\alpha_i}.
$$

The minus sign indicates recession. The radius equation and porosity equation are coupled through $\beta(t)$ and $\varepsilon(t)$.

## Dynamic tortuosity and diffusivity

Assume

$$
\boxed{\kappa(t)=\kappa_0\left(\frac{\varepsilon_0}{\varepsilon(t)}\right)^q}.
$$

The Millington--Quirk closure is

$$
\boxed{D_{\mathrm{eff}}(t)=D_0\frac{\varepsilon(t)^{3/2}}{\kappa(t)^2}}
=\frac{D_0}{\kappa_0^2}\varepsilon_0^{-2q}\varepsilon(t)^{3/2+2q}.
$$

Thus degradation changes transport even when the molecular diffusivity $D_0$ is fixed.

## Coupled PDE and Brinkman flow

For ion concentration $C_i$,

$$
\frac{\partial C_i}{\partial t}+\nabla\cdot(\mathbf u C_i)=\nabla\cdot[D_{\mathrm{eff}}(t)\nabla C_i]+S_i-R_i.
$$

The porous-medium momentum balance follows by combining viscous stress, pressure, and Darcy drag:

$$
\boxed{-\nabla p+\mu_{\mathrm{eff}}\nabla^2\mathbf u-\frac{\mu}{\kappa_m(\varepsilon)}\mathbf u=0},
\qquad \nabla\cdot\mathbf u=0.
$$

A Kozeny--Carman closure can be used for $\kappa_m(\varepsilon)$, linking flow resistance to the same moving geometry.
