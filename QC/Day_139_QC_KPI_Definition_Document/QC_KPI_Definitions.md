

\# Day 139 – QC KPI Definition Document



\## 1. Purpose



This document defines the key Quality Control (QC) Key Performance Indicators (KPIs) used to monitor inspection performance, product quality, defects and rework activities for ATM E-Surveillance devices.



The purpose is to establish consistent KPI definitions, calculation formulas, reporting methods and management interpretation.



\## 2. QC KPI Definitions



\### KPI 1 – Inspection Coverage



\*\*Purpose:\*\* Measures how much of the received quantity has been inspected.



Formula:



Inspection Coverage (%) = (Inspected Quantity / Received Quantity) × 100



Example:

\- Received Quantity: 120

\- Inspected Quantity: 100

\- Result: 83.33%



Interpretation: 83.33% of received devices have been inspected.



\### KPI 2 – First Pass Yield (FPY)



\*\*Purpose:\*\* Measures the percentage of inspected devices accepted without requiring rework or correction during the first inspection.



Formula:



FPY (%) = (First Pass Accepted Quantity / Inspected Quantity) × 100



Example:

\- Inspected Quantity: 100

\- First Pass Accepted: 85

\- Result: 85%



Interpretation: 85% of inspected devices passed the first inspection.



\### KPI 3 – First Pass Failure Rate



\*\*Purpose:\*\* Measures the percentage of inspected devices that failed the first inspection.



Formula:



First Pass Failure Rate (%) = (First Pass Failed Quantity / Inspected Quantity) × 100



Example:

\- Inspected Quantity: 100

\- First Pass Failed: 15

\- Result: 15%



Interpretation: 15% of inspected devices failed the first inspection.



\### KPI 4 – Defective Unit Rate



\*\*Purpose:\*\* Measures the percentage of inspected devices identified as defective.



Formula:



Defective Unit Rate (%) = (Unique Defective Units / Inspected Quantity) × 100



Example:

\- Inspected Quantity: 100

\- Unique Defective Units: 12

\- Result: 12%



Interpretation: 12% of inspected devices were identified as defective.



Note: Defective units and defect incidents are different. One device may have multiple defect incidents.



\### KPI 5 – Rework Rate



\*\*Purpose:\*\* Measures the percentage of inspected devices requiring rework.



Formula:



Rework Rate (%) = (Units Requiring Rework / Inspected Quantity) × 100



Example:

\- Inspected Quantity: 100

\- Units Requiring Rework: 10

\- Result: 10%



Interpretation: 10% of inspected devices required rework.



\### KPI 6 – Rework Closure Rate



\*\*Purpose:\*\* Measures the percentage of rework items completed out of the total items requiring rework in the reporting group.



Formula:



Rework Closure Rate (%) = (Rework Units Completed / Units Requiring Rework) × 100



Example:

\- Units Requiring Rework: 10

\- Units Rework Completed: 8

\- Result: 80%



Interpretation: 80% of the rework items have been completed.



\### KPI 7 – Recurring Defect Incident Rate



\*\*Purpose:\*\* Measures the percentage of defect incidents that are repeat occurrences of previously recorded defects for the same device and defect category.



Formula:



Recurring Defect Incident Rate (%) = (Repeat Defect Incidents / Total Defect Incidents) × 100



Example:

\- Total Defect Incidents: 20

\- Repeat Defect Incidents: 6

\- Result: 30%



Interpretation: 30% of recorded defect incidents are repeat occurrences.



\## 3. Sample Input Data



File: sample\_qc\_kpi\_input.csv



| Parameter | Sample Value |

|---|---:|

| Reporting Date | 19-Nov-2026 |

| Received Quantity | 120 |

| Inspected Quantity | 100 |

| First Pass Accepted | 85 |

| First Pass Failed | 15 |

| Unique Defective Units | 12 |

| Units Requiring Rework | 10 |

| Units Rework Completed | 8 |

| Total Defect Incidents | 20 |

| Repeat Defect Incidents | 6 |



\## 4. Expected KPI Output



| KPI | Expected Result |

|---|---:|

| Inspection Coverage | 83.33% |

| First Pass Yield | 85.00% |

| First Pass Failure Rate | 15.00% |

| Defective Unit Rate | 12.00% |

| Rework Rate | 10.00% |

| Rework Closure Rate | 80.00% |

| Recurring Defect Incident Rate | 30.00% |



\## 5. Data Validation Rules



Before calculating the KPIs, verify:



1\. Received Quantity must be greater than zero.

2\. Inspected Quantity cannot exceed Received Quantity.

3\. First Pass Accepted + First Pass Failed must equal Inspected Quantity.

4\. Unique Defective Units cannot exceed Inspected Quantity.

5\. Units Requiring Rework cannot exceed Inspected Quantity.

6\. Rework Units Completed cannot exceed Units Requiring Rework.

7\. Repeat Defect Incidents cannot exceed Total Defect Incidents.

8\. All quantity values must be zero or positive.



\## 6. KPI Reporting Frequency



| KPI | Suggested Frequency |

|---|---|

| Inspection Coverage | Daily |

| First Pass Yield | Daily / Monthly |

| First Pass Failure Rate | Daily / Monthly |

| Defective Unit Rate | Daily / Monthly |

| Rework Rate | Daily / Monthly |

| Rework Closure Rate | Daily / Monthly |

| Recurring Defect Incident Rate | Weekly / Monthly |



\## 7. Management Application



These KPIs help management:



\- Monitor inspection efficiency.

\- Identify quality performance trends.

\- Measure first-pass acceptance.

\- Monitor defective devices.

\- Track rework workload and closure.

\- Identify recurring defects requiring Root Cause Analysis.

\- Prioritize corrective and preventive actions.



\## 8. Important KPI Measurement Notes



\- Use the same reporting period for all quantities in a calculation.

\- Count unique defective devices separately from individual defect incidents.

\- Define recurring incidents consistently using device and defect-category history.

\- Do not treat rework closure as first-pass acceptance.

\- Establish KPI targets using company baselines, customer requirements and operational priorities.



\## 9. Conclusion



A consistent QC KPI framework enables better quality monitoring, measurable performance reporting, faster identification of recurring issues and improved management decisions.



Practice data in this document is fictional and intended for learning purposes.



