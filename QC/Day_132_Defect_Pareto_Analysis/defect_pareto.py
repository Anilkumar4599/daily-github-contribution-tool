
import csv
from pathlib import Path

REQUIRED_COLUMNS = {"defect_category", "defect_count"}

REPORT_COLUMNS = [
    "defect_category",
    "defect_count",
    "cumulative_count",
    "cumulative_percentage",
]


def validate_defect_rows(rows):
    """Check that defect categories and counts are valid."""

    if not rows:
        raise ValueError("Input file has no defect records.")

    cleaned_rows = []
    seen_categories = set()

    for line_number, row in enumerate(rows, start=2):
        category = (row.get("defect_category") or "").strip()
        raw_count = (row.get("defect_count") or "").strip()

        if not category:
            raise ValueError(
                f"Row {line_number}: defect category cannot be blank."
            )

        if not raw_count:
            raise ValueError(
                f"Row {line_number}: defect count cannot be blank."
            )

        try:
            count = int(raw_count)
        except ValueError:
            raise ValueError(
                f"Row {line_number}: defect count must be a whole number."
            )

        if count <= 0:
            raise ValueError(
                f"Row {line_number}: defect count must be greater than zero."
            )

        category_key = category.casefold()

        if category_key in seen_categories:
            raise ValueError(
                f"Row {line_number}: duplicate category '{category}'."
            )

        seen_categories.add(category_key)

        cleaned_rows.append({
            "defect_category": category,
            "defect_count": count,
        })

    return cleaned_rows


def load_defects(file_path):
    """Read the CSV file and validate its contents."""

    with file_path.open("r", newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError("CSV file is missing its header.")

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing_columns))}"
            )

        rows = list(reader)

    return validate_defect_rows(rows)


def calculate_pareto(defects):
    """Sort defects and calculate cumulative counts and percentages."""

    if not defects:
        raise ValueError("No valid defect records to analyse.")

    total_defects = sum(item["defect_count"] for item in defects)

    if total_defects <= 0:
        raise ValueError("Total defect count must be greater than zero.")

    sorted_defects = sorted(
        defects,
        key=lambda item: (
            -item["defect_count"],
            item["defect_category"].casefold()
        )
    )

    cumulative_count = 0
    report = []

    for item in sorted_defects:
        cumulative_count += item["defect_count"]

        percentage = (cumulative_count / total_defects) * 100

        report.append({
            "defect_category": item["defect_category"],
            "defect_count": item["defect_count"],
            "cumulative_count": cumulative_count,
            "cumulative_percentage": round(percentage, 2),
        })

    return report


def write_report(report, output_path):
    """Save the Pareto results as a CSV report."""

    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=REPORT_COLUMNS
        )

        writer.writeheader()

        for item in report:
            output_row = item.copy()
            output_row["cumulative_percentage"] = (
                f"{item['cumulative_percentage']:.2f}"
            )
            writer.writerow(output_row)


def main():
    project_folder = Path(__file__).resolve().parent

    input_file = project_folder / "sample_defects.csv"
    output_file = project_folder / "pareto_report.csv"

    try:
        defects = load_defects(input_file)
        report = calculate_pareto(defects)
        write_report(report, output_file)

    except (OSError, ValueError, csv.Error) as error:
        print(f"ERROR: {error}")
        return 1

    total_defects = sum(item["defect_count"] for item in defects)

    print("\nDEFECT PARETO ANALYSIS")
    print("-" * 70)
    print(f"Total defects: {total_defects}\n")

    print(
        f"{'Defect Category':<28}"
        f"{'Count':>8}"
        f"{'Cumulative':>14}"
        f"{'Cumulative %':>16}"
    )

    print("-" * 70)

    for item in report:
        print(
            f"{item['defect_category']:<28}"
            f"{item['defect_count']:>8}"
            f"{item['cumulative_count']:>14}"
            f"{item['cumulative_percentage']:>15.2f}%"
        )

    top_three_count = sum(
        item["defect_count"] for item in report[:3]
    )

    top_three_percentage = (top_three_count / total_defects) * 100

    print("\n" + "-" * 70)
    print(
        f"Top 3 categories: {top_three_count} defects "
        f"({top_three_percentage:.2f}%)"
    )
    print(f"Report saved to: {output_file.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
