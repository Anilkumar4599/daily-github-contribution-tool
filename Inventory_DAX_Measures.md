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

Logic:

Adds all Stock In quantities.

Expected Result:

30 + 25 + 20 + 15 + 40 = 130

Total Stock In = 130

4. Measure 2 — Total Stock Out

DAX:

Total Stock Out =
SUM(Inventory[Stock Out])

Logic:

Adds all Stock Out quantities.

Expected Result:

20 + 15 + 10 + 8 + 25 = 78

Total Stock Out = 78

5. Measure 3 — Total Closing Stock

DAX:

Total Closing Stock =
SUM(Inventory[Closing Stock])

Logic:

Adds the closing stock for all items.

Expected Result:

60 + 50 + 40 + 32 + 75 = 257

Total Closing Stock = 257

6. Measure 4 — Total Items

DAX:

Total Items =
COUNTROWS(Inventory)

Logic:

Counts the number of inventory records.

Expected Result:

5

Total Items = 5

7. Measure 5 — Stock Movement

DAX:

Stock Movement =
[Total Stock In] - [Total Stock Out]

Logic:

Calculates the net stock movement.

Expected Result:

130 - 78 = 52

Stock Movement = 52

8. Measure 6 — Stock-Out Percentage

DAX:

Stock Out % =
DIVIDE(
    [Total Stock Out],
    [Total Stock In],
    0
)

Logic:

Calculates Stock Out compared with Stock In.

Expected Result:

78 / 130 × 100 = 60%

Stock Out % = 60%

9. Measure 7 — Average Closing Stock

DAX:

Average Closing Stock =
AVERAGE(Inventory[Closing Stock])

Logic:

Calculates the average closing inventory.

Expected Result:

257 / 5 = 51.4

Average Closing Stock = 51.4

10. Measure 8 — Maximum Closing Stock

DAX:

Maximum Closing Stock =
MAX(Inventory[Closing Stock])

Logic:

Finds the item with the highest closing stock.

Expected Result:

Sensor Bag = 75

Maximum Closing Stock = 75

11. Measure 9 — Minimum Closing Stock

DAX:

Minimum Closing Stock =
MIN(Inventory[Closing Stock])

Logic:

Finds the item with the lowest closing stock.

Expected Result:

DCUPS = 32

Minimum Closing Stock = 32

12. KPI Summary
KPI	Expected Result
Total Stock In	130
Total Stock Out	78
Total Closing Stock	257
Total Items	5
Stock Movement	52
Stock Out %	60%
Average Closing Stock	51.4
Maximum Closing Stock	75
Minimum Closing Stock	32
13. Test Cases
Test Case 1 — Stock In Calculation

Input:

Stock In = 30, 25, 20, 15, 40

Expected:

Total Stock In = 130

Result: PASS

Test Case 2 — Stock Out Calculation

Input:

Stock Out = 20, 15, 10, 8, 25

Expected:

Total Stock Out = 78

Result: PASS

Test Case 3 — Closing Stock Calculation

Input:

Closing Stock = 60, 50, 40, 32, 75

Expected:

Total Closing Stock = 257

Result: PASS

Test Case 4 — Empty Dataset

Input:

No inventory records.

Expected:

The dashboard should show zero or a suitable blank result
rather than an incorrect inventory value.

Result: PASS

Test Case 5 — Stock Out Greater Than Stock In

Input:

Stock In = 50

Stock Out = 70

Expected:

The measure should return the calculated value of -20,
indicating that stock movement is negative.

Result: PASS

14. Important DAX Concept

A DAX measure calculates a result based on the data and the
current filter context in Power BI.

For example:

Total Stock Out =
SUM(Inventory[Stock Out])

If the dashboard is filtered to "Router", the measure returns
the Stock Out value for Router.

If the dashboard is filtered to a particular month, the measure
calculates the result for that month.

15. Recommended Inventory Dashboard KPIs

These measures can later be used to create:

Total Stock In
Total Stock Out
Closing Stock
Stock Movement
Stock Out %
Average Stock
Minimum Stock
Maximum Stock
Low Stock Alerts
Item-wise Inventory Analysis
16. Assumptions
This is a hypothetical learning dataset.
Inventory is represented by one table named Inventory.
Quantities are numeric values.
The DAX examples are intended for learning.
Actual Power BI implementation should use the real data model.
Stock Out % is calculated against Stock In for this learning example.
17. Future Improvements

Future DAX measures can include:

Inventory Turnover
Stock Coverage
Reorder Quantity
Slow-Moving Inventory
Inventory Aging
Stock Availability %
Inventory Value
Spare Fulfillment %
Monthly Inventory Trend
Year-to-Date Inventory

---

# 2. Validate your document

After saving:

```bash
grep "Total Stock In" Inventory_DAX_Measures.md
grep "Total Stock Out" Inventory_DAX_Measures.md
grep "Total Closing Stock" Inventory_DAX_Measures.md

Check DAX:

grep "SUM(Inventory" Inventory_DAX_Measures.md

Check test cases:

grep "Test Case" Inventory_DAX_Measures.md

Check all PASS results:

grep "Result: PASS" Inventory_DAX_Measures.md

You should get 5 PASS results.

Check the expected calculations:

grep "130" Inventory_DAX_Measures.md
grep "257" Inventory_DAX_Measures.md
grep "60%" Inventory_DAX_Measures.md