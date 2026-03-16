This document records reproducible experiments performed using the
QEC simulator. Each experiment specifies:

- the research question  
- simulation parameters  
- experimental setup  
- results  
- conclusions  

All experiments can be reproduced using the CLI commands provided.
Experiments get more and more complex the further you scroll down.

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

## Observations
- Logical error rate decreases as repetition code length increases.
- Larger codes suppress errors more effectively at low physical error rates.
- At higher physical error rates, logical errors increase rapidly.

**Conclusion:**
  
Increasing code distance improves logical error suppression under independent bit‑flip noise, particularly when the physical error probability is small.

# Experiment 2: Code Distance Effect at Fixed Noise

## Research Question

How does increasing repetition code length affect logical error rate at a fixed physical error probability?

## Setup

Noise model: independent bit‑flip noise  
Decoder: majority vote  
Simulation method: Monte Carlo sampling  

| Parameter | Value |
|----------|------|
| Trials | 5000 |
| Seed | 0 |
| Physical error probability | p = 0.10 |
| Code sizes tested | n = 3, 5, 7 |

## Command

```bash
python -m QECsim.plot --n 3 5 7 --trials 5000 --seed 0 --logicalbit 0 --pmin 0.10 --pmax 0.10 --pstep 0.01
```
**Results:**

[QECsim_noise_results.txt](https://github.com/user-attachments/files/26032889/QECsim_noise_results.txt)
<img width="1755" height="1298" alt="plot" src="https://github.com/user-attachments/assets/1f123168-b058-42e6-a968-1d0b8c3e80ab" />

## Observations
- Logical error decreases significantly as repetition code length increases.
- Larger codes suppress errors more effectively at the same physical noise level.
- The n=7 code performs substantially better than the n=3 code.

**Conclusion:** 

Increasing redundancy through larger repetition codes significantly improves logical error suppression when physical error probability is moderate.

# Experiment 3: Monte Carlo Convergence

## Research Question

How many Monte Carlo trials are required for the logical error rate estimate to stabilize?

Since the simulator uses Monte Carlo sampling to estimate logical error rates, the number of trials affects the statistical reliability of the result.

## Setup

| Parameter | Value |
|----------|------|
| Code size | n = 5 |
| Physical error probability (p) | 0.10 |
| Trial counts tested | 500, 1000, 5000, 10000 |
| Random seed | 0 |

Noise model: independent bit‑flip noise  
Decoder: majority vote  
Simulation method: Monte Carlo sampling  

## Commands

Example commands used to test convergence:

```bash
python -m QECsim.plot --n 5 --trials 500 --seed 0 --logicalbit 0 --pmin 0.10 --pmax 0.10
```
```bash
python -m QECsim.plot --n 5 --trials 1000 --seed 0 --logicalbit 0 --pmin 0.10 --pmax 0.10
```
```bash
python -m QECsim.plot --n 5 --trials 5000 --seed 0 --logicalbit 0 --pmin 0.10 --pmax 0.10
```
```bash
python -m QECsim.plot --n 5 --trials 10000 --seed 0 --logicalbit 0 --pmin 0.10 --pmax 0.10
```

I will run all of them.

**Results:**

[1.txt](https://github.com/user-attachments/files/26033322/1.txt)
[2.txt](https://github.com/user-attachments/files/26033310/2.txt)
[3.txt](https://github.com/user-attachments/files/26033325/3.txt)[4.txt](https://github.com/user-attachments/files/26033327/4.txt)
[4.txt](https://github.com/user-attachments/files/26033331/4.txt)
<img width="877" height="631" alt="image" src="https://github.com/user-attachments/assets/2ae6a861-ac7f-46cf-9a72-b172e606056c" />

## Observations
- Logical error estimates vary when the number of trials is small due to statistical noise.
- As the number of Monte Carlo trials increases, the estimated logical error rate stabilizes.
- Larger trial counts reduce variance in the simulation results.

**Conclusion:**

Monte Carlo simulations require sufficiently large trial counts to produce reliable estimates of logical error rates. Increasing the number of trials improves statistical stability and reduces sampling noise.


