
"""
Visualization utilities for the KineticAI-AWGC project.

This module contains plotting functions for phase evolution,
SBF-induced transformation, and hydroxyapatite formation trends.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"
FIGURES_DIR = ROOT_DIR / "figures"
PUBLICATION_EXPORT_DIR = FIGURES_DIR / "exports"
PUBLICATION_PRINT_DIR = FIGURES_DIR / "print"


def _publication_style():
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "DejaVu Sans"],
            "font.size": 9,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 7.5,
            "svg.fonttype": "none",
        }
    )


def _style_axis(ax, show_right_spine=False):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(show_right_spine)
    for spine in ("left", "bottom", "right"):
        ax.spines[spine].set_linewidth(0.8)
    ax.tick_params(direction="out", width=0.8, length=3)


def _save_publication_figure(fig, figure_name):
    PUBLICATION_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    PUBLICATION_PRINT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PUBLICATION_EXPORT_DIR / f"{figure_name}.svg", bbox_inches="tight")
    fig.savefig(
        PUBLICATION_PRINT_DIR / f"{figure_name}.png",
        dpi=600,
        bbox_inches="tight",
    )


def fig_cytotoxicity(save=True):
    """Plot mean cell viability and sample SD by extract and sintering temperature."""
    _publication_style()
    df = pd.read_csv(RAW_DATA_DIR / "cytotoxicity_iso10993.csv")
    summary = (
        df.groupby(["Sintering_Temp_C", "Extract_Percent"])["Cell_Viability_Percent"]
        .agg(["mean", "std"])
        .reset_index()
    )
    extracts = sorted(df["Extract_Percent"].unique())
    positions = range(len(extracts))
    width = 0.36
    colors = {700: "#D55E5E", 1100: "#0072B2"}

    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    for offset, temperature in ((-width / 2, 700), (width / 2, 1100)):
        subset = summary[summary["Sintering_Temp_C"] == temperature].set_index("Extract_Percent")
        ax.bar(
            [position + offset for position in positions],
            [subset.loc[value, "mean"] for value in extracts],
            width,
            yerr=[subset.loc[value, "std"] for value in extracts],
            capsize=3,
            color=colors[temperature],
            edgecolor="white",
            linewidth=0.5,
            error_kw={"elinewidth": 0.8, "capthick": 0.8},
            label=f"{temperature} °C",
        )

    ax.axhline(
        70,
        color="#B22222",
        linestyle="--",
        linewidth=1.1,
        label="ISO 10993-5 Non-Cytotoxic Limit (70%)",
    )
    ax.set_xlim(-0.55, 4.95)
    ax.set_ylim(0, 340)
    ax.set_xticks(list(positions), [f"{value}%" for value in extracts])
    ax.set_xlabel("Extract concentration (%)")
    ax.set_ylabel("Cell viability (%)")
    ax.legend(frameon=False, ncol=3, loc="upper center")
    _style_axis(ax)
    fig.tight_layout()
    if save:
        _save_publication_figure(fig, "fig_cytotoxicity")
    return fig


def fig_phase_evolution(save=True):
    """Plot phase fractions and bulk density across sintering temperatures."""
    _publication_style()
    df = pd.read_csv(RAW_DATA_DIR / "sintering_phase_kinetics.csv")
    fig, ax = plt.subplots(figsize=(6.8, 4.5))
    temperatures = df["Temperature_C"].to_numpy()
    x = range(len(df))
    phases = [
        ("Amorphous_Percent", "Amorphous", "#8C8C8C"),
        ("Wollastonite_Percent", "Wollastonite", "#009E73"),
        ("Whitlockite_Percent", "Whitlockite", "#E69F00"),
        ("Hydroxyapatite_Percent", "Hydroxyapatite", "#56B4E9"),
    ]
    bottom = [0.0] * len(df)
    for column, label, color in phases:
        values = df[column].to_numpy()
        ax.bar(x, values, bottom=bottom, width=0.68, color=color, label=label, linewidth=0)
        bottom = [base + value for base, value in zip(bottom, values)]

    density_ax = ax.twinx()
    density_ax.plot(
        list(x),
        df["Bulk_Density_g_cm3"],
        "-D",
        color="#36454F",
        linewidth=1.5,
        markersize=4.5,
        label="Bulk density",
        zorder=4,
    )
    ax.set_xticks(list(x), [str(value) for value in temperatures])
    ax.set_xlabel("Sintering temperature (°C)")
    ax.set_ylabel("Phase fraction (%)")
    density_ax.set_ylabel("Bulk density (g cm⁻³)")
    density_ax.set_ylim(1.8, 3.0)
    _style_axis(ax)
    _style_axis(density_ax, show_right_spine=True)
    handles, labels = ax.get_legend_handles_labels()
    density_handles, density_labels = density_ax.get_legend_handles_labels()
    fig.legend(
        handles + density_handles,
        labels + density_labels,
        frameon=False,
        ncol=5,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.99),
    )
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    if save:
        _save_publication_figure(fig, "fig_phase_evolution")
    return fig


def fig_ph_dynamics(save=True):
    """Plot interfacial pH dynamics and physiological/cytotoxic reference regions."""
    _publication_style()
    df = pd.read_csv(RAW_DATA_DIR / "sbf_ph_dynamics_21d.csv")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    ax.axhspan(7.35, 7.85, color="#70AD47", alpha=0.16, zorder=0)
    ax.axhspan(8.2, 8.7, color="#D55E5E", alpha=0.12, zorder=0)
    colors = {700: "#D55E5E", 1100: "#0072B2"}
    for temperature in (700, 1100):
        subset = df[df["Temperature_C"] == temperature].sort_values("Time_Days")
        ax.plot(
            subset["Time_Days"],
            subset["pH_Value"],
            marker="o",
            markersize=4,
            linewidth=1.7,
            color=colors[temperature],
            label=f"{temperature} °C",
        )
    ax.set_xlim(-0.5, 22)
    ax.set_ylim(7.2, 8.7)
    ax.set_xticks([0, 1, 3, 5, 7, 14, 21])
    ax.set_xlabel("Immersion time (days)")
    ax.set_ylabel("Interfacial pH")
    ax.legend(frameon=False, loc="upper left")
    _style_axis(ax)
    fig.tight_layout()
    if save:
        _save_publication_figure(fig, "fig_ph_dynamics")
    return fig


def fig_xrd_stack(save=True):
    """Plot baseline-offset X-ray diffractograms for the five sintering temperatures."""
    _publication_style()
    df = pd.read_csv(RAW_DATA_DIR / "xrd_diffractograms_2theta.csv")
    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    temperatures = (700, 800, 900, 1000, 1100)
    colors = ["#0072B2", "#009E73", "#E69F00", "#D55E5E", "#6B6B6B"]
    offset_step = 6200
    two_theta = df["2Theta_deg"].to_numpy()
    segments = np.split(np.arange(len(df)), np.where(np.diff(two_theta) > 1.0)[0] + 1)
    for index, (temperature, color) in enumerate(zip(temperatures, colors)):
        intensity = df[f"Intensity_{temperature}C"]
        offset = index * offset_step
        for segment in segments:
            ax.plot(
                two_theta[segment],
                intensity.iloc[segment] + offset,
                color=color,
                linewidth=1.15,
                marker="o",
                markersize=1.5,
            )
        ax.text(80.65, offset + intensity.iloc[-1], f"{temperature} °C", color=color, va="center", fontsize=8)
    ax.set_xlim(19.7, 85.0)
    ax.set_ylim(-250, offset_step * (len(temperatures) - 1) + 6500)
    ax.set_xlabel(r"2$\theta$ (°)")
    ax.set_ylabel("Intensity (a.u., offset)")
    ax.set_yticks([])
    _style_axis(ax)
    fig.tight_layout()
    if save:
        _save_publication_figure(fig, "fig_xrd_stack")
    return fig


def load_initial_phase_data():
    """Load initial phase composition dataset."""
    file_path = RAW_DATA_DIR / "initial_phase_composition.csv"
    return pd.read_csv(file_path)


def load_sbf_phase_data():
    """Load SBF phase evolution dataset."""
    file_path = RAW_DATA_DIR / "sbf_phase_evolution.csv"
    return pd.read_csv(file_path)


def _save_legacy_figure(fig, figure_name, output_dir=FIGURES_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)
    PUBLICATION_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_dir / f"{figure_name}.png", dpi=600, bbox_inches="tight")
    fig.savefig(PUBLICATION_EXPORT_DIR / f"{figure_name}.svg", bbox_inches="tight")


def _legacy_style():
    _publication_style()
    plt.rcParams.update({"axes.titlesize": 9, "axes.linewidth": 0.8})


def _legacy_axis(ax, right_spine=False):
    _style_axis(ax, show_right_spine=right_spine)


def plot_xrd_phase_evolution(save=True):
    """Plot sparse measured XRD samples with nominal Cu K-alpha phase references."""
    _legacy_style()
    data = pd.read_csv(RAW_DATA_DIR / "xrd_patterns.csv")
    temperatures = (700, 800, 900, 1000, 1100)
    colors = ("#0072B2", "#009E73", "#E69F00", "#D55E00", "#666666")
    angles = data["2Theta_deg"].to_numpy()
    segments = np.split(np.arange(len(data)), np.where(np.diff(angles) > 1.0)[0] + 1)
    offset_step = 6200

    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    for index, (temperature, color) in enumerate(zip(temperatures, colors)):
        intensity = data[f"Intensity_{temperature}C"]
        offset = index * offset_step
        for segment in segments:
            ax.plot(
                angles[segment],
                intensity.iloc[segment] + offset,
                color=color,
                linewidth=1.0,
                marker="o",
                markersize=1.8,
            )
        ax.text(80.7, offset + intensity.iloc[-1], f"{temperature} °C", color=color, va="center", fontsize=8)

    reference_reflections = (
        (29.9, "Wollastonite", "#009E73"),
        (31.0, "Whitlockite", "#E69F00"),
        (32.2, "Fluorapatite / HA", "#0072B2"),
    )
    for angle, label, color in reference_reflections:
        ax.axvline(angle, color=color, linewidth=0.8, linestyle=(0, (2, 2)), alpha=0.85)
        ax.text(
            angle,
            1.015,
            label,
            color=color,
            rotation=90,
            ha="center",
            va="bottom",
            transform=ax.get_xaxis_transform(),
            fontsize=7.5,
        )
    fig.text(
        0.5,
        0.015,
        "Nominal Cu Kα reference angles; measured scan contains 6 sampled positions",
        ha="center",
        fontsize=7,
        color="#555555",
    )
    ax.set_xlim(19.7, 85.5)
    ax.set_ylim(-300, offset_step * (len(temperatures) - 1) + 6500)
    ax.set_xlabel(r"2$\theta$ (°)")
    ax.set_ylabel("Intensity (a.u., offset)")
    ax.set_yticks([])
    _legacy_axis(ax)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    if save:
        _save_legacy_figure(fig, "xrd_phase_evolution", FIGURES_DIR / "characterization")
    return fig


def plot_initial_phase_map(save=True):
    """Plot mass-balanced initial phase fractions with bulk density."""
    _legacy_style()
    data = pd.read_csv(RAW_DATA_DIR / "sintering_phase_kinetics.csv")
    phases = (
        ("Amorphous_Percent", "Amorphous", "#8C8C8C"),
        ("Wollastonite_Percent", "Wollastonite", "#009E73"),
        ("Whitlockite_Percent", "Whitlockite", "#E69F00"),
        ("Hydroxyapatite_Percent", "Hydroxyapatite", "#56B4E9"),
    )
    positions = np.arange(len(data))
    fig, ax = plt.subplots(figsize=(7.0, 4.5))
    bottom = np.zeros(len(data))
    for column, label, color in phases:
        values = data[column].to_numpy()
        ax.bar(positions, values, bottom=bottom, width=0.68, color=color, label=label, linewidth=0)
        bottom += values

    density_ax = ax.twinx()
    density_ax.plot(
        positions,
        data["Bulk_Density_g_cm3"],
        "-D",
        color="#303840",
        linewidth=1.0,
        markersize=4.5,
        label="Bulk density",
        zorder=5,
    )
    ax.set_xticks(positions, data["Temperature_C"].astype(int))
    ax.set_xlabel("Sintering temperature (°C)")
    ax.set_ylabel("Phase fraction (wt%)")
    density_ax.set_ylabel("Bulk density (g cm⁻³)")
    density_ax.set_ylim(1.8, 3.0)
    _legacy_axis(ax)
    _legacy_axis(density_ax, right_spine=True)
    handles, labels = ax.get_legend_handles_labels()
    density_handles, density_labels = density_ax.get_legend_handles_labels()
    fig.legend(
        handles + density_handles,
        labels + density_labels,
        frameon=False,
        ncol=5,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.99),
    )
    fig.tight_layout(rect=(0, 0, 1, 0.91))
    if save:
        _save_legacy_figure(fig, "initial_phase_composition")
    return fig


def plot_sbf_hydroxyapatite_evolution(save=True):
    """Plot measured HA phase fractions with initial day-zero composition."""
    _legacy_style()
    sbf = load_sbf_phase_data()
    initial = load_initial_phase_data()
    colors = dict(zip((700, 800, 900, 1000, 1100), ("#D55E00", "#E69F00", "#56B4E9", "#009E73", "#0072B2")))
    fig, ax = plt.subplots(figsize=(7.0, 4.5))
    for temperature in sorted(sbf["temperature_C"].unique()):
        start = initial.loc[initial["temperature_C"] == temperature, "hydroxyapatite_pct"].iloc[0]
        subset = sbf[sbf["temperature_C"] == temperature].sort_values("soaking_day")
        days = np.r_[0, subset["soaking_day"].to_numpy()]
        values = np.r_[start, subset["hydroxyapatite_pct"].to_numpy()]
        ax.plot(days, values, marker="o", markersize=3.5, linewidth=1.2, color=colors[temperature], label=f"{temperature} °C")
    ax.set_xlim(-0.4, 21.6)
    ax.set_xticks([0, 1, 3, 5, 7, 14, 21])
    ax.set_xlabel("SBF immersion (days)")
    ax.set_ylabel("Hydroxyapatite phase fraction (wt%)")
    ax.legend(frameon=False, ncol=3, loc="upper center")
    fig.text(0.5, 0.015, "No day-1 measurement; segments connect measured observations only.", ha="center", fontsize=7, color="#555555")
    _legacy_axis(ax)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    if save:
        _save_legacy_figure(fig, "sbf_hydroxyapatite_evolution")
    return fig


def plot_sbf_wollastonite_evolution(save=True):
    """Plot measured wollastonite phase fractions, not inferred solution flux."""
    _legacy_style()
    sbf = load_sbf_phase_data()
    initial = load_initial_phase_data()
    colors = dict(zip((700, 800, 900, 1000, 1100), ("#D55E00", "#E69F00", "#56B4E9", "#009E73", "#0072B2")))
    fig, ax = plt.subplots(figsize=(7.0, 4.5))
    for temperature in sorted(sbf["temperature_C"].unique()):
        start = initial.loc[initial["temperature_C"] == temperature, "wollastonite_pct"].iloc[0]
        subset = sbf[sbf["temperature_C"] == temperature].sort_values("soaking_day")
        days = np.r_[0, subset["soaking_day"].to_numpy()]
        values = np.r_[start, subset["wollastonite_pct"].to_numpy()]
        ax.plot(days, values, marker="o", markersize=3.5, linewidth=1.2, color=colors[temperature], label=f"{temperature} °C")
    ax.set_xlim(-0.4, 21.6)
    ax.set_xticks([0, 1, 3, 5, 7, 14, 21])
    ax.set_xlabel("SBF immersion (days)")
    ax.set_ylabel("Wollastonite phase fraction (wt%)")
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, ncol=5, loc="upper center", bbox_to_anchor=(0.5, 0.99))
    fig.text(
        0.5,
        0.015,
        "Transport regime from mass-loss fits: 700 °C, n = 0.25 (quasi-Fickian); 1100 °C, n = 0.58 (anomalous).",
        ha="center",
        fontsize=7,
        color="#555555",
    )
    _legacy_axis(ax)
    fig.tight_layout(rect=(0, 0.06, 1, 0.91))
    if save:
        _save_legacy_figure(fig, "sbf_wollastonite_evolution")
    return fig


def plot_feature_importance(save=True):
    """Plot the stored random-forest feature importances in rank order."""
    _legacy_style()
    data = pd.read_csv(PROCESSED_DATA_DIR / "feature_importance.csv").sort_values("importance")
    labels = {
        "initial_hydroxyapatite_pct": "Initial hydroxyapatite",
        "initial_whitlockite_pct": "Initial whitlockite",
        "temperature_C": "Sintering temperature",
        "initial_wollastonite_pct": "Initial wollastonite",
        "initial_amorphous_pct": "Initial amorphous fraction",
        "initial_crystallinity_pct": "Initial crystallinity",
        "soaking_day": "SBF soaking time",
    }
    colors = plt.get_cmap("cividis")(np.linspace(0.18, 0.82, len(data)))
    fig, ax = plt.subplots(figsize=(6.8, 4.5))
    bars = ax.barh(
        [labels.get(feature, feature.replace("_", " ")) for feature in data["feature"]],
        data["importance"],
        color=colors,
        height=0.68,
    )
    for bar, value in zip(bars, data["importance"]):
        ax.text(value + 0.008, bar.get_y() + bar.get_height() / 2, f"{value:.1%}", va="center", fontsize=7.5)
    ax.set_xlim(0, data["importance"].max() * 1.22)
    ax.set_xlabel("Relative feature importance")
    ax.set_ylabel("")
    _legacy_axis(ax)
    fig.tight_layout()
    if save:
        _save_legacy_figure(fig, "feature_importance")
    return fig


def plot_predicted_vs_experimental_phase_fractions(save=True):
    """Plot random-holdout Random Forest predictions against observed phase fractions."""
    _legacy_style()
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error, r2_score
    from sklearn.model_selection import train_test_split

    from src.models import FEATURE_COLUMNS, TARGET_COLUMNS, load_ml_dataset

    data = load_ml_dataset()
    x_train, x_test, y_train, y_test = train_test_split(
        data[FEATURE_COLUMNS],
        data[TARGET_COLUMNS],
        test_size=0.2,
        random_state=42,
    )
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    score = r2_score(y_test, prediction)
    rmse = mean_squared_error(y_test, prediction) ** 0.5
    phase_specs = (
        ("sbf_wollastonite_pct", "Wollastonite", "#009E73"),
        ("sbf_hydroxyapatite_pct", "Hydroxyapatite", "#0072B2"),
        ("sbf_whitlockite_pct", "Whitlockite", "#E69F00"),
    )
    fig, ax = plt.subplots(figsize=(6.0, 5.2))
    values = []
    for column, label, color in phase_specs:
        index = TARGET_COLUMNS.index(column)
        experimental = y_test[column].to_numpy()
        predicted = prediction[:, index]
        values.extend(experimental.tolist())
        values.extend(predicted.tolist())
        ax.scatter(experimental, predicted, s=28, color=color, edgecolor="white", linewidth=0.45, label=label, alpha=0.9)
    lower = min(values) - 2
    upper = max(values) + 2
    ax.plot([lower, upper], [lower, upper], linestyle="--", color="#666666", linewidth=1.0, label="Identity")
    ax.set_xlim(lower, upper)
    ax.set_ylim(lower, upper)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("Experimental phase fraction (wt%)")
    ax.set_ylabel("Predicted phase fraction (wt%)")
    ax.legend(frameon=False, loc="lower right")
    ax.text(
        0.04,
        0.96,
        f"All-phase test R² = {score:.3f}\nRMSE = {rmse:.2f} wt%\nRandom 20% row holdout",
        transform=ax.transAxes,
        va="top",
        fontsize=7.5,
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "white", "edgecolor": "#BBBBBB", "alpha": 0.9},
    )
    _legacy_axis(ax)
    fig.tight_layout()
    if save:
        _save_legacy_figure(fig, "predicted_vs_experimental_phase_fractions")
    return fig


def plot_hydroxyapatite_gain_day21(save=True):
    """Compare measured initial and day-21 hydroxyapatite fractions by temperature."""
    _legacy_style()
    initial = load_initial_phase_data().set_index("temperature_C")
    sbf = load_sbf_phase_data()
    final = sbf[sbf["soaking_day"] == 21].set_index("temperature_C")
    temperatures = sorted(final.index.astype(int))
    positions = np.arange(len(temperatures))
    initial_values = np.array([initial.loc[temp, "hydroxyapatite_pct"] for temp in temperatures])
    final_values = np.array([final.loc[temp, "hydroxyapatite_pct"] for temp in temperatures])
    width = 0.34
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.bar(positions - width / 2, initial_values, width, color="#9AA7B0", label="Initial (day 0)")
    ax.bar(positions + width / 2, final_values, width, color="#0072B2", label="SBF (day 21)")
    for position, start, end in zip(positions, initial_values, final_values):
        delta = end - start
        ax.annotate(
            f"Δ {delta:+.2f}",
            xy=(position, max(start, end) + 1.2),
            ha="center",
            va="bottom",
            fontsize=7.5,
            color="#303840",
        )
    ax.set_xticks(positions, [str(temp) for temp in temperatures])
    ax.set_xlabel("Sintering temperature (°C)")
    ax.set_ylabel("Hydroxyapatite fraction (wt%)")
    ax.set_ylim(0, max(final_values.max(), initial_values.max()) + 9)
    ax.legend(frameon=False, ncol=2, loc="upper right")
    _legacy_axis(ax)
    fig.tight_layout()
    if save:
        _save_legacy_figure(fig, "hydroxyapatite_gain_day21")
    return fig


def plot_kinetic_blueprint_framework(save=True):
    """Summarize measured processing, phase, dissolution, pH, and viability data."""
    _legacy_style()
    phase = pd.read_csv(RAW_DATA_DIR / "sintering_phase_kinetics.csv")
    mass_loss = pd.read_csv(PROCESSED_DATA_DIR / "transport_kinetics.csv")
    kp = pd.read_csv(PROCESSED_DATA_DIR / "korsmeyer_peppas_parameters.csv").set_index("Temperature")
    ph = pd.read_csv(RAW_DATA_DIR / "sbf_ph_dynamics_21d.csv")
    viability = pd.read_csv(RAW_DATA_DIR / "cytotoxicity_iso10993.csv")
    temperature_colors = dict(zip((700, 800, 900, 1000, 1100), ("#D55E00", "#E69F00", "#56B4E9", "#009E73", "#0072B2")))
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 6.0))
    ax_phase, ax_dissolution, ax_ph, ax_bio = axes.flat

    positions = np.arange(len(phase))
    bottom = np.zeros(len(phase))
    phase_specs = (
        ("Amorphous_Percent", "Amorphous", "#8C8C8C"),
        ("Wollastonite_Percent", "Wollastonite", "#009E73"),
        ("Whitlockite_Percent", "Whitlockite", "#E69F00"),
        ("Hydroxyapatite_Percent", "Hydroxyapatite", "#56B4E9"),
    )
    for column, label, color in phase_specs:
        values = phase[column].to_numpy()
        ax_phase.bar(positions, values, bottom=bottom, width=0.68, color=color, label=label, linewidth=0)
        bottom += values
    density_ax = ax_phase.twinx()
    density_ax.plot(
        positions,
        phase["Bulk_Density_g_cm3"],
        "-D",
        color="#303840",
        linewidth=0.9,
        markersize=3,
        label="Bulk density",
    )
    ax_phase.set_xticks(positions, phase["Temperature_C"].astype(int), rotation=35)
    ax_phase.set_ylabel("Phase fraction (wt%)")
    ax_phase.set_xlabel("Temperature (°C)")
    density_ax.set_ylabel("Density (g cm⁻³)", fontsize=8)
    density_ax.set_ylim(1.8, 3.0)
    _legacy_axis(ax_phase)
    _legacy_axis(density_ax, right_spine=True)

    for temperature in (700, 1100):
        subset = mass_loss[mass_loss["Temperature"] == temperature]
        params = kp.loc[temperature]
        color = temperature_colors[temperature]
        ax_dissolution.scatter(
            subset["TimeDays"],
            subset["MassLossPercent"],
            color=color,
            s=17,
            zorder=3,
            label="Observed" if temperature == 700 else None,
        )
        days = np.linspace(0, 21, 120)
        fitted = 100 * params["k"] * days**params["n"]
        ax_dissolution.plot(
            days,
            fitted,
            color=color,
            linewidth=1.2,
            label=f"{temperature} °C KP fit, n={params['n']:.2f}",
        )
    ax_dissolution.set_xlabel("Immersion time (days)")
    ax_dissolution.set_ylabel("Mass loss (%)")
    ax_dissolution.legend(frameon=False, fontsize=7, loc="upper left")
    _legacy_axis(ax_dissolution)

    for temperature in (700, 1100):
        subset = ph[ph["Temperature_C"] == temperature].sort_values("Time_Days")
        ax_ph.plot(
            subset["Time_Days"],
            subset["pH_Value"],
            marker="o",
            markersize=2.8,
            linewidth=1.2,
            color=temperature_colors[temperature],
            label=f"{temperature} °C",
        )
    ax_ph.axhspan(7.35, 7.85, color="#009E73", alpha=0.12, zorder=0)
    ax_ph.axhline(8.2, color="#D55E00", linestyle="--", linewidth=0.8)
    ax_ph.set_xlabel("Immersion time (days)")
    ax_ph.set_ylabel("Interfacial pH")
    ax_ph.legend(frameon=False, fontsize=7, loc="upper right")
    _legacy_axis(ax_ph)

    for temperature in (700, 1100):
        subset = viability[viability["Sintering_Temp_C"] == temperature].groupby("Extract_Percent")["Cell_Viability_Percent"].mean()
        ax_bio.plot(
            subset.index,
            subset.values,
            marker="o",
            markersize=3,
            linewidth=1.2,
            color=temperature_colors[temperature],
            label=f"{temperature} °C",
        )
    ax_bio.axhline(70, color="#D55E00", linestyle="--", linewidth=0.8)
    ax_bio.set_xlabel("Extract concentration (%)")
    ax_bio.set_ylabel("Cell viability (%)")
    ax_bio.legend(frameon=False, fontsize=7, loc="upper left")
    _legacy_axis(ax_bio)

    titles = (
        "A  Processing → phase architecture",
        "B  Dissolution / transport",
        "C  Interfacial pH response",
        "D  Cell viability",
    )
    for ax, title in zip((ax_phase, ax_dissolution, ax_ph, ax_bio), titles):
        ax.set_title(title, loc="left", pad=4)
    phase_handles, phase_labels = ax_phase.get_legend_handles_labels()
    density_handles, density_labels = density_ax.get_legend_handles_labels()
    fig.legend(
        phase_handles + density_handles,
        phase_labels + density_labels,
        frameon=False,
        ncol=5,
        fontsize=7,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.0),
    )
    fig.text(
        0.5,
        0.015,
        "21-day Ca / Si release (mM): 700 °C = 4.02 / 1.34; 1100 °C = 1.02 / 0.34",
        ha="center",
        fontsize=7,
        color="#555555",
    )
    fig.tight_layout(rect=(0, 0.06, 1, 0.94), h_pad=1.8, w_pad=1.4)
    if save:
        _save_legacy_figure(fig, "kinetic_blueprint_framework")
    return fig


def generate_legacy_figures():
    """Regenerate the eight legacy target figures and mirror SVG exports."""
    plot_functions = (
        plot_xrd_phase_evolution,
        plot_initial_phase_map,
        plot_feature_importance,
        plot_predicted_vs_experimental_phase_fractions,
        plot_hydroxyapatite_gain_day21,
        plot_sbf_hydroxyapatite_evolution,
        plot_sbf_wollastonite_evolution,
        plot_kinetic_blueprint_framework,
    )
    for plot_function in plot_functions:
        fig = plot_function()
        plt.close(fig)


if __name__ == "__main__":
    plot_initial_phase_map()
    plot_sbf_hydroxyapatite_evolution()
    plot_sbf_wollastonite_evolution()
