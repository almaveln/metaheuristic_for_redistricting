from .unit import Units, Unit
from .district import District
from .region_map import RegionMap
import json


def get_units_from_json(file_name):
    with open(file_name) as f:
        json_obj = json.load(f)
    json_list_of_units = json_obj["units"]

    units_lst = []
    for json_unit in json_list_of_units:
        units_lst.append(Unit(json_unit["id"],
                              json_unit["pop"],
                              json_unit["registration"]["rep"],
                              json_unit["registration"]["dem"],
                              json_unit["neighbors"],
                              json_unit["is_on_region_border"]))

    return units_lst


if __name__ == "__main__":
    _units_lst = get_units_from_json("../data_3_3.json")
    Units.initialize(_units_lst)
    print(len(Units.get_units_on_region_border()))
    pass
