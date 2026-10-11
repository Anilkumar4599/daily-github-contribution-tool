\# Day 100 — CSV Comparison Tool



\## Objective



Build a Python program that compares two CSV reports and identifies new, missing, changed, and unchanged records.



\## Procurement Use Case



A procurement manager can compare two PO reports to identify:



\- New purchase orders

\- Purchase orders missing from the latest report

\- Changed quantities, vendors, items, or statuses

\- Records that have not changed



\## Project Files



\- `old\_report.csv` — Earlier PO report

\- `new\_report.csv` — Latest PO report

\- `compare\_csv.py` — Comparison program

\- `invalid\_report.csv` — Input validation test

\- `duplicate\_report.csv` — Duplicate-key test

\- `README.md` — Documentation



\## How It Works



1\. Read both CSV files.

2\. Validate the headers and required PO Number column.

3\. Reject missing or duplicate PO numbers.

4\. Match records using PO Number as the unique key.

5\. Identify new and missing PO numbers.

6\. Compare the other column values for matching records.

7\. Print the comparison report.



\## Sample Results



\- New records: 1 — PO1005

\- Missing records: 1 — PO1003

\- Changed records: 2 — PO1002 and PO1004

\- Unchanged records: 1 — PO1001



\## Assumptions



\- Both files use the same columns in the same order.

\- PO Number uniquely identifies each record.

\- Leading and trailing whitespace is ignored.

\- Values are compared as text. For example, `20` and `20.0` are treated as different.

\- The program reports differences but does not modify either input file.



\## Validation Tests



1\. Missing input file.

2\. Missing required key column.

3\. Duplicate PO number.

4\. Valid comparison with new, missing, changed, and unchanged records.



\## Learning Outcomes



Practiced CSV processing, dictionaries, sets, functions, file validation, exception handling, record matching, and change detection.



\## Project Status



Day 100 Python practical exercise.



