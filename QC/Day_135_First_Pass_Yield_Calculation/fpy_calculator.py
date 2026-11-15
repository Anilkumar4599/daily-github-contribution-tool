
import csv
from pathlib import Path


def calculate_fpy(passed_first_time, total_inspected):
    """Calculate First-Pass Yield as a percentage."""

    if total_inspected <= 0:
        raise ValueError("Total inspected must be greater than zero.")

    if passed_first_time < 0 or passed_first_time > total_inspected:
        raise ValueError("Passed units must be between zero and total inspected.")

    return round((passed_first_time / total_inspected) * 100, 2)


def create_fpy_report(input_file, output_file):
    """Read QC data, calculate daily FPY and save a report."""

    daily_results = []
    total_inspected = 0
    total_passed_first_time = 0

    with open(input_file, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            inspected = int(row["units_inspected"])
            passed = int(row["passed_first_time"])

            fpy = calculate_fpy(passed, inspected)

            daily_results.append({
                "date": row["date"],
                "units_inspected": inspected,
                "passed_first_time": passed,
                "failed_first_pass": inspected - passed,
                "fpy_percent": fpy
            })

            total_inspected += inspected
            total_passed_first_time += passed

    if not daily_results:
        raise ValueError("No QC records found in the input file.")

    overall_fpy = calculate_fpy(
        total_passed_first_time,
        total_inspected
    )

    fieldnames = [
        "date",
        "units_inspected",
        "passed_first_time",
        "failed_first_pass",
        "fpy_percent"
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(daily_results)

    print("\nFIRST-PASS YIELD (FPY) REPORT")
    print("-" * 65)

    for result in daily_results:
        print(
            f"{result['date']} | "
            f"Inspected: {result['units_inspected']} | "
            f"Passed first time: {result['passed_first_time']} | "
            f"FPY: {result['fpy_percent']}%"
        )

    print("-" * 65)
    print(f"Total units inspected       : {total_inspected}")
    print(f"Total passed first time     : {total_passed_first_time}")
    print(f"Total failed first pass     : {total_inspected - total_passed_first_time}")
    print(f"Overall FPY                 : {overall_fpy}%")
    print(f"\nReport saved to: {output_file}")


if __name__ == "__main__":
    project_folder = Path(__file__).parent

    input_file = project_folder / "sample_fpy_data.csv"
    output_file = project_folder / "fpy_report.csv"

    create_fpy_report(input_file, output_file)
