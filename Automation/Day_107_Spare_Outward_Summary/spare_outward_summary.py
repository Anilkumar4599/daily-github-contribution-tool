
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "spare_outward_data.csv"
OUTPUT_FILE = BASE_DIR / "spare_outward_summary.csv"

REQUIRED_COLUMNS = [
    "Transaction ID",
    "Transaction Date",
    "Item Code",
    "Item Name",
    "Category",
    "Quantity Issued",
    "Unit",
    "Destination",
    "Reference",
]


def load_transactions(filename):
    """Read and validate spare-outward transactions."""

    path = Path(filename)

    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {path}")

    with path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV is empty or has no header.")

        if len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError("CSV contains duplicate column names.")

        missing = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        rows = list(reader)

    if not rows:
        raise ValueError("CSV contains no transaction records.")

    seen_ids = set()
    item_details = {}

    for row_number, row in enumerate(rows, start=2):
        for column in REQUIRED_COLUMNS:
            if row.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at CSV row {row_number}."
                )
            row[column] = row[column].strip()

        transaction_id = row["Transaction ID"]

        if not transaction_id:
            raise ValueError(
                f"Transaction ID is blank at row {row_number}."
            )

        if transaction_id in seen_ids:
            raise ValueError(
                f"Duplicate Transaction ID: {transaction_id}"
            )
        seen_ids.add(transaction_id)

        for column in [
            "Item Code", "Item Name", "Category",
            "Unit", "Destination", "Reference",
        ]:
            if not row[column]:
                raise ValueError(
                    f"{column} is required at CSV row {row_number}."
                )

        try:
            datetime.strptime(row["Transaction Date"], "%Y-%m-%d")
        except ValueError as error:
            raise ValueError(
                f"Invalid Transaction Date at row {row_number}. "
                "Use YYYY-MM-DD."
            ) from error

        try:
            quantity = int(row["Quantity Issued"])
        except ValueError as error:
            raise ValueError(
                f"Quantity Issued must be a whole number "
                f"at row {row_number}."
            ) from error

        if quantity <= 0:
            raise ValueError(
                f"Quantity Issued must be greater than zero "
                f"at row {row_number}."
            )

        item_code = row["Item Code"]
        details = (
            row["Item Name"],
            row["Category"],
            row["Unit"],
        )

        if item_code in item_details and item_details[item_code] != details:
            raise ValueError(
                f"Inconsistent item name, category, or unit "
                f"for Item Code {item_code} at row {row_number}."
            )

        item_details[item_code] = details
        row["_quantity"] = quantity

    return rows


def summarize_by_item(transactions):
    """Group transactions by item code and total the quantities."""

    grouped = defaultdict(
        lambda: {
            "Item Name": "",
            "Category": "",
            "Unit": "",
            "Transaction Count": 0,
            "Total Quantity Issued": 0,
            "Destinations": set(),
            "First Transaction Date": "",
            "Last Transaction Date": "",
        }
    )

    for row in transactions:
        item_code = row["Item Code"]
        item = grouped[item_code]
        transaction_date = row["Transaction Date"]

        item["Item Name"] = row["Item Name"]
        item["Category"] = row["Category"]
        item["Unit"] = row["Unit"]
        item["Transaction Count"] += 1
        item["Total Quantity Issued"] += row["_quantity"]
        item["Destinations"].add(row["Destination"])

        if (
            not item["First Transaction Date"]
            or transaction_date < item["First Transaction Date"]
        ):
            item["First Transaction Date"] = transaction_date

        if (
            not item["Last Transaction Date"]
            or transaction_date > item["Last Transaction Date"]
        ):
            item["Last Transaction Date"] = transaction_date

    report = []

    for item_code, item in sorted(grouped.items()):
        report.append({
            "Item Code": item_code,
            "Item Name": item["Item Name"],
            "Category": item["Category"],
            "Unit": item["Unit"],
            "Transaction Count": item["Transaction Count"],
            "Total Quantity Issued": item["Total Quantity Issued"],
            "Unique Destinations": len(item["Destinations"]),
            "First Transaction Date": item["First Transaction Date"],
            "Last Transaction Date": item["Last Transaction Date"],
        })

    return report


def save_report(report, filename):
    """Write the item-wise summary to a CSV file."""

    if not report:
        raise ValueError("No summary data available to save.")

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=list(report[0].keys()))
        writer.writeheader()
        writer.writerows(report)


def print_summary(transactions, report):
    """Print a management-friendly summary."""

    total_transactions = len(transactions)
    total_quantity = sum(row["_quantity"] for row in transactions)

    print("\n=== SPARE-OUTWARD SUMMARY BY ITEM ===")
    print(f"Total outward transactions: {total_transactions}")
    print(f"Unique spare items: {len(report)}")
    print(f"Total quantity issued across all items: {total_quantity}")

    print("\n=== ITEM-WISE DETAILS ===")

    for row in report:
        print(
            f"{row['Item Code']} | {row['Item Name']} | "
            f"Transactions: {row['Transaction Count']} | "
            f"Total Issued: {row['Total Quantity Issued']} "
            f"{row['Unit']} | "
            f"Destinations: {row['Unique Destinations']}"
        )


def main():
    transactions = load_transactions(INPUT_FILE)
    report = summarize_by_item(transactions)
    save_report(report, OUTPUT_FILE)
    print_summary(transactions, report)
    print(f"\nReport saved: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")
