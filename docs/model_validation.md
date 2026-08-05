# Model Validation

## Objective

To identify the transport mechanism governing mass attenuation in phase-programmed apatite-wollastonite glass-ceramic systems.

## Models Evaluated

The experimental data were fitted using:

- Zero-order kinetics
- First-order kinetics
- Higuchi diffusion model
- Korsmeyer-Peppas model

## Data

Fits use the committed degradation time series in `data/processed/transport_kinetics.csv` (notebook `09_transport_model_validation.ipynb`). The reported parameters below are reproduced exactly by re-running that notebook.

## Results

### 700°C Sample

Best Model:

Korsmeyer-Peppas

Parameters:

- n = 0.256
- k = 4.69E-02
- R² = 0.9990

Interpretation:

Rapid quasi-Fickian burst transport.

---

### 1100°C Sample

Best Model:

Korsmeyer-Peppas

Parameters:

- n = 0.581
- k = 4.49E-03
- R² = 0.9997

Interpretation:

Controlled anomalous transport.

---

## Scientific Significance

Thermal processing changes the governing transport mechanism.

700°C:

Burst dissolution

↓

1100°C:

Controlled diffusion-governed transport

This transition forms the basis of the Kinetic Blueprint Framework.
