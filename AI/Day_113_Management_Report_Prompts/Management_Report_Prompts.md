\# Day 113 — AI Management-Report Generation Prompts



\## 1. Objective



Build a reusable library of 10 AI prompts that help managers turn operational data into accurate, concise, decision-oriented management reports.



\## 2. Business Context



The example business supplies ATM E-Surveillance systems across India. The management team oversees Procurement, Quality Control (QC), Inventory, Supplier Performance, and Service Operations.



The prompts should help managers identify risks, explain performance, recommend actions, and communicate clearly with senior management.



\## 3. General Instructions for Every Prompt



When using any prompt:



1\. Validate the supplied data before analysis.

2\. State the reporting period and report date.

3\. Separate confirmed facts from assumptions.

4\. Calculate totals and percentages from the supplied data.

5\. Do not invent missing figures, owners, deadlines, or explanations.

6\. Identify data-quality issues and missing information.

7\. Present the key findings first.

8\. Recommend actions with a proposed owner, priority, and deadline only when supported by the input or clearly labelled as proposed.

9\. Protect confidential supplier, customer, employee, and company information.

10\. State any limitations that may affect management decisions.



\## 4. Ten Reusable Prompts



\### Prompt 1 — Executive Management Summary



Act as an experienced Senior Operations Manager.



Review the supplied operational data and prepare a concise executive management report.



Include:

\- Reporting period and data coverage

\- Five key findings, or fewer if the data supports fewer

\- Important performance metrics

\- Critical risks and exceptions

\- Decisions required from management

\- Recommended actions and next steps



Use a professional, factual tone. Lead with business impact, not raw data. Do not invent explanations for performance changes.



\### Prompt 2 — Procurement Performance Report



Act as a Senior Procurement Manager.



Analyse the supplied purchase-order data.



Report:

\- Total purchase orders

\- Total order value

\- Orders by status

\- Overdue open purchase orders

\- Supplier-wise order value

\- Delayed deliveries and potential supply risks

\- Missing purchase-order or delivery information

\- Recommended follow-up actions



Show currency and reporting dates clearly. Distinguish overdue open orders from orders that were delivered late but are now complete.



\### Prompt 3 — Supplier Performance and Risk Report



Analyse supplier performance using the available order, delivery, quality, and response data.



Include:

\- Orders and spend by supplier

\- On-time delivery performance, if the necessary fields exist

\- Quality issues and recurring failures

\- Outstanding commitments

\- Supplier concentration risks

\- Suppliers requiring escalation

\- Recommended corrective actions



Do not label a supplier poor-performing based only on one delayed order. State the available evidence and any missing performance data.



\### Prompt 4 — QC and Defect Management Report



Act as a Senior QC Manager for ATM E-Surveillance products.



Analyse the defect tracker and report:

\- Total valid defects

\- Defects by priority and status

\- HW, SW, EDGE, and joint-ownership issues

\- Show-stopper defects affecting critical functions

\- Recurring failure categories

\- Missing evidence or investigation details

\- Engineering actions and management decisions required



Prioritise verified critical-function failures. Do not claim a root cause without supporting evidence.



\### Prompt 5 — Inventory and Stock-Out Risk Report



Analyse the supplied inventory data.



Include:

\- Current stock by item

\- Items below minimum stock level

\- Items at or below reorder point

\- Potential stock-out risks

\- Supplier lead-time concerns

\- Suggested replenishment priorities

\- Data required to improve inventory planning



If consumption, lead time, open purchase orders, or safety-stock information is missing, explain how that limits the risk assessment. Do not invent demand forecasts.



\### Prompt 6 — Service Performance and Escalation Report



Analyse service tickets and escalation data.



Report:

\- Tickets received, open, in progress, and closed

\- Critical and high-priority open tickets

\- Overdue tickets against the supplied SLA

\- Ticket ageing

\- Repeat issues

\- Regional or team-level workload, where data is available

\- Recommended escalation and recovery actions



Use only the SLA definitions and ticket data supplied. Do not assume an SLA target if none is provided.



\### Prompt 7 — Monthly KPI and Trend Report



Prepare a monthly performance report using the supplied KPI data.



Include:

\- Actual versus target

\- Month-on-month change, when comparable prior-period data exists

\- KPI trend and major exceptions

\- Positive and negative performance movements

\- Likely explanations supported by evidence

\- Improvement actions



Show the calculation method for percentages. If the target or previous-month data is missing, mark the comparison unavailable.



\### Prompt 8 — Cost, Spend, and Budget Variance Report



Act as a Procurement and Finance reporting analyst.



Analyse actual spend, budget, taxes, freight, and other supplied cost components.



Include:

\- Total actual spend

\- Budget versus actual

\- Absolute variance and percentage variance, where valid

\- Supplier and category cost breakdown

\- Significant cost increases or savings

\- Potential cost-control opportunities

\- Questions requiring Finance or Procurement confirmation



Use consistent currency and tax treatment. Do not describe a variance as a saving unless the comparison supports that conclusion.



\### Prompt 9 — Weekly Action Tracker and Management Follow-Up



Convert the supplied meeting notes or action tracker into a structured weekly management follow-up report.



Include:

\- Action ID and description

\- Current status

\- Responsible owner

\- Original due date

\- Overdue days, if calculable

\- Blocker or dependency

\- Next action

\- Decisions required



Keep confirmed commitments separate from proposed actions. Flag missing owners, dates, and unclear statuses rather than filling them with invented details.



\### Prompt 10 — Board-Ready Management Report



Transform validated operational data into a concise, senior-leadership report.



Structure:

1\. Executive summary

2\. Performance scorecard

3\. Major achievements

4\. Critical business risks

5\. Financial and operational impact

6\. Root causes, only when verified

7\. Corrective and preventive actions

8\. Decisions and support required

9\. Next reporting period's priorities

10\. Data limitations



Use clear headings, concise tables, and decision-focused language. Include only metrics that can be supported by the source data. Label unverified explanations and proposed actions appropriately.



\## 5. Sample Test Dataset



Use this fictional procurement dataset to test the prompts.



| PO | Supplier | Order Value (₹) | Status | Due Date | Delivery Date |

|---|---|---:|---|---|---|

| PO001 | Alpha Electronics | 50,000 | Delivered | 2026-10-10 | 2026-10-10 |

| PO002 | Beta Power | 30,000 | Open | 2026-10-20 | Not delivered |

| PO003 | Alpha Electronics | 20,000 | Delivered | 2026-10-18 | 2026-10-21 |

| PO004 | SecureParts | 40,000 | Open | 2026-10-22 | Not delivered |



\*\*Assumed report date:\*\* 2026-10-24.



\### Sample calculations



\- Total purchase orders: 4

\- Total order value: ₹140,000

\- Delivered orders: 2

\- Open orders: 2

\- Open orders past their due date: 2

\- Delivered late: 1

\- Alpha Electronics order value: ₹70,000



These calculations use the sample rows only. They do not represent actual company performance.



\## 6. Required Test Cases



\### Test Case 1 — Correct totals and status counts



\*\*Input:\*\* Use all four rows in the sample dataset.



\*\*Expected result:\*\*

\- Total orders = 4

\- Total order value = ₹140,000

\- Delivered = 2

\- Open = 2



\*\*Pass criteria:\*\* All four values match. The report must not count open orders as delivered.



\### Test Case 2 — Overdue order identification



\*\*Input:\*\* Use the sample dataset with report date 2026-10-24.



\*\*Expected result:\*\*

\- PO002 is overdue by 4 calendar days.

\- PO004 is overdue by 2 calendar days.

\- PO003 was delivered 3 calendar days after its due date.

\- PO001 was delivered on time.



\*\*Pass criteria:\*\* Open overdue orders are listed separately from late deliveries that are already complete.



\### Test Case 3 — Missing-data validation



\*\*Input:\*\* Remove the due date from PO004 and remove the supplier name from PO002.



\*\*Expected result:\*\*

\- Flag the missing due date for PO004.

\- Flag the missing supplier name for PO002.

\- Do not calculate PO004's overdue days without a valid due date.

\- Do not silently assign PO002 to an invented supplier.

\- Report the affected records and the actions needed to correct them.



\*\*Pass criteria:\*\* Missing data is explicitly reported and no missing values are fabricated.



\## 7. Review Checklist



\- \[ ] All 10 prompts are present.

\- \[ ] Each prompt defines clear report sections.

\- \[ ] The sample dataset is labelled fictional.

\- \[ ] Test Case 1 passes.

\- \[ ] Test Case 2 passes.

\- \[ ] Test Case 3 passes.

\- \[ ] All calculations have a clear basis.

\- \[ ] Missing data and assumptions are identified.

\- \[ ] Reports avoid unsupported conclusions.



\## 8. Conclusion



This prompt library provides a consistent starting point for AI-assisted management reporting across Procurement, QC, Inventory, Service, and operational performance.



AI-generated reports must be reviewed against source records before they are shared with management or used for business decisions.



