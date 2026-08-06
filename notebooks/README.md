# Notebooks

This directory contains the analytical notebooks supporting the KineticAI-AWGC platform and the Kinetic Blueprint framework for deterministic materials design.

The notebooks are organized to follow the complete scientific workflow from raw experimental data to biological response.

---

## 01 Data Cleaning

Purpose:

- Data preparation
- Dataset integration
- Feature engineering

Key Outputs:

- Processed machine-learning dataset (`data/processed/awgc_ml_dataset.csv`)

---

## 02 Exploratory Analysis

Purpose:

- Structure–transport relationships
- Mechanistic discovery

Key Topics:

- NBO/BO ratio
- Density
- Amorphous content
- Mass loss
- Calcium release
- Silicon release

---

## 03 Phase Prediction Model

Purpose:

- Machine-learning prediction of phase evolution

Key Topics:

- Random Forest modeling
- Feature importance analysis
- Predictive confirmation of Kinetic Blueprint relationships

---

## 04 Bioactivity Interpretation

Purpose:

- Scientific synthesis
- Deterministic materials-design framework

Key Topics:

- Processing–structure–transport relationships
- Kinetic Blueprint design regions
- Bioactivity interpretation

---

## 05 Microenvironment Evolution

Purpose:

- Analysis of pH evolution during SBF immersion

Key Topics:

- NBO/BO vs pH
- Mass loss vs pH
- Calcium release vs pH
- Silicon release vs pH
- Microenvironment regulation

---

## 06 Biological Response

Purpose:

- Evaluation of cellular response

Key Topics:

- Cell viability
- ISO 10993 interpretation
- Processing-dependent biological behavior
- Microenvironment–biological response relationships

---

## 07 XRD-Derived Phase Composition Analysis

Purpose:

- Investigation of crystallization pathways using XRD-quantified phase composition

Key Topics:

- Phase architecture vs sintering temperature
- Crystallinity evolution
- Crystallization trends
- Phase-architecture foundation

Note: the raw diffraction spectra are published with the source studies (see `docs/publications.md`); this repository ships the XRD-quantified phase fractions extracted from them.

---

## 08 Microstructure Analysis

Purpose:

- Investigation of SEM-derived microstructural evolution

Key Topics:

- Morphological evolution
- Degradation morphology
- Mineral-layer formation
- Microstructure–transport relationships

---

## Scientific Workflow

The notebooks collectively support the Kinetic Blueprint framework:

Thermal Processing
↓
Crystallization Pathways
↓
Phase Architecture
↓
Microstructure
↓
Transport Behavior
↓
Microenvironment Evolution
↓
Biological Response
↓
Deterministic Materials Design
