\# Day 120 — Five Practical Ways AI Can Reduce Manual Excel Work



\## 1. Objective



Document five practical ways Artificial Intelligence (AI) can reduce repetitive Excel work in Procurement, Quality Control (QC), Inventory, Vendor Management, and Management Reporting.



The goal is to understand how AI can help analyse, organise, validate, and summarise Excel data while keeping business decisions under human control.



\## 2. Five Practical AI Use Cases



\### Use Case 1 — Excel Data Cleaning and Validation



\*\*Current manual work:\*\*



\- Checking blank cells.

\- Finding duplicate PO numbers.

\- Correcting inconsistent supplier names.

\- Identifying invalid dates.

\- Checking missing quantities and amounts.



\*\*How AI helps:\*\*



AI can review a sample or uploaded Excel dataset, identify data-quality problems, suggest corrections, and generate a validation checklist.



\*\*Simple implementation logic:\*\*



1\. Prepare the Excel data with clear column headings.

2\. Provide the data to an approved AI tool.

3\. Ask AI to identify missing values, duplicates, inconsistent formats, and invalid entries.

4\. Review the suggested corrections.

5\. Correct the original Excel file only after verification.



\*\*Example AI prompt:\*\*



"Act as a Procurement Data Analyst. Review the supplied PO data and identify duplicate PO numbers, missing supplier names, invalid dates, blank quantities, and inconsistent PO statuses. Do not modify or invent any values. Provide a data validation report with the affected row and recommended action."



\*\*Expected benefit:\*\*



Less time spent manually checking records and improved data accuracy.



\*\*Important control:\*\* A repeated PO number may represent multiple legitimate line items. Verify before removing duplicates.



\---



\### Use Case 2 — Purchase Order Follow-Up and Overdue Analysis



\*\*Current manual work:\*\*



\- Checking open purchase orders.

\- Comparing PO due dates with the reporting date.

\- Identifying overdue orders.

\- Preparing supplier follow-up lists.

\- Writing repetitive follow-up emails.



\*\*How AI helps:\*\*



AI can analyse supplied PO information, identify overdue orders, prioritise follow-ups, and prepare supplier email drafts.



\*\*Simple implementation logic:\*\*



1\. Maintain an Excel PO tracker.

2\. Include PO number, supplier, PO date, due date, status, and delivery confirmation.

3\. Calculate overdue days in Excel.

4\. Provide the relevant records to AI.

5\. Ask AI to prepare a follow-up summary and draft emails.

6\. Verify the information before sending any email.



\*\*Example Excel formula:\*\*



Assume:

\- Due Date is in column E.

\- PO Status is in column F.

\- Reporting date is in cell B1.



Formula for overdue days:



`=IF(AND(F2="Open",E2<>"",E2<$B$1),$B$1-E2,0)`



\*\*Example AI prompt:\*\*



"Review the supplied open PO records. Identify overdue POs using the reporting date provided. Prepare a supplier-wise follow-up list showing PO number, due date, overdue days, and recommended next action. Draft professional supplier follow-up emails. Do not invent revised delivery dates or supplier explanations."



\*\*Expected benefit:\*\*



Faster PO review, consistent follow-ups, and better visibility of delayed orders.



\*\*Important control:\*\* AI must not invent supplier commitments or send emails without human approval.



\---



\### Use Case 3 — Vendor Performance Analysis



\*\*Current manual work:\*\*



\- Calculating supplier delivery performance.

\- Comparing promised and actual delivery dates.

\- Reviewing delayed deliveries.

\- Preparing vendor performance summaries.

\- Identifying suppliers requiring improvement.



\*\*How AI helps:\*\*



AI can interpret a validated supplier performance dataset, summarise delivery trends, highlight exceptions, and recommend areas for improvement.



\*\*Simple implementation logic:\*\*



1\. Maintain supplier-wise delivery records.

2\. Include supplier name, PO number, committed date, actual delivery date, and delivery status.

3\. Calculate on-time and delayed deliveries using Excel.

4\. Provide the validated summary to AI.

5\. Ask AI to prepare a vendor performance report.

6\. Verify the calculations before management review.



\*\*Example Excel calculation:\*\*



Assume:

\- Committed Date is in column C.

\- Actual Delivery Date is in column D.



On-time delivery indicator:



`=IF(OR(C2="",D2=""),"Not Available",IF(D2<=C2,"On Time","Delayed"))`



\*\*Example AI prompt:\*\*



"Analyse the supplied vendor delivery performance summary. Identify suppliers with the highest number of delayed deliveries, summarise the available on-time delivery percentages, and recommend practical supplier improvement actions. State the number of records analysed and identify missing information. Do not assume a supplier is poor-performing without sufficient data."



\*\*Expected benefit:\*\*



Faster supplier comparisons and clearer identification of delivery improvement requirements.



\*\*Important control:\*\* Use a consistent reporting period and a clearly defined on-time delivery calculation.



\---



\### Use Case 4 — QC Defect Classification and Analysis



\*\*Current manual work:\*\*



\- Reviewing defect descriptions.

\- Classifying hardware and software defects.

\- Assigning defect severity.

\- Identifying repeated defects.

\- Preparing QC summaries and Pareto reports.



\*\*How AI helps:\*\*



AI can review defect descriptions, suggest categories, identify similar symptoms, and prepare structured defect summaries for QC review.



\*\*Simple implementation logic:\*\*



1\. Maintain a QC defect tracker in Excel.

2\. Include defect ID, product, module, defect description, date, and status.

3\. Provide the defect records to AI.

4\. Ask AI to suggest HW/SW/EDGE classification and severity.

5\. Review classifications with the QC team.

6\. Prepare a validated defect summary.



\*\*Example AI prompt:\*\*



"Act as a Senior Hardware and Software QC Analyst. Analyse the supplied defect records. Suggest HW, SW, EDGE, Combination, or Unknown ownership. Classify severity as Critical, High, Medium, or Low only when the supplied evidence supports it. Identify similar defect descriptions and possible recurring patterns. Do not claim a common root cause without supporting evidence."



\*\*Expected benefit:\*\*



Reduced repetitive defect review and faster preparation of QC reports.



\*\*Important control:\*\* AI suggestions are not confirmed root-cause findings. QC engineers must validate defect ownership, severity, and recurrence.



\---



\### Use Case 5 — Automated Management Summary from Excel Data



\*\*Current manual work:\*\*



\- Collecting information from multiple Excel sheets.

\- Preparing daily or weekly summaries.

\- Writing management highlights.

\- Identifying delayed activities and pending actions.

\- Formatting reports for management review.



\*\*How AI helps:\*\*



AI can convert validated Excel summaries into concise management reports with key figures, exceptions, risks, and recommended actions.



\*\*Simple implementation logic:\*\*



1\. Prepare a clean Excel summary.

2\. Validate total counts, amounts, and percentages.

3\. Provide the summary data to AI.

4\. Ask AI to prepare an executive summary.

5\. Review every figure and business conclusion.

6\. Copy the approved summary into the management report.



\*\*Example AI prompt:\*\*



"Act as a Senior Operations Reporting Analyst. Convert the supplied procurement, QC, and inventory summary into a professional management report. Include key performance figures, major exceptions, pending actions, and recommended next steps. Separate confirmed facts from observations and recommendations. Do not change figures or invent missing information."



\*\*Expected benefit:\*\*



Less time spent writing repetitive reports and more time available for analysis and decision-making.



\*\*Important control:\*\* Validate all totals, percentages, and business conclusions against the original Excel workbook.



\---



\## 3. Comparison of the Five Use Cases



| No. | Use Case | Manual Work Reduced | Business Area |

|---|---|---|---|

| 1 | Excel Data Cleaning and Validation | Manual checking and correction | Procurement |

| 2 | PO Follow-Up and Overdue Analysis | Repeated PO checking and email drafting | Procurement |

| 3 | Vendor Performance Analysis | Supplier comparisons and report preparation | Procurement |

| 4 | QC Defect Classification and Analysis | Repeated defect review and categorisation | QC |

| 5 | Management Summary Generation | Manual report writing and formatting | Management |



\## 4. Practical Implementation Approach



AI does not automatically eliminate the need for Excel formulas or a clean data structure.



A practical workflow is:



1\. \*\*Excel:\*\* Store and organise business data.

2\. \*\*Excel formulas:\*\* Calculate reliable counts, dates, quantities, and percentages.

3\. \*\*AI:\*\* Interpret the supplied information and generate summaries or recommendations.

4\. \*\*Human review:\*\* Validate the results and approve business decisions.

5\. \*\*Final report:\*\* Save the approved analysis in Excel, Word, or PDF.



\## 5. Suggested Learning Tools



| Tool | Practical Use |

|---|---|

| Microsoft Excel | Data storage, formulas, filters, and validation |

| ChatGPT | Data analysis assistance, prompt-based summaries, and draft reports |

| Microsoft Copilot for Excel | AI assistance within supported Microsoft Excel environments |

| Power Query | Repeatable data cleaning and transformation |

| Power BI | Dashboards and management reporting |



\*\*Note:\*\* Features and availability depend on the product version, subscription, organisational configuration, and data-access permissions. AI should only receive business data through approved company tools and policies.



\## 6. Validation Checklist



\- \[ ] All five use cases documented.

\- \[ ] Manual work explained for each use case.

\- \[ ] AI benefits explained.

\- \[ ] Simple implementation logic included.

\- \[ ] Practical example prompts included.

\- \[ ] Excel formula examples included.

\- \[ ] Human validation requirements documented.

\- \[ ] No unsupported claims about guaranteed time or cost savings.

\- \[ ] Documentation reviewed.



\## 7. Conclusion



AI can reduce repetitive Excel work by helping with data validation, purchase-order follow-ups, vendor performance analysis, QC defect classification, and management reporting.



The most effective approach is not to replace Excel completely. Instead, use Excel for structured data and calculations, AI for analysis and communication, and human review for accuracy and business decisions.



This approach can help procurement and QC teams improve productivity, reporting quality, and operational visibility.

