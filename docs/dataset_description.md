# Dataset Description

## Overview

This document provides the machine-readable metadata for the **Kinetic Blueprint** project, including the experimental datasets, scientific workflow, and planned computational modules.

```json
{
  "project": {
    "name": "Kinetic Blueprint",
    "version": "1.0.0",
    "description": "Open experimental datasets and computational framework for deterministic materials design through thermal processing, phase architecture, network connectivity, transport behavior, and biointerface engineering.",
    "keywords": [
      "glass-ceramics",
      "biomaterials",
      "bone-regeneration",
      "materials-science",
      "kinetics",
      "transport",
      "machine-learning",
      "kinetic-blueprint",
      "kineticai",
      "apatite",
      "wollastonite",
      "open-science"
    ],
    "license": "MIT",
    "repository": "https://github.com/yourusername/Kinetic-Blueprint",
    "homepage": "https://github.com/yourusername/Kinetic-Blueprint",
    "datasets": [
      {
        "name": "Kinetic Blueprint Master Dataset",
        "file": "data/kinetic_blueprint_master.csv",
        "description": "Experimental dataset describing relationships among thermal processing, phase architecture, network connectivity, transport behavior, and bioactivity in apatite–wollastonite glass-ceramic systems."
      },
      {
        "name": "Interfacial pH Time-Series Dataset",
        "file": "data/interfacial_ph_timeseries.csv",
        "description": "Time-resolved pH evolution during SBF immersion capturing interfacial microenvironment evolution and functional classification.",
        "variables": [
          {
            "name": "Time_Days",
            "type": "integer",
            "unit": "days",
            "description": "Immersion time in simulated body fluid (SBF)."
          },
          {
            "name": "Temperature_C",
            "type": "integer",
            "unit": "°C",
            "description": "Sintering temperature."
          },
          {
            "name": "pH_Value",
            "type": "number",
            "unit": "pH",
            "description": "Measured solution pH."
          },
          {
            "name": "Interfacial_Classification",
            "type": "string",
            "description": "Classification of the interfacial chemical environment."
          }
        ],
        "records": [
          {
            "Time_Days": 0,
            "Temperature_C": 700,
            "pH_Value": 7.40,
            "Microenvironment_Region": "Baseline SBF"
          },
          {
            "Time_Days": 1,
            "Temperature_C": 700,
            "pH_Value": 8.32,
            "Microenvironment_Region": "Alkaline Shock"
          },
          {
            "Time_Days": 3,
            "Temperature_C": 700,
            "pH_Value": 8.55,
            "Microenvironment_Region": "Peak Alkaline Shock"
          },
          {
            "Time_Days": 5,
            "Temperature_C": 700,
            "pH_Value": 8.48,
            "Microenvironment_Region": "Cytotoxic Region"
          },
          {
            "Time_Days": 7,
            "Temperature_C": 700,
            "pH_Value": 8.42,
            "Microenvironment_Region": "Cytotoxic Region"
          },
          {
            "Time_Days": 14,
            "Temperature_C": 700,
            "pH_Value": 8.38,
            "Microenvironment_Region": "Cytotoxic Region"
          },
          {
            "Time_Days": 21,
            "Temperature_C": 700,
            "pH_Value": 8.35,
            "Interfacial_Classification": "Cytotoxic Region"
          },
          {
            "Time_Days": 0,
            "Temperature_C": 1100,
            "pH_Value": 7.40,
            "Microenvironment_Region": "Baseline SBF"
          },
          {
            "Time_Days": 1,
            "Temperature_C": 1100,
            "pH_Value": 7.48,
            "Microenvironment_Region": "Homeostatic Buffer"
          },
          {
            "Time_Days": 3,
            "Temperature_C": 1100,
            "pH_Value": 7.55,
            "Microenvironment_Region": "Homeostatic Buffer"
          },
          {
            "Time_Days": 5,
            "Temperature_C": 1100,
            "pH_Value": 7.60,
            "Microenvironment_Region": "Homeostatic Buffer"
          },
          {
            "Time_Days": 7,
            "Temperature_C": 1100,
            "pH_Value": 7.65,
            "Microenvironment_Region": "Homeostatic Buffer"
          },
          {
            "Time_Days": 14,
            "Temperature_C": 1100,
            "pH_Value": 7.72,
            "Microenvironment_Region": "Homeostatic Buffer"
          },
          {
            "Time_Days": 21,
            "Temperature_C": 1100,
            "pH_Value": 7.82,
            "Microenvironment_Region": "Homeostatic Buffer"
          }
        ]
      }
    ],
    "scientific_workflow": [
      "Thermal Processing",
      "Phase Architecture",
      "Network Connectivity",
      "Transport Behavior",
      "Microenvironment_Region",
      "Biointerface Performance"
    ],
    "future_modules": [
      "Python Analysis",
      "Machine Learning",
      "Physics-Informed Modeling",
      "Interactive Visualization",
      "KineticAI-AWGC"
    ]
  }
}
```

## Notes

- **Master Dataset:** `data/kinetic_blueprint_master.csv`
- **Interfacial pH Dataset:** `data/interfacial_ph_timeseries.csv`
- **Framework:** Kinetic Blueprint
- **Platform:** KineticAI-AWGC

This metadata describes the datasets, scientific workflow, and future computational development of the Kinetic Blueprint framework.
