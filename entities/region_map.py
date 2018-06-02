from .district import District
from .unit import Unit, Units
from typing import Union, Tuple, Set, List, Iterable
import json


class RegionMap:
    def __init__(self):
        self._districts = tuple()
        self._units_lookup_table = {}
        self._districts_adjacency = [[]]

    def __str__(self):
        return "{ region map:\n " + ";\n ".join(map(str, self._districts)) + "\n}"

    def __repr__(self):
        return self.__str__()

    @property
    def districts(self) -> tuple:
        return self._districts

    @classmethod
    def create_district_for_each_unit(cls, units: Tuple[Unit, ...]) -> "RegionMap":
        region = cls()
        k = len(units)
        region._districts = region._create_k_districts(k)

        for index, district in enumerate(region._districts):
            district.add_unit(units[index])

        return region

    def find_district_by_unit(self, unit: Unit) -> Union[District, None]:
        # should try to search districts if not found in lookup table?
        try:
            return self._units_lookup_table[unit.id]
        except KeyError:
            return None

    def get_neighboring_districts_of(self, district: District) -> Set[District]:
        # print(district)
        units = district.units
        units_ids = {unit.id for unit in units}
        units_of_other_districts = {neighbor.id for unit in units
                                    for neighbor in Units.get_neighbors_of(unit)
                                    if neighbor.id not in units_ids}
        # print(units_of_other_districts)
        return {self._units_lookup_table[unit_id] for unit_id in units_of_other_districts}

    def _create_k_districts(self, k: int) -> tuple:
        return tuple(District.create_with_id_and_callbacks(i, self._add_to_lookup_table, self._remove_from_lookup_table)
                     for i in range(1, k + 1))

    def _add_to_lookup_table(self, unit: Unit, district: District):
        assert unit.id not in self._units_lookup_table
        self._units_lookup_table[unit.id] = district

    def _remove_from_lookup_table(self, unit: Unit):
        assert unit.id in self._units_lookup_table
        del self._units_lookup_table[unit.id]

    @classmethod
    def create_district_for_each_split(cls, splits) -> "RegionMap":
        region = cls()
        k = len(splits)
        region._districts = region._create_k_districts(k)

        for index, district in enumerate(region._districts):
            district.add_units(splits[index].members)

        return region

    def find_district_by_split(self, split):
        units = split.members
        return self.find_district_by_unit(units[0])

    def get_as_json_str(self) -> str:
        return json.dumps([district.get_as_json() for district in self._districts])
