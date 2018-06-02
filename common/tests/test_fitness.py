import unittest

from common import fitness as ft
from entities import Unit, District, Units


class FitnessTestCase(unittest.TestCase):
    def setUp(self):
        unit_1 = Unit(1, 100, 0.5, 0.5, [])
        unit_2 = Unit(2, 120, 0.6, 0.4, [])
        unit_3 = Unit(3, 140, 0.35, 0.65, [])
        unit_4 = Unit(4, 90, 0.55, 0.45, [])
        unit_5 = Unit(5, 50, 0.4, 0.6, [])

        self.dist_1 = District.create_with_units({unit_1, unit_3})
        self.dist_2 = District.create_with_units({unit_2, unit_4, unit_5})
        self.districts = [self.dist_1, self.dist_2]

    def test_rep_deviation(self):
        # todo; recheck
        # k = 2; rep  = 50 + 49 = 99; dem = 50 + 91 = 141;
        # rep_pct = 0.4125; dem_pct = 0.5875;
        #
        # 2 district
        # rep = 72.0 + 49.50000000000001 + 20.0 = 141.5; 0.544
        # dem = 118.5; 0.456
        # 0.5 * (abs(0.4125 - 0.5) + abs(0.544 - 0.5)) = 0.06575
        # print(ft.rep_deviation(self.districts))
        self.assertTrue(0.06590 < ft.calc_republican_deviation(self.districts) < 0.06596)

    def test_calc_weighting_factor(self):
        expected = 0
        actual = ft.calc_weighting_factor(self.districts)
        self.assertEqual(expected, actual)

    def test_calc_number_of_republican_districts(self):
        expected = 1
        actual = ft.calc_number_of_republican_districts(self.districts)
        self.assertEqual(expected, actual)


class FitnessTestCase1(unittest.TestCase):
    def setUp(self):
        self.unit_1 = Unit(1, 100, 0.6, 0.4, [2, 4], True)
        self.unit_2 = Unit(2, 100, 0.4, 0.6, [1, 3, 5], True)
        self.unit_3 = Unit(3, 100, 0.7, 0.3, [2, 6], True)
        self.unit_4 = Unit(4, 100, 0.5, 0.5, [1, 5, 7], True)
        self.unit_5 = Unit(5, 100, 0.5, 0.5, [2, 4, 6, 8], False)
        self.unit_6 = Unit(6, 100, 0.3, 0.7, [3, 5, 9], True)
        self.unit_7 = Unit(7, 100, 0.3, 0.7, [4, 8], True)
        self.unit_8 = Unit(8, 100, 0.8, 0.2, [5, 7, 9], True)
        self.unit_9 = Unit(9, 100, 0.4, 0.6, [6, 8], True)
        self.units = [self.unit_1, self.unit_2, self.unit_3, self.unit_4, self.unit_5,
                      self.unit_6, self.unit_7, self.unit_8, self.unit_9]
        Units.initialize(self.units)

        self.dist_1 = District.create_with_units({self.units[0], self.units[1], self.units[3],
                                                  self.units[2], self.units[6]})
        self.dist_2 = District.create_with_units({self.units[4]})
        self.dist_3 = District.create_with_units({self.units[5], self.units[7], self.units[8]})

        self.dists = [self.dist_1, self.dist_2, self.dist_3]

    def test_calc_population_deviation(self):
        expected = 1
        actual = ft.calc_population_deviation(self.dists)
        self.assertEquals(expected, actual)

    def test_calc_republican_deviation(self):
        expected = 0
        actual = ft.calc_republican_deviation(self.dists)
        self.assertEquals(expected, actual)

    def test_calc_weighting_factor(self):
        expected = 0.5
        actual = ft.calc_weighting_factor(self.dists)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
