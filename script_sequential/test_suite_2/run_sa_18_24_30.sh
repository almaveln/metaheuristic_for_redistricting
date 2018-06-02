#!/bin/bash

#SBATCH -p main
#SBATCH -J sa_v1_main
#SBATCH -N 3
#SBATCH --output=sa_v1_main.out
#SBATCH -t 2-00:00:00

# python ./scripts_test_suite_2/region_18_18/main_region_18_18_v1.py
# python ./scripts_test_suite_2/region_24_24/main_region_24_24_v1.py
# python ./scripts_test_suite_2/region_30_30/main_region_30_30_v1.py

# ./scripts_test_suite_2/region_18_18/run_sa_region_18_18_v1.sh
# ./scripts_test_suite_2/region_24_24/run_sa_region_24_24_v1.sh
# ./scripts_test_suite_2/region_30_30/run_sa_region_30_30_v1.sh
# Sequential Simulated Annealing; region 18x18, region 24x24, region 30x30

echo "START"
# sleep 5
# hostname
# hostname
srun -N 1 ./scripts_test_suite_2/region_18_18/run_sa_region_18_18_v1.sh &
srun -N 1 ./scripts_test_suite_2/region_24_24/run_sa_region_24_24_v1.sh &
srun -N 1 ./scripts_test_suite_2/region_30_30/run_sa_region_30_30_v1.sh &
wait
