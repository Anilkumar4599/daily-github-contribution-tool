\# Day 84 — QC Defect Reporting Process Improvement



\## 1. Process Improvement Example



\### Process Name



QC Defect Reporting and Management



\### Objective



Improve the process of recording, validating, prioritizing, and communicating

QC defects so that important issues can be identified and escalated quickly.



\---



\# 2. BEFORE Process



In the previous process, QC defects may be recorded manually in a tracker

with different levels of detail.



\### Typical Before Process



1\. QC engineer identifies a defect.

2\. Defect is entered into the tracker.

3\. Basic information such as defect number and description is recorded.

4\. HW or SW ownership may be entered manually.

5\. Priority may be assigned without complete supporting information.

6\. The development team reviews the defect.

7\. Additional information may be requested later.

8\. QC updates the tracker after receiving responses.

9\. Management receives a summary periodically.



\### Example BEFORE Record



| Field | Value |

|---|---|

| Defect No. | DEF-1025 |

| Description | Camera not working |

| Priority | High |

| Owner | HW |

| Status | Open |

| Trials | Not recorded |

| Failure % | Not recorded |

| Module | Not recorded |

| Business Impact | Not recorded |

| Reproduction Procedure | Not recorded |

| Evidence | Not attached |



\### Problems in the BEFORE Process



\- Important validation information may be missing.

\- Priority may not be supported by sufficient evidence.

\- Failure frequency may not be known.

\- The affected module may be unclear.

\- Reproduction steps may be missing.

\- HW/SW ownership may require further investigation.

\- Management may not immediately know the business impact.

\- Additional clarification can delay defect resolution.



\---



\# 3. AFTER Process



The improved process introduces mandatory validation fields before a defect

is treated as a fully analyzed issue.



\### Improved Process



1\. QC identifies a defect.

2\. QC records the defect number and description.

3\. Affected device/module is identified.

4\. HW/SW/EDGE/HW+SW ownership is classified.

5\. Priority is recorded.

6\. Number of trials is recorded.

7\. Failure percentage is calculated or recorded.

8\. The defect is classified as reproducible or intermittent.

9\. Business impact is documented.

10\. Reproduction steps are recorded.

11\. Logs, screenshots, videos, or test reports are attached where available.

12\. Missing information is clearly identified.

13\. Show-stopper defects are separately identified.

14\. The responsible team receives the validated defect.

15\. Management receives a focused summary of high-impact issues.



\---



\# 4. AFTER Record



The same fictional defect is now documented with additional information.



| Field | Value |

|---|---|

| Defect No. | DEF-1025 |

| Description | Camera video unavailable after system restart |

| Priority | High |

| Owner | HW+SW |

| Status | Open |

| Trials | 10 |

| Failure % | 80% |

| Failure Type | Reproducible |

| Affected Module | Camera interface |

| Business Impact | Live video unavailable for monitoring |

| Reproduction Procedure | Restart system and verify camera video |

| Evidence | Test report and screenshots attached |

| Blocks Function? | Yes |

| Blocked Function | Live camera monitoring |



\---



\# 5. Before vs After Comparison



| Area | BEFORE | AFTER |

|---|---|---|

| Defect description | Basic | Specific and functional |

| Module identification | Missing | Recorded |

| Ownership | Manual/unclear | HW+SW classification |

| Number of trials | Missing | 10 |

| Failure percentage | Missing | 80% |

| Failure behavior | Unknown | Reproducible |

| Business impact | Missing | Documented |

| Reproduction steps | Missing | Documented |

| Evidence | Missing | Attached |

| Function blocked | Unknown | Yes |

| Escalation decision | Difficult | Better supported by evidence |



\---



\# 6. Example Input



The following is a fictional example input received from QC.



```text

Defect No      : DEF-1025

Description    : Camera not working

Priority       : High

Trials         : 10

Failures       : 8

Module         : Camera interface

Status         : Open

Evidence       : Screenshot attached

