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
n p logical_error_rate
3 0.00 0.000000
3 0.02 0.000800
3 0.04 0.005600
3 0.06 0.009400
3 0.08 0.016600
3 0.10 0.026600
3 0.12 0.039000
3 0.14 0.050200
3 0.16 0.069800
3 0.18 0.091600
3 0.20 0.098200
5 0.00 0.000000
5 0.02 0.000000
5 0.04 0.001200
5 0.06 0.001200
5 0.08 0.003400
5 0.10 0.008000
5 0.12 0.014800
5 0.14 0.018000
5 0.16 0.035800
5 0.18 0.045800
5 0.20 0.057800
7 0.00 0.000000
7 0.02 0.000000
7 0.04 0.000200
7 0.06 0.000200
7 0.08 0.001000
7 0.10 0.002400
7 0.12 0.006000
7 0.14 0.008600
7 0.16 0.016000
7 0.18 0.024600
7 0.20 0.031400
<img width="1728" height="1298" alt="plot" src="https://github.com/user-attachments/assets/7256f1e0-fcd0-480f-8e73-e75b4ee3874d" />



