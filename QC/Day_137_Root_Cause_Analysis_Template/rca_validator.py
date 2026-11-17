
import csv
from datetime import date
from pathlib import Path


REQUIRED_FIELDS = [
    "rca_id",
    "reported_date",
    "device_name",
    "defect_description",
    "severity",
    "containment_action",
    "root_cause",
    "corrective_action",
    "preventive_action",
    "owner",
    "target_date",
    "status"
]

VALID_SEVERITIES = {"Critical", "Major", "Minor"}
VALID_STATUSES = {"Open", "In Progress", "Closed"}


def validate_rca(record):
    """Validate required RCA fields, dates, severity and status."""

    errors = []

    for field in REQUIRED_FIELDS:
        if not record.get(field, "").strip():
            errors.append(f"Missing required field: {field}")

    if errors:
        return errors

    for field in ["reported_date", "target_date"]:
        try:
            date.fromisoformat(record[field])
        except ValueError:
            errors.append(f"Invalid date format for {field}. Use YYYY-MM-DD.")

    if record["severity"] not in VALID_SEVERITIES:
        errors.append("Invalid severity. Use Critical, Major or Minor.")

    if record["status"] not in VALID_STATUSES:
        errors.append("Invalid status. Use Open, In Progress or Closed.")

    return errors


def read_rca_records(input_file):
    """Read RCA records from CSV."""

    with open(input_file, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or missing its header.")

        missing_columns = [
            field for field in REQUIRED_FIELDS
            if field not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(
                "Missing CSV columns: " + ", ".join(missing_columns)
            )

        return list(reader)


def main():
    folder = Path(__file__).parent
    input_file = folder / "sample_rca.csv"

    records = read_rca_records(input_file)

    print("\nROOT-CAUSE ANALYSIS VALIDATION")
    print("-" * 55)

    for number, record in enumerate(records, start=1):
        errors = validate_rca(record)

        print(f"\nRCA Record: {record.get('rca_id', 'Unknown')}")

        if errors:
            print("Validation Status: FAILED")
            for error in errors:
                print(f"- {error}")
        else:
            print("Validation Status: PASSED")
            print(f"Device: {record['device_name']}")
            print(f"Severity: {record['severity']}")
            print(f"Status: {record['status']}")

    print("\nTotal RCA records:", len(records))
    print("Validation completed.")


if __name__ == "__main__":
    main()
