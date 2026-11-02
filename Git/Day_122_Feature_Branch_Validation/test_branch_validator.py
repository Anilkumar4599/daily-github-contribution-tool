
import unittest

from branch_validator import validate_branch_name


class TestBranchValidator(unittest.TestCase):

    def test_valid_feature_branch(self):
        valid, message = validate_branch_name(
            "feature/day-122-branch-validation"
        )
        self.assertTrue(valid)

    def test_valid_bugfix_branch(self):
        valid, message = validate_branch_name(
            "bugfix/fix-date-calculation"
        )
        self.assertTrue(valid)

    def test_reject_spaces(self):
        valid, message = validate_branch_name(
            "feature Day 122"
        )
        self.assertFalse(valid)

    def test_reject_empty_name(self):
        valid, message = validate_branch_name("")
        self.assertFalse(valid)

    def test_reject_missing_task_name(self):
        valid, message = validate_branch_name("feature/")
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main(verbosity=2)
