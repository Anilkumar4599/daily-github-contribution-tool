
import csv
from collections import defaultdict
from pathlib import Path


def build_recurring_tracker(records, threshold=2):
    """Group defects by device and category and identify recurrence."""

    if threshold < 1:
        raise ValueError("Threshold must be at least 1.")

    grouped = defaultdict(list)

    for record in records:
        device = record["device_name"].strip()
        category = record["defect_category"].strip()
        severity = record["severity"].strip()
        date = record["date"].strip()

        if not device or not category or not severity or not date:
            raise ValueError("Defect records must not contain blank fields.")

        key = (device, category)
        grouped[key].append({
            "date": date,
            "severity": severity
        })

    report = []

    for (device, category), incidents in grouped.items():
        dates = sorted(item["date"] for item in incidents)
        severities = {item["severity"] for item in incidents}

        if len(severities) > 1:
            raise ValueError(
                f"Inconsistent severity for {device} - {category}"
            )

        count = len(incidents)

        report.append({
            "device_name": device,
            "defect_category": category,
            "severity": incidents[0]["severity"],
            "occurrence_count": count,
            "first_reported": dates[0],
            "last_reported": dates[-1],
            "status": "Recurring" if count >= threshold else "Not Recurring"
        })

    report.sort(
        key=lambda item: (
            -item["occurrence_count"],
            item["device_name"],
            item["defect_category"]
        )
    )

    return report


def read_defect_data(input_file):
    """Read defect incidents from a CSV file."""

    with open(input_file, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        required_fields = {
            "date", "device_name", "defect_category", "severity"
        }

        if not required_fields.issubset(set(reader.fieldnames or [])):
            raise ValueError("Input CSV is missing required columns.")

        return list(reader)


def save_report(report, output_file):
    """Save the recurring-defect tracker to CSV."""

    fields = [
        "device_name",
        "defect_category",
        "severity",
        "occurrence_count",
        "first_reported",
        "last_reported",
        "status"
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(report)


def main():
    folder = Path(__file__).parent
    input_file = folder / "sample_defects.csv"
    output_file = folder / "recurring_defect_report.csv"

    records = read_defect_data(input_file)
    report = build_recurring_tracker(records)

    save_report(report, output_file)

    recurring_count = sum(
        1 for item in report if item["status"] == "Recurring"
    )

    recurring_incidents = sum(
        item["occurrence_count"]
        for item in report
        if item["status"] == "Recurring"
    )

    print("\nRECURRING DEFECT TRACKER")
    print("-" * 75)

    for item in report:
        print(
            f"{item['device_name']} | "
            f"{item['defect_category']} | "
            f"Occurrences: {item['occurrence_count']} | "
            f"Status: {item['status']}"
        )

    print("-" * 75)
    print(f"Total defect incidents       : {len(records)}")
    print(f"Unique device/defect groups  : {len(report)}")
    print(f"Recurring defect groups      : {recurring_count}")
    print(f"Incidents in recurring groups: {recurring_incidents}")
    print(f"\nReport saved to: {output_file}")


if __name__ == "__main__":
    main()
