# ResumeRepository

This repository collects homework solutions and research code in Python, MATLAB, and R.  Each directory contains standalone scripts demonstrating techniques in machine learning, economics, and data analysis.

## Directory Overview

* **CodeforPapers/** – Scripts used in course projects and papers.
  - `Homework3.py` performs value iteration for a dynamic discrete-choice model.
  - `dataAndAnalysis.py` provides helper routines for CSV processing.
  - `NeuralNetCode.py` implements a deep belief network with restricted Boltzmann machines.
  - `EndtoEndAnalysisMortgageData.r` analyzes mortgage data in R.

* **EconomicModels/** – Experiments with economic simulations and optimization.
  - Pricing games with and without regulation (`QlearnerWithRegulator Rewritten Det Costs.py` and `QlearnerWithoutRegulator Stochastic Marginal Costs.py`).
  - MATLAB files such as `Main.m` and `NormalCostFunction.m` explore market-entry conditions and gradient calculations.
  - `Homework1.py` demonstrates instrumental variable estimation with Python.

* **MachineLearningCode/** – A variety of Python scripts for machine learning coursework.
  - Classification examples: `Analysis of email spam.py`, `ClassifierHorseRace.py`.
  - Unsupervised learning examples: `kmeans.py`, `isomap.py`.
  - Other utilities including density estimation and face recognition.

* **MachineLearningMatlabCode/** – MATLAB versions of regression, PCA, logistic regression, and related algorithms.

* **sportsPrediction/** – Simple models that predict sports outcomes using logistic regression, random forests, and neural networks.

## Running the Code

Many scripts were originally executed in custom local environments and include `os.chdir` commands pointing to absolute paths.  These lines are now commented out.  When running a script, place the required data files in the expected locations or modify the file paths as needed.

The repository does not include a single environment file.  Installing common packages such as `numpy`, `pandas`, `matplotlib`, `scikit-learn`, and `torch` should satisfy most dependencies.

## Learning Next

Because the scripts are independent, explore them directory by directory.  The reinforcement-learning pricing games in `EconomicModels/` and the neural network implementation in `CodeforPapers/NeuralNetCode.py` are good starting points.
