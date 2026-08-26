\# Inventory Item-Wise Consumption Report



\## 1. Purpose



This document provides a sample item-wise inventory consumption report.



The objective is to understand:



\- Opening stock

\- Stock received

\- Stock consumed

\- Closing stock

\- Consumption percentage

\- High-consumption items



This is a hypothetical learning example.



\---



\## 2. Inventory Calculation Logic



Closing Stock = Opening Stock + Stock In - Stock Out



Consumption % = Stock Out / (Opening Stock + Stock In) × 100



\---



\## 3. Sample Input Data



| Item | Opening Stock | Stock In | Stock Out |

|---|---:|---:|---:|

| Main Unit | 100 | 50 | 80 |

| Lobby Camera | 120 | 40 | 100 |

| Backroom Camera | 100 | 30 | 60 |

| Router | 80 | 40 | 70 |

| DCUPS | 60 | 20 | 30 |



\---



\## 4. Item-Wise Consumption Calculation



\### Main Unit



Available Stock = 100 + 50 = 150



Stock Out = 80



Closing Stock = 150 - 80 = 70



Consumption % = 80 / 150 × 100 = 53.33%



\---



\### Lobby Camera



Available Stock = 120 + 40 = 160



Stock Out = 100



Closing Stock = 160 - 100 = 60



Consumption % = 100 / 160 × 100 = 62.50%



\---



\### Backroom Camera



Available Stock = 100 + 30 = 130



Stock Out = 60



Closing Stock = 130 - 60 = 70



Consumption % = 60 / 130 × 100 = 46.15%



\---



\### Router



Available Stock = 80 + 40 = 120



Stock Out = 70



Closing Stock = 120 - 70 = 50



Consumption % = 70 / 120 × 100 = 58.33%



\---



\### DCUPS



Available Stock = 60 + 20 = 80



Stock Out = 30



Closing Stock = 80 - 30 = 50



Consumption % = 30 / 80 × 100 = 37.50%



\---



\## 5. Expected Output



| Item | Opening | Stock In | Stock Out | Closing | Consumption % |

|---|---:|---:|---:|---:|---:|

| Main Unit | 100 | 50 | 80 | 70 | 53.33% |

| Lobby Camera | 120 | 40 | 100 | 60 | 62.50% |

| Backroom Camera | 100 | 30 | 60 | 70 | 46.15% |

| Router | 80 | 40 | 70 | 50 | 58.33% |

| DCUPS | 60 | 20 | 30 | 50 | 37.50% |



\---



\## 6. Management Finding



The highest consumption item is:



Lobby Camera = 62.50%



The second highest consumption item is:



Router = 58.33%



The lowest consumption item is:



DCUPS = 37.50%



Therefore, Lobby Camera and Router stock should receive closer monitoring.



\---



\## 7. Inventory Management Actions



Management should:



1\. Monitor high-consumption items.

2\. Review daily stock-out trends.

3\. Compare consumption with shipment requirements.

4\. Maintain minimum stock levels.

5\. Identify frequently consumed spare items.

6\. Review supplier lead time.

7\. Plan replenishment before stock reaches critical level.



\---



\## 8. Input Validation Rules



Before calculating consumption:



1\. Item name must not be blank.

2\. Opening stock must be numeric.

3\. Stock In must be numeric.

4\. Stock Out must be numeric.

5\. Stock quantities cannot be negative.

6\. Stock Out cannot exceed available stock.

7\. Consumption percentage cannot be greater than 100%.



\---



\## 9. Test Cases



\### Test Case 1 — Normal Calculation



Input:



Opening Stock = 100



Stock In = 50



Stock Out = 80



Expected:



Closing Stock = 70



Consumption = 53.33%



Result: PASS



\---



\### Test Case 2 — Zero Consumption



Input:



Opening Stock = 100



Stock In = 50



Stock Out = 0



Expected:



Closing Stock = 150



Consumption = 0%



Result: PASS



\---



\### Test Case 3 — Invalid Stock Out



Input:



Opening Stock = 50



Stock In = 20



Stock Out = 80



Available Stock = 70



Expected:



Invalid Input — Stock Out cannot exceed available stock.



Result: PASS



\---



\### Test Case 4 — Negative Quantity



Input:



Opening Stock = 100



Stock In = -10



Stock Out = 20



Expected:



Invalid Input — Stock quantities cannot be negative.



Result: PASS



\---



\## 10. Management Interpretation



Item-wise consumption reporting helps inventory management identify:



\- Fast-moving items

\- Slow-moving items

\- High stock-out items

\- Replenishment requirements

\- Potential stock shortages

\- Spare consumption trends



The report can also be linked with shipment and BAU spare requirements.



\---



\## 11. Recommended KPI



\### Inventory Consumption Rate



Inventory Consumption Rate (%) =



Total Stock Out / Total Available Stock × 100



This KPI can be monitored daily, weekly and monthly.



\---



\## 12. Future Automation



This report can later be automated using:



\- Excel

\- Python

\- Power BI

\- SQL

\- AI-based inventory analysis

\- Automated stock alerts



\---



\## 13. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company inventory.

\- Stock Out represents inventory consumed or issued.

\- Actual inventory transactions should be validated before management reporting.

