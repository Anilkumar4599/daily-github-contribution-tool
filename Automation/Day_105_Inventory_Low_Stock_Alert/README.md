\# Day 105 — Inventory Low-Stock Alert Report



\## Objective



Build a Python script that reads inventory data from a CSV file, identifies items requiring replenishment, and generates a low-stock alert report.



\## Business Use Case



Procurement, QC, and Service teams need visibility into items that may run out of stock.



The tool compares current stock with minimum stock levels and flags critical shortages, low stock, and items at their reorder point.



\## Project Files



\- `inventory\_data.csv` — Sample inventory input.

\- `inventory\_alert.py` — Python automation.

\- `low\_stock\_alert\_report.csv` — Generated report.

\- `invalid\_inventory.csv` — Validation test data.

\- `README.md` — Project documentation.



\## Output Fields



\- Current Stock

\- Minimum Stock

\- Shortage to Minimum

\- Reorder Quantity

\- Suggested Order Quantity

\- Stock Status

\- Priority



\## Classification Rules



\- Critical: current stock is zero.

\- High: current stock is below minimum but above zero.

\- Medium: current stock equals minimum.

\- None: current stock is above minimum.



\## Input Validation



The program checks:



1\. Input file existence

2\. Required CSV columns

3\. Duplicate or blank item codes

4\. Numeric stock values

5\. Non-negative current stock

6\. Positive minimum and reorder quantities

7\. Required item descriptions and units



\## Assumptions



\- Sample data is fictional.

\- Stock quantities are whole numbers.

\- Minimum stock is the alert threshold.

\- Suggested order quantity uses the configured reorder quantity.

\- Shortage to minimum is calculated separately.

\- This is a sample tool, not a live ERP or inventory-system integration.



\## Test Cases



\- Valid inventory dataset

\- Missing input file

\- Negative current stock

\- Zero stock classification

\- Low-stock classification

\- Reorder-point classification

\- Adequate-stock classification



\## Learning Outcomes



Practiced CSV processing, input validation, conditional logic, inventory calculations, and automated report generation.



\## Project Status



Day 105 practical automation exercise.



