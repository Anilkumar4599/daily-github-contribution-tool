

\# Day 107 — Spare-Outward Summary Grouped by Item



\## Objective

Create a Python automation that groups spare-outward transactions by item code and produces an item-wise quantity summary.



\## Business use case

Procurement, inventory, QC, and service teams can use the report to understand which spare parts are being issued, how frequently each item is issued, and which destinations receive the items.



\## Project files

\- `spare\_outward\_data.csv` — sample outward transactions

\- `spare\_outward\_summary.py` — Python processing and validation

\- `spare\_outward\_summary.csv` — generated summary

\- `invalid\_spare\_data.csv` — invalid test data

\- `README.md` — documentation



\## How to run

```bash

python spare\_outward\_summary.py

```



\## Report fields

\- Item Code

\- Item Name

\- Category

\- Unit

\- Transaction Count

\- Total Quantity Issued

\- Unique Destinations

\- First Transaction Date

\- Last Transaction Date



\## Validation rules

1\. Required columns must exist.

2\. Transaction IDs must be unique and nonblank.

3\. Required item and transaction details must be present.

4\. Transaction dates must use YYYY-MM-DD.

5\. Quantity Issued must be a positive whole number.

6\. An item code must retain the same name, category, and unit across records.

7\. CSV records must have the expected number of fields.



\## Sample assumptions

\- The data is fictional training data, not actual company records.

\- Each row represents one outward transaction.

\- Transactions are grouped by Item Code.

\- Quantities are added only for the same item and unit.

\- Unique Destinations counts distinct destination names per item.

\- The report includes only items appearing in the input data.

\- The report does not calculate stock balance because opening stock and inward transactions are not included.



\## Expected sample results

\- Outward transactions: 10

\- Unique spare items: 5

\- Total quantity issued: 51 units across the sample records

\- CAM001 Indoor Camera: 6 Nos across 3 transactions

\- CAB001 Network Cable: 25 Meters across 2 transactions

\- PWR001 Power Supply: 12 Nos across 3 transactions

\- SEN001 Door Sensor: 6 Nos across 1 transaction

\- UPS001 DC UPS: 2 Nos across 1 transaction



\## Learning outcomes

CSV processing, data validation, grouping, aggregation, reporting, exception handling, and Git version control.



\## Project status

Training project. Mark complete after testing the output and pushing the project to GitHub.



