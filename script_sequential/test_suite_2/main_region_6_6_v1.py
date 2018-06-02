from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import visualisation
import plotting

TEST_ID_NUMBER = 1
SA_VERSION = "v1"
REGION_ID = "region_6_6"

REGION_DATA_FILE_PATH_6_6 = "./data/region_6_6/region_6_6_data_ts2.json"
MAX_ITERATIONS = 5000
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 4

for i in range(3):
    OUTPUT_FILE_6_6 = ("./experiments_output/region_6_6/output_{0}_sa_{1}_id{2}.csv"
                       .format(REGION_ID, SA_VERSION, TEST_ID_NUMBER))
    sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_6_6, OUTPUT_FILE_6_6, MAX_ITERATIONS, MAX_TEMP,
                                NUMBER_OF_DISTRICTS)
    sa.run()
    TEST_ID_NUMBER += 1
