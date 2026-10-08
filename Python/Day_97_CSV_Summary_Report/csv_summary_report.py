import csv
from pathlib import Path


REQUIRED_COLUMNS = [
    "PO Number",
    "Vendor",
    "Item",
    "Ordered Qty",
    "Received Qty",
    "Status"
]


def read_csv_file(filename):
    """Read and validate the CSV file."""

    file_path = Path(filename)

    if not file_path.exists():
        print(f"Error: File does not exist: {filename}")
        return None

    if not file_path.is_file():
        print(f"Error: Path is not a file: {filename}")
        return None

    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: CSV file has no header.")
                return None

            missing_columns = [
                column
                for column in REQUIRED_COLUMNS
                if column not in reader.fieldnames
            ]

            if missing_columns:
                print(f"Error: Missing columns: {missing_columns}")
                return None

            rows = list(reader)

            if not rows:
                print("Error: CSV file contains no data.")
                return None

            return rows

    except Exception as error:
        print(f"Error reading CSV file: {error}")
        return None


def create_summary(rows):
    """Create summary information from procurement records."""

    total_pos = len(rows)
    total_ordered = 0
    total_received = 0

    status_counts = {}

    for row in rows:

        try:
            ordered_qty = int(row["Ordered Qty"])
            received_qty = int(row["Received Qty"])
        except (ValueError, TypeError):
            print(f"Warning: Invalid quantity in PO {row['PO Number']}")
            continue

        total_ordered += ordered_qty
        total_received += received_qty

        status = row["Status"].strip()

        if status:
            status_counts[status] = status_counts.get(status, 0) + 1

    pending_qty = total_ordered - total_received

    return {
        "total_pos": total_pos,
        "total_ordered": total_ordered,
        "total_received": total_received,
        "pending_qty": pending_qty,
        "status_counts": status_counts
    }


def print_summary(summary):
    """Display the summary report."""

    print("\n=== PROCUREMENT CSV SUMMARY REPORT ===")

    print(f"Total POs       : {summary['total_pos']}")
    print(f"Total Ordered   : {summary['total_ordered']}")
    print(f"Total Received  : {summary['total_received']}")
    print(f"Pending Qty     : {summary['pending_qty']}")

    print("\nPO Status Summary:")

    for status, count in summary["status_counts"].items():
        print(f"{status:<15}: {count}")


if __name__ == "__main__":

    csv_file = "sample_procurement.csv"

    rows = read_csv_file(csv_file)

    if rows is not None:
        summary = create_summary(rows)
        print_summary(summary)