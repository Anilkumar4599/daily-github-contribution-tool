\# Day 97 - CSV Summary Report



\## Objective



Create a Python program that reads an Excel-style table exported as CSV and generates a procurement summary report.



\## Business Use Case



Procurement teams frequently export Excel reports as CSV files.



Python can be used to automatically:



\- Read the CSV file

\- Validate required columns

\- Count purchase orders

\- Calculate ordered quantity

\- Calculate received quantity

\- Calculate pending quantity

\- Summarize PO status



\## Input File



The sample input file is:



`sample\_procurement.csv`



Columns:



\- PO Number

\- Vendor

\- Item

\- Ordered Qty

\- Received Qty

\- Status



\## Sample Data



The project contains 8 sample purchase orders.



\## Expected Summary



```text

Total POs       : 8

Total Ordered   : 100

Total Received  : 80

Pending Qty     : 20

