import csv
from datetime import date
from pathlib import Path

# Report date for this sample exercise
REPORT_DATE = date(2026, 11, 22)

BASE_DIR = Path(__file__).parent

OPENING_FILE = BASE_DIR / "opening_stock.csv"
TRANSACTION_FILE = BASE_DIR / "stock_transactions.csv"

OPENING_FIELDS = {"item_code", "item_name", "opening_qty"}

TRANSACTION_FIELDS = {
    "transaction_id",
    "transaction_date",
    "item_code",
    "transaction_type",
    "quantity",
    "reference"
}

VALID_TYPES = {"Stock In", "Stock Out"}


def read_csv_file(file_path, required_fields):
    """Read CSV and validate required columns."""

    if not file_path.exists():
        raise ValueError(f"File not found: {file_path.name}")

    with file_path.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError(f"CSV has no header: {file_path.name}")

        missing_fields = required_fields - set(reader.fieldnames)

        if missing_fields:
            raise ValueError(
                f"Missing columns in {file_path.name}: "
                f"{', '.join(sorted(missing_fields))}"
            )

        return list(reader)


def load_opening_stock():
    """Load and validate opening inventory balances."""

    records = read_csv_file(OPENING_FILE, OPENING_FIELDS)

    if not records:
        raise ValueError("Opening stock file contains no records.")

    inventory = {}

    for row_number, row in enumerate(records, start=2):

        item_code = (row["item_code"] or "").strip()
        item_name = (row["item_name"] or "").strip()

        if not item_code or not item_name:
            raise ValueError(
                f"Missing item code or name at row {row_number}."
            )

        if item_code in inventory:
            raise ValueError(f"Duplicate item code: {item_code}")

        try:
            opening_qty = int(row["opening_qty"])
        except (ValueError, TypeError):
            raise ValueError(
                f"Invalid opening quantity at row {row_number}."
            )

        if opening_qty < 0:
            raise ValueError(
                f"Negative opening quantity for {item_code}."
            )

        inventory[item_code] = {
            "item_name": item_name,
            "opening_qty": opening_qty,
            "stock_in": 0,
            "stock_out": 0,
            "closing_qty": opening_qty
        }

    return inventory


def load_transactions(inventory):
    """Read and validate all stock transactions."""

    records = read_csv_file(TRANSACTION_FILE, TRANSACTION_FIELDS)

    if not records:
        raise ValueError("Transaction file contains no records.")

    transactions = []
    transaction_ids = set()

    for row_number, row in enumerate(records, start=2):

        transaction_id = (row["transaction_id"] or "").strip()
        item_code = (row["item_code"] or "").strip()
        transaction_type = (row["transaction_type"] or "").strip()
        date_text = (row["transaction_date"] or "").strip()
        reference = (row["reference"] or "").strip()

        if not all([
            transaction_id,
            item_code,
            transaction_type,
            date_text,
            reference
        ]):
            raise ValueError(
                f"Missing required transaction data at row {row_number}."
            )

        if transaction_id in transaction_ids:
            raise ValueError(
                f"Duplicate transaction ID: {transaction_id}"
            )

        transaction_ids.add(transaction_id)

        if item_code not in inventory:
            raise ValueError(
                f"Unknown item code at row {row_number}: {item_code}"
            )

        if transaction_type not in VALID_TYPES:
            raise ValueError(
                f"Invalid transaction type: {transaction_type}"
            )

        try:
            transaction_date = date.fromisoformat(date_text)
        except ValueError:
            raise ValueError(
                f"Invalid date at row {row_number}. Use YYYY-MM-DD."
            )

        if transaction_date > REPORT_DATE:
            raise ValueError(
                f"Transaction date is after report date: {transaction_id}"
            )

        try:
            quantity = int(row["quantity"])
        except (ValueError, TypeError):
            raise ValueError(
                f"Invalid quantity at row {row_number}."
            )

        if quantity <= 0:
            raise ValueError(
                f"Quantity must be greater than zero: {transaction_id}"
            )

        transactions.append({
            "transaction_id": transaction_id,
            "transaction_date": transaction_date,
            "item_code": item_code,
            "transaction_type": transaction_type,
            "quantity": quantity
        })

    return transactions


def calculate_stock_movement(inventory, transactions):
    """Calculate stock-in, stock-out and closing balances."""

    # Process transactions in date order
    transactions.sort(key=lambda item: item["transaction_date"])

    for transaction in transactions:

        item = inventory[transaction["item_code"]]
        quantity = transaction["quantity"]

        if transaction["transaction_type"] == "Stock In":

            item["stock_in"] += quantity
            item["closing_qty"] += quantity

        else:

            if quantity > item["closing_qty"]:
                raise ValueError(
                    f"Insufficient stock for {transaction['item_code']} "
                    f"at transaction {transaction['transaction_id']}."
                )

            item["stock_out"] += quantity
            item["closing_qty"] -= quantity


def display_report(inventory, transactions):

    print("\nSTOCK-IN VS STOCK-OUT SUMMARY")
    print("=" * 90)
    print(f"Report Date: {REPORT_DATE}")
    print("-" * 90)

    print(
        f"{'Item Code':<12}"
        f"{'Item Name':<26}"
        f"{'Opening':>10}"
        f"{'Stock In':>10}"
        f"{'Stock Out':>12}"
        f"{'Closing':>10}"
    )

    print("-" * 90)

    total_opening = 0
    total_in = 0
    total_out = 0
    total_closing = 0

    for item_code, item in inventory.items():

        print(
            f"{item_code:<12}"
            f"{item['item_name']:<26}"
            f"{item['opening_qty']:>10}"
            f"{item['stock_in']:>10}"
            f"{item['stock_out']:>12}"
            f"{item['closing_qty']:>10}"
        )

        total_opening += item["opening_qty"]
        total_in += item["stock_in"]
        total_out += item["stock_out"]
        total_closing += item["closing_qty"]

    print("-" * 90)

    print(
        f"{'TOTAL':<38}"
        f"{total_opening:>10}"
        f"{total_in:>10}"
        f"{total_out:>12}"
        f"{total_closing:>10}"
    )

    print("\nMOVEMENT SUMMARY")
    print("-" * 45)

    print(f"Total transactions : {len(transactions)}")
    print(f"Total stock-in qty : {total_in}")
    print(f"Total stock-out qty: {total_out}")
    print(f"Net movement       : {total_in - total_out}")

    print("\nStock movement report completed successfully.")


def main():

    inventory = load_opening_stock()

    transactions = load_transactions(inventory)

    calculate_stock_movement(inventory, transactions)

    display_report(inventory, transactions)


if __name__ == "__main__":

    try:
        main()

    except (ValueError, OSError) as error:
        print(f"\nVALIDATION ERROR: {error}")
        raise SystemExit(1)
