
import csv
from datetime import date
from pathlib import Path

# Report period
START_DATE = date(2026, 11, 1)
END_DATE = date(2026, 11, 24)

CSV_FILE = Path(__file__).with_name(
    "stock_issue_transactions.csv"
)

REQUIRED_FIELDS = {
    "issue_id",
    "issue_date",
    "item_code",
    "item_name",
    "issued_qty",
    "project"
}


def load_consumption_data():
    """Read and validate stock issue transactions."""

    if not CSV_FILE.exists():
        raise ValueError("Stock issue CSV file not found.")

    with CSV_FILE.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file has no header.")

        missing_fields = REQUIRED_FIELDS - set(reader.fieldnames)

        if missing_fields:
            raise ValueError(
                f"Missing CSV columns: {', '.join(sorted(missing_fields))}"
            )

        records = list(reader)

    if not records:
        raise ValueError("No stock issue records found.")

    return records


def generate_report(records):
    """Validate transactions and calculate item-wise consumption."""

    summary = {}
    issue_ids = set()

    for row_number, row in enumerate(records, start=2):

        issue_id = (row["issue_id"] or "").strip()
        issue_date_text = (row["issue_date"] or "").strip()
        item_code = (row["item_code"] or "").strip()
        item_name = (row["item_name"] or "").strip()
        project = (row["project"] or "").strip()

        if not all([
            issue_id,
            issue_date_text,
            item_code,
            item_name,
            project,
            row["issued_qty"]
        ]):
            raise ValueError(
                f"Missing required data at CSV row {row_number}."
            )

        if issue_id in issue_ids:
            raise ValueError(f"Duplicate issue ID: {issue_id}")

        issue_ids.add(issue_id)

        try:
            issue_date = date.fromisoformat(issue_date_text)
        except ValueError:
            raise ValueError(
                f"Invalid date at row {row_number}. Use YYYY-MM-DD."
            )

        if not START_DATE <= issue_date <= END_DATE:
            raise ValueError(
                f"Issue date outside report period: {issue_id}"
            )

        try:
            quantity = int(row["issued_qty"])
        except (ValueError, TypeError):
            raise ValueError(
                f"Invalid issue quantity at row {row_number}."
            )

        if quantity <= 0:
            raise ValueError(
                f"Issue quantity must be positive: {issue_id}"
            )

        if item_code not in summary:
            summary[item_code] = {
                "item_name": item_name,
                "issue_count": 0,
                "total_qty": 0
            }

        elif summary[item_code]["item_name"] != item_name:
            raise ValueError(
                f"Inconsistent item name for item code: {item_code}"
            )

        summary[item_code]["issue_count"] += 1
        summary[item_code]["total_qty"] += quantity

    return summary, len(records)


def display_report(summary, transaction_count):

    print("\nITEM-WISE CONSUMPTION REPORT")
    print("=" * 85)

    print(f"Report Period: {START_DATE} to {END_DATE}")

    print("-" * 85)

    print(
        f"{'Item Code':<12}"
        f"{'Item Name':<29}"
        f"{'Issues':>10}"
        f"{'Total Qty':>13}"
        f"{'Avg/Issue':>13}"
    )

    print("-" * 85)

    grand_total = 0
    total_issues = 0

    for item_code in sorted(summary):

        item = summary[item_code]

        issue_count = item["issue_count"]
        total_qty = item["total_qty"]

        average_qty = total_qty / issue_count

        print(
            f"{item_code:<12}"
            f"{item['item_name']:<29}"
            f"{issue_count:>10}"
            f"{total_qty:>13}"
            f"{average_qty:>13.2f}"
        )

        grand_total += total_qty
        total_issues += issue_count

    overall_average = grand_total / total_issues

    print("-" * 85)

    print(
        f"{'TOTAL':<41}"
        f"{total_issues:>10}"
        f"{grand_total:>13}"
        f"{overall_average:>13.2f}"
    )

    print("\nCONSUMPTION SUMMARY")
    print("-" * 45)

    print(f"Total item types       : {len(summary)}")
    print(f"Total issue records    : {transaction_count}")
    print(f"Total consumed quantity: {grand_total}")
    print(f"Average per transaction: {overall_average:.2f}")

    print("\nItem-wise consumption report completed successfully.")


def main():

    records = load_consumption_data()

    summary, transaction_count = generate_report(records)

    display_report(summary, transaction_count)


if __name__ == "__main__":

    try:
        main()

    except (ValueError, OSError) as error:
        print(f"\nVALIDATION ERROR: {error}")
        raise SystemExit(1)
