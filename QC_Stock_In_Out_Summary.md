\# QC Stock In vs Stock Out Summary



\## 1. Purpose



This document demonstrates a simple inventory stock-in versus stock-out

analysis using a hypothetical sample dataset.



The objective is to understand:



\- Opening stock

\- Stock received

\- Stock issued

\- Closing stock

\- Stock reconciliation

\- Inventory movement



This is a learning example and does not represent actual company data.



\---



\## 2. Inventory Formula



Closing Stock = Opening Stock + Stock In - Stock Out



\---



\## 3. Sample Data



| Item | Opening Stock | Stock In | Stock Out | Expected Closing |

|---|---:|---:|---:|---:|

| Main Unit | 100 | 50 | 80 | 70 |

| Lobby Camera | 80 | 40 | 60 | 60 |

| Router | 60 | 30 | 45 | 45 |

| DCUPS | 50 | 20 | 25 | 45 |

| Sensor Bag | 70 | 30 | 50 | 50 |



\---



\## 4. Calculation



\### Main Unit



100 + 50 - 80 = 70



Closing Stock = 70



\### Lobby Camera



80 + 40 - 60 = 60



Closing Stock = 60



\### Router



60 + 30 - 45 = 45



Closing Stock = 45



\### DCUPS



50 + 20 - 25 = 45



Closing Stock = 45



\### Sensor Bag



70 + 30 - 50 = 50



Closing Stock = 50



\---



\## 5. Summary



| Metric | Quantity |

|---|---:|

| Total Opening Stock | 360 |

| Total Stock In | 170 |

| Total Stock Out | 260 |

| Total Closing Stock | 270 |



Validation:



360 + 170 - 260 = 270



Result: PASS



\---



\## 6. Stock Movement Observation



The sample dataset shows that:



\- 170 units were received.

\- 260 units were issued.

\- Inventory reduced by 90 units.

\- Closing inventory is 270 units.



Management should monitor items with high stock-out frequency.



\---



\## 7. Input Validation Rules



Before calculating closing stock:



1\. Item name must not be blank.

2\. Opening stock must be numeric.

3\. Stock In must be numeric.

4\. Stock Out must be numeric.

5\. Stock quantities cannot be negative.

6\. Closing stock cannot be negative.

7\. Closing stock must equal:



Opening Stock + Stock In - Stock Out



\---



\## 8. Test Cases



\### Test Case 1 — Normal Calculation



Opening Stock = 100



Stock In = 50



Stock Out = 80



Expected:



100 + 50 - 80 = 70



Result: PASS



\---



\### Test Case 2 — No Stock In



Opening Stock = 100



Stock In = 0



Stock Out = 30



Expected:



100 + 0 - 30 = 70



Result: PASS



\---



\### Test Case 3 — No Stock Out



Opening Stock = 100



Stock In = 50



Stock Out = 0



Expected:



100 + 50 - 0 = 150



Result: PASS



\---



\### Test Case 4 — Invalid Negative Input



Opening Stock = 100



Stock In = -20



Stock Out = 30



Expected:



Invalid Input — Stock quantity cannot be negative.



Result: PASS



\---



\### Test Case 5 — Stock Out Greater Than Available Stock



Opening Stock = 20



Stock In = 10



Stock Out = 40



Available Stock = 30



Expected:



Invalid Input — Stock Out exceeds available stock.



Result: PASS



\---



\## 9. Management Interpretation



Stock-in versus stock-out analysis can help management identify:



\- Fast-moving items

\- Slow-moving items

\- Inventory shortages

\- Excess inventory

\- Frequent stock-out items

\- Procurement requirements

\- Shipment consumption trends



\---



\## 10. Recommended Management Actions



1\. Monitor high stock-out items.

2\. Maintain minimum stock levels.

3\. Review procurement requirements regularly.

4\. Compare stock movement against shipment demand.

5\. Investigate inventory mismatches.

6\. Perform periodic physical stock verification.



\---



\## 11. Recommended KPI



\### Stock Utilization Rate



Stock Utilization Rate (%) =



Stock Out / Available Stock × 100



Where:



Available Stock = Opening Stock + Stock In



Example:



Opening Stock = 100



Stock In = 50



Stock Out = 80



Available Stock = 150



Stock Utilization Rate = 80 / 150 × 100



Stock Utilization Rate = 53.33%



\---



\## 12. Assumptions



\- This is a hypothetical learning dataset.

\- All quantities are sample values.

\- Stock In represents received inventory.

\- Stock Out represents issued inventory.

\- Actual company inventory data should be validated before reporting.



\---



\## 13. Future Automation



This analysis can later be automated using:



\- Excel

\- Python

\- Power BI

\- SQL

\- Automated inventory dashboards

\- AI-based inventory analysis

