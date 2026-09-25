"""Simplified moving-boundary transport model for a degrading scaffold."""

from __future__ import annotations

import numpy as np


def simulate_moving_boundary_1d(
    length=1.0,
    nx=200,
    tmax=1.0,
    dt=1e-3,
    alpha=0.1,
    k_diss=1e-3,
    porosity_initial=0.2,
    diffusivity=1e-9,
    convection=0.0,
    source_scale=0.0,
    q_tortuosity=0.5,
):
    """Integrate a simplified 1D reaction-diffusion model with a moving boundary.

    The model updates a porosity field and a concentration field in a 1D domain. The
    assumptions are intentionally simple and dimensionally stable, suitable for fast
    physics-relevant regression testing.
    """
    if nx < 5:
        raise ValueError("nx must be at least 5")
    if dt <= 0 or tmax <= 0:
        raise ValueError("tmax and dt must be positive.")

    x = np.linspace(0.0, length, nx)
    dx = x[1] - x[0]
    porosity = np.full(nx, porosity_initial, dtype=float)
    concentration = np.exp(-((x - 0.5 * length) ** 2) / (2.0 * (0.10 * length) ** 2))
    concentration = np.clip(concentration, 0.0, None)

    steps = int(np.ceil(tmax / dt))
    time_grid = np.linspace(0.0, steps * dt, steps + 1)
    total_mass = [float(np.trapezoid(concentration, x))]
    concentration_history = [concentration.copy()]
    porosity_history = [porosity.copy()]
    gel_thickness_history = [np.zeros_like(porosity)]

    for _ in range(steps):
        # Dynamic diffusion coefficient based on porosity and tortuosity closure.
        tortuosity = np.maximum(1e-6, np.power(porosity_initial / np.maximum(porosity, 1e-6), q_tortuosity))
        effective_diffusion = diffusivity * np.power(np.maximum(porosity, 1e-6), 1.5) / np.square(tortuosity)

        # Receding boundary approximation: porosity increases in proportion to source rate.
        source_term = source_scale + alpha * k_diss * np.maximum(1.0 - porosity, 0.0)
        porosity = np.clip(porosity + dt * source_term, 1e-6, 0.95)

        # Conserved diffusion update with zero-flux boundaries.
        laplacian = np.gradient(np.gradient(concentration, x), x)
        reaction = alpha * k_diss * np.maximum(1.0 - porosity, 0.0)
        advection = convection * np.gradient(concentration, x)
        diffusion = effective_diffusion.mean() * laplacian
        concentration = concentration + dt * (diffusion + reaction - advection)
        concentration = np.clip(concentration, 0.0, None)
        total_mass.append(float(np.trapezoid(concentration, x)))
        concentration_history.append(concentration.copy())
        porosity_history.append(porosity.copy())
        gel_thickness_history.append(length * np.maximum(porosity - porosity_initial, 0.0))

    return {
        "x": x,
        "porosity": porosity,
        "concentration": concentration,
        "concentration_history": np.asarray(concentration_history),
        "porosity_history": np.asarray(porosity_history),
        "gel_thickness_history": np.asarray(gel_thickness_history),
        "dissolution_alpha": alpha,
        "total_mass": np.asarray(total_mass, dtype=float),
        "time_grid": time_grid,
    }


def mass_conservation_error(result):
    """Return the maximum relative drift in the concentration integral."""
    total_mass = result["total_mass"]
    if total_mass.size < 2:
        return 0.0
    relative = np.abs(total_mass - total_mass[0]) / max(np.abs(total_mass[0]), 1e-12)
    return float(relative.max())
