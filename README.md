**Current Version:** v1.1

**Status:** Baseline implementation with analytical validation
# QECops - Reproducible Quantum Error Correction Simulator 
## Overview:
**Example Result:**
Logical error rate vs physical error rate for repetition codes under independent bit-flip noise, including analytical validation with binomial distribution.
<img width="1910" height="1018" alt="Screenshot 2026-03-28 095221" src="https://github.com/user-attachments/assets/e0b6846a-d227-4d7b-bfea-b8c97c34de2b" />

This project provides an open-source, reproducible simulation framework for analyzing how noise assumptions affect quantum error correction (QEC) performance. This project investigates **How sensitive are QEC results to noise assumptions.**

This tool focuses on a simple but fundamental setting: repetition codes under independent bit-flip noise, comparing Monte Carlo simulation with exact analytical predictions.

**Why does it matter:**
Many existing tools are held to large institutions, this tool is open to the public, free, and completely open-source.

Error correction suppresses noise only under certain conditions, so small changes in noise assumptions can lead to very large differences in outputs/conclusions.

This tool makes those assumptions inspectable, transparent and reproducible, thus allowing users to:
  - test the strength of results
  - compare code sizes
  - understand failure behaviors
  - reproduce and resimulate baseline behaviors easily

### This tool aims to:
  - Simulate bit-flip noise
  - Will apply a repetition code
  - Will decode using majority-vote decoding
  - Measures logical error as a function of physical error rate
  - Plots the analytical curve based on binomial distribution

Primary output is essentially a standard diagnostic plot used in many quantum error correction research - being logical error rate vs physical error rate, but for different code sizes.

**Noise Model:**
This project models independent bit-flip noise, where each bit is flipped with a probability known as _p_. This represents assumed hardware error rate, which is supplied as an input to the simulation.
The tool also finds the analytical logical error rate using the binomial probability model so as to validate the Monte Carlo results which are based on repeated random trials.

**Error correction:**
Logical information is protected with a reptition code, which encodes one logical bit into multiple physical bits. Decoding is done with majority-vote decoding, which selects the most likely logical value after the noise is applied.

**Output:**
For a given physical error rate _p_ and the size of the code _n_, the tool will estimate the logical error rate, which is the probability that decoding will fail, and it uses the Monte Carlo simulation by repeatedly sampling random noise.
So by producing _p_ across a range of values and comparing the different code sizes, the tool will make a standard diagnostic plot that shows logical error rate vs physical error rate. The plot quantifies the data and shows how effectively the redundancy suppresses the errors and identifies where error correction will succeed or fail.

As for the analytical curve, it uses binomial distribution to calculate the theoretical baseline. The similarity between each curve shows validation.

### Limitations:
  - The tool does not measure hardware noise, it analyzes the error correction performance of a given assumed noise parameters
  - Noise is assumed to be independent and uncorrelated
  - The current version mode focuses on repetition codes and majority-vote decoding

The goal of this project is to give a simple, transparent, and reproducible simulation framework open to the public for studying how noise assumptions can change and impact error correction and its results.

**Assumptions:**

Currently:
  - Independent bit flip noise
  - no correlated errors
  - classical repetition code
  - majority vote decoding
  - Analytical binomial distribution

This project does not attempt to create or show new error-correction codes or to prove theoretical thresholds and boundaries. It is made and intended to be used as a measurement and analysis tool, **NOT** a theory checker or unfound breakthrough, just an easy tool for all to use.

**Project status:**

v1 has been successfully pushed! v2 planning/coding has begun.
Future extensions/ideas are seen down below under v2 plans.

**Current Project structure:**
```
src/
  QECops/
    __init__.py
    noise.py
    decode.py
    simulation.py
    plot.py
    analytical.py
REPORTS/
  EXPERIMENTS.md
  reportlinks.md
requirements.txt
README.md
LICENSE
ExampleResult.png
.gitignore
```
## Technical Reports:
A detailed explanation of the methodology, experiments, and results is available in the REPORTS folder.

**See /REPORTS for excecuted experiments and more on the stored technical reports related to this project and its methodology**

## Getting Started:
### Installation:
Make sure to download/update latest versions of pip, python, git, and related packages prior to running this simulation for best/optimal results. Once complete, proceed with installation instructions.

Clone the repository:
```bash
git clone https://github.com/JitheshMithra/QECops.git
cd QECops
```
Install required dependencies:
```bash
pip install -r requirements.txt
```
### Running the simulation:
All simulations are executed from the src directory
```bash
#example simulation:
cd src
python -m QECops.plot --n 3 5 7 --trials 20000 --seed 0 --logicalbit 0 --pmin 0.0 --pmax 0.2 --pstep 0.02
```
Command Line arguments:
  - --n: one or more ODD repetition-code lengths
  - --trials: # of Monte Carlo trials per data point
  - --logicalbit: Logical bit to encode (0 or 1)
  - --pmin, --pmax, --pstep: Physical error rate sweep parameters
  - --seed: Random seed for reproducibility
### Output:
Each run will generate timestamped results directory which contains:
  - plot.png: Static plot image of logical error rate vs physical error rate and analytical curve
  - plot.html: interactive Plotly html graph, useful for visualization and analytical curve
  - QECops_noise_results.txt: Table numerical values

These values/outputs will show direct comparison of logical error reduction across different code sizes under specified noise assumptions

### Reproducibility:
  - All simulations are fully reproducible using the fixed random seeds specified in the CLI
  - Noise models and decoding assumptions are expected to be explicitly and specifically defined
  - Results can be regenerated or extended by changing simulation parameters

Future additions (v2 plans):
  - Extended noise models (biased, correlated)
  - Log scale plots (users can plot LER on a log scale, clear error suppression, effective distance scaling)
  - Seed control per-p (use rng across entire sweep, improves statistical independence and interpretation)
  - Parameter sweeps BEYOND p 
  - Optional saving results as JSON or CSV

### Acknowledgements:
- Special thanks to _Daniel Strano_ from the Unitary Fund for external review and consistent feedback and mentoring on my methodology.
- Special thanks to _Dr. Thomas Scruby_ from the Okinawa Institute of Science and Technology (OIST) for external review and possible extensions in this project

### License:
If used or mentioned in published works please cite in the recommended format.


Copyright (c) [2025] [Jithesh Mithra].
It is licensed under the MIT License, available at [https://github.com/JitheshMithra/QECops].

Also check License page in files.
