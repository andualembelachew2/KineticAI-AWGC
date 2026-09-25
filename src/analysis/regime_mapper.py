"""Damk\"ohler and P\'eclet regime classification for trajectory engineering."""

from __future__ import annotations

import numpy as np


def da_pe_from_state(alpha, k_diss, beta, length, effective_diffusivity, velocity):
    """Compute the reaction-transport numbers for a given local state."""
    da = (k_diss * alpha * beta * length**2) / max(effective_diffusivity, 1e-12)
    pe = (velocity * length) / max(effective_diffusivity, 1e-12)
    return float(da), float(pe)


def classify_regime(da, pe):
    """Return a text regime label based on Damk\"ohler and P\'eclet values."""
    if da < 1.0 and pe < 1.0:
        return "Q1 reaction-limited"
    if da >= 1.0 and pe < 1.0:
        return "Q2 diffusion-limited burst"
    if da < 1.0 and pe >= 1.0:
        return "Q3 convective washout"
    return "Q4 convection-amplified"


def design_corridor_score(da, pe):
    """Score proximity to the nominal design corridor where Da ~ 1 and Pe ~ 1."""
    return float(-abs(np.log10(da + 1e-12) + 0.0) - abs(np.log10(pe + 1e-12) - 0.0))
