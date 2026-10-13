\# Day 102 — Vendor Follow-up Email Draft Generator



\## Objective



Generate vendor follow-up email drafts automatically from a CSV file containing purchase-order data.



\## Business Use Case



Procurement teams often spend time manually preparing emails for overdue deliveries.



This tool identifies overdue POs with pending quantities and prepares a consistent email draft containing the PO details, pending quantity, delay, and request for a revised delivery commitment.



\## Project Files



\- `vendor\_po\_data.csv` — Sample input data.

\- `vendor\_email\_generator.py` — Python automation.

\- `vendor\_email\_drafts.csv` — Generated email drafts.

\- `invalid\_vendor\_data.csv` — Input validation test.

\- `README.md` — Documentation.



\## How It Works



1\. Read the PO CSV file.

2\. Validate required columns and data.

3\. Check vendor email formatting.

4\. Calculate pending quantities.

5\. Identify overdue POs using a reference date.

6\. Generate a subject and email body for each eligible PO.

7\. Save the drafts in a separate CSV file.



\## Eligibility Rules



\- A PO must have a pending quantity.

\- Its expected delivery date must be before the reference date.

\- Completed POs are skipped.

\- POs due today or in the future are skipped.



\## Input Validation



The program checks:



\- File existence

\- Required columns

\- Duplicate or blank PO numbers

\- Basic email format

\- Valid dates

\- Numeric quantities

\- Received quantity not exceeding ordered quantity



\## Assumptions



\- The reference date is fixed at 13 October 2026 for reproducible testing.

\- Dates use ISO format: YYYY-MM-DD.

\- Quantity values are whole numbers.

\- The email validation uses basic string rules, not the full email standard.

\- The tool creates drafts only; it does not send emails.

\- The sample data does not represent live vendor information.



\## Testing



1\. Valid PO dataset

2\. Missing input file

3\. Invalid vendor email

4\. Completed PO skipped

5\. Future delivery date skipped



\## Learning Outcomes



Practiced CSV processing, input validation, date comparisons, quantity calculations, formatted text generation, and automated report creation.



\## Project Status



Day 102 practical automation exercise.



