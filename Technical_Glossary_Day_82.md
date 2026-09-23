\# Technical Glossary — Day 82



\## 1. Purpose



This glossary explains technical terms from my current learning areas:

Quality Control (QC), Procurement, Power BI, AWS, Git/GitHub, and DevOps.



The explanations are written in simple language for learning and revision.



\---



\## 2. Quality Control (QC)



| Term | Meaning |

|---|---|

| Quality Control (QC) | Activities used to check whether a product meets specified requirements. |

| Quality Assurance (QA) | Planned activities intended to provide confidence that quality requirements will be met. |

| Defect | A problem where a product or function does not meet its requirement. |

| Severity | How serious the effect of a defect is. |

| Priority | How urgently a defect should be addressed. |

| Root Cause Analysis (RCA) | A structured investigation to identify the underlying cause of a problem. |

| First Pass Yield (FPY) | The proportion of units that pass a process the first time without rework. |

| Show-stopper | A defect that prevents an important function or process from working. |

| Rework | Work performed to correct a product that did not meet requirements. |

| Pareto Analysis | A method of organizing categories to identify those contributing most to a measured result. |



\## 3. Procurement and Inventory



| Term | Meaning |

|---|---|

| Purchase Order (PO) | A formal document sent to a supplier requesting goods or services. |

| Lead Time | The time between starting a request or order and receiving the required item. |

| Supplier | A person or organization that provides goods or services. |

| Stock-out | A situation where an item is unavailable when it is needed. |

| Reorder Level | A stock quantity at which replenishment should be considered or triggered. |

| Safety Stock | Additional inventory held to help manage uncertainty in demand or supply. |

| Inventory Aging | An analysis of how long items have remained in inventory. |

| Consumption | The quantity of inventory used during a period. |

| Reconciliation | Comparing records with actual quantities or another trusted record to identify differences. |

| ODA | Often means “Out of Delivery Area” in shipping contexts; confirm the exact definition used by your courier. |



\## 4. Power BI and Data Analysis



| Term | Meaning |

|---|---|

| Power BI | A Microsoft platform used to connect to data, analyze it, and build reports and dashboards. |

| Dashboard | A visual summary of important information and performance indicators. |

| KPI | Key Performance Indicator: a measure used to monitor progress or performance. |

| Dataset | A collection of data used for analysis. |

| Data Cleaning | Finding and correcting or handling missing, inconsistent, or invalid data. |

| DAX | Data Analysis Expressions, a formula language used in Power BI and related Microsoft tools. |

| Measure | A calculation evaluated in the context of a report or visual. |

| Filter | A condition used to limit the data included in a view or calculation. |

| Data Model | The structure connecting tables and defining how data is analyzed. |

| FPY % | First Pass Yield expressed as a percentage. |



\## 5. AWS and Cloud Computing



| Term | Meaning |

|---|---|

| Cloud Computing | Using computing resources and services delivered over a network. |

| AWS | Amazon Web Services, a provider of cloud services. |

| EC2 | An AWS service that provides virtual computing instances. |

| S3 | An AWS object storage service. |

| RDS | An AWS service for managed relational databases. |

| IAM | AWS Identity and Access Management, used to manage access to AWS resources. |

| Least Privilege | Giving a user or service only the permissions needed for its tasks. |

| CloudWatch | An AWS monitoring and observability service. |

| SNS | An AWS messaging service that can distribute notifications. |

| Deployment | Making an application or system available in a target environment. |



\## 6. Git and GitHub



| Term | Meaning |

|---|---|

| Git | A version-control system used to track changes to files. |

| GitHub | An online platform for hosting Git repositories and collaborating on projects. |

| Repository | A location containing project files and their version history. |

| Commit | A recorded set of changes in Git. |

| Push | Sending local commits to a remote repository. |

| Pull | Fetching and integrating changes from a remote repository. |

| Branch | A separate line of development in a repository. |

| Merge | Combining changes from different branches. |

| Working Tree | The files and changes currently present in the local working directory. |

| README | A document explaining a project, its purpose, and how to use or understand it. |



\## 7. DevOps



| Term | Meaning |

|---|---|

| DevOps | Practices and collaboration that help development and operations teams deliver and maintain software. |

| SDLC | Software Development Life Cycle: the stages involved in developing and maintaining software. |

| Agile | An approach to work that emphasizes iterative delivery, feedback, and adaptation. |

| CI | Continuous Integration: frequently integrating code changes and checking them through automated processes. |

| CD | Continuous Delivery or Continuous Deployment, depending on the context; both involve automating software release activities. |

| Pipeline | A sequence of automated steps used to build, test, or deliver software. |

| Build | Producing a deployable software artifact from source materials. |

| Test Case | A defined set of conditions, inputs, and expected results used to verify behavior. |

| Monitoring | Observing a system to understand its status, performance, and events. |

| Rollback | Returning a deployment or system to an earlier known state. |



\---



\## 8. Input Validation Exercise



The following fictional examples can be used to practice validating glossary entries.



\### Required fields



Each glossary entry must contain:



\- Term

\- Meaning

\- Category



\### Validation rules



1\. Term must not be blank.

2\. Meaning must not be blank.

3\. Category must be one of:

&#x20;  - QC

&#x20;  - Procurement

&#x20;  - Power BI

&#x20;  - AWS

&#x20;  - Git/GitHub

&#x20;  - DevOps

4\. Duplicate terms should be flagged for review.

5\. Invalid entries should not be accepted as valid glossary records.



\### Sample input dataset



| Term | Meaning | Category |

|---|---|---|

| EC2 | AWS virtual computing instances | AWS |

| Defect | A problem that does not meet a requirement | QC |

| DAX | A formula language used in Power BI | Power BI |

|  | A version-control system | Git/GitHub |

| Pipeline |  | DevOps |

| S3 | AWS object storage service | Cloud |



\### Expected validation results



| Row | Result | Reason |

|---|---|---|

| 1 | Valid | All required fields are present and category is allowed. |

| 2 | Valid | All required fields are present and category is allowed. |

| 3 | Valid | All required fields are present and category is allowed. |

| 4 | Invalid | Term is blank. |

| 5 | Invalid | Meaning is blank. |

| 6 | Invalid | Category “Cloud” is not in the allowed category list. |



\### Validation pseudocode



```text

FOR each entry:



&#x20;   IF term is blank:

&#x20;       mark entry as invalid



&#x20;   ELSE IF meaning is blank:

&#x20;       mark entry as invalid



&#x20;   ELSE IF category is not in the allowed category list:

&#x20;       mark entry as invalid



&#x20;   ELSE IF term already exists:

&#x20;       flag duplicate for review



&#x20;   ELSE:

&#x20;       mark entry as valid

