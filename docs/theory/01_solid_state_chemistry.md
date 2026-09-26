# Solid-State Chemistry and Reactive Speciation

## $Q^{n}$ connectivity and spectroscopy

For $Q^{n}$ units, $n$ counts bridging oxygens around silicon. If $A_{n}$ is the fitted $^{29}$Si MAS-NMR area, then

$$
f(Q^{n})=\frac{A_{n}}{\sum_{m=0}^{4} A_{m}},\qquad \sum_{n=0}^{4}f(Q^{n})=1,
$$

and

$$
\langle n\rangle=\sum_{n=0}^{4} n f(Q^{n})=\frac{\sum_{n} nA_{n}}{\sum_{n}A_{n}}.
$$

Representative isotropic assignments are $Q^{0}\approx-72$, $Q^{1}\approx-80$, $Q^{2}\approx-88$, $Q^{3}\approx-97$, and $Q^{4}\approx-112$ ppm. The trend toward more negative shift reflects increasing polymerization and bridging-oxygen connectivity.

## Arrhenius reactivity

For a $Q^{n}$ population, the hydrated network-cleavage rate is

$$
k_{n}(T)=\nu_{n}\exp\left(-\frac{E_{a,n}^{\mathrm{hydr}}}{RT}\right).
$$

Weighting each environment by its spectroscopic fraction gives

$$
\bar{k}(T)=\sum_{n=0}^{4} f(Q^{n})\nu_{n}\exp\left(-\frac{E_{a,n}^{\mathrm{hydr}}}{RT}\right).
$$

Taking the reference frequency as unity defines the activity-like reactivity

$$
\boxed{\alpha(Q^{n};T)=\sum_{n=0}^{4} f(Q^{n})\nu_{n} \exp\left(-\frac{E_{a,n}^{\mathrm{hydr}}}{RT}\right)}.
$$

If $k_{\mathrm{diss},i}^{\circ}$ is the intrinsic rate for species $i$, its source is

$$
r_{i}=k_{\mathrm{diss},i}^{\circ}\alpha(Q^{n};T)c_{i}^{\mathrm{network}}.
$$

## Incongruent dissolution and XPS tracking

Modifier exchange and siloxane hydrolysis have separate balances:

$$
\frac{dN_{M}}{dt}=-k_{M}a_{s}[\mathrm{H}^{+}],\qquad
\frac{dN_{Si}}{dt}=-k_{Si}a_{s}[\mathrm{OH}^{-}]^{m}.
$$

Therefore

$$
\frac{dN_{M}}{dN_{Si}}=\frac{k_{M}[\mathrm{H}^{+}]}{k_{Si}[\mathrm{OH}^{-}]^{m}},
$$

so preferential modifier loss creates a silica-rich gel. The gel flux is

$$
\boxed{J_{i}=\frac{D_{g}}{\delta_{g}}(C_{i,s}-C_{i,b})}.
$$

For O 1s XPS, fit

$$
I(E)=A_{BO}g_{BO}(E)+A_{NBO}g_{NBO}(E)+A_{OH}g_{OH}(E),
$$

with Gaussian components $g_{j}$. Since each $g_{j}$ integrates to one,

$$
\left(\frac{NBO}{BO}\right)_{s}=\frac{A_{NBO}}{A_{BO}},
$$

using representative centers near 531.5 eV (NBO) and 532.8 eV (BO). This surface ratio tracks the reactive front rather than the bulk average.

## Autocatalytic pH feedback and bifurcation

Let $h=[\mathrm{H}^{+}]$, $[\mathrm{OH}^{-}]=K_{w}/h$, and let exchange consume protons while hydrolysis generates them through an alkaline feedback term:

$$
\frac{dh}{dt}=-a k_{ex}h+b k_{h}^{0}K_{w}^{m} h^{-m}\left(1+\chi K_{w}^{m} h^{-m}\right)=F(h).
$$

A steady state satisfies

$$
F(h_{\ast})=0.
$$

Local stability follows from linearization, $h=h_{\ast}+\eta$:

$$
\frac{d\eta}{dt}=F'(h_{\ast})\eta+O(\eta^{2}),
$$

so $F'(h_{\ast})<0$ is stable. A saddle-node bifurcation occurs when

$$
F(h_{\ast})=0,\qquad F'(h_{\ast})=0.
$$

These equations define the threshold between a near-neutral branch and an alkaline high-reactivity branch. The coupled chain is therefore

$$
Q^{n}\rightarrow E_{a}\rightarrow\alpha(Q^{n};T)\rightarrow r_{i}\rightarrow J_{i}\rightarrow\mathrm{pH}(t).
$$
