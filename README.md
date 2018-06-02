# Analysis of a metaheuristic for redistricting 

The project goal is to implement a metaheuristic for redistricting and analyze it. 

## Getting Started

### Project overview

    .
    ├── common                  # includes code that can be later reused in other metaheuristics
    ├── data                    # contains data and optimal solutions for test cases    
    ├── entities                # contains data types that are used as a means of bundling geographic data  
    ├── experiments_output      # contains csv output files of run  
    ├── profiling               # contains profling info on code
    ├── script_parallel         # contains scripts that can be used to run the parallel version of SA
    ├── script_sequential       # contains scripts that can be used to run sequential version of SA
    ├── simulated_annealing     # contains an implemented version of simulated annealing 
    ├── slurm_output            # contains slurm ouput files fir test suite 1 and test suite 2 
    ├── utils                   # contains code to generate test cases and some other things
    ├── visualisation           # contains scripts/tools for visualization
    └── visualisation_output_sa # contains visualization output files 

## Running the algorithm

Simulated annealing can be run through scripts that are located in script_parallel and script_sequential
