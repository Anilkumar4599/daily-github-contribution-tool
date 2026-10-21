

\# Day 110 — Weekly Management Summary Generator



\## Objective

Generate a weekly management summary from ticket CSV data using Python.



\## Business use case

Helps QC and service managers monitor ticket volumes, open issues, critical tickets, overdue work, and team-level performance.



\## Project files

\- `weekly\_ticket\_data.csv` — sample ticket input

\- `weekly\_management\_summary.py` — processing and validation

\- `weekly\_team\_summary.csv` — team-level KPI report

\- `weekly\_management\_summary.txt` — management summary

\- `invalid\_ticket\_data.csv` — duplicate-ID validation test

\- `README.md` — documentation



\## How to run

```bash

python weekly\_management\_summary.py

```



\## Reporting rules

\- Reporting period: 14 October to 20 October 2026.

\- Report date: 21 October 2026.

\- Only tickets created within the selected week are included in weekly KPIs.

\- Records outside the week are counted separately.

\- Critical open includes Critical tickets that are not Closed.

\- An open or in-progress ticket older than 5 calendar days is flagged for follow-up.



\## Expected results

\- Tickets created during the week: 8

\- Open tickets: 4

\- In-progress tickets: 1

\- Closed tickets: 3

\- Critical open tickets: 1

\- Overdue open tickets: 1

\- Records outside the reporting week: 2



\## Validation

\- Required columns must exist.

\- Ticket IDs must be unique and nonblank.

\- Priority and Status must use supported values.

\- Required fields must not be blank.

\- Created Date must use YYYY-MM-DD.



\## Limitations

\- All data is fictional training data.

\- Reporting dates are fixed for reproducible practice.

\- This sample reports tickets created during the week; it does not include older tickets still open unless they fall within the selected period.

\- Calendar days are used for ticket age.



\## Learning outcomes

CSV processing, date calculations, validation, aggregation, reporting, and Git version control.



