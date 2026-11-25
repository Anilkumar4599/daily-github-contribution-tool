\# Day 145 – Minimum and Maximum Stock Calculator



\## 1. Project Overview



This project is a simple Python-based inventory management tool that checks current stock levels against predefined minimum and maximum stock quantities.



It helps procurement and inventory teams identify items requiring replenishment, maintain appropriate stock levels, and identify excess inventory.



\*\*Business Example:\*\* ATM E-Surveillance inventory management.



\## 2. Project Objectives



\- Identify items that have reached or fallen below minimum stock.

\- Calculate suggested replenishment quantities.

\- Identify items with healthy stock levels.

\- Highlight items exceeding maximum stock.

\- Generate an item-wise inventory report.



\## 3. Project Files



| File | Description |

|---|---|

| `stock\_levels.csv` | Sample inventory input data |

| `min\_max\_stock\_calculator.py` | Python calculation program |

| `README.md` | Project documentation |



\## 4. Stock Calculation Logic



The program uses three conditions:



\### Condition 1: Reorder Now



If Current Stock is less than or equal to Minimum Stock:



`Reorder Quantity = Maximum Stock - Current Stock`



Example:



\- Current Stock: 8

\- Minimum Stock: 10

\- Maximum Stock: 30

\- Suggested Reorder: 30 - 8 = 22 units



\### Condition 2: Stock OK



If Current Stock is greater than Minimum Stock and less than or equal to Maximum Stock:



\- Status: STOCK OK

\- Reorder Quantity: 0



\### Condition 3: Above Maximum



If Current Stock is greater than Maximum Stock:



\- Status: ABOVE MAXIMUM

\- Reorder Quantity: 0



Excess stock should be reviewed before placing additional orders.



\## 5. Sample Input Data



The following sample records are maintained in `stock\_levels.csv`.



| Item | Current | Minimum | Maximum |

|---|---:|---:|---:|

| 2TB WD Surveillance HDD | 8 | 10 | 30 |

| 4G Router | 15 | 8 | 25 |

| Lobby Camera | 5 | 5 | 20 |

| DCUPS | 22 | 10 | 20 |

| ATM Main Unit | 12 | 10 | 15 |



\## 6. Expected Output



| Item | Status | Reorder Qty |

|---|---|---:|

| 2TB WD Surveillance HDD | REORDER NOW | 22 |

| 4G Router | STOCK OK | 0 |

| Lobby Camera | REORDER NOW | 15 |

| DCUPS | ABOVE MAXIMUM | 0 |

| ATM Main Unit | STOCK OK | 0 |



\### Summary



\- Total items checked: 5

\- Items requiring reorder: 2

\- Total suggested reorder: 37 units



\## 7. Validation Rules



The Python program checks:



1\. Input CSV file availability.

2\. Required CSV column headers.

3\. Availability of inventory records.

4\. Mandatory item code and item name.

5\. Duplicate item codes.

6\. Valid integer stock quantities.

7\. Negative stock quantities.

8\. Minimum stock not exceeding maximum stock.



\## 8. How to Run the Program



Open Git Bash at the repository root and execute:



```bash

python "Inventory/Day\_145\_Min\_Max\_Stock\_Calculator/min\_max\_stock\_calculator.py"

```



\## 9. Business Benefits



\- Improves inventory visibility.

\- Supports timely procurement planning.

\- Reduces the risk of stock-outs.

\- Helps identify excess inventory.

\- Provides a simple replenishment reference for procurement teams.



\## 10. Assumptions and Limitations



\- All quantities are measured in units.

\- Maximum stock is treated as the target stock level after replenishment.

\- Reorder quantity is calculated as Maximum Stock minus Current Stock when replenishment is required.

\- Supplier lead time, pending purchase orders, reserved stock and safety stock are not included.

\- Suggested reorder quantities should be reviewed by the procurement team before placing purchase orders.



\---



\*\*Project:\*\* Day 145 – Minimum and Maximum Stock Calculator  

\*\*Domain:\*\* Inventory Management  

\*\*Technology:\*\* Python, CSV, GitHub  

\*\*Learning Focus:\*\* Inventory calculations, stock-level validation and basic Python automation.

