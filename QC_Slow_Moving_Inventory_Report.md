\# QC Slow-Moving Inventory Report



\## 1. Purpose



This document provides a simple example for identifying slow-moving

inventory items.



The objective is to identify items where the current stock level is

relatively high compared with average daily consumption.



This can help inventory management reduce excess stock and improve

inventory utilization.



This is a hypothetical learning example.



\---



\## 2. Slow-Moving Definition



For this learning example:



An item is classified as Slow Moving when stock coverage is greater

than 30 days.



Stock Coverage (Days) = Current Stock / Average Daily Consumption



\---



\## 3. Sample Input Data



| Item | Current Stock | Average Daily Consumption |

|---|---:|---:|

| Main Unit | 80 | 5 |

| Lobby Camera | 150 | 8 |

| Backroom Camera | 120 | 4 |

| Router | 45 | 6 |

| DCUPS | 90 | 3 |

| Sensor Bag | 25 | 5 |



\---



\## 4. Stock Coverage Calculation



\### Main Unit



Current Stock = 80



Average Daily Consumption = 5



Stock Coverage:



80 / 5 = 16 days



Classification: Normal



\---



\### Lobby Camera



Current Stock = 150



Average Daily Consumption = 8



Stock Coverage:



150 / 8 = 18.75 days



Classification: Normal



\---



\### Backroom Camera



Current Stock = 120



Average Daily Consumption = 4



Stock Coverage:



120 / 4 = 30 days



Classification: Normal



\---



\### Router



Current Stock = 45



Average Daily Consumption = 6



Stock Coverage:



45 / 6 = 7.5 days



Classification: Normal



\---



\### DCUPS



Current Stock = 90



Average Daily Consumption = 3



Stock Coverage:



90 / 3 = 30 days



Classification: Normal



\---



\### Sensor Bag



Current Stock = 25



Average Daily Consumption = 5



Stock Coverage:



25 / 5 = 5 days



Classification: Normal



\---



\## 5. Important Observation



The sample dataset above does not contain an item with stock coverage

greater than 30 days.



Therefore, no item is classified as Slow Moving.



To demonstrate the slow-moving condition, the following additional

example is used.



\---



\## 6. Slow-Moving Example



Item: Backroom Camera



Current Stock = 160



Average Daily Consumption = 4



Stock Coverage:



160 / 4 = 40 days



Since:



40 > 30



Classification:



Slow Moving



\---



\## 7. Expected Output



| Item | Current Stock | Daily Consumption | Coverage Days | Classification |

|---|---:|---:|---:|---|

| Main Unit | 80 | 5 | 16 | Normal |

| Lobby Camera | 150 | 8 | 18.75 | Normal |

| Backroom Camera | 160 | 4 | 40 | Slow Moving |

| Router | 45 | 6 | 7.5 | Normal |

| DCUPS | 90 | 3 | 30 | Normal |

| Sensor Bag | 25 | 5 | 5 | Normal |



\---



\## 8. Management Finding



Backroom Camera is classified as Slow Moving in the sample example.



Stock Coverage = 40 days.



The item should be reviewed for:



\- Excess inventory

\- Reduced consumption

\- Historical demand

\- Open shipment requirements

\- Future project requirements

\- Procurement planning

\- Possible inventory redistribution



\---



\## 9. Management Action



For slow-moving inventory:



1\. Review historical consumption.

2\. Check upcoming shipment requirements.

3\. Check whether the item is reserved for future projects.

4\. Review open procurement orders.

5\. Avoid unnecessary additional procurement.

6\. Consider redistribution if appropriate.

7\. Monitor the item monthly.



\---



\## 10. Input Validation Rules



Before calculating stock coverage:



1\. Item name must not be blank.

2\. Current stock must be numeric.

3\. Average daily consumption must be numeric.

4\. Current stock cannot be negative.

5\. Average daily consumption cannot be negative.

6\. Average daily consumption cannot be zero when calculating coverage.

7\. Classification threshold must be greater than zero.



\---



\## 11. Test Cases



\### Test Case 1 — Normal Item



Input:



Current Stock = 80



Daily Consumption = 5



Expected:



80 / 5 = 16 days



Classification = Normal



Result: PASS



\---



\### Test Case 2 — Slow-Moving Item



Input:



Current Stock = 160



Daily Consumption = 4



Expected:



160 / 4 = 40 days



Classification = Slow Moving



Result: PASS



\---



\### Test Case 3 — Zero Consumption



Input:



Current Stock = 100



Daily Consumption = 0



Expected:



Invalid Input — Daily consumption cannot be zero.



Result: PASS



\---



\### Test Case 4 — Negative Stock



Input:



Current Stock = -10



Daily Consumption = 5



Expected:



Invalid Input — Current stock cannot be negative.



Result: PASS



\---



\## 12. Management Decision Logic



If:



Stock Coverage > 30 days



Then:



Slow Moving



If:



Stock Coverage <= 30 days



Then:



Normal



If:



Daily Consumption = 0



Then:



Invalid Input / Manual Review Required



\---



\## 13. KPI



\### Slow-Moving Inventory Rate



Slow-Moving Inventory Rate (%) =



Number of Slow-Moving Items / Total Inventory Items × 100



For the sample output:



Slow-Moving Items = 1



Total Items = 6



Slow-Moving Inventory Rate:



1 / 6 × 100 = 16.67%



Expected KPI:



Slow-Moving Inventory Rate = 16.67%



\---



\## 14. Management Summary



The sample analysis identifies one slow-moving item.



Item:



Backroom Camera



Coverage:



40 days



The sample slow-moving inventory rate is:



16.67%



Management should review the reason for the higher stock coverage

before making additional procurement decisions.



\---



\## 15. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company inventory.

\- 30 days is used only as a learning threshold.

\- Actual slow-moving definitions should be established by business

&#x20; requirements.

\- Consumption is assumed to be reasonably stable.

\- Inventory reserved for future requirements should not automatically

&#x20; be considered excess inventory.



\---



\## 16. Future Automation



This analysis can later be automated using:



\- Excel

\- Python

\- Power BI

\- SQL

\- Automated inventory dashboards

\- AI-based inventory analysis

\- Automated excess-stock alerts

