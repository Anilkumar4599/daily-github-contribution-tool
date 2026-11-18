import unittest
from rework_tracker import validate_rework


def valid_record():
    return {
        "rework_id": "RW-001",
        "reported_date": "2026-11-18",
        "device_name": "ATM Main Unit",
        "defect_description": "Power Failure",
        "severity": "Critical",
        "rework_action": "Replace defective power supply",
        "assigned_to": "QC Team",
        "target_date": "2026-11-20",
        "status": "In Progress",
        "reinspection_result": "Pending",
        "completion_date": ""
    }


class TestReworkTracker(unittest.TestCase):

    def test_valid_pending_record(self):
        self.assertEqual(validate_rework(valid_record()), [])

    def test_missing_assigned_to(self):
        record = valid_record()
        record["assigned_to"] = ""
        self.assertTrue(
            any("assigned_to" in error for error in validate_rework(record))
        )

    def test_invalid_reported_date(self):
        record = valid_record()
        record["reported_date"] = "18-11-2026"
        self.assertTrue(
            any("reported_date" in error for error in validate_rework(record))
        )

    def test_invalid_severity(self):
        record = valid_record()
        record["severity"] = "Urgent"
        self.assertTrue(
            any("Invalid severity" in error for error in validate_rework(record))
        )

    def test_invalid_status(self):
        record = valid_record()
        record["status"] = "Closed"
        self.assertTrue(
            any("Invalid status" in error for error in validate_rework(record))
        )

    def test_completed_requires_pass(self):
        record = valid_record()
        record["status"] = "Completed"
        record["completion_date"] = "2026-11-18"
        record["reinspection_result"] = "Fail"
        self.assertTrue(
            any("must have a Pass" in error for error in validate_rework(record))
        )

    def test_completed_requires_completion_date(self):
        record = valid_record()
        record["status"] = "Completed"
        record["reinspection_result"] = "Pass"
        self.assertTrue(
            any("completion date" in error for error in validate_rework(record))
        )

    def test_valid_completed_record(self):
        record = valid_record()
        record["status"] = "Completed"
        record["reinspection_result"] = "Pass"
        record["completion_date"] = "2026-11-18"
        self.assertEqual(validate_rework(record), [])


if __name__ == "__main__":
    unittest.main()
