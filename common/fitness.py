"""
Contains the objective function and other functions that are used for measuring
the solution (region, map) quality

Additional info:
0 ≤ republican_deviation (T_p) ≤ 0.5
0 ≤ weighting_factor (T_e) ≤ 0.5

Abbreviations
dist[s] :: district[s]
"""
import json
from typing import Sequence
import entities as ent
from entities import RegionMap

# ALPHA :: defines the weight of the weighting_factor in the competitiveness measure
ALPHA = 1
# BETA :: a normalizing constant so that the value of f spans the range [0, 1]
BETA = 4 / 3
COMPETITIVENESS_WEIGHT = 0.5


def calc_competitiveness(dists: Sequence):
    """Calculates the competitiveness (fitness) score of a region (map)"""

    republican_deviation = calc_republican_deviation(dists)
    weighting_factor = calc_weighting_factor(dists)

    return republican_deviation * (1 + ALPHA * weighting_factor) * BETA


def calc_republican_deviation(dists: Sequence):
    """
    Calculates a deviation of the Republican two-party registration from
    0.50 in each district
    """

    def calc_republican_deviation_in_district(dist):
        return abs((dist.republicans_pct() / (dist.republicans_pct() + dist.democrats_pct())) - 0.5)

    sum_of_deviations = (sum([calc_republican_deviation_in_district(dist) for dist in dists]))
    number_of_districts = len(dists)

    return round(sum_of_deviations / number_of_districts, 5)


def calc_weighting_factor(dists: Sequence):
    """Captures the differential (difference, margin) in the number of seats won by the two parties"""

    number_of_republican_dists = calc_number_of_republican_districts(dists)
    number_of_districts = len(dists)

    return round(abs((number_of_republican_dists / number_of_districts) - 0.5), 5)


def calc_number_of_republican_districts(dists: Sequence):
    """
    Calculates the number of districts where Republican registration is larger
    than the Democratic registration
    """

    return sum(1 for dist in dists if dist.republicans_pct() > dist.democrats_pct())


def calc_solution_quality(sln: RegionMap):
    weight = COMPETITIVENESS_WEIGHT
    return calc_population_deviation(sln.districts) * (1 - weight) + calc_competitiveness(sln.districts) * weight


def get_quality_scores(sln: RegionMap):
    weight = COMPETITIVENESS_WEIGHT
    unfitness_score = calc_population_deviation(sln.districts) * (1 - weight)
    fitness_score = calc_competitiveness(sln.districts) * weight
    return unfitness_score + fitness_score, unfitness_score, fitness_score


def calc_population_deviation(dists: Sequence) -> int:
    """Calculates the population deviation (unfitness) of a region (map)"""

    _districts = sorted(dists, key=lambda dist: dist.population())
    average_pop = round(sum([dist.population() for dist in _districts]) / len(_districts), 5)
    min_pop = _districts[0].population()
    max_pop = _districts[-1].population()
    population_deviation = round((max_pop - min_pop) / average_pop, 5)

    return 1 if population_deviation > 1 else population_deviation


if __name__ == "__main__":
    f = open("../data/hand_picked_3_3_test_case.json")
    json_obj = json.load(f)
    f.close()

    json_units = json_obj["units"]
    units = []
    for json_unit in json_units:
        units.append(ent.Unit(json_unit["id"],
                              json_unit["pop"],
                              json_unit["registration"]["rep"],
                              json_unit["registration"]["dem"],
                              json_unit["neighbors"]))

    # dist_1 = ent.District.create_with_units({units[0], units[1], units[3]})
    # dist_2 = ent.District.create_with_units({units[2], units[4], units[5]})
    # dist_3 = ent.District.create_with_units({units[6], units[7], units[8]})
    dist_1 = ent.District.create_with_units({units[0], units[1], units[3], units[2], units[6]})
    dist_2 = ent.District.create_with_units({units[4]})
    dist_3 = ent.District.create_with_units({units[5], units[7], units[8]})

    districts = [dist_1, dist_2, dist_3]

    print("calc_weighting_factor: {0}".format(calc_weighting_factor(districts)))
    print("dem: {0}".format(dist_1._democrats))
    print("rep: {0}".format(dist_1._republicans))
    print("dem: {0}".format(dist_2._democrats))
    print("rep: {0}".format(dist_2._republicans))
    print("dem: {0}".format(dist_3._democrats))
    print("rep: {0}".format(dist_3._republicans))

    print("calc_n_of_rep_districts: {0}".format(calc_number_of_republican_districts(districts)))
    print("rep_deviation: {0}".format(calc_republican_deviation(districts)))
    print("calc_unfitness_value: {}".format(calc_population_deviation(districts)))
