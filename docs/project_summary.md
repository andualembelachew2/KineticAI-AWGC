
# Project Summary

## Project Title

**KineticAI-AWGC: Physics-Informed Machine Learning for Bioactive Glass-Ceramics**

## Objective

This project develops an interpretable materials informatics workflow for modeling phase evolution and bioactivity-related trends in spray-pyrolyzed apatite–wollastonite glass-ceramics.

The project is based on experimentally derived datasets from Dr. Andualem Belachew Workie's Ph.D. research and first-author publications.

## Scientific Background

Apatite–wollastonite glass-ceramics are bioactive ceramic materials with potential applications in bone repair, implant coatings, and regenerative biomaterials.

Their performance depends strongly on the balance between:

- Crystalline phase composition
- Amorphous glass content
- Hydroxyapatite formation
- Wollastonite stability
- Simulated body fluid response

In the experimental system used here, sintering temperature controls the initial phase assemblage. Subsequent immersion in simulated body fluid produces time-dependent phase evolution that reflects the material's bioactive response.

## Dataset

The current project uses two manually curated datasets:

1. `initial_phase_composition.csv`

   This dataset contains the initial phase composition of AWGC samples sintered at 700, 800, 900, 1000, and 1100 °C.

2. `sbf_phase_evolution.csv`

   This dataset contains phase evolution after SBF immersion for 3, 5, 7, 14, and 21 days.

## Machine Learning Goal

The main goal is to explore whether basic machine-learning models can learn relationships between:

- Sintering temperature
- SBF soaking time
- Phase composition
- Hydroxyapatite evolution
- Bioactivity-related trends

## Planned Workflow

The project will proceed through four stages:

1. Data cleaning and feature engineering
2. Exploratory data visualization
3. Phase-fraction prediction
4. Bioactivity interpretation

## Why This Project Matters

This project demonstrates how experimental materials science data can be converted into a structured artificial-intelligence workflow.

Rather than using generic datasets, this repository uses real experimental data from spray pyrolysis, XRD-based phase quantification, and SBF bioactivity testing.

The project represents a first step toward AI-assisted design of bioactive glass-ceramics.
