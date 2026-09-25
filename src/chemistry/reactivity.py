"""Reactive-speciation models for silicate dissolution and network reactivity."""

from __future__ import annotations

import numpy as np


R_GAS = 8.31446261815324


def alpha_arrhenius(qn_distribution, activation_energies, temperature=298.15, weights=None):
    """Estimate an Arrhenius-weighted network reactivity from a Q^n distribution.

    Parameters
    ----------
    qn_distribution : array-like
        Fractions for Q^0 to Q^4 species. Must sum to approximately 1.
    activation_energies : array-like
        Activation energies in J/mol corresponding to each Q^n contribution.
    temperature : float, default 298.15
        Absolute temperature in kelvin.
    weights : array-like, optional
        Optional multiplicative amplitudes for each Q^n. Defaults to ones.

    Returns
    -------
    float
        Dimensionless activity-like measure of network reactivity.
    """
    f = np.asarray(qn_distribution, dtype=float)
    e = np.asarray(activation_energies, dtype=float)
    if weights is None:
        w = np.ones_like(f)
    else:
        w = np.asarray(weights, dtype=float)
    if f.shape != e.shape or f.shape != w.shape:
        raise ValueError("qn_distribution, activation_energies, and weights must share the same shape.")
    if np.any(f < 0):
        raise ValueError("Q^n fractions must be non-negative.")
    if not np.isclose(np.sum(f), 1.0, atol=1e-6):
        raise ValueError("Q^n fractions must sum to 1.")
    return float(np.sum(f * w * np.exp(-e / (R_GAS * temperature))))


def dissolution_rate(alpha, k0, network_concentration):
    """Return a pseudo-first-order dissolution rate."""
    return float(alpha * k0 * network_concentration)


def nbo_bo_ratio(nbo_area, bo_area):
    if bo_area <= 0:
        raise ValueError("bo_area must be positive.")
    return float(nbo_area / bo_area)


def qn_mean_connectivity(qn_distribution):
    f = np.asarray(qn_distribution, dtype=float)
    if np.any(f < 0):
        raise ValueError("Q^n fractions must be non-negative.")
    n_index = np.arange(len(f))
    return float(np.dot(f, n_index))
