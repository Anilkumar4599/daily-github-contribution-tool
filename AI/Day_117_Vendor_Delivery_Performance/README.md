\# Day 117 — Vendor Delivery Performance Analysis



\## Project Overview



A reusable AI prompt for measuring vendor delivery performance, identifying overdue POs, validating delivery data, and preparing supplier follow-up reports.



\## Objectives



\- Calculate on-time delivery rates using valid records.

\- Identify late deliveries and open overdue POs.

\- Detect missing and inconsistent dates.

\- Compare vendors fairly using sample size and consistent definitions.

\- Recommend evidence-based follow-up actions.



\## Project Files



\- `Vendor\_Delivery\_Performance\_Prompt.md` — Reusable prompt, validation rules, sample dataset, expected output, and test cases.

\- `README.md` — Project overview and usage instructions.



\## How to Use



1\. Supply PO records and the reporting date.

2\. Define the company's on-time delivery rule.

3\. Validate PO statuses and delivery dates.

4\. Review KPI calculations and excluded records.

5\. Verify findings against receiving records and supplier commitments.

6\. Follow up on overdue deliveries using the approved procurement process.



\## Validation Rules



\- Do not treat open orders as completed deliveries.

\- Exclude missing or invalid dates from KPIs that require them.

\- Report the KPI denominator and sample size.

\- Do not invent supplier explanations or performance targets.

\- Distinguish confirmed late deliveries from potential delivery risks.



\## Test Cases



1\. Delivery on the due date is classified as on time.

2\. Delivery after the due date is classified as late.

3\. Missing due dates are flagged and excluded from on-time calculations.



\## Limitations



The sample dataset is fictional. Vendor comparisons require consistent delivery definitions, validated records, and sufficient sample sizes.



\## Completion Checklist



\- \[ ] Prompt file created.

\- \[ ] README created.

\- \[ ] Three test cases reviewed.

\- \[ ] KPI calculations checked.

\- \[ ] Files committed and pushed.

\- \[ ] Daily tracker updated.



