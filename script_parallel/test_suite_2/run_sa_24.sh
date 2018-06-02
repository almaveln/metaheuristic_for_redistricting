#!/bin/bash

#SBATCH -J plsa24
#SBATCH -n 60
#SBATCH --cpus-per-task=1
#SBATCH --mem=10000
#SBATCH -t 2-00:00:00
#SBATCH -p main
#SBATCH --output=region_24_24_sa_v80_ranks_main.out

mpirun python mpi_region_24_24.py
