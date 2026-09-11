\# Day 70 - Power BI Data Cleaning Checklist



\## 1. Purpose



The purpose of this checklist is to ensure that data is clean, consistent, and ready for Power BI analysis.



Data cleaning should be completed before creating dashboards, charts, KPIs, and DAX measures.



\---



\## 2. Simple Data-Cleaning Checklist



| No. | Check | What to Verify | Example |

|---|---|---|---|

| 1 | Missing Values | Check for blank or empty values | Customer name is blank |

| 2 | Duplicate Records | Check whether the same record appears more than once | Shipment SH001 repeated |

| 3 | Date Format | Ensure all dates use the same format | 10-09-2026 |

| 4 | Number Format | Ensure numeric columns contain numbers | Quantity = 100 |

| 5 | Text Consistency | Check spelling and naming consistency | Chennai vs chennai |

| 6 | Extra Spaces | Remove unnecessary spaces | " Chennai " → "Chennai" |

| 7 | Invalid Values | Check for impossible or incorrect values | Quantity = -50 |

| 8 | Column Names | Use clear and meaningful column names | Shipment\_ID |

| 9 | Data Types | Confirm correct data type | Date column should be Date |

| 10 | Business Validation | Check whether data makes business sense | Actual delivery date should not be blank for completed shipment |



\---



\## 3. Simple Implementation



The cleaning process can be performed using Power Query in Power BI.



\### Basic Process



1\. Load the data into Power BI.

2\. Open Power Query.

3\. Check column names.

4\. Check data types.

5\. Remove unnecessary columns.

6\. Remove duplicate records.

7\. Handle blank values.

8\. Clean text values.

9\. Validate dates and numbers.

10\. Apply the changes.

11\. Load the cleaned data into the Power BI model.



\---



\## 4. Example Input



\### Raw Shipment Data



| Shipment\_ID | Customer | Shipment\_Date | Quantity | Status |

|---|---|---|---:|---|

| SH001 | ABC Bank | 09-09-2026 | 100 | Delivered |

| SH002 | abc bank | 09-09-2026 | 50 | Delivered |

| SH003 |  XYZ Bank  | 10-09-2026 | 75 | Pending |

| SH003 | XYZ Bank | 10-09-2026 | 75 | Pending |

| SH004 | | 10-09-2026 | -20 | Delivered |



\---



\## 5. Problems Identified



The raw data contains several issues:



\### SH002

Customer name is written as:



`abc bank`



It should follow the same naming convention as:



`ABC Bank`



\### SH003

There are unnecessary spaces around:



` XYZ Bank `



The spaces should be removed.



\### SH003

The record appears twice.



This is a duplicate record.



\### SH004

Customer name is blank.



This requires validation or correction.



\### SH004

Quantity is `-20`.



A negative shipment quantity is considered invalid for this example.



\---



\## 6. Expected Cleaned Output



| Shipment\_ID | Customer | Shipment\_Date | Quantity | Status |

|---|---|---|---:|---|

| SH001 | ABC Bank | 09-09-2026 | 100 | Delivered |

| SH002 | ABC Bank | 09-09-2026 | 50 | Delivered |

| SH003 | XYZ Bank | 10-09-2026 | 75 | Pending |



SH004 should be kept aside for business validation because the customer is missing and the quantity is invalid.



\---



\## 7. Simple Cleaning Logic



The cleaning logic is:



\### Step 1 - Remove duplicates



If the same Shipment\_ID appears more than once, investigate and remove the duplicate where appropriate.



\### Step 2 - Clean text



Remove unnecessary spaces and standardize text values.



Example:



` XYZ Bank `



becomes:



`XYZ Bank`



\### Step 3 - Standardize names



Example:



`abc bank`



becomes:



`ABC Bank`



\### Step 4 - Validate numbers



Check whether quantity is a valid positive number.



Example:



`-20`



should be flagged as invalid.



\### Step 5 - Validate missing values



If an important field such as Customer is blank, do not automatically guess the value.



Flag it for business validation.



\---



\## 8. Power BI Implementation



For a simple implementation in Power Query:



\- Remove Rows → Remove Duplicates

\- Transform → Format → Trim

\- Transform → Format → Clean

\- Change Data Type → Date

\- Change Data Type → Whole Number

\- Filter or flag invalid values

\- Review null/blank values



The objective is not to change data blindly.



The objective is to make the data reliable for reporting while preserving business accuracy.



\---



\## 9. Test Cases



\### Test Case 1 - Duplicate Record



\*\*Input:\*\* SH003 appears twice.



\*\*Expected Result:\*\* Only one valid SH003 record remains after duplicate validation.



\*\*Status:\*\* PASS



\---



\### Test Case 2 - Extra Spaces



\*\*Input:\*\* ` XYZ Bank `



\*\*Expected Result:\*\* `XYZ Bank`



\*\*Status:\*\* PASS



\---



\### Test Case 3 - Invalid Quantity



\*\*Input:\*\* Quantity = `-20`



\*\*Expected Result:\*\* Record is flagged for business validation.



\*\*Status:\*\* PASS



\---



\## 10. Final Validation Checklist



Before creating a Power BI dashboard, confirm:



\- \[ ] No unexpected duplicate records

\- \[ ] Important fields are not blank

\- \[ ] Text values are consistent

\- \[ ] Unnecessary spaces are removed

\- \[ ] Dates have the correct data type

\- \[ ] Numeric columns have the correct data type

\- \[ ] Invalid values are identified

\- \[ ] Column names are clear

\- \[ ] Business rules are validated

\- \[ ] Cleaned data is ready for Power BI analysis



\---



\## 11. Key Learning



Data cleaning is an important step before Power BI reporting.



A dashboard is only as reliable as the data behind it.



Simple rule:



\*\*Raw Data → Clean Data → Validate Data → Power BI Model → DAX → Dashboard\*\*



\---



\## 12. Day 70 Conclusion



A simple data-cleaning checklist was created for Power BI.



The checklist covers:



\- Missing values

\- Duplicate records

\- Text cleaning

\- Date validation

\- Number validation

\- Data types

\- Invalid values

\- Business validation



This checklist can be reused for future QC, inventory, shipment, and procurement dashboards.

