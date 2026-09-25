#!/usr/bin/env python3
"""Generate publication-style vector figures for the spatiotemporal trajectory engineering manuscript.

This script exports matching SVG and PNG files into both `docs/figures/` and `figures/exports/`.
It is intentionally Python-native so it does not depend on a LaTeX toolchain.
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DOC_FIG_DIR = ROOT / "docs" / "figures"
EXPORT_DIR = ROOT / "figures" / "exports"

for d in (DOC_FIG_DIR, EXPORT_DIR):
    d.mkdir(parents=True, exist_ok=True)


def save_figure(fig, stem: str) -> None:
    for d in (DOC_FIG_DIR, EXPORT_DIR):
        fig.savefig(d / f"{stem}.svg", format="svg", bbox_inches="tight", dpi=300)
        fig.savefig(d / f"{stem}.png", format="png", bbox_inches="tight", dpi=300)


def fig1_chemical_trajectory() -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 5.5))
    t = np.linspace(0, 1, 500)
    band_bottom = 0.8
    band_top = 1.9
    ax.fill_between([0, 1], [band_bottom, band_bottom], [band_top, band_top], color="#dfeaf7", alpha=0.9, zorder=0)
    ax.axvspan(0.0, 1 / 3, color="#f7f7f7", alpha=0.25, zorder=0)
    ax.axvspan(1 / 3, 2 / 3, color="#f1f6f4", alpha=0.35, zorder=0)
    ax.axvspan(2 / 3, 1.0, color="#f4f0fb", alpha=0.35, zorder=0)

    ax.plot([0.0, 1.0], [band_bottom, band_bottom], color="#1d4e89", linestyle="--", linewidth=1.5)
    ax.plot([0.0, 1.0], [band_top, band_top], color="#1d4e89", linestyle="--", linewidth=1.5)

    x_stage = np.array([0.15, 0.5, 0.82])
    labels = ["Stage I\nion exchange", "Stage II\ngel-layer barrier", "Stage III\nHCA + passivation"]
    for xi, label in zip(x_stage, labels):
        ax.text(xi, 2.45, label, ha="center", va="center", fontsize=10, weight="bold", color="#3a3a3a")

    ax.plot(t, 1.2 * np.exp(-((t - 0.12) / 0.18) ** 2) + 0.3, color="#6b4fa8", linewidth=2.5)
    ax.plot(t, 0.75 + 1.15 * (1 / (1 + np.exp(-20 * (t - 0.45)))) * (1 - 0.2 * t), color="#1d7a6d", linewidth=2.5)
    ax.plot(t, 0.35 + 0.22 * np.ones_like(t), color="#1f5aa8", linewidth=2.5)

    ax.text(0.03, 0.85, "high NBO/BO", color="#6b4fa8", fontsize=10, ha="left", va="center")
    ax.text(0.52, 1.35, "sustained release", color="#1d7a6d", fontsize=10, ha="center", va="center")
    ax.text(0.13, 0.55, "low NBO/BO", color="#1f5aa8", fontsize=10, ha="left", va="center")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 3.1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("Time $t$", fontsize=11)
    ax.set_ylabel("Ion release flux", fontsize=11)
    ax.text(0.97, 2.15, "RTZ tube", fontsize=10, color="#1d4e89", ha="right", va="center")
    ax.set_frame_on(False)
    fig.tight_layout()
    return fig


def fig2_moving_boundary_erosion() -> plt.Figure:
    fig = plt.figure(figsize=(12, 5.5))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1.35])

    ax_left = fig.add_subplot(gs[0, 0])
    ax_right = fig.add_subplot(gs[0, 1])

    center = (0, 0)
    outer_initial = plt.Circle(center, 1.8, facecolor="none", edgecolor="gray", linestyle="--", linewidth=1.5)
    ax_left.add_patch(outer_initial)
    ax_left.text(0, 1.9, "initial boundary ($t=0$)", ha="center", va="bottom", fontsize=9, color="gray")

    gel = plt.Circle(center, 1.38, facecolor="#dfeaf7", edgecolor="#1d7a6d", linewidth=2)
    core = plt.Circle(center, 0.82, facecolor="#efefef", edgecolor="#3b3b3b", linewidth=2)
    ax_left.add_patch(gel)
    ax_left.add_patch(core)
    ax_left.text(0.9, 1.1, "gel layer", color="#1d7a6d", fontsize=10)
    ax_left.text(0, 0.15, "unreacted\ncore", ha="center", va="center", fontsize=10, color="#3b3b3b")

    ax_left.annotate("", xy=(1.38, 0), xytext=(0.82, 0), arrowprops=dict(arrowstyle="<->", color="#1d7a6d", lw=2))
    ax_left.text(1.1, -0.25, r"$\delta_g(t)$", color="#1d7a6d", fontsize=11)

    ax_left.annotate("", xy=(0.6, 0.5), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="#1d7a6d", lw=2))
    ax_left.text(0.45, 0.52, r"$r_s(t)$", fontsize=11, color="#1d7a6d")

    ax_left.annotate("", xy=(1.8, 0), xytext=(1.55, 0), arrowprops=dict(arrowstyle="->", color="#a91d33", lw=2.5))
    ax_left.text(2.0, 0.1, "receding", color="#a91d33", fontsize=10)
    ax_left.text(1.7, 1.2, "pore solution", fontsize=9, color="gray")

    ax_left.set_aspect("equal")
    ax_left.set_xlim(-2.4, 2.6)
    ax_left.set_ylim(-2.2, 2.3)
    ax_left.set_xticks([])
    ax_left.set_yticks([])
    ax_left.axis("off")

    t = np.linspace(0, 1, 400)
    eps = 0.18 + 0.75 * t**1.8
    kappa = 2.0 - 1.15 * t**1.2
    v_eff = 0.12 + 0.9 * t**1.5
    ax_right.plot(t, eps, color="#6b4fa8", linewidth=2.5, label=r"$\varepsilon(t)$")
    ax_right.plot(t, v_eff, color="#a91d33", linewidth=2.2, label=r"$D_{\mathrm{eff}}(t)$")
    ax_right.plot(t, kappa, color="#1d7a6d", linestyle="--", linewidth=2.0, label=r"$\bar{\kappa}(t)$")

    ax_right.axvline(0.88, color="gray", linestyle="--", linewidth=1.2)
    ax_right.text(0.9, 0.6, "collapse", fontsize=9, color="gray")

    ax_right.set_xlim(0, 1)
    ax_right.set_ylim(0, 2.6)
    ax_right.set_xlabel("Time, $t$", fontsize=11)
    ax_right.set_ylabel(r"$\varepsilon(t), D_{\mathrm{eff}}(t)$", fontsize=11)
    ax_right.legend(loc="upper right", frameon=False, fontsize=10)
    ax_right.set_frame_on(False)
    fig.tight_layout()
    return fig


def fig3_regime_map() -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-1.0, 1.0)
    ax.set_xticks([-1.0, 0.0, 1.0])
    ax.set_yticks([-1.0, 0.0, 1.0])
    ax.set_xticklabels([r"$\ll 1$", r"$\sim 1$", r"$\gg 1$"])
    ax.set_yticklabels([r"$\ll 1$", r"$\sim 1$", r"$\gg 1$"])
    ax.set_xlabel(r"$\log_{10}(\mathrm{Pe})$ (convection / diffusion)", fontsize=11)
    ax.set_ylabel(r"$\log_{10}(\mathrm{Da})$ (reaction / diffusion)", fontsize=11)
    ax.set_aspect("equal")

    ax.add_patch(plt.Rectangle((-1.0, -1.0), 1.0, 1.0, facecolor="#dfeaf7", edgecolor="none", alpha=0.7))
    ax.add_patch(plt.Rectangle((-1.0, 0.0), 1.0, 1.0, facecolor="#f3eaf9", edgecolor="none", alpha=0.7))
    ax.add_patch(plt.Rectangle((0.0, -1.0), 1.0, 1.0, facecolor="#eaf7ee", edgecolor="none", alpha=0.7))
    ax.add_patch(plt.Rectangle((0.0, 0.0), 1.0, 1.0, facecolor="#fef5df", edgecolor="none", alpha=0.7))
    ax.add_patch(plt.Rectangle((-0.15, -0.15), 0.3, 0.3, facecolor="none", edgecolor="#a91d33", linestyle="--", linewidth=2))

    ax.axvline(0.0, color="gray", linestyle="--", linewidth=1)
    ax.axhline(0.0, color="gray", linestyle="--", linewidth=1)

    ax.text(-0.55, -0.5, "Q1\nreaction-limited", ha="center", va="center", fontsize=10, weight="bold")
    ax.text(-0.55, 0.55, "Q2\ndiffusion-limited", ha="center", va="center", fontsize=10, weight="bold")
    ax.text(0.55, -0.5, "Q3\nconvective washout", ha="center", va="center", fontsize=10, weight="bold")
    ax.text(0.55, 0.55, "Q4\nconvection-amplified", ha="center", va="center", fontsize=10, weight="bold")
    ax.text(0.0, 0.0, "Design\nCorridor", ha="center", va="center", fontsize=10, color="#a91d33", weight="bold")

    ax.scatter([-0.7, -0.8, 0.7, 0.0], [-0.6, 0.7, -0.7, 0.0], c=["#1f5aa8", "#6b4fa8", "#1d7a6d", "#a91d33"], s=40, zorder=5)
    ax.text(-0.7, -0.55, "slow plateau", fontsize=8)
    ax.text(-0.8, 0.72, "burst / passivation", fontsize=8)
    ax.text(0.72, -0.7, "washout regime", fontsize=8)
    ax.text(0.02, -0.08, "Target Locus", fontsize=8, color="#a91d33")

    ax.set_frame_on(False)
    fig.tight_layout()
    return fig


def fig4_rtz_tube() -> plt.Figure:
    fig, ax = plt.subplots(figsize=(10, 5.8))
    phase_x = [0.0, 1.7, 4.4, 8.9]
    ax.axvspan(0, 1.7, color="#fbe5e7", alpha=0.8)
    ax.axvspan(1.7, 4.4, color="#e8f7ef", alpha=0.8)
    ax.axvspan(4.4, 8.9, color="#e8f0fb", alpha=0.8)
    ax.axvline(1.7, color="gray", linestyle="--", linewidth=1.2)
    ax.axvline(4.4, color="gray", linestyle="--", linewidth=1.2)

    ax.text(0.85, 5.2, "Phase I\n0--48 h", ha="center", va="center", fontsize=10, weight="bold")
    ax.text(3.05, 5.2, "Phase II\nD3--D7", ha="center", va="center", fontsize=10, weight="bold")
    ax.text(6.65, 5.2, "Phase III\n$>$D14", ha="center", va="center", fontsize=10, weight="bold")

    x = np.linspace(0, 8.9, 500)
    lower = 0.9 + 0.1 * np.sin(x / 2.2) + 0.2 * np.exp(-0.6 * x)
    upper = 2.9 + 0.55 * np.sin(x / 1.9 + 0.7) + 0.4 * np.exp(-0.4 * x)
    ax.plot(x, lower, color="#a91d33", linestyle="--", linewidth=2, label=r"$C_i^{\min}(t)$")
    ax.plot(x, upper, color="#a91d33", linestyle="--", linewidth=2, label=r"$C_i^{\max}(t)$")

    admissible = 1.5 + 0.8 * np.exp(-0.3 * x) + 0.25 * np.sin(x / 1.6)
    overshoot = 1.0 + 2.3 * (1 / (1 + np.exp(-8 * (x - 2.0))))
    undershoot = 0.5 + 0.15 * x / 8.9

    ax.plot(x, admissible, color="#1d7a6d", linewidth=2.8)
    ax.plot(x, overshoot, color="#6b4fa8", linewidth=2.8)
    ax.plot(x, undershoot, color="#1f5aa8", linewidth=2.8)

    ax.text(5.0, 3.2, "admissible", color="#1d7a6d", fontsize=10, weight="bold")
    ax.text(2.2, 3.8, "overshoot", color="#6b4fa8", fontsize=10, weight="bold")
    ax.text(6.2, 0.5, "undershoot", color="#1f5aa8", fontsize=10, weight="bold")

    ax.set_xlim(0, 9.2)
    ax.set_ylim(0, 5.8)
    ax.set_xlabel("Time (days)", fontsize=11)
    ax.set_ylabel("Ion concentration / flux", fontsize=11)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    fig.tight_layout()
    return fig


def main() -> None:
    fig1 = fig1_chemical_trajectory()
    save_figure(fig1, "fig1_chemical_trajectory")
    plt.close(fig1)

    fig2 = fig2_moving_boundary_erosion()
    save_figure(fig2, "fig2_moving_boundary_erosion")
    plt.close(fig2)

    fig3 = fig3_regime_map()
    save_figure(fig3, "fig3_regime_map")
    plt.close(fig3)

    fig4 = fig4_rtz_tube()
    save_figure(fig4, "fig4_rtz_tube")
    plt.close(fig4)

    print("Generated figures:")
    for d in (DOC_FIG_DIR, EXPORT_DIR):
        print(f" - {d}")
        for name in [
            "fig1_chemical_trajectory",
            "fig2_moving_boundary_erosion",
            "fig3_regime_map",
            "fig4_rtz_tube",
        ]:
            print(f"   * {name}.svg, {name}.png")


if __name__ == "__main__":
    main()
