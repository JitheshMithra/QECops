# Experiments

This document records reproducible experiments performed using the
QEC simulator. Each experiment specifies:

- the research question  
- simulation parameters  
- experimental setup  
- results  
- conclusions  

All experiments can be reproduced using the CLI commands provided.

# Experiment 1: Logical Error Scaling With Physical Noise

## Research Question

How does the logical error rate change as the physical bit‑flip probability increases for repetition codes of different lengths?

## Setup

Code: repetition code  
Decoder: majority vote  
Noise model: independent bit‑flip noise  
Simulation method: Monte Carlo sampling  

Parameters:

| Parameter | Value |
|----------|------|
| code sizes | n = 3, 5, 7 |
| trials | 5000 |
| seed | 0 |
| physical error range | 0.0 – 0.2 |
| step size | 0.02 |

## Command

```bash
cd src
python -m QECsim.plot --n 3 5 7 --trials 5000 --seed 0 --logicalbit 0 --pmin 0.0 --pmax 0.2 --pstep 0.02
```

**Results:**

[QECsim_noise_results.txt](https://github.com/user-attachments/files/26032775/QECsim_noise_results.txt)
<img width="1728" height="1298" alt="plot" src="https://github.com/user-attachments/assets/7256f1e0-fcd0-480f-8e73-e75b4ee3874d" />



