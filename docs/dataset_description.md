{
  "repository": "seetin/KineticAI-AWGC",
  "framework": "Kinetic Blueprint",
  "datasets": {
    "master_dataset": {
      "title": "Kinetic Blueprint Master Dataset",
      "description": "This dataset summarizes the relationships between thermal processing, phase architecture, transport behavior, and network connectivity in spray-pyrolyzed apatite–wollastonite glass-ceramic systems.",
      "origin": "Derived from peer-reviewed experimental studies forming the foundation of the Kinetic Blueprint framework and the KineticAI-AWGC computational research platform.",
      "scientific_significance": "Explores how thermal processing governs phase architecture, network connectivity, transport behavior, and bioactivity in glass-ceramic systems by integrating structural descriptors with functional outcomes.",
      "variables": [
        {
          "name": "Temperature_C",
          "description": "Sintering temperature"
        },
        {
          "name": "Amorphous_Percent",
          "description": "Residual amorphous phase content"
        },
        {
          "name": "Wollastonite_Percent",
          "description": "Wollastonite phase fraction"
        },
        {
          "name": "Hydroxyapatite_Percent",
          "description": "Hydroxyapatite phase fraction"
        },
        {
          "name": "Whitlockite_Percent",
          "description": "Whitlockite phase fraction"
        },
        {
          "name": "Bulk_Density_g_cm3",
          "description": "Measured bulk density"
        },
        {
          "name": "MassLoss_21d_Percent",
          "description": "Mass loss after 21 days SBF immersion"
        },
        {
          "name": "Final_pH_21d",
          "description": "Solution pH after 21 days"
        },
        {
          "name": "Ca_Release_21d_mM",
          "description": "Calcium release after 21 days"
        },
        {
          "name": "Si_Release_21d_mM",
          "description": "Silicon release after 21 days"
        },
        {
          "name": "NBO_BO_Ratio",
          "description": "Non-bridging oxygen to bridging oxygen ratio"
        },
        {
          "name": "Kinetic_Exponent_n",
          "description": "Transport exponent"
        },
        {
          "name": "Transport_Mechanism",
          "description": "Mechanistic interpretation of transport behavior"
        }
      ]
    },
    "ph_time_series_dataset": {
      "title": "pH Time-Series Dataset",
      "description": "Captures the evolution of solution pH during SBF immersion for AWGC samples sintered between 700 °C and 1100 °C.",
      "scientific_significance": "Provides a direct measure of microenvironment evolution during degradation and bioactivity processes, serving as a bridge between transport behavior and biological response.",
      "variables": [
        {
          "name": "Time_Days",
          "description": "SBF immersion duration"
        },
        {
          "name": "pH_700C",
          "description": "Measured pH for 700 °C sample"
        },
        {
          "name": "pH_800C",
          "description": "Measured pH for 800 °C sample"
        },
        {
          "name": "pH_900C",
          "description": "Measured pH for 900 °C sample"
        },
        {
          "name": "pH_1000C",
          "description": "Measured pH for 1000 °C sample"
        },
        {
          "name": "pH_1100C",
          "description": "Measured pH for 1100 °C sample"
        }
      ]
    }
  }
}
