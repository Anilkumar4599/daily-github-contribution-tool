\# Day 141 – Inventory Aging Report



\## 1. Project Overview



This project demonstrates a simple Inventory Aging Report using Python and a sample inventory dataset.



The report identifies how long inventory has been held, classifies stock into aging categories, and calculates the inventory value for each category.



\## 2. Project Files



\- `inventory\_aging\_sample.csv` – Sample inventory records.

\- `inventory\_aging\_report.py` – Python program for inventory aging calculations.

\- `README.md` – Project documentation and assumptions.



\## 3. Aging Classification



| Inventory Age | Aging Category |

|---|---|

| 0–30 days | Fresh |

| 31–60 days | Normal |

| 61–90 days | Slow-moving |

| Above 90 days | Old stock |



\## 4. Calculation Logic



\*\*Inventory Age (Days)\*\*



Inventory Age = Report Date − Received Date



\*\*Stock Value\*\*



Stock Value = Quantity on Hand × Unit Cost



The Python program reads the CSV file, calculates inventory age, assigns an aging category, and summarizes stock quantity and value.



\## 5. Sample Report Results



Report Date: 21-Nov-2026



| Aging Category | Records | Quantity | Stock Value |

|---|---:|---:|---:|

| Fresh | 1 | 3 | ₹19,500 |

| Normal | 1 | 8 | ₹25,600 |

| Slow-moving | 1 | 5 | ₹22,500 |

| Old stock | 2 | 12 | ₹1,41,000 |

| \*\*Total\*\* | \*\*5\*\* | \*\*28\*\* | \*\*₹2,08,600\*\* |



\## 6. Key Management Observation



\- Total inventory value: ₹2,08,600.

\- Old stock value: ₹1,41,000.

\- Old stock represents approximately 67.6% of total inventory value.

\- Old stock should be reviewed for consumption planning, redistribution, project requirements, or procurement control.



\## 7. Assumptions



1\. The report date is fixed at 21-Nov-2026 for this sample exercise.

2\. Inventory age is calculated using calendar days.

3\. Each CSV row represents one inventory stock lot.

4\. Received date is used as the starting point for aging.

5\. Stock value is calculated using quantity on hand multiplied by unit cost.

6\. Sample records are illustrative and do not represent actual company inventory.

7\. The report does not consider stock movements, returns, reservations, or subsequent issues after the received date.



\## 8. Validation



The program checks:



\- Required CSV columns are available.

\- Received dates follow YYYY-MM-DD format.

\- Future received dates are rejected.

\- Negative quantity and unit cost are rejected.



\## 9. Business Benefits



\- Identifies slow-moving and old inventory.

\- Helps prioritize inventory reviews.

\- Supports better stock utilization.

\- Helps reduce excess and obsolete inventory.

\- Improves inventory visibility for procurement and management.



\## 10. Execution



Run the following command:



```bash

python inventory\_aging\_report.py

```



\*\*Project Status:\*\* Completed sample implementation and verified output.



