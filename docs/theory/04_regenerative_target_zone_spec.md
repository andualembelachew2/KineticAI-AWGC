# 04. Regenerative Target Zone Specification

## 4.1 Functional specification of trajectory admissibility

The Regenerative Target Zone (RTZ) is defined as a continuous admissibility tube in the state space of the evolving scaffold trajectory. Let the local state vector be

$$
\mathbf{S}(t)=\left[C_{\mathrm{Ca}}(t), C_{\mathrm{Si}}(t), C_{\mathrm{Mg}}(t), \mathrm{pH}(t), \varepsilon(t), D_{\mathrm{eff}}(t)\right]^T.
$$

The RTZ is then the set

$$
\RZT(t)=\left\{\mathbf{S}(\cdot)\in C^0([0,T];\mathbb R^6)\;\middle|\; C_i^{\min}(t)\le C_i(t)\le C_i^{\max}(t),\; [\ce{H+}](t)\in[\ce{H+}]^{\mathrm{lo},\mathrm{hi}},\; \varepsilon(t)\ge \varepsilon^{\mathrm{perc}}\right\},
$$

for all $t\in(0,T]$.

This formulation emphasizes the key idea that biological admissibility is temporal and continuous; it is not a single static endpoint.

## 4.2 Projection-based distance metric

To test whether a predicted trajectory belongs to the RTZ, define the orthogonal projection onto the admissible tube $\Pi_{\RZT}$ and the tube-distance metric

$$
 d_{\RZT}(\mathbf{S}) = \max_{t\in[0,T]} \left\|\mathbf{S}(t)-\Pi_{\RZT}(\mathbf{S}(t))\right\|_2.
$$

Then the admissibility criterion is

$$
\mathbf{S}\in \RZT \iff d_{\RZT}(\mathbf{S})\le \delta^*.
$$

This directly gives a measurable scalar for trajectory quality.

## 4.3 Phase-indexed biological logic

The trajectory is partitioned into three operational phases:

### Phase I: inflammation / M1 gating

- Window: $0<t\le 48\,\mathrm{h}$
- Goal: allow effective debris clearance and recruitment without excessive inflammatory overshoot
- Constraint: keep pH and ionic doses below a permissible ceiling

### Phase II: M1 $\to$ M2 transition

- Window: Days 3–7
- Goal: sustain pro-regenerative polarization and M2 dominance
- Constraint: ion dose must remain within an intermediate, sustained band

### Phase III: HCA mineralization and osteogenic maturation

- Window: $t\gtrsim 14\,\mathrm{days}$
- Goal: support mineralization and osteogenic consolidation
- Constraint: maintain both active mineralization and sufficient open porosity for vascular infiltration

## 4.4 Phase-weighted tube bounds

The overall tube is a phase-scheduled specification. With phase weights $\Omega_k(t)$ satisfying

$$
\sum_k \Omega_k(t)=1,
$$

we define the time-dependent minimum and maximum bounds:

$$
C_i^{\min}(t)=\sum_k \Omega_k(t) C_{i,k}^{\min},\qquad
C_i^{\max}(t)=\sum_k \Omega_k(t) C_{i,k}^{\max}.
$$

The biological design problem becomes:

$$
\text{find } (\alpha,\beta_0) \text{ such that } \mathbf{S}(t) \in \RZT(t) \text{ for all } t\in[0,T].
$$

This is not a discrete threshold test but an entire trajectory specification.

## 4.5 Why the RTZ is scientifically stronger than endpoint testing

Endpoint tests cannot distinguish between e.g. a burst-and-passivation profile and a controlled gradual profile if both satisfy a single endpoint criterion. By contrast, the RTZ uses the full temporal envelope to judge the trajectory. This makes it directly relevant to tissue repair biology, where timing is often more important than the final average value.
