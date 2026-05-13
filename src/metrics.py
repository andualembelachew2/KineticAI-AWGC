
"""
Evaluation metrics for the KineticAI-AWGC project.

This module provides helper functions for evaluating phase-fraction
prediction models in a scientifically interpretable way.
"""

import pandas as pd

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_regression_model(y_true, y_pred, target_names=None):
    """
    Evaluate a regression model using standard regression metrics.

    Parameters
    ----------
    y_true : array-like
        Experimental target values.
    y_pred : array-like
        Predicted target values.
    target_names : list, optional
        Names of predicted target variables.

    Returns
    -------
    pandas.DataFrame
        Regression metrics for each target variable.
    """
    if target_names is None:
        target_names = [f"target_{i}" for i in range(y_true.shape[1])]

    results = []

    for i, target in enumerate(target_names):
        results.append(
            {
                "target": target,
                "MAE": mean_absolute_error(y_true.iloc[:, i], y_pred[:, i]),
                "MSE": mean_squared_error(y_true.iloc[:, i], y_pred[:, i]),
                "R2": r2_score(y_true.iloc[:, i], y_pred[:, i]),
            }
        )

    return pd.DataFrame(results)


def summarize_model_results(results):
    """
    Convert model training results into a readable summary table.

    Parameters
    ----------
    results : dict
        Dictionary containing model names and evaluation metrics.

    Returns
    -------
    pandas.DataFrame
        Summary table of model-level metrics.
    """
    rows = []

    for model_name, metrics in results.items():
        rows.append(
            {
                "model": model_name,
                "MAE": metrics["mae"],
                "MSE": metrics["mse"],
                "R2": metrics["r2"],
            }
        )

    return pd.DataFrame(rows)
