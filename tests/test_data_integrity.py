"""
Data-integrity and reproducibility tests for the KineticAI-AWGC repository.

These tests codify the invariant checks described in VALIDATION.md:

- phase-fraction closure (phase compositions sum to 100 %);
- consistency between related datasets;
- conformity of qualitative labels to standard categories;
- reproducibility of the reported kinetic and machine-learning results.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
PROC = DATA / "processed"

PHASE_COLS = ["amorphous_pct", "wollastonite_pct", "hydroxyapatite_pct", "whitlockite_pct"]
MASTER_PHASE_COLS = [
    "Amorphous_Percent",
    "Wollastonite_Percent",
    "Hydroxyapatite_Percent",
    "Whitlockite_Percent",
]

CLOSURE_TOLERANCE = 0.06


def test_initial_phase_composition_sums_to_100():
    """The initial phase composition must close to 100 % at every temperature."""
    df = pd.read_csv(RAW / "initial_phase_composition.csv")
    deviation = (df[PHASE_COLS].sum(axis=1) - 100).abs()
    assert deviation.max() <= CLOSURE_TOLERANCE


def test_sbf_phase_evolution_sums_to_100():
    """Every SBF phase-evolution row must close to 100 %."""
    df = pd.read_csv(RAW / "sbf_phase_evolution.csv")
    deviation = (df[PHASE_COLS].sum(axis=1) - 100).abs()
    assert deviation.max() <= CLOSURE_TOLERANCE


def test_master_phase_composition_sums_to_100():
    """The master-dataset phase composition must close to 100 %."""
    df = pd.read_csv(DATA / "kinetic_blueprint_master.csv")
    deviation = (df[MASTER_PHASE_COLS].sum(axis=1) - 100).abs()
    assert deviation.max() <= CLOSURE_TOLERANCE


def test_processed_datasets_contain_no_missing_values():
    """Analysis-ready datasets must be free of missing values."""
    datasets = [
        "awgc_ml_dataset.csv",
        "model_results.csv",
        "feature_importance.csv",
        "korsmeyer_peppas_parameters.csv",
        "transport_kinetics.csv",
        "ph_evolution.csv",
    ]
    for name in datasets:
        df = pd.read_csv(PROC / name)
        assert df.notna().all().all(), f"{name} contains missing values"


def test_final_ph_is_consistent_between_datasets():
    """Final_pH_21d in the master dataset must equal the day-21 pH record
    for every temperature for which the pH time series provides a value."""
    master = pd.read_csv(DATA / "kinetic_blueprint_master.csv")
    ph = pd.read_csv(DATA / "pH_time_series.csv")
    final_ph = ph[ph["Time_Days"] == 21].set_index("Temperature_C")["pH_Value"]

    # The pH time series covers the 700 C and 1100 C conditions; the
    # consistency invariant applies to that intersection.
    for temperature in final_ph.index:
        row = master[master["Temperature_C"] == temperature].iloc[0]
        assert abs(row["Final_pH_21d"] - final_ph[temperature]) < 1e-6


def test_iso_statuses_conform_to_standard_categories():
    """Biological-response labels must use the standard ISO 10993-5 categories."""
    bio = pd.read_csv(DATA / "biological_response.csv")
    allowed = {"Non-Cytotoxic", "Cytotoxic (<70%)"}
    assert set(bio["ISO_10993_Status"]).issubset(allowed)


def test_korsmeyer_peppas_parameters_are_reproducible():
    """The reported Korsmeyer-Peppas parameters must be reproduced by a
    linear fit of the committed transport time series."""
    transport = pd.read_csv(PROC / "transport_kinetics.csv")
    reported = pd.read_csv(PROC / "korsmeyer_peppas_parameters.csv").set_index("Temperature")

    for temperature in [700, 1100]:
        subset = transport[transport["Temperature"] == temperature]
        model = LinearRegression().fit(
            subset["ln_t"].values.reshape(-1, 1),
            subset["ln_F"].values,
        )
        exponent = model.coef_[0]
        constant = np.exp(model.intercept_)

        assert abs(exponent - reported.loc[temperature, "n"]) < 0.01
        assert abs(constant - reported.loc[temperature, "k"]) < 0.001


def test_model_results_contain_both_evaluation_schemes():
    """model_results.csv must report both evaluation schemes."""
    df = pd.read_csv(PROC / "model_results.csv")
    assert set(df["scheme"]) == {"fixed_80_20_split", "leave_one_temperature_out_cv"}


def test_ml_dataset_has_expected_shape_and_no_duplicates():
    """The machine-learning dataset must contain 25 unique samples."""
    df = pd.read_csv(PROC / "awgc_ml_dataset.csv")
    assert len(df) == 25
    assert df.duplicated().sum() == 0
