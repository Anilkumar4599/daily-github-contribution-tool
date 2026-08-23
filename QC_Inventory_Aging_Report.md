\# Inventory Aging Report — ATM Surveillance Devices



\## 1. Purpose



This document demonstrates a sample inventory aging analysis for

ATM surveillance devices.



The objective is to identify inventory that has remained unused for

long periods and may require attention from Inventory, Procurement,

QC and Shipment teams.



This is a hypothetical learning example.



\---



\## 2. Inventory Aging Concept



Inventory aging measures how long an item has remained in inventory

without being consumed, shipped or otherwise moved.



The basic logic is:



Current Date - Stock Entry Date = Inventory Age



Older inventory should receive greater management attention.



\---



\## 3. Aging Categories



| Aging Bucket | Age Range | Management Meaning |

|---|---:|---|

| Fresh | 0–30 days | Normal inventory |

| Aging | 31–60 days | Monitor |

| Old | 61–90 days | Action required |

| Critical Aging | >90 days | Immediate review |



\---



\## 4. Sample Inventory Dataset



The following sample data is hypothetical.



| Item ID | Device | Quantity | Stock Entry Date | Inventory Age | Aging Bucket | Status |

|---|---|---:|---|---:|---|---|

| INV-001 | Main Unit | 100 | 2026-08-10 | 13 | Fresh | Available |

| INV-002 | Lobby Camera | 75 | 2026-07-05 | 49 | Aging | Available |

| INV-003 | Router | 50 | 2026-06-10 | 74 | Old | Available |

| INV-004 | DCUPS | 40 | 2026-05-15 | 100 | Critical Aging | Review |

| INV-005 | Sensor Bag | 60 | 2026-08-01 | 22 | Fresh | Available |

| INV-006 | Outdoor Camera | 30 | 2026-04-20 | 125 | Critical Aging | Review |

| INV-007 | PCMU | 45 | 2026-07-20 | 34 | Aging | Available |

| INV-008 | Lobby Unit | 25 | 2026-06-25 | 59 | Aging | Available |



\---



\## 5. Aging Summary



| Aging Bucket | Number of Items | Quantity |

|---|---:|---:|

| Fresh | 2 | 160 |

| Aging | 3 | 145 |

| Old | 1 | 50 |

| Critical Aging | 2 | 70 |

| Total | 8 | 425 |



\---



\## 6. Aging Percentage



Total Inventory Quantity = 425



Fresh Inventory = 160



Aging Inventory = 145



Old Inventory = 50



Critical Aging Inventory = 70



\### Fresh Inventory %



160 / 425 × 100 = 37.65%



\### Aging Inventory %



145 / 425 × 100 = 34.12%



\### Old Inventory %



50 / 425 × 100 = 11.76%



\### Critical Aging %



70 / 425 × 100 = 16.47%



\---



\## 7. Management Observation



The sample inventory contains 425 units.



70 units are classified as Critical Aging.



Therefore:



Critical Aging % = 16.47%



These items should receive immediate review.



Management should determine whether these items are:



\- Required for upcoming shipments

\- Excess inventory

\- Slow-moving inventory

\- Obsolete inventory

\- Awaiting QC clearance

\- Awaiting configuration

\- Blocked due to technical issues



\---



\## 8. Recommended Actions



\### Fresh Inventory



Continue normal inventory monitoring.



\### Aging Inventory



Review upcoming shipment requirements and consumption trends.



\### Old Inventory



Create an action plan to consume or redistribute the inventory.



\### Critical Aging Inventory



Perform immediate management review.



Check:



1\. Why has the inventory remained unused?

2\. Is there an upcoming requirement?

3\. Is the device technically usable?

4\. Is QC clearance pending?

5\. Is the item obsolete?

6\. Can the item be allocated to another location or project?



\---



\## 9. Management Logic



The inventory aging process follows:



Stock Entry Date

&#x20;       ↓

Calculate Inventory Age

&#x20;       ↓

Assign Aging Bucket

&#x20;       ↓

Identify Slow-Moving Inventory

&#x20;       ↓

Prioritize Critical Aging

&#x20;       ↓

Take Corrective Action



\---



\## 10. Validation Test Cases



\### Test Case 1 — Total Quantity



Expected:



160 + 145 + 50 + 70 = 425



Result: PASS



\---



\### Test Case 2 — Aging Bucket Count



Expected:



Fresh = 2



Aging = 3



Old = 1



Critical Aging = 2



Total = 8



Result: PASS



\---



\### Test Case 3 — Critical Aging Percentage



Critical Aging Quantity = 70



Total Quantity = 425



70 / 425 × 100 = 16.47%



Result: PASS



\---



\### Test Case 4 — Highest Aging Item



Expected:



INV-006 — Outdoor Camera — 125 days



Result: PASS



\---



\### Test Case 5 — Critical Aging Items



Expected:



INV-004 — DCUPS — 100 days



INV-006 — Outdoor Camera — 125 days



Result: PASS



\---



\## 11. Key KPI



\### Critical Aging Inventory %



Critical Aging Quantity / Total Inventory Quantity × 100



Example:



70 / 425 × 100 = 16.47%



Therefore:



Critical Aging Inventory = 16.47%



\---



\## 12. Management Recommendation



If Critical Aging Inventory increases over time:



1\. Review consumption trends.

2\. Check upcoming shipment requirements.

3\. Identify slow-moving devices.

4\. Review excess inventory.

5\. Check technical or QC blocks.

6\. Coordinate with Procurement and Shipment teams.

7\. Create an action plan for aged inventory.



\---



\## 13. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company inventory.

\- Inventory age is calculated from the sample stock entry date.

\- Aging buckets are defined for demonstration purposes.

\- Actual business aging rules may differ.

\- Inventory quantities should be validated against the actual inventory system.



\---



\## 14. Future Automation



This inventory aging report can later be automated using:



\- Excel

\- Python

\- Power BI

\- SQL

\- Automated inventory dashboards

\- AI-assisted inventory analysis

s

