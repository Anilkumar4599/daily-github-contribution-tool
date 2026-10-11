import csv
from pathlib import Path


KEY_COLUMN = "PO Number"


def read_csv(filename):
    """Read a CSV file and validate its structure."""

    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {filename}")

    with open(path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError(f"CSV has no header: {filename}")

        if len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError(f"Duplicate column names: {filename}")

        if KEY_COLUMN not in reader.fieldnames:
            raise ValueError(
                f"Required column '{KEY_COLUMN}' is missing: {filename}"
            )

        rows = list(reader)

    records = {}

    for row_number, row in enumerate(rows, start=2):
        key = (row.get(KEY_COLUMN) or "").strip()

        if not key:
            raise ValueError(
                f"Missing {KEY_COLUMN} at CSV row {row_number}: {filename}"
            )

        if key in records:
            raise ValueError(
                f"Duplicate {KEY_COLUMN} '{key}' in {filename}"
            )

        if any(value is None for value in row.values()):
            raise ValueError(
                f"Incorrect number of fields at CSV row {row_number}: {filename}"
            )

        records[key] = {
            column: (value or "").strip()
            for column, value in row.items()
        }

    return reader.fieldnames, records


def compare_csv(old_filename, new_filename):
    """Identify new, missing, unchanged and changed records."""

    old_columns, old_records = read_csv(old_filename)
    new_columns, new_records = read_csv(new_filename)

    if old_columns != new_columns:
        raise ValueError("The two CSV files must have the same columns in the same order.")

    old_keys = set(old_records)
    new_keys = set(new_records)

    added = sorted(new_keys - old_keys)
    missing = sorted(old_keys - new_keys)
    common = sorted(old_keys & new_keys)

    changed = {}
    unchanged = []

    for key in common:
        differences = {}

        for column in old_columns:
            if column == KEY_COLUMN:
                continue

            old_value = old_records[key][column]
            new_value = new_records[key][column]

            if old_value != new_value:
                differences[column] = {
                    "old": old_value,
                    "new": new_value
                }

        if differences:
            changed[key] = differences
        else:
            unchanged.append(key)

    return added, missing, changed, unchanged


def print_report(added, missing, changed, unchanged):
    """Print the comparison results."""

    print("\n=== CSV COMPARISON REPORT ===")

    print(f"\nNew records: {len(added)}")
    for key in added:
        print(f"  + {key}")

    print(f"\nMissing records: {len(missing)}")
    for key in missing:
        print(f"  - {key}")

    print(f"\nChanged records: {len(changed)}")
    for key, differences in changed.items():
        print(f"  * {key}")
        for column, values in differences.items():
            print(
                f"      {column}: "
                f"{values['old']} -> {values['new']}"
            )

    print(f"\nUnchanged records: {len(unchanged)}")
    for key in unchanged:
        print(f"  = {key}")


if __name__ == "__main__":
    try:
        added, missing, changed, unchanged = compare_csv(
            "old_report.csv",
            "new_report.csv"
        )
        print_report(added, missing, changed, unchanged)

    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")