import numpy as np

from src.analysis.regime_mapper import classify_regime, da_pe_from_state
from src.analysis.rtz_classifier import admissible_tube, inside_rtz
from src.chemistry.reactivity import alpha_arrhenius, nbo_bo_ratio, qn_mean_connectivity
from src.transport.moving_boundary_solver import mass_conservation_error, simulate_moving_boundary_1d


def test_alpha_arrhenius_is_positive_and_dimensionless():
    qn = np.array([0.10, 0.25, 0.40, 0.20, 0.05])
    energies = np.array([90000.0, 70000.0, 50000.0, 35000.0, 25000.0])
    alpha = alpha_arrhenius(qn, energies, temperature=298.15)
    assert alpha > 0.0
    assert np.isfinite(alpha)


def test_qn_mean_connectivity_is_in_range():
    qn = np.array([0.10, 0.25, 0.40, 0.20, 0.05])
    connectivity = qn_mean_connectivity(qn)
    assert 0.0 < connectivity < 4.0


def test_nbo_bo_ratio_monotonic_and_positive():
    ratio = nbo_bo_ratio(12.0, 8.0)
    assert ratio > 0.0
    assert ratio == 1.5


def test_moving_boundary_solver_preserves_mass_without_source():
    result = simulate_moving_boundary_1d(
        length=1.0,
        nx=150,
        tmax=0.1,
        dt=1e-3,
        alpha=0.0,
        k_diss=1e-3,
        source_scale=0.0,
    )
    assert mass_conservation_error(result) < 1e-2
    assert np.all(result["porosity"] > 0.0)
    assert np.all(result["concentration"] >= 0.0)


def test_regime_classification_returns_known_quadrant():
    da, pe = da_pe_from_state(alpha=0.8, k_diss=0.7, beta=1.2, length=1.5, effective_diffusivity=1.0, velocity=0.2)
    regime = classify_regime(da, pe)
    assert "Q" in regime
    assert regime.startswith("Q")


def test_rtz_bounds_are_respected_for_admissible_segment():
    values = np.array([0.5, 0.7, 0.9])
    lower = np.array([0.4, 0.6, 0.8])
    upper = np.array([0.6, 0.8, 1.0])
    assert inside_rtz(values, lower, upper, tolerance=1e-8)
    assert admissible_tube(values, lower, upper, tolerance=1e-8)
