\# QC First-Pass Yield (FPY) Calculation



\## 1. Purpose



First-Pass Yield (FPY) measures the percentage of units that pass QC

inspection the first time without rework, repair, or correction.



FPY is an important quality KPI because it helps management understand

the effectiveness of the production and QC process.



\---



\## 2. FPY Formula



FPY (%) = Units Passed First Time / Total Units Inspected × 100



\---



\## 3. Example Input



The following is a hypothetical sample dataset.



| Metric | Value |

|---|---:|

| Total Units Inspected | 100 |

| Units Passed First Time | 92 |

| Units Requiring Rework | 8 |



\---



\## 4. Calculation



FPY = 92 / 100 × 100



FPY = 92%



\---



\## 5. Expected Output



\*\*First-Pass Yield (FPY) = 92%\*\*



This means 92 out of every 100 inspected units passed QC during

the first inspection without requiring rework.



\---



\## 6. QA Validation



\### Test 1 — Basic Calculation



Input:



\- Total Units Inspected = 100

\- First-Time Pass = 92



Calculation:



92 / 100 × 100 = 92%



Result: PASS



\---



\### Test 2 — Rework Reconciliation



Total Units Inspected = 100



First-Time Pass = 92



Rework Required = 8



Validation:



92 + 8 = 100



Result: PASS



\---



\### Test 3 — Zero Inspection Check



If:



Total Units Inspected = 0



FPY should not be calculated because division by zero is invalid.



Expected result:



\*\*Invalid Input — No units inspected.\*\*



Result: PASS



\---



\## 7. Management Interpretation



An FPY of 92% means that 92% of inspected units passed QC without

requiring rework.



The remaining 8% required rework or corrective action.



Management should monitor:



\- Recurring defects

\- Device-level failure patterns

\- Hardware defects

\- Software defects

\- Supplier-related issues

\- Rework trends



\---



\## 8. Recommended Management Action



If FPY decreases over time:



1\. Identify the most frequent defect categories.

2\. Perform Root Cause Analysis (RCA).

3\. Identify HW, SW, EDGE or supplier ownership.

4\. Track corrective actions.

5\. Monitor FPY improvement after corrective action.



\---



\## 9. Assumptions



\- This is a hypothetical learning example.

\- The sample data does not represent actual company data.

\- First-time pass means the unit passed without rework or repair.

\- Actual production data should be validated before management reporting.



\---



\## 10. Future Automation



This FPY calculation can later be automated using:



\- Excel

\- Python

\- Power BI

\- AI-based QC analysis

\- Automated daily QC reports

