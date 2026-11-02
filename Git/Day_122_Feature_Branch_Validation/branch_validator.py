
import re


def validate_branch_name(branch_name):
    """
    Validate a Git feature branch name.

    Accepted formats:
    feature/example-task
    bugfix/example-fix
    docs/example-documentation
    hotfix/example-hotfix
    """

    if not isinstance(branch_name, str):
        return False, "Branch name must be text."

    branch_name = branch_name.strip()

    if not branch_name:
        return False, "Branch name cannot be empty."

    pattern = r"^(feature|bugfix|docs|hotfix)/[a-z0-9]+(?:-[a-z0-9]+)*$"

    if not re.fullmatch(pattern, branch_name):
        return False, (
            "Invalid branch name. Use a supported prefix "
            "and lowercase words separated by hyphens."
        )

    return True, "Valid branch name."


def main():
    print("=== GIT BRANCH NAME VALIDATOR ===")

    branch_name = input("Enter a branch name: ")

    is_valid, message = validate_branch_name(branch_name)

    print(message)

    if is_valid:
        print(f"Accepted branch: {branch_name}")
    else:
        print("Please enter a valid branch name.")


if __name__ == "__main__":
    main()
