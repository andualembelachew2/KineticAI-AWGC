"""Importable trajectory-engineering API under the src package namespace."""

from src.analysis.regime_mapper import classify_regime, da_pe_from_state
from src.analysis.rtz_classifier import admissible_tube, phase_trajectory_distance
from src.transport.moving_boundary_solver import simulate_moving_boundary_1d

__all__ = [
    "admissible_tube",
    "classify_regime",
    "da_pe_from_state",
    "phase_trajectory_distance",
    "simulate_moving_boundary_1d",
]
