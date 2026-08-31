\# QC Spare Request vs Outward Analysis



\## 1. Purpose



This document provides a sample analysis comparing spare requests

with actual spare outward quantities.



The objective is to identify demand fulfillment, shortages,

excess outward movement, and recurring spare requirements.



This is a hypothetical learning example.



\---



\## 2. Business Objective



The analysis helps Inventory and QC management:



\- Compare requested spares against outward quantities.

\- Identify fulfilled and partially fulfilled requests.

\- Identify shortages.

\- Monitor frequently requested spare items.

\- Support inventory planning.

\- Improve spare availability.



\---



\## 3. Formula



Fulfillment % = Spare Outward / Spare Request × 100



Shortage = Spare Request - Spare Outward



\---



\## 4. Example Input



| Item | Spare Request | Spare Outward |

|---|---:|---:|

| Lobby Camera | 20 | 18 |

| Router | 15 | 15 |

| Main Unit | 10 | 8 |

| DCUPS | 12 | 10 |

| Sensor Bag | 25 | 25 |



\---



\## 5. Calculation



\### Lobby Camera



Request = 20



Outward = 18



Shortage = 20 - 18 = 2



Fulfillment = 18 / 20 × 100 = 90%



\---



\### Router



Request = 15



Outward = 15



Shortage = 15 - 15 = 0



Fulfillment = 15 / 15 × 100 = 100%



\---



\### Main Unit



Request = 10



Outward = 8



Shortage = 10 - 8 = 2



Fulfillment = 8 / 10 × 100 = 80%



\---



\### DCUPS



Request = 12



Outward = 10



Shortage = 12 - 10 = 2



Fulfillment = 10 / 12 × 100 = 83.33%



\---



\### Sensor Bag



Request = 25



Outward = 25



Shortage = 25 - 25 = 0



Fulfillment = 25 / 25 × 100 = 100%



\---



\## 6. Expected Output



| Item | Request | Outward | Shortage | Fulfillment % |

|---|---:|---:|---:|---:|

| Lobby Camera | 20 | 18 | 2 | 90% |

| Router | 15 | 15 | 0 | 100% |

| Main Unit | 10 | 8 | 2 | 80% |

| DCUPS | 12 | 10 | 2 | 83.33% |

| Sensor Bag | 25 | 25 | 0 | 100% |



\---



\## 7. Overall Summary



Total Spare Requests = 82



Total Spare Outward = 76



Total Shortage = 6



Overall Fulfillment = 76 / 82 × 100



Overall Fulfillment = 92.68%



\---



\## 8. Management Findings



1\. Sensor Bag and Router requests were fully fulfilled.



2\. Main Unit has the lowest fulfillment percentage at 80%.



3\. Lobby Camera has a shortage of 2 units.



4\. DCUPS has a shortage of 2 units.



5\. Total shortage across the sample is 6 units.



6\. Main Unit should be reviewed for inventory availability.



7\. Repeated shortages should be considered during inventory planning.



\---



\## 9. Recommended Actions



1\. Review stock availability for Main Unit.



2\. Review Lobby Camera spare consumption.



3\. Check DCUPS stock levels.



4\. Monitor frequently requested spare items.



5\. Maintain minimum stock levels for critical spares.



6\. Review request versus outward trends periodically.



\---



\## 10. Test Cases



\### Test Case 1 — Fully Fulfilled Request



Input:



Request = 15



Outward = 15



Expected:



Shortage = 0



Fulfillment = 100%



Result: PASS



\---



\### Test Case 2 — Partial Fulfillment



Input:



Request = 20



Outward = 18



Expected:



Shortage = 2



Fulfillment = 90%



Result: PASS



\---



\### Test Case 3 — Zero Request



Input:



Request = 0



Outward = 0



Expected:



Fulfillment should not be calculated because division by zero

is invalid.



Expected Result:



Invalid Input — No spare request.



Result: PASS



\---



\### Test Case 4 — Outward Greater Than Request



Input:



Request = 10



Outward = 12



Expected:



The data should be reviewed because outward quantity is greater

than the requested quantity.



Expected Result:



Validation Warning



Result: PASS



\---



\## 11. Input Validation Rules



\- Item name must not be blank.

\- Spare request must be numeric.

\- Spare request cannot be negative.

\- Spare outward must be numeric.

\- Spare outward cannot be negative.

\- Spare outward greater than request should be flagged for review.

\- Fulfillment percentage should not be calculated when request = 0.



\---



\## 12. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company records.

\- Spare outward means quantity actually issued or dispatched.

\- Actual business data should be validated before management reporting.



\---



\## 13. Future Automation



This analysis can later be automated using:



\- Excel

\- Python

\- Power BI

\- Automated inventory dashboards

\- AI-assisted inventory analysis

\- Automated shortage alerts

