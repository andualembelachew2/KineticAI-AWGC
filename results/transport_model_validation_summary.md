# Transport Model Validation Summary

## Objective

Identify the transport mechanism governing mass attenuation in phase-programmed apatite–wollastonite glass-ceramic systems.

## Dataset

transport_kinetics.csv

## Model

Korsmeyer–Peppas

## Results

| Temperature (°C) | n | k | R² |
|------------------|----|---------|-------|
| 700 | 0.256 | 4.69E-02 | 0.9990 |
| 1100 | 0.581 | 4.49E-03 | 0.9997 |

*Parameters reproduced by re-running `notebooks/09_transport_model_validation.ipynb` on the committed dataset.*

## Transport Regime Interpretation

### 700°C

- Quasi-Fickian burst transport
- Rapid dissolution of the amorphous-rich matrix
- High mass attenuation rate

### 1100°C

- Anomalous transport
- Controlled diffusion-governed behavior
- Reduced mass attenuation rate

## Key Finding

Thermal phase partitioning modifies the governing transport mechanism.

700°C:

Burst dissolution

↓

1100°C:

Controlled anomalous transport

This transition demonstrates how processing-induced phase architecture can regulate transport behavior and microenvironment evolution.
