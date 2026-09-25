# SciML and Bayesian Trajectory Validation

## Functional PCA

For centered trajectories $y_i(t)-\bar y(t)$, the covariance kernel is

$$
K(t,s)=\frac{1}{N-1}\sum_i[y_i(t)-\bar y(t)][y_i(s)-\bar y(s)].
$$

The eigenfunctions satisfy

$$
\boxed{\int_0^T K(t,s)\phi_k(s)\,ds=\lambda_k\phi_k(t)},
\qquad\int_0^T\phi_j(t)\phi_k(t)\,dt=\delta_{jk}.
$$

Scores and reconstruction are

$$
a_{ik}=\int_0^T[y_i(t)-\bar y(t)]\phi_k(t)\,dt,
\qquad \hat y_i(t)=\bar y(t)+\sum_{k=1}^{K}a_{ik}\phi_k(t).
$$

## Dynamic Time Warping

For sequences $x_{1:n}$ and $y_{1:m}$, set $D_{0,0}=0$ and $D_{i,0}=D_{0,j}=\infty$. Then

$$
D_{ij}=|x_i-y_j|+\min(D_{i-1,j},D_{i,j-1},D_{i-1,j-1}),
$$

and $d_{DTW}(x,y)=D_{n,m}/|\pi^*|$ for optimal path $\pi^*$.

## Neural ODE adjoint

For $\dot z=f_\theta(z,t)$ and terminal loss $L=\ell(z(T))$, define $a(t)=\partial L/\partial z(t)$. Reverse integration uses

$$
\dot a=-a^T\frac{\partial f_\theta}{\partial z},\qquad a(T)=\frac{\partial\ell}{\partial z(T)},
$$

and

$$
\frac{dL}{d\theta}=\frac{\partial\ell}{\partial\theta}-\int_T^0a(t)^T\frac{\partial f_\theta}{\partial\theta}\,dt.
$$

## PINN moving-boundary loss

For $\hat C_\theta(x,t)$, define the PDE residual

$$
r_f=\partial_t\hat C_\theta+u\partial_x\hat C_\theta-\partial_x(D_{eff}\partial_x\hat C_\theta)-S(\hat C_\theta,\varepsilon),
$$

with initial, boundary, data, and moving-front residuals $r_0,r_b,r_d,r_\Gamma$. The composite objective is

$$
\mathcal L=\lambda_f\|r_f\|_2^2+\lambda_0\|r_0\|_2^2+\lambda_b\|r_b\|_2^2+\lambda_d\|r_d\|_2^2+\lambda_\Gamma\|r_\Gamma\|_2^2.
$$

## HMC credible RTZ tubes

With parameters $\vartheta$ and data $\mathcal D$,

$$
\pi(\vartheta\mid\mathcal D)\propto p(\mathcal D\mid\vartheta)p(\vartheta).
$$

HMC augments this with $p\sim\mathcal N(0,M)$ and Hamiltonian

$$
H(\vartheta,p)=-\log\pi(\vartheta\mid\mathcal D)+\frac12p^TM^{-1}p,
$$

using $\dot\vartheta=M^{-1}p$ and $\dot p=\nabla_\vartheta\log\pi$. If $\mathbf S^{(s)}(t)$ are posterior forward solves, then

$$
\boxed{\Pr(\mathbf S(t)\in\mathcal R_{TZ}(t)\ \forall t\mid\mathcal D)
\approx\frac1S\sum_{s=1}^S\mathbf1\{\mathbf S^{(s)}(t)\in\mathcal R_{TZ}(t)\ \forall t\}}.
$$

Pointwise credible tube bounds are posterior quantiles of $S_j^{(s)}(t)$ and can be compared directly with the phase-specific RTZ bounds.
