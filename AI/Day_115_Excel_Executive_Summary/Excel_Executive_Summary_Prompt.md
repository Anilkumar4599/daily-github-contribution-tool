\# Day 115 — Prompt to Convert Raw Excel Data into an Executive Summary



\## 1. Objective



Create a reusable AI prompt that converts raw Excel data into a concise, accurate, management-ready executive summary.



The prompt is intended for Procurement, QC, Inventory, Supplier Performance, and Service Operations.



\## 2. Reusable Prompt



Copy the prompt below and paste it into your AI tool. Attach your Excel file or paste the relevant table when prompted.



\---



\### ROLE



Act as a Senior Operations and Data Analysis Manager with expertise in Procurement, Quality Control, Inventory, Supplier Management, and Service Operations.



Your responsibility is to convert raw spreadsheet data into clear business insights for senior management.



\### CONTEXT



I will provide an Excel file or tabular data containing operational or business information.



The data may include:

\- Purchase orders and supplier details

\- Order values and delivery dates

\- QC defects and defect priorities

\- Inventory levels and reorder points

\- Service tickets and resolution status

\- Monthly performance indicators



\*\*Reporting period:\*\* \[Enter the period]



\*\*Report date:\*\* \[Enter the date]



\*\*Business objective:\*\* \[Explain the decision or question management needs answered]



\*\*Intended audience:\*\* Senior management



\### TASK



Perform the following steps in order.



1\. \*\*Validate the data\*\*

&#x20;  - Identify the available columns and number of records.

&#x20;  - Flag blank fields, duplicate identifiers, invalid dates, inconsistent categories, and suspicious values.

&#x20;  - Identify any missing information that limits the analysis.

&#x20;  - Do not silently remove records or assume missing values are zero.



2\. \*\*Calculate key metrics\*\*

&#x20;  - Calculate totals, counts, averages, and percentages only where the data supports them.

&#x20;  - State the calculation basis.

&#x20;  - Check for duplicate records that could inflate totals.

&#x20;  - Compare performance against targets or previous periods only if those values are supplied.



3\. \*\*Identify key findings\*\*

&#x20;  - Highlight the most important positive and negative results.

&#x20;  - Identify significant delays, risks, exceptions, recurring issues, or cost movements.

&#x20;  - Distinguish facts directly supported by the data from possible explanations.



4\. \*\*Assess business impact\*\*

&#x20;  - Explain the known or potential operational, financial, quality, or customer impact.

&#x20;  - State when the impact cannot be quantified from the available data.



5\. \*\*Recommend actions\*\*

&#x20;  - Identify the most important next actions.

&#x20;  - Suggest an owner or deadline only when provided or explicitly labelled as proposed.

&#x20;  - Identify management decisions or approvals required.



\### OUTPUT FORMAT



Produce the report using the following structure.



\*\*A. Executive Summary\*\*

\- Reporting period and dataset coverage

\- Three to five key findings, or fewer if the data supports fewer

\- Overall business position



\*\*B. KPI Snapshot\*\*



| KPI | Result | Calculation Basis | Interpretation |

|---|---|---|---|



Include only KPIs that can be calculated reliably.



\*\*C. Key Findings and Risks\*\*



| Finding | Supporting Data | Business Impact | Priority |

|---|---|---|---|



\*\*D. Data Quality Issues\*\*



| Issue | Affected Record or Field | Why It Matters | Corrective Action |

|---|---|---|---|



\*\*E. Recommended Management Actions\*\*



| Action | Reason | Proposed Owner | Target Date |

|---|---|---|---|



Clearly label proposed owners and dates when they have not been supplied.



\*\*F. Decisions Required\*\*



List the specific decisions or approvals management needs to provide. If none can be established from the data, state that.



\*\*G. Assumptions and Limitations\*\*



State missing information, calculation limitations, assumptions, and unverified explanations.



\### IMPORTANT RULES



\- Never fabricate figures, trends, supplier explanations, causes, owners, or deadlines.

\- Do not confuse correlation with causation.

\- Do not label a target as missed unless a valid target is available.

\- Do not treat open orders as delivered.

\- Do not count duplicate records as separate business transactions without checking.

\- State the reporting date and currency.

\- Keep the executive summary concise and professional.

\- Show enough calculation detail for important figures to be verified.

\- Protect confidential company, customer, supplier, and employee information.

\- If critical data is missing, explain what can be concluded and what needs validation.



\---



\## 3. Example Input — Procurement Data



The following fictional dataset demonstrates how the prompt works.



\*\*Report date:\*\* 26 October 2026.



| PO Number | Supplier | Order Value (₹) | Status | Due Date |

|---|---|---:|---|---|

| PO201 | Alpha Electronics | 50,000 | Open | 2026-10-20 |

| PO202 | Beta Power | 30,000 | Open | 2026-10-28 |

| PO203 | Alpha Electronics | 20,000 | Delivered | 2026-10-18 |

| PO204 | SecureParts | 40,000 | Open | 2026-10-24 |

| PO205 | NetworkPro | 10,000 | Delivered | 2026-10-25 |



The dataset does not include actual delivery dates, supplier explanations, contractual lead times, or criticality of the materials.



\## 4. Example Expected Output



\### A. Executive Summary



As of 26 October 2026, the sample dataset contains five purchase orders with a combined value of ₹150,000. Three orders are open, and two are marked Delivered.



Two open orders are overdue, with a combined value of ₹90,000. One open order valued at ₹30,000 is not yet due. The supplied data identifies overdue exposure but does not establish the reasons for delays or their confirmed operational impact.



\### B. KPI Snapshot



| KPI | Result | Calculation Basis | Interpretation |

|---|---:|---|---|

| Total purchase orders | 5 | Count of sample rows | Five records supplied |

| Total PO value | ₹150,000 | Sum of all order values | Total value represented by the sample |

| Open orders | 3 | Count where Status = Open | Follow-up is required |

| Delivered orders | 2 | Count where Status = Delivered | Delivery status is recorded as complete |

| Overdue open orders | 2 | Open orders with due date before 26 Oct 2026 | Two orders require follow-up |

| Overdue open PO value | ₹90,000 | ₹50,000 + ₹40,000 | Value of open orders past their due dates |



\### C. Key Findings and Risks



| Finding | Supporting Data | Business Impact | Priority |

|---|---|---|---|

| PO201 is overdue | ₹50,000; due 20 Oct | Delivery risk; actual impact unknown | High follow-up priority |

| PO204 is overdue | ₹40,000; due 24 Oct | Delivery risk; actual impact unknown | High follow-up priority |

| PO202 is not yet due | ₹30,000; due 28 Oct | Monitor upcoming commitment | Routine monitoring |



The priority labels above are proposed follow-up priorities for this example, not verified company risk classifications.



\### D. Data Quality Issues



\- Actual delivery dates are not available.

\- Supplier explanations and revised delivery commitments are not supplied.

\- Material criticality and downstream business impact are unknown.

\- No prior-period data or performance targets are available for comparison.



\### E. Recommended Management Actions



1\. Request updated delivery commitments for PO201 and PO204.

2\. Check whether either order affects QC completion, production, or customer deployments.

3\. Monitor PO202 before its due date.

4\. Update the official procurement tracker after supplier responses are verified.



\### F. Decisions Required



Confirm whether either overdue order affects a critical business requirement and whether escalation under company policy is necessary.



\### G. Assumptions and Limitations



This is a fictional dataset. Calculations use the five supplied rows, assume each row represents a distinct purchase order, and treat the stated statuses as accurate. The report does not establish why delays occurred.



\## 5. Test Cases



\### Test Case 1 — Validate totals



\*\*Input:\*\* Use all five example rows.



\*\*Expected output:\*\*

\- Total PO count = 5

\- Total PO value = ₹150,000

\- Open orders = 3

\- Delivered orders = 2



\*\*Pass condition:\*\* Every result matches the supplied data.



\### Test Case 2 — Identify overdue open orders



\*\*Input:\*\* Use report date 26 October 2026.



\*\*Expected output:\*\*

\- PO201 is overdue by 6 calendar days.

\- PO204 is overdue by 2 calendar days.

\- PO202 is not overdue.



\*\*Pass condition:\*\* Only open orders with valid due dates earlier than the report date are identified as overdue.



\### Test Case 3 — Handle missing data



\*\*Input:\*\* Remove PO204's due date.



\*\*Expected output:\*\*

\- Flag the missing due date for PO204.

\- Do not calculate its overdue days.

\- Do not include PO204 in the confirmed overdue-value total until its due date is validated.

\- State that the overdue analysis is incomplete.



\*\*Pass condition:\*\* Missing information is disclosed, and no unsupported calculation is presented as confirmed.



\## 6. Completion Checklist



\- \[ ] Reusable prompt documented.

\- \[ ] Example input included.

\- \[ ] Expected output included.

\- \[ ] Test Case 1 checked.

\- \[ ] Test Case 2 checked.

\- \[ ] Test Case 3 checked.

\- \[ ] Figures and assumptions reviewed.

\- \[ ] Files committed and pushed to GitHub.



\## 7. Conclusion



A structured prompt can help convert raw Excel data into an executive summary more consistently. The quality of the report still depends on source-data quality, valid calculations, and human review before management decisions are made.



