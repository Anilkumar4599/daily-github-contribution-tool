\# QC Pareto Analysis — ATM Surveillance Devices



\## Purpose



This project demonstrates a sample Pareto analysis of defects found

during QC inspection of ATM surveillance devices.



The objective is to identify the defect categories contributing the

largest share of total defects and help management prioritize corrective

actions.



\## Assumptions



\- This is a hypothetical sample dataset created for learning.

\- The data does not represent actual company defect records.

\- Each number represents the count of defects recorded for a category.

\- Defect counts must be whole numbers greater than or equal to zero.

\- Categories are arranged from highest defect count to lowest defect count.

\- The Pareto analysis is intended to support QC prioritization and RCA.



\## Sample Defect Data



| Rank | Defect Category | Defect Count |

|---:|---|---:|

| 1 | Camera No Video | 18 |

| 2 | Router / Network Issue | 12 |

| 3 | Power Failure | 8 |

| 4 | Sensor Issue | 5 |

| 5 | Storage Issue | 4 |

| 6 | Communication Failure | 3 |



\*\*Total Defects: 50\*\*



\## Pareto Calculation



| Rank | Defect Category | Count | Percentage | Cumulative Percentage |

|---:|---|---:|---:|---:|

| 1 | Camera No Video | 18 | 36% | 36% |

| 2 | Router / Network Issue | 12 | 24% | 60% |

| 3 | Power Failure | 8 | 16% | 76% |

| 4 | Sensor Issue | 5 | 10% | 86% |

| 5 | Storage Issue | 4 | 8% | 94% |

| 6 | Communication Failure | 3 | 6% | 100% |



\## Pareto Findings



The top three defect categories are:



1\. Camera No Video — 36%

2\. Router / Network Issue — 24%

3\. Power Failure — 16%



Together, these three categories account for \*\*76% of the total defects\*\*.



Therefore, QC management should initially focus corrective and preventive

actions on these three areas.



\## Recommended Management Actions



\### 1. Camera No Video



\- Check camera power supply.

\- Check cable and connector quality.

\- Verify camera configuration.

\- Analyze recurring camera models/vendors.

\- Perform RCA for repeated failures.



\### 2. Router / Network Issue



\- Check SIM and network signal.

\- Review router restart frequency.

\- Check configuration and firmware.

\- Identify recurring locations or router models.

\- Review vendor performance.



\### 3. Power Failure



\- Check power supply and DCUPS.

\- Verify battery performance.

\- Check wiring and connectors.

\- Analyze recurring hardware failures.

\- Review supplier/component quality.



\## Input Validation Rules



The following rules should be applied before calculating Pareto results:



\- Defect category must not be blank.

\- Defect count must be a number.

\- Defect count must be a whole number.

\- Defect count cannot be negative.

\- Total defect count must be greater than zero.



\## QA Validation



Expected total defects:



\*\*18 + 12 + 8 + 5 + 4 + 3 = 50\*\*



Expected top-three cumulative percentage:



\*\*36% + 24% + 16% = 76%\*\*



Expected final cumulative percentage:



\*\*100%\*\*



\## Conclusion



Pareto analysis helps QC management identify the small number of defect

categories that contribute most of the overall defect volume.



In this sample, Camera No Video, Router / Network Issue, and Power Failure

represent 76% of total defects and should receive priority for RCA and

corrective action.



\## Future Improvement



This manual analysis can later be automated using:



\- Python

\- Excel

\- Power BI

\- Automated QC reports

