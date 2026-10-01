\# Day 90 - Power BI: From Excel Data to Management Dashboard



\## 1. Concept



Power BI is a business intelligence tool used to convert data into interactive reports and dashboards.



A simple Power BI workflow is:



Excel Data

&#x20;   ↓

Power Query

&#x20;   ↓

Data Model

&#x20;   ↓

DAX Measures

&#x20;   ↓

Visualizations

&#x20;   ↓

Management Dashboard



The purpose is not only to display data, but to convert raw operational information into useful business insights.



\---



\## 2. Example Business Problem



A QC team may have daily inspection information containing:



\- Inspection Date

\- Device/Module

\- Units Inspected

\- Units Passed

\- Units Failed

\- Defect Category

\- Priority

\- Status



Management may want to know:



\- How many units were inspected?

\- How many passed?

\- How many failed?

\- What is the FPY percentage?

\- Which defect category is most common?

\- How many critical defects are open?



Doing these calculations manually every day can take time.



Power BI can automate the reporting and visualization of this information after the data model and calculations are configured.



\---



\## 3. Input Data



Example:



| Date | Module | Inspected | Passed | Failed | Priority |

|---|---|---:|---:|---:|---|

| 01-Oct-2026 | Camera | 100 | 97 | 3 | High |

| 01-Oct-2026 | Router | 80 | 76 | 4 | Critical |

| 02-Oct-2026 | Camera | 120 | 116 | 4 | Medium |

| 02-Oct-2026 | NVR | 100 | 98 | 2 | High |



This is sample data for learning.



\---



\## 4. Data Preparation



Before creating a dashboard, the data should be checked.



Important checks include:



\- Correct column names

\- Correct data types

\- Valid dates

\- Numeric quantities

\- No unexpected blank values

\- No duplicate records where duplicates are not allowed

\- Passed + Failed should be logically consistent with Inspected



Example:



Inspected = 100



Passed = 97



Failed = 3



The numbers are consistent because:



Passed + Failed = Inspected



\---



\## 5. Data Model



The cleaned data is loaded into the Power BI data model.



For a beginner project, a single clean table can be sufficient.



As projects become more complex, separate tables can be created for:



\- QC inspections

\- Defect master

\- Date/calendar

\- Device/module

\- Vendor



The data model determines how different pieces of information can be analysed together.



\---



\## 6. DAX Measures



DAX is used to create calculations in Power BI.



Examples of useful QC measures include:



Total Units Inspected



Total Units Passed



Total Units Failed



FPY %



Defect Count



Critical Defect Count



A simple FPY calculation concept is:



FPY % = Passed Units / Inspected Units × 100



Example:



Passed Units = 291



Inspected Units = 300



FPY = 97%



\---



\## 7. Dashboard



The final dashboard could contain:



\### KPI Cards



\- Total Units Inspected

\- Total Units Passed

\- Total Units Failed

\- FPY %



\### Charts



\- Passed vs Failed

\- Defects by Category

\- Defects by Module

\- Defects by Priority

\- Daily QC Trend



\### Filters



\- Date

\- Module

\- Priority

\- Status



This allows management to interact with the report rather than reviewing raw Excel rows.



\---



\## 8. Simple Logic



The overall logic is:



1\. Collect operational data.

2\. Validate the data.

3\. Clean the data.

4\. Load the data into Power BI.

5\. Create calculations.

6\. Create visualizations.

7\. Test the results.

8\. Use the dashboard for analysis.



The dashboard is only useful when the underlying data and calculations are correct.



\---



\## 9. Practical Experience vs Documentation



This document explains the Power BI concept.



It does not represent production Power BI experience.



Practical experience will require actually:



1\. Creating the Excel dataset.

2\. Importing it into Power BI.

3\. Cleaning the data.

4\. Creating DAX measures.

5\. Building the dashboard.

6\. Testing the numbers.

7\. Saving the PBIX project.

8\. Capturing evidence of the completed dashboard.



Therefore:



Documentation = Understanding



Hands-on project = Practical Experience



\---



\## 10. Planned Hands-on Project



The next practical Power BI project will be:



QC Management Dashboard



Expected workflow:



Excel

&#x20;   ↓

Power BI

&#x20;   ↓

Power Query

&#x20;   ↓

DAX

&#x20;   ↓

KPI Cards

&#x20;   ↓

Charts

&#x20;   ↓

Filters

&#x20;   ↓

QC Management Dashboard



The project will use fictional sample data for learning.



\---



\## 11. Conclusion



Power BI provides a way to transform operational data into management information.



The important learning is not simply knowing the names of Power BI features.



The real skill comes from being able to take raw data, clean it, calculate meaningful KPIs, build a dashboard, test the results, and explain the business insight.



The next step is therefore hands-on implementation rather than creating another documentation-only exercise.



\---



\## Author



MAK



AI Learning \& Technical Skills Development Journey

