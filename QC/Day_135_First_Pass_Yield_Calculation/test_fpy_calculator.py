
import unittest
from fpy_calculator import calculate_fpy


class TestFPYCalculator(unittest.TestCase):

    def test_normal_fpy(self):
        self.assertEqual(calculate_fpy(85, 100), 85.0)

    def test_all_units_pass(self):
        self.assertEqual(calculate_fpy(20, 20), 100.0)

    def test_no_units_pass(self):
        self.assertEqual(calculate_fpy(0, 20), 0.0)

    def test_decimal_fpy(self):
        self.assertEqual(calculate_fpy(17, 20), 85.0)

    def test_zero_inspected(self):
        with self.assertRaises(ValueError):
            calculate_fpy(0, 0)

    def test_passed_more_than_inspected(self):
        with self.assertRaises(ValueError):
            calculate_fpy(21, 20)

    def test_negative_passed_units(self):
        with self.assertRaises(ValueError):
            calculate_fpy(-1, 20)


if __name__ == "__main__":
    unittest.main()
