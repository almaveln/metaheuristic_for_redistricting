#!/bin/bash

#SBATCH -J plsa30
#SBATCH -n 40
#SBATCH --cpus-per-task=1
#SBATCH --mem=10000
#SBATCH -t 2-00:00:00
#SBATCH -p main
#SBATCH --output=region_30_30_sa_v80_ranks_main.out

mpirun python mpi_region_30_30.py
