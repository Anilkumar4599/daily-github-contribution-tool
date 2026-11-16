import unittest

from recurring_defect_tracker import build_recurring_tracker


class TestRecurringDefectTracker(unittest.TestCase):

    def setUp(self):
        self.records = [
            {
                "date": "2026-11-10",
                "device_name": "ATM Main Unit",
                "defect_category": "Power Failure",
                "severity": "Critical"
            },
            {
                "date": "2026-11-11",
                "device_name": "ATM Main Unit",
                "defect_category": "Power Failure",
                "severity": "Critical"
            },
            {
                "date": "2026-11-12",
                "device_name": "Lobby Camera",
                "defect_category": "No Video",
                "severity": "Critical"
            }
        ]

    def test_recurring_defect_identified(self):
        report = build_recurring_tracker(self.records)
        self.assertEqual(report[0]["status"], "Recurring")

    def test_occurrence_count(self):
        report = build_recurring_tracker(self.records)
        self.assertEqual(report[0]["occurrence_count"], 2)

    def test_single_occurrence_not_recurring(self):
        report = build_recurring_tracker(self.records)
        lobby = next(
            item for item in report
            if item["device_name"] == "Lobby Camera"
        )
        self.assertEqual(lobby["status"], "Not Recurring")

    def test_first_and_last_dates(self):
        report = build_recurring_tracker(self.records)
        self.assertEqual(report[0]["first_reported"], "2026-11-10")
        self.assertEqual(report[0]["last_reported"], "2026-11-11")

    def test_custom_threshold(self):
        report = build_recurring_tracker(self.records, threshold=3)
        self.assertEqual(report[0]["status"], "Not Recurring")

    def test_invalid_threshold(self):
        with self.assertRaises(ValueError):
            build_recurring_tracker(self.records, threshold=0)

    def test_blank_device_name(self):
        invalid_records = self.records + [{
            "date": "2026-11-13",
            "device_name": "",
            "defect_category": "Power Failure",
            "severity": "Critical"
        }]

        with self.assertRaises(ValueError):
            build_recurring_tracker(invalid_records)


if __name__ == "__main__":
    unittest.main()
