\# QC Root-Cause Analysis (RCA) Template



\## 1. Purpose



This template provides a structured method for investigating QC defects.



The objective is to identify the immediate cause and root cause of a defect,

define corrective and preventive actions, and verify that the defect has

been effectively resolved.



This is a hypothetical learning example.



\---



\## 2. RCA Process



The basic RCA flow is:



Problem

↓

Evidence Collection

↓

Immediate Cause

↓

Root Cause

↓

Corrective Action

↓

Preventive Action

↓

Verification

↓

Closure



\---



\## 3. RCA Information



| Field | Details |

|---|---|

| Defect ID | DEF-RCA-001 |

| Device | Lobby Camera |

| Defect | No video output |

| Severity | Critical |

| Ownership | HW |

| Date Identified | Sample Date |

| Status | Under Investigation |



\---



\## 4. Problem Statement



The Lobby Camera does not provide video output during QC inspection.



The defect prevents successful completion of the surveillance video

functionality test.



\---



\## 5. Evidence



The following evidence should be collected before confirming the root cause:



\- QC inspection result

\- Camera power status

\- Cable/connector condition

\- Video output test result

\- Test screenshots

\- Device logs, if available

\- Reproduction steps

\- Previous occurrence history



\---



\## 6. Pre-Analysis Validation



Before starting RCA, confirm:



| Validation Item | Status |

|---|---|

| Defect number available | PASS |

| Defect description available | PASS |

| Severity available | PASS |

| Device identified | PASS |

| Reproduction procedure available | PASS |

| Evidence/logs available | REVIEW |

| Failure frequency known | REVIEW |

| Ownership confirmed | REVIEW |



\### Important Rule



Do not assume a root cause when evidence is missing.



If information is unavailable, mark it as:



\*\*Unknown / Information Required\*\*



\---



\## 7. Immediate Cause



\### Question



What directly caused the failure during the test?



\### Example



Video output was unavailable because the camera was not successfully

communicating with the test system.



\### Status



Initial hypothesis — requires technical validation.



\---



\## 8. Root Cause



\### Question



Why did the immediate cause occur?



\### Example Investigation



Possible areas:



1\. Camera hardware

2\. Cable or connector

3\. Power supply

4\. Configuration

5\. Firmware

6\. Manufacturing process

7\. Supplier component



\### Root Cause



\*\*Not confirmed — technical investigation required.\*\*



Do not classify a suspected cause as a confirmed root cause until

supporting evidence is available.



\---



\## 9. Five-Why Analysis



\### Why 1



Why was there no video output?



\*\*Because the camera was not communicating with the test system.\*\*



\### Why 2



Why was the camera not communicating?



\*\*Cause not yet confirmed.\*\*



\### Why 3



Why is the cause not confirmed?



\*\*Required technical evidence has not yet been completed.\*\*



\### Why 4



What evidence is required?



\- Cable/connector inspection

\- Power verification

\- Camera substitution test

\- Configuration verification

\- Log review



\### Why 5



What is required before final RCA closure?



\*\*Technical validation and repeat testing.\*\*



\---



\## 10. Corrective Action



Corrective action should address the immediate problem.



Example actions:



\- Inspect cable and connector.

\- Verify camera power.

\- Replace defective component if confirmed.

\- Correct configuration if applicable.

\- Re-test the camera.



\### Corrective Action Owner



\*\*HW Team\*\*



\### Status



Open



\---



\## 11. Preventive Action



Preventive action should reduce the chance of recurrence.



Possible actions:



\- Add connector inspection to QC checklist.

\- Add camera video-output verification before shipment.

\- Review recurring failure trends.

\- Improve supplier quality checks if supplier-related cause is confirmed.

\- Monitor recurrence after corrective action.



\---



\## 12. Verification



After corrective action, perform:



| Verification | Expected Result | Status |

|---|---|---|

| Camera power test | Power available | PASS |

| Cable/connector test | Connection stable | PASS |

| Video output test | Video available | PASS |

| Repeat test | No recurrence | PASS |



\---



\## 13. Closure Criteria



The RCA should not be closed until:



\- Root cause is supported by evidence.

\- Corrective action is completed.

\- Verification testing is completed.

\- No recurrence is observed during agreed monitoring period.

\- Required evidence is attached.

\- QC approval is completed.



\---



\## 14. Management Summary



\### Problem



Lobby Camera has no video output.



\### Impact



Surveillance video functionality cannot be confirmed.



\### Immediate Cause



Camera communication failure — pending technical validation.



\### Root Cause



Not confirmed.



\### Corrective Action



Inspect, repair/replace the affected component and re-test.



\### Preventive Action



Strengthen inspection and monitor recurrence.



\### Current Status



\*\*Under Investigation\*\*



\---



\## 15. Assumptions



\- This is a hypothetical learning example.

\- The defect does not represent actual company data.

\- The root cause has intentionally not been assumed.

\- Technical teams must validate the actual root cause.

\- Evidence should be reviewed before final RCA approval.



\---



\## 16. Final RCA Principle



\*\*No evidence = No confirmed root cause.\*\*



A suspected cause should remain a hypothesis until technical evidence

supports the conclusion.

