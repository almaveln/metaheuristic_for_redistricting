

from mpi4py import MPI
from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import visualisation
import plotting
import time

start = time.time()
TEST_ID_NUMBER = 80
SA_VERSION = "v1"
REGION_ID = "region_24_24"

REGION_DATA_FILE_PATH_24_24 = "./data/region_24_24/region_24_24_data.json"
MAX_ITERATIONS = 250
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 16

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None

if rank == 0:
    data = [None for i in range(size)]

OUTPUT_FILE_24_24 = ("./experiments_output/region_24_24/output_{0}_sa_{1}_run_{2}_rank{3}.csv"
                     .format(REGION_ID, SA_VERSION, TEST_ID_NUMBER, rank))
sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_24_24, OUTPUT_FILE_24_24, MAX_ITERATIONS, MAX_TEMP,
                            NUMBER_OF_DISTRICTS)

best_state, best_energy = sa.run_instance(rank)
data = comm.gather((rank, best_energy), root=0)

if rank == 0:
    end = time.time()
    data.sort(key=lambda x: x[1], reverse=False)
    print(data)
    running_time = end - start
    print("TEST_ID_NUMBER {0}; REGION_ID {1}".format(TEST_ID_NUMBER, REGION_ID))
    print("start time {0} seconds; end time {1} seconds; running time {2} seconds".format(start, end, running_time))
