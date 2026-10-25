\# Day 114 — Reusable RCTO Prompt Template



\## 1. Objective



Create a reusable AI prompt framework using RCTO:



\- \*\*R — Role:\*\* Who should the AI act as?

\- \*\*C — Context:\*\* What business situation and background should it understand?

\- \*\*T — Task:\*\* What specific work must it perform?

\- \*\*O — Output:\*\* What format and level of detail should it produce?



The template is designed for Procurement, QC, Inventory, Service Operations, and Management Reporting.



\## 2. Reusable RCTO Template



Copy the template below and replace the instructions in square brackets with your own details.



\### R — ROLE



Act as a \[job title or subject-matter expert] with \[relevant experience or expertise].



Your responsibilities include \[key responsibilities relevant to the task].



Use clear, professional, beginner-friendly language where appropriate.



\### C — CONTEXT



\*\*Business or department:\*\* \[department or business area]



\*\*Industry or product:\*\* \[industry, product, or service]



\*\*Current situation:\*\* \[explain the problem or business requirement]



\*\*Available data:\*\* \[describe the files, columns, records, or evidence supplied]



\*\*Constraints:\*\* \[budget, timeline, company policy, data limitations, or other restrictions]



\*\*Reporting date or period:\*\* \[date or period, if relevant]



Do not assume facts that are not supplied. Clearly identify missing information and distinguish facts from assumptions.



\### T — TASK



Complete the following steps:



1\. Validate the supplied information for missing, invalid, duplicate, or inconsistent records.

2\. Identify the key findings relevant to the business requirement.

3\. Perform calculations only when the required data is available and valid.

4\. Classify risks, priorities, or issues using the stated criteria.

5\. Explain the operational or business impact.

6\. Recommend practical next actions.

7\. Identify additional information needed to reach a reliable conclusion.

8\. Highlight any decisions that require human or management approval.



\### O — OUTPUT



Present the result using the following structure:



1\. \*\*Executive Summary:\*\* The most important findings.

2\. \*\*Data Validation:\*\* Missing fields, inconsistencies, and limitations.

3\. \*\*Analysis:\*\* Findings, calculations, and supporting evidence.

4\. \*\*Risk and Priority Assessment:\*\* Issues ranked using the supplied criteria.

5\. \*\*Recommended Actions:\*\* Action, proposed owner, priority, and due date where supported.

6\. \*\*Management Decisions:\*\* Decisions or approvals required.

7\. \*\*Assumptions and Limitations:\*\* Information that is unknown or unverified.



Use tables where they improve readability. State the reporting date and units. Do not invent numbers, evidence, owners, deadlines, or root causes.



\## 3. Example Input — Procurement Overdue PO Analysis



\### R — Role



Act as a Senior Procurement Manager experienced in supplier follow-up, purchase-order management, and delivery risk.



\### C — Context



A company supplies ATM E-Surveillance systems across India. The Procurement team needs to identify open purchase orders that are past their delivery due dates.



Reporting date: 25 October 2026.



Sample data:



| PO Number | Supplier | PO Value (₹) | Status | Due Date |

|---|---|---:|---|---|

| PO101 | Alpha Electronics | 50,000 | Open | 2026-10-20 |

| PO102 | Beta Power | 30,000 | Open | 2026-10-28 |

| PO103 | SecureParts | 40,000 | Delivered | 2026-10-22 |

| PO104 | NetworkPro | 25,000 | Open | 2026-10-23 |



Assume the dates are valid and the reporting date is 25 October 2026. No actual delivery dates, supplier commitments, or business-impact details are supplied for the open orders.



\### T — Task



1\. Identify open purchase orders past their due dates.

2\. Calculate overdue days using calendar days.

3\. Calculate the total value of overdue open purchase orders.

4\. Separate overdue orders from orders that are not yet due.

5\. Recommend follow-up actions.

6\. Identify information needed before escalating suppliers.

7\. Do not invent reasons for delays or supplier commitments.



\### O — Output



Provide:

\- An executive summary

\- A table of overdue open purchase orders

\- Total overdue PO value

\- Orders not yet due

\- Recommended follow-up actions

\- Missing information and limitations



\## 4. Example Expected Output



\### Executive Summary



As of 25 October 2026, \*\*two open purchase orders are overdue\*\*, with a combined order value of ₹75,000. One additional open order is not yet due. One order is marked Delivered and is excluded from the open overdue list.



\### Overdue Open Purchase Orders



| PO Number | Supplier | PO Value (₹) | Due Date | Overdue Days |

|---|---|---:|---|---:|

| PO101 | Alpha Electronics | 50,000 | 2026-10-20 | 5 |

| PO104 | NetworkPro | 25,000 | 2026-10-23 | 2 |

| \*\*Total\*\* | | \*\*75,000\*\* | | |



\### Orders Not Yet Due



| PO Number | Supplier | PO Value (₹) | Due Date | Status |

|---|---|---:|---|---|

| PO102 | Beta Power | 30,000 | 2026-10-28 | Open |



\### Recommended Actions



1\. Contact Alpha Electronics and NetworkPro to confirm current delivery status and obtain revised delivery commitments.

2\. Check whether the overdue items affect production, QC completion, or customer deployments.

3\. Record supplier responses and the next committed delivery date in the official PO tracker.

4\. Escalate according to company policy if the delays affect critical business requirements.



These are proposed follow-up actions, not evidence that the suppliers have been contacted.



\### Data Limitations



\- Actual delivery status and supplier explanations are not supplied for the open overdue orders.

\- Criticality of the materials is unknown.

\- No contractual lead times, escalation thresholds, or customer-impact information is supplied.

\- The analysis uses calendar days, not working days.



\## 5. Test Cases



\### Test Case 1 — Correct overdue calculation



\*\*Input:\*\* PO101 is Open, due 20 October 2026. Reporting date is 25 October 2026.



\*\*Expected:\*\* Overdue by 5 calendar days.



\*\*Pass condition:\*\* The result is 5 days, not 4 or 6.



\### Test Case 2 — Exclude a delivered order



\*\*Input:\*\* PO103 has status Delivered and due date 22 October 2026.



\*\*Expected:\*\* PO103 does not appear in the open overdue list.



\*\*Pass condition:\*\* Delivered orders are reported separately from open overdue orders.



\### Test Case 3 — Identify missing data



\*\*Input:\*\* Remove the due date for PO104.



\*\*Expected:\*\* Flag PO104's missing due date and state that overdue days cannot be calculated reliably for this record.



\*\*Pass condition:\*\* No overdue-day value is fabricated for PO104 when its due date is missing.



\## 6. Reuse Guide



To adapt this template for another business task:



1\. Replace the Role with the appropriate professional role.

2\. Describe the real business situation in Context.

3\. List the required work in Task.

4\. Define the expected report structure in Output.

5\. Supply validated data or evidence.

6\. Check the results against known facts and expected calculations.

7\. Record assumptions and unresolved questions.



\## 7. Success Criteria



\- The RCTO structure is clearly explained.

\- The template can be reused across different business tasks.

\- The example contains sample input and expected output.

\- All three test cases have explicit expected results.

\- Calculations and business recommendations are traceable to supplied information.

\- Missing data is reported instead of invented.



\## 8. Conclusion



A structured RCTO prompt makes AI instructions clearer, more consistent, and easier to validate. The framework improves the quality of analysis but does not replace source-data checks, professional judgement, or required management approvals.



