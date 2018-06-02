from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import visualisation
import plotting

TEST_ID_NUMBER = 1
SA_VERSION = "v1"
REGION_ID = "region_18_18"

REGION_DATA_FILE_PATH_18_18 = "./data/region_18_18/region_18_18_data.json"
MAX_ITERATIONS = 5000
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 9

OUTPUT_FILE_18_18 = ("./experiments_output/region_18_18/output_{0}_sa_{1}_id{2}.csv"
                     .format(REGION_ID, SA_VERSION, TEST_ID_NUMBER))
sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_18_18, OUTPUT_FILE_18_18, MAX_ITERATIONS, MAX_TEMP,
                            NUMBER_OF_DISTRICTS)
sa.run()
