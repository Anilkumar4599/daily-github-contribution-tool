\# QC Recurring Defect Tracker — ATM Surveillance Devices



\## 1. Purpose



This tracker identifies recurring defects using a small hypothetical

sample dataset.



The objective is to identify defects that occur repeatedly and help

QC management prioritize Root Cause Analysis (RCA), corrective action,

and recurrence monitoring.



\---



\## 2. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company records.

\- Each occurrence represents one observed defect.

\- Recurring defect means a defect category occurring two or more times.

\- Severity is based on the potential business impact.

\- Possible ownership is an initial classification and requires technical validation.

\- Actual defect records should be validated before management reporting.



\---



\## 3. Sample Defect Data



| Defect ID | Device | Defect Description | Severity | Ownership | Occurrence |

|---|---|---|---|---|---:|

| DEF-001 | Router | Network connectivity failure | High | EDGE | 6 |

| DEF-002 | Lobby Camera | No video output | Critical | HW | 5 |

| DEF-003 | Sensor Bag | Sensor not detected | Medium | HW | 3 |

| DEF-004 | Main Unit | Firmware issue | Medium | SW | 2 |

| DEF-005 | Outdoor Camera | Intermittent restart | High | HW+SW | 2 |

| DEF-006 | Main Unit | Serial number mismatch | Low | QC | 1 |



\---



\## 4. Recurring Defect Classification



A defect is considered recurring when its occurrence count is

two or more.



| Defect Description | Occurrences | Recurring? |

|---|---:|---|

| Network connectivity failure | 6 | Yes |

| No video output | 5 | Yes |

| Sensor not detected | 3 | Yes |

| Firmware issue | 2 | Yes |

| Intermittent restart | 2 | Yes |

| Serial number mismatch | 1 | No |



\---



\## 5. Recurring Defect Summary



| Rank | Defect | Occurrences | Severity | Ownership |

|---:|---|---:|---|---|

| 1 | Network connectivity failure | 6 | High | EDGE |

| 2 | No video output | 5 | Critical | HW |

| 3 | Sensor not detected | 3 | Medium | HW |

| 4 | Firmware issue | 2 | Medium | SW |

| 5 | Intermittent restart | 2 | High | HW+SW |



\---



\## 6. Management Priority



The following defects require priority investigation:



\### Priority 1 — No Video Output



\- Occurrences: 5

\- Severity: Critical

\- Ownership: HW

\- Management concern: Surveillance footage may be unavailable.



Recommended action:



\- Validate camera and cable connections.

\- Check power supply.

\- Review failure evidence.

\- Perform RCA.

\- Re-test after corrective action.



\---



\### Priority 2 — Network Connectivity Failure



\- Occurrences: 6

\- Severity: High

\- Ownership: EDGE

\- Management concern: Connectivity problems may affect remote

&#x20; monitoring and footage availability.



Recommended action:



\- Check router configuration.

\- Check SIM/network signal.

\- Review recurring sites.

\- Check restart frequency.

\- Perform RCA.



\---



\### Priority 3 — Sensor Not Detected



\- Occurrences: 3

\- Severity: Medium

\- Ownership: HW

\- Management concern: Sensor functionality may be affected.



Recommended action:



\- Check sensor wiring.

\- Verify connector condition.

\- Test the sensor.

\- Replace the sensor if required.

\- Monitor recurrence.



\---



\## 7. QA Validation



\### Test 1 — Recurring Classification



A defect with two or more occurrences should be classified as recurring.



Expected:



\- Occurrence = 1 → Not Recurring

\- Occurrence >= 2 → Recurring



Result: PASS



\---



\### Test 2 — Highest Occurrence



The defect with the highest occurrence count should be:



\*\*Network connectivity failure = 6 occurrences\*\*



Result: PASS



\---



\### Test 3 — Critical Recurring Defect



The sample contains one Critical recurring defect:



\*\*No video output = 5 occurrences\*\*



Result: PASS



\---



\### Test 4 — Non-Recurring Defect



Serial number mismatch has:



\*\*1 occurrence\*\*



Therefore:



\*\*Not Recurring\*\*



Result: PASS



\---



\## 8. Management Observations



1\. Network connectivity failure has the highest recurrence count.

2\. No video output is the most important recurring defect by severity.

3\. Hardware-related recurring defects require focused RCA.

4\. EDGE-related network issues should be reviewed for site-level recurrence.

5\. Repeated defects should be tracked after corrective action.

6\. Recurrence should be monitored weekly or monthly.

7\. Critical recurring defects should be reviewed before shipment or release.



\---



\## 9. Recommended KPI



Management can track:



\*\*Recurring Defect Rate (%)\*\*



Formula:



Recurring Defect Occurrences / Total Defect Occurrences × 100



For this sample:



Total occurrences:



6 + 5 + 3 + 2 + 2 + 1 = 19



Recurring occurrences:



6 + 5 + 3 + 2 + 2 = 18



Recurring Defect Rate:



18 / 19 × 100 = 94.74%



\---



\## 10. Management Conclusion



The sample analysis shows that recurring defects represent a significant

portion of the observed defect occurrences.



Network connectivity failure has the highest occurrence count, while

No Video Output is the most critical recurring defect.



QC management should prioritize RCA based on both:



1\. Frequency of recurrence

2\. Business impact / severity



Recurring defects should be monitored after corrective action to confirm

that the problem does not return.



\---



\## 11. Future Automation



This tracker can later be automated using:



\- Excel

\- Python

\- Power BI

\- AI-based QC analysis

\- Automated recurring-defect alerts

\- Weekly QC management reports



\---



\## 12. Disclaimer



This is a hypothetical learning project.



The sample data does not represent actual company defect records or

confidential business information.

