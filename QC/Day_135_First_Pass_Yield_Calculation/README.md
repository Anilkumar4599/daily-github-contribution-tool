\# Day 135 – First-Pass Yield (FPY) Calculation



\## Objective

Build a simple Python example to calculate First-Pass Yield using sample ATM E-Surveillance QC inspection data.



\## What is FPY?

First-Pass Yield measures the percentage of inspected units that pass QC during their first inspection without requiring rework.



\## Formula



FPY = (Units Passed First Time / Total Units Inspected) × 100



\## Sample Data



| Date | Inspected | Passed First Time |

|---|---:|---:|

| 2026-11-10 | 20 | 17 |

| 2026-11-11 | 18 | 15 |

| 2026-11-12 | 22 | 19 |

| 2026-11-13 | 20 | 16 |

| 2026-11-14 | 20 | 18 |

| \*\*Total\*\* | \*\*100\*\* | \*\*85\*\* |



\## Expected Result



\- Total inspected: 100

\- Passed first time: 85

\- Failed first pass: 15

\- Overall FPY: 85%



\## Business Interpretation

The sample shows that 85 out of every 100 inspected units passed QC during the first inspection. The remaining 15 units failed their first inspection and may require rework or further investigation.



\## Important Rule

Units that pass after rework must not be counted as first-pass successes.



\## Files

\- `sample\_fpy\_data.csv` – Sample QC inspection data.

\- `fpy\_calculator.py` – FPY calculation program.

\- `test\_fpy\_calculator.py` – Automated tests.

\- `fpy\_report.csv` – Generated FPY report.



\## How to Run



```bash

python fpy\_calculator.py

python -m unittest -v test\_fpy\_calculator.py

```



\## Learning Outcome

Understand the FPY formula, calculate daily and overall yield, validate inputs, and generate a CSV report using Python.



