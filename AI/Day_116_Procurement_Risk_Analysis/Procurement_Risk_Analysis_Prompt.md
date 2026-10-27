\# Day 116 — Procurement Risk Analysis Without Inventing Missing Information



\## 1. Objective



Create a reusable AI prompt that identifies procurement risks from purchase-order and supplier data without fabricating missing facts, causes, financial impact, or delivery commitments.



The prompt is designed for procurement teams supporting hardware, electronics, ATM E-Surveillance equipment, inventory, QC, and service operations.



\## 2. Reusable AI Prompt



\### ROLE



Act as a Senior Procurement and Supply Chain Risk Analyst experienced in purchase-order management, supplier follow-up, inventory coordination, delivery tracking, and operational risk assessment.



Your job is to identify evidence-supported procurement risks and recommend practical next actions.



\### CONTEXT



I will provide a purchase-order dataset that may contain:



\- PO number

\- Supplier name

\- PO value and currency

\- Order date

\- Required delivery date

\- Actual delivery date

\- PO status

\- Item or material description

\- Quantity ordered and quantity received

\- Stock on hand

\- Supplier lead time

\- QC status

\- Business criticality

\- Supplier commitment

\- Remarks or evidence



\*\*Reporting date:\*\* \[Enter date]



\*\*Reporting period:\*\* \[Enter period]



\*\*Business objective:\*\* \[Describe the procurement question or decision]



Not every field will necessarily be available.



\### TASK



\#### Step 1 — Validate the input data



Check for:

\- Missing PO numbers or supplier names

\- Duplicate PO numbers or repeated line items

\- Invalid or missing dates

\- Inconsistent PO statuses

\- Missing PO values or quantities

\- Missing required delivery dates

\- Conflicting delivery status and actual delivery dates

\- Missing stock, lead-time, or material-criticality data



Do not silently remove duplicate-looking records. Identify them for review because a PO may legitimately contain multiple line items.



\#### Step 2 — Identify evidence-supported risks



Review the available data for:



\- Open orders past their required delivery dates

\- Upcoming delivery commitments

\- Supplier delivery delays supported by dates

\- Potential material shortages where stock and demand information exist

\- Concentration of orders with a single supplier

\- Unusual order-value or quantity entries

\- QC holds or rejected deliveries where recorded

\- Unconfirmed delivery commitments

\- Data-quality gaps that prevent reliable risk assessment



Do not assume that every overdue order is business-critical.



\#### Step 3 — Classify findings



Use these categories:



\- \*\*Confirmed risk or exception:\*\* Directly supported by valid supplied data.

\- \*\*Potential risk:\*\* Plausible concern requiring additional information or verification.

\- \*\*Unknown / insufficient data:\*\* The available data cannot support a reliable conclusion.

\- \*\*No issue identified in supplied data:\*\* The available fields do not show the specified issue. This does not prove that no risk exists.



Use Critical, High, Medium, and Low only when a documented risk-rating method and sufficient evidence are available. Otherwise use a provisional priority and explain the basis.



\#### Step 4 — Assess impact carefully



For every finding, explain:

\- What the data confirms

\- What could happen

\- What information is missing

\- What evidence is required to establish business impact



Do not claim production stoppage, stock-out, customer impact, financial loss, or supplier negligence unless supported by supplied evidence.



\#### Step 5 — Recommend actions



Recommend practical actions such as:

\- Confirming the latest delivery commitment

\- Checking physical stock and open demand

\- Verifying QC or receiving status

\- Obtaining a supplier recovery plan

\- Checking alternative supply options

\- Escalating according to company policy

\- Correcting incomplete records



Distinguish proposed actions from actions already completed. Do not invent an owner or deadline. If useful, suggest a role as a proposed owner and label it clearly.



\### REQUIRED OUTPUT



\#### A. Executive Summary



Summarise the most important confirmed findings, potential risks, and key information gaps.



\#### B. Data Validation Table



| Record / PO | Field or Issue | Validation Finding | Action Required |

|---|---|---|---|



\#### C. Procurement Risk Register



| PO / Item | Confirmed Facts | Risk Classification | Potential Impact | Missing Information | Recommended Action |

|---|---|---|---|---|---|



\#### D. Priority Follow-Up List



List the records requiring immediate verification or action. Explain why each one is prioritised.



\#### E. Supplier Risk Summary



Summarise supplier-specific issues only where the data supports the comparison. State the number of records used and the limitations of the sample.



\#### F. Management Decisions Required



Identify the decisions that management may need to make. If the data does not support a specific decision, state what must be verified first.



\#### G. Assumptions and Limitations



List all assumptions, missing fields, data limitations, and conclusions that cannot yet be confirmed.



\### MANDATORY SAFEGUARDS



1\. Never invent supplier explanations, delivery dates, stock quantities, demand forecasts, or financial losses.

2\. Never assume a missing value is zero.

3\. Never infer supplier negligence from a delay alone.

4\. Never claim a stock-out without sufficient stock and demand evidence.

5\. Never classify an order as delivered unless the supplied status or receiving evidence supports it.

6\. Never calculate overdue days without a valid due date and reporting date.

7\. Never calculate supplier on-time delivery performance without suitable delivery records and a defined calculation method.

8\. Separate confirmed facts from possible consequences.

9\. If data conflicts, report the conflict instead of choosing a value without explanation.

10\. Use the currency and date conventions supplied.

11\. Treat the sample data as confidential if it contains sensitive business information.

12\. State clearly when further investigation is required.



\## 3. Sample Input Dataset



The following fictional dataset demonstrates the prompt.



\*\*Reporting date:\*\* 27 October 2026.



| PO | Supplier | PO Value (₹) | Status | Due Date | Stock on Hand | Demand / Required Qty |

|---|---|---:|---|---|---:|---:|

| PO301 | Alpha Electronics | 50,000 | Open | 2026-10-22 | 20 | 35 |

| PO302 | Beta Power | 30,000 | Open | 2026-10-30 | 15 | 10 |

| PO303 | SecureParts | 40,000 | Delivered | 2026-10-25 | Not supplied | Not supplied |

| PO304 | Alpha Electronics | 25,000 | Open | Missing | Not supplied | Not supplied |



\### Sample Assumptions



\- All four rows are assumed to represent distinct POs for this exercise.

\- The PO values and supplied statuses are assumed accurate.

\- Dates are interpreted as calendar dates in YYYY-MM-DD format.

\- The reporting date is 27 October 2026.

\- Stock and required quantity are assumed to use the same unit for PO301 and PO302.

\- The meaning of “Demand / Required Qty” and its time horizon are not defined; therefore, the quantities are insufficient to prove a stock-out.

\- No supplier explanations, lead times, material criticality, contractual terms, or production-impact records are supplied.

\- The dataset is fictional and does not represent actual company records.



\## 4. Example Expected Output



\### A. Executive Summary



The sample contains four purchase orders with a combined value of ₹145,000. Two open orders are past their recorded due dates: PO301 and PO304. PO302 remains open but is not yet due. PO304 has no due date, so its overdue status cannot be established from the supplied data.



PO301 has a recorded stock quantity of 20 and a required quantity of 35. If these values refer to comparable units and the same requirement period, the recorded quantity gap is 15 units. This indicates a potential shortage requiring validation, but it does not by itself prove an actual stock-out or production impact.



\### B. Data Validation Table



| PO | Issue | Finding | Action Required |

|---|---|---|---|

| PO301 | Demand definition | Stock is 20 and required quantity is 35; time horizon is unspecified | Confirm unit, demand period, and open replenishment |

| PO304 | Missing due date | Overdue status cannot be calculated | Confirm the required delivery date |

| All records | Business criticality | Not supplied | Confirm whether materials affect critical operations |



\### C. Procurement Risk Register



| PO | Confirmed Facts | Classification | Potential Impact | Recommended Action |

|---|---|---|---|---|

| PO301 | Open; due 22 Oct; report date 27 Oct; stock 20; required quantity 35 | Confirmed overdue exception; potential supply risk | Delivery delay is confirmed by the recorded dates; actual operational impact is unknown | Obtain supplier commitment and validate stock, demand, and replenishment |

| PO302 | Open; due 30 Oct; report date 27 Oct | Upcoming commitment | Potential future delay if delivery is not completed on time | Monitor the due date and confirm delivery readiness |

| PO303 | Status recorded as Delivered; due 25 Oct | No open-order issue identified in the supplied status | Actual delivery timing cannot be independently verified without receipt date | Verify receipt and QC acceptance if required |

| PO304 | Open; due date missing | Unknown overdue status; data-quality issue confirmed | Delay exposure cannot be quantified | Obtain the required delivery date and supplier commitment |



\### D. Management Decisions Required



No confirmed production stoppage or financial loss can be established from this dataset. Management should first confirm whether PO301 supports a critical requirement and whether alternative stock or supply is available.



\### E. Limitations



\- No actual delivery date is supplied for the open orders.

\- PO304 has no due date.

\- The stock and demand period are not defined.

\- No supplier lead times or contractual escalation rules are supplied.

\- Supplier performance cannot be reliably ranked using this small dataset.



\## 5. Test Cases



\### Test Case 1 — Overdue PO identification



\*\*Input:\*\* PO301 is Open, due 22 October 2026. Report date is 27 October 2026.



\*\*Expected:\*\* Identify PO301 as overdue by 5 calendar days.



\*\*Pass condition:\*\* The calculation is correct and the report does not invent a reason for the delay.



\### Test Case 2 — Missing due date



\*\*Input:\*\* PO304 is Open and its due date is blank.



\*\*Expected:\*\* Report the missing due date. Do not calculate overdue days or label the PO as confirmed overdue.



\*\*Pass condition:\*\* The report explicitly identifies the unknown status.



\### Test Case 3 — Potential stock shortage



\*\*Input:\*\* PO301 has stock on hand of 20 and required quantity of 35, with the demand period unspecified.



\*\*Expected:\*\* Identify a potential quantity gap of 15 units, conditional on the units being comparable. State that a stock-out is not confirmed and request validation of the demand period and available replenishment.



\*\*Pass condition:\*\* The report does not claim an actual stock-out or production stoppage.



\## 6. Completion Checklist



\- \[ ] Reusable prompt created.

\- \[ ] Sample dataset included.

\- \[ ] Assumptions documented.

\- \[ ] Expected output included.

\- \[ ] Test Case 1 checked.

\- \[ ] Test Case 2 checked.

\- \[ ] Test Case 3 checked.

\- \[ ] Facts, risks, and unknowns clearly separated.

\- \[ ] Files committed and pushed to GitHub.



\## 7. Conclusion



A reliable procurement risk report must distinguish what the data proves from what needs investigation. This prompt provides a structured way to identify exceptions, document uncertainty, and recommend proportionate actions without fabricating missing information.



