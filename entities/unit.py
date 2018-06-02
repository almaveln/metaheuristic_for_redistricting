from typing import Union, Tuple, Set, List, Iterable


class Unit:
    def __init__(self, unit_id: int, population: int, rep: float, dem: float, neighbors: list,
                 is_on_region_border: bool = False):
        self._id = unit_id
        self._population = population
        self._rep = rep
        self._dem = dem
        self._neighbors = tuple(neighbors)
        self._is_on_region_border = is_on_region_border

    def __str__(self):
        return "{ unit id: " + str(self._id) + " }"

    # def __repr__(self):
    #     return "{ " + (
    #         "unit id: " + str(self._id) +
    #         "; population: " + str(self._population) +
    #         "; rep: " + str(self._rep) +
    #         "; dem: " + str(self._dem) +
    #         "; ids of neighbors: " + str(self._neighbors) +
    #         "; is_on_region_border: " + str(self._is_on_region_border)
    #     ) + " }"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self._id, self._population, self._rep, self._dem))

    def __eq__(self, other):
        return isinstance(other, Unit) and self._id == other._id

    @property
    def neighbors(self) -> Tuple[int]:
        return self._neighbors

    @property
    def is_on_region_border(self) -> bool:
        return self._is_on_region_border

    @property
    def id(self) -> int:
        return self._id

    @property
    def dem(self) -> float:
        return self._dem

    @property
    def rep(self) -> float:
        return self._rep

    @property
    def population(self) -> int:
        return self._population

    def check_if_neighbor_to(self, other_unit: "Unit") -> bool:
        return self.id in other_unit.neighbors


class Units:
    _units = None  # type: Tuple[Unit]
    _units_on_region_border = None  # type: Tuple[Unit]
    _lookup_neighbors = {}

    @classmethod
    def units(cls) -> Tuple[Unit]:
        return cls._units

    @classmethod
    def get_units_on_region_border(cls) -> Tuple[Unit, ...]:
        return cls._units_on_region_border

    @classmethod
    def get_neighbors_of(cls, unit: Unit) -> Tuple[Unit, ...]:
        _id = unit.id
        if _id not in cls._lookup_neighbors:
            tmp = tuple(neighbor for neighbor in cls._units if neighbor.id in unit.neighbors)
            cls._lookup_neighbors[_id] = tmp
        return cls._lookup_neighbors[_id]

    @classmethod
    def initialize(cls, units: List[Unit]) -> None:
        if cls._units is None:
            cls._units = tuple(units)
            cls._units_on_region_border = tuple(unit for unit in cls._units if unit.is_on_region_border)
