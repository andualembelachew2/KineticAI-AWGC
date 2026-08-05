"""
Machine-learning models for the KineticAI-AWGC project.

This module provides baseline regression models for predicting
phase fractions in spray-pyrolyzed apatite-wollastonite glass-ceramics.

Evaluation strategy
-------------------
Because the dataset covers only five sintering temperatures (25 samples),
a single fixed split is not a reliable estimate of predictive performance.
We therefore report:

1. a fixed 80/20 train/test split (for direct comparison with earlier
   results), and
2. leave-one-temperature-out cross-validation (LOTO-CV): each fold holds
   out every sample of one sintering temperature. This is the appropriate
   generalization test for predicting a *new processing condition*.
"""

from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


ROOT_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"


TARGET_COLUMNS = [
    "sbf_amorphous_pct",
    "sbf_wollastonite_pct",
    "sbf_hydroxyapatite_pct",
    "sbf_whitlockite_pct",
]

# Note: "initial_crystallinity_pct" is intentionally excluded: it is an
# exact linear transform of "initial_amorphous_pct" (100 - amorphous),
# so it carries no additional information as a feature.
FEATURE_COLUMNS = [
    "temperature_C",
    "soaking_day",
    "initial_amorphous_pct",
    "initial_wollastonite_pct",
    "initial_hydroxyapatite_pct",
    "initial_whitlockite_pct",
]


def load_ml_dataset():
    """
    Load the processed machine-learning dataset.

    Returns
    -------
    pandas.DataFrame
        Processed AWGC machine-learning dataset.
    """
    file_path = PROCESSED_DATA_DIR / "awgc_ml_dataset.csv"
    return pd.read_csv(file_path)


def _make_models(random_state=42):
    """Return the baseline model zoo (shared by all evaluation schemes)."""
    return {
        "linear_regression": LinearRegression(),
        "random_forest": RandomForestRegressor(
            n_estimators=100,
            random_state=random_state,
        ),
    }


def train_baseline_models(test_size=0.2, random_state=42):
    """
    Train baseline models on a single fixed 80/20 split.

    Provided for direct comparison with the original workflow; use
    leave_one_temperature_out_cv() for the generalization estimate.
    """
    df = load_ml_dataset()

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMNS]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
    )

    results = {}

    for model_name, model in _make_models(random_state).items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        results[model_name] = {
            "model": model,
            "mae": mean_absolute_error(y_test, predictions),
            "mse": mean_squared_error(y_test, predictions),
            "r2": r2_score(y_test, predictions),
        }

    return results


def leave_one_temperature_out_cv(random_state=42):
    """
    Leave-one-temperature-out cross-validation.

    Each fold trains on four sintering temperatures and predicts all
    samples of the held-out temperature (700-1100 C). Predictions from
    all folds are aggregated into a single MAE/MSE/R2 per model.

    Returns
    -------
    dict
        Dictionary containing trained models and evaluation results.
    """
    df = load_ml_dataset()

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMNS]

    results = {}

    for model_name, model in _make_models(random_state).items():
        y_true_parts = []
        y_pred_parts = []

        for temperature in sorted(df["temperature_C"].unique()):
            held_out = df["temperature_C"] == temperature

            model.fit(X[~held_out], y[~held_out])
            y_true_parts.append(y[held_out].to_numpy())
            y_pred_parts.append(model.predict(X[held_out]))

        y_true = np.vstack(y_true_parts)
        y_pred = np.vstack(y_pred_parts)

        results[model_name] = {
            "model": model,
            "mae": mean_absolute_error(y_true, y_pred),
            "mse": mean_squared_error(y_true, y_pred),
            "r2": r2_score(y_true, y_pred),
        }

    return results


def feature_importance(random_state=42):
    """
    Random-forest feature importances computed on the full dataset.

    Returns
    -------
    pandas.DataFrame
        Features sorted by importance (descending).
    """
    df = load_ml_dataset()

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMNS]

    rf = RandomForestRegressor(n_estimators=100, random_state=random_state)
    rf.fit(X, y)

    importance_df = pd.DataFrame(
        {
            "feature": FEATURE_COLUMNS,
            "importance": rf.feature_importances_,
        }
    ).sort_values("importance", ascending=False)

    return importance_df.reset_index(drop=True)


def save_ml_results(random_state=42):
    """
    Re-run both evaluation schemes and write the results to
    data/processed/model_results.csv and feature_importance.csv.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    split_results = train_baseline_models(random_state=random_state)
    loto_results = leave_one_temperature_out_cv(random_state)

    split_summary = summarize_model_results(split_results)
    split_summary.insert(0, "scheme", "fixed_80_20_split")

    loto_summary = summarize_model_results(loto_results)
    loto_summary.insert(0, "scheme", "leave_one_temperature_out_cv")

    summary = pd.concat([split_summary, loto_summary], ignore_index=True)

    results_path = PROCESSED_DATA_DIR / "model_results.csv"
    summary.to_csv(results_path, index=False)
    print(f"Model results saved to: {results_path}")

    importance_df = feature_importance(random_state)
    importance_path = PROCESSED_DATA_DIR / "feature_importance.csv"
    importance_df.to_csv(importance_path, index=False)
    print(f"Feature importance saved to: {importance_path}")


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
    display_names = {
        "linear_regression": "Linear Regression",
        "random_forest": "Random Forest",
    }

    rows = []

    for model_name, metrics in results.items():
        rows.append(
            {
                "model": display_names.get(model_name, model_name),
                "MAE": metrics["mae"],
                "MSE": metrics["mse"],
                "R2": metrics["r2"],
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    print("Fixed 80/20 split (reference only):")
    for model_name, metrics in train_baseline_models().items():
        print(
            f"  {model_name}: MAE={metrics['mae']:.3f}  "
            f"MSE={metrics['mse']:.3f}  R2={metrics['r2']:.3f}"
        )

    print("\nLeave-one-temperature-out cross-validation:")
    for model_name, metrics in leave_one_temperature_out_cv().items():
        print(
            f"  {model_name}: MAE={metrics['mae']:.3f}  "
            f"MSE={metrics['mse']:.3f}  R2={metrics['r2']:.3f}"
        )

    save_ml_results()
