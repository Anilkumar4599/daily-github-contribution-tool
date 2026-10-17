# Day 106 — Daily Shipment Summary Automation

## Objective
Generate a daily shipment performance report from CSV data using Python.

## Business use case
Identify late deliveries, overdue shipments, in-transit shipments, and vendors requiring follow-up.

## Files
- shipment_data.csv: sample input records
- shipment_summary.py: validation and reporting automation
- daily_shipment_summary.csv: generated report
- invalid_shipment_data.csv: deliberately invalid test record
- README.md: documentation

## How to run
python shipment_summary.py

## Sample results
- Reporting date: 2026-10-17
- Total shipments: 8
- Delivered: 4
- In transit: 4
- Delivered on time: 3
- Delivered late: 1
- Delayed and still in transit: 3
- On-time delivery rate: 75.0%

## KPI assumptions
- The reporting date is fixed at 2026-10-17 for repeatable testing.
- Dates use YYYY-MM-DD format.
- On-time delivery rate is calculated using delivered shipments only.
- A delivery on the expected date counts as on time.
- In-transit shipments are overdue only when the expected date is before the report date.
- Calendar days are used; weekends and holidays are not excluded.
- The sample data is illustrative and does not represent actual company shipments.

## Validation
The program checks required columns, duplicate shipment IDs, date formats, date sequence, status values, and consistency between delivery status and actual delivery date.

## Learning outcomes
CSV processing, date calculations, KPI reporting, data validation, error handling, and GitHub version control.
