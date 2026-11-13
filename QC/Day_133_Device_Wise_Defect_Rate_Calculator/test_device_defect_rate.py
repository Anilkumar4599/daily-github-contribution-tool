
import unittest

from device_defect_rate import calculate_device_defect_rates


class TestDeviceDefectRate(unittest.TestCase):

    def test_single_device_defect_rate(self):
        rows = [
            {
                "device_name": "ATM Main Unit",
                "units_inspected": "100",
                "defective_units": "8"
            }
        ]

        result = calculate_device_defect_rates(rows)

        self.assertEqual(result[0]["good_units"], 92)
        self.assertAlmostEqual(
            result[0]["defect_rate_percent"], 8.0
        )

    def test_devices_sorted_by_highest_defect_rate(self):
        rows = [
            {
                "device_name": "ATM Main Unit",
                "units_inspected": "100",
                "defective_units": "8"
            },
            {
                "device_name": "Outdoor Camera",
                "units_inspected": "80",
                "defective_units": "10"
            }
        ]

        result = calculate_device_defect_rates(rows)

        self.assertEqual(
            result[0]["device_name"], "Outdoor Camera"
        )
        self.assertAlmostEqual(
            result[0]["defect_rate_percent"], 12.5
        )

    def test_zero_units_inspected_rejected(self):
        rows = [
            {
                "device_name": "DCUPS",
                "units_inspected": "0",
                "defective_units": "0"
            }
        ]

        with self.assertRaises(ValueError):
            calculate_device_defect_rates(rows)

    def test_negative_defective_units_rejected(self):
        rows = [
            {
                "device_name": "DCUPS",
                "units_inspected": "60",
                "defective_units": "-2"
            }
        ]

        with self.assertRaises(ValueError):
            calculate_device_defect_rates(rows)

    def test_defective_units_cannot_exceed_inspected(self):
        rows = [
            {
                "device_name": "Lobby Camera",
                "units_inspected": "10",
                "defective_units": "12"
            }
        ]

        with self.assertRaises(ValueError):
            calculate_device_defect_rates(rows)

    def test_duplicate_device_names_rejected(self):
        rows = [
            {
                "device_name": "DCUPS",
                "units_inspected": "60",
                "defective_units": "3"
            },
            {
                "device_name": "dcups",
                "units_inspected": "40",
                "defective_units": "2"
            }
        ]

        with self.assertRaises(ValueError):
            calculate_device_defect_rates(rows)

    def test_blank_device_name_rejected(self):
        rows = [
            {
                "device_name": "",
                "units_inspected": "50",
                "defective_units": "5"
            }
        ]

        with self.assertRaises(ValueError):
            calculate_device_defect_rates(rows)


if __name__ == "__main__":
    unittest.main()
