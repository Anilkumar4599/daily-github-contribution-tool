\# QC Rework Tracking Table



\## 1. Purpose



This document provides a simple method for tracking QC rework activities.



The objective is to identify:



\- Which devices require rework

\- Type of defect

\- Responsible team

\- Rework status

\- Rework duration

\- Final verification result

\- Recurring rework patterns



This is a hypothetical learning example.



\---



\## 2. Rework Tracking Table



| Rework ID | Defect ID | Device | Defect | Owner | Rework Required | Rework Time (min) | Verification | Status |

|---|---|---|---|---|---|---:|---|---|

| RW-001 | DEF-001 | Main Unit | Power failure | HW | PCB replacement | 45 | PASS | Closed |

| RW-002 | DEF-002 | Lobby Camera | No video | HW | Camera replacement | 30 | PASS | Closed |

| RW-003 | DEF-003 | Router | Network failure | EDGE | Configuration correction | 20 | PASS | Closed |

| RW-004 | DEF-004 | Sensor Bag | Sensor not detected | HW | Sensor replacement | 25 | PASS | Closed |

| RW-005 | DEF-005 | Main Unit | Firmware issue | SW | Firmware update | 35 | PASS | Closed |

| RW-006 | DEF-006 | Lobby Camera | No video | HW | Cable replacement | 15 | FAIL | Rework Required |



\---



\## 3. Rework Summary



| Metric | Value |

|---|---:|

| Total Rework Cases | 6 |

| Closed Cases | 5 |

| Rework Required | 1 |

| Total Rework Time | 170 minutes |

| Average Rework Time | 28.33 minutes |



\---



\## 4. Team-wise Rework



| Team | Rework Cases |

|---|---:|

| HW | 4 |

| SW | 1 |

| EDGE | 1 |



\---



\## 5. Defect-wise Observation



The sample data shows that camera-related problems can result in

multiple rework activities.



The Lobby Camera appears in two rework records.



This should be reviewed for possible recurrence.



\---



\## 6. Test Case 1 — Total Rework Cases



Expected:



Total Rework Cases = 6



Result:



PASS



\---



\## 7. Test Case 2 — Closed + Rework Required



Expected:



Closed Cases + Rework Required = Total Rework Cases



5 + 1 = 6



Result:



PASS



\---



\## 8. Test Case 3 — Rework Time Validation



Expected:



45 + 30 + 20 + 25 + 35 + 15 = 170 minutes



Result:



PASS



\---



\## 9. Test Case 4 — Team Count Validation



Expected:



HW + SW + EDGE = Total Rework Cases



4 + 1 + 1 = 6



Result:



PASS



\---



\## 10. Management Observations



1\. Five of the six sample rework cases were successfully closed.



2\. One Lobby Camera case requires additional rework.



3\. Hardware represents the largest share of rework cases in this sample.



4\. Repeated camera-related rework should be investigated through RCA.



5\. Rework duration should be monitored because excessive rework time

&#x20;  can affect production and shipment schedules.



\---



\## 11. Recommended Management Actions



\- Monitor recurring rework by device.

\- Identify high-frequency defect categories.

\- Track rework time by team.

\- Perform RCA for repeated failures.

\- Verify corrective actions.

\- Monitor rework trends weekly.

\- Escalate repeated Critical/High defects.



\---



\## 12. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company information.

\- Rework time is measured in minutes.

\- A case is considered Closed only after successful verification.

\- Actual QC data should be validated before management reporting.



\---



\## 13. Key KPI



A useful rework KPI is:



Rework Rate = Units Requiring Rework / Total Units Inspected × 100



Example:



If 8 out of 100 units require rework:



Rework Rate = 8 / 100 × 100 = 8%



\---



\## 14. Future Improvements



This tracker can later be automated using:



\- Excel

\- Power BI

\- Python

\- AI-assisted QC analysis

\- Automated daily QC reports

