import csv
from pathlib import Path


def find_missing_values(filename, column_name):
    """Return row numbers where a CSV column has missing values."""

    file_path = Path(filename)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {filename}")

    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no header.")

        if column_name not in reader.fieldnames:
            raise ValueError(f"Column not found: {column_name}")

        missing_rows = []

        for row_number, row in enumerate(reader, start=2):
            value = row.get(column_name)

            if value is None or not value.strip():
                missing_rows.append(row_number)

        return missing_rows


def display_missing_values(filename, columns):
    """Display missing-value counts for selected columns."""

    print("\n=== CSV MISSING VALUES REPORT ===")

    for column in columns:
        missing_rows = find_missing_values(filename, column)

        print(f"\nColumn: {column}")
        print(f"Missing count: {len(missing_rows)}")

        if missing_rows:
            print(f"CSV row numbers: {missing_rows}")
        else:
            print("No missing values found.")


if __name__ == "__main__":
    csv_file = "sample_data.csv"

    columns_to_check = [
        "PO Number",
        "Vendor",
        "Item",
        "Ordered Qty"
    ]

    display_missing_values(csv_file, columns_to_check)