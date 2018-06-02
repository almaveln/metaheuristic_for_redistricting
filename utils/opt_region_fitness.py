import json
from entities import Unit, District, RegionMap
from common import fitness


def show_fitness_score(sln_file_path, data_file):
    with open(sln_file_path) as f:
        result = json.load(f)["result"]
    with open(data_file) as f:
        units = json.load(f)["units"]

    units_lst = []
    for json_unit in units:
        units_lst.append(Unit(json_unit["id"],
                              json_unit["pop"],
                              json_unit["registration"]["rep"],
                              json_unit["registration"]["dem"],
                              json_unit["neighbors"],
                              json_unit["is_on_region_border"]))

    units_lst.sort(key=lambda x: x.id)
    districts = [District.create_with_units({units_lst[unit_id - 1] for unit_id in dst["units_ids"]})
                 for dst in result]

    region = RegionMap()
    region._districts = tuple(districts)
    print("solution quality: {0}".format(fitness.calc_solution_quality(region)))


if __name__ == "__main__":
    OPTIMAL_SLN_FILE_PATH_3_3 = "../data/region_3_3/region_3_3_opt_sln.json"
    REGION_DATA_FILE_PATH_3_3 = "../data/region_3_3/region_3_3_data.json"
    print("3x3")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_3_3, REGION_DATA_FILE_PATH_3_3)

    OPTIMAL_SLN_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_opt_sln_ts2.json"
    REGION_DATA_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_data_ts2.json"
    print("6x6")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_6_6, REGION_DATA_FILE_PATH_6_6)

    OPTIMAL_SLN_FILE_PATH_18_18 = "../data/region_18_18/region_18_18_opt_sln.json"
    REGION_DATA_FILE_PATH_18_18 = "../data/region_18_18/region_18_18_data.json"
    print("18x18")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_18_18, REGION_DATA_FILE_PATH_18_18)

    OPTIMAL_SLN_FILE_PATH_24_24 = "../data/region_24_24/region_24_24_opt_sln.json"
    REGION_DATA_FILE_PATH_24_24 = "../data/region_24_24/region_24_24_data.json"
    print("24x24")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_24_24, REGION_DATA_FILE_PATH_24_24)

    OPTIMAL_SLN_FILE_PATH_30_30 = "../data/region_30_30/region_30_30_opt_sln.json"
    REGION_DATA_FILE_PATH_30_30 = "../data/region_30_30/region_30_30_data.json"
    print("30x30")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_30_30, REGION_DATA_FILE_PATH_30_30)

    # new test cases
    OPTIMAL_SLN_FILE_PATH_4_4 = "../data/region_4_4/region_4_4_opt_sln.json"
    REGION_DATA_FILE_PATH_4_4 = "../data/region_4_4/region_4_4_data.json"
    print("4x4")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_4_4, REGION_DATA_FILE_PATH_4_4)

    OPTIMAL_SLN_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_opt_sln.json"
    REGION_DATA_FILE_PATH_6_6 = "../data/region_6_6/region_6_6_data.json"
    print("6x6")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_6_6, REGION_DATA_FILE_PATH_6_6)

    OPTIMAL_SLN_FILE_PATH_8_8 = "../data/region_8_8/region_8_8_opt_sln.json"
    REGION_DATA_FILE_PATH_8_8 = "../data/region_8_8/region_8_8_data.json"
    print("8x8")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_8_8, REGION_DATA_FILE_PATH_8_8)

    OPTIMAL_SLN_FILE_PATH_10_10 = "../data/region_10_10/region_10_10_opt_sln.json"
    REGION_DATA_FILE_PATH_10_10 = "../data/region_10_10/region_10_10_data.json"
    print("10x10")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_10_10, REGION_DATA_FILE_PATH_10_10)

    OPTIMAL_SLN_FILE_PATH_12_12 = "../data/region_12_12/region_12_12_opt_sln.json"
    REGION_DATA_FILE_PATH_12_12 = "../data/region_12_12/region_12_12_data.json"
    print("12x12")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_12_12, REGION_DATA_FILE_PATH_12_12)

    OPTIMAL_SLN_FILE_PATH_14_14 = "../data/region_14_14/region_14_14_opt_sln.json"
    REGION_DATA_FILE_PATH_14_14 = "../data/region_14_14/region_14_14_data.json"
    print("14x14")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_14_14, REGION_DATA_FILE_PATH_14_14)

    OPTIMAL_SLN_FILE_PATH_16_16 = "../data/region_16_16/region_16_16_opt_sln.json"
    REGION_DATA_FILE_PATH_16_16 = "../data/region_16_16/region_16_16_data.json"
    print("16x16")
    show_fitness_score(OPTIMAL_SLN_FILE_PATH_16_16, REGION_DATA_FILE_PATH_16_16)