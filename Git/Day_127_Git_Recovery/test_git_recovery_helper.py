
import unittest

from git_recovery_helper import validate_recovery_action


class TestGitRecoveryHelper(unittest.TestCase):

    def test_valid_restore(self):
        valid, message = validate_recovery_action(
            "restore", "README.md"
        )
        self.assertTrue(valid)

    def test_valid_unstage(self):
        valid, message = validate_recovery_action(
            "unstage", "README.md"
        )
        self.assertTrue(valid)

    def test_invalid_action(self):
        valid, message = validate_recovery_action(
            "delete", "README.md"
        )
        self.assertFalse(valid)

    def test_empty_filename(self):
        valid, message = validate_recovery_action(
            "restore", ""
        )
        self.assertFalse(valid)

    def test_folder_path_rejected(self):
        valid, message = validate_recovery_action(
            "restore", "Git/README.md"
        )
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
