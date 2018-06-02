import unittest
from copy import deepcopy
from entities import Unit, Units


class UnitTestCase(unittest.TestCase):
    def setUp(self):
        self.unit_1 = Unit(1, 100, 0.5, 0.5, [2, 3, 4, 5], True)
        self.unit_2 = Unit(2, 120, 0.6, 0.4, [1], True)
        self.unit_3 = Unit(3, 140, 0.35, 0.65, [1, 4, 5], False)
        self.unit_4 = Unit(4, 90, 0.55, 0.45, [1, 3, 5], True)
        self.unit_5 = Unit(5, 50, 0.4, 0.6, [1, 3, 4], True)
        self.units = [self.unit_1, self.unit_2, self.unit_3, self.unit_4, self.unit_5]
        self.units_on_border = [self.unit_1, self.unit_2, self.unit_4, self.unit_5]
        Units.initialize(self.units)

    def test_check_if_neighbor_to(self):
        self.assertTrue(self.unit_3.check_if_neighbor_to(self.unit_5))
        self.assertFalse(self.unit_2.check_if_neighbor_to(self.unit_3))


class UnitsTestCase(unittest.TestCase):
    def setUp(self):
        self.unit_1 = Unit(1, 100, 0.5, 0.5, [2, 3, 4, 5], True)
        self.unit_2 = Unit(2, 120, 0.6, 0.4, [1], True)
        self.unit_3 = Unit(3, 140, 0.35, 0.65, [1, 4, 5], False)
        self.unit_4 = Unit(4, 90, 0.55, 0.45, [1, 3, 5], True)
        self.unit_5 = Unit(5, 50, 0.4, 0.6, [1, 3, 4], True)
        self.units = [self.unit_1, self.unit_2, self.unit_3, self.unit_4, self.unit_5]
        self.units_on_border = [self.unit_1, self.unit_2, self.unit_4, self.unit_5]
        Units.initialize(self.units)

    def test_initialize(self):
        actual_units = Units.units()
        self.assertCountEqual(self.units, actual_units)

    def test_get_units_on_border(self):
        actual_units_on_border = Units.get_units_on_region_border()
        self.assertCountEqual(self.units_on_border, actual_units_on_border)

    def test_get_neighbors_of(self):
        actual_neighbors = Units.get_neighbors_of(self.unit_5)
        expected_neighbors = [self.unit_1, self.unit_3, self.unit_4]
        self.assertCountEqual(expected_neighbors, actual_neighbors)


if __name__ == '__main__':
    unittest.main()
