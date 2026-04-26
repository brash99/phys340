# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

University course repository for **Physics 340 - Methods of Theoretical Physics** at Christopher Newport University (CNU), taught by Professor Edward Brash. All course content is delivered via Jupyter Notebooks (.ipynb).

## Repository Structure

- **JupyterNotebooks/** — Core lecture material organized into 7 topical parts:
  - `PartI_Vectors/` — Vector algebra, 2D/3D operations
  - `PartII_Matrices/` — Matrix operations, eigenvalues, transformations, moment of inertia
  - `PartIII_VectorCalculus/` — Vector calculus and applications
  - `PartIV_ComplexAnalysis/` — Complex numbers and functions
  - `PartV_FourierSeries/` — Fourier analysis and transforms
  - `PartVI_PDE/` — Partial differential equations (heat, wave, Laplace)
  - `PartVII_ExtraMaterial/` — Keplerian orbits and special topics
- **Assignments/** — Student assignments and exams (Midterm1, Midterm2, FinalExam subdirectories)
- **LectureNotes/** — PDF lecture notes organized by week
- **Documents/** — Course materials and reference PDFs

## Shared Python Modules

Three utility modules at the repo root are imported by notebooks:

- **`imports.py`** — Centralized imports for all common dependencies (NumPy, SciPy, SymPy, Matplotlib, Pandas, librosa, etc.) with environment diagnostics
- **`rk_functions.py`** — Runge-Kutta 4th-order (`rk4`) and adaptive Runge-Kutta (`rka`) implementations for orbital mechanics (gravitational N-body via `gravrk`)
- **`timer.py`** — Simple `Timer` class for benchmarking code execution

## Key Dependencies

NumPy, SciPy (integrate, optimize, special, signal, fftpack), SymPy, Matplotlib, Pandas, librosa. No requirements.txt — students use pre-configured environments.

## Branch Strategy

- **`main`** — Primary branch with course materials (assignments without solutions)
- **`solutions`** — Contains assignment solutions
- Shell scripts `update_main_branch` and `update_solutions_branch` automate merging between branches

## Notebook Naming Convention

Notebooks use alphabetical prefixes (AAA_, BBB_, CCC_, etc.) indicating sequential progression within each Part directory.

## Running Notebooks

Notebooks are run via Jupyter. To verify the environment has all dependencies:
```
jupyter notebook JupyterNotebooks/test_imports.ipynb
```
