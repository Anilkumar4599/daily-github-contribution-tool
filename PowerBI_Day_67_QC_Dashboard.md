\# Power BI Day 67 — QC Dashboard



\## Objective



Load QC sample data into Power BI and create the first QC management dashboard.



\## Source Data



File:

QC\_Sample\_Data.xlsx



Columns:



\- Date

\- Device

\- Category

\- Inspected

\- Passed

\- Failed



\## Power BI Tasks Completed



1\. Imported Excel data

2\. Verified the data

3\. Created Total Units Inspected measure

4\. Created Total Units Passed measure

5\. Created Total Units Failed measure

6\. Created FPY % measure

7\. Created KPI cards

8\. Created device-wise failure chart

9\. Created category-wise failure chart

10\. Created device-level QC table



\## DAX Measures



\### Total Units Inspected



Total Units Inspected = SUM(QC\_Sample\_Data\[Inspected])



\### Total Units Passed



Total Units Passed = SUM(QC\_Sample\_Data\[Passed])



\### Total Units Failed



Total Units Failed = SUM(QC\_Sample\_Data\[Failed])



\### FPY %



FPY % = DIVIDE(\[Total Units Passed], \[Total Units Inspected], 0)



\## Expected Results



Total Units Inspected = 1000



Total Units Passed = 971



Total Units Failed = 29



FPY = 97.1%



\## Validation



\### Test Case 1 — Inspection Total



Expected:

1000



Result:

PASS / FAIL



\### Test Case 2 — Passed Total



Expected:

971



Result:

PASS / FAIL



\### Test Case 3 — Failed Total



Expected:

29



Result:

PASS / FAIL



\### Test Case 4 — FPY



Expected:

97.1%



Result:

PASS / FAIL



\## Power BI Output



Created:



\- Total Units Inspected KPI

\- Total Units Passed KPI

\- Total Units Failed KPI

\- FPY KPI

\- Device-wise failure chart

\- Category-wise failure chart

\- Device-level QC table



\## Assumptions



\- Sample data is hypothetical.

\- Data is created only for Power BI learning.

\- Actual company data is not used.

\- FPY is calculated using first-time passed units divided by total inspected units.

