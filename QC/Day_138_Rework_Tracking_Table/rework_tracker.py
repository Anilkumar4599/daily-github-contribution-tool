import csv
from datetime import date
from pathlib import Path

CSV_COLUMNS = [
    "rework_id",
    "reported_date",
    "device_name",
    "defect_description",
    "severity",
    "rework_action",
    "assigned_to",
    "target_date",
    "status",
    "reinspection_result",
    "completion_date"
]

REQUIRED_FIELDS = [
    field for field in CSV_COLUMNS if field != "completion_date"
]

VALID_SEVERITIES = {"Critical", "Major", "Minor"}
VALID_STATUSES = {"Pending", "In Progress", "Completed"}
VALID_REINSPECTION_RESULTS = {"Pending", "Pass", "Fail"}


def validate_rework(record):
    """Validate rework tracking information."""

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
            errors.append(
                f"Invalid date format for {field}. Use YYYY-MM-DD."
            )

    completion_date = record.get("completion_date", "").strip()

    if completion_date:
        try:
            date.fromisoformat(completion_date)
        except ValueError:
            errors.append(
                "Invalid date format for completion_date. Use YYYY-MM-DD."
            )

    if record["severity"] not in VALID_SEVERITIES:
        errors.append("Invalid severity. Use Critical, Major or Minor.")

    if record["status"] not in VALID_STATUSES:
        errors.append(
            "Invalid status. Use Pending, In Progress or Completed."
        )

    if record["reinspection_result"] not in VALID_REINSPECTION_RESULTS:
        errors.append("Invalid reinspection result. Use Pending, Pass or Fail.")

    if record["status"] == "Completed":
        if record["reinspection_result"] != "Pass":
            errors.append("Completed rework must have a Pass reinspection.")

        if not completion_date:
            errors.append("Completed rework must have a completion date.")

    elif completion_date:
        errors.append(
            "Completion date must be blank unless status is Completed."
        )

    return errors


def read_rework_records(input_file):
    """Read rework records from CSV."""

    with open(input_file, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or missing its header.")

        missing_columns = [
            field for field in CSV_COLUMNS
            if field not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(
                "Missing CSV columns: " + ", ".join(missing_columns)
            )

        return list(reader)


def main():
    folder = Path(__file__).parent
    input_file = folder / "rework_tracker.csv"

    records = read_rework_records(input_file)

    print("\nQC REWORK TRACKING REPORT")
    print("-" * 55)

    valid_count = 0

    for record in records:
        errors = validate_rework(record)

        print(f"\nRework ID: {record['rework_id']}")
        print(f"Device: {record['device_name']}")
        print(f"Status: {record['status']}")
        print(f"Reinspection: {record['reinspection_result']}")

        if errors:
            print("Validation: FAILED")
            for error in errors:
                print("-", error)
        else:
            print("Validation: PASSED")
            valid_count += 1

    print("\nTotal rework records:", len(records))
    print("Valid records:", valid_count)
    print("Invalid records:", len(records) - valid_count)
    print("Validation completed.")


if __name__ == "__main__":
    main()
