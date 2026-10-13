import csv
from datetime import date
from pathlib import Path


REQUIRED_COLUMNS = [
    "PO Number",
    "Vendor",
    "Vendor Email",
    "Item",
    "Expected Date",
    "Ordered Qty",
    "Received Qty",
]


def load_po_data(filename):
    """Read and validate purchase-order records."""

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

        missing_columns = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

        rows = list(reader)

    if not rows:
        raise ValueError("CSV contains no purchase-order records.")

    seen_po_numbers = set()

    for row_number, row in enumerate(rows, start=2):
        for column in REQUIRED_COLUMNS:
            if row.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at CSV row {row_number}."
                )
            row[column] = row[column].strip()

        po_number = row["PO Number"]

        if not po_number:
            raise ValueError(f"PO Number is blank at row {row_number}.")

        if po_number in seen_po_numbers:
            raise ValueError(f"Duplicate PO Number: {po_number}")

        seen_po_numbers.add(po_number)

        if not row["Vendor"] or not row["Item"]:
            raise ValueError(
                f"Vendor and Item are required at row {row_number}."
            )

        email = row["Vendor Email"]

        if (
            not email
            or email.count("@") != 1
            or " " in email
            or "." not in email.split("@")[1]
            or email.startswith("@")
            or email.endswith(".")
        ):
            raise ValueError(
                f"Invalid basic email format at row {row_number}: {email}"
            )

        try:
            expected_date = date.fromisoformat(row["Expected Date"])
            ordered_qty = int(row["Ordered Qty"])
            received_qty = int(row["Received Qty"])
        except ValueError as error:
            raise ValueError(
                f"Invalid date or quantity at row {row_number}."
            ) from error

        if ordered_qty <= 0:
            raise ValueError(
                f"Ordered Qty must be positive at row {row_number}."
            )

        if received_qty < 0 or received_qty > ordered_qty:
            raise ValueError(
                f"Received Qty must be between 0 and Ordered Qty "
                f"at row {row_number}."
            )

    return rows


def create_email_draft(row, reference_date):
    """Create a polite follow-up email for an overdue PO."""

    expected_date = date.fromisoformat(row["Expected Date"])
    ordered_qty = int(row["Ordered Qty"])
    received_qty = int(row["Received Qty"])
    pending_qty = ordered_qty - received_qty

    if pending_qty == 0:
        return None

    if expected_date >= reference_date:
        return None

    delay_days = (reference_date - expected_date).days

    subject = (
        f"Delivery Status Follow-up - PO {row['PO Number']}"
    )

    body = f"""Dear {row['Vendor']},

We are following up on the outstanding delivery against the following purchase order:

PO Number: {row['PO Number']}
Item: {row['Item']}
Ordered Quantity: {ordered_qty}
Received Quantity: {received_qty}
Pending Quantity: {pending_qty}
Expected Delivery Date: {row['Expected Date']}
Delay: {delay_days} day(s)

Please confirm the current dispatch/delivery status and your revised delivery date for the pending quantity.

Kindly share any relevant shipment details and inform us promptly if there are constraints affecting delivery.

Thank you for your support.

Best regards,
Procurement Team
"""

    return {
        "PO Number": row["PO Number"],
        "Vendor": row["Vendor"],
        "Vendor Email": row["Vendor Email"],
        "Pending Qty": pending_qty,
        "Delay Days": delay_days,
        "Email Subject": subject,
        "Email Body": body,
    }


def generate_drafts(rows, reference_date):
    """Generate drafts for overdue POs only."""

    drafts = []

    for row in rows:
        draft = create_email_draft(row, reference_date)

        if draft is not None:
            drafts.append(draft)

    return drafts


def save_drafts(drafts, filename):
    """Save email drafts to a CSV file."""

    columns = [
        "PO Number",
        "Vendor",
        "Vendor Email",
        "Pending Qty",
        "Delay Days",
        "Email Subject",
        "Email Body",
    ]

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(drafts)


def main():
    reference_date = date(2026, 10, 13)

    rows = load_po_data("vendor_po_data.csv")
    drafts = generate_drafts(rows, reference_date)

    save_drafts(drafts, "vendor_email_drafts.csv")

    print("=== VENDOR FOLLOW-UP EMAIL DRAFT REPORT ===")
    print(f"PO records reviewed: {len(rows)}")
    print(f"Email drafts generated: {len(drafts)}")

    for draft in drafts:
        print(
            f"{draft['PO Number']} | {draft['Vendor']} | "
            f"Pending: {draft['Pending Qty']} | "
            f"Delay: {draft['Delay Days']} days"
        )

    print("\nDraft report saved: vendor_email_drafts.csv")
    print("No emails have been sent.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")