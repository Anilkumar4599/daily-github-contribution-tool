import csv
from pathlib import Path


REQUIRED_COLUMNS = [
    "Item Code",
    "Item Name",
    "Category",
    "Current Stock",
    "Minimum Stock",
    "Reorder Quantity",
    "Unit",
]


def load_inventory(filename):
    """Read and validate inventory records from a CSV file."""

    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {filename}")

    if not path.is_file():
        raise ValueError(f"Input path is not a file: {filename}")

    with open(path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty or has no header.")

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
        raise ValueError("CSV contains no inventory records.")

    seen_codes = set()

    for row_number, row in enumerate(rows, start=2):
        for column in REQUIRED_COLUMNS:
            if row.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at CSV row {row_number}."
                )
            row[column] = row[column].strip()

        item_code = row["Item Code"]

        if not item_code:
            raise ValueError(f"Item Code is blank at row {row_number}.")

        if item_code in seen_codes:
            raise ValueError(f"Duplicate Item Code: {item_code}")

        seen_codes.add(item_code)

        if not row["Item Name"] or not row["Category"] or not row["Unit"]:
            raise ValueError(
                f"Item Name, Category, and Unit are required "
                f"at row {row_number}."
            )

        try:
            current_stock = int(row["Current Stock"])
            minimum_stock = int(row["Minimum Stock"])
            reorder_quantity = int(row["Reorder Quantity"])
        except ValueError as error:
            raise ValueError(
                f"Stock values must be whole numbers at row {row_number}."
            ) from error

        if current_stock < 0:
            raise ValueError(
                f"Current Stock cannot be negative at row {row_number}."
            )

        if minimum_stock <= 0:
            raise ValueError(
                f"Minimum Stock must be greater than zero "
                f"at row {row_number}."
            )

        if reorder_quantity <= 0:
            raise ValueError(
                f"Reorder Quantity must be greater than zero "
                f"at row {row_number}."
            )

    return rows


def analyze_inventory(rows):
    """Classify stock and calculate replenishment quantities."""

    report = []

    for row in rows:
        current = int(row["Current Stock"])
        minimum = int(row["Minimum Stock"])
        reorder_qty = int(row["Reorder Quantity"])

        shortage = max(0, minimum - current)

        if current == 0:
            status = "Critical - Out of Stock"
            priority = "Critical"
        elif current < minimum:
            status = "Low Stock"
            priority = "High"
        elif current == minimum:
            status = "At Reorder Point"
            priority = "Medium"
        else:
            status = "Adequate"
            priority = "None"

        if priority == "None":
            suggested_order = 0
        else:
            # Use the configured reorder quantity for flagged items.
            suggested_order = reorder_qty

        report.append({
            "Item Code": row["Item Code"],
            "Item Name": row["Item Name"],
            "Category": row["Category"],
            "Current Stock": current,
            "Minimum Stock": minimum,
            "Shortage to Minimum": shortage,
            "Reorder Quantity": reorder_qty,
            "Suggested Order Quantity": suggested_order,
            "Unit": row["Unit"],
            "Stock Status": status,
            "Priority": priority,
        })

    return report


def save_report(report, filename):
    """Write the inventory analysis to a CSV report."""

    if not report:
        raise ValueError("No inventory records available to report.")

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=list(report[0].keys()))
        writer.writeheader()
        writer.writerows(report)


def print_summary(report):
    """Print the key stock alerts for management."""

    critical = [
        row for row in report if row["Priority"] == "Critical"
    ]
    high = [
        row for row in report if row["Priority"] == "High"
    ]
    medium = [
        row for row in report if row["Priority"] == "Medium"
    ]
    adequate = [
        row for row in report if row["Priority"] == "None"
    ]

    print("\n=== INVENTORY LOW-STOCK ALERT REPORT ===")
    print(f"Total inventory items: {len(report)}")
    print(f"Critical - Out of Stock: {len(critical)}")
    print(f"High - Low Stock: {len(high)}")
    print(f"Medium - At Reorder Point: {len(medium)}")
    print(f"Adequate Stock: {len(adequate)}")

    print("\nItems Requiring Attention:")

    for row in report:
        if row["Priority"] != "None":
            print(
                f"{row['Item Code']} | {row['Item Name']} | "
                f"Current: {row['Current Stock']} | "
                f"Minimum: {row['Minimum Stock']} | "
                f"Status: {row['Stock Status']} | "
                f"Priority: {row['Priority']} | "
                f"Suggested Order: "
                f"{row['Suggested Order Quantity']} {row['Unit']}"
            )


def main():
    input_file = "inventory_data.csv"
    output_file = "low_stock_alert_report.csv"

    inventory = load_inventory(input_file)
    report = analyze_inventory(inventory)

    save_report(report, output_file)
    print_summary(report)

    print(f"\nReport saved: {output_file}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")