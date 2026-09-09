\# Power BI Vendor Performance Dashboard Specification



\## 1. Purpose



This document defines a sample Power BI dashboard for monitoring vendor performance.



The dashboard is intended to help management identify:



\- Vendor delivery performance

\- Quality performance

\- Defect levels

\- Rejection rates

\- On-time delivery

\- Vendor-related risks



This is a hypothetical learning example.



\---



\## 2. Business Objective



The dashboard should help management answer:



1\. Which vendors are performing well?

2\. Which vendors have poor quality performance?

3\. Which vendors have delivery delays?

4\. Which vendors have high rejection rates?

5\. Which vendors require corrective action?



\---



\## 3. Sample Vendor Dataset



| Vendor | Category | Ordered Qty | Received Qty | Accepted Qty | Rejected Qty | On-Time Deliveries | Total Deliveries |

|---|---|---:|---:|---:|---:|---:|---:|

| Vendor A | Camera | 500 | 500 | 485 | 15 | 9 | 10 |

| Vendor B | Router | 400 | 380 | 360 | 20 | 7 | 10 |

| Vendor C | Sensor | 600 | 600 | 594 | 6 | 10 | 10 |

| Vendor D | DCUPS | 300 | 290 | 275 | 15 | 8 | 10 |

| Vendor E | Main Unit | 250 | 250 | 242 | 8 | 9 | 10 |



\---



\## 4. Recommended KPIs



\### KPI 1 — Ordered Quantity



Total quantity ordered from vendors.



Example:



500 + 400 + 600 + 300 + 250 = 2,050



Expected result:



2050 units



\---



\### KPI 2 — Received Quantity



Total quantity received from vendors.



Expected result:



500 + 380 + 600 + 290 + 250 = 2,020 units



\---



\### KPI 3 — Accepted Quantity



Total quantity accepted after QC inspection.



Expected result:



485 + 360 + 594 + 275 + 242 = 1,956 units



\---



\### KPI 4 — Rejected Quantity



Total quantity rejected during QC.



Expected result:



15 + 20 + 6 + 15 + 8 = 64 units



\---



\### KPI 5 — Rejection Rate



Formula:



Rejection Rate (%) =

Rejected Quantity / Received Quantity × 100



Example:



64 / 2020 × 100 = 3.17%



Expected result:



3.17%



\---



\### KPI 6 — On-Time Delivery Rate



Formula:



On-Time Delivery Rate (%) =

On-Time Deliveries / Total Deliveries × 100



Example:



Vendor A:



9 / 10 × 100 = 90%



\---



\## 5. Recommended Dashboard Layout



The dashboard should contain four main KPI cards:



| KPI | Example |

|---|---:|

| Total Ordered | 2,050 |

| Total Received | 2,020 |

| Total Rejected | 64 |

| Rejection Rate | 3.17% |



\---



\## 6. Recommended Visuals



\### Visual 1 — Vendor Rejection Rate



Chart:



Vendor vs Rejection Rate



Purpose:



Identify vendors with high rejection rates.



\---



\### Visual 2 — Vendor On-Time Delivery



Chart:



Vendor vs On-Time Delivery Rate



Purpose:



Identify vendors with delivery performance problems.



\---



\### Visual 3 — Accepted vs Rejected Quantity



Chart:



Vendor vs Accepted Quantity vs Rejected Quantity



Purpose:



Compare vendor quality performance.



\---



\### Visual 4 — Vendor Performance Table



The table should contain:



| Vendor | Ordered | Received | Accepted | Rejected | Rejection % | On-Time % |

|---|---:|---:|---:|---:|---:|---:|



\---



\## 7. Recommended Filters



The dashboard should eventually include:



\- Vendor

\- Category

\- Date

\- Performance status



These filters should allow management to focus on a specific vendor or product category.



\---



\## 8. Vendor Performance Classification



Sample classification:



| Rejection Rate | Performance |

|---:|---|

| 0%–2% | Good |

| >2%–5% | Watch |

| >5% | Poor |



This is a sample learning rule and should be validated before real business use.



\---



\## 9. Management Actions



If a vendor has high rejection:



1\. Review rejected items.

2\. Identify recurring defects.

3\. Perform Root Cause Analysis.

4\. Contact the vendor.

5\. Create corrective action.

6\. Monitor vendor performance after correction.



If on-time delivery is low:



1\. Review delivery delays.

2\. Identify affected orders.

3\. Discuss recovery plan with vendor.

4\. Monitor future deliveries.



\---



\# 10. Test Cases



\## Test Case 1 — Rejection Quantity



Input:



Vendor A Rejected Quantity = 15



Expected:



Vendor A rejection quantity should display as 15.



Result:



PASS



\---



\## Test Case 2 — Rejection Rate



Input:



Total Rejected = 64



Total Received = 2,020



Calculation:



64 / 2020 × 100 = 3.17%



Expected:



Rejection Rate = 3.17%



Result:



PASS



\---



\## Test Case 3 — On-Time Delivery Rate



Input:



Vendor A:



On-Time Deliveries = 9



Total Deliveries = 10



Calculation:



9 / 10 × 100 = 90%



Expected:



Vendor A On-Time Delivery Rate = 90%



Result:



PASS



\---



\## Test Case 4 — Data Reconciliation



Accepted Quantity + Rejected Quantity should equal Received Quantity.



For all vendors:



Vendor A:



485 + 15 = 500



Vendor B:



360 + 20 = 380



Vendor C:



594 + 6 = 600



Vendor D:



275 + 15 = 290



Vendor E:



242 + 8 = 250



Expected:



All vendor quantities reconcile correctly.



Result:



PASS



\---



\## 11. Assumptions



\- This is a hypothetical learning dataset.

\- Vendor names are sample names.

\- The data does not represent actual company information.

\- Rejection-rate thresholds are sample management rules.

\- Actual vendor performance should be calculated using validated production data.

\- KPI definitions should be agreed with management before deployment.



\---



\## 12. Future Power BI Implementation



This specification can later be implemented in Power BI using:



\- Excel as the source

\- Power Query for data preparation

\- DAX measures for KPI calculations

\- KPI cards

\- Bar charts

\- Tables

\- Slicers

\- Conditional formatting



\---



\## 13. Expected Management Outcome



The dashboard should allow management to quickly identify:



\- Best-performing vendors

\- Poor-quality vendors

\- Vendors with delivery delays

\- High rejection rates

\- Vendors requiring corrective action



The final objective is to improve vendor quality, delivery performance, and overall supply reliability.

