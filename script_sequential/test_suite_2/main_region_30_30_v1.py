from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import visualisation
import plotting

TEST_ID_NUMBER = 1
# OPTIMAL_SLN_FILE_PATH_30_30 = "../data/region_30_30/region_30_30_opt_sln.json"
IMG_OUTPUT_TEMPLATE_30_30 = ("./visualisation_output_sa/region_30_30/out_img_region_30_30_sa_v1_id{0}_iter{1}.svg"
                             .format(TEST_ID_NUMBER, "{0}"))
POLITICAL_LANDSCAPE_IMG_30_30 = "./visualisation_output_sa/region_30_30/political_landscape_region_30_30.svg"
PLOT_FILE_30_30 = "./plotting_output/region_30_30/plot_region_30_30_sa_v1_id{0}.png".format(TEST_ID_NUMBER)
# PLOT_FILE_30_30 = "./plotting_output/region_30_30/region_30_30_plot_{0}.png".format(ID_NUMBER)


REGION_DATA_FILE_PATH_30_30 = "./data/region_30_30/region_30_30_data.json"
OUTPUT_FILE_30_30 = "./experiments_output/region_30_30/output_region_30_30_sa_v1_id{0}.csv".format(TEST_ID_NUMBER)
MAX_ITERATIONS = 5000
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 25

sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_30_30, OUTPUT_FILE_30_30, MAX_ITERATIONS, MAX_TEMP,
                            NUMBER_OF_DISTRICTS)
sa.run()
