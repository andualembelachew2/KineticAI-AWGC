# Regenerative Target Zone

## Continuous admissibility tube

Let

$$
\mathbf S(t)=\left[C_{Ca}(t),C_{Si}(t),C_{Mg}(t),\mathrm{pH}(t),\varepsilon(t)\right]^T.
$$

With phase-scheduled lower and upper bounds $\mathbf S_{\min}(t)$ and $\mathbf S_{\max}(t)$,

$$
\boxed{\mathcal R_{TZ}(t)=\{\mathbf s:\mathbf S_{\min}(t)\le\mathbf s\le\mathbf S_{\max}(t)\}}.
$$

For a positive scaling vector $\boldsymbol\sigma$, define the projection

$$
\Pi_{\mathcal R_{TZ}}(S_j)=\min\{\max\{S_j,S_{j,\min}\},S_{j,\max}\},
$$

and trajectory distance

$$
\boxed{d_{\mathcal R_{TZ}}(\mathbf S)=\max_t\left\|\frac{\mathbf S(t)-\Pi_{\mathcal R_{TZ}}(\mathbf S(t))}{\boldsymbol\sigma}\right\|_2}.
$$

Admissibility means $d_{\mathcal R_{TZ}}=0$, or $d_{\mathcal R_{TZ}}\le\delta$ when measurement tolerance is accepted.

## Explicit phase bounds

The following normalized bounds define the executable demonstration tube.

### Phase I: 0--48 h, M1 gating

$$
0.15\le C_{Ca}\le0.55,\quad0.10\le C_{Si}\le0.45,\quad0.05\le C_{Mg}\le0.35,
$$

$$
7.35\le\mathrm{pH}\le7.85,\qquad0.20\le\varepsilon\le0.55.
$$

### Phase II: D3--D7, M1 to M2 transition

$$
0.35\le C_{Ca}\le0.90,\quad0.30\le C_{Si}\le0.85,\quad0.15\le C_{Mg}\le0.60,
$$

$$
7.40\le\mathrm{pH}\le8.20,\qquad0.30\le\varepsilon\le0.70.
$$

### Phase III: after D14, maturation

$$
0.50\le C_{Ca}\le1.10,\quad0.45\le C_{Si}\le1.00,\quad0.10\le C_{Mg}\le0.50,
$$

$$
7.40\le\mathrm{pH}\le8.00,\qquad0.45\le\varepsilon\le0.85.
$$

The bounds are applied at every sampled time point, not only at the final endpoint.
