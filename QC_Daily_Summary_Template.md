\# QC Daily Summary — ATM E-Surveillance



\## 1. Daily Summary Information



| Field | Value |

|---|---|

| Date | |

| Prepared By | |

| Shift / Team | |

| Production / QC Area | |



\## 2. QC Inspection Summary



| Metric | Count |

|---|---:|

| Units Received for QC | |

| Units Inspected | |

| Units Passed | |

| Units Failed | |

| Pending Inspection | |



\## 3. Defect Severity Summary



| Severity | Count |

|---|---:|

| Critical | |

| High | |

| Medium | |

| Low | |

| Total Defects | |



\## 4. Defect Ownership



| Ownership | Count |
|---|---:|
| Hardware (HW) | |
| Software (SW) | |
| HW + SW | |
| EDGE | |
| QC / Documentation | |
| Unknown / Pending Analysis | |

\## 5. Top Defects



| Rank | Defect | Device | Severity | Ownership | Status |

|---:|---|---|---|---|---|

| 1 | | | | | |

| 2 | | | | | |

| 3 | | | | | |

| 4 | | | | | |

| 5 | | | | | |



\## 6. Show-Stoppers / Blocking Issues



| Defect | Impact | Owner | Required Action | Target Date |

|---|---|---|---|---|

| | | | | |



\## 7. Today's Key Observations



\- 

\- 

\- 



\## 8. Recommended Management Actions



1\. 

2\. 

3\. 



\---



\# Example Input



The following is a hypothetical example for learning and testing.



\### Daily Information



| Field | Example |

|---|---|

| Date | 16-Aug-2026 |

| Prepared By | QC Team |

| Shift / Team | Day Shift |

| Production / QC Area | ATM E-Surveillance |



\### QC Inspection Data



| Metric | Count |

|---|---:|

| Units Received for QC | 100 |

| Units Inspected | 100 |

| Units Passed | 92 |

| Units Failed | 8 |

| Pending Inspection | 0 |



\### Defect Data



| Defect | Device | Severity | Ownership | Count |

|---|---|---|---|---:|

| No video output | Lobby Camera | Critical | HW | 2 |

| Router connectivity failure | Router | High | EDGE | 2 |

| DCUPS backup failure | DCUPS | High | HW | 1 |

| Sensor not detected | Sensor Bag | Medium | HW | 1 |

| Firmware issue | Main Unit | Medium | SW | 1 |

| Serial number mismatch | Main Unit | Low | QC | 1 |



\### Expected Output



Based on the example input:



\- Units Inspected = \*\*100\*\*

\- Units Passed = \*\*92\*\*

\- Units Failed = \*\*8\*\*

\- Pending Inspection = \*\*0\*\*

\- Total Defects = \*\*8\*\*

\- Critical = \*\*2\*\*

\- High = \*\*3\*\*

\- Medium = \*\*2\*\*

\- Low = \*\*1\*\*

\- HW = \*\*4\*\*

\- SW = \*\*1\*\*

\- EDGE = \*\*2\*\*

\- QC / Documentation = \*\*1\*\*



\### Expected Management Summary



> \*\*QC inspected 100 units today. 92 units passed and 8 units failed. A total of 8 defects were identified, including 2 Critical and 3 High-severity defects. The main concerns are Lobby Camera no-video issues and Router connectivity failures. HW and EDGE teams should prioritize the Critical and High defects. The Lobby Camera issue is considered a potential show-stopper until the failure is resolved and the unit passes re-test.\*\*



\## QA Validation Checks



Before publishing the daily summary:



1\. Units Inspected must equal Passed + Failed + Pending.

2\. Total defect count must equal the sum of Critical + High + Medium + Low.

3\. Ownership counts must reconcile with the defect records.

4\. Critical defects must be reviewed before shipment.

5\. Show-stopper issues must have an owner and action.

6\. Missing information must be identified rather than assumed.



\## Assumptions



\- This is a hypothetical sample dataset created for learning.

\- The example does not represent actual company QC data.

\- Severity and ownership classifications are sample classifications.

\- Actual defects should be validated using evidence, logs, screenshots and technical analysis.



\## Future Improvement



This template can later be automated using:



\- Excel

\- Python

\- Power BI

\- AI-based QC analysis

\- Automated daily management reports

