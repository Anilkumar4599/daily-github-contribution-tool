\# Day 144 – Item-wise Consumption Report



\## 1. Project Overview



This project creates an Item-wise Consumption Report using Python and CSV.



The report summarizes material consumption by item, calculates the number of issue transactions, and determines the average quantity issued per transaction.



\## 2. Project Files



\- `stock\_issue\_transactions.csv` – Sample stock issue records.

\- `item\_wise\_consumption\_report.py` – Python program for validation and consumption calculations.

\- `README.md` – Project documentation.



\## 3. Report Period



1-Nov-2026 to 24-Nov-2026.



\## 4. Calculation Logic



\*\*Total Consumption\*\* = Sum of all issued quantities.



\*\*Average Consumption per Issue\*\* = Total Issued Quantity / Number of Issue Transactions.



\## 5. Sample Expected Output



| Item | Issue Records | Total Consumption | Average per Issue |

|---|---:|---:|---:|

| 2TB WD Surveillance HDD | 3 | 6 | 2.00 |

| 4G Router | 3 | 6 | 2.00 |

| Lobby Camera | 2 | 6 | 3.00 |

| DCUPS | 1 | 1 | 1.00 |

| ATM Main Unit | 1 | 1 | 1.00 |

| \*\*Total\*\* | \*\*10\*\* | \*\*20\*\* | \*\*2.00\*\* |



\## 6. Input Validation



The program validates:



1\. Required CSV columns.

2\. Missing mandatory fields.

3\. Duplicate issue IDs.

4\. Valid transaction dates.

5\. Dates within the report period.

6\. Positive issue quantities.

7\. Consistent item names for each item code.



\## 7. Assumptions



1\. The report period is 1-Nov-2026 to 24-Nov-2026.

2\. Each CSV row represents one material issue transaction.

3\. All quantities are measured in units.

4\. Only stock issue transactions are included.

5\. Sample data is illustrative and does not represent actual company consumption.

6\. The report measures issued quantity, not necessarily material actually installed or consumed at the site.

7\. Returns and cancellations are not included in this sample.



\## 8. Business Benefits



\- Identifies frequently issued materials.

\- Supports item-wise consumption monitoring.

\- Helps forecast procurement requirements.

\- Improves material planning for projects.

\- Helps identify high-consumption items.

\- Supports inventory management reporting.



\## 9. Execution



```bash

python item\_wise\_consumption\_report.py

```



\*\*Project Status:\*\* Sample implementation and output verification.



