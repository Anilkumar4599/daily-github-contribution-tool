
import csv
from pathlib import Path

CSV_FILE = Path(__file__).with_name("stock_levels.csv")

REQUIRED_COLUMNS = [
    "item_code",
    "item_name",
    "current_stock",
    "minimum_stock",
    "maximum_stock"
]


def main():
    if not CSV_FILE.exists():
        print("Error: stock_levels.csv file not found.")
        return

    with open(CSV_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            print("Error: CSV file is empty.")
            return

        missing = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing:
            print("Error: Missing columns:", ", ".join(missing))
            return

        rows = list(reader)

    if not rows:
        print("Error: No inventory records found.")
        return

    seen_codes = set()
    reorder_count = 0
    total_reorder_qty = 0

    print("\n=== MINIMUM AND MAXIMUM STOCK REPORT ===")
    print("-" * 112)

    print(
        f"{'Item Code':<10} | "
        f"{'Item Name':<28} | "
        f"{'Current':>7} | "
        f"{'Minimum':>7} | "
        f"{'Maximum':>7} | "
        f"{'Status':<14} | "
        f"{'Reorder Qty':>11}"
    )

    print("-" * 112)

    for row_number, row in enumerate(rows, start=2):
        item_code = (row["item_code"] or "").strip()
        item_name = (row["item_name"] or "").strip()

        if not item_code or not item_name:
            print(f"Error: Missing item details at row {row_number}.")
            return

        if item_code in seen_codes:
            print(f"Error: Duplicate item code {item_code}.")
            return

        seen_codes.add(item_code)

        try:
            current = int(row["current_stock"])
            minimum = int(row["minimum_stock"])
            maximum = int(row["maximum_stock"])
        except (ValueError, TypeError):
            print(f"Error: Invalid stock quantity at row {row_number}.")
            return

        if current < 0 or minimum < 0 or maximum < 0:
            print(f"Error: Negative stock quantity at row {row_number}.")
            return

        if minimum > maximum:
            print(f"Error: Minimum exceeds maximum for {item_code}.")
            return

        if current > maximum:
            status = "ABOVE MAXIMUM"
            reorder_qty = 0

        elif current <= minimum:
            status = "REORDER NOW"
            reorder_qty = maximum - current
            reorder_count += 1
            total_reorder_qty += reorder_qty

        else:
            status = "STOCK OK"
            reorder_qty = 0

        print(
            f"{item_code:<10} | "
            f"{item_name:<28} | "
            f"{current:>7} | "
            f"{minimum:>7} | "
            f"{maximum:>7} | "
            f"{status:<14} | "
            f"{reorder_qty:>11}"
        )

    print("-" * 112)
    print(f"Total items checked       : {len(rows)}")
    print(f"Items requiring reorder   : {reorder_count}")
    print(f"Total suggested reorder   : {total_reorder_qty} units")


if __name__ == "__main__":
    main()
