#!/bin/bash

#SBATCH -J sa8_s1
#SBATCH -n 1
#SBATCH --cpus-per-task=1
#SBATCH -t 02:00:00
#SBATCH -p testing
#SBATCH --output=region_8_8_sa_v1_test_id10.out

python seq_region_8_8.py
