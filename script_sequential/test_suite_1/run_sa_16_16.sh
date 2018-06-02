#!/bin/bash

#SBATCH -J sa16_s1
#SBATCH -n 1
#SBATCH --cpus-per-task=1
#SBATCH --mem=10000
#SBATCH -t 2-00:00:00
#SBATCH -p main
#SBATCH --output=region_16_16_sa_v1_test_id20.out

python seq_region_16_16.py
