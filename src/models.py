
"""
Machine-learning models for the KineticAI-AWGC project.

This module provides baseline regression models for predicting
phase fractions in spray-pyrolyzed apatite-wollastonite glass-ceramics.
"""

from pathlib import Path
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


FEATURE_COLUMNS = [
    "temperature_C",
    "soaking_day",
    "initial_amorphous_pct",
    "initial_wollastonite_pct",
    "initial_hydroxyapatite_pct",
    "initial_whitlockite_pct",
    "initial_crystallinity_pct",
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


def train_baseline_models(test_size=0.2, random_state=42):
    """
    Train baseline machine-learning models for phase-fraction prediction.

    Parameters
    ----------
    test_size : float
        Fraction of dataset used for testing.
    random_state : int
        Random seed for reproducibility.

    Returns
    -------
    dict
        Dictionary containing trained models and evaluation results.
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

    models = {
        "linear_regression": LinearRegression(),
        "random_forest": RandomForestRegressor(
            n_estimators=100,
            random_state=random_state,
        ),
    }

    results = {}

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        results[model_name] = {
            "model": model,
            "mae": mean_absolute_error(y_test, predictions),
            "mse": mean_squared_error(y_test, predictions),
            "r2": r2_score(y_test, predictions),
        }

    return results


if __name__ == "__main__":
    results = train_baseline_models()

    for model_name, metrics in results.items():
        print(f"\nModel: {model_name}")
        print(f"MAE: {metrics['mae']:.3f}")
        print(f"MSE: {metrics['mse']:.3f}")
        print(f"R2: {metrics['r2']:.3f}")
