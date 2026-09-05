\# QC Shipment Dashboard Layout



\## 1. Purpose



This document defines a sample layout for a future Power BI

shipment dashboard.



The dashboard is intended to provide management visibility into

shipment volume, shipment status, delivery performance, pending

shipments and operational issues.



This is a hypothetical learning example.



\---



\## 2. Dashboard Layout



```text

============================================================

&#x20;                QC SHIPMENT DASHBOARD

============================================================



FILTERS

\------------------------------------------------------------

Date | Customer | Location | Shipment Status | Product



\------------------------------------------------------------

KPI CARDS

\------------------------------------------------------------



Total Shipments | Completed | Pending | Delayed | Success %



\------------------------------------------------------------

SHIPMENT SUMMARY

\------------------------------------------------------------



Total Shipments

Completed

Pending

Delayed

Cancelled



\------------------------------------------------------------

SHIPMENT TREND

\------------------------------------------------------------



Date        Shipments

01-Sep      45

02-Sep      52

03-Sep      48

04-Sep      60

05-Sep      55



\------------------------------------------------------------

STATUS DISTRIBUTION

\------------------------------------------------------------



Completed     210

Pending        25

Delayed        15

Cancelled       5



\------------------------------------------------------------

LOCATION-WISE SHIPMENT

\------------------------------------------------------------



Location       Shipments

Chennai           80

Bangalore        65

Hyderabad        55

Mumbai           40

Delhi            15



\------------------------------------------------------------

MANAGEMENT ALERTS

\------------------------------------------------------------



1\. Delayed shipments require investigation.

2\. Pending shipments should be monitored.

3\. Locations with high shipment volume should be reviewed.

4\. Shipment performance should be monitored daily.



============================================================

3. Sample Input
Date	Location	Total Shipments	Completed	Pending	Delayed
2026-09-01	Chennai	45	40	3	2
2026-09-02	Chennai	52	48	2	2
2026-09-03	Bangalore	48	43	3	2
2026-09-04	Hyderabad	60	55	3	2
2026-09-05	Mumbai	55	49	4	2
4. Expected Output

Total Shipments:

45 + 52 + 48 + 60 + 55 = 260

Completed:

40 + 48 + 43 + 55 + 49 = 235

Pending:

3 + 2 + 3 + 3 + 4 = 15

Delayed:

2 + 2 + 2 + 2 + 2 = 10

Shipment Success Rate:

Completed / Total Shipments × 100

235 / 260 × 100 = 90.38%

Expected Output:

Total Shipments = 260
Completed = 235
Pending = 15
Delayed = 10
Shipment Success Rate = 90.38%

5. Power BI KPI Candidates

The dashboard can contain:

Total Shipments
Completed Shipments
Pending Shipments
Delayed Shipments
Cancelled Shipments
Shipment Success Rate
Daily Shipment Volume
Location-wise Shipment Volume
Pending Shipment %
Delayed Shipment %
6. Business Rules
Completed shipments must not be counted as pending.
Completed shipments must not be counted as delayed.
Total shipment count should reconcile with shipment statuses.
Shipment success rate should be calculated only when total shipments are greater than zero.
Delayed shipments should be highlighted for management review.
Pending shipments should be monitored until completion.
7. Validation Test Cases
Test Case 1 — Basic Shipment Calculation

Input:

Total Shipments = 100
Completed = 90

Expected:

Shipment Success Rate = 90%

Result: PASS

Test Case 2 — Zero Shipment Validation

Input:

Total Shipments = 0

Expected:

Invalid Input — Shipment success rate cannot be calculated.

Result: PASS

Test Case 3 — Status Reconciliation

Input:

Completed = 90
Pending = 5
Delayed = 5

Expected:

90 + 5 + 5 = 100

Result: PASS

Test Case 4 — Invalid Status Data

Input:

Total Shipments = 100
Completed = 110

Expected:

Invalid Input — Completed shipments cannot exceed total shipments.

Result: PASS

8. Management Insights

Based on the sample data:

Total shipment volume is 260.
235 shipments were completed.
15 shipments are pending.
10 shipments are delayed.
Shipment success rate is 90.38%.
Delayed shipments require operational review.
9. Recommended Power BI Visuals
Business Requirement	Recommended Visual
Total Shipments	KPI Card
Completed Shipments	KPI Card
Pending Shipments	KPI Card
Delayed Shipments	KPI Card
Shipment Trend	Line Chart
Status Distribution	Donut Chart
Location-wise Shipments	Bar Chart
Daily Shipment Volume	Column Chart
Management Alerts	Table/Card
10. Assumptions
This is a hypothetical learning dataset.
Each row represents one day's shipment summary.
Completed, Pending and Delayed are mutually exclusive for this example.
Actual shipment data should be validated before management reporting.
Power BI will be used later to create the interactive dashboard.
11. Future Improvements

The dashboard can later be enhanced with:

Customer-wise shipment analysis
Product-wise shipment analysis
Courier/vendor performance
Delivery TAT
Shipment aging
State-wise analysis
Daily/weekly/monthly trends
Automatic alerts
Power BI drill-down
AI-based shipment forecasting