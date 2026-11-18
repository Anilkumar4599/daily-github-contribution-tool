

\# Day 138 - QC Rework Tracking Table



\## Project Objective

Build a reusable rework tracking table to monitor defective ATM E-Surveillance devices, rework actions, assigned owners and reinspection results.



\## Project Files

\- `rework\_tracker.csv` - Sample QC rework tracking data.

\- `rework\_tracker.py` - Python validation and reporting program.

\- `test\_rework\_tracker.py` - Automated unit tests.



\## Tracking Information

The table captures:

\- Rework ID and reported date

\- Device and defect description

\- Defect severity

\- Rework action and assigned team

\- Target date

\- Rework status

\- Reinspection result

\- Completion date



\## Validation Rules

1\. Required fields cannot be blank.

2\. Dates must use YYYY-MM-DD format.

3\. Severity must be Critical, Major or Minor.

4\. Status must be Pending, In Progress or Completed.

5\. Reinspection result must be Pending, Pass or Fail.

6\. Completed rework must have a Pass result and completion date.



\## How to Run



Run the tracking report:



```bash

python rework\_tracker.py

```



Run automated tests:



```bash

python -m unittest -v test\_rework\_tracker.py

```



\## Business Application

This tracker helps the QC and Service teams monitor pending rework, identify overdue actions, track responsibility and confirm that defective devices pass reinspection before closure.



\## Practice Data Note

All sample records are fictional and intended for learning and validation practice.



