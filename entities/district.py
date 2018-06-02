from typing import Union, Tuple, Set, List, Iterable, Callable
from .unit import Unit, Units


class District:
    def __init__(self):
        self._id = None
        self._units = set()
        self._democrats = None
        self._republicans = None
        # callbacks to RegionMap
        self._add_to_lookup_table = None
        self._remove_from_lookup_table = None

    def __str__(self):
        return "{ district id " + str(self._id) + ": " + ", ".join(map(str, self._units)) + " }"

    def __repr__(self):
        return "\n{ district id " + str(self._id) + ":\n " + ",\n ".join(map(str, self._units)) + "\n}"

    # def __repr__(self):
    #     return "{ " + (
    #         "unit id: " + str(self._id) +
    #         "; units: " + str(self._units) +
    #         "; rep: " + str(self._republicans) +
    #         "; dem: " + str(self._democrats)
    #     ) + " }"

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return isinstance(other, District) and self._id == other._id

    def __len__(self):
        return len(self._units)

    def __contains__(self, unit: Unit):
        return unit in self.units

    @property
    def units(self) -> set:
        return self._units

    @property
    def id(self) -> int:
        return self._id

    @classmethod
    def create_with_units(cls, units: set) -> "District":
        district = cls()
        district._units = units
        return district

    @classmethod
    def create_with_id_and_callbacks(cls, dist_id: int, add: Callable[[Unit, "District"], None],
                                     remove: Callable[[Unit], None]) -> "District":
        district_inst = cls()
        district_inst._id = dist_id
        district_inst._add_to_lookup_table = add
        district_inst._remove_from_lookup_table = remove
        return district_inst

    def population(self):
        if len(self._units) > 0:
            self._recalculate_population()
            return self._population
        else:
            raise Exception("District does not contain any units")

    def republicans_pct(self):
        if len(self._units) > 0:
            self._recalculate_population()
            self._republicans = sum([int(unit.population * unit.rep) for unit in self._units])
            return round(self._republicans / self._population, 5)
        else:
            raise Exception("District does not contain any units")

    def democrats_pct(self):
        if len(self._units) > 0:
            self._recalculate_population()
            self._democrats = sum([int(unit.population * unit.dem) for unit in self._units])
            return round(self._democrats / self._population, 5)
        else:
            raise Exception("District does not contain any units")

    def get_units_bordering_that_district(self, that_district: "District") -> Tuple[Unit, ...]:
        """Returns those units of this district that border units of that_district"""

        that_district_units = that_district.units
        return tuple({this_district_unit for this_district_unit in self._units
                      for that_district_unit in that_district_units
                      if this_district_unit.id in that_district_unit.neighbors})

    # todo assert that unit is in district?
    def get_district_neighbors_of(self, this_unit: Unit) -> Tuple[Unit, ...]:
        """Gets neighbors of this_unit that belong to this district"""
        return tuple(self._units & set(Units.get_neighbors_of(this_unit)))

    def add_unit(self, unit: Unit) -> None:
        self._units.add(unit)
        self._add_to_lookup_table(unit, self)

    def remove_unit(self, unit: Unit) -> None:
        self._units.remove(unit)
        self._remove_from_lookup_table(unit)

    def add_units(self, units: Iterable[Unit]) -> None:
        for unit in units:
            self.add_unit(unit)

    def remove_units(self, units: Iterable[Unit]) -> None:
        for unit in units:
            self.remove_unit(unit)

    def get_district_units_on_region_border(self) -> List[Unit]:
        return [unit for unit in self.units if unit.is_on_region_border]

    def _get_other_districts_units_that_border_this_district_units(self):
        raise NotImplementedError

    def _recalculate_population(self):
        self._population = sum(unit.population for unit in self._units)

    def get_as_json(self) -> dict:
        return {'district_id': self.id, 'units_ids': [unit.id for unit in self.units]}
