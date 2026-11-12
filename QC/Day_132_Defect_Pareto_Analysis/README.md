\# Day 132 - QC Defect Pareto Analysis



\## Objective

Build a Python-based defect Pareto analysis using sample QC data.

The analysis identifies the defect categories contributing most

to the total number of defects.



\## Sample Dataset



| Defect Category | Defect Count |

|---|---:|

| Camera No Video | 18 |

| Router/Network Issue | 12 |

| Power Failure | 8 |

| Intermittent Restart | 5 |

| DCUPS Backup Issue | 4 |

| Other Defects | 3 |

| \*\*Total\*\* | \*\*50\*\* |



\## Key Results



\- Total defects analysed: 50

\- Top three defect categories: 38

\- Contribution of top three categories: 76%

\- Highest defect category: Camera No Video



\## Files



\- `sample\_defects.csv` - Input defect dataset.

\- `defect\_pareto.py` - Python analysis program.

\- `test\_defect\_pareto.py` - Automated validation tests.

\- `pareto\_report.csv` - Generated Pareto analysis report.



\## How to Run



Run the analysis:



```bash

python defect\_pareto.py

