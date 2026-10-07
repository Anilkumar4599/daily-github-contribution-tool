def validate_email(email):
    """
    Validate an email address using basic string rules.

    Rules:
    1. Input must be a string.
    2. Email must contain exactly one @ symbol.
    3. Email must contain text before @.
    4. Email must contain text after @.
    5. Domain must contain a dot.
    6. Email must not contain spaces.
    """

    if not isinstance(email, str):
        return False

    email = email.strip()

    if not email:
        return False

    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username:
        return False

    if not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def check_sample_emails(emails):
    """Check a list of sample email addresses."""

    for email in emails:
        result = validate_email(email)

        if result:
            print(f"{email:<35} VALID")
        else:
            print(f"{email:<35} INVALID")


if __name__ == "__main__":

    sample_emails = [
        "anil@example.com",
        "procurement@apar.com",
        "qa.manager@company.co.in",
        "service.team@example.org",
        "invalid-email",
        "user@",
        "@example.com",
        "user example@gmail.com",
        "user@@example.com",
        "user@example"
    ]

    print("=== EMAIL VALIDATION ===")
    check_sample_emails(sample_emails)