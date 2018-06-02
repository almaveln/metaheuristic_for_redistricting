#!/bin/bash

#SBATCH -J plsa18
#SBATCH -n 250
#SBATCH --cpus-per-task=1
#SBATCH --mem=10000
#SBATCH -t 2-00:00:00
#SBATCH -p main
#SBATCH --output=region_18_18_sa_v90_ranks_main.out

mpirun python mpi_region_18_18.py
