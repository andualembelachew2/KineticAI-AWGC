"""Public API for trajectory-engineering simulations.

Entry points of the Kinetic Blueprint workflow:

Transport
    simulate_moving_boundary_1d
        Forward 1D moving-boundary reaction-diffusion simulation.

Regime mapping
    da_pe_from_state
        Damköhler and Péclet numbers from a simulation state.
    classify_regime
        Transport-regime classification from (Da, Pe).

Regenerative Target Zone (RTZ)
    admissible_tube
        Spatio-temporal admissibility tube for ion and pH trajectories.
    phase_trajectory_distance
        Distance of a trajectory from the admissible region.
"""

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
