\# QC Minimum and Maximum Stock Calculator



\## 1. Purpose



This document provides a simple example for calculating minimum and

maximum inventory stock levels.



The objective is to help inventory management determine when stock

levels require replenishment and how much inventory should normally

be maintained.



This is a hypothetical learning example.



\---



\## 2. Basic Inventory Logic



Minimum Stock = Average Daily Consumption × Lead Time



Maximum Stock = Minimum Stock + Reorder Quantity



Where:



\- Average Daily Consumption = Average number of units consumed per day

\- Lead Time = Number of days required to receive replenishment

\- Reorder Quantity = Quantity normally ordered for replenishment



\---



\## 3. Sample Input Data



| Item | Average Daily Consumption | Lead Time (Days) | Reorder Quantity |

|---|---:|---:|---:|

| Main Unit | 5 | 7 | 50 |

| Lobby Camera | 8 | 7 | 60 |

| Backroom Camera | 4 | 10 | 40 |

| Router | 6 | 5 | 50 |

| DCUPS | 3 | 10 | 30 |



\---



\## 4. Calculation



\### Main Unit



Average Daily Consumption = 5



Lead Time = 7 days



Reorder Quantity = 50



Minimum Stock:



5 × 7 = 35



Maximum Stock:



35 + 50 = 85



\---



\### Lobby Camera



Average Daily Consumption = 8



Lead Time = 7 days



Reorder Quantity = 60



Minimum Stock:



8 × 7 = 56



Maximum Stock:



56 + 60 = 116



\---



\### Backroom Camera



Average Daily Consumption = 4



Lead Time = 10 days



Reorder Quantity = 40



Minimum Stock:



4 × 10 = 40



Maximum Stock:



40 + 40 = 80



\---



\### Router



Average Daily Consumption = 6



Lead Time = 5 days



Reorder Quantity = 50



Minimum Stock:



6 × 5 = 30



Maximum Stock:



30 + 50 = 80



\---



\### DCUPS



Average Daily Consumption = 3



Lead Time = 10 days



Reorder Quantity = 30



Minimum Stock:



3 × 10 = 30



Maximum Stock:



30 + 30 = 60



\---



\## 5. Expected Output



| Item | Daily Consumption | Lead Time | Reorder Qty | Minimum Stock | Maximum Stock |

|---|---:|---:|---:|---:|---:|

| Main Unit | 5 | 7 | 50 | 35 | 85 |

| Lobby Camera | 8 | 7 | 60 | 56 | 116 |

| Backroom Camera | 4 | 10 | 40 | 40 | 80 |

| Router | 6 | 5 | 50 | 30 | 80 |

| DCUPS | 3 | 10 | 30 | 30 | 60 |



\---



\## 6. Management Finding



Lobby Camera has the highest minimum stock requirement:



Minimum Stock = 56 units



Lobby Camera also has the highest maximum stock requirement:



Maximum Stock = 116 units



This indicates that Lobby Camera consumption is relatively high in

this sample dataset.



Inventory management should monitor high-consumption items closely.



\---



\## 7. Reorder Decision Logic



The following simple logic can be used:



If Current Stock <= Minimum Stock:



&#x20;   Replenishment Required



If Current Stock > Minimum Stock:



&#x20;   No Immediate Replenishment Required



If Current Stock >= Maximum Stock:



&#x20;   Avoid Additional Ordering Unless Business Demand Requires It



\---



\## 8. Example Reorder Decision



Example:



Item = Lobby Camera



Current Stock = 50



Minimum Stock = 56



Maximum Stock = 116



Since:



50 < 56



Expected Result:



Replenishment Required



\---



\## 9. Input Validation Rules



Before performing the calculation:



1\. Item name must not be blank.

2\. Average daily consumption must be numeric.

3\. Lead time must be numeric.

4\. Reorder quantity must be numeric.

5\. Consumption cannot be negative.

6\. Lead time cannot be negative.

7\. Reorder quantity cannot be negative.

8\. Maximum stock must be greater than or equal to minimum stock.



\---



\## 10. Test Cases



\### Test Case 1 — Normal Calculation



Input:



Average Daily Consumption = 5



Lead Time = 7



Reorder Quantity = 50



Expected:



Minimum Stock = 35



Maximum Stock = 85



Result: PASS



\---



\### Test Case 2 — Zero Consumption



Input:



Average Daily Consumption = 0



Lead Time = 7



Reorder Quantity = 50



Expected:



Minimum Stock = 0



Maximum Stock = 50



Result: PASS



\---



\### Test Case 3 — Replenishment Required



Input:



Current Stock = 50



Minimum Stock = 56



Expected:



Replenishment Required



Result: PASS



\---



\### Test Case 4 — Invalid Negative Consumption



Input:



Average Daily Consumption = -5



Lead Time = 7



Reorder Quantity = 50



Expected:



Invalid Input — Consumption cannot be negative.



Result: PASS



\---



\## 11. Management Interpretation



Minimum and maximum stock levels help inventory management:



\- Prevent stock shortages

\- Plan replenishment

\- Monitor fast-moving items

\- Reduce emergency procurement

\- Maintain adequate spare availability

\- Support shipment planning

\- Improve inventory control



The calculation should be reviewed periodically because consumption

patterns and supplier lead times can change.



\---



\## 12. Recommended KPI



\### Stock Availability Rate



Stock Availability Rate (%) =



Items Available When Required / Total Items Required × 100



A higher stock availability rate indicates better inventory readiness.



\---



\## 13. Important Management Note



Minimum and maximum stock levels should not be treated as permanent

values.



They should be reviewed using:



\- Historical consumption

\- Current shipment requirements

\- Supplier lead time

\- Emergency demand

\- Seasonal demand

\- Open customer requirements

\- Safety stock requirements



Actual inventory decisions should be based on validated business data.



\---



\## 14. Future Automation



This calculator can later be automated using:



\- Excel

\- Python

\- Power BI

\- SQL

\- Automated inventory dashboards

\- AI-based demand analysis

\- Automated reorder alerts



\---



\## 15. Assumptions



\- This is a hypothetical learning dataset.

\- The data does not represent actual company inventory.

\- Average daily consumption is assumed to be stable.

\- Lead time is assumed to remain constant.

\- Reorder quantity is predetermined for this example.

\- Actual minimum and maximum stock levels should be validated using

&#x20; historical inventory data and business requirements.

