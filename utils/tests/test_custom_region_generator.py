import unittest
from utils import custom_region_generator as gen


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_on_region_border(self):
        self.assertTrue(gen.is_on_region_border(3, 3, 3))
        self.assertFalse(gen.is_on_region_border(107, 100, 100))
        self.assertTrue(gen.is_on_region_border(101, 100, 100))

    def test_get_dist_number_by_unit_index(self):
        self.assertEquals(gen.get_dist_number_by_unit_number(1, 18, 18), 1)
        self.assertEquals(gen.get_dist_number_by_unit_number(12, 18, 18), 2)
        self.assertEquals(gen.get_dist_number_by_unit_number(24, 24, 24), 4)
        self.assertEquals(gen.get_dist_number_by_unit_number(336, 24, 24), 12)
        self.assertEquals(gen.get_dist_number_by_unit_number(48, 30, 30), 8)


if __name__ == "__main__":
    unittest.main()
