from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import visualisation
import plotting

TEST_ID_NUMBER = 1
SA_VERSION = "v1"
REGION_ID = "region_3_3"

REGION_DATA_FILE_PATH_3_3 = "./data/region_3_3/region_3_3_data.json"
IMG_OUTPUT_TEMPLATE_3_3 = "./visualisation_output_sa/region_3_3/out_img_region_3_3_sa_v1_id{0}_iter{1}.svg".format(
    TEST_ID_NUMBER, "{0}")
POLITICAL_LANDSCAPE_IMG_3_3 = "./visualisation_output_sa/region_3_3/political_landscape_region_30_30.svg"
PLOT_FILE_3_3 = "./plotting_output/region_3_3/plot_region_3_3_sa_v1_id{0}.png".format(TEST_ID_NUMBER)

MAX_ITERATIONS = 5000
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 3

for i in range(3):
    OUTPUT_FILE_3_3 = ("./experiments_output/region_3_3/output_{0}_sa_{1}_id{2}.csv"
                       .format(REGION_ID, SA_VERSION, TEST_ID_NUMBER))
    sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_3_3, OUTPUT_FILE_3_3, MAX_ITERATIONS, MAX_TEMP,
                                NUMBER_OF_DISTRICTS)
    sa.run()
    TEST_ID_NUMBER += 1
