from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import visualisation
import plotting

TEST_ID_NUMBER = 1
SA_VERSION = "v1"
REGION_ID = "region_24_24"

REGION_DATA_FILE_PATH_24_24 = "./data/region_24_24/region_24_24_data.json"
MAX_ITERATIONS = 5000
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 16


OUTPUT_FILE_24_24 = ("./experiments_output/region_24_24/output_{0}_sa_{1}_id{2}.csv"
                     .format(REGION_ID, SA_VERSION, TEST_ID_NUMBER))
sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_24_24, OUTPUT_FILE_24_24, MAX_ITERATIONS, MAX_TEMP,
                            NUMBER_OF_DISTRICTS)
sa.run()
