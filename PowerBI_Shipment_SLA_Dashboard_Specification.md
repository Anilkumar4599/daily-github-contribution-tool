\# Power BI Shipment SLA Dashboard Specification



\## 1. Purpose



This dashboard is designed to monitor shipment performance against

the agreed Shipment Service Level Agreement (SLA).



The objective is to help management identify:



\- Total shipments

\- On-time shipments

\- Delayed shipments

\- SLA achievement percentage

\- Delayed shipment trends

\- Customer or location-level delays



This is a hypothetical learning example.



\---



\## 2. Sample Input Data



| Shipment ID | Customer | Shipment Date | Promised Date | Actual Delivery Date | Status |

|---|---|---|---|---|---|

| SH001 | Customer A | 2026-09-01 | 2026-09-03 | 2026-09-03 | On Time |

| SH002 | Customer B | 2026-09-01 | 2026-09-03 | 2026-09-04 | Delayed |

| SH003 | Customer C | 2026-09-02 | 2026-09-05 | 2026-09-05 | On Time |

| SH004 | Customer A | 2026-09-03 | 2026-09-06 | 2026-09-08 | Delayed |

| SH005 | Customer B | 2026-09-04 | 2026-09-07 | 2026-09-07 | On Time |

| SH006 | Customer C | 2026-09-05 | 2026-09-08 | 2026-09-09 | Delayed |

| SH007 | Customer A | 2026-09-06 | 2026-09-09 | 2026-09-09 | On Time |

| SH008 | Customer B | 2026-09-07 | 2026-09-10 | 2026-09-10 | On Time |

| SH009 | Customer C | 2026-09-08 | 2026-09-11 | 2026-09-13 | Delayed |

| SH010 | Customer A | 2026-09-09 | 2026-09-12 | 2026-09-12 | On Time |



\---



\## 3. Key KPIs



The dashboard should contain the following KPI cards:



\### KPI 1 — Total Shipments



Expected value:



10



\### KPI 2 — On-Time Shipments



Expected value:



6



\### KPI 3 — Delayed Shipments



Expected value:



4



\### KPI 4 — SLA Achievement



Formula:



SLA Achievement (%) =

On-Time Shipments / Total Shipments × 100



Expected result:



6 / 10 × 100 = 60%



\---



\## 4. Dashboard Layout



Recommended dashboard structure:



\### Top Row — KPI Cards



1\. Total Shipments

2\. On-Time Shipments

3\. Delayed Shipments

4\. SLA Achievement %



\### Middle Section



Recommended visuals:



\- On-Time vs Delayed Shipment chart

\- Shipment SLA trend

\- Customer-wise SLA performance



\### Bottom Section



Recommended table:



| Customer | Total Shipments | On-Time | Delayed | SLA % |

|---|---:|---:|---:|---:|

| Customer A | 4 | 3 | 1 | 75% |

| Customer B | 3 | 2 | 1 | 66.67% |

| Customer C | 3 | 1 | 2 | 33.33% |



\---



\## 5. Business Rules



A shipment is considered On Time when:



Actual Delivery Date <= Promised Date



A shipment is considered Delayed when:



Actual Delivery Date > Promised Date



SLA Achievement is calculated as:



On-Time Shipments / Total Shipments × 100



\---



\## 6. Example Expected Output



Total Shipments = 10



On-Time Shipments = 6



Delayed Shipments = 4



SLA Achievement = 60%



Management interpretation:



60% of shipments were delivered within the agreed SLA.



40% of shipments were delayed and require further investigation.



\---



\## 7. Test Cases



\### Test Case 1 — On-Time Shipment



Input:



Promised Date = 2026-09-03



Actual Delivery Date = 2026-09-03



Expected Result:



Status = On Time



Result:



PASS



\---



\### Test Case 2 — Delayed Shipment



Input:



Promised Date = 2026-09-03



Actual Delivery Date = 2026-09-04



Expected Result:



Status = Delayed



Result:



PASS



\---



\### Test Case 3 — SLA Calculation



Input:



Total Shipments = 10



On-Time Shipments = 6



Expected Result:



SLA Achievement = 60%



Result:



PASS



\---



\## 8. Management Actions



If SLA achievement decreases:



1\. Identify delayed shipments.

2\. Identify customers with high delay rates.

3\. Review shipment dates and delivery dates.

4\. Identify recurring delay reasons.

5\. Assign corrective actions.

6\. Monitor SLA improvement.



\---



\## 9. Assumptions



\- This is a hypothetical learning dataset.

\- Dates are sample dates.

\- The data does not represent actual company information.

\- SLA is calculated based on promised delivery date versus actual delivery date.

\- Actual business SLA rules may include additional conditions.



\---



\## 10. Future Power BI Implementation



This specification can later be implemented in Power BI.



Possible Power BI components:



\- KPI Cards

\- Bar Chart

\- Line Chart

\- Customer-wise SLA table

\- Slicers

\- DAX measures

\- Conditional formatting



\---



\## 11. Learning Objective



This exercise demonstrates how a business requirement can first be

converted into a dashboard specification before building the actual

Power BI dashboard.



The next stage is to implement this specification in Power BI Desktop.

