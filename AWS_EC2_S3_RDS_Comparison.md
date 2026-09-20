\# Day 79 – Difference Between AWS EC2, S3 and RDS



\## 1. Objective



Understand the differences between three commonly used AWS services:



\- Amazon EC2

\- Amazon S3

\- Amazon RDS



Explain their purposes using a simple ATM surveillance monitoring example.



This is a learning exercise. No AWS resources are created today.



\---



\## 2. Introduction



AWS provides different services for different technical requirements.



For example:



\- An application may need a computer to run on.

\- The application may need a place to store files.

\- The application may need a database to store structured information.



EC2, S3 and RDS address these different requirements.



\---



\## 3. What is Amazon EC2?



EC2 stands for Elastic Compute Cloud.



Amazon EC2 provides virtual servers in the AWS cloud.



A virtual server can run an application, process data, or perform computing tasks.



\### Example



An ATM surveillance monitoring application needs a server to run its application software.



An EC2 instance could provide that computing environment.



\### Simple explanation



EC2 = A computer/server in the cloud.



\### Typical uses



\- Hosting applications

\- Running services

\- Processing data

\- Running web servers

\- Performing computing tasks



\---



\## 4. What is Amazon S3?



S3 stands for Simple Storage Service.



Amazon S3 is an object storage service used to store and retrieve objects such as files and data.



\### Example



An ATM monitoring system generates daily reports and log files.



S3 could be used to store those files.



\### Simple explanation



S3 = A place in the cloud to store files and objects.



\### Typical uses



\- Storing reports

\- Storing log files

\- Storing images and documents

\- Storing backups

\- Hosting static website content



\---



\## 5. What is Amazon RDS?



RDS stands for Relational Database Service.



Amazon RDS helps users set up, operate, and manage relational databases in AWS.



It supports database engines such as MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server, and Amazon Aurora.



\### Example



An ATM monitoring application needs to store structured information such as:



\- ATM ID

\- Device location

\- Last communication time

\- Device status

\- Incident reference



A relational database hosted through RDS could store this information.



\### Simple explanation



RDS = A managed relational database service in the cloud.



\### Typical uses



\- Storing structured application data

\- Managing relational databases

\- Supporting applications that use SQL

\- Storing business records and transactions



\---



\## 6. EC2 vs S3 vs RDS



| Feature | Amazon EC2 | Amazon S3 | Amazon RDS |

|---|---|---|---|

| Main purpose | Cloud computing/server | Object storage | Managed relational database |

| What it provides | Virtual machine instances | Storage for objects/files | Managed relational database |

| Example | Run a monitoring application | Store reports and logs | Store structured ATM records |

| Typical data/workload | Application processing | Files, images, logs, backups | Structured data in relational tables |

| User responsibility | Manage guest OS and application; AWS manages underlying infrastructure | Manage objects, access, and storage configuration | Manage database usage, data, and configuration; AWS handles many database administration tasks |

| Common use | Application hosting | File and object storage | Application database |



\---



\## 7. ATM Surveillance Example



Imagine a monitoring application that receives information from ATM surveillance devices.



The system needs:



1\. A server to run the monitoring application.

2\. Storage for reports and log files.

3\. A database for structured device information.



A possible design is:



```text

ATM Surveillance Devices

&#x20;         |

&#x20;         v

Monitoring Application

&#x20;         |

&#x20;         v

&#x20;      Amazon EC2

&#x20;         |

&#x20;         +------------------+

&#x20;         |                  |

&#x20;         v                  v

&#x20;     Amazon S3           Amazon RDS

&#x20;  Reports and Logs    Structured Device Data

```



This is a conceptual example. A real architecture may use additional services and security controls.



\---



\## 8. Example Input



Business requirement:



```text

Project:

ATM Surveillance Monitoring



Requirements:



1\. Run a monitoring application.

2\. Store daily monitoring reports.

3\. Store structured ATM device records.

```



\---



\## 9. Expected Output



```text

Requirement 1:

Run the monitoring application.



Suggested AWS service:

Amazon EC2



Reason:

EC2 provides virtual computing instances on which the application can run.

```



```text

Requirement 2:

Store daily monitoring reports.



Suggested AWS service:

Amazon S3



Reason:

S3 provides object storage for reports and other files.

```



```text

Requirement 3:

Store structured ATM device records.



Suggested AWS service:

Amazon RDS



Reason:

RDS provides a managed relational database for structured application data.

```



\---



\## 10. Service Selection Exercise



Select the service that best matches each requirement.



| No. | Requirement | Expected Service |

|---|---|---|

| 1 | Run a web application | EC2 |

| 2 | Store PDF reports | S3 |

| 3 | Store structured records in relational tables | RDS |

| 4 | Store image files | S3 |

| 5 | Run a background processing application | EC2 |

| 6 | Store relational application data | RDS |



\---



\## 11. Validation Test Cases



\### Test Case 1 – Application Hosting



Input:



```text

Requirement:

Run an application on a virtual server.

```



Expected:



```text

Service:

Amazon EC2

```



Result:



```text

PASS – Correct service identified.

```



\### Test Case 2 – File Storage



Input:



```text

Requirement:

Store daily PDF monitoring reports.

```



Expected:



```text

Service:

Amazon S3

```



Result:



```text

PASS – Correct service identified.

```



\### Test Case 3 – Relational Database



Input:



```text

Requirement:

Store structured ATM records in relational tables.

```



Expected:



```text

Service:

Amazon RDS

```



Result:



```text

PASS – Correct service identified.

```



\### Test Case 4 – Image Storage



Input:



```text

Requirement:

Store exported surveillance image files as objects.

```



Expected:



```text

Service:

Amazon S3

```



Result:



```text

PASS – Correct service identified.

```



\### Test Case 5 – Application Data



Input:



```text

Requirement:

Use a relational database for application records.

```



Expected:



```text

Service:

Amazon RDS

```



Result:



```text

PASS – Correct service identified.

```



\---



\## 12. Important Security and Cost Considerations



\### Security



\- Configure access permissions carefully.

\- Apply least-privilege IAM permissions.

\- Protect application credentials and database passwords.

\- Restrict network access to only what is required.

\- Review storage and database access settings.



\### Cost



AWS services may incur charges depending on configuration and usage.



Before creating resources:



\- Review the selected service and pricing.

\- Choose an appropriate region and configuration.

\- Set budgets or cost alerts where suitable.

\- Remove resources that are no longer required.

\- Verify cleanup after practical exercises.



This documentation exercise does not create resources or incur AWS resource charges.



\---



\## 13. Key Learning



Remember the simple distinction:



```text

EC2 = Compute

S3  = Object Storage

RDS = Relational Database

```



Example:



```text

Run the application       → EC2

Store reports and logs    → S3

Store structured records  → RDS

```



\---



\## 14. Assumptions and Limitations



1\. The ATM surveillance example is fictional.

2\. No real customer or production data is used.

3\. No AWS resources are created in this exercise.

4\. EC2, S3, and RDS are selected as illustrative services.

5\. A production solution may require other AWS services.

6\. The final architecture should be reviewed for security, availability, performance, and cost.

7\. Service selection depends on the actual application requirements.



\---



\## 15. Day 79 Summary



Task:

\#79 – Document the difference between EC2, S3 and RDS.



Domain:

AWS



Deliverable:

AWS\_EC2\_S3\_RDS\_Comparison.md



Included:



\- EC2 explanation

\- S3 explanation

\- RDS explanation

\- Comparison table

\- ATM surveillance example

\- Example input and expected output

\- Five validation test cases

\- Security and cost considerations

\- Assumptions and limitations



Status:

Complete after review and GitHub commit.

