\# Inventory DAX Measures — Power BI



\## 1. Purpose



This document contains simple DAX measures that can be used

for inventory analysis in a future Power BI dashboard.



The objective is to understand basic DAX measures and their

business logic.



This is a hypothetical learning example.



\---



\## 2. Sample Inventory Data



| Item | Opening Stock | Stock In | Stock Out | Closing Stock |

|---|---:|---:|---:|---:|

| Lobby Camera | 50 | 30 | 20 | 60 |

| Router | 40 | 25 | 15 | 50 |

| Main Unit | 30 | 20 | 10 | 40 |

| DCUPS | 25 | 15 | 8 | 32 |

| Sensor Bag | 60 | 40 | 25 | 75 |



\---



\## 3. Measure 1 — Total Stock In



DAX:



```DAX

Total Stock In =

SUM(Inventory\[Stock In])

