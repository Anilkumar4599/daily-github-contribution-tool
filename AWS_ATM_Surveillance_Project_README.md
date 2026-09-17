\# Day 76 – AWS ATM Surveillance Monitoring Project



\## 1. Project Overview



This project demonstrates a simple AWS-based monitoring concept for ATM surveillance systems.



The objective is to monitor basic ATM device health information and identify devices that require attention.



This is a learning project and uses a small sample dataset.



No real customer or production data is used.



\---



\## 2. Business Problem



ATM surveillance systems may have issues such as:



\- Camera offline

\- Network connectivity failure

\- Storage/NVR issue

\- Power failure

\- Device unavailable

\- High CPU usage

\- High memory usage



A monitoring solution should help the support team identify problems quickly.



\---



\## 3. Project Objective



The objective is to design a simple AWS monitoring solution that can:



1\. Receive monitoring information.

2\. Store monitoring information.

3\. Monitor system health.

4\. Identify abnormal conditions.

5\. Generate an alert for important failures.

6\. Help the support team take corrective action.



\---



\## 4. Simple Architecture



```text

ATM / Surveillance Device

&#x20;         |

&#x20;         v

&#x20;   Monitoring Data

&#x20;         |

&#x20;         v

&#x20;      AWS

&#x20;         |

&#x20;   +-----+------+

&#x20;   |            |

&#x20;   v            v

&#x20;Storage      Monitoring

&#x20;   |            |

&#x20;   |            v

&#x20;   |          Alert

&#x20;   |            |

&#x20;   +-------> Support Team



5\. Possible AWS Services



For this learning project, the following AWS services are considered:



AWS Service	Purpose

Amazon EC2	Host a monitoring application

Amazon S3	Store monitoring reports/log files

Amazon CloudWatch	Monitor application/system metrics

Amazon SNS	Send notifications

IAM	Control access and permissions



These services are part of the project design.



Actual AWS resource creation will be performed separately during a controlled practical lab.



6\. Sample Dataset



The following small dataset represents monitoring information from ATM surveillance devices.



ATM ID	Location	Camera Status	Network Status	Storage Status	CPU %	Overall Status

ATM001	Chennai-01	Online	Online	Normal	35	Healthy

ATM002	Chennai-02	Offline	Online	Normal	42	Attention

ATM003	Chennai-03	Online	Offline	Normal	38	Critical

ATM004	Chennai-04	Online	Online	Normal	55	Healthy

ATM005	Chennai-05	Online	Online	Warning	72	Attention

7\. Sample Dataset Interpretation

ATM001

Camera  : Online

Network : Online

Storage : Normal

CPU     : 35%

Status  : Healthy



Expected action:



No immediate action required.

ATM002

Camera  : Offline

Network : Online

Storage : Normal

CPU     : 42%

Status  : Attention



Expected action:



Check camera connectivity and camera hardware.

ATM003

Camera  : Online

Network : Offline

Storage : Normal

CPU     : 38%

Status  : Critical



Expected action:



Check network connectivity immediately.

ATM004

Camera  : Online

Network : Online

Storage : Normal

CPU     : 55%

Status  : Healthy



Expected action:



No immediate action required.

ATM005

Camera  : Online

Network : Online

Storage : Warning

CPU     : 72%

Status  : Attention



Expected action:



Check storage condition and CPU utilization.

8\. Monitoring Logic



Simple monitoring rules are defined for learning purposes.



Condition	Status	Action

Camera Online + Network Online + Storage Normal	Healthy	No immediate action

Camera Offline	Attention	Investigate camera

Network Offline	Critical	Investigate network immediately

Storage Warning	Attention	Check storage

CPU above 80%	Attention	Investigate high CPU

Multiple failures	Critical	Immediate investigation



These thresholds are sample values for this learning project and are not production recommendations.



9\. Example Alert



Example:



ATM ID       : ATM003

Location     : Chennai-03

Problem      : Network Offline

Severity     : Critical



Required Action:

Check ATM network connectivity immediately.

10\. Example Project Flow

1\. ATM generates monitoring information

&#x20;             ↓

2\. Monitoring application collects data

&#x20;             ↓

3\. Data is stored

&#x20;             ↓

4\. AWS monitoring service evaluates metrics

&#x20;             ↓

5\. Abnormal condition detected

&#x20;             ↓

6\. Alert generated

&#x20;             ↓

7\. Support team investigates

&#x20;             ↓

8\. Issue resolved

11\. IAM Principle



The monitoring application should not receive unnecessary AWS permissions.



For example:



Monitoring Application

&#x20;       ↓

&#x20;    IAM Role

&#x20;       ↓

Required permissions only



The application should not automatically receive administrator access.



This follows the least-privilege principle learned in Day 75.



12\. Assumptions



The project uses the following assumptions:



The sample dataset is fictional.

No production ATM data is used.

No customer-sensitive information is included.

Monitoring data is assumed to be generated periodically.

CPU threshold of 80% is used only as a sample learning threshold.

Network Offline is treated as a critical condition for this example.

Camera Offline is treated as an attention condition.

Storage Warning requires investigation.

AWS resources will not be created during this documentation exercise.

Actual production thresholds must be defined based on business and technical requirements.

13\. Validation Test Cases

Test Case 1 – Healthy ATM



Input:



Camera   : Online

Network  : Online

Storage  : Normal

CPU      : 35%



Expected:



Status: Healthy



Result:



PASS

Test Case 2 – Camera Offline



Input:



Camera   : Offline

Network  : Online

Storage  : Normal

CPU      : 42%



Expected:



Status: Attention

Action: Investigate camera



Result:



PASS

Test Case 3 – Network Offline



Input:



Camera   : Online

Network  : Offline

Storage  : Normal

CPU      : 38%



Expected:



Status: Critical

Action: Investigate network immediately



Result:



PASS

Test Case 4 – Storage Warning



Input:



Camera   : Online

Network  : Online

Storage  : Warning

CPU      : 72%



Expected:



Status: Attention

Action: Check storage and CPU



Result:



PASS

Test Case 5 – High CPU



Input:



Camera   : Online

Network  : Online

Storage  : Normal

CPU      : 85%



Expected:



Status: Attention

Action: Investigate high CPU utilization



Result:



PASS

14\. Expected Project Outcome



The proposed solution should provide:



Centralized monitoring

Basic health visibility

Failure identification

Alert generation

Controlled AWS access

Support-team visibility

A foundation for future automation

15\. Future Practical Implementation



This README is the design stage.



Future practical sessions can implement the project step by step:



Phase 1

AWS account and IAM basics

&#x20;       ↓

Phase 2

Create controlled EC2 environment

&#x20;       ↓

Phase 3

Install simple monitoring application

&#x20;       ↓

Phase 4

Configure CloudWatch monitoring

&#x20;       ↓

Phase 5

Configure alerting

&#x20;       ↓

Phase 6

Test failure scenarios

&#x20;       ↓

Phase 7

Clean up AWS resources

&#x20;       ↓

Phase 8

Document results in GitHub



All practical exercises should be performed with cost and resource cleanup considerations.



16\. Key Learning



The important AWS concepts demonstrated in this project are:



IAM

&#x20;↓

EC2

&#x20;↓

Monitoring

&#x20;↓

CloudWatch

&#x20;↓

Alerts

&#x20;↓

Support Action



The project demonstrates how a business requirement can be converted into a simple AWS solution.



17\. Day 76 Summary



Task:



\#76 – Create a simple AWS project README



Domain:



AWS



Project:



ATM Surveillance Monitoring



Dataset:



5 sample ATM records



Main learning:



Business Requirement

&#x20;       ↓

AWS Architecture

&#x20;       ↓

Sample Data

&#x20;       ↓

Monitoring Logic

&#x20;       ↓

Expected Result



Status:



Completed after review and GitHub commit.



\---



\# Step 2 — Save the file



In Notepad:



\*\*Ctrl + S\*\*



Then close Notepad.



\---



\# Step 3 — Validate the file



Run:



```bash

ls -l AWS\_ATM\_Surveillance\_Project\_README.md

