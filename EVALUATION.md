# Evaluation — KineticAI-AWGC

**Repo:** `andualembelachew2/KineticAI-AWGC` · **Branch reviewed:** `main` @ `dd4af49` (single commit) · **Date:** 2026-08-04
**Method:** full static review of data/docs/code, execution of all 10 notebooks and all `src/` scripts in a fresh venv, cross-checks of committed results against reproducible runs, DOI verification.

---

## 1. What it is

An open computational-materials repository that packages experimental data, notebooks, and Python modules around the "Kinetic Blueprint Framework" for **spray-pyrolyzed apatite–wollastonite glass-ceramics (AWGC)** — a bioactive bone-graft material. The narrative chain is: thermal processing (700–1100 °C) → phase architecture → transport behavior (Korsmeyer–Peppas kinetics) → pH microenvironment → cell viability → "deterministic materials design."

The author is the first author of the underlying peer-reviewed study, which is real and verifiable:

- **Crystals 13(7):1049 (2023)** — *An Investigation of In Vitro Bioactivities and Cytotoxicities of Spray Pyrolyzed Apatite–Wollastonite Glass-Ceramics* — DOI resolves to the MDPI article. ✔
- Zenodo badge is genuine: `10.5281/zenodo.21759552` → archived release **v1.0.1 (2026-08-02)** with the MIT license. ✔
- 4 further 2025–2026 publications (Ceramics Int., RSC Adv., Biomater. Sci.) are listed; these are recent and I did not independently verify each DOI.

---

## 2. Strengths

| Area | Observation |
|---|---|
| Scientific grounding | Real author, real underlying paper; the framework narrative (processing → structure → transport → bioresponse) is coherent and well-motivated. |
| Structure & documentation | Clean `data/ docs/ notebooks/ results/ src/ figures/` layout; README at every level; reading-order guide; publication list; MIT license. |
| Runnable core | `src/data_processing.py` and `src/models.py` run end-to-end in a fresh environment; the ML dataset merge is deterministic (regeneration is byte-identical to the committed file). |
| Self-consistent pipeline | Notebooks 01, 02, 03, 06, 07, 09, 10 execute cleanly; K–P fits reproduce from `transport_kinetics.csv` (n ≈ 0.256 / 0.581); RF phase prediction is reproducible (R² ≈ 0.93). |
| Asset hygiene | 300-dpi figures committed; results summaries for each workflow; `.gitignore` sensible. |

---

## 3. Critical findings

### 3.1 Reproducibility — 3 of 10 notebooks fail on a fresh run ❌
Executed all notebooks top-to-bottom with the repo's own `requirements.txt`:

| Notebook | Failure | Root cause |
|---|---|---|
| `04_bioactivity_interpretation` | `NameError: kb_df` | Uses `kb_df` (master dataset) but never loads it — only `initial_df`/`sbf_df` are read. |
| `05_microenvironment_evolution` | `KeyError: 'NBO_BO_Ratio'` | Loads `awgc_ml_dataset.csv` into `kb_df`, then accesses columns (`NBO_BO_Ratio`, `Final_pH_21d`, `MassLoss_21d_Percent`, `Ca_Release_21d_mM`, `Si_Release_21d_mM`) that exist only in `kinetic_blueprint_master.csv`. 4 of 5 plot cells crash. |
| `08_microstructure_analysis` | `NameError: kb_df` | Same undefined-variable bug. |

No notebook has committed outputs, so nothing is verified.

### 3.2 Committed results do not match the code + data ❌
- **`data/processed/model_results.csv`**: claims Random Forest MAE = 1.4663, R² = 0.9371. Reproducible run of notebook 03 / `src/models.py` gives **MAE = 1.5232, R² = 0.9333**. Exhaustive search over random states 0–19 × tree counts 50–500 found no configuration producing the committed numbers.
- **`data/processed/korsmeyer_peppas_parameters.csv` + `docs/model_validation.md` + `results/transport_model_validation_summary.md`**: claim n = 0.25 / R² = 0.993 and n = 0.58 / R² = 0.997. The actual OLS fit on the committed `transport_kinetics.csv` gives **n = 0.256 / R² = 0.999 and n = 0.581 / R² = 0.9997**. The committed parameters and the R² values quoted in the docs were evidently produced from a different (earlier) dataset version.

### 3.3 Data integrity issues
- **Phase fractions that don't sum to 100%:** `data/raw/initial_phase_composition.csv` @ 700 °C = 54.40 + 4.14 + 37.31 + 8.29 = **104.14%**.
- **Two conflicting versions of the 700 °C composition:** raw file says 54.4/4.1/37.3/8.3; `kinetic_blueprint_master.csv` and `data/processed/phase_composition.csv` say 52.2/4.0/35.8/8.0. The ML dataset is built from the raw (non-normalized) version — so the "master" dataset and the ML dataset disagree at 700 °C.
- **pH inconsistency:** master says `Final_pH_21d` = 8.38 @ 700 °C; `pH_time_series.csv` says 8.35 @ day 21; notebook 06 hardcodes 8.35. Three different values for the same quantity.
- **SBF 900 °C day-3 row sums to 99.76%** (rounding — minor).
- **`Kinetic_Exponent_n` for 800/900/1000 °C** (0.38/0.44/0.49) appears in the master dataset with no supporting time-series in the repo — only 700 °C and 1100 °C have transport data to fit.

### 3.4 "Raw XRD patterns" are not real diffraction data ⚠️
`data/raw/xrd_patterns.csv` contains **6 rows**: 2θ = 20.00, 20.05, 20.10, 29.90, 30.00, 80.00. A real XRD scan spans tens of degrees with hundreds–thousands of points. This is a placeholder, and `figures/characterization/xrd_phase_evolution.png` (the figure notebook 07 is supposed to produce) is **1 byte — corrupt/empty**.

### 3.5 Missing data claimed in docs
- `sem_metadata.csv` references `data/sem_images/700C/…` etc. — **the `sem_images/` directory does not exist** anywhere in the repo or in the Zenodo archive, yet docs/README/notebook-08 advertise an "SEM Image Archive."
- `docs/dataset_description.md` gives wrong paths (`data/processed/kinetic_blueprint_master.csv`, `data/processed/sem_metadata.csv` — actual locations are `data/`).
- `figures/README.md` references `notebooks/11_xrd_pattern_visualization.ipynb`, which doesn't exist (it's `07_xrd_pattern_analysis.ipynb`).

### 3.6 Bioactivity data looks idealized ⚠️
`biological_response.csv`: triplicate "replicates" are spaced almost exactly linearly (e.g., 700 °C: 92.5/81.0/71.5/62.0/56.5 with σ ≈ 1.5; 1100 °C: 192/238/268/288/302 with σ ≈ 3). Real experimental triplicates are not this clean. Also, `ISO_10993_Status` values include `"Upregulated"` and `"Upregulated (~300%)"` — not ISO 10993-5 categories (the standard classifies relative to control; >100% viability isn't a defined status). These data appear curated/idealized rather than raw measurements; fine as *derived* values, but they're labeled as experimental.

### 3.7 ML claims are statistically thin ⚠️
- 25 samples total, 5 in the test set; single fixed 80/20 split, no cross-validation. R² ≈ 0.93 on 5 points is not evidence of predictive power.
- Features include `initial_crystallinity_pct = 100 − initial_amorphous_pct` — near-duplicate of `initial_amorphous_pct` (mild leakage/redundancy).
- The README promises "physics-informed modeling"; the actual code is plain `LinearRegression` + `RandomForestRegressor`. Scope/claim mismatch.

### 3.8 Packaging & archive drift
- `requirements.txt` lists the same 6 packages **twice** (duplicated block), and omits `scipy`, which notebook 02 imports directly (works only via sklearn's transitive dependency).
- Zenodo v1.0.1 (2026-08-02) ≠ current `main`: the archive has 8 notebooks, no `results/`, no `model_validation.md`/`kinetic_blueprint_evidence.md`/`research_assets.md`, fewer processed CSVs. The DOI badge points at a stale snapshot; there's no newer release.
- Git history is a single squashed commit (`Restore 'Research Context' section in README`) — no incremental history, no tags on main (tag `v1.0.1` exists on origin only).

---

## 4. Verdict

**Overall: promising skeleton, not yet a trustworthy "reproducible research platform."** The concept, author credibility, documentation, and packaging are good — this is a legitimate research-adjacent repo (not spam or an AI-generated artifact dump). But in its current state it fails its own central promise: **3/10 notebooks crash, and the headline numbers in `model_results.csv`, `korsmeyer_peppas_parameters.csv`, and the docs cannot be reproduced from the committed code and data.** Combined with the placeholder XRD file, the missing SEM image archive, and the impossible-looking bioactivity triplicates, the "experimental datasets" should be treated as curated/synthetic until provenance is clarified.

### Recommended priority fixes
1. Fix notebooks 04, 05, 08 (load `kinetic_blueprint_master.csv` as `kb_df`; fix column references; merge in `sem_metadata`), re-run all 10, and commit outputs.
2. Re-run the pipeline and regenerate `model_results.csv` + `korsmeyer_peppas_parameters.csv`, and update R² values in `docs/model_validation.md` and `results/transport_model_validation_summary.md`.
3. Normalize/correct the 700 °C initial phase composition (104.14% → 100%) and reconcile the two 700 °C variants; reconcile `Final_pH_21d` (8.35 vs 8.38).
4. Either replace `xrd_patterns.csv` with the real scan (from the Crystals 2023 paper) and regenerate the figure, or remove the XRD claims; same for SEM images.
5. State data provenance explicitly in `data/README.md` (which values are digitized from the paper vs. computed/idealized), and label ISO-status categories correctly.
6. Add cross-validation (e.g., leave-one-temperature-out) to the ML workflow and soften "physics-informed" language, or add an actual mechanistic model.
7. Clean `requirements.txt` (dedupe, add `scipy`); re-archive to Zenodo so the DOI matches `main`.

---

*Evaluation performed by running the repo's own code in a clean Python 3.11 venv with `requirements.txt`; all test artifacts were reverted afterward (working tree clean).*
