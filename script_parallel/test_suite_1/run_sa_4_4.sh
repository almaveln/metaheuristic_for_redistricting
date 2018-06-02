#!/bin/bash

#SBATCH -J sa4_p1
#SBATCH -n 60
#SBATCH --cpus-per-task=1
#SBATCH -t 02:00:00
#SBATCH -p testing
#SBATCH --output=region_4_4_sa_v1_ranks_test_1.out

mpirun python mpi_region_4_4.py
