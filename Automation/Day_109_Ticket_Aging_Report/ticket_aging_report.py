
import csv
from datetime import date, datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "ticket_data.csv"
OUTPUT_FILE = BASE_DIR / "ticket_aging_report.csv"

# Fixed report date makes the sample output reproducible.
# Change this date when practicing with another dataset.
REPORT_DATE = date(2026, 10, 20)

REQUIRED_COLUMNS = [
    "Ticket ID",
    "Ticket Title",
    "Priority",
    "Status",
    "Open Date",
    "Assigned Team",
]

VALID_PRIORITIES = {"Critical", "High", "Medium", "Low"}
VALID_STATUSES = {"Open", "In Progress", "Closed"}


def load_tickets(filename):
    """Read tickets and validate required data."""

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

        tickets = list(reader)

    if not tickets:
        raise ValueError("CSV contains no ticket records.")

    seen_ids = set()

    for row_number, ticket in enumerate(tickets, start=2):
        for column in REQUIRED_COLUMNS:
            if ticket.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at row {row_number}."
                )
            ticket[column] = ticket[column].strip()

        ticket_id = ticket["Ticket ID"]

        if not ticket_id:
            raise ValueError(f"Ticket ID is blank at row {row_number}.")

        if ticket_id in seen_ids:
            raise ValueError(f"Duplicate Ticket ID: {ticket_id}")

        seen_ids.add(ticket_id)

        for column in [
            "Ticket Title", "Priority", "Status", "Open Date", "Assigned Team"
        ]:
            if not ticket[column]:
                raise ValueError(
                    f"{column} is required at row {row_number}."
                )

        if ticket["Priority"] not in VALID_PRIORITIES:
            raise ValueError(
                f"Invalid Priority at row {row_number}: "
                f"{ticket['Priority']}"
            )

        if ticket["Status"] not in VALID_STATUSES:
            raise ValueError(
                f"Invalid Status at row {row_number}: "
                f"{ticket['Status']}"
            )

        try:
            opened = datetime.strptime(
                ticket["Open Date"], "%Y-%m-%d"
            ).date()
        except ValueError as error:
            raise ValueError(
                f"Invalid Open Date at row {row_number}. "
                "Use YYYY-MM-DD."
            ) from error

        if opened > REPORT_DATE:
            raise ValueError(
                f"Open Date cannot be after the report date "
                f"at row {row_number}."
            )

        ticket["_opened_date"] = opened

    return tickets


def calculate_aging(tickets):
    """Calculate ticket age and assign an aging category."""

    report = []

    for ticket in tickets:
        age_days = (REPORT_DATE - ticket["_opened_date"]).days
        status = ticket["Status"]

        if status == "Closed":
            category = "Closed"
        elif age_days <= 2:
            category = "0-2 Days"
        elif age_days <= 5:
            category = "3-5 Days"
        elif age_days <= 10:
            category = "6-10 Days"
        else:
            category = "Over 10 Days"

        # Closed tickets are excluded from overdue follow-up.
        overdue = (
            status != "Closed"
            and age_days > 5
        )

        report.append({
            "Ticket ID": ticket["Ticket ID"],
            "Ticket Title": ticket["Ticket Title"],
            "Priority": ticket["Priority"],
            "Status": status,
            "Open Date": ticket["Open Date"],
            "Age Days": age_days,
            "Aging Category": category,
            "Overdue Follow-up": "Yes" if overdue else "No",
            "Assigned Team": ticket["Assigned Team"],
        })

    return report


def save_report(report, filename):
    """Save detailed ticket-aging results to CSV."""

    if not report:
        raise ValueError("No report data available.")

    fieldnames = list(report[0].keys())

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report)


def print_summary(report):
    """Print management-level aging statistics."""

    total = len(report)
    open_tickets = [
        row for row in report if row["Status"] != "Closed"
    ]
    closed_count = sum(
        row["Status"] == "Closed" for row in report
    )
    overdue = [
        row for row in report
        if row["Overdue Follow-up"] == "Yes"
    ]
    critical_open = [
        row for row in open_tickets
        if row["Priority"] == "Critical"
    ]

    print("\n=== TICKET AGING SUMMARY ===")
    print(f"Report date: {REPORT_DATE}")
    print(f"Total tickets: {total}")
    print(f"Open / in-progress tickets: {len(open_tickets)}")
    print(f"Closed tickets: {closed_count}")
    print(f"Overdue open tickets (>5 days): {len(overdue)}")
    print(f"Critical open tickets: {len(critical_open)}")

    print("\n=== TICKETS REQUIRING FOLLOW-UP ===")

    if not overdue:
        print("No overdue tickets found.")
    else:
        for row in sorted(
            overdue,
            key=lambda item: (
                item["Priority"] != "Critical",
                item["Age Days"] * -1
            )
        ):
            print(
                f"{row['Ticket ID']} | {row['Priority']} | "
                f"{row['Age Days']} days | {row['Status']} | "
                f"{row['Ticket Title']} | Team: {row['Assigned Team']}"
            )


def main():
    tickets = load_tickets(INPUT_FILE)
    report = calculate_aging(tickets)
    save_report(report, OUTPUT_FILE)
    print_summary(report)
    print(f"\nDetailed report saved: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")
