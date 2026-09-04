\# QC Dashboard Data Dictionary



\## 1. Purpose



This document defines the fields required for a future QC

Power BI dashboard.



The objective is to ensure that QC data is consistently

defined before dashboard development.



This is a hypothetical learning example.



\---



\## 2. Data Dictionary



| Field Name | Description | Data Type | Example | Mandatory |

|---|---|---|---|---|

| Defect ID | Unique defect number | Text | DEF-001 | Yes |

| Defect Date | Date defect was identified | Date | 2026-09-04 | Yes |

| Product | Product/device affected | Text | Lobby Camera | Yes |

| Category | HW/SW/EDGE/QC | Text | HW | Yes |

| Priority | Defect severity | Text | Critical | Yes |

| Status | Current defect status | Text | Open | Yes |

| Owner | Responsible team | Text | HW | Yes |

| Failure Count | Number of failures | Number | 5 | Yes |

| Total Tested | Total units tested | Number | 100 | Yes |

| Failure Rate | Failure percentage | Decimal | 5% | No |

| Root Cause | Identified root cause | Text | Loose connector | No |

| Corrective Action | Action taken to fix defect | Text | Replace connector | No |

| Verification Status | Verification result | Text | Passed | No |

| Closure Date | Date defect was closed | Date | 2026-09-05 | No |



\---



\## 3. Sample Input



| Defect ID | Product | Category | Priority | Status | Owner | Failure Count | Total Tested |

|---|---|---|---|---|---|---:|---:|

| DEF-001 | Lobby Camera | HW | Critical | Open | HW | 5 | 100 |

| DEF-002 | Router | EDGE | High | In Progress | EDGE | 3 | 100 |

| DEF-003 | Firmware | SW | Medium | Closed | SW | 2 | 100 |



\---



\## 4. Expected Output



Failure Rate:



Failure Rate = Failure Count / Total Tested × 100



DEF-001:



5 / 100 × 100 = 5%



DEF-002:



3 / 100 × 100 = 3%



DEF-003:



2 / 100 × 100 = 2%



\---



\## 5. Power BI KPI Candidates



The following KPIs can be created from this data:



1\. Total Defects

2\. Critical Defects

3\. High Defects

4\. Medium Defects

5\. Open Defects

6\. Closed Defects

7\. Failure Rate

8\. Defects by Category

9\. Defects by Owner

10\. Defects by Product



\---



\## 6. Data Validation Rules



1\. Defect ID must not be blank.

2\. Priority must be Critical, High, Medium or Low.

3\. Category must be HW, SW, EDGE or QC.

4\. Status must be Open, In Progress or Closed.

5\. Failure Count must not be negative.

6\. Total Tested must be greater than zero.

7\. Failure Count must not exceed Total Tested.



\---



\## 7. Test Cases



\### Test Case 1 — Valid Record



Input:



Failure Count = 5

Total Tested = 100



Expected:



Failure Rate = 5%



Result: PASS





\### Test Case 2 — Zero Total Tested



Input:



Failure Count = 5

Total Tested = 0



Expected:



Invalid Input — Total Tested must be greater than zero.



Result: PASS





\### Test Case 3 — Invalid Failure Count



Input:



Failure Count = 110

Total Tested = 100



Expected:



Invalid Input — Failure Count cannot exceed Total Tested.



Result: PASS





\### Test Case 4 — Invalid Priority



Input:



Priority = Urgent



Expected:



Invalid Input — Priority must be Critical, High, Medium or Low.



Result: PASS



\---



\## 8. Assumptions



\- This is a hypothetical learning dataset.

\- Actual QC data should be validated before dashboard development.

\- Defect ID should be unique.

\- Failure Rate should be calculated only when Total Tested is greater than zero.

\- Power BI will be used later for visualization.



\---



\## 9. Future Power BI Dashboard



The data dictionary can later support:



\- QC KPI cards

\- Defect trend charts

\- Pareto analysis

\- Defect category analysis

\- Team-wise defect analysis

\- Product-wise defect analysis

\- Critical defect alerts

\- Failure-rate trends

