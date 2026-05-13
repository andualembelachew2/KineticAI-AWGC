
# KineticAI-AWGC

**Physics-informed machine learning for predicting phase evolution and bioactivity in spray-pyrolyzed apatite–wollastonite glass-ceramics.**

## Overview

KineticAI-AWGC is a materials informatics project based on experimentally derived datasets from Dr. Andualem Belachew Workie's Ph.D. research on spray-pyrolyzed apatite–wollastonite glass-ceramics.

The project aims to translate experimental materials science data into a structured machine-learning workflow for modeling:

- Sintering-driven phase evolution
- Simulated body fluid (SBF)-induced phase transformation
- Hydroxyapatite evolution
- Bioactivity-related trends in glass-ceramic systems

## Scientific Motivation

Apatite–wollastonite glass-ceramics are promising biomaterials for bone repair because their functional performance depends on the balance between bioactivity, controlled degradation, and mechanical stability.

In this system, sintering temperature controls the formation of key phases:

- Amorphous glass phase
- Wollastonite
- Hydroxyapatite
- Whitlockite

This repository explores whether machine-learning tools can capture the processing–structure–bioactivity relationship from experimentally curated datasets.

## Research Question

Can sintering temperature and SBF soaking time be used to predict phase evolution and bioactivity-related trends in spray-pyrolyzed apatite–wollastonite glass-ceramics?

## Dataset

The current dataset includes:

1. `initial_phase_composition.csv`  
   Phase composition of AWGC samples sintered from 700 °C to 1100 °C.

2. `sbf_phase_evolution.csv`  
   Phase evolution of AWGC samples after immersion in simulated body fluid for 3, 5, 7, 14, and 21 days.

The datasets are manually curated from Ph.D.-derived experimental results and first-author publications.

## Planned Machine Learning Workflow

The project will develop an interpretable machine-learning workflow with the following stages:

1. Data cleaning and feature engineering
2. Exploratory data visualization
3. Phase-fraction prediction
4. Bioactivity trend interpretation
5. Model interpretation and scientific discussion

## Planned Notebooks

The planned notebooks are:

1. `01_data_cleaning.ipynb`
2. `02_exploratory_analysis.ipynb`
3. `03_phase_prediction_model.ipynb`
4. `04_bioactivity_interpretation.ipynb`

## Current Status

This repository is under active development.

Completed:

- Repository setup
- Raw dataset creation
- Initial phase composition dataset
- SBF phase evolution dataset
- Python dependency file

Next steps:

- Create processed dataset
- Add exploratory analysis notebook
- Develop phase-prediction model
- Generate scientific visualizations

## Technical Stack

- Python
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn
- Jupyter Notebook

## Project Significance

This project demonstrates a transition from experimental materials science toward artificial intelligence and materials informatics. It provides a reproducible framework for converting XRD-derived phase data and SBF bioactivity measurements into structured datasets suitable for interpretable machine learning.

## Author

**Dr. Andualem Belachew Workie**  
Materials Scientist | Spray Pyrolysis | Bioactive Glass-Ceramics | Materials Informatics  

GitHub: https://github.com/andualembelachew2
