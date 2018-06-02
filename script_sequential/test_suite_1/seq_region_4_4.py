from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import time

start = time.time()
TEST_ID_NUMBER = 10
SA_VERSION = "v1"
REGION_ID = "region_4_4"
OUTPUT_REGION_FOLDER = "region_4_4" + "_seq"

REGION_DATA_FILE_PATH = "./data/{0}/{0}_data.json".format(REGION_ID)
MAX_ITERATIONS = 5000
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 4

OUTPUT_FILE = ("./experiments_output/{0}/output_{1}_sa_{2}_run_{3}_{4}.csv"
               .format(OUTPUT_REGION_FOLDER, REGION_ID, SA_VERSION, TEST_ID_NUMBER, "seq"))
sa = simulated_annealing.SA(REGION_DATA_FILE_PATH, OUTPUT_FILE, MAX_ITERATIONS, MAX_TEMP,
                            NUMBER_OF_DISTRICTS)

best_state, best_energy = sa.run()

end = time.time()
running_time = end - start
print("TEST_ID_NUMBER {0}; REGION_ID {1}".format(TEST_ID_NUMBER, REGION_ID))
print("start time {0} seconds; end time {1} seconds; running time {2} seconds".format(start, end, running_time))
