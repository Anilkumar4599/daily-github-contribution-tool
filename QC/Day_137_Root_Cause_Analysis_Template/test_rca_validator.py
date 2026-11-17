import unittest
from rca_validator import validate_rca


def valid_record():
    return {
        "rca_id": "RCA-001",
        "reported_date": "2026-11-17",
        "device_name": "ATM Main Unit",
        "defect_description": "Power Failure",
        "severity": "Critical",
        "containment_action": "Defective unit isolated",
        "root_cause": "Power supply component failure",
        "corrective_action": "Replace defective power component",
        "preventive_action": "Add power component inspection",
        "owner": "QC Team",
        "target_date": "2026-11-20",
        "status": "Open"
    }


class TestRCAValidator(unittest.TestCase):

    def test_valid_record(self):
        self.assertEqual(validate_rca(valid_record()), [])

    def test_missing_root_cause(self):
        record = valid_record()
        record["root_cause"] = ""
        self.assertTrue(
            any("root_cause" in error for error in validate_rca(record))
        )

    def test_invalid_reported_date(self):
        record = valid_record()
        record["reported_date"] = "17-11-2026"
        self.assertTrue(
            any("reported_date" in error for error in validate_rca(record))
        )

    def test_invalid_target_date(self):
        record = valid_record()
        record["target_date"] = "20-11-2026"
        self.assertTrue(
            any("target_date" in error for error in validate_rca(record))
        )

    def test_invalid_severity(self):
        record = valid_record()
        record["severity"] = "Urgent"
        self.assertTrue(
            any("Invalid severity" in error for error in validate_rca(record))
        )

    def test_invalid_status(self):
        record = valid_record()
        record["status"] = "Pending"
        self.assertTrue(
            any("Invalid status" in error for error in validate_rca(record))
        )

    def test_missing_owner(self):
        record = valid_record()
        record["owner"] = ""
        self.assertTrue(
            any("owner" in error for error in validate_rca(record))
        )


if __name__ == "__main__":
    unittest.main()
