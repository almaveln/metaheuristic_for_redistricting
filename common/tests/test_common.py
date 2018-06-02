import unittest
from entities import Unit, Units, RegionMap, District
from common import check_if_contiguous, check_if_has_holes


# managed to solve the problem with imports by adding __init__

class CommonTestCase(unittest.TestCase):
    def setUp(self):
        self.unit_1 = Unit(1, 100, 0.5, 0.5, [2, 4], True)
        self.unit_2 = Unit(2, 120, 0.6, 0.4, [1, 3, 5], True)
        self.unit_3 = Unit(3, 140, 0.35, 0.65, [2, 6], True)
        self.unit_4 = Unit(4, 90, 0.55, 0.45, [1, 5, 7], True)
        self.unit_5 = Unit(5, 50, 0.4, 0.6, [2, 4, 6, 8], False)
        self.unit_6 = Unit(6, 50, 0.4, 0.6, [3, 5, 9], True)
        self.unit_7 = Unit(7, 50, 0.4, 0.6, [4, 8], True)
        self.unit_8 = Unit(8, 50, 0.4, 0.6, [5, 7, 9], True)
        self.unit_9 = Unit(9, 50, 0.4, 0.6, [6, 8], True)
        self.units = [self.unit_1,
                      self.unit_2,
                      self.unit_3,
                      self.unit_4,
                      self.unit_5,
                      self.unit_6,
                      self.unit_7,
                      self.unit_8,
                      self.unit_9]

        Units.initialize(self.units)

    def test_check_if_contiguous_False(self):
        district = District.create_with_units({self.unit_4, self.unit_6})
        expected = False
        actual = check_if_contiguous(district)
        self.assertEqual(expected, actual)

    def test_check_if_contiguous_True(self):
        district = District.create_with_units({self.unit_1, self.unit_4, self.unit_5, self.unit_6})
        expected = True
        actual = check_if_contiguous(district)
        self.assertEqual(expected, actual)

    def test_check_if_has_holes_True(self):
        initial_units = (self.unit_1, self.unit_5)
        region = RegionMap.create_district_for_each_unit(initial_units)
        district_1 = region.find_district_by_unit(self.unit_1)
        district_1.add_units([self.unit_2, self.unit_3, self.unit_4, self.unit_6, self.unit_7,
                              self.unit_8, self.unit_9])
        expected = True
        actual = check_if_has_holes(region)
        self.assertEqual(expected, actual)

    def test_check_if_has_holes_False(self):
        initial_units = (self.unit_1, self.unit_5)
        region = RegionMap.create_district_for_each_unit(initial_units)
        district_1 = region.find_district_by_unit(self.unit_1)
        district_1.add_units([self.unit_3, self.unit_4, self.unit_6, self.unit_7,
                              self.unit_8, self.unit_9])
        district_2 = region.find_district_by_unit(self.unit_5)
        district_2.add_unit(self.unit_2)

        expected = False
        actual = check_if_has_holes(region)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
