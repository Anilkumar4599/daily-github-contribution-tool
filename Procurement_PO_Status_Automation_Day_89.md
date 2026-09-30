\# Day 89 - Procurement PO Status Automation



\## 1. Project Overview



This project documents a manual procurement process that could be automated using Python and Excel.



The objective is to identify pending purchase orders, calculate pending quantities, identify delayed POs, and classify procurement risk.



The current process requires manually reviewing PO information and calculating status.



The future objective is to automate these calculations and generate a management-ready report.



\---



\# 2. Current Manual Process



The current process can be represented as:



Excel PO Data

&#x20;   ↓

Review PO records

&#x20;   ↓

Check ordered quantity

&#x20;   ↓

Check received quantity

&#x20;   ↓

Calculate pending quantity

&#x20;   ↓

Check expected delivery date

&#x20;   ↓

Calculate delay

&#x20;   ↓

Identify PO status

&#x20;   ↓

Identify risk

&#x20;   ↓

Prepare report



\---



\# 3. Manual Activities



The following activities are currently performed manually:



1\. Open the PO data file.

2\. Review each PO.

3\. Compare ordered quantity with received quantity.

4\. Calculate pending quantity.

5\. Compare expected delivery date with the current date.

6\. Identify delayed POs.

7\. Assign a risk level.

8\. Prepare a summary for management.



\---



\# 4. Example Input



Sample input data:



| PO Number | Vendor | PO Date | Expected Date | Ordered Qty | Received Qty |

|---|---|---|---|---:|---:|

| PO001 | Vendor A | 2026-09-01 | 2026-09-20 | 100 | 100 |

| PO002 | Vendor B | 2026-09-03 | 2026-09-25 | 200 | 150 |

| PO003 | Vendor C | 2026-09-05 | 2026-09-28 | 50 | 20 |

| PO004 | Vendor D | 2026-09-10 | 2026-10-05 | 100 | 0 |

| PO005 | Vendor E | 2026-09-12 | 2026-09-15 | 75 | 75 |



All data above is fictional and is used only for learning.



\---



\# 5. Required Calculations



\## Pending Quantity



Pending Quantity should be calculated as:



Pending Quantity = Ordered Quantity - Received Quantity



Example:



Ordered Quantity = 200



Received Quantity = 150



Pending Quantity = 50



\---



\## PO Status



Suggested status rules:



\### Completed



Received Quantity = Ordered Quantity



\### Partially Received



Received Quantity > 0 AND Received Quantity < Ordered Quantity



\### Not Received



Received Quantity = 0



\---



\## Delay



For this learning exercise:



Delay should be calculated by comparing the Expected Date with the reporting date.



If the Expected Date has already passed and the PO is not fully received, the PO is considered delayed.



\---



\# 6. Risk Classification



Suggested learning rules:



\### Low



PO is completed and there is no pending quantity.



\### Medium



PO has pending quantity but is not delayed.



\### High



PO has pending quantity and is delayed.



\---



\# 7. Expected Output



The expected automated output should contain:



| PO Number | Vendor | Ordered Qty | Received Qty | Pending Qty | Status | Risk |

|---|---|---:|---:|---:|---|---|

| PO001 | Vendor A | 100 | 100 | 0 | Completed | Low |

| PO002 | Vendor B | 200 | 150 | 50 | Partially Received | Medium |

| PO003 | Vendor C | 50 | 20 | 30 | Partially Received | High |

| PO004 | Vendor D | 100 | 0 | 100 | Not Received | High |

| PO005 | Vendor E | 75 | 75 | 0 | Completed | Low |



\---



\# 8. Management Summary



The automated process should eventually provide a summary such as:



Total POs: 5



Completed POs: 2



Partially Received POs: 2



Not Received POs: 1



High Risk POs: 2



Medium Risk POs: 1



Low Risk POs: 2



Total Ordered Quantity: 525



Total Received Quantity: 345



Total Pending Quantity: 180



\---



\# 9. Automation Opportunity



The following manual activities could be automated:



| Manual Activity | Possible Automation |

|---|---|

| Read PO Excel file | Python |

| Calculate pending quantity | Python |

| Determine PO status | Python |

| Calculate delay | Python |

| Classify risk | Python |

| Create summary | Python |

| Generate output Excel | Python |

| Identify high-risk POs | Python |

| Prepare management report | Python |



\---



\# 10. Future Automation Design



The future solution could work as follows:



Excel Input

&#x20;   ↓

Python Program

&#x20;   ↓

Input Validation

&#x20;   ↓

Calculate Pending Quantity

&#x20;   ↓

Calculate Delay

&#x20;   ↓

Determine PO Status

&#x20;   ↓

Determine Risk

&#x20;   ↓

Generate Output

&#x20;   ↓

Management Report



\---



\# 11. Input Validation Requirements



Before processing the data, the future automation should check:



1\. PO Number is not blank.

2\. Vendor name is not blank.

3\. PO Date is valid.

4\. Expected Date is valid.

5\. Ordered Quantity is numeric.

6\. Received Quantity is numeric.

7\. Quantities are not negative.

8\. Received Quantity should not exceed Ordered Quantity.

9\. Duplicate PO numbers should be identified.



\---



\# 12. Test Cases



\## Test Case 1 - Completed PO



Input:



Ordered Qty = 100



Received Qty = 100



Expected Result:



Status = Completed



Risk = Low



Result: PASS



\---



\## Test Case 2 - Partially Received PO



Input:



Ordered Qty = 200



Received Qty = 150



Expected Result:



Pending Qty = 50



Status = Partially Received



Result: PASS



\---



\## Test Case 3 - Not Received PO



Input:



Ordered Qty = 100



Received Qty = 0



Expected Result:



Pending Qty = 100



Status = Not Received



Result: PASS



\---



\## Test Case 4 - Invalid Quantity



Input:



Ordered Qty = 100



Received Qty = 120



Expected Result:



Validation Failure



Reason:



Received quantity cannot exceed ordered quantity.



Result: PASS



\---



\## Test Case 5 - Missing PO Number



Input:



PO Number = Blank



Expected Result:



Validation Failure



Reason:



PO Number is mandatory.



Result: PASS



\---



\# 13. Business Benefit



If implemented, this automation could help reduce:



\- Manual calculation effort

\- Excel formula errors

\- Delayed PO identification time

\- Report preparation effort



It could also improve:



\- Procurement visibility

\- Pending PO monitoring

\- Vendor follow-up

\- Risk identification

\- Management reporting



\---



\# 14. Current Status



Status: Documentation / Process Design



This Day 89 activity documents the automation opportunity.



It does NOT represent a completed Python automation.



The actual Python implementation will be treated as a separate hands-on project.



\---



\# 15. Future Hands-on Project



Planned implementation:



1\. Create sample Excel input file.

2\. Write Python program.

3\. Read Excel data.

4\. Validate input.

5\. Calculate pending quantity.

6\. Calculate delay.

7\. Determine PO status.

8\. Determine risk.

9\. Generate output Excel file.

10\. Test the program with valid and invalid records.

11\. Store the project in GitHub.



\---



\# 16. Learning Principle



Documentation identifies what should be automated.



Hands-on implementation demonstrates that the automation actually works.



Therefore:



Documentation ≠ Practical Implementation



The next stage should convert this process design into a working Python project.



\---



\## Author



MAK



AI Learning \& Technical Skills Development Journey



\---



\## Disclaimer



All sample procurement data in this document is fictional and intended only for learning and demonstration.

