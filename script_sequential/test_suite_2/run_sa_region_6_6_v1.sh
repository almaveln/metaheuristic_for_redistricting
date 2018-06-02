#!/bin/bash

#SBATCH -p testing
#SBATCH -J sa_v1_region_6_6
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=region_6_6_sa_v1.out
#SBATCH -t 02:00:00

python ./scripts/region_6_6/main_region_6_6_v1.py
