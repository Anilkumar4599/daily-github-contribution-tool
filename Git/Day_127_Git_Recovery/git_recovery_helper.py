
from pathlib import Path


def validate_recovery_action(action, filename):
    """Validate a Git recovery action and filename."""

    allowed_actions = [
        "restore",
        "unstage",
        "revert"
    ]

    if not action or not action.strip():
        return False, "Action cannot be empty."

    if action not in allowed_actions:
        return False, "Invalid recovery action."

    if not filename or not filename.strip():
        return False, "Filename cannot be empty."

    if Path(filename).name != filename:
        return False, "Enter a filename only, not a folder path."

    return True, "Input accepted."


if __name__ == "__main__":
    print("Git Recovery Helper")

    action = input("Enter action (restore/unstage/revert): ").strip()
    filename = input("Enter filename: ").strip()

    valid, message = validate_recovery_action(action, filename)

    print(message)

    if valid:
        print("Selected action:", action)
        print("Selected file:", filename)
        print("Reminder: Review git status and git diff before recovery.")
