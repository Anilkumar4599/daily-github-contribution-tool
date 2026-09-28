\# Input Validation - Day 87



\## Objective



Input validation ensures that incorrect or incomplete information is identified before it is used for analysis, reporting, or automation.



\---



\## Validation Rules



| Field | Rule |

|---|---|

| Record ID | Cannot be blank |

| Category | Must be an approved category |

| Quantity | Must be a valid number |

| Quantity | Cannot be negative |

| Status | Must be an approved status |

| Date | Must use a valid date |

| Duplicate Record | Should be identified |



\---



\## Approved Categories



\- QC

\- Procurement

\- Inventory

\- Power BI

\- AWS

\- DevOps

\- AI



\---



\## Approved Status Values



\- Open

\- Working

\- Completed

\- Cancelled



\---



\## Test Cases



\### Test Case 1 — Valid Record



Input:



```text

Record ID: QC001

Category: QC

Quantity: 10

Status: Completed





Test Case 2 — Negative Quantity



Input:



Record ID: QC002

Category: QC

Quantity: -5

Status: Open



Expected Result:



FAIL - Quantity cannot be negative

Test Case 3 — Invalid Status



Input:



Record ID: QC003

Category: QC

Quantity: 5

Status: ABC



Expected Result:



FAIL - Invalid status

Test Case 4 — Missing Record ID



Input:



Record ID:

Category: Inventory

Quantity: 10

Status: Completed



Expected Result:



FAIL - Record ID is required

Test Case 5 — Invalid Category



Input:



Record ID: PO001

Category: Finance

Quantity: 10

Status: Completed



Expected Result:



FAIL - Invalid category

Validation Principle



Invalid data should be identified before:



Analysis

Dashboard creation

Reporting

Automation

Management decision-making

Conclusion



Simple input validation reduces data-quality problems and improves the reliability of reports and automation.





Save and close Notepad.



\---



\# Step 3 — Check the files



Run:



```bash

ls -l Project\_README\_Day\_87.md Input\_Validation\_Day\_87.md

