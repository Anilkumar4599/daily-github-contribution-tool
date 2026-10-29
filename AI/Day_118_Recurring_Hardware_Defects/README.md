\# Day 118 — Recurring Hardware Defect Analysis



\## Project Overview



A reusable AI prompt for identifying recurring hardware defect patterns in ATM E-Surveillance QC records.



\## Objectives



\- Identify repeated hardware failure symptoms.

\- Group candidate defects using module and test evidence.

\- Detect missing or inconsistent defect information.

\- Quantify recurrence when valid data is available.

\- Prioritise engineering investigations.

\- Recommend evidence-based corrective actions.



\## Project Files



\- `Recurring\_Hardware\_Defect\_Analysis\_Prompt.md` — Reusable prompt, validation rules, sample data, expected output, and three test cases.

\- `README.md` — Project overview and usage instructions.



\## How to Use



1\. Provide the QC defect tracker and reporting date.

2\. Validate defect IDs, modules, dates, statuses, and evidence.

3\. Run the prompt against the supplied records.

4\. Review candidate recurrence groups.

5\. Verify physical-unit identifiers, logs, and test results.

6\. Confirm root causes through engineering investigation.

7\. Track corrective actions and retest evidence.



\## Validation Rules



\- Similar symptoms do not prove a common root cause.

\- Duplicate records must be reviewed before counting recurrence.

\- Failure rates require valid trial and failure counts.

\- A defect must not be marked resolved without closure evidence.

\- Unknown information must remain explicitly unknown.



\## Test Cases



1\. Identify repeated DCUPS failure symptoms.

2\. Avoid unsupported grouping of different backup-power symptoms.

3\. Detect missing trial counts and avoid fabricating failure rates.



\## Limitations



The sample data is fictional. AI findings support investigation but do not replace engineering validation or formal QC approval.



\## Completion Checklist



\- \[ ] Prompt file created.

\- \[ ] README created.

\- \[ ] Three test cases reviewed.

\- \[ ] Calculations and assumptions checked.

\- \[ ] Files committed and pushed.

\- \[ ] Daily tracker updated.



