\# Day 117 — Vendor Delivery Performance Analysis Prompt



\## 1. Objective



Create a reusable AI prompt to analyse vendor delivery performance from purchase-order records. The prompt should calculate delivery KPIs, identify late deliveries, validate input data, and recommend evidence-based supplier follow-up actions.



It must not invent delivery dates, supplier explanations, performance targets, or root causes.



\## 2. Reusable AI Prompt



\### ROLE



Act as a Senior Procurement and Supplier Performance Manager experienced in purchase-order tracking, delivery reliability, supplier follow-up, and supply-chain risk.



\### CONTEXT



I will provide PO-level or PO-line-level data for vendor delivery performance.



The data may include:



\- PO number and line number

\- Supplier name

\- Item or material

\- PO order date

\- Required delivery date

\- Actual delivery or goods-receipt date

\- PO status

\- Quantity ordered and received

\- Supplier's committed delivery date

\- Agreed delivery tolerance

\- Supplier performance target



\*\*Reporting date:\*\* \[Enter date]



\*\*Reporting period:\*\* \[Enter period]



\*\*On-time delivery definition:\*\* \[Enter the agreed company definition, including any tolerance]



If no delivery-performance definition or target is supplied, explicitly state that limitation. Do not invent a company policy.



\### TASK



\#### Step 1 — Validate the data



Check:

\- Missing PO numbers or supplier names

\- Duplicate PO or line identifiers

\- Invalid dates

\- Missing required delivery dates

\- Missing actual delivery dates for delivered orders

\- Conflicting status and delivery-date information

\- Missing quantities or supplier commitments

\- Inconsistent supplier names

\- Duplicate rows that could inflate counts



Do not silently delete duplicate-looking rows. Flag them for review because one PO may contain multiple valid line items or partial deliveries.



\#### Step 2 — Classify delivery status



Use the following classifications:



\- \*\*Delivered on time:\*\* Actual delivery date meets the defined delivery commitment.

\- \*\*Delivered late:\*\* Actual delivery date is after the defined delivery commitment, considering any documented tolerance.

\- \*\*Open and overdue:\*\* Order remains open after its required delivery date.

\- \*\*Open and not yet due:\*\* Order is open, but the required delivery date has not passed.

\- \*\*Delivery status unknown:\*\* Missing or conflicting information prevents classification.

\- \*\*Other status:\*\* Cancelled, partially delivered, or another explicitly supplied status requiring separate treatment.



Do not count open orders as completed deliveries. Define how partial deliveries are handled before calculating supplier KPIs.



\#### Step 3 — Calculate delivery KPIs



Calculate only metrics supported by valid records:



1\. Total eligible delivery records.

2\. Delivered on-time records.

3\. Delivered-late records.

4\. Open overdue orders.

5\. Open orders not yet due.

6\. Records with unknown delivery status.

7\. On-time delivery rate.

8\. Average calendar days late, if valid late-delivery dates are available.



Use the following formula when the eligible population and on-time definition are clear:



On-time delivery rate (%) = (Eligible deliveries delivered on time ÷ Total eligible completed deliveries) × 100



State the denominator and exclusions. Do not include open orders in the completed-delivery denominator. If the eligible completed-delivery population is zero, report the rate as unavailable rather than dividing by zero.



For late days, calculate:



Late days = Actual delivery date − Required delivery date



Use calendar days unless a different documented convention is supplied.



\#### Step 4 — Analyse vendor performance fairly



For each vendor, report:

\- Number of eligible completed deliveries

\- On-time and late counts

\- On-time delivery rate

\- Open overdue orders

\- Unknown or excluded records

\- Evidence-based observations



State the sample size. Do not compare suppliers as if their performance is directly equivalent when definitions, periods, or data completeness differ.



Do not label a supplier as poor-performing based on one isolated delay without considering sample size and the available evidence.



\#### Step 5 — Identify risk and recommend action



Highlight:

\- Repeated late deliveries supported by records

\- Open overdue POs

\- Critical deliveries only if criticality is supplied

\- Missing delivery commitments

\- Data-quality problems affecting KPI accuracy

\- Suppliers requiring further review



Recommend practical next steps, such as confirming delivery dates, requesting recovery plans, validating receiving records, or reviewing alternative supply options.



Do not claim a supplier caused production stoppage, financial loss, or customer impact unless evidence supports the claim.



\### REQUIRED OUTPUT



\#### A. Executive Summary



State the reporting period, number of records analysed, main delivery findings, and key data limitations.



\#### B. Data Validation Report



| Record / PO | Data Issue | Impact on Analysis | Corrective Action |

|---|---|---|---|



\#### C. Overall Delivery KPI Summary



| KPI | Result | Calculation Basis | Limitations |

|---|---|---|---|



\#### D. Vendor Performance Table



| Vendor | Eligible Deliveries | On-Time | Late | On-Time Rate | Open Overdue POs | Unknown Records |

|---|---:|---:|---:|---:|---:|---:|



\#### E. Overdue PO Follow-Up



| PO | Vendor | Due Date | Days Overdue | Confirmed Facts | Recommended Action |

|---|---|---|---:|---|---|



Calculate days overdue only when the status, due date, and reporting date support the calculation.



\#### F. Recommended Actions



Prioritise follow-up actions based on verified delivery exposure, documented criticality, and available evidence. Clearly label proposed owners and deadlines.



\#### G. Assumptions and Limitations



List missing dates, excluded records, delivery definitions, data-quality issues, and any conclusion that cannot yet be confirmed.



\### MANDATORY SAFEGUARDS



1\. Never invent delivery dates, supplier explanations, or performance targets.

2\. Never treat an open PO as a completed delivery.

3\. Never calculate on-time delivery performance without a clear definition and valid denominator.

4\. Never treat missing dates as on-time or late.

5\. Never combine partial deliveries without a documented rule.

6\. Never hide data exclusions or duplicate-record concerns.

7\. Never infer supplier negligence from a delay alone.

8\. Distinguish confirmed facts from potential risks.

9\. State the reporting date and whether days are calendar or working days.

10\. Explain any KPI that cannot be calculated reliably.



\## 3. Sample Input Dataset



The following dataset is fictional and is intended only for testing.



\*\*Reporting date:\*\* 28 October 2026.



| PO | Vendor | Status | Due Date | Actual Delivery Date |

|---|---|---|---|---|

| PO401 | Alpha Electronics | Delivered | 2026-10-20 | 2026-10-20 |

| PO402 | Alpha Electronics | Delivered | 2026-10-22 | 2026-10-25 |

| PO403 | Beta Power | Delivered | 2026-10-24 | 2026-10-23 |

| PO404 | Beta Power | Open | 2026-10-26 | Missing |

| PO405 | SecureParts | Open | 2026-10-30 | Missing |

| PO406 | SecureParts | Delivered | Missing | 2026-10-27 |



\### Sample assumptions



\- Each row represents one distinct PO and one eligible delivery record, unless stated otherwise.

\- Dates are valid calendar dates in YYYY-MM-DD format.

\- The on-time rule is delivery on or before the due date, with no additional tolerance.

\- Only completed deliveries with valid due and actual delivery dates are eligible for the on-time delivery rate.

\- The sample does not establish supplier explanations, material criticality, contractual penalties, or business impact.



\## 4. Example Expected Output



\### A. Executive Summary



Six fictional PO records are supplied. Three records have valid completed-delivery dates and due dates, so they are eligible for the sample on-time delivery calculation. Two eligible deliveries were on time and one was late, giving an on-time delivery rate of 66.7%.



One open PO is overdue by two calendar days. One open PO is not yet due. One delivered record lacks a due date and cannot be classified as on time or late.



\### B. Overall Delivery KPI Summary



| KPI | Result | Calculation Basis |

|---|---:|---|

| Total records | 6 | All sample rows |

| Eligible completed deliveries | 3 | Delivered records with valid due and actual dates |

| Delivered on time | 2 | PO401 and PO403 |

| Delivered late | 1 | PO402 |

| On-time delivery rate | 66.7% | 2 ÷ 3 × 100 |

| Open overdue POs | 1 | PO404 |

| Open POs not yet due | 1 | PO405 |

| Delivery status unknown for KPI | 1 | PO406 lacks a due date |



\### C. Vendor Performance Table



| Vendor | Eligible Deliveries | On-Time | Late | On-Time Rate | Open Overdue POs |

|---|---:|---:|---:|---:|---:|

| Alpha Electronics | 2 | 1 | 1 | 50.0% | 0 |

| Beta Power | 1 | 1 | 0 | 100.0% | 1 |

| SecureParts | 0 | 0 | 0 | Not available | 0 |



These small sample sizes are not sufficient to establish a long-term vendor ranking. SecureParts' delivery rate is unavailable because its delivered record lacks a due date.



\### D. Overdue PO Follow-Up



| PO | Vendor | Due Date | Days Overdue | Recommended Action |

|---|---|---|---:|---|

| PO404 | Beta Power | 2026-10-26 | 2 | Confirm current delivery status and obtain a revised commitment |



PO405 is open but not overdue as of 28 October 2026. PO406 is excluded from on-time delivery calculations because the due date is missing.



\### E. Limitations



\- The sample contains few records per vendor.

\- No supplier explanations are provided.

\- No criticality, contractual tolerance, or production impact is provided.

\- The sample does not support conclusions about long-term supplier reliability.



\## 5. Test Cases



\### Test Case 1 — On-time delivery calculation



\*\*Input:\*\* PO401 was due 20 October 2026 and delivered 20 October 2026.



\*\*Expected:\*\* Classify as on time.



\*\*Pass condition:\*\* Delivery on the due date is considered on time under the stated sample rule.



\### Test Case 2 — Late delivery calculation



\*\*Input:\*\* PO402 was due 22 October 2026 and delivered 25 October 2026.



\*\*Expected:\*\* Classify as delivered late by 3 calendar days.



\*\*Pass condition:\*\* The actual and due dates are compared correctly.



\### Test Case 3 — Missing due date



\*\*Input:\*\* PO406 is marked Delivered, with actual delivery on 27 October 2026, but the due date is missing.



\*\*Expected:\*\* Flag the missing due date and exclude the record from on-time delivery calculations.



\*\*Pass condition:\*\* The record is not incorrectly classified as on time or late.



\## 6. Completion Checklist



\- \[ ] Prompt created.

\- \[ ] Input validation rules included.

\- \[ ] Sample dataset and assumptions documented.

\- \[ ] Expected output included.

\- \[ ] All three test cases reviewed.

\- \[ ] KPI calculations verified.

\- \[ ] README created.

\- \[ ] Files committed and pushed to GitHub.



\## 7. Conclusion



This prompt supports evidence-based vendor delivery analysis by standardising KPI calculations, exposing data-quality issues, and distinguishing verified performance from unknown information. Supplier decisions should be based on validated records, a consistent delivery definition, and sufficient evidence.



