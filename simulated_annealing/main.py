"""
calc_solution_quality :: plays the role of energy
"""

import math
import random as rd
import copy
from common import check_if_contiguous, check_if_has_holes
from common.fitness import calc_solution_quality, get_quality_scores
from common.initialisation import generate_init_solution, generate_init_solution_new_seeding
from entities import Units, RegionMap, get_units_from_json
from utils import write_to_csv_file, create_csv_file, get_current_time, CumulativeTime

DATA_FILE = "../data/old/data_3_3_rook_picked.json"
OUTPUT_FILE = "../output_sa/output_test_{0}_picked.csv".format(get_current_time())
IMG_OUTPUT_TEMPLATE = "../visualisation_output_sa/simple_case_3_3_{0}.png"
MAX_ITERATIONS = 5000
MAX_TEMP = 25000
NUMBER_OF_DISTRICTS = 3


class SA:
    def __init__(self, input_file_name, output_file_name, max_iterations, max_temp,
                 number_of_districts):
        global DATA_FILE, OUTPUT_FILE, MAX_TEMP, MAX_ITERATIONS, NUMBER_OF_DISTRICTS
        # DATA_FILE = "../data/{0}.json".format(input_file_name)
        DATA_FILE = input_file_name
        # OUTPUT_FILE = "../output_sa/{0}.csv".format(output_file_name)
        OUTPUT_FILE = output_file_name
        MAX_TEMP = max_temp
        MAX_ITERATIONS = max_iterations
        NUMBER_OF_DISTRICTS = number_of_districts

    def run(self):
        _initialize()
        print("SA parameters: MAX_ITERATIONS {0}; MAX_TEMP {1}; NUMBER_OF_DISTRICTS {2}"
              .format(MAX_ITERATIONS, MAX_TEMP, NUMBER_OF_DISTRICTS))
        print("SA started")
        best_state, best_energy = run_sa()
        print("SA completed")
        return best_state, best_energy

    def run_in_parallel_1(self, iterations=1, population_size=1):
        pass

    def run_instance(self, index):
        _initialize()
        print("SA parameters: MAX_ITERATIONS {0}; MAX_TEMP {1}; NUMBER_OF_DISTRICTS {2}; index {3}"
              .format(MAX_ITERATIONS, MAX_TEMP, NUMBER_OF_DISTRICTS, index))
        print("SA started, index {0}".format(index))
        best_state, best_energy = run_sa()
        print("SA completed; index {0}; best_energy: {1}; best_state: {2}".format(index, best_energy, best_state))
        return best_state, best_energy


class Snapshot:
    csv_head = ["iteration", "cumtime", "best_quality", "cur_unfitness_value", "cur_fitness_value",
                "current_energy", "current_temp", "elite_solution_structure"]

    def __init__(self):
        self.iteration = 0

    def take_sln_snapshot(self, sln: RegionMap, unfitness_score: float, fitness_score: float, sln_quality: float,
                          current_energy: float, current_temp: float):
        solution_json = sln.get_as_json_str()

        csv_row = [self.iteration,
                   CumulativeTime.get_cumtime(),
                   sln_quality,
                   unfitness_score,
                   fitness_score,
                   current_energy,
                   current_temp,
                   solution_json]
        write_to_csv_file(OUTPUT_FILE, csv_row)
        self.iteration += 1

    def initialise(self):
        create_csv_file(OUTPUT_FILE, self.csv_head)
        CumulativeTime.initialize()


def _initialize():
    """Initializes the units data (geographic) needed to run thr algorithm"""

    _units_lst = get_units_from_json(DATA_FILE)
    Units.initialize(_units_lst)


# modify the algorithm
def run_sa():
    snapshot = Snapshot()
    snapshot.initialise()
    cur_state = generate_initial_solution()
    best_state = copy.deepcopy(cur_state)
    prev_energy, unfitness_score, fitness_score = get_quality_scores(cur_state)
    best_energy = prev_energy

    snapshot.take_sln_snapshot(best_state, unfitness_score, fitness_score, best_energy, best_energy, MAX_TEMP)
    for i in range(1, MAX_ITERATIONS + 1):
        new_state = create_neighboring_sln(cur_state)
        E, unfitness_score, fitness_score = get_quality_scores(new_state)
        cur_temp = decrease_temperature(i)

        if cur_temp == 0:
            return best_state, best_energy

        dE = E - prev_energy
        if dE < 0:
            cur_state = new_state
            prev_energy = E
            if E < best_energy:
                best_state = copy.deepcopy(new_state)
                best_energy = E
        elif math.exp(-dE / cur_temp) > rd.random():
            cur_state = new_state
            prev_energy = E

        snapshot.take_sln_snapshot(best_state, unfitness_score, fitness_score, best_energy, E, cur_temp)

    return best_state, best_energy


def generate_initial_solution():
    sln = generate_init_solution(NUMBER_OF_DISTRICTS)
    return sln


# do not make a move if not needed? Might get stuck in a local minimum?
def create_neighboring_sln(cur_sln: RegionMap):
    """Generates a neighboring solution using the Ising models approach"""

    # if unit borders several districts, choose one of these districts randomly
    # decide randomly if unit should "go" to another district
    all_units = Units.units()
    for cur_unit in all_units:
        cur_district = cur_sln.find_district_by_unit(cur_unit)

        # if cur_unit is the only unit in the district, do not change cur_unit "membership"
        # (in favor of another district)
        if len(cur_district) <= 1:
            continue

        neighboring_districts_collection = cur_sln.get_neighboring_districts_of(cur_district)

        # find those districts that cur_unit borders
        districts_that_cur_unit_borders = []
        for neighboring_district in neighboring_districts_collection:
            bordering_units = cur_district.get_units_bordering_that_district(neighboring_district)

            if cur_unit in bordering_units:
                districts_that_cur_unit_borders.append(neighboring_district)

        if len(districts_that_cur_unit_borders) == 0:
            continue

        random_district = rd.choice(districts_that_cur_unit_borders)

        cur_district.remove_unit(cur_unit)
        random_district.add_unit(cur_unit)

        # revert the move if it breaks contiguity or if the move creates holes
        if not check_if_contiguous(cur_district) or check_if_has_holes(cur_sln):
            random_district.remove_unit(cur_unit)
            cur_district.add_unit(cur_unit)

    return cur_sln


def decrease_temperature(i):
    return MAX_TEMP * (0.9967 ** i)


def _test_gen_neighbor():
    cur_sln = generate_initial_solution()
    print(cur_sln)
    return create_neighboring_sln(cur_sln)


if __name__ == "__main__":
    # create_csv_file()
    # create_csv_file(OUTPUT_FILE)
    _initialize()
    best_sln = run_sa()
    # best_sln = _test_gen_neighbor()
    print("fitness")
    print(best_sln)
    print(calc_solution_quality(best_sln))
    # run_visualiser(OUTPUT_FILE, DATA_FILE, IMG_OUTPUT_TEMPLATE)
