\# Day 126 – Python .gitignore



\## Objective

Create and test a Python-specific `.gitignore` file.



\## Project Files

\- `.gitignore` – Ignore rules for Python projects.

\- `README.md` – Project explanation and assumptions.

\- `sample\_project/main.py` – Small Python sample.

\- `sample\_project/.env.example` – Safe example configuration.



\## Sample Dataset



The Python program uses the following sample values:



| Item | Value |

|---|---:|

| Item 1 | 100 |

| Item 2 | 200 |

| Item 3 | 300 |

| Total | 600 |



\## Test Cases



1\. Ignore `.env`.

2\. Ignore Python `.pyc` cache files.

3\. Ignore application log files.

4\. Allow `.env.example`.

5\. Ignore temporary `.tmp` files.

6\. Run the Python sample and verify total = 600.



\## Assumptions



\- The project uses Python.

\- Local virtual environments should not be uploaded.

\- Python cache and temporary files are unnecessary in Git.

\- Environment files may contain confidential information.

\- `.env.example` is safe to share only when it contains placeholders and no real secrets.

\- This `.gitignore` is a starter template and may need adjustments for individual projects.



\## Learning Outcome



Understand how `.gitignore` protects a repository from unnecessary temporary files and accidental inclusion of local configuration files.



\*\*Day 126:\*\* Python Git Ignore Practice.

