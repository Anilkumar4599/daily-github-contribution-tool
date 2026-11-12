
import unittest

from defect_pareto import (
    validate_defect_rows,
    calculate_pareto,
)


def sample_rows():
    return [
        {"defect_category": "Camera No Video", "defect_count": "18"},
        {"defect_category": "Router/Network Issue", "defect_count": "12"},
        {"defect_category": "Power Failure", "defect_count": "8"},
        {"defect_category": "Intermittent Restart", "defect_count": "5"},
        {"defect_category": "DCUPS Backup Issue", "defect_count": "4"},
        {"defect_category": "Other Defects", "defect_count": "3"},
    ]


class TestDefectPareto(unittest.TestCase):

    def test_pareto_order_and_percentages(self):
        defects = validate_defect_rows(sample_rows())
        report = calculate_pareto(defects)

        self.assertEqual(report[0]["defect_category"], "Camera No Video")

        percentages = [
            item["cumulative_percentage"] for item in report
        ]

        self.assertEqual(
            percentages,
            [36.0, 60.0, 76.0, 86.0, 94.0, 100.0]
        )

    def test_blank_category_rejected(self):
        rows = [
            {"defect_category": "", "defect_count": "5"}
        ]

        with self.assertRaisesRegex(ValueError, "cannot be blank"):
            validate_defect_rows(rows)

    def test_non_numeric_count_rejected(self):
        rows = [
            {"defect_category": "Camera Issue", "defect_count": "ABC"}
        ]

        with self.assertRaisesRegex(ValueError, "whole number"):
            validate_defect_rows(rows)

    def test_zero_and_negative_counts_rejected(self):
        for count in ["0", "-2"]:
            with self.subTest(count=count):
                rows = [
                    {"defect_category": "Camera Issue", "defect_count": count}
                ]

                with self.assertRaisesRegex(ValueError, "greater than zero"):
                    validate_defect_rows(rows)

    def test_duplicate_categories_rejected(self):
        rows = [
            {"defect_category": "Camera Issue", "defect_count": "5"},
            {"defect_category": "camera issue", "defect_count": "3"},
        ]

        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_defect_rows(rows)

    def test_missing_count_rejected(self):
        rows = [
            {"defect_category": "Camera Issue", "defect_count": ""}
        ]

        with self.assertRaisesRegex(ValueError, "cannot be blank"):
            validate_defect_rows(rows)


if __name__ == "__main__":
    unittest.main()
