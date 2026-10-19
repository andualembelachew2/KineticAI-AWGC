# 04. Regenerative Target Zone (RTZ) Specification

## 4.1 Functional specification of trajectory admissibility

The Regenerative Target Zone (RTZ) is a continuous admissibility tube in the state space of the evolving scaffold. The local state vector is

```math
\mathbf{S}(t) = \left( C_{\mathrm{Ca}}(t),\ C_{\mathrm{Si}}(t),\ C_{\mathrm{Mg}}(t),\ \mathrm{pH}(t),\ \varepsilon(t),\ D_{\mathrm{eff}}(t) \right)^{T}
```

Let $`h(t) = [\mathrm{H}^{+}](t)`$ denote the proton concentration derived from $`\mathrm{pH}(t)`$. The RTZ is the set of continuous trajectories

```math
\mathrm{RTZ} = \lbrace\, \mathbf{S} \in C^{0}([0,T];\mathbb{R}^{6}) \;\mid\; \mathbf{S} \text{ satisfies (R1)–(R3) for all } t \in (0,T] \,\rbrace
```

where the three conditions are:

**(R1) Ion concentration bounds**, for $`i \in \lbrace \mathrm{Ca}, \mathrm{Si}, \mathrm{Mg} \rbrace`$:

```math
C_i^{\min}(t) \le C_i(t) \le C_i^{\max}(t)
```

**(R2) Proton concentration (pH) window:**

```math
h_{\mathrm{lo}} \le h(t) \le h_{\mathrm{hi}}
```

**(R3) Percolation-limited porosity:**

```math
\varepsilon(t) \ge \varepsilon_{\mathrm{perc}}
```

Biological admissibility is **temporal and continuous**. It is not a single static endpoint.

## 4.2 Projection-based distance metric

To test whether a predicted trajectory belongs to the RTZ, let $`\Pi_{\mathrm{RTZ}}`$ be the orthogonal projection onto the admissible tube. The tube-distance metric is

```math
d_{\mathrm{RTZ}}(\mathbf{S}) = \max_{t \in [0,T]} \left\| \mathbf{S}(t) - \Pi_{\mathrm{RTZ}}\big(\mathbf{S}(t)\big) \right\|_{2}
```

and the admissibility criterion is

```math
\mathbf{S} \in \mathrm{RTZ} \iff d_{\mathrm{RTZ}}(\mathbf{S}) \le \delta^{*}
```

where $`\delta^{*}`$ is the tolerance. This gives a single measurable scalar for trajectory quality.

## 4.3 Phase-indexed biological logic

The trajectory is partitioned into three operational phases.

| Phase | Window | Goal | Constraint |
|---|---|---|---|
| **I. Inflammation / M1 gating** | $`0 < t \le 48\ \mathrm{h}`$ | Allow debris clearance and cell recruitment without excessive inflammatory overshoot | Keep pH and ionic doses below a permissible ceiling |
| **II. M1 to M2 transition** | Days 3–7 | Sustain pro-regenerative polarization and M2 dominance | Keep ion dose within an intermediate, sustained band |
| **III. HCA mineralization and osteogenic maturation** | $`t \gtrsim 14\ \mathrm{days}`$ | Support mineralization and osteogenic consolidation | Maintain active mineralization and enough open porosity for vascular infiltration |

## 4.4 Phase-weighted tube bounds

The tube is a phase-scheduled specification. With phase weights $`\Omega_k(t)`$ satisfying

```math
\sum_k \Omega_k(t) = 1
```

the time-dependent bounds are

```math
C_i^{\min}(t) = \sum_k \Omega_k(t)\, C_{i,k}^{\min}
```

```math
C_i^{\max}(t) = \sum_k \Omega_k(t)\, C_{i,k}^{\max}
```

The design problem is then

```math
\text{find } (\alpha, \beta_0) \text{ such that } \mathbf{S}(t) \in \mathrm{RTZ}(t) \quad \forall\, t \in [0,T]
```

This is a full trajectory specification, not a discrete threshold test.

## 4.5 Advantage over endpoint testing

An endpoint test cannot distinguish a burst-and-passivation profile from a controlled gradual profile if both meet the same endpoint criterion. The RTZ judges the full temporal envelope instead. This matters in tissue repair, where timing is often more important than the final average value.
