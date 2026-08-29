\# QC Slow-Moving Inventory Report — README



\## Project Overview



This project demonstrates a simple method for identifying slow-moving

inventory.



The analysis uses stock coverage days to compare current inventory

against average daily consumption.



\---



\## Business Purpose



The report can help inventory management:



\- Identify slow-moving items

\- Reduce excess inventory

\- Improve inventory utilization

\- Avoid unnecessary procurement

\- Support inventory redistribution

\- Improve working-capital management



\---



\## Calculation



Stock Coverage (Days) =



Current Stock / Average Daily Consumption



\---



\## Classification Rule



For this learning project:



| Coverage | Classification |

|---|---|

| > 30 days | Slow Moving |

| <= 30 days | Normal |



\---



\## Sample Result



Backroom Camera:



Current Stock = 160



Daily Consumption = 4



Coverage = 40 days



Classification = Slow Moving



\---



\## KPI



Slow-Moving Inventory Rate:



Slow-Moving Items / Total Inventory Items × 100



Sample:



1 / 6 × 100 = 16.67%



\---



\## Input Validation



The analysis validates:



\- Item name

\- Current stock

\- Daily consumption

\- Negative values

\- Zero consumption

\- Classification threshold



\---



\## Assumptions



This is a hypothetical learning project.



The 30-day threshold is only an example and should be replaced by an

approved business rule when actual inventory data is used.



\---



\## Future Improvements



The report can later be automated using:



\- Excel

\- Python

\- Power BI

\- SQL

\- AI-based inventory analysis

\- Automated alerts

