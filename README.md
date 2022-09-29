# Learning to Take a Break: Sustainable Optimization of Long-Term User Engagement 

Anonymous submission to ICLR 2023 🦊🐇

## Environment setup
```
conda create -n lvml anaconda
conda activate lvml
conda install -c conda-forge scikit-surprise
```

## Repository structure
* `movielens_experiment.ipynb` - Run and analyze MovieLens experient. Results are written to `./output`.
* `analyze_experiment.ipynb` - Reproduce experiment analysis (Figure 3). Analysis was performed on 10 random seeds `[1,...,10]`.
* `schematic_diagrams.ipynb` - Reproduce the remaining figures.
* `lvml/core/simulation.py` - Core simulation code, optimized TPP simulator, ODE solver wrapper.
* `lvml/core/policy.py` - Implementation of core policy optimizers (`LV`, `best-of`, `default`).
* `lvml/experiment/*` - Experiment-related utilities. 
