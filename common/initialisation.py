"""Algorithm 2, Generating  feasible contiguous solution from PEAR p.84"""
import numpy as np

from entities import Units, RegionMap, get_units_from_json


def generate_init_solution(k: int) -> RegionMap:
    """Randomly generates an initial solution (district) that contains k districts"""

    seeds = set()
    # gets a tuple of units neighboring unit 0
    units_on_border = Units.get_units_on_region_border()

    while len(seeds) < k:
        unit = np.random.choice(units_on_border, 1)[0]
        if unit not in seeds:
            seeds.add(unit)

    region = RegionMap.create_district_for_each_unit(tuple(seeds))
    pool = seeds
    while pool:
        unit = pool.pop()
        district_of_unit = region.find_district_by_unit(unit)
        neighbors = Units.get_neighbors_of(unit)

        for neighbor in neighbors:
            neighbor_district = region.find_district_by_unit(neighbor)

            if neighbor_district is None and neighbor not in pool:
                pool.add(neighbor)
                district_of_unit.add_unit(neighbor)
    return region


def generate_init_solution_new_seeding(k: int) -> RegionMap:
    seeds = set()
    # gets a tuple of units neighboring unit 0

    units = Units.units()

    while len(seeds) < k:
        unit = np.random.choice(units, 1)[0]
        if unit not in seeds:
            seeds.add(unit)

    region = RegionMap.create_district_for_each_unit(tuple(seeds))
    pool = seeds
    while pool:
        unit = pool.pop()
        district_of_unit = region.find_district_by_unit(unit)
        neighbors = Units.get_neighbors_of(unit)

        for neighbor in neighbors:
            neighbor_district = region.find_district_by_unit(neighbor)

            if neighbor_district is None and neighbor not in pool:
                pool.add(neighbor)
                district_of_unit.add_unit(neighbor)

    return region

if __name__ == "__main__":
    # _units_lst = get_units_from_json("data_3_3.json")
    # Units.initialize(_units_lst)
    # region = generate_init_solution(3)
    # print(region)

    _units_lst = get_units_from_json("../data/region_8_8/region_8_8_data.json")
    Units.initialize(_units_lst)
    region = generate_init_solution_new_seeding(8)
    print(region)
