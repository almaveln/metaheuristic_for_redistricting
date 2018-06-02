#!/bin/bash

#SBATCH -p testing
#SBATCH -J sa_v1_region_24_24
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=region_24_24_sa_v1.out
#SBATCH -t 00:10:00

echo "Started sa_v1_region_24_24"
python ./scripts/region_24_24/main_region_24_24_v1.py
