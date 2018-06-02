

from mpi4py import MPI
from os import path
import sys
import importlib

sys.path.append(path.abspath('.'))

import simulated_annealing
import visualisation
import plotting

# TEST_ID_NUMBER = 5
# SA_VERSION = "v1"
# REGION_ID = "region_6_6"

# REGION_DATA_FILE_PATH_6_6 = "./data/region_6_6/region_6_6_data_ts2.json"
# MAX_ITERATIONS = 1000
# MAX_TEMP = 10000
# NUMBER_OF_DISTRICTS = 4

# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()

# data = None

# if rank == 0:
#     data = [None for i in range(size)]

# OUTPUT_FILE_6_6 = ("./experiments_output/region_6_6/output_{0}_sa_{1}_run_{2}_rank{3}.csv"
#                    .format(REGION_ID, SA_VERSION, TEST_ID_NUMBER, rank))
# sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_6_6, OUTPUT_FILE_6_6, MAX_ITERATIONS, MAX_TEMP,
#                             NUMBER_OF_DISTRICTS)

# best_state, best_energy = sa.run_instance(rank)
# data = comm.gather((rank, best_energy), root=0)

# if rank == 0:
#     data.sort(key=lambda x: x[1], reverse=False)
#     print(data)
    
# from mpi4py import MPI
# import random
# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()

# # Kõigil protsessidel väljaarvatud järjekorranumbriga 0 andmed puuduvad.
# data = None
# # Loome protsessil järjekorranumbriga 0 massiivi, mis on pikkusega size (ehk protsesside arv)
# if rank == 0:
#         algAndmed = [None for i in range(size)]
#         print("algsed andmed", algAndmed)
# # data = comm.scatter(data, root=0)
# data = comm.gather((random.random(), rank), root=0)

# if rank == 0:
#     data.sort(key=lambda x: x[0], reverse=True)
#     print("lõplikud andmed", data)
import time

start = time.time()
TEST_ID_NUMBER = 90
SA_VERSION = "v1"
REGION_ID = "region_18_18"

REGION_DATA_FILE_PATH_18_18 = "./data/region_18_18/region_18_18_data.json"
MAX_ITERATIONS = 250
MAX_TEMP = 10000
NUMBER_OF_DISTRICTS = 9

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None

if rank == 0:
    data = [None for i in range(size)]

OUTPUT_FILE_18_18 = ("./experiments_output/region_18_18/output_{0}_sa_{1}_run_{2}_rank{3}.csv"
                     .format(REGION_ID, SA_VERSION, TEST_ID_NUMBER, rank))
sa = simulated_annealing.SA(REGION_DATA_FILE_PATH_18_18, OUTPUT_FILE_18_18, MAX_ITERATIONS, MAX_TEMP,
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
