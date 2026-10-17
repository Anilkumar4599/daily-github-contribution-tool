
import csv
from datetime import date, datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "shipment_data.csv"
OUTPUT_FILE = BASE_DIR / "daily_shipment_summary.csv"

# Fixed reporting date makes this training example reproducible.
REPORT_DATE = date(2026, 10, 17)

REQUIRED_COLUMNS = [
    "Shipment ID",
    "PO Number",
    "Vendor",
    "Destination",
    "Dispatch Date",
    "Expected Delivery Date",
    "Actual Delivery Date",
    "Status",
    "Transport Mode",
]

VALID_STATUSES = {"Delivered", "In Transit"}


def parse_date(value, column, row_number, required=True):
    """Validate a date in YYYY-MM-DD format."""
    value = value.strip()

    if not value:
        if required:
            raise ValueError(
                f"{column} is required at CSV row {row_number}."
            )
        return None

    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as error:
        raise ValueError(
            f"Invalid {column} at CSV row {row_number}: {value}. "
            "Use YYYY-MM-DD."
        ) from error


def load_shipments(filename):
    """Load and validate shipment records from a CSV file."""
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
        raise ValueError("CSV contains no shipment records.")

    seen_ids = set()

    for row_number, row in enumerate(rows, start=2):
        for column in REQUIRED_COLUMNS:
            if row.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at CSV row {row_number}."
                )
            row[column] = row[column].strip()

        shipment_id = row["Shipment ID"]
        if not shipment_id:
            raise ValueError(
                f"Shipment ID is blank at CSV row {row_number}."
            )
        if shipment_id in seen_ids:
            raise ValueError(f"Duplicate Shipment ID: {shipment_id}")
        seen_ids.add(shipment_id)

        for column in [
            "PO Number", "Vendor", "Destination", "Transport Mode"
        ]:
            if not row[column]:
                raise ValueError(
                    f"{column} is required at CSV row {row_number}."
                )

        dispatch = parse_date(
            row["Dispatch Date"], "Dispatch Date", row_number
        )
        expected = parse_date(
            row["Expected Delivery Date"],
            "Expected Delivery Date",
            row_number,
        )
        actual = parse_date(
            row["Actual Delivery Date"],
            "Actual Delivery Date",
            row_number,
            required=False,
        )

        if dispatch > expected:
            raise ValueError(
                f"Dispatch Date is after Expected Delivery Date "
                f"at CSV row {row_number}."
            )

        if actual and actual < dispatch:
            raise ValueError(
                f"Actual Delivery Date is before Dispatch Date "
                f"at CSV row {row_number}."
            )

        status = row["Status"].title()
        if status not in VALID_STATUSES:
            raise ValueError(
                f"Invalid Status at CSV row {row_number}. "
                "Use Delivered or In Transit."
            )

        if status == "Delivered" and actual is None:
            raise ValueError(
                f"Delivered shipment must have Actual Delivery Date "
                f"at CSV row {row_number}."
            )

        if status == "In Transit" and actual is not None:
            raise ValueError(
                f"In Transit shipment must not have Actual Delivery Date "
                f"at CSV row {row_number}."
            )

        if dispatch > REPORT_DATE:
            raise ValueError(
                f"Dispatch Date is after the reporting date "
                f"at CSV row {row_number}."
            )

        row["_dispatch"] = dispatch
        row["_expected"] = expected
        row["_actual"] = actual
        row["Status"] = status

    return rows


def analyze_shipments(shipments):
    """Calculate delivery performance and shipment delays."""
    report = []

    for row in shipments:
        expected = row["_expected"]
        actual = row["_actual"]
        status = row["Status"]

        if status == "Delivered":
            days_late = max(0, (actual - expected).days)
            performance = "Late" if days_late > 0 else "On Time"
            days_to_delivery = (actual - row["_dispatch"]).days
            attention = "No" if days_late == 0 else "Yes"
        else:
            days_to_delivery = ""
            if REPORT_DATE > expected:
                days_late = (REPORT_DATE - expected).days
                performance = "Delayed - In Transit"
                attention = "Yes"
            else:
                days_late = 0
                performance = "In Transit - Within Schedule"
                attention = "No"

        report.append({
            "Report Date": REPORT_DATE.isoformat(),
            "Shipment ID": row["Shipment ID"],
            "PO Number": row["PO Number"],
            "Vendor": row["Vendor"],
            "Destination": row["Destination"],
            "Dispatch Date": row["Dispatch Date"],
            "Expected Delivery Date": row["Expected Delivery Date"],
            "Actual Delivery Date": row["Actual Delivery Date"],
            "Status": status,
            "Transport Mode": row["Transport Mode"],
            "Delivery Performance": performance,
            "Days Late": days_late,
            "Days from Dispatch to Delivery": days_to_delivery,
            "Requires Follow-up": attention,
        })

    return report


def save_report(report, filename):
    """Save the shipment-level report to CSV."""
    if not report:
        raise ValueError("No shipment data available to report.")

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=list(report[0].keys()))
        writer.writeheader()
        writer.writerows(report)


def print_summary(report):
    """Print management-level shipment KPIs."""
    total = len(report)
    delivered = [r for r in report if r["Status"] == "Delivered"]
    in_transit = [r for r in report if r["Status"] == "In Transit"]
    on_time = [r for r in delivered if r["Delivery Performance"] == "On Time"]
    late_delivered = [
        r for r in delivered if r["Delivery Performance"] == "Late"
    ]
    delayed_transit = [
        r for r in report
        if r["Delivery Performance"] == "Delayed - In Transit"
    ]

    on_time_rate = (len(on_time) / len(delivered) * 100) if delivered else 0

    print("\n=== DAILY SHIPMENT SUMMARY ===")
    print(f"Report date: {REPORT_DATE.isoformat()}")
    print(f"Total shipments: {total}")
    print(f"Delivered: {len(delivered)}")
    print(f"In transit: {len(in_transit)}")
    print(f"Delivered on time: {len(on_time)}")
    print(f"Delivered late: {len(late_delivered)}")
    print(f"Delayed and still in transit: {len(delayed_transit)}")
    print(f"On-time delivery rate: {on_time_rate:.1f}%")

    print("\n=== SHIPMENTS REQUIRING FOLLOW-UP ===")
    flagged = [r for r in report if r["Requires Follow-up"] == "Yes"]

    if not flagged:
        print("No shipments require follow-up.")
    else:
        for row in flagged:
            print(
                f"{row['Shipment ID']} | {row['Vendor']} | "
                f"{row['Destination']} | {row['Delivery Performance']} | "
                f"Days late: {row['Days Late']}"
            )


def main():
    shipments = load_shipments(INPUT_FILE)
    report = analyze_shipments(shipments)
    save_report(report, OUTPUT_FILE)
    print_summary(report)
    print(f"\nDetailed report saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")
