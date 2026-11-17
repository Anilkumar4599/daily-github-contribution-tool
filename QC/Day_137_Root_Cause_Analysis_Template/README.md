

\# Day 137 - Root Cause Analysis (RCA) Template



\## Project Objective

Create a reusable Root Cause Analysis template for tracking and investigating QC defects in ATM E-Surveillance devices.



\## Project Files

\- `rca\_template.md` - Reusable RCA documentation template.

\- `sample\_rca.csv` - Sample RCA data for validation.

\- `rca\_validator.py` - Python program to validate RCA records.

\- `test\_rca\_validator.py` - Automated unit tests.



\## Validation Checks

The Python validator checks:

1\. Required RCA fields are not empty.

2\. Reported date and target date use YYYY-MM-DD format.

3\. Severity must be Critical, Major or Minor.

4\. Status must be Open, In Progress or Closed.



\## How to Run



Run the validation program:



```bash

python rca\_validator.py

```



Run automated tests:



```bash

python -m unittest -v test\_rca\_validator.py

```



\## Test Results

\- Total automated tests: 7

\- Expected result: All 7 tests pass.



\## Business Application

This template helps the QC team document defect containment, identify potential root causes, assign corrective and preventive actions, and monitor closure.



\## Practice Data Note

The sample RCA record is fictional and intended for learning and validation practice. Its stated root cause is not a verified technical finding.



