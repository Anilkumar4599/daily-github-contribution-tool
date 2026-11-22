\# Day 142 – Stock-In vs Stock-Out Summary



\## 1. Project Overview



This project creates a simple Stock-In vs Stock-Out Summary using Python and CSV files.



It calculates opening stock, material received, material issued, and closing stock for each inventory item.



\## 2. Project Files



\- `opening\_stock.csv` – Opening inventory balances.

\- `stock\_transactions.csv` – Sample stock-in and stock-out transactions.

\- `stock\_movement\_summary.py` – Python program for movement calculations and validation.

\- `README.md` – Project documentation.



\## 3. Calculation Formula



\*\*Closing Stock = Opening Stock + Stock-In − Stock-Out\*\*



Net Movement = Total Stock-In − Total Stock-Out



\## 4. Sample Report Results



Report Date: 22-Nov-2026



| Item | Opening | Stock-In | Stock-Out | Closing |

|---|---:|---:|---:|---:|

| 2TB WD Surveillance HDD | 20 | 10 | 6 | 24 |

| 4G Router | 12 | 5 | 4 | 13 |

| Lobby Camera | 15 | 8 | 10 | 13 |

| DCUPS | 8 | 4 | 2 | 10 |

| ATM Main Unit | 5 | 2 | 5 | 2 |

| \*\*Total\*\* | \*\*60\*\* | \*\*29\*\* | \*\*27\*\* | \*\*62\*\* |



\## 5. Input Validation



The Python program checks:



1\. Required CSV columns.

2\. Duplicate inventory item codes.

3\. Duplicate transaction IDs.

4\. Valid item codes.

5\. Valid transaction types.

6\. Date format and future dates.

7\. Positive transaction quantities.

8\. Available stock before issuing material.



Invalid transactions are rejected with a validation error.



\## 6. Assumptions



1\. Report date is fixed at 22-Nov-2026.

2\. Opening stock represents the balance at the beginning of 1-Nov-2026.

3\. Each transaction represents one stock movement.

4\. Stock-In increases inventory.

5\. Stock-Out decreases inventory.

6\. All sample quantities are in units.

7\. The sample dataset is illustrative and does not represent actual company inventory.

8\. No stock adjustments, damaged stock, returns, or transfers are included unless recorded as transactions.



\## 7. Business Benefits



\- Monitors material receipts and issues.

\- Identifies closing stock quantities.

\- Supports procurement planning.

\- Helps prevent stock shortages.

\- Improves inventory movement visibility.

\- Provides a simple reconciliation of stock movements.



\## 8. Execution



Run:



```bash

python stock\_movement\_summary.py

```



\*\*Project Status:\*\* Sample implementation and validation exercise.



