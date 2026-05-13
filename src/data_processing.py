
"""
Data processing utilities for the KineticAI-AWGC project.

This script loads raw experimental datasets and prepares a merged
machine-learning dataset for modeling phase evolution and bioactivity
trends in spray-pyrolyzed apatite-wollastonite glass-ceramics.
"""

from pathlib import Path
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"


def load_initial_phase_data():
    """
    Load initial phase composition data.

    Returns
    -------
    pandas.DataFrame
        Initial phase composition as a function of sintering temperature.
    """
    file_path = RAW_DATA_DIR / "initial_phase_composition.csv"
    return pd.read_csv(file_path)


def load_sbf_phase_data():
    """
    Load SBF phase evolution data.

    Returns
    -------
    pandas.DataFrame
        Phase composition after simulated body fluid immersion.
    """
    file_path = RAW_DATA_DIR / "sbf_phase_evolution.csv"
    return pd.read_csv(file_path)


def create_ml_dataset():
    """
    Merge initial phase composition with SBF phase evolution data
    and generate engineered features for machine learning.

    Returns
    -------
    pandas.DataFrame
        Processed machine-learning dataset.
    """
    initial_df = load_initial_phase_data()
    sbf_df = load_sbf_phase_data()

    initial_df = initial_df.rename(
        columns={
            "amorphous_pct": "initial_amorphous_pct",
            "wollastonite_pct": "initial_wollastonite_pct",
            "hydroxyapatite_pct": "initial_hydroxyapatite_pct",
            "whitlockite_pct": "initial_whitlockite_pct",
        }
    )

    sbf_df = sbf_df.rename(
        columns={
            "amorphous_pct": "sbf_amorphous_pct",
            "wollastonite_pct": "sbf_wollastonite_pct",
            "hydroxyapatite_pct": "sbf_hydroxyapatite_pct",
            "whitlockite_pct": "sbf_whitlockite_pct",
        }
    )

    ml_df = sbf_df.merge(initial_df, on="temperature_C", how="left")

    ml_df["initial_crystallinity_pct"] = 100 - ml_df["initial_amorphous_pct"]
    ml_df["sbf_crystallinity_pct"] = 100 - ml_df["sbf_amorphous_pct"]

    ml_df["hydroxyapatite_gain_pct"] = (
        ml_df["sbf_hydroxyapatite_pct"]
        - ml_df["initial_hydroxyapatite_pct"]
    )

    ml_df["wollastonite_change_pct"] = (
        ml_df["sbf_wollastonite_pct"]
        - ml_df["initial_wollastonite_pct"]
    )

    return ml_df


def save_ml_dataset():
    """
    Save the processed machine-learning dataset as a CSV file.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    ml_df = create_ml_dataset()
    output_path = PROCESSED_DATA_DIR / "awgc_ml_dataset.csv"
    ml_df.to_csv(output_path, index=False)

    print(f"Processed dataset saved to: {output_path}")


if __name__ == "__main__":
    save_ml_dataset()
