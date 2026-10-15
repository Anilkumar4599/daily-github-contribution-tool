import csv
from datetime import date
from pathlib import Path


REQUIRED_COLUMNS = [
    "Invoice Number",
    "Vendor",
    "PO Number",
    "Invoice Date",
    "Credit Days",
    "Invoice Amount",
    "Payment Status",
]


def load_credit_data(filename):
    """Read and validate invoice credit data."""

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
        raise ValueError("CSV contains no invoice records.")

    seen_invoices = set()

    for row_number, row in enumerate(rows, start=2):
        for column in REQUIRED_COLUMNS:
            if row.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at CSV row {row_number}."
                )
            row[column] = row[column].strip()

        invoice_number = row["Invoice Number"]

        if not invoice_number:
            raise ValueError(
                f"Invoice Number is blank at CSV row {row_number}."
            )

        if invoice_number in seen_invoices:
            raise ValueError(f"Duplicate invoice number: {invoice_number}")

        seen_invoices.add(invoice_number)

        if not row["Vendor"] or not row["PO Number"]:
            raise ValueError(
                f"Vendor and PO Number are required at row {row_number}."
            )

        try:
            invoice_date = date.fromisoformat(row["Invoice Date"])
            credit_days = int(row["Credit Days"])
            invoice_amount = float(row["Invoice Amount"])
        except ValueError as error:
            raise ValueError(
                f"Invalid date, credit days, or amount at row {row_number}."
            ) from error

        if credit_days < 0:
            raise ValueError(
                f"Credit Days cannot be negative at row {row_number}."
            )

        if invoice_amount < 0:
            raise ValueError(
                f"Invoice Amount cannot be negative at row {row_number}."
            )

        if invoice_date > date(2026, 10, 15):
            raise ValueError(
                f"Invoice Date is in the future at row {row_number}."
            )

        if row["Payment Status"].strip().lower() not in {
            "paid", "unpaid", "partially paid"
        }:
            raise ValueError(
                f"Invalid Payment Status at row {row_number}."
            )

    return rows


def build_credit_report(rows, reference_date):
    """Calculate due dates and flag overdue unpaid invoices."""

    report = []

    for row in rows:
        invoice_date = date.fromisoformat(row["Invoice Date"])
        credit_days = int(row["Credit Days"])
        invoice_amount = float(row["Invoice Amount"])
        payment_status = row["Payment Status"].strip().title()

        due_date = date.fromordinal(
            invoice_date.toordinal() + credit_days
        )

        days_overdue = max(0, (reference_date - due_date).days)

        if payment_status == "Paid":
            status = "Paid"
            days_overdue = 0
            priority = "No Follow-up"
        elif reference_date > due_date:
            status = "Overdue"
            priority = "High"
        elif reference_date == due_date:
            status = "Due Today"
            priority = "High"
        else:
            status = "Within Credit Period"
            priority = "Monitor"

        report.append({
            "Invoice Number": row["Invoice Number"],
            "Vendor": row["Vendor"],
            "PO Number": row["PO Number"],
            "Invoice Date": row["Invoice Date"],
            "Credit Days": credit_days,
            "Due Date": due_date.isoformat(),
            "Invoice Amount": f"{invoice_amount:.2f}",
            "Payment Status": payment_status,
            "Days Overdue": days_overdue,
            "Credit Status": status,
            "Follow-up Priority": priority,
        })

    return report


def save_report(report, filename):
    """Save the calculated credit report to a CSV file."""

    if not report:
        raise ValueError("No report records available.")

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=list(report[0].keys()))
        writer.writeheader()
        writer.writerows(report)


def print_summary(report):
    """Display the credit-time summary."""

    print("\n=== PROCUREMENT CREDIT-TIME REPORT ===")
    print(f"Total invoices: {len(report)}")

    overdue = [row for row in report if row["Credit Status"] == "Overdue"]
    due_today = [
        row for row in report if row["Credit Status"] == "Due Today"
    ]
    within_credit = [
        row for row in report
        if row["Credit Status"] == "Within Credit Period"
    ]
    paid = [row for row in report if row["Credit Status"] == "Paid"]

    print(f"Overdue invoices: {len(overdue)}")
    print(f"Due today: {len(due_today)}")
    print(f"Within credit period: {len(within_credit)}")
    print(f"Paid invoices: {len(paid)}")

    print("\nInvoice Details:")

    for row in report:
        print(
            f"{row['Invoice Number']} | {row['Vendor']} | "
            f"Due: {row['Due Date']} | "
            f"Status: {row['Credit Status']} | "
            f"Overdue: {row['Days Overdue']} day(s)"
        )


def main():
    # Fixed date makes sample output reproducible.
    reference_date = date(2026, 10, 15)

    rows = load_credit_data("credit_data.csv")
    report = build_credit_report(rows, reference_date)

    save_report(report, "credit_time_report.csv")
    print_summary(report)

    print("\nReport saved: credit_time_report.csv")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")