#!/bin/bash

#SBATCH -J sa12_p1
#SBATCH -n 60
#SBATCH --cpus-per-task=1
#SBATCH -t 02:00:00
#SBATCH -p testing
#SBATCH --output=region_12_12_sa_v1_ranks_test.out

mpirun python mpi_region_12_12.py
