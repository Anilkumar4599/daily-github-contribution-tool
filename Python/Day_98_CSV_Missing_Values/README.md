\# Day 98 — CSV Missing Values Detector



\## Objective



Create a Python function that identifies missing values in a specified CSV column.



\## Business Use Case



Procurement and QC reports may contain incomplete records. Missing PO numbers, vendor names, item descriptions, or quantities can affect analysis and management reporting.



This tool helps identify records requiring correction before further processing.



\## Project Files



\- `sample\_data.csv` — Sample procurement dataset with intentionally missing values.

\- `missing\_values\_detector.py` — Python program.

\- `README.md` — Project documentation.



\## Function



`find\_missing\_values(filename, column\_name)`



The function returns the CSV row numbers where the selected column is blank or contains only whitespace.



\## Validation



The program checks that:



1\. The input file exists.

2\. The path points to a file.

3\. The CSV has a header.

4\. The requested column exists.



\## Test Cases



1\. Detect a missing Vendor value.

2\. Detect a missing PO Number.

3\. Detect a missing Item value.

4\. Reject a column name that does not exist.

5\. Detect blank quantity values.



\## Assumptions



\- The input is a CSV file with a header row.

\- Blank cells and whitespace-only cells count as missing.

\- CSV row numbers include the header as row 1.

\- The program reports missing values but does not modify the source file.

\- This project checks missing values only; it does not validate every business rule.



\## Learning Outcome



Practiced Python functions, CSV reading, dictionaries, loops, conditional statements, file validation, exception handling, and test cases.



\## Project Status



Day 98 Python practical exercise.



