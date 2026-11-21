
import csv
from datetime import date, datetime
from pathlib import Path

# Fixed report date for this sample exercise
REPORT_DATE = date(2026, 11, 21)

CSV_FILE = Path(__file__).with_name("inventory_aging_sample.csv")

AGING_CATEGORIES = [
    "Fresh",
    "Normal",
    "Slow-moving",
    "Old stock"
]


def classify_inventory(age_days):
    """Classify stock based on the number of days held."""

    if age_days <= 30:
        return "Fresh"
    elif age_days <= 60:
        return "Normal"
    elif age_days <= 90:
        return "Slow-moving"
    else:
        return "Old stock"


def main():
    inventory_records = []

    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_fields = {
            "inventory_id",
            "item_name",
            "category",
            "received_date",
            "qty_on_hand",
            "unit_cost"
        }

        if not reader.fieldnames or not required_fields.issubset(reader.fieldnames):
            raise ValueError("CSV is missing one or more required columns.")

        for row in reader:
            received_date = datetime.strptime(
                row["received_date"], "%Y-%m-%d"
            ).date()

            age_days = (REPORT_DATE - received_date).days

            if age_days < 0:
                raise ValueError(
                    f"Received date is after report date: {row['inventory_id']}"
                )

            quantity = int(row["qty_on_hand"])
            unit_cost = float(row["unit_cost"])

            if quantity < 0 or unit_cost < 0:
                raise ValueError(
                    f"Negative quantity or cost: {row['inventory_id']}"
                )

            stock_value = quantity * unit_cost
            aging_category = classify_inventory(age_days)

            inventory_records.append({
                "inventory_id": row["inventory_id"],
                "item_name": row["item_name"],
                "age_days": age_days,
                "quantity": quantity,
                "stock_value": stock_value,
                "aging_category": aging_category
            })

    print("\nINVENTORY AGING REPORT")
    print("=" * 75)
    print(f"Report Date: {REPORT_DATE}")
    print("-" * 75)

    for item in inventory_records:
        print(f"\nInventory ID : {item['inventory_id']}")
        print(f"Item         : {item['item_name']}")
        print(f"Age          : {item['age_days']} days")
        print(f"Quantity     : {item['quantity']}")
        print(f"Stock Value  : Rs. {item['stock_value']:,.2f}")
        print(f"Aging Status : {item['aging_category']}")

    print("\n\nAGING CATEGORY SUMMARY")
    print("-" * 75)

    total_value = 0

    for category in AGING_CATEGORIES:
        matching_items = [
            item for item in inventory_records
            if item["aging_category"] == category
        ]

        item_count = len(matching_items)
        total_quantity = sum(item["quantity"] for item in matching_items)
        category_value = sum(item["stock_value"] for item in matching_items)

        total_value += category_value

        print(
            f"{category:<15} | Records: {item_count} "
            f"| Quantity: {total_quantity} "
            f"| Value: Rs. {category_value:,.2f}"
        )

    print("-" * 75)
    print(f"Total inventory records : {len(inventory_records)}")
    print(f"Total stock value       : Rs. {total_value:,.2f}")
    print("\nInventory aging report completed successfully.")


if __name__ == "__main__":
    main()
