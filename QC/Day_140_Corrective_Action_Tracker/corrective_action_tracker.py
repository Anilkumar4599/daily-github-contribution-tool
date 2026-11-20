import csv
from datetime import date
from pathlib import Path

REQUIRED_FIELDS = [
    "action_id",
    "reported_date",
    "defect_id",
    "device_name",
    "root_cause",
    "corrective_action",
    "owner",
    "target_date",
    "status"
]

VALID_STATUSES = {"Open", "In Progress", "Closed"}


def validate_action(record):
    """Check required fields, dates and action status."""

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
            errors.append(f"Invalid date format: {field}")

    closure_date = record.get("closure_date", "").strip()

    if closure_date:
        try:
            date.fromisoformat(closure_date)
        except ValueError:
            errors.append("Invalid closure date format.")

    if record["status"] not in VALID_STATUSES:
        errors.append("Invalid status. Use Open, In Progress or Closed.")

    if record["status"] == "Closed" and not closure_date:
        errors.append("Closed action must have a closure date.")

    if record["status"] != "Closed" and closure_date:
        errors.append("Only closed actions can have a closure date.")

    return errors


def main():
    folder = Path(__file__).parent
    input_file = folder / "corrective_action_tracker.csv"

    with open(input_file, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is missing its header.")

        missing = [
            field for field in REQUIRED_FIELDS + ["closure_date"]
            if field not in reader.fieldnames
        ]

        if missing:
            raise ValueError("Missing columns: " + ", ".join(missing))

        records = list(reader)

    print("\nCORRECTIVE ACTION TRACKING REPORT")
    print("-" * 50)

    counts = {"Open": 0, "In Progress": 0, "Closed": 0}

    for record in records:
        errors = validate_action(record)

        print(f"\nAction ID: {record['action_id']}")
        print(f"Device: {record['device_name']}")
        print(f"Owner: {record['owner']}")
        print(f"Status: {record['status']}")

        if errors:
            print("Validation: FAILED")
            for error in errors:
                print("-", error)
        else:
            print("Validation: PASSED")
            counts[record["status"]] += 1

    print("\nACTION SUMMARY")
    print("-" * 30)
    print("Total records:", len(records))
    print("Open:", counts["Open"])
    print("In Progress:", counts["In Progress"])
    print("Closed:", counts["Closed"])
    print("Validation completed.")


if __name__ == "__main__":
    main()
