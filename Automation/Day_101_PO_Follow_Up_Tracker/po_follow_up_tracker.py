import csv
from datetime import date
from pathlib import Path


REQUIRED_COLUMNS = [
    "PO Number",
    "Vendor",
    "Item",
    "PO Date",
    "Expected Date",
    "Ordered Qty",
    "Received Qty",
]


def load_po_data(filename):
    """Read and validate purchase-order data from a CSV file."""

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
        raise ValueError("CSV contains no purchase-order records.")

    seen_po_numbers = set()

    for row_number, row in enumerate(rows, start=2):
        po_number = (row.get("PO Number") or "").strip()

        if not po_number:
            raise ValueError(f"PO Number is blank at CSV row {row_number}.")

        if po_number in seen_po_numbers:
            raise ValueError(f"Duplicate PO Number: {po_number}")

        seen_po_numbers.add(po_number)

        for column in REQUIRED_COLUMNS:
            if row.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at CSV row {row_number}."
                )

            row[column] = row[column].strip()

        try:
            po_date = date.fromisoformat(row["PO Date"])
            expected_date = date.fromisoformat(row["Expected Date"])
            ordered_qty = int(row["Ordered Qty"])
            received_qty = int(row["Received Qty"])
        except ValueError as error:
            raise ValueError(
                f"Invalid date or quantity at CSV row {row_number}."
            ) from error

        if not row["Vendor"] or not row["Item"]:
            raise ValueError(
                f"Vendor and Item are required at CSV row {row_number}."
            )

        if ordered_qty <= 0:
            raise ValueError(
                f"Ordered Qty must be positive at CSV row {row_number}."
            )

        if received_qty < 0 or received_qty > ordered_qty:
            raise ValueError(
                f"Received Qty must be between 0 and Ordered Qty "
                f"at CSV row {row_number}."
            )

        if expected_date < po_date:
            raise ValueError(
                f"Expected Date is before PO Date at CSV row {row_number}."
            )

    return rows


def build_tracker(rows, as_of_date):
    """Calculate pending quantities, delay days, and follow-up priorities."""

    tracker = []

    for row in rows:
        ordered_qty = int(row["Ordered Qty"])
        received_qty = int(row["Received Qty"])
        expected_date = date.fromisoformat(row["Expected Date"])

        pending_qty = ordered_qty - received_qty

        if pending_qty == 0:
            status = "Completed"
            priority = "No Follow-up"
            delay_days = 0
        elif expected_date < as_of_date:
            status = "Overdue"
            priority = "High"
            delay_days = (as_of_date - expected_date).days
        elif expected_date == as_of_date:
            status = "Due Today"
            priority = "High"
            delay_days = 0
        else:
            status = "Pending"
            priority = "Monitor"
            delay_days = 0

        tracker.append({
            "PO Number": row["PO Number"],
            "Vendor": row["Vendor"],
            "Item": row["Item"],
            "Ordered Qty": ordered_qty,
            "Received Qty": received_qty,
            "Pending Qty": pending_qty,
            "Expected Date": row["Expected Date"],
            "Delay Days": delay_days,
            "Status": status,
            "Follow-up Priority": priority,
        })

    return tracker


def save_tracker(tracker, filename):
    """Save the follow-up tracker as a CSV report."""

    if not tracker:
        raise ValueError("No tracker records available to save.")

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(tracker[0].keys()))
        writer.writeheader()
        writer.writerows(tracker)


def print_summary(tracker):
    """Print a concise management summary."""

    print("\n=== PURCHASE-ORDER FOLLOW-UP TRACKER ===")
    print(f"Total POs: {len(tracker)}")
    print(f"Pending quantity: {sum(row['Pending Qty'] for row in tracker)}")

    for priority in ["High", "Monitor", "No Follow-up"]:
        count = sum(
            1 for row in tracker
            if row["Follow-up Priority"] == priority
        )
        print(f"{priority} priority: {count}")

    print("\nPO Details:")

    for row in tracker:
        print(
            f"{row['PO Number']} | {row['Vendor']} | "
            f"Pending: {row['Pending Qty']} | "
            f"Status: {row['Status']} | "
            f"Priority: {row['Follow-up Priority']} | "
            f"Delay: {row['Delay Days']} days"
        )


if __name__ == "__main__":
    try:
        # Fixed reference date makes sample results reproducible.
        reference_date = date(2026, 10, 12)

        source_file = "sample_po_data.csv"
        output_file = "po_follow_up_report.csv"

        purchase_orders = load_po_data(source_file)
        tracker = build_tracker(purchase_orders, reference_date)

        save_tracker(tracker, output_file)
        print_summary(tracker)

        print(f"\nReport saved to: {output_file}")

    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")