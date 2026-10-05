"""
src/kinetic_blueprint.py
=============================================================================
KINETIC BLUEPRINT FRAMEWORK: COMPUTATIONAL ENGINE
=============================================================================
Implements forward simulation and analysis of:
  1. 1D Moving-Boundary Reaction-Diffusion PDE for strut dissolution
  2. Damköhler (Da) and Péclet (Pe) dimensionless regime mapping
  3. Korsmeyer-Peppas transport kinetics (n, k)
  4. Stoichiometric ion release balance (Ca/Si = 3.0)
  5. Regenerative Target Zone (RTZ) spatio-temporal tube validation
  6. Trajectory descriptors (tau, Sigma_28)

Author: Dr. Andualem Belachew Workie (KineticAI-AWGC)
License: MIT
=============================================================================
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# =============================================================================
# 1. MATERIAL & DOMAIN CONFIGURATION DATA CLASS
# =============================================================================
@dataclass
class CeramicParameters:
    """Solid-state chemical and structural parameters for AWGC systems."""
    name: str
    temp_c: float              # Sintering temperature (°C)
    alpha: float               # Reactive amorphous fraction (0 to 1)
    k_diss_0: float            # Intrinsic dissolution rate constant (mol / (m^2 * day))
    q_n_connectivity: float    # Average bridging oxygen connectivity Q^n (1.0 to 4.0)
    initial_porosity: float    # Initial strut/matrix porosity epsilon_0
    strut_radius_um: float     # Initial micro-strut radius (microns)
    bulk_density_g_cm3: float  # Consolidated bulk density (g/cm^3)
    c_sat_si_mM: float = 2.0   # Silica saturation limit in medium (mM)
    c_sat_ca_mM: float = 6.0   # Calcium saturation limit in medium (mM)


# =============================================================================
# 2. 1D MOVING-BOUNDARY REACTION-DIFFUSION SOLVER
# =============================================================================
class MovingBoundaryDissolutionSolver:
    """
    Solves coupled 1D mass conservation and moving-boundary dissolution:
      ∂C/∂t + u * ∂C/∂x = ∂/∂x (D_eff(ε) * ∂C/∂x) + S(x, t) - R(x, t)
      ∂ε/∂t = k_diss * α * β(t) * V_m * (1 - C / C_sat)
    """

    def __init__(
        self,
        material: CeramicParameters,
        domain_length_um: float = 250.0,
        nx: int = 100,
        t_max_days: float = 28.0,
        dt_days: float = 0.01,
        flow_velocity_um_s: float = 1.0,
        molecular_diffusivity_um2_s: float = 500.0,
    ):
        self.mat = material
        self.L = domain_length_um
        self.nx = nx
        self.dx = domain_length_um / (nx - 1)
        self.x = np.linspace(0, domain_length_um, nx)

        self.t_max = t_max_days
        self.dt = dt_days
        self.nt = int(t_max_days / dt_days)
        self.time = np.linspace(0, t_max_days, self.nt)

        # Convert flow and diffusion to um / day units
        seconds_per_day = 86400.0
        self.u = flow_velocity_um_s * seconds_per_day
        self.D0 = molecular_diffusivity_um2_s * seconds_per_day

    def run_simulation(self) -> Dict[str, np.ndarray]:
        """Executes forward explicit finite-difference integration."""
        # State arrays
        c_si = np.zeros(self.nx)  # Aqueous Si (mM)
        c_ca = np.zeros(self.nx)  # Aqueous Ca (mM)
        porosity = np.full(self.nx, self.mat.initial_porosity)
        strut_r = np.full(self.nx, self.mat.strut_radius_um)

        # Time-series history collectors (sampled at the scaffold effluent / exit x=L)
        si_history = np.zeros(self.nt)
        ca_history = np.zeros(self.nt)
        ph_history = np.zeros(self.nt)
        mass_loss_history = np.zeros(self.nt)

        molar_vol_glass = 2.4e-5  # m^3 / mol
        stoich_ca_si = 3.00       # Congruent matrix ratio

        for it in range(self.nt):
            # 1. Update geometric specific surface area beta(t) = 3(1 - eps) / r
            r_clamped = np.maximum(strut_r, 0.1)
            beta = 3.0 * (1.0 - porosity) / (r_clamped * 1e-6)  # m^2 / m^3

            # 2. Driving force: chemical undersaturation
            undersat_si = np.clip(1.0 - (c_si / self.mat.c_sat_si_mM), 0.0, 1.0)

            # 3. Source terms: Congruent dissolution
            s_si = self.mat.k_diss_0 * self.mat.alpha * beta * undersat_si * 1e-3  # mM/day
            s_ca = stoich_ca_si * s_si

            # 4. Sink term: Hydroxycarbonate apatite (HCA) nucleation sink for Ca
            # Ca precipitates when supersaturation threshold is crossed
            hca_supersat = np.maximum(c_ca - 2.5, 0.0)
            k_precip = 0.15  # 1/day
            r_ca = k_precip * (hca_supersat ** 1.5)

            # 5. Effective diffusivity closure: D_eff = D0 * eps^1.5 (Archie's Law)
            d_eff = self.D0 * (porosity ** 1.5)

            # 6. Spatial derivative discretization (Central differences for diffusion, Upwind for advection)
            d2c_dx2_si = np.zeros(self.nx)
            dc_dx_si = np.zeros(self.nx)
            d2c_dx2_si[1:-1] = (c_si[2:] - 2.0 * c_si[1:-1] + c_si[:-2]) / (self.dx ** 2)
            dc_dx_si[1:-1] = (c_si[1:-1] - c_si[:-2]) / self.dx  # Upwind advection

            d2c_dx2_ca = np.zeros(self.nx)
            dc_dx_ca = np.zeros(self.nx)
            d2c_dx2_ca[1:-1] = (c_ca[2:] - 2.0 * c_ca[1:-1] + c_ca[:-2]) / (self.dx ** 2)
            dc_dx_ca[1:-1] = (c_ca[1:-1] - c_ca[:-2]) / self.dx

            # 7. Time stepping: Concentration PDE
            c_si[1:-1] += self.dt * (d_eff[1:-1] * d2c_dx2_si[1:-1] - self.u * dc_dx_si[1:-1] + s_si[1:-1])
            c_ca[1:-1] += self.dt * (d_eff[1:-1] * d2c_dx2_ca[1:-1] - self.u * dc_dx_ca[1:-1] + s_ca[1:-1] - r_ca[1:-1])

            # Boundary Conditions:
            # x=0 (strut wall): zero-flux ∂C/∂x = 0
            c_si[0] = c_si[1]
            c_ca[0] = c_ca[1]
            # x=L (open pore exit): convective outflow ∂C/∂x = 0
            c_si[-1] = c_si[-2]
            c_ca[-1] = c_ca[-2]

            # 8. Moving Boundary & Porosity evolution
            # d(eps)/dt = k_diss * alpha * beta * V_m * undersat
            deps_dt = self.mat.k_diss_0 * self.mat.alpha * beta * molar_vol_glass * undersat_si
            porosity = np.clip(porosity + deps_dt * self.dt, 0.0, 0.95)
            # Strut erosion: dr/dt = -k_diss * V_m * undersat
            strut_r -= (self.mat.k_diss_0 * molar_vol_glass * undersat_si * 1e6) * self.dt

            # 9. Compute bulk/effluent readouts at pore exit
            effluent_si = float(c_si[-1])
            effluent_ca = float(c_ca[-1])
            si_history[it] = effluent_si
            ca_history[it] = effluent_ca

            # Interfacial pH coupling: baseline 7.40 + proton consumption from cation exchange
            # Normalized alkaline shift proportional to total dissolved Si and Ca
            ph_history[it] = 7.40 + 0.35 * (effluent_ca / 2.0) * (self.mat.alpha / 0.5)

            # Cumulative mass loss (%)
            mass_loss_history[it] = float(np.mean(porosity - self.mat.initial_porosity) / (1.0 - self.mat.initial_porosity) * 100.0)

        return {
            "time_days": self.time,
            "c_si_effluent": si_history,
            "c_ca_effluent": ca_history,
            "ph_effluent": ph_history,
            "cumulative_mass_loss": mass_loss_history,
            "final_porosity_profile": porosity,
        }


# =============================================================================
# 3. DIMENSIONLESS REGIME & KINETIC ANALYSIS
# =============================================================================
class KineticBlueprintAnalyzer:
    """Calculates Da, Pe, Korsmeyer-Peppas exponent n, and trajectory descriptors."""

    @staticmethod
    def compute_dimensionless_numbers(
        mat: CeramicParameters,
        characteristic_length_um: float = 200.0,
        flow_velocity_um_s: float = 1.0,
        d0_um2_s: float = 500.0,
    ) -> Tuple[float, float, str]:
        """
        Computes Damköhler (Da) and Péclet (Pe) numbers:
          Da = (k_diss * alpha * beta_0 * L^2) / (D_eff * C0)
          Pe = (U * L) / D_eff
        """
        seconds_per_day = 86400.0
        l_m = characteristic_length_um * 1e-6
        u_m_s = flow_velocity_um_s * 1e-6
        d_eff_m2_s = (d0_um2_s * 1e-12) * (mat.initial_porosity ** 1.5)

        # Volumetric dissolution rate
        beta_0 = 3.0 * (1.0 - mat.initial_porosity) / (mat.strut_radius_um * 1e-6)
        r_diss = mat.k_diss_0 * mat.alpha * beta_0 / seconds_per_day  # mol / (m^3 * s)
        c0 = mat.c_sat_si_mM * 1e-3 * 1e3  # mol / m^3

        da = (r_diss * (l_m ** 2)) / (d_eff_m2_s * c0)
        pe = (u_m_s * l_m) / d_eff_m2_s

        # Classification of transport regimes
        if da > 2.0:
            regime = "Region I: Reactive Burst Regime (Da >> 1)"
        elif 0.5 <= da <= 2.0:
            regime = "Region II: Balanced Transport Regime (Da ~ 1)"
        else:
            regime = "Region III: Transport-Limited Regime (Da < 1)"

        return float(da), float(pe), regime

    @staticmethod
    def fit_korsmeyer_peppas(time_days: np.ndarray, mass_loss_pct: np.ndarray) -> Tuple[float, float, float]:
        """
        Fits Korsmeyer-Peppas model: M_t / M_inf = k * t^n
        Returns: (rate_constant k, kinetic_exponent n, R_squared)
        """
        # Fit on early-to-intermediate release window (first 60% of total mass loss)
        cutoff = np.argmax(mass_loss_pct >= 0.60 * mass_loss_pct[-1])
        cutoff = max(cutoff, 5)
        t_fit = time_days[1:cutoff]
        m_fit = mass_loss_pct[1:cutoff] / max(mass_loss_pct[-1], 1e-5)

        def power_law(t, k, n):
            return k * (t ** n)

        popt, _ = curve_fit(power_law, t_fit, m_fit, p0=[0.1, 0.45], bounds=([1e-4, 0.05], [5.0, 1.2]))
        k_fit, n_fit = popt

        # R^2 calculation
        residuals = m_fit - power_law(t_fit, *popt)
        ss_res = np.sum(residuals ** 2)
        ss_tot = np.sum((m_fit - np.mean(m_fit)) ** 2)
        r2 = 1.0 - (ss_res / max(ss_tot, 1e-8))

        return float(k_fit), float(n_fit), float(r2)

    @staticmethod
    def compute_trajectory_descriptors(time_days: np.ndarray, c_profile: np.ndarray) -> Tuple[float, float]:
        """
        Calculates:
          Sigma_28: Cumulative 28-day exposure dose = Integral(C(t) dt)
          tau: Half-dose arrival time (days) where cumulative dose reaches 50%
        """
        dt = np.gradient(time_days)
        cumulative_dose = np.cumsum(c_profile * dt)
        sigma_28 = float(cumulative_dose[-1])

        half_idx = np.searchsorted(cumulative_dose, 0.50 * sigma_28)
        tau = float(time_days[min(half_idx, len(time_days) - 1)])

        return tau, sigma_28


# =============================================================================
# 4. REGENERATIVE TARGET ZONE (RTZ) VALIDATOR
# =============================================================================
class RegenerativeTargetZone:
    """Validates whether temporal trajectories stay within therapeutic, sub-cytotoxic bounds."""

    def __init__(
        self,
        si_range_mM: Tuple[float, float] = (0.2, 1.5),
        ca_range_mM: Tuple[float, float] = (1.0, 5.0),
        ph_range: Tuple[float, float] = (7.35, 7.85),
    ):
        self.si_min, self.si_max = si_range_mM
        self.ca_min, self.ca_max = ca_range_mM
        self.ph_min, self.ph_max = ph_range

    def check_admissibility(
        self,
        time_days: np.ndarray,
        c_si: np.ndarray,
        c_ca: np.ndarray,
        ph_traj: np.ndarray,
    ) -> Dict[str, any]:
        """Returns boolean compliance and violation percentage across time."""
        valid_si = (c_si >= self.si_min) & (c_si <= self.si_max)
        valid_ca = (c_ca >= self.ca_min) & (c_ca <= self.ca_max)
        valid_ph = (ph_traj >= self.ph_min) & (ph_traj <= self.ph_max)

        overall_valid = valid_si & valid_ca & valid_ph
        compliance_pct = float(np.mean(overall_valid) * 100.0)

        return {
            "is_admissible": compliance_pct >= 85.0,  # Pre-registered tolerance
            "compliance_pct": compliance_pct,
            "ph_violations": int(np.sum(~valid_ph)),
            "si_violations": int(np.sum(~valid_si)),
        }


# =============================================================================
# 5. PUBLICATION-GRADE FIGURE GENERATOR
# =============================================================================
def generate_framework_figure(results: Dict[str, Dict], export_dir: Path):
    """Exports 4-panel publication-grade vector SVG and 600 DPI PNG figures."""
    export_dir.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "DejaVu Sans"],
        "font.size": 8,
        "axes.labelsize": 9,
        "axes.titlesize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 7.5,
        "lines.linewidth": 1.2,
        "figure.dpi": 300,
    })

    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.8), dpi=300)
    colors = {"700C": "#D9534F", "900C": "#F0AD4E", "1100C": "#1F77B4"}

    # --- Panel A: Mass Loss & Korsmeyer-Peppas Fit ---
    ax = axes[0, 0]
    for key, data in results.items():
        t = data["sim"]["time_days"]
        m = data["sim"]["cumulative_mass_loss"]
        n_val = data["metrics"]["n"]
        k_val = data["metrics"]["k"]
        ax.plot(t, m, label=f"{key} (n={n_val:.2f})", color=colors[key])
    ax.set_xlabel("Immersion Duration (Days)")
    ax.set_ylabel("Cumulative Mass Loss (wt%)")
    ax.set_title("(a) Dissolution Kinetics & Regime Exponent n", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False)

    # --- Panel B: Interfacial pH Dynamics & Safety Window ---
    ax = axes[0, 1]
    ax.axhspan(7.35, 7.85, color="#D4EDDA", alpha=0.6, label="RTZ Homeostatic Buffer (7.35-7.85)")
    ax.axhspan(8.20, 8.80, color="#F8D7DA", alpha=0.4, label="Alkaline Shock / Cytotoxic (>8.20)")
    for key, data in results.items():
        t = data["sim"]["time_days"]
        ph = data["sim"]["ph_effluent"]
        ax.plot(t, ph, label=f"{key}", color=colors[key])
    ax.set_xlabel("Immersion Duration (Days)")
    ax.set_ylabel("Interfacial Microenvironmental pH")
    ax.set_title("(b) Microenvironmental pH Trajectories", fontweight="bold")
    ax.set_ylim(7.2, 8.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, loc="upper right")

    # --- Panel C: Silicon vs Calcium Release Balance ---
    ax = axes[1, 0]
    for key, data in results.items():
        si = data["sim"]["c_si_effluent"]
        ca = data["sim"]["c_ca_effluent"]
        ax.scatter(si, ca, s=12, label=f"{key} Trajectory", color=colors[key], alpha=0.7)
    # 3:1 theoretical matrix stoichiometry line
    si_grid = np.linspace(0.1, 1.6, 50)
    ax.plot(si_grid, 3.0 * si_grid, "k--", label="Congruent Ratio 3:1 (Ca/Si)")
    ax.set_xlabel("Aqueous Silicon Concentration [Si⁴⁺] (mM)")
    ax.set_ylabel("Aqueous Calcium Concentration [Ca²⁺] (mM)")
    ax.set_title("(c) Multi-Ion Stoichiometric Dissolution", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False)

    # --- Panel D: Trajectory Descriptors (tau vs Sigma_28) ---
    ax = axes[1, 1]
    for key, data in results.items():
        tau = data["metrics"]["tau_si"]
        sigma = data["metrics"]["sigma_si"]
        da = data["metrics"]["da"]
        ax.scatter(tau, sigma, s=120, color=colors[key], edgecolor="black", linewidth=0.8, zorder=3)
        ax.text(tau + 0.3, sigma, f"{key}\n(Da={da:.2f})", fontsize=7.5, verticalalignment="center")
    ax.set_xlabel("Characteristic Release Time τ (Days)")
    ax.set_ylabel("28-Day Cumulative Dose Σ₂₈ (mM·day)")
    ax.set_title("(d) (τ, Σ) Trajectory Space Mapping", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)

    plt.tight_layout()
    fig.savefig(export_dir / "kinetic_blueprint_simulation.svg")
    fig.savefig(export_dir / "kinetic_blueprint_simulation.png", dpi=600)
    plt.close()
    print(f" [✓] Figures successfully saved to {export_dir.resolve()}")


# =============================================================================
# 6. PIPELINE DEMONSTRATION & EXECUTION ENTRY POINT
# =============================================================================
def main():
    print("=" * 75)
    print(" EXECUTING KINETIC BLUEPRINT SIMULATION (700 °C, 900 °C, 1100 °C)")
    print("=" * 75)

    # Instantiate parameters representing Regions I, II, and III
    materials = [
        CeramicParameters(
            name="700C", temp_c=700.0, alpha=0.522, k_diss_0=0.0471,
            q_n_connectivity=1.85, initial_porosity=0.35, strut_radius_um=150.0,
            bulk_density_g_cm3=2.02
        ),
        CeramicParameters(
            name="900C", temp_c=900.0, alpha=0.360, k_diss_0=0.0185,
            q_n_connectivity=2.40, initial_porosity=0.28, strut_radius_um=150.0,
            bulk_density_g_cm3=2.61
        ),
        CeramicParameters(
            name="1100C", temp_c=1100.0, alpha=0.226, k_diss_0=0.00455,
            q_n_connectivity=3.20, initial_porosity=0.18, strut_radius_um=150.0,
            bulk_density_g_cm3=2.78
        ),
    ]

    rtz = RegenerativeTargetZone()
    results = {}

    for mat in materials:
        print(f"\n--- Simulating {mat.name} ({mat.temp_c:.0f} °C) ---")
        solver = MovingBoundaryDissolutionSolver(material=mat, t_max_days=28.0)
        sim_data = solver.run_simulation()

        # Dimensionless numbers
        da, pe, regime = KineticBlueprintAnalyzer.compute_dimensionless_numbers(mat)

        # Korsmeyer-Peppas exponent
        k_kp, n_kp, r2 = KineticBlueprintAnalyzer.fit_korsmeyer_peppas(
            sim_data["time_days"], sim_data["cumulative_mass_loss"]
        )

        # Trajectory coordinates (tau, sigma_28) for Silicon tracer
        tau, sigma_28 = KineticBlueprintAnalyzer.compute_trajectory_descriptors(
            sim_data["time_days"], sim_data["c_si_effluent"]
        )

        # RTZ compliance
        admissibility = rtz.check_admissibility(
            sim_data["time_days"],
            sim_data["c_si_effluent"],
            sim_data["c_ca_effluent"],
            sim_data["ph_effluent"],
        )

        results[mat.name] = {
            "sim": sim_data,
            "metrics": {
                "da": da, "pe": pe, "regime": regime,
                "k": k_kp, "n": n_kp, "r2": r2,
                "tau_si": tau, "sigma_si": sigma_28,
                "admissible": admissibility["is_admissible"],
                "compliance_pct": admissibility["compliance_pct"]
            }
        }

        print(f"  Regime              : {regime}")
        print(f"  Coordinates (Da, Pe): Da = {da:.3f}, Pe = {pe:.3f}")
        print(f"  Transport Kinetics  : n = {n_kp:.3f} (R² = {r2:.3f}), k = {k_kp:.4f}")
        print(f"  Trajectory (τ, Σ₂₈) : τ = {tau:.1f} days, Σ₂₈ = {sigma_28:.2f} mM·day")
        print(f"  Target Zone Check   : {'PASS' if admissibility['is_admissible'] else 'FAIL'} ({admissibility['compliance_pct']:.1f}% in-zone)")

    # Generate and export publication figures
    export_path = Path("figures/exports")
    generate_framework_figure(results, export_path)
    print("\n" + "=" * 75)
    print(" SIMULATION COMPLETE & AUDITED AGAINST KINETIC BLUEPRINT SPECIFICATIONS")
    print("=" * 75)


if __name__ == "__main__":
    main()
