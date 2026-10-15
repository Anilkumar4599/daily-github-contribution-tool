\# Day 104 — Procurement Credit-Time Tracker



\## Objective



Create a Python program that calculates invoice due dates from agreed credit periods and flags overdue procurement invoices.



\## Business Use Case



Procurement and Accounts teams need to monitor supplier invoices against agreed credit periods.



The tracker calculates due dates, days overdue, and follow-up status so that outstanding invoices can be reviewed.



\## Input File



`credit\_data.csv`



Required fields:



\- Invoice Number

\- Vendor

\- PO Number

\- Invoice Date

\- Credit Days

\- Invoice Amount

\- Payment Status



\## Output File



`credit\_time\_report.csv`



The report includes:



\- Calculated due date

\- Days overdue

\- Credit status

\- Follow-up priority



\## Rules



\- Due date = invoice date + agreed credit days.

\- Overdue: outstanding invoice with a reference date after the due date.

\- Due Today: outstanding invoice whose due date equals the reference date.

\- Within Credit Period: outstanding invoice whose due date is in the future.

\- Paid: invoice marked Paid; no overdue follow-up is required.



\## Input Validation



The program checks:



1\. Input file existence

2\. Required columns

3\. Duplicate or blank invoice numbers

4\. Valid invoice dates

5\. Numeric credit days and amounts

6\. Non-negative credit days and amounts

7\. Valid payment status



\## Assumptions



\- Reference date is fixed at 15 October 2026 for reproducible testing.

\- Credit days are calendar days, not business days.

\- Due date is calculated from the invoice date.

\- Paid invoices are excluded from overdue follow-up.

\- This is a sample tracker and does not connect to a live ERP or Accounts system.



\## Testing



\- Valid sample dataset

\- Missing input file

\- Negative credit days

\- Due-date and overdue-day calculations



\## Learning Outcomes



Practiced CSV processing, date arithmetic, validation, report generation, and procurement follow-up automation.



\## Project Status



Day 104 practical automation exercise.



