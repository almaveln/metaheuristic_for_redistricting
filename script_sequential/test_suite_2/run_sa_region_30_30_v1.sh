#!/bin/bash

#SBATCH -p testing
#SBATCH -J sa_v1_region_30_30
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=region_30_30_sa_v1.out
#SBATCH -t 00:10:00

echo "Started sa_v1_region_30_30"
python ./scripts/region_30_30/main_region_30_30_v1.py

