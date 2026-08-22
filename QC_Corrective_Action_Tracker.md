\# QC Corrective Action Tracker — ATM Surveillance Devices



\## 1. Purpose



This document provides a sample corrective-action tracker for monitoring

QC defects and ensuring that corrective actions are assigned, completed,

and verified.



This is a hypothetical learning example.



\---



\## 2. Corrective Action Process



The basic corrective-action process is:



Defect → Root Cause → Corrective Action → Owner → Due Date → Status → Verification



The objective is to ensure that identified defects are not only fixed

but also verified to prevent recurrence.



\---



\## 3. Sample Corrective Action Tracker



| Action ID | Defect | Category | Root Cause | Corrective Action | Owner | Priority | Due Date | Status | Verification |

|---|---|---|---|---|---|---|---|---|---|

| CA-001 | Camera no video | HW | Loose connector | Replace connector and perform video test | HW | Critical | 2026-08-23 | Open | Pending |

| CA-002 | Router connectivity failure | EDGE | Incorrect configuration | Correct configuration and perform connectivity test | EDGE | High | 2026-08-24 | In Progress | Pending |

| CA-003 | Sensor not detected | HW | Sensor wiring issue | Correct wiring and perform sensor test | HW | Medium | 2026-08-25 | Open | Pending |

| CA-004 | Firmware issue | SW | Incorrect firmware version | Install approved firmware and perform regression test | SW | Medium | 2026-08-24 | In Progress | Pending |

| CA-005 | Serial number mismatch | QC | Incorrect labeling | Verify label against system record | QC | Low | 2026-08-23 | Closed | Passed |



\---



\## 4. Status Definitions



| Status | Meaning |

|---|---|

| Open | Action identified but work has not started |

| In Progress | Corrective action is currently being performed |

| Closed | Corrective action completed and verified |



\---



\## 5. Priority Definitions



| Priority | Meaning |

|---|---|

| Critical | May block shipment or affect a critical product function |

| High | Significant functional or customer impact |

| Medium | Requires correction but does not normally stop shipment |

| Low | Minor issue with limited business impact |



\---



\## 6. Ownership



| Owner | Responsibility |

|---|---|

| HW | Hardware-related corrective actions |

| SW | Software and firmware-related corrective actions |

| EDGE | Router, network and edge-device corrective actions |

| QC | Inspection, documentation and verification activities |



\---



\## 7. Management Summary



\### Total Corrective Actions



5



\### Critical Actions



1



\### High Actions



1



\### Medium Actions



2



\### Low Actions



1



\### Open Actions



2



\### In Progress Actions



2



\### Closed Actions



1



\---



\## 8. Management Observations



1\. Critical actions should receive immediate attention.



2\. Corrective actions should have a clearly identified owner.



3\. Every action should have a target completion date.



4\. Completed actions should be verified before closure.



5\. Repeated defects should be reviewed for Root Cause Analysis (RCA).



6\. Critical defects should be reviewed before shipment release.



\---



\## 9. Corrective Action Validation



\### Test Case 1 — Owner Check



Every corrective action must have an assigned owner.



Expected Result:



All 5 actions have an owner.



Result: PASS



\---



\### Test Case 2 — Status Check



Every corrective action must have a valid status.



Valid statuses:



\- Open

\- In Progress

\- Closed



Expected Result:



All 5 actions have a valid status.



Result: PASS



\---



\### Test Case 3 — Verification Check



Every Closed action must have a verification result.



Expected Result:



CA-005 is Closed and has verification status = Passed.



Result: PASS



\---



\### Test Case 4 — Priority Check



Every corrective action must have a priority.



Expected Result:



All 5 actions have a defined priority.



Result: PASS



\---



\### Test Case 5 — Due Date Check



Every corrective action must have a target due date.



Expected Result:



All 5 actions have a due date.



Result: PASS



\---



\## 10. Management Logic



The tracker follows a simple management logic:



1\. Identify the defect.

2\. Determine the likely root cause.

3\. Define the corrective action.

4\. Assign an owner.

5\. Set a target completion date.

6\. Track the action status.

7\. Verify the completed action.

8\. Close the action only after successful verification.



\---



\## 11. Recommended KPI



The corrective-action tracker can later be used to calculate:



\### Corrective Action Closure Rate



Closure Rate (%) =

Closed Corrective Actions / Total Corrective Actions × 100



Example:



Closed Actions = 1



Total Actions = 5



Closure Rate = 1 / 5 × 100



Closure Rate = 20%



\---



\## 12. Future Improvements



This tracker can later be automated using:



\- Excel

\- Power BI

\- Python

\- Automated QC dashboards

\- AI-assisted RCA

\- Automated overdue-action alerts



\---



\## 13. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company information.

\- Root causes shown are initial sample assumptions.

\- Actual RCA should be validated using technical evidence.

\- Corrective actions should be verified before closure.

