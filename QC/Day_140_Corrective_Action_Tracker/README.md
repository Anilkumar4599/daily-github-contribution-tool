

\# Day 140 – Corrective Action Tracker



\## Project Objective

Create a simple corrective-action tracker to monitor QC defects, identified root causes, corrective actions, responsible owners and closure status.



\## Project Files

\- `corrective\_action\_tracker.csv` – Sample corrective-action records.

\- `corrective\_action\_tracker.py` – Python validation and reporting program.

\- `README.md` – Project documentation.



\## Tracking Information

\- Action ID

\- Reported date

\- Defect ID and device name

\- Root cause

\- Corrective action

\- Responsible owner

\- Target date

\- Action status

\- Closure date



\## Validation Rules

1\. Required fields cannot be blank.

2\. Dates must use YYYY-MM-DD format.

3\. Status must be Open, In Progress or Closed.

4\. Closed actions must have a closure date.

5\. Open and In Progress actions must not have a closure date.



\## How to Run



```bash

python corrective\_action\_tracker.py

```



\## Expected Sample Summary



\- Total records: 3

\- Open: 1

\- In Progress: 1

\- Closed: 1



\## Business Application

The tracker helps QC and Service teams monitor corrective actions, assign ownership, follow up on pending activities and maintain closure records.



\## Practice Data

All sample records are fictional and intended for learning purposes.



