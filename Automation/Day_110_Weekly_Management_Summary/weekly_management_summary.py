
import csv
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "weekly_ticket_data.csv"
TEAM_REPORT_FILE = BASE_DIR / "weekly_team_summary.csv"
TEXT_REPORT_FILE = BASE_DIR / "weekly_management_summary.txt"

# Reporting period: 14 October to 20 October 2026.
WEEK_START = date(2026, 10, 14)
WEEK_END = date(2026, 10, 20)

# The date used to calculate ticket age.
REPORT_DATE = date(2026, 10, 21)

# An unresolved ticket older than 5 days needs follow-up.
OVERDUE_AFTER_DAYS = 5

REQUIRED_COLUMNS = [
    "Ticket ID",
    "Priority",
    "Status",
    "Assigned Team",
    "Created Date",
]

VALID_PRIORITIES = {"Critical", "High", "Medium", "Low"}
VALID_STATUSES = {"Open", "In Progress", "Closed"}


def load_tickets(filename):
    """Read the CSV file and validate its data."""

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

        # Validate that every required column has a value.
        for column in REQUIRED_COLUMNS:
            if ticket.get(column) is None:
                raise ValueError(
                    f"Incorrect number of fields at row {row_number}."
                )

            ticket[column] = ticket[column].strip()

        # Check ticket ID.
        ticket_id = ticket["Ticket ID"]

        if not ticket_id:
            raise ValueError(
                f"Ticket ID is blank at row {row_number}."
            )

        if ticket_id in seen_ids:
            raise ValueError(f"Duplicate Ticket ID: {ticket_id}")

        seen_ids.add(ticket_id)

        # Check required text fields.
        for column in [
            "Priority", "Status", "Assigned Team", "Created Date"
        ]:
            if not ticket[column]:
                raise ValueError(
                    f"{column} is required at row {row_number}."
                )

        # Validate priority.
        if ticket["Priority"] not in VALID_PRIORITIES:
            raise ValueError(
                f"Invalid Priority at row {row_number}: "
                f"{ticket['Priority']}"
            )

        # Validate status.
        if ticket["Status"] not in VALID_STATUSES:
            raise ValueError(
                f"Invalid Status at row {row_number}: "
                f"{ticket['Status']}"
            )

        # Validate the created date.
        try:
            created_date = datetime.strptime(
                ticket["Created Date"], "%Y-%m-%d"
            ).date()
        except ValueError as error:
            raise ValueError(
                f"Invalid Created Date at row {row_number}. "
                "Use YYYY-MM-DD."
            ) from error

        if created_date > REPORT_DATE:
            raise ValueError(
                f"Created Date cannot be after the report date "
                f"at row {row_number}."
            )

        ticket["_created_date"] = created_date

    return tickets


def select_weekly_tickets(tickets):
    """Select tickets created during the reporting week."""

    return [
        ticket for ticket in tickets
        if WEEK_START <= ticket["_created_date"] <= WEEK_END
    ]


def calculate_ticket_age(ticket):
    """Calculate ticket age in calendar days."""

    return (REPORT_DATE - ticket["_created_date"]).days


def build_team_summary(weekly_tickets):
    """Calculate ticket counts and aging metrics for each team."""

    teams = defaultdict(
        lambda: {
            "Total Tickets": 0,
            "Open": 0,
            "In Progress": 0,
            "Closed": 0,
            "Critical Open": 0,
            "Overdue Open": 0,
        }
    )

    for ticket in weekly_tickets:
        team = teams[ticket["Assigned Team"]]
        status = ticket["Status"]

        # Count tickets by status.
        team["Total Tickets"] += 1
        team[status] += 1

        # Count unresolved critical tickets.
        if (
            ticket["Priority"] == "Critical"
            and status != "Closed"
        ):
            team["Critical Open"] += 1

        # Count unresolved tickets older than the threshold.
        age_days = calculate_ticket_age(ticket)

        if status != "Closed" and age_days > OVERDUE_AFTER_DAYS:
            team["Overdue Open"] += 1

    return [
        {"Assigned Team": team_name, **values}
        for team_name, values in sorted(teams.items())
    ]


def save_team_report(team_summary):
    """Save team-wise metrics to a CSV file."""

    if not team_summary:
        raise ValueError("No team summary data available.")

    with TEAM_REPORT_FILE.open(
        "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=list(team_summary[0].keys())
        )
        writer.writeheader()
        writer.writerows(team_summary)


def save_management_report(
    weekly_tickets, team_summary, all_tickets
):
    """Generate and save the management summary."""

    total = len(weekly_tickets)

    open_count = sum(
        ticket["Status"] == "Open"
        for ticket in weekly_tickets
    )

    progress_count = sum(
        ticket["Status"] == "In Progress"
        for ticket in weekly_tickets
    )

    closed_count = sum(
        ticket["Status"] == "Closed"
        for ticket in weekly_tickets
    )

    critical_open = sum(
        ticket["Priority"] == "Critical"
        and ticket["Status"] != "Closed"
        for ticket in weekly_tickets
    )

    overdue_tickets = [
        ticket for ticket in weekly_tickets
        if ticket["Status"] != "Closed"
        and calculate_ticket_age(ticket) > OVERDUE_AFTER_DAYS
    ]

    outside_week = len(all_tickets) - total

    lines = [
        "WEEKLY MANAGEMENT SUMMARY",
        "=" * 30,
        f"Reporting period: {WEEK_START} to {WEEK_END}",
        f"Report generated for: {REPORT_DATE}",
        "",
        "OVERALL KPIs",
        f"Tickets created during the week: {total}",
        f"Open tickets: {open_count}",
        f"In-progress tickets: {progress_count}",
        f"Closed tickets: {closed_count}",
        f"Critical open tickets: {critical_open}",
        (
            f"Overdue open tickets "
            f"(> {OVERDUE_AFTER_DAYS} days): "
            f"{len(overdue_tickets)}"
        ),
        f"Records outside reporting week: {outside_week}",
        "",
        "TEAM-WISE SUMMARY",
    ]

    for team in team_summary:
        lines.append(
            f"{team['Assigned Team']}: "
            f"Total={team['Total Tickets']}, "
            f"Open={team['Open']}, "
            f"In Progress={team['In Progress']}, "
            f"Closed={team['Closed']}, "
            f"Critical Open={team['Critical Open']}, "
            f"Overdue Open={team['Overdue Open']}"
        )

    lines.extend([
        "",
        "OVERDUE TICKETS REQUIRING FOLLOW-UP"
    ])

    if overdue_tickets:
        for ticket in sorted(
            overdue_tickets,
            key=lambda item: (
                item["Priority"] != "Critical",
                -calculate_ticket_age(item)
            )
        ):
            age = calculate_ticket_age(ticket)

            lines.append(
                f"{ticket['Ticket ID']} | "
                f"{ticket['Priority']} | "
                f"{age} days | "
                f"{ticket['Status']} | "
                f"Team: {ticket['Assigned Team']}"
            )
    else:
        lines.append("No overdue tickets found.")

    report_text = "\n".join(lines) + "\n"

    TEXT_REPORT_FILE.write_text(
        report_text,
        encoding="utf-8"
    )

    print("\n" + report_text)
    print(f"Team CSV saved: {TEAM_REPORT_FILE.name}")
    print(f"Text report saved: {TEXT_REPORT_FILE.name}")


def main():
    """Run the complete weekly reporting process."""

    all_tickets = load_tickets(INPUT_FILE)

    weekly_tickets = select_weekly_tickets(all_tickets)

    if not weekly_tickets:
        raise ValueError(
            "No tickets found in the selected reporting week."
        )

    team_summary = build_team_summary(weekly_tickets)

    save_team_report(team_summary)

    save_management_report(
        weekly_tickets,
        team_summary,
        all_tickets
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")
