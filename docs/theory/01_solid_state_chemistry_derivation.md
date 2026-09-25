# 01. Solid-State Chemistry Derivation

## 1.1 Network speciation from $^{29}$Si MAS-NMR

Silicate glasses and glass-ceramics are built from tetrahedral $\mathrm{SiO}_4$ units connected by bridging oxygens (BO) and non-bridging oxygens (NBO). The $Q^n$ notation tracks the number of bridging oxygens attached to each silicon center, with

$$
Q^0, Q^1, Q^2, Q^3, Q^4
$$

representing increasingly connected silicate environments. The isotropic chemical shifts recorded by $^{29}$Si MAS-NMR separate these species, roughly as

$$
Q^4 \approx -110\text{ to } -115\,\mathrm{ppm},\quad
Q^3 \approx -97\,\mathrm{ppm},\quad
Q^2 \approx -88\,\mathrm{ppm},\quad
Q^1 \approx -80\,\mathrm{ppm},\quad
Q^0 \approx -72\,\mathrm{ppm}.
$$

The network connectivity is therefore described by a distribution $f(Q^n)$ satisfying

$$
\sum_{n=0}^4 f(Q^n)=1,
$$

and the mean connectivity is

$$
\langle n \rangle = \sum_{n=0}^4 n f(Q^n).
$$

This is the first bridge between spectroscopy and kinetics: the network speciation determines where the most reactive sites reside.

## 1.2 Two activation barriers: hydration versus hydrolysis

The dissolution pathway is not a single reaction but a sequence of two distinct activated events.

### Hydration / modifier exchange

Modifier ions such as $\mathrm{Ca}^{2+}$, $\mathrm{Mg}^{2+}$, or $\mathrm{Na}^{+}$ are removed by proton attack:

$$
\ce{\equiv Si-O-M+_{(s)} + H3O+_{(aq)} <=> \equiv Si-OH_{(s)} + M+_{(aq)} + H2O}
$$

This process is governed by a relatively modest activation barrier

$$
E_{a,n}^{\mathrm{hyd}} \in [35,65]\;\mathrm{kJ\,mol^{-1}}.
$$

### Hydrolysis / network breakdown

The siloxane bridge is cleaved by nucleophilic attack:

$$
\ce{\equiv Si-O-Si\equiv{} + OH- \longrightarrow \equiv Si-OH + {}^{-}O-Si\equiv}
$$

This is more demanding thermodynamically because it breaks the covalent network itself:

$$
E_{a,n}^{\mathrm{hydr}} \text{ increases steeply with } n.
$$

The key consequence is incongruent dissolution: modifiers are stripped faster than the network is hydrolyzed, leaving a silica-rich surface layer that evolves into a gel barrier.

## 1.3 Arrhenius-weighted reactivity function

We define the network reactivity as the weighted susceptibility of a silicate network to hydrolytic attack:

$$
\alpha(Q^n;T)=\sum_{n=0}^{4} f(Q^n) w_n(T),
\qquad
w_n(T)=\nu_n e^{-E_{a,n}^{\mathrm{hydr}}/RT}.
$$

This is the essential expression connecting spectroscopy to kinetics. Lower-$Q^n$ species (especially $Q^2$ and $Q^1$) generally dominate the reactivity because their activation barriers are lower and their local connectivity is more easily attacked by water or hydroxide. In matrix notation,

$$
\alpha(Q^n;T) = \mathbf{f}^T \mathbf{w}(T),
$$

where the vector $\mathbf{f}$ represents the NMR-resolved speciation distribution.

The dissolution rate constant is then 

$$
k_{\mathrm{diss},i}^{\circ}(T) = \alpha(Q^n;T) k_0 c_i(\mathrm{network}),
$$

which identifies the kinetic boundary condition driving the moving-boundary problem.

## 1.4 Gel-layer diffusion barrier

After modifier leaching and network hydrolysis, ions must migrate through an evolving hydrated silica-rich layer. The flux across the gel barrier is modeled as

$$
J_i(\mathbf{x},t)=\frac{D_g}{\delta_g(\mathbf{x},t)}\left(C_{i,s}-C_{i,b}\right).
$$

Here:
- $D_g$ is the gel-layer diffusivity;
- $\delta_g$ is the gel thickness;
- $C_{i,s}$ is concentration at the solid-gel interface;
- $C_{i,b}$ is concentration at the gel-solution interface.

This equation states that the flux is limited by a diffusive resistance that grows with gel thickness. Thus, as the barrier matures, the dose-rate envelope collapses unless fresh reactive surface is generated.

## 1.5 XPS O 1s deconvolution and front tracking

Bulk $^{29}$Si MAS-NMR gives a volume-averaged network description, but the dissolution front is a surface phenomenon. Surface-sensitive XPS resolves the O 1s envelope into contributions from bridging oxygen (BO) and non-bridging oxygen (NBO):

$$
\mathrm{BO} \approx 532.8\,\mathrm{eV},\qquad
\mathrm{NBO} \approx 531.5\,\mathrm{eV}.
$$

The surface metric is therefore

$$
\left(\frac{\mathrm{NBO}}{\mathrm{BO}}\right)_s(t) = \frac{A_{\mathrm{NBO}}(t)}{A_{\mathrm{BO}}(t)}.
$$

Since the gel layer is relatively NBO-poor, this ratio tracks the remaining reactive fraction at the front:

$$
\left(\frac{\mathrm{NBO}}{\mathrm{BO}}\right)_s(t) \propto \alpha\bigl(Q^n_{\mathrm{front}}(t)\bigr).
$$

This combination of XPS and NMR gives a surface-sensitive measure of how the dissolution front evolves, beyond what bulk spectroscopy alone can tell.

## 1.6 Autocatalytic pH feedback and bifurcation structure

The ion-exchange step liberates hydroxide and creates a feedback loop:

$$
\frac{d[\ce{H+}]}{dt} = -\mathcal A_1 r_{\mathrm{ex}} + \mathcal A_2 k_{\mathrm{hydr}}[\ce{OH-}]^{m},
$$

with

$$
k_{\mathrm{hydr}}([\ce{OH-}]) = k_{\mathrm{hydr}}^0\left(1 + \chi [\ce{OH-}]^m\right).
$$

This indicates autocatalytic behavior: increased pH accelerates hydrolysis, which further increases hydroxide generation. In steady state, the system can settle at either a near-neutral state or a high-pH alkaline state. The transition defines a bifurcation threshold in reactivity space. This is the physical origin of the observed chemically distinct trajectory classes.

## 1.7 Summary

The chemistry layer creates the source-term envelope through a chain of observables:

$$
Q^n \;\rightarrow\; \{E_{a,n}\}\;\rightarrow\; \alpha(Q^n,T)\;\rightarrow\; k_{\mathrm{diss},i}^{\circ}\;\rightarrow\; J_i\;\rightarrow\; \mathrm{HCA\ growth}.
$$

This is the foundation of trajectory engineering: the material chemistry is not just an initial property; it is a time-programmed source function.
