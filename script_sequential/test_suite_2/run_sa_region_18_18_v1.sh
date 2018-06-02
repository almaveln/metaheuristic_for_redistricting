#!/bin/bash

#SBATCH -p testing
#SBATCH -J sa_v1_region_18_18
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=region_18_18_sa_v1.out
#SBATCH -t 00:10:00

echo "Started sa_v1_region_18_18"
python ./scripts/region_18_18/main_region_18_18_v1.py
