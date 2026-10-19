# 01. Solid-State Chemistry Derivation

## 1.1 Network speciation from <sup>29</sup>Si MAS-NMR

Silicate glasses and glass-ceramics are built from tetrahedral $`\mathrm{SiO}_4`$ units connected by bridging oxygens (BO) and non-bridging oxygens (NBO). The $`Q^n`$ notation tracks the number of bridging oxygens attached to each silicon center, with

```math
Q^0,\ Q^1,\ Q^2,\ Q^3,\ Q^4
```

representing increasingly connected silicate environments. The isotropic chemical shifts recorded by <sup>29</sup>Si MAS-NMR separate these species, roughly as follows:

| Species | Approximate shift (ppm) |
|---|---|
| $`Q^4`$ | $`-110`$ to $`-115`$ |
| $`Q^3`$ | $`-97`$ |
| $`Q^2`$ | $`-88`$ |
| $`Q^1`$ | $`-80`$ |
| $`Q^0`$ | $`-72`$ |

The network connectivity is described by a distribution $`f(Q^n)`$ satisfying

```math
\sum_{n=0}^{4} f(Q^n) = 1
```

and the mean connectivity is

```math
\langle n \rangle = \sum_{n=0}^{4} n\, f(Q^n)
```

This is the first bridge between spectroscopy and kinetics: the network speciation determines where the most reactive sites reside.

## 1.2 Two activation barriers: hydration versus hydrolysis

The dissolution pathway is not a single reaction but a sequence of two distinct activated events.

### Hydration / modifier exchange

Modifier ions such as $`\mathrm{Ca}^{2+}`$, $`\mathrm{Mg}^{2+}`$, or $`\mathrm{Na}^{+}`$ are removed by proton attack:

```math
\equiv\!\mathrm{Si}\text{-}\mathrm{O}\text{-}\mathrm{M}^{+}_{(\mathrm{s})} + \mathrm{H}_3\mathrm{O}^{+}_{(\mathrm{aq})} \rightleftharpoons\ \equiv\!\mathrm{Si}\text{-}\mathrm{OH}_{(\mathrm{s})} + \mathrm{M}^{+}_{(\mathrm{aq})} + \mathrm{H}_2\mathrm{O}
```

This process is governed by a relatively modest activation barrier:

```math
E_{a,n}^{\mathrm{hyd}} \in [35,\,65]\ \mathrm{kJ\,mol^{-1}}
```

### Hydrolysis / network breakdown

The siloxane bridge is cleaved by nucleophilic attack:

```math
\equiv\!\mathrm{Si}\text{-}\mathrm{O}\text{-}\mathrm{Si}\!\equiv\ +\ \mathrm{OH}^{-} \longrightarrow\ \equiv\!\mathrm{Si}\text{-}\mathrm{OH}\ +\ {}^{-}\mathrm{O}\text{-}\mathrm{Si}\!\equiv
```

This is more demanding thermodynamically because it breaks the covalent network itself. The barrier $`E_{a,n}^{\mathrm{hydr}}`$ increases steeply with $`n`$.

The key consequence is incongruent dissolution: modifiers are stripped faster than the network is hydrolyzed, leaving a silica-rich surface layer that evolves into a gel barrier.

## 1.3 Arrhenius-weighted reactivity function

The network reactivity is defined as the weighted susceptibility of a silicate network to hydrolytic attack:

```math
\alpha(Q^n;T) = \sum_{n=0}^{4} f(Q^n)\, w_n(T)
```

```math
w_n(T) = \nu_n\, e^{-E_{a,n}^{\mathrm{hydr}} / RT}
```

where $`\nu_n`$ is the pre-exponential factor of species $`Q^n`$, $`R`$ is the gas constant, and $`T`$ is the absolute temperature.

This is the essential expression connecting spectroscopy to kinetics. Lower-$`Q^n`$ species (especially $`Q^2`$ and $`Q^1`$) generally dominate the reactivity because their activation barriers are lower and their local connectivity is more easily attacked by water or hydroxide. In matrix notation,

```math
\alpha(Q^n;T) = \mathbf{f}^{T}\, \mathbf{w}(T)
```

where the vector $`\mathbf{f}`$ is the NMR-resolved speciation distribution.

The dissolution rate constant is then

```math
k_{\mathrm{diss},i}^{\circ}(T) = \alpha(Q^n;T)\, k_0\, c_i^{\mathrm{network}}
```

where $`k_0`$ is a reference rate constant and $`c_i^{\mathrm{network}}`$ is the content of species $`i`$ in the network. This identifies the kinetic boundary condition driving the moving-boundary problem.

## 1.4 Gel-layer diffusion barrier

After modifier leaching and network hydrolysis, ions must migrate through an evolving hydrated silica-rich layer. The flux across the gel barrier is modeled as

```math
J_i(\mathbf{x},t) = \frac{D_g}{\delta_g(\mathbf{x},t)} \left( C_{i,s} - C_{i,b} \right)
```

where:

- $`D_g`$ is the gel-layer diffusivity,
- $`\delta_g`$ is the gel thickness,
- $`C_{i,s}`$ is the concentration at the solid-gel interface,
- $`C_{i,b}`$ is the concentration at the gel-solution interface.

This equation states that the flux is limited by a diffusive resistance that grows with gel thickness. As the barrier matures, the dose-rate envelope collapses unless fresh reactive surface is generated.

## 1.5 XPS O 1s deconvolution and front tracking

Bulk <sup>29</sup>Si MAS-NMR gives a volume-averaged network description, but the dissolution front is a surface phenomenon. Surface-sensitive XPS resolves the O 1s envelope into contributions from bridging oxygen (BO) and non-bridging oxygen (NBO):

| Species | Approximate binding energy (eV) |
|---|---|
| BO | $`532.8`$ |
| NBO | $`531.5`$ |

The surface metric is

```math
\left( \frac{\mathrm{NBO}}{\mathrm{BO}} \right)_{s}(t) = \frac{A_{\mathrm{NBO}}(t)}{A_{\mathrm{BO}}(t)}
```

where $`A`$ denotes the fitted peak area. Since the gel layer is relatively NBO-poor, this ratio tracks the remaining reactive fraction at the front:

```math
\left( \frac{\mathrm{NBO}}{\mathrm{BO}} \right)_{s}(t) \propto \alpha\!\left( Q^n_{\mathrm{front}}(t) \right)
```

This combination of XPS and NMR gives a surface-sensitive measure of how the dissolution front evolves, beyond what bulk spectroscopy alone can provide.

## 1.6 Autocatalytic pH feedback and bifurcation structure

The ion-exchange step liberates hydroxide and creates a feedback loop:

```math
\frac{d[\mathrm{H}^{+}]}{dt} = -\mathcal{A}_1\, r_{\mathrm{ex}} + \mathcal{A}_2\, k_{\mathrm{hydr}}\, [\mathrm{OH}^{-}]^{m}
```

with

```math
k_{\mathrm{hydr}}\!\left( [\mathrm{OH}^{-}] \right) = k_{\mathrm{hydr}}^{0} \left( 1 + \chi\, [\mathrm{OH}^{-}]^{m} \right)
```

where $`r_{\mathrm{ex}}`$ is the ion-exchange rate, $`\mathcal{A}_1`$ and $`\mathcal{A}_2`$ are stoichiometric coupling factors, and $`\chi`$ is the autocatalytic coefficient.

This indicates autocatalytic behavior: increased pH accelerates hydrolysis, which further increases hydroxide generation. In steady state, the system can settle at either a near-neutral state or a high-pH alkaline state. The transition defines a bifurcation threshold in reactivity space. This is the physical origin of the observed chemically distinct trajectory classes.

## 1.7 Summary

The chemistry layer creates the source-term envelope through a chain of observables:

```math
Q^n \;\to\; \lbrace E_{a,n} \rbrace \;\to\; \alpha(Q^n,T) \;\to\; k_{\mathrm{diss},i}^{\circ} \;\to\; J_i \;\to\; \text{HCA growth}
```

This is the foundation of trajectory engineering: the material chemistry is not just an initial property; it is a time-programmed source function.
