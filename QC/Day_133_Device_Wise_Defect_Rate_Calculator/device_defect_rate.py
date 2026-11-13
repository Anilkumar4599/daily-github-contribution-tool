
import csv
from pathlib import Path

INPUT_FILE = Path(__file__).with_name("sample_device_data.csv")
OUTPUT_FILE = Path(__file__).with_name("device_defect_rate_report.csv")

REQUIRED_COLUMNS = {
    "device_name",
    "units_inspected",
    "defective_units"
}


def parse_integer(value, field_name, row_number, allow_zero=True):
    """Convert a value into an integer and validate its range."""

    if value is None or not str(value).strip():
        raise ValueError(
            f"Row {row_number}: {field_name} cannot be blank."
        )

    try:
        number = int(str(value).strip())
    except ValueError:
        raise ValueError(
            f"Row {row_number}: {field_name} must be a whole number."
        )

    if allow_zero and number < 0:
        raise ValueError(
            f"Row {row_number}: {field_name} cannot be negative."
        )

    if not allow_zero and number <= 0:
        raise ValueError(
            f"Row {row_number}: {field_name} must be greater than zero."
        )

    return number


def load_device_data(file_path):
    """Read device inspection data from the CSV file."""

    with open(file_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("Input CSV is empty or has no header.")

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            raise ValueError(
                "Missing required columns: "
                + ", ".join(sorted(missing_columns))
            )

        return list(reader)


def validate_device_rows(rows):
    """Validate device names and inspection quantities."""

    if not rows:
        raise ValueError("No device records found in the input file.")

    validated_rows = []
    seen_devices = set()

    for row_number, row in enumerate(rows, start=2):
        device_name = str(row.get("device_name") or "").strip()

        if not device_name:
            raise ValueError(
                f"Row {row_number}: Device name cannot be blank."
            )

        device_key = device_name.casefold()

        if device_key in seen_devices:
            raise ValueError(
                f"Row {row_number}: Duplicate device name: {device_name}."
            )

        seen_devices.add(device_key)

        units_inspected = parse_integer(
            row.get("units_inspected"),
            "units_inspected",
            row_number,
            allow_zero=False
        )

        defective_units = parse_integer(
            row.get("defective_units"),
            "defective_units",
            row_number,
            allow_zero=True
        )

        if defective_units > units_inspected:
            raise ValueError(
                f"Row {row_number}: Defective units cannot exceed "
                "units inspected."
            )

        validated_rows.append({
            "device_name": device_name,
            "units_inspected": units_inspected,
            "defective_units": defective_units
        })

    return validated_rows


def calculate_device_defect_rates(rows):
    """Calculate defect rates and good units for each device."""

    validated_rows = validate_device_rows(rows)
    report = []

    for row in validated_rows:
        inspected = row["units_inspected"]
        defective = row["defective_units"]

        good_units = inspected - defective
        defect_rate = (defective / inspected) * 100

        report.append({
            "device_name": row["device_name"],
            "units_inspected": inspected,
            "defective_units": defective,
            "good_units": good_units,
            "defect_rate_percent": defect_rate
        })

    return sorted(
        report,
        key=lambda item: (
            -item["defect_rate_percent"],
            item["device_name"].casefold()
        )
    )


def write_report(report, output_file):
    """Save the calculated results into a CSV report."""

    columns = [
        "device_name",
        "units_inspected",
        "defective_units",
        "good_units",
        "defect_rate_percent"
    ]

    with open(output_file, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        for row in report:
            output_row = row.copy()
            output_row["defect_rate_percent"] = (
                f"{row['defect_rate_percent']:.2f}"
            )
            writer.writerow(output_row)


def main():
    try:
        raw_data = load_device_data(INPUT_FILE)
        report = calculate_device_defect_rates(raw_data)

        write_report(report, OUTPUT_FILE)

    except (OSError, ValueError) as error:
        raise SystemExit(f"ERROR: {error}")

    total_devices = len(report)
    total_inspected = sum(row["units_inspected"] for row in report)
    total_defective = sum(row["defective_units"] for row in report)
    total_good = total_inspected - total_defective

    overall_rate = (total_defective / total_inspected) * 100
    highest = report[0]

    print("\nDEVICE-WISE DEFECT RATE ANALYSIS")
    print("-" * 85)
    print(f"Total devices analysed : {total_devices}")
    print(f"Total units inspected : {total_inspected}")
    print(f"Total defective units : {total_defective}")
    print(f"Total good units      : {total_good}")
    print(f"Overall defect rate   : {overall_rate:.2f}%")

    print("\n" + "-" * 85)
    print(
        f"{'Device Name':<22}"
        f"{'Inspected':>12}"
        f"{'Defective':>12}"
        f"{'Good':>10}"
        f"{'Defect Rate':>15}"
    )
    print("-" * 85)

    for row in report:
        print(
            f"{row['device_name']:<22}"
            f"{row['units_inspected']:>12}"
            f"{row['defective_units']:>12}"
            f"{row['good_units']:>10}"
            f"{row['defect_rate_percent']:>14.2f}%"
        )

    print("\n" + "-" * 85)
    print(
        f"Highest defect rate: {highest['device_name']} "
        f"({highest['defect_rate_percent']:.2f}%)"
    )
    print(f"Report saved to: {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
