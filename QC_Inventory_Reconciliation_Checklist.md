\# QC Inventory Reconciliation Checklist



\## 1. Purpose



This document provides a practical checklist for reconciling physical

inventory, system inventory, receipts, issues, and shipment records.



The objective is to identify inventory mismatches before they affect

shipment planning, procurement, or stock availability.



This is a hypothetical learning example.



\---



\## 2. Inventory Reconciliation Principle



Inventory reconciliation compares the expected system quantity with

the physically verified quantity.



Expected Closing Stock = Opening Stock + Stock In - Stock Out



Variance = Physical Stock - System Stock



\---



\## 3. Reconciliation Checklist



| No. | Checkpoint | Validation | Status |

|---|---|---|---|

| 1 | Opening stock | Verify opening balance against previous closing balance | PASS |

| 2 | Stock received | Verify GRN/receipt records | PASS |

| 3 | Stock issued | Verify issue/shipment records | PASS |

| 4 | Physical stock | Perform physical count | PASS |

| 5 | System stock | Check inventory system quantity | PASS |

| 6 | Variance | Compare physical and system stock | PASS |

| 7 | Damaged stock | Identify damaged/non-usable units | PASS |

| 8 | Pending returns | Check returnable inventory | PASS |

| 9 | Serial numbers | Verify device serial numbers | PASS |

| 10 | Shipment records | Reconcile shipped quantities | PASS |

| 11 | Open tickets | Check items blocked due to QC issues | PASS |

| 12 | Final approval | QC/Inventory manager review | PASS |



\---



\## 4. Sample Inventory Reconciliation



| Item | Opening | Stock In | Stock Out | System Stock | Physical Stock | Variance |

|---|---:|---:|---:|---:|---:|---:|

| Main Unit | 100 | 50 | 70 | 80 | 80 | 0 |

| Lobby Camera | 80 | 30 | 50 | 60 | 58 | -2 |

| Router | 60 | 20 | 30 | 50 | 50 | 0 |

| DCUPS | 50 | 10 | 20 | 40 | 41 | +1 |

| Sensor Bag | 70 | 20 | 40 | 50 | 50 | 0 |



\---



\## 5. Reconciliation Calculation



\### Main Unit



Opening = 100



Stock In = 50



Stock Out = 70



Expected Closing:



100 + 50 - 70 = 80



System Stock = 80



Physical Stock = 80



Variance:



80 - 80 = 0



Result: PASS



\---



\### Lobby Camera



Opening = 80



Stock In = 30



Stock Out = 50



Expected Closing:



80 + 30 - 50 = 60



System Stock = 60



Physical Stock = 58



Variance:



58 - 60 = -2



Result: INVESTIGATE



\---



\### Router



Opening = 60



Stock In = 20



Stock Out = 30



Expected Closing:



60 + 20 - 30 = 50



System Stock = 50



Physical Stock = 50



Variance:



50 - 50 = 0



Result: PASS



\---



\### DCUPS



Opening = 50



Stock In = 10



Stock Out = 20



Expected Closing:



50 + 10 - 20 = 40



System Stock = 40



Physical Stock = 41



Variance:



41 - 40 = +1



Result: INVESTIGATE



\---



\### Sensor Bag



Opening = 70



Stock In = 20



Stock Out = 40



Expected Closing:



70 + 20 - 40 = 50



System Stock = 50



Physical Stock = 50



Variance:



50 - 50 = 0



Result: PASS



\---



\## 6. Variance Classification



| Variance | Classification | Action |

|---:|---|---|

| 0 | Matched | No action |

| Positive | Excess physical stock | Investigate transaction records |

| Negative | Stock shortage | Immediate investigation |

| Any unexplained variance | Exception | Perform RCA |



\---



\## 7. Management Summary



Total items reconciled = 5



Matched items = 3



Items requiring investigation = 2



Lobby Camera variance = -2



DCUPS variance = +1



The Lobby Camera shortage requires priority investigation because

negative inventory variance may affect shipment availability.



The DCUPS excess quantity should also be reconciled against recent

receipts, returns, or transaction records.



\---



\## 8. Recommended Investigation



For a negative variance:



1\. Recount physical stock.

2\. Verify recent stock-out transactions.

3\. Check shipment records.

4\. Verify returnable items.

5\. Check damaged or rejected units.

6\. Verify serial numbers.

7\. Review inventory system transactions.

8\. Identify the root cause.

9\. Correct the system quantity if authorized.

10\. Document the corrective action.



\---



\## 9. Inventory Reconciliation Checklist



\### Before Reconciliation



\- \[ ] Freeze or control inventory movement during counting.

\- \[ ] Obtain latest system stock report.

\- \[ ] Obtain previous closing stock.

\- \[ ] Collect stock-in records.

\- \[ ] Collect stock-out records.

\- \[ ] Identify damaged/blocked inventory.



\### During Physical Verification



\- \[ ] Count each item physically.

\- \[ ] Verify serial numbers where applicable.

\- \[ ] Separate usable and damaged inventory.

\- \[ ] Record actual physical quantity.

\- \[ ] Compare against system quantity.



\### After Reconciliation



\- \[ ] Calculate variance.

\- \[ ] Investigate all unexplained differences.

\- \[ ] Identify root cause.

\- \[ ] Correct authorized system records.

\- \[ ] Record corrective action.

\- \[ ] Obtain management approval.

\- \[ ] Maintain reconciliation evidence.



\---



\## 10. Test Cases



\### Test Case 1 — Matching Inventory



System Stock = 100



Physical Stock = 100



Variance:



100 - 100 = 0



Expected Result:



PASS — Inventory matched.



Result: PASS



\---



\### Test Case 2 — Negative Variance



System Stock = 100



Physical Stock = 95



Variance:



95 - 100 = -5



Expected Result:



INVESTIGATE — Physical stock is lower than system stock.



Result: PASS



\---



\### Test Case 3 — Positive Variance



System Stock = 100



Physical Stock = 103



Variance:



103 - 100 = +3



Expected Result:



INVESTIGATE — Physical stock is higher than system stock.



Result: PASS



\---



\### Test Case 4 — Opening/Movement Reconciliation



Opening Stock = 100



Stock In = 30



Stock Out = 20



Expected Closing:



100 + 30 - 20 = 110



Expected Result:



System stock should be 110.



Result: PASS



\---



\## 11. Input Validation Rules



Before reconciliation:



1\. Item name must not be blank.

2\. Opening stock must be numeric.

3\. Stock In must be numeric.

4\. Stock Out must be numeric.

5\. System stock must be numeric.

6\. Physical stock must be numeric.

7\. Quantities must not be negative.

8\. Variance must be calculated using:



Physical Stock - System Stock



9\. Opening + Stock In - Stock Out should reconcile with expected

closing stock.



\---



\## 12. Recommended KPIs



\### Inventory Accuracy



Inventory Accuracy (%) =



Matched Items / Total Items Reconciled × 100



Sample:



Matched Items = 3



Total Items = 5



Inventory Accuracy = 3 / 5 × 100



Inventory Accuracy = 60%



\---



\### Inventory Variance Count



Number of items with unexplained inventory variance.



Sample:



Variance Items = 2



\---



\## 13. Management Actions



Management should:



1\. Prioritize negative stock variance.

2\. Investigate serial-number mismatches.

3\. Reconcile shipment transactions daily.

4\. Monitor damaged and returnable inventory.

5\. Review inventory accuracy periodically.

6\. Maintain evidence for every adjustment.

7\. Track recurring inventory discrepancies.

8\. Perform RCA for repeated variances.



\---



\## 14. Assumptions



\- This is a hypothetical learning dataset.

\- Physical quantities are sample values.

\- System quantities are assumed to be available from an inventory system.

\- All unexplained variances require investigation.

\- Inventory adjustments should only be performed by authorized personnel.

\- Actual company inventory records must be validated before management reporting.



\---



\## 15. Future Automation



The reconciliation process can later be automated using:



\- Excel

\- Python

\- SQL

\- Power BI

\- Inventory management systems

\- Automated serial-number validation

\- AI-assisted inventory analysis

\- Automated variance alerts

