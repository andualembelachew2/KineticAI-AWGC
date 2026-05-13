
"""
Visualization utilities for the KineticAI-AWGC project.

This module contains plotting functions for phase evolution,
SBF-induced transformation, and hydroxyapatite formation trends.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"
FIGURES_DIR = ROOT_DIR / "figures"


def load_initial_phase_data():
    """Load initial phase composition dataset."""
    file_path = RAW_DATA_DIR / "initial_phase_composition.csv"
    return pd.read_csv(file_path)


def load_sbf_phase_data():
    """Load SBF phase evolution dataset."""
    file_path = RAW_DATA_DIR / "sbf_phase_evolution.csv"
    return pd.read_csv(file_path)


def plot_initial_phase_map(save=True):
    """
    Plot initial phase composition as a function of sintering temperature.
    """
    df = load_initial_phase_data()

    plt.figure(figsize=(8, 5))
    plt.plot(df["temperature_C"], df["amorphous_pct"], marker="o", label="Amorphous")
    plt.plot(df["temperature_C"], df["wollastonite_pct"], marker="o", label="Wollastonite")
    plt.plot(df["temperature_C"], df["hydroxyapatite_pct"], marker="o", label="Hydroxyapatite")
    plt.plot(df["temperature_C"], df["whitlockite_pct"], marker="o", label="Whitlockite")

    plt.xlabel("Sintering temperature (°C)")
    plt.ylabel("Phase fraction (%)")
    plt.title("Initial Phase Composition of AWGC")
    plt.legend()
    plt.tight_layout()

    if save:
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        plt.savefig(FIGURES_DIR / "initial_phase_composition.png", dpi=300)

    plt.show()


def plot_sbf_hydroxyapatite_evolution(save=True):
    """
    Plot hydroxyapatite evolution during SBF immersion.
    """
    df = load_sbf_phase_data()

    plt.figure(figsize=(8, 5))

    for temperature in sorted(df["temperature_C"].unique()):
        subset = df[df["temperature_C"] == temperature]
        plt.plot(
            subset["soaking_day"],
            subset["hydroxyapatite_pct"],
            marker="o",
            label=f"{temperature} °C",
        )

    plt.xlabel("SBF soaking time (days)")
    plt.ylabel("Hydroxyapatite fraction (%)")
    plt.title("Hydroxyapatite Evolution During SBF Immersion")
    plt.legend(title="Sintering temperature")
    plt.tight_layout()

    if save:
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        plt.savefig(FIGURES_DIR / "sbf_hydroxyapatite_evolution.png", dpi=300)

    plt.show()


def plot_sbf_wollastonite_evolution(save=True):
    """
    Plot wollastonite evolution during SBF immersion.
    """
    df = load_sbf_phase_data()

    plt.figure(figsize=(8, 5))

    for temperature in sorted(df["temperature_C"].unique()):
        subset = df[df["temperature_C"] == temperature]
        plt.plot(
            subset["soaking_day"],
            subset["wollastonite_pct"],
            marker="o",
            label=f"{temperature} °C",
        )

    plt.xlabel("SBF soaking time (days)")
    plt.ylabel("Wollastonite fraction (%)")
    plt.title("Wollastonite Evolution During SBF Immersion")
    plt.legend(title="Sintering temperature")
    plt.tight_layout()

    if save:
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        plt.savefig(FIGURES_DIR / "sbf_wollastonite_evolution.png", dpi=300)

    plt.show()


if __name__ == "__main__":
    plot_initial_phase_map()
    plot_sbf_hydroxyapatite_evolution()
    plot_sbf_wollastonite_evolution()
