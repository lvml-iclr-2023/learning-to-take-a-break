# Learning to Take a Break: Sustainable Optimization of Long-Term User Engagement 

Predator-Prey models for long-term engagement optimization. 🦊🐇

Comments are welcome!

## Environment setup
```
conda create -n lvml anaconda
conda activate lvml
conda install -c conda-forge scikit-surprise
```

## Repository structure
* `run_experiments.ipynb` - Run and analyze MovieLens/Goodreads experients. Results are written to `./output`.
* `analyze_experiment.ipynb` - Reproduce experiment analysis (Figure 3, Figure 6). Analysis of each dataset was performed on 10 random seeds `[1,...,10]`.
* `schematic_diagrams.ipynb` - Reproduce the remaining figures.
* `prepare_goodreads_dataset.ipynb` - Prepare the Goodreads dataset for analysis.
* `lvml/core/simulation.py` - Core simulation code, optimized TPP simulator, ODE solver wrapper.
* `lvml/core/policy.py` - Implementation of core policy optimizers (`LV`, `best-of`, `default`).
* `lvml/experiment/*` - Experiment-related utilities. 
