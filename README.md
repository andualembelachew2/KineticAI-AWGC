{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# KineticAI-AWGC\n",
    "\n",
    "[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21759552.svg)](https://doi.org/10.5281/zenodo.21759552)\n",
    "[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)\n",
    "[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)\n",
    "\n",
    "![Kinetic Blueprint Framework](figures/kinetic_blueprint_framework.png)\n",
    "\n",
    "## Overview\n",
    "\n",
    "**KineticAI** is an open computational research platform for predictive materials design through physics-informed modeling, kinetic analysis, multiscale characterization, and data-driven materials engineering.\n",
    "\n",
    "The platform integrates experimental observations, mechanistic understanding, and computational workflows to establish predictive processing–structure–property relationships across complex materials systems."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Research Context\n",
    "\n",
    "While developed using bioactive glass-ceramic systems, the computational principles demonstrated in **KineticAI-AWGC** are broadly applicable to predictive materials research involving:\n",
    "\n",
    "* Structure evolution\n",
    "* Transport phenomena\n",
    "* Reaction kinetics\n",
    "* Property evolution\n",
    "* Data-driven materials design"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scientific Workflow\n",
    "\n",
    "The framework follows a sequential pipeline to achieve predictive materials design:\n",
    "\n",
    "```text\n",
    "Thermal Processing\n",
    "        ↓\n",
    "Crystallization Pathways\n",
    "        ↓\n",
    "Phase Architecture\n",
    "        ↓\n",
    "Microstructure\n",
    "        ↓\n",
    "Transport Behavior\n",
    "        ↓\n",
    "Microenvironment Evolution\n",
    "        ↓\n",
    "Biological Response\n",
    "        ↓\n",
    "Predictive Materials Design\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Repository Structure\n",
    "\n",
    "```text\n",
    "docs/        Scientific documentation\n",
    "data/        Experimental and processed datasets\n",
    "notebooks/   Reproducible computational workflows\n",
    "results/     Scientific findings and interpretations\n",
    "figures/     Framework and analysis figures\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Research Assets\n",
    "\n",
    "Key quantitative evidence and analysis domains within the framework:\n",
    "\n",
    "### Asset 1 — Phase Evolution\n",
    "Processing-induced phase architecture evolution across thermal treatment conditions.\n",
    "\n",
    "### Asset 2 — Density Evolution\n",
    "Thermal densification behavior and structural compaction kinetics.\n",
    "\n",
    "### Asset 3 — Transport Model Validation\n",
    "Parameter identification, diffusional mechanics, and transport-regime classification.\n",
    "\n",
    "### Asset 4 — Microenvironment Evolution\n",
    "pH regulation, ion release dynamics, and interfacial microenvironment behavior.\n",
    "\n",
    "> **Detailed Evidence & Documentation:**\n",
    "> * `docs/research_assets.md`\n",
    "> * `docs/kinetic_blueprint_evidence.md`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reproducible Workflows\n",
    "\n",
    "Key computational modules demonstrating end-to-end data transformation and parameter estimation:\n",
    "\n",
    "### 09 — Transport Model Validation\n",
    "Experimental dissolution data are analyzed using the Korsmeyer–Peppas framework to extract:\n",
    "* Diffusional exponent ($n$)\n",
    "* Kinetic constant ($k$)\n",
    "* Goodness-of-fit ($R^2$)\n",
    "\n",
    "*Outputs:*\n",
    "* `data/processed/transport_kinetics.csv`\n",
    "* `data/processed/korsmeyer_peppas_parameters.csv` \n",
    "\n",
    "### 10 — Phase Evolution Analysis\n",
    "Quantification of processing-induced phase evolution across the thermal processing spectrum.\n",
    "\n",
    "*Outputs:*\n",
    "* `data/processed/phase_composition.csv` \n",
    "* `docs/phase_evolution_summary.md`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Analytical Notebooks\n",
    "\n",
    "The `notebooks/` directory contains complete, reproducible analytical workflows broken down by stage:\n",
    "\n",
    "* **01** Data Cleaning\n",
    "* **02** Exploratory Analysis\n",
    "* **03** Phase Prediction Model\n",
    "* **04** Bioactivity Interpretation\n",
    "* **05** Microenvironment Evolution\n",
    "* **06** Biological Response\n",
    "* **07** XRD Pattern Analysis\n",
    "* **08** Microstructure Analysis\n",
    "* **09** Transport Model Validation\n",
    "* **10** Phase Evolution Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Current Datasets\n",
    "\n",
    "The repository maintains the following core and processed datasets in the `data/` directory:\n",
    "\n",
    "* `phase_composition.csv` \n",
    "* `density_evolution.csv` \n",
    "* `transport_kinetics.csv` \n",
    "* `korsmeyer_peppas_parameters.csv` \n",
    "* `ph_evolution.csv` \n",
    "* Raw XRD Pattern Dataset\n",
    "* SEM Metadata Dataset & Image Archive\n",
    "* Biological Response Dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Model Validation\n",
    "\n",
    "The repository includes reproducible transport-model validation workflows based on experimentally measured mass attenuation data.\n",
    "\n",
    "The Korsmeyer–Peppas model provided the highest goodness-of-fit ($R^2 > 0.99$) and revealed a transition from quasi-Fickian burst transport (700°C) to controlled anomalous transport (1100°C).\n",
    "\n",
    "**Associated Resources:**\n",
    "* Dataset: `data/processed/transport_kinetics.csv` \n",
    "* Documentation: `docs/model_validation.md` \n",
    "* Workflow Notebook: `notebooks/09_transport_model_validation.ipynb`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Installation & Quick Start\n",
    "\n",
    "### 1. Environment Setup\n",
    "\n",
    "Clone the repository and enter the directory:\n",
    "\n",
    "```bash\n",
    "git clone [https://github.com/](https://github.com/)<username>/KineticAI-AWGC.git\n",
    "cd KineticAI-AWGC\n",
    "```\n",
    "\n",
    "Install the required Python dependencies:\n",
    "\n",
    "```bash\n",
    "pip install -r requirements.txt\n",
    "```\n",
    "\n",
    "### Core Dependencies\n",
    "* `pandas` \n",
    "* `numpy` \n",
    "* `matplotlib` \n",
    "* `seaborn` \n",
    "* `scikit-learn` \n",
    "* `scipy` \n",
    "* `jupyter` \n",
    "\n",
    "### 2. Execution\n",
    "\n",
    "Launch Jupyter Notebook:\n",
    "\n",
    "```bash\n",
    "jupyter notebook\n",
    "```\n",
    "\n",
    "**Recommended Execution Sequence:**\n",
    "1. `07_xrd_pattern_analysis.ipynb` \n",
    "2. `08_microstructure_analysis.ipynb` \n",
    "3. `02_exploratory_analysis.ipynb` \n",
    "4. `05_microenvironment_evolution.ipynb` \n",
    "5. `06_biological_response.ipynb` \n",
    "6. `09_transport_model_validation.ipynb` \n",
    "7. `10_phase_evolution_analysis.ipynb`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Documentation & Publications\n",
    "\n",
    "Additional scientific context, methodologies, and publication records are available in the `docs/` directory:\n",
    "\n",
    "* **Publications:** `docs/publications.md` \n",
    "* **Project Summary:** `docs/project_summary.md` \n",
    "* **Scientific Background:** `docs/scientific_background.md` \n",
    "* **Framework Overview:** `docs/framework_overview.md` \n",
    "* **Dataset Description:** `docs/dataset_description.md` \n",
    "* **Materials Informatics Relevance:** `docs/materials_informatics_relevance.md`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Research Vision\n",
    "\n",
    "**KineticAI-AWGC** serves as a demonstration platform for the **Kinetic Blueprint Framework** and contributes toward the broader goal of predictive computational materials research.\n",
    "\n",
    "The long-term vision is to integrate experimental characterization, physics-informed modeling, quantitative analysis, and machine learning into reproducible frameworks capable of connecting processing history, structure evolution, and performance prediction across complex materials systems."
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
