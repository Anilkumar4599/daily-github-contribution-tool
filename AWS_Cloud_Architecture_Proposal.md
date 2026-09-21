\# Day 80 – AWS Cloud Architecture Proposal



\## 1. Project Overview



Project Name:

ATM Surveillance Monitoring System



Domain:

AWS Cloud Architecture



Purpose:



Propose a simple cloud architecture for collecting and monitoring ATM surveillance device health information.



The proposed solution should help a support team identify device issues and review monitoring information from a centralized location.



This is a learning proposal. It is not a production-ready architecture.



\---



\## 2. Business Problem



ATM surveillance devices may experience problems such as:



\- Camera offline

\- Network connectivity failure

\- Storage warning

\- High CPU utilization

\- Application unavailable



When monitoring information is not centrally available, support teams may need to investigate devices individually.



A centralized monitoring solution can help organize monitoring information and identify conditions that require attention.



\---



\## 3. Project Objectives



The proposed solution should:



1\. Collect sample monitoring information.

2\. Process monitoring information through an application.

3\. Store monitoring reports and logs.

4\. Store structured device information.

5\. Monitor application health.

6\. Generate alerts for selected failures.

7\. Restrict access using appropriate permissions.

8\. Support investigation by the support team.



\---



\## 4. Proposed AWS Services



| AWS Service | Proposed Purpose | Reason |

|---|---|---|

| Amazon EC2 | Host a simple monitoring application | Provides virtual computing capacity |

| Amazon S3 | Store monitoring reports and log files | Provides object storage |

| Amazon RDS | Store structured device records | Provides a managed relational database |

| Amazon CloudWatch | Collect and monitor application or infrastructure metrics and logs | Supports monitoring and alerting |

| Amazon SNS | Deliver notifications | Can send notifications to configured subscribers |

| AWS IAM | Manage identities and permissions | Helps restrict access to required resources |



These services are proposed for learning purposes. A production design may use different services depending on requirements.



\---



\## 5. Simple Architecture Diagram



```text

ATM Surveillance Devices

&#x20;         |

&#x20;         v

Monitoring Information

&#x20;         |

&#x20;         v

Monitoring Application

&#x20;      (Amazon EC2)

&#x20;         |

&#x20;    +----+-----+

&#x20;    |          |

&#x20;    v          v

&#x20;Amazon S3   Amazon RDS

Reports/Logs  Device Records



Amazon EC2 / Application

&#x20;         |

&#x20;         v

&#x20;   Amazon CloudWatch

&#x20;         |

&#x20;         v

&#x20;     Amazon SNS

&#x20;         |

&#x20;         v

&#x20;   Support Team



AWS IAM controls access to the relevant resources.

```



\---



\## 6. Architecture Logic



\### Step 1 – Collect Monitoring Information



ATM devices or an approved data collection process provide monitoring information.



Example fields:



\- ATM ID

\- Device location

\- Camera status

\- Network status

\- Storage status

\- CPU utilization

\- Event timestamp



For this learning proposal, the data is fictional.



\### Step 2 – Process the Information



A monitoring application hosted on Amazon EC2 processes the incoming information.



The application can evaluate the reported device status against defined monitoring rules.



\### Step 3 – Store Reports and Logs



Amazon S3 can store generated reports and log files as objects.



Example:



```text

Daily\_ATM\_Monitoring\_Report.csv

Application\_Log.txt

```



\### Step 4 – Store Structured Records



Amazon RDS can store structured information such as:



\- ATM ID

\- Location

\- Current status

\- Last communication time

\- Incident reference



The database design and access permissions must be defined before implementation.



\### Step 5 – Monitor Application Health



Amazon CloudWatch can be used to monitor supported metrics and collect configured logs.



Monitoring rules and alarms should be selected according to the application's requirements.



\### Step 6 – Send Notifications



Amazon SNS can deliver notifications when configured monitoring alarms publish messages to a topic.



The notification channel and subscribers must be configured and tested.



\### Step 7 – Support-Team Investigation



The support team reviews alerts and monitoring information, investigates the reported condition, and records the corrective action.



\---



\## 7. Sample Dataset



The following fictional dataset illustrates the type of information the system may process.



| ATM ID | Camera Status | Network Status | Storage Status | CPU % | Overall Status |

|---|---|---|---|---:|---|

| ATM001 | Online | Online | Normal | 35 | Healthy |

| ATM002 | Offline | Online | Normal | 42 | Attention |

| ATM003 | Online | Offline | Normal | 38 | Critical |

| ATM004 | Online | Online | Normal | 55 | Healthy |

| ATM005 | Online | Online | Warning | 72 | Attention |



This sample dataset is not connected to an actual AWS environment.



\---



\## 8. Example Monitoring Rules



| Condition | Example Status | Example Action |

|---|---|---|

| Camera, network, and storage are normal | Healthy | Continue monitoring |

| Camera is offline | Attention | Investigate camera connectivity |

| Network is offline | Critical | Investigate network connectivity |

| Storage reports a warning | Attention | Check storage condition |

| CPU utilization exceeds the configured example threshold | Attention | Investigate resource utilization |



These are illustrative application-level rules, not AWS default alarm settings or approved production thresholds.



\---



\## 9. Security Considerations



1\. Use IAM roles and policies to grant only required permissions.

2\. Avoid unnecessary administrator access.

3\. Restrict network access to approved sources and destinations.

4\. Protect credentials and secrets.

5\. Review S3 and database access settings.

6\. Enable appropriate logging and monitoring.

7\. Review permissions periodically.

8\. Do not place credentials or sensitive production data in GitHub.



Security configuration must be reviewed before a real deployment.



\---



\## 10. Availability and Recovery Considerations



Before production use, the design should address:



\- Application availability requirements

\- Database backup and recovery

\- Report and log retention

\- Monitoring and alert delivery

\- Recovery time objectives

\- Recovery point objectives

\- Failure handling and escalation



These requirements have not yet been finalized for this learning proposal.



\---



\## 11. Cost Considerations



AWS charges depend on the services, region, resource configuration, and usage.



Before implementation:



1\. Estimate the expected resource usage.

2\. Review the pricing for each proposed service.

3\. Select suitable test-environment configurations.

4\. Consider budgets and cost alerts.

5\. Avoid leaving unnecessary resources running.

6\. Follow a cleanup checklist after practical exercises.

7\. Verify that resources have been removed or stopped as intended.



No AWS resources are created as part of this documentation exercise.



\---



\## 12. Example Input and Expected Output



\### Input



```text

ATM ID: ATM003



Camera Status: Online

Network Status: Offline

Storage Status: Normal

CPU: 38%

```



\### Expected Output



```text

ATM ID: ATM003



Detected Condition:

Network Offline



Example Severity:

Critical



Suggested Investigation:

Check the ATM network connection and related connectivity components.



Notification:

A notification may be generated if the corresponding monitoring rule

and alert integration have been configured.

```



This is an illustrative expected result, not the output of a running AWS system.



\---



\## 13. Validation Test Cases



\### Test Case 1 – Healthy Device



Input:



```text

Camera: Online

Network: Online

Storage: Normal

```



Expected:



```text

Overall status: Healthy

```



\### Test Case 2 – Network Failure



Input:



```text

Camera: Online

Network: Offline

Storage: Normal

```



Expected:



```text

Overall status: Critical

Network investigation required.

```



\### Test Case 3 – Storage Warning



Input:



```text

Camera: Online

Network: Online

Storage: Warning

```



Expected:



```text

Overall status: Attention

Storage investigation required.

```



\### Test Case 4 – Report Storage



Input:



```text

A monitoring report is generated.

```



Expected:



```text

The design identifies Amazon S3 as the proposed object-storage service.

```



\### Test Case 5 – Alert Delivery



Input:



```text

A configured monitoring alarm publishes a notification.

```



Expected:



```text

Amazon SNS can deliver the notification to configured subscribers.

```



These are design-level test cases. They have not been executed against deployed AWS resources.



\---



\## 14. Assumptions and Limitations



1\. The ATM surveillance scenario is fictional.

2\. The sample dataset contains no production or customer-sensitive information.

3\. The architecture is conceptual and intended for learning.

4\. No AWS resources are created in this exercise.

5\. The design assumes a monitoring application can collect or receive device information.

6\. Actual connectivity from ATM devices to AWS has not been designed.

7\. Authentication, network connectivity, and data-ingestion methods require further design.

8\. Production monitoring thresholds must be agreed with the responsible technical and business teams.

9\. Security, availability, backup, disaster recovery, and cost requirements require further review.

10\. The proposed services may change after detailed requirements are collected.



\---



\## 15. Future Practical Implementation Plan



The proposal can be developed through controlled practical sessions.



\### Phase 1 – AWS Fundamentals



\- Review IAM concepts.

\- Understand the AWS account and region.

\- Review cost and security precautions.



\### Phase 2 – Compute



\- Learn how an EC2 instance is configured.

\- Review secure access and instance lifecycle.

\- Perform a controlled test only after cost checks.



\### Phase 3 – Storage



\- Learn S3 buckets and objects.

\- Review access permissions.

\- Test with non-sensitive sample files.



\### Phase 4 – Database



\- Understand relational database requirements.

\- Review RDS configuration and cost.

\- Use a controlled test environment if appropriate.



\### Phase 5 – Monitoring and Alerts



\- Learn CloudWatch metrics and alarms.

\- Understand SNS topics and subscriptions.

\- Test alert behavior in a controlled environment.



\### Phase 6 – Validation and Cleanup



\- Execute approved test cases.

\- Record results and evidence.

\- Remove test resources as appropriate.

\- Verify cleanup and review any applicable charges.



\---



\## 16. Key Learning



The proposed architecture separates different responsibilities:



```text

EC2        = Run the application

S3         = Store reports and files

RDS        = Store structured relational data

CloudWatch = Monitor supported metrics and logs

SNS        = Deliver notifications

IAM        = Control access

```



The purpose of the architecture is to connect business requirements with suitable cloud services while considering security, availability, monitoring, and cost.



\---



\## 17. Day 80 Summary



Task:

\#80 – Create a simple cloud architecture proposal.



Domain:

AWS



Deliverable:

AWS\_Cloud\_Architecture\_Proposal.md



Included:



\- Business problem and objectives

\- Proposed AWS services

\- Simple architecture diagram

\- Architecture logic

\- Sample dataset

\- Monitoring rules

\- Security and cost considerations

\- Example input and expected output

\- Five design-level test cases

\- Assumptions and limitations

\- Future practical implementation plan



Status:

Complete after review and GitHub commit.

