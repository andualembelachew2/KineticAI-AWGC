"""Utilities for classifying whether a trajectory remains inside a regenerative target zone."""

from __future__ import annotations

import numpy as np


def phase_trajectory_distance(values, lower_bound, upper_bound):
    """Return the signed distance of a 1D trajectory to the admissible tube bounds."""
    values = np.asarray(values, dtype=float)
    lower = np.asarray(lower_bound, dtype=float)
    upper = np.asarray(upper_bound, dtype=float)
    if values.shape != lower.shape or values.shape != upper.shape:
        raise ValueError("values, lower_bound, and upper_bound must share a shape.")
    max_below = np.max(np.clip(lower - values, 0.0, None))
    max_above = np.max(np.clip(values - upper, 0.0, None))
    return float(max(max_below, max_above))


def inside_rtz(values, lower_bound, upper_bound, tolerance=1e-8):
    """Return True when the trajectory remains inside the admissible tube."""
    return phase_trajectory_distance(values, lower_bound, upper_bound) <= tolerance


def admissible_tube(array, lower_bounds, upper_bounds, tolerance=1e-8):
    """Check a multi-dimensional trajectory against a set of independent bounds."""
    array = np.asarray(array, dtype=float)
    lower = np.asarray(lower_bounds, dtype=float)
    upper = np.asarray(upper_bounds, dtype=float)
    if array.shape != lower.shape or array.shape != upper.shape:
        raise ValueError("array, lower_bounds, and upper_bounds must share a shape.")
    return bool(np.all(array >= lower - tolerance) and np.all(array <= upper + tolerance))
