

\# Day 133 - Device-Wise Defect Rate Calculator



\## Objective



Build a Python-based QC calculator to measure the defect

rate of different ATM E-Surveillance device categories.



\## Formula



Defect Rate (%) = (Defective Units / Units Inspected) \* 100



Good Units = Units Inspected - Defective Units



\## Sample Dataset



| Device | Inspected | Defective |

|---|---:|---:|

| ATM Main Unit | 100 | 8 |

| Lobby Camera | 150 | 12 |

| Outdoor Camera | 80 | 10 |

| DCUPS | 60 | 3 |



\## Sample Results



\- Total devices analysed: 4

\- Total units inspected: 390

\- Total defective units: 33

\- Total good units: 357

\- Overall defect rate: 8.46%

\- Highest defect rate: Outdoor Camera (12.50%)



\## Project Files



\- sample\_device\_data.csv - Sample QC input data

\- device\_defect\_rate.py - Main calculator

\- test\_device\_defect\_rate.py - Automated test cases

\- device\_defect\_rate\_report.csv - Generated report



\## How to Run



Run the calculator:



python device\_defect\_rate.py



Run automated tests:



python -m unittest -v



\## Input Validation



The program checks:



\- Blank device names

\- Duplicate device names

\- Missing or invalid quantities

\- Zero or negative inspection quantities

\- Negative defective quantities

\- Defective units exceeding inspected units



\## Business Application



Device-wise defect rates help the QC team identify

which device categories need closer inspection and

Root Cause Analysis (RCA).



The sample dataset is illustrative and is not actual

company production data.



