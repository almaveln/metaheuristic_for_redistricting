#!/bin/bash

#SBATCH -p testing
#SBATCH -J sa_v1_region_3_3
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=region_3_3_sa_v1.out
#SBATCH -t 02:00:00

python ./scripts/region_3_3/main_region_3_3_v1.py
