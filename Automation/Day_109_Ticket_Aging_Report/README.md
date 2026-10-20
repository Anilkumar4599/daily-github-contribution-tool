

\# Day 109 — Ticket-Aging Report Automation



\## Objective

Calculate ticket age, group tickets into aging categories, identify overdue open tickets, and export a detailed CSV report.



\## Business use case

This tool helps QC and service managers identify aging defects and unresolved service issues that need follow-up.



\## Files

\- `ticket\_data.csv` — fictional sample ticket data

\- `ticket\_aging\_report.py` — report generation and validation

\- `ticket\_aging\_report.csv` — generated output

\- `invalid\_ticket\_data.csv` — duplicate-ticket validation test

\- `README.md` — project documentation



\## How to run

```bash

python ticket\_aging\_report.py

```



\## Aging rules

\- 0-2 days: recently opened

\- 3-5 days: approaching follow-up threshold

\- 6-10 days: overdue follow-up

\- Over 10 days: long-aging ticket

\- Closed tickets are labelled Closed and excluded from overdue follow-up.

\- An open ticket older than 5 days is flagged for follow-up.



\## Validation

\- Required columns must exist.

\- Ticket IDs must be nonblank and unique.

\- Priority and Status must use supported values.

\- Required fields cannot be blank.

\- Open Date must use YYYY-MM-DD.

\- Open Date cannot be after the report date.



\## Sample results

\- Total tickets: 8

\- Open/in-progress tickets: 7

\- Closed tickets: 1

\- Overdue open tickets: 4

\- Critical open tickets: 2



\## Assumptions and limitations

\- All data is fictional training data.

\- The report date is fixed at 2026-10-20 to make sample results reproducible.

\- Ticket age is calculated in calendar days.

\- The follow-up threshold is more than 5 days.

\- Priority and ticket age should both be considered by a manager; aging alone does not determine business severity.



\## Learning outcomes

CSV processing, date calculations, input validation, report generation, exception handling, and Git version control.



