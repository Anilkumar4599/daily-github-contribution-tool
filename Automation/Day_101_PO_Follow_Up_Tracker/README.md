\# Day 101 — Purchase-Order Follow-up Tracker



\## Objective



Create a Python automation that converts a sample purchase-order CSV into a follow-up tracker.



\## Business Use Case



Procurement teams need to follow up on POs with incomplete deliveries and identify overdue suppliers.



The tool calculates pending quantities, delivery delays, status, and follow-up priority.



\## Input



`sample\_po\_data.csv`



Required fields:



\- PO Number

\- Vendor

\- Item

\- PO Date

\- Expected Date

\- Ordered Qty

\- Received Qty



\## Output



`po\_follow\_up\_report.csv`



The generated report includes:



\- Pending quantity

\- Expected delivery date

\- Delay days

\- Status

\- Follow-up priority



\## Classification Rules



\- Completed: pending quantity is zero.

\- Overdue: pending quantity remains and expected date is before the reference date.

\- Due Today: pending quantity remains and expected date equals the reference date.

\- Pending: pending quantity remains and expected date is in the future.

\- High: overdue or due today.

\- Monitor: future expected date with pending quantity.

\- No Follow-up: fully received order.



\## Validation



The program checks for:



1\. Missing input files

2\. Required columns

3\. Duplicate or blank PO numbers

4\. Invalid dates or quantities

5\. Received quantity greater than ordered quantity

6\. Expected date before PO date



\## Assumptions



\- Sample reference date is fixed at 12 October 2026 to make test results reproducible.

\- Quantities are whole numbers.

\- A PO is complete when received quantity equals ordered quantity.

\- This is a sample tracker, not a live supplier or ERP integration.

\- High priority is a simple rule-based classification and may need business-specific escalation rules.



\## Test Cases



\- Valid sample CSV

\- Missing input file

\- Received quantity exceeding ordered quantity

\- Overdue date calculations



\## Learning Outcomes



Practiced Python CSV processing, date calculations, input validation, dictionaries, loops, report generation, and basic procurement automation.



\## Project Status



Day 101 practical automation exercise.



