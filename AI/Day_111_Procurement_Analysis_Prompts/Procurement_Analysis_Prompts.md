

\# Day 111 — Procurement Analysis Prompt Library



\*\*Date:\*\* 22 October 2026  

\*\*Domain:\*\* AI  

\*\*Objective:\*\* Create 10 reusable prompts for procurement analysis.



\## 1. Business Purpose



This prompt library helps procurement professionals analyse purchase orders, supplier performance, delivery delays, spending, price changes, inventory risks, and management priorities.



The prompts are designed for use with ChatGPT or another AI assistant. Replace the sample data with verified business data when using them for real work.



\## 2. Sample Dataset



The following eight purchase orders are fictional training data.



| PO ID | Supplier | Item | Qty | Unit Price (₹) | PO Value (₹) | PO Date | Expected Date | Actual Delivery | Status |

|---|---|---|---:|---:|---:|---|---|---|---|

| PO001 | Alpha Electronics | CCTV Camera | 20 | 2500 | 50000 | 2026-10-01 | 2026-10-10 | 2026-10-09 | Delivered |

| PO002 | Beta Power | UPS | 10 | 4800 | 48000 | 2026-10-02 | 2026-10-12 | | Open |

| PO003 | Alpha Electronics | Router | 15 | 3200 | 48000 | 2026-10-03 | 2026-10-13 | 2026-10-16 | Delivered |

| PO004 | SecureParts | Sensor | 30 | 450 | 13500 | 2026-10-04 | 2026-10-14 | | Open |

| PO005 | Beta Power | Power Supply | 25 | 800 | 20000 | 2026-10-05 | 2026-10-15 | 2026-10-15 | Delivered |

| PO006 | NetworkPro | Cable | 100 | 35 | 3500 | 2026-10-06 | 2026-10-16 | | Open |

| PO007 | SecureParts | Camera | 8 | 2600 | 20800 | 2026-10-07 | 2026-10-17 | 2026-10-18 | Delivered |

| PO008 | NetworkPro | Switch | 5 | 5500 | 27500 | 2026-10-08 | 2026-10-18 | | Open |



\### Dataset assumptions



1\. The report date is 20 October 2026.

2\. PO Value equals Quantity multiplied by Unit Price.

3\. Blank Actual Delivery means the order has not yet been delivered.

4\. An open PO is overdue when its Expected Date is earlier than the report date.

5\. A delivered PO is late when its Actual Delivery date is later than its Expected Date.

6\. All amounts are in Indian rupees (₹).

7\. Taxes, freight, cancellations, partial deliveries, and payment terms are excluded.

8\. The sample is fictional and must not be treated as actual company procurement data.



\## 3. Prompt 1 — Procurement Spend Analysis



\*\*Purpose:\*\* Understand total PO value and spending distribution.



\*\*Prompt:\*\*



Act as a Senior Procurement Manager with 20 years of experience.



Analyse the purchase-order dataset provided below.



Tasks:

1\. Calculate total PO value.

2\. Calculate total value by supplier.

3\. Rank suppliers by PO value from highest to lowest.

4\. Calculate each supplier's percentage of total PO value.

5\. Identify the three highest-value purchase orders.

6\. Highlight spending concentration and potential supplier dependency.

7\. Recommend three actions for management.



Rules:

\- Verify all calculations from the supplied records.

\- Do not invent missing values.

\- Show formulas for important calculations.

\- Separate factual findings from recommendations.



Output:

\- Executive summary

\- Supplier-wise spend table

\- Highest-value PO table

\- Key risks

\- Recommended actions



\*\*Input:\*\* Use the sample dataset in Section 2.



\## 4. Prompt 2 — Overdue PO and Delivery Follow-Up



\*\*Purpose:\*\* Identify orders requiring immediate supplier follow-up.



\*\*Prompt:\*\*



Act as a Senior Procurement and Supply Chain Manager.



Using the supplied PO dataset and report date of 20 October 2026:



1\. Identify all open POs.

2\. Calculate overdue days for each open PO.

3\. Identify delivered orders that arrived late.

4\. Separate overdue open orders from completed late deliveries.

5\. Prioritize issues as Critical, High, Medium, or Low using business impact and delay.

6\. Recommend the next action and responsible team for each issue.

7\. Draft a concise supplier follow-up message for each overdue open PO.



Rules:

\- Overdue days = Report Date minus Expected Date for open POs whose due date has passed.

\- Delivery delay = Actual Delivery minus Expected Date for delivered late POs.

\- Do not flag an order as overdue if it is not yet due.

\- Do not confuse a completed late delivery with an open overdue PO.

\- Do not invent supplier commitments or reasons for delay.



Output:

PO ID | Supplier | PO Value | Status | Expected Date | Delay Days | Priority | Recommended Action



Then provide a management escalation summary.



\*\*Input:\*\* Use the sample dataset in Section 2.



\## 5. Prompt 3 — Supplier Performance Analysis



\*\*Purpose:\*\* Compare suppliers using available delivery evidence.



\*\*Prompt:\*\*



Act as a Supplier Performance Manager.



Analyse the purchase-order data supplied below.



Tasks:

1\. Calculate total POs per supplier.

2\. Count delivered and open POs.

3\. Calculate late deliveries among delivered orders.

4\. Identify suppliers with open overdue orders.

5\. Prepare a supplier-wise performance table.

6\. Recommend supplier improvement actions.



Important:

\- Distinguish between late-delivery rate among delivered orders and overdue open orders.

\- The sample is small; do not claim a supplier's long-term performance from this dataset alone.

\- Do not invent quality, cost, or service ratings that are not supplied.



Output:

Supplier | Total POs | Delivered | Open | Late Delivered | Overdue Open | Recommended Action



\## 6. Prompt 4 — Purchase Price Comparison



\*\*Purpose:\*\* Compare item prices and identify potential savings.



\*\*Prompt:\*\*



Act as a Strategic Sourcing Manager.



Review the supplied purchase-order dataset.



Tasks:

1\. Compare unit prices for the same or genuinely comparable items.

2\. Identify missing information needed for a fair comparison.

3\. Calculate price differences and percentage differences where comparable data exists.

4\. Identify potential negotiation opportunities.

5\. Recommend a price benchmarking process.



Rules:

\- Do not compare different products as if they were identical.

\- Consider specifications, quality, quantity, taxes, freight, and payment terms where available.

\- Clearly state when the data is insufficient to prove savings.

\- Never claim negotiated savings without supporting evidence.



Output:

Comparison table, data gaps, potential opportunities, and recommended actions.



\## 7. Prompt 5 — Procurement Risk Analysis



\*\*Purpose:\*\* Identify risks that may affect business continuity.



\*\*Prompt:\*\*



Act as a Procurement Risk Manager for an ATM E-Surveillance equipment supplier.



Analyse the PO dataset.



Tasks:

1\. Identify overdue open orders.

2\. Identify high-value open orders.

3\. Highlight potential supply-continuity risks.

4\. Assess the possible operational impact, stating assumptions.

5\. Classify risks by severity and urgency.

6\. Recommend mitigation and escalation actions.



Output:

Risk | Related PO | Evidence | Potential Impact | Priority | Mitigation | Owner



Do not assume that an overdue component has caused a site failure unless evidence supports that conclusion.



\## 8. Prompt 6 — Inventory and Stock-Out Risk



\*\*Purpose:\*\* Connect procurement delays to inventory availability.



\*\*Prompt:\*\*



Act as an Inventory and Materials Planning Manager.



Review the supplied PO data and identify orders that could create inventory risks.



Tasks:

1\. List overdue open orders by item.

2\. Identify which items require inventory verification.

3\. Explain which additional data is required to calculate stock-out risk.

4\. Recommend a stock-risk monitoring process.

5\. Suggest actions for critical spare parts.



Additional data required for a reliable stock-out calculation may include:

\- Current stock

\- Minimum stock level

\- Average daily consumption

\- Supplier lead time

\- Open demand and service requirements

\- Alternative suppliers



Do not declare an actual stock-out based on PO delays alone.



Output:

Item | Open PO | Expected Date | Data Missing | Potential Risk | Recommended Action



\## 9. Prompt 7 — Monthly Procurement KPI Report



\*\*Purpose:\*\* Build a repeatable management scorecard.



\*\*Prompt:\*\*



Act as a Procurement Reporting Manager.



Create a procurement KPI summary from the supplied dataset.



Calculate:

1\. Total PO count.

2\. Total PO value.

3\. Delivered PO count and value.

4\. Open PO count and value.

5\. Late-delivery count among delivered POs.

6\. Open overdue PO count.

7\. Supplier-wise PO value.



For each KPI, provide:

\- Definition

\- Calculation method

\- Result

\- Business interpretation



Do not calculate on-time delivery percentage without clearly defining the denominator and confirming the relevant population.



Output:

Executive summary, KPI table, exceptions, and management recommendations.



\## 10. Prompt 8 — Supplier Email Drafting



\*\*Purpose:\*\* Prepare professional follow-up emails.



\*\*Prompt:\*\*



Act as an experienced Procurement Executive.



Draft a professional supplier follow-up email using the supplied PO details.



Include:

\- PO number

\- Item or material

\- Expected delivery date

\- Current status

\- Business urgency, if supported by the data

\- Request for confirmed dispatch and delivery dates

\- Request for the reason for delay

\- A clear response deadline placeholder



Rules:

\- Do not invent a supplier contact name.

\- Do not invent a delivery commitment.

\- Use a professional, firm, and respectful tone.

\- Use placeholders for details not supplied.

\- Do not threaten penalties unless an applicable contractual basis is provided.



Output:

Subject line and ready-to-edit email body.



\## 11. Prompt 9 — Procurement Data Quality Audit



\*\*Purpose:\*\* Detect missing or inconsistent procurement data.



\*\*Prompt:\*\*



Act as a Procurement Data Quality Analyst.



Audit the supplied PO dataset for:

1\. Missing PO numbers, suppliers, items, quantities, prices, and dates.

2\. Duplicate PO numbers.

3\. Invalid dates.

4\. Incorrect PO value calculations.

5\. Inconsistent delivery status and actual delivery dates.

6\. Open POs with actual delivery dates.

7\. Delivered POs with missing actual delivery dates.

8\. Potentially inconsistent supplier or item names.



Output:

PO ID | Data Issue | Evidence | Business Impact | Correction Required



Do not silently correct source data. Flag suspected errors for human review.



\## 12. Prompt 10 — Management Action Plan



\*\*Purpose:\*\* Convert procurement analysis into decisions.



\*\*Prompt:\*\*



Act as a Senior Procurement Manager presenting to senior leadership.



Review the supplied procurement dataset and prepare an action-oriented management summary.



Tasks:

1\. Identify the five most important findings.

2\. Rank issues by urgency and business impact.

3\. Separate immediate actions from longer-term improvements.

4\. Recommend actions for Procurement, Stores, Service, and Management where relevant.

5\. Assign a suggested owner and target date to each action.

6\. Identify additional information required before making major decisions.



Output:

\- Executive summary

\- Top risks and exceptions

\- Prioritized action register

\- Suggested owner

\- Suggested target date

\- Required management decisions



Clearly label suggested owners and dates as proposals, not agreed commitments.



\## 13. Validation Results for the Sample Dataset



These results can be used to check the arithmetic from Prompts 1 and 2.



\### Overall PO metrics



| Metric | Expected Result |

|---|---:|

| Total POs | 8 |

| Total PO value | ₹2,31,300 |

| Delivered POs | 4 |

| Delivered PO value | ₹1,38,800 |

| Open POs | 4 |

| Open PO value | ₹92,500 |

| Late delivered POs | 2 |

| Open overdue POs | 4 |



\### Supplier-wise PO value



| Supplier | PO Count | Total PO Value |

|---|---:|---:|

| Alpha Electronics | 2 | ₹98,000 |

| Beta Power | 2 | ₹68,000 |

| SecureParts | 2 | ₹34,300 |

| NetworkPro | 2 | ₹31,000 |

| \*\*Total\*\* | \*\*8\*\* | \*\*₹2,31,300\*\* |



\### Open overdue PO validation



Report date: 20 October 2026.



| PO ID | Supplier | Expected Date | Overdue Days |

|---|---|---|---:|

| PO002 | Beta Power | 2026-10-12 | 8 |

| PO004 | SecureParts | 2026-10-14 | 6 |

| PO006 | NetworkPro | 2026-10-16 | 4 |

| PO008 | NetworkPro | 2026-10-18 | 2 |



\### Late delivered PO validation



| PO ID | Supplier | Expected Date | Actual Delivery | Days Late |

|---|---|---|---|---:|

| PO003 | Alpha Electronics | 2026-10-13 | 2026-10-16 | 3 |

| PO007 | SecureParts | 2026-10-17 | 2026-10-18 | 1 |



\## 14. How to Use These Prompts



1\. Select the prompt that matches your procurement task.

2\. Paste the prompt into your AI assistant.

3\. Add the relevant, authorized data.

4\. Review the calculations against the source records.

5\. Correct errors and clarify assumptions before using the analysis.

6\. Convert useful findings into an action tracker.

7\. Protect confidential supplier prices, contracts, personal information, and other sensitive company data according to company policy.



\## 15. Learning Outcomes



By completing this task, I will practise:

\- Structuring reusable AI prompts.

\- Procurement spend and supplier analysis.

\- Delivery delay and overdue PO tracking.

\- Inventory risk identification.

\- Data quality checks.

\- Management reporting and action planning.

\- Validating AI-generated results against known figures.



\## 16. Completion Checklist



\- \[ ] Created this Markdown file.

\- \[ ] Reviewed all 10 prompts.

\- \[ ] Tested Prompt 1 against the sample data.

\- \[ ] Tested Prompt 2 against the sample data.

\- \[ ] Verified key calculations against Section 13.

\- \[ ] Reviewed the file for clarity and formatting.

\- \[ ] Committed and pushed the file to GitHub.



\*\*Project status:\*\* Training exercise. Mark complete only after validation and GitHub push.



