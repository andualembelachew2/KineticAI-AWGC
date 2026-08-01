{
  "repository": {
    "name": "KineticAI-AWGC",
    "owner": "seetin",
    "framework": "Kinetic Blueprint"
  },
  "datasets": {
    "master_dataset": {
      "title": "Kinetic Blueprint Master Dataset",
      "description": "This dataset summarizes the relationships between thermal processing, phase architecture, transport behavior, and network connectivity in spray-pyrolyzed apatite–wollastonite glass-ceramic systems. Derived from peer-reviewed experimental studies forming the foundation of the Kinetic Blueprint framework.",
      "scientific_significance": "The Kinetic Blueprint Master Dataset was created to explore how thermal processing governs phase architecture, network connectivity, transport behavior, and bioactivity in glass-ceramic systems. It integrates structural descriptors (phase fractions, density, NBO/BO ratio) with functional outcomes (mass loss, ion release, pH evolution, and transport mechanism) to support deterministic materials-design strategies.",
      "dataset_origin": "Integrates experimental measurements reported across multiple peer-reviewed studies on spray-pyrolyzed apatite–wollastonite and related glass-ceramic systems. Variables were selected to capture the relationships among thermal processing, phase architecture, network connectivity, transport behavior, and bio-interface performance. Serves as the foundational data resource for the KineticAI-AWGC computational research platform.",
      "variables": {
        "Temperature_C": "Sintering temperature",
        "Amorphous_Percent": "Residual amorphous phase content",
        "Wollastonite_Percent": "Wollastonite phase fraction",
        "Hydroxyapatite_Percent": "Hydroxyapatite phase fraction",
        "Whitlockite_Percent": "Whitlockite phase fraction",
        "Bulk_Density_g_cm3": "Measured bulk density",
        "MassLoss_21d_Percent": "Mass loss after 21 days SBF immersion",
        "Final_pH_21d": "Solution pH after 21 days",
        "Ca_Release_21d_mM": "Calcium release after 21 days",
        "Si_Release_21d_mM": "Silicon release after 21 days",
        "NBO_BO_Ratio": "Non-bridging oxygen to bridging oxygen ratio",
        "Kinetic_Exponent_n": "Transport exponent",
        "Transport_Mechanism": "Mechanistic interpretation of transport behavior"
      }
    },
    "ph_timeseries_dataset": {
      "title": "pH Time-Series Dataset",
      "description": "This dataset captures the evolution of solution pH during SBF immersion for AWGC samples sintered between 700 °C and 1100 °C.",
      "scientific_significance": "The pH dataset provides a direct measure of microenvironment evolution during degradation and bioactivity processes. It serves as a bridge between transport behavior and biological response within the Kinetic Blueprint framework.",
      "variables": {
        "Time_Days": "SBF immersion duration",
        "pH_700C": "Measured pH for 700 °C sample",
        "pH_800C": "Measured pH for 800 °C sample",
        "pH_900C": "Measured pH for 900 °C sample",
        "pH_1000C": "Measured pH for 1000 °C sample",
        "pH_1100C": "Measured pH for 1100 °C sample"
      }
    }
  }
}
