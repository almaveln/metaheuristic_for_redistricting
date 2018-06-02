import unittest
from utils import custom_region_generator_v2 as gen


# unittest.TestCase
# unittest.TestCase
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_district_layout(self):
        # print(gen.generate_district_layout(8, 8))
        self.assertTrue(check_result(gen.generate_district_layout(4, 4), 4, 4))
        self.assertTrue(check_result(gen.generate_district_layout(6, 6), 6, 6))
        self.assertTrue(check_result(gen.generate_district_layout(8, 8), 8, 8))
        self.assertTrue(check_result(gen.generate_district_layout(10, 10), 10, 10))
        self.assertTrue(check_result(gen.generate_district_layout(12, 12), 12, 12))
        self.assertTrue(check_result(gen.generate_district_layout(14, 14), 14, 14))
        self.assertTrue(check_result(gen.generate_district_layout(16, 16), 16, 16))

    def test_get_dist_number_by_unit_number(self):
        self.assertEquals(gen.get_dist_number_by_unit_number(1, 4, 4), 1)
        self.assertEquals(gen.get_dist_number_by_unit_number(3, 4, 4), 2)
        self.assertEquals(gen.get_dist_number_by_unit_number(10, 4, 4), 3)
        self.assertEquals(gen.get_dist_number_by_unit_number(12, 4, 4), 4)

        self.assertEquals(gen.get_dist_number_by_unit_number(7, 8, 8), 2)

    def test_select_republican_support(self):
        nrows = 4
        ncolumns = 4
        support = gen.generate_district_layout(nrows, ncolumns)
        rep_support = gen.select_republican_support(support, 1, nrows, ncolumns)
        self.assertEquals(rep_support, 0.7)

        nrows = 6
        ncolumns = 6
        support = gen.generate_district_layout(nrows, ncolumns)
        rep_support = gen.select_republican_support(support, 1, nrows, ncolumns)
        self.assertEquals(rep_support, 0.7)

        nrows = 8
        ncolumns = 8
        support = gen.generate_district_layout(nrows, ncolumns)
        rep_support = gen.select_republican_support(support, 32, nrows, ncolumns)
        self.assertEquals(rep_support, 0.7)

        nrows = 8
        ncolumns = 8
        support = gen.generate_district_layout(nrows, ncolumns)
        print(support)
        rep_support = gen.select_republican_support(support, 30, nrows, ncolumns)
        self.assertEquals(rep_support, 0.8)

        nrows = 8
        ncolumns = 8
        support = gen.generate_district_layout(nrows, ncolumns)
        print(support)
        rep_support = gen.select_republican_support(support, 38, nrows, ncolumns)
        self.assertEquals(rep_support, 0.4)


def check_result(arr, nrows, ncolumns):
    n_elem = int(nrows * ncolumns / 4)
    total = sum([percent for row in arr for percent in row])
    # print(total)
    # print(n_elem)
    # print((total / n_elem))
    # print(round(total / n_elem, 2))
    return 0.5 == round(total / n_elem, 1)


if __name__ == "__main__":
    unittest.main()
    # print(check_result(gen.generate_district_layout(4, 4), 4, 4))
    # print(check_result(gen.generate_district_layout(6, 6), 6, 6))
    # print(check_result(gen.generate_district_layout(8, 8), 8, 8))
    # print(check_result(gen.generate_district_layout(10, 10), 10, 10))
    # print(check_result(gen.generate_district_layout(12, 12), 12, 12))
    # print(check_result(gen.generate_district_layout(14, 14), 14, 14))
    # print(check_result(gen.generate_district_layout(16, 16), 16, 16))

    # print(gen.get_dist_number_by_unit_number(1, 4, 4))
    # print(gen.get_dist_number_by_unit_number(3, 4, 4))
    # print(gen.get_dist_number_by_unit_number(10, 4, 4))
    # print(gen.get_dist_number_by_unit_number(12, 4, 4))

    # [[0.7, 0.4, 0.7, 0.7], [0.6, 0.3, 0.4, 0.4], [0.3, 0.8, 0.3, 0.3], [0.3, 0.8, 0.3, 0.7]]


    # print(gen.get_dist_number_by_unit_number(12, 8, 8))
