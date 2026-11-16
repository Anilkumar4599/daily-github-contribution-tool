

\# Day 136 – Recurring-Defect Tracker



\## Objective

Build a simple Python tool to identify recurring QC defects using sample ATM E-Surveillance inspection records.



\## Business Purpose

Recurring defects help the QC team identify repeated quality problems and prioritize investigation, corrective actions, and supplier discussions.



\## Recurrence Rule

A device and defect-category combination is classified as recurring when it appears in two or more records.



\## Assumptions

1\. Each CSV row represents one defect incident.

2\. Records are grouped by device name and defect category.

3\. Two or more records indicate recurrence.

4\. One record indicates a non-recurring defect.

5\. Severity is assumed consistent for each device/defect combination.

6\. First and last reported dates refer only to the supplied dataset.

7\. Sample data is for learning and does not establish a confirmed root cause.



\## Sample Results



| Device | Defect | Occurrences | Status |

|---|---|---:|---|

| ATM Main Unit | Power Failure | 2 | Recurring |

| Lobby Camera | No Video | 2 | Recurring |

| Outdoor Camera | Intermittent Restart | 2 | Recurring |

| DCUPS | Backup Failure | 1 | Not Recurring |

| Router | Network Connectivity | 1 | Not Recurring |



\## Summary

\- Total defect incidents: 8

\- Unique device/defect groups: 5

\- Recurring defect groups: 3

\- Incidents in recurring groups: 6



\## Files

\- sample\_defects.csv – Sample defect incident data.

\- recurring\_defect\_tracker.py – Tracker program.

\- test\_recurring\_defect\_tracker.py – Automated tests.

\- recurring\_defect\_report.csv – Generated tracker report.



\## How to Run



Run `python recurring\_defect\_tracker.py`



Run `python -m unittest -v test\_recurring\_defect\_tracker.py`



\## Learning Outcome

Understand how to group QC incidents, count repeated defects, identify recurrence, and generate a CSV report using Python.



