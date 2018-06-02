import unittest
from copy import deepcopy
from entities import Unit, Units, District


class DistrictTestCase(unittest.TestCase):
    def setUp(self):
        self.unit_1 = Unit(1, 100, 0.5, 0.5, [2, 3, 4, 5], True)
        self.unit_2 = Unit(2, 120, 0.6, 0.4, [1], True)
        self.unit_3 = Unit(3, 140, 0.35, 0.65, [1, 4, 5], False)
        self.unit_4 = Unit(4, 90, 0.55, 0.45, [1, 3, 5], True)
        self.unit_5 = Unit(5, 50, 0.4, 0.6, [1, 3, 4], True)
        self.units = [self.unit_1, self.unit_2, self.unit_3, self.unit_4, self.unit_5]
        self.units_on_border = [self.unit_1, self.unit_2, self.unit_4, self.unit_5]
        Units.initialize(self.units)

        district_units_1 = {self.unit_1, self.unit_2, self.unit_3}
        district_units_2 = {self.unit_4, self.unit_5}
        self.district_1 = District.create_with_units(district_units_1)
        self.district_2 = District.create_with_units(district_units_2)

    def test_get_neighbors_of(self):
        actual_neighbors = self.district_1.get_district_neighbors_of(self.unit_1)
        expected_neighbors = [self.unit_2, self.unit_3]
        self.assertCountEqual(expected_neighbors, actual_neighbors)

    def test_get_units_bordering_that_district(self):
        actual = self.district_1.get_units_bordering_that_district(self.district_2)
        expected = [self.unit_1, self.unit_3]
        self.assertCountEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
