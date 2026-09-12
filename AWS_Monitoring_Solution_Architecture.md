\# Day 71 - AWS Monitoring Solution Architecture



\## 1. Objective



The objective is to document a simple AWS monitoring solution for monitoring an application running in AWS.



The solution should help the support team identify:



\- Server performance problems

\- Application availability issues

\- High CPU usage

\- High memory usage

\- High disk usage

\- Network problems

\- Application errors



The solution should generate an alert when an important threshold is exceeded.



\---



\## 2. Business Scenario



Assume an application is running on an AWS EC2 instance.



The application is used by customers and must be available continuously.



The support team wants to monitor the EC2 instance and receive an alert when the server has a problem.



Example:



If CPU utilization goes above 80% for a sustained period, the monitoring system should generate an alert.



\---



\## 3. Simple AWS Monitoring Architecture



The proposed architecture is:



AWS EC2

&#x20;  |

&#x20;  v

Amazon CloudWatch

&#x20;  |

&#x20;  +---- Metrics

&#x20;  |

&#x20;  +---- Logs

&#x20;  |

&#x20;  +---- Alarms

&#x20;  |

&#x20;  v

Amazon SNS

&#x20;  |

&#x20;  v

Email / Support Team



\---



\## 4. Main AWS Components



\### 4.1 Amazon EC2



Amazon EC2 is used as the example compute resource.



The application is assumed to be running on an EC2 instance.



Example:



EC2 Instance:

\- Name: ATM-App-Server-01

\- Environment: Production

\- Application: ATM Surveillance Application



\---



\### 4.2 Amazon CloudWatch



Amazon CloudWatch is the main monitoring service in this solution.



It can be used to monitor:



\- CPU utilization

\- Network traffic

\- Instance status

\- Application logs

\- Custom application metrics



CloudWatch stores and displays monitoring information.



\---



\### 4.3 CloudWatch Alarm



CloudWatch Alarm checks whether a metric crosses a defined threshold.



Example:



CPU Utilization > 80%



If the condition continues for the configured evaluation period, the alarm changes to an alert state.



\---



\### 4.4 Amazon SNS



Amazon SNS can be used to send notifications.



Example:



CloudWatch Alarm

&#x20;      |

&#x20;      v

Amazon SNS

&#x20;      |

&#x20;      v

Email Notification

&#x20;      |

&#x20;      v

Support Team



\---



\## 5. Sample Monitoring Dataset



The following is a small sample dataset for testing the monitoring logic.



| Time | Server | CPU % | Memory % | Disk % | Network Mbps | Errors | Status |

|---|---|---:|---:|---:|---:|---:|---|

| 10:00 | ATM-App-01 | 45 | 52 | 61 | 20 | 0 | Healthy |

| 10:05 | ATM-App-01 | 55 | 58 | 62 | 24 | 1 | Healthy |

| 10:10 | ATM-App-01 | 72 | 64 | 65 | 30 | 2 | Healthy |

| 10:15 | ATM-App-01 | 85 | 70 | 67 | 35 | 4 | Warning |

| 10:20 | ATM-App-01 | 91 | 78 | 68 | 42 | 10 | Critical |

| 10:25 | ATM-App-01 | 88 | 80 | 70 | 40 | 8 | Critical |

| 10:30 | ATM-App-01 | 65 | 65 | 71 | 28 | 2 | Healthy |



\---



\## 6. Monitoring Thresholds



For this example, the following thresholds are assumed.



| Metric | Threshold | Action |

|---|---:|---|

| CPU Utilization | > 80% | Generate warning/alert |

| Memory Utilization | > 80% | Generate warning/alert |

| Disk Utilization | > 85% | Generate warning/alert |

| Application Errors | > 5 | Generate alert |

| Server Availability | Unavailable | Generate critical alert |



These thresholds are example assumptions and should be finalized based on the application's actual performance requirements.



\---



\## 7. Example Alert Logic



\### CPU Alert



Condition:



CPU > 80%



Example:



At 10:15:



CPU = 85%



Expected result:



CPU alarm should be triggered if the configured evaluation conditions are satisfied.



\---



\### Critical CPU Alert



At 10:20:



CPU = 91%



Expected result:



The monitoring system should identify high CPU utilization and generate an alert.



\---



\### Error Alert



At 10:20:



Application Errors = 10



Threshold:



Errors > 5



Expected result:



An application error alert should be generated.



\---



\## 8. Example End-to-End Flow



The monitoring process is:



1\. Application runs on EC2.

2\. EC2 produces monitoring metrics.

3\. CloudWatch collects and monitors the metrics.

4\. CloudWatch compares metrics against thresholds.

5\. CloudWatch Alarm identifies abnormal conditions.

6\. Alarm sends notification through SNS.

7\. SNS sends notification to the support team.

8\. Support team investigates the problem.

9\. Support team takes corrective action.

10\. Monitoring continues.



\---



\## 9. Example Alert



\### Alert Details



Alert ID:



AWS-ALERT-001



Server:



ATM-App-01



Metric:



CPU Utilization



Current Value:



91%



Threshold:



80%



Severity:



Critical



Time:



10:20



Expected Action:



Support team should investigate the server/application performance immediately.



\---



\## 10. Expected Output



Using the sample dataset:



| Time | CPU % | Errors | Expected Monitoring Result |

|---|---:|---:|---|

| 10:00 | 45 | 0 | Healthy |

| 10:05 | 55 | 1 | Healthy |

| 10:10 | 72 | 2 | Healthy |

| 10:15 | 85 | 4 | CPU Warning |

| 10:20 | 91 | 10 | Critical Alert |

| 10:25 | 88 | 8 | Critical Alert |

| 10:30 | 65 | 2 | Healthy |



\---



\## 11. Assumptions



The following assumptions are used for this simple architecture:



1\. The application is running on an AWS EC2 instance.

2\. CloudWatch is used as the primary monitoring service.

3\. CPU utilization is available as a monitoring metric.

4\. Application logs can be sent to CloudWatch Logs where required.

5\. SNS is used for notification.

6\. Email is used as the example notification method.

7\. CPU above 80% is treated as a warning/alert condition.

8\. Application errors above 5 are treated as an alert condition.

9\. The thresholds are examples and must be reviewed for the real application.

10\. The solution is designed as a simple starting architecture and can be expanded later.



\---



\## 12. Simple Architecture Diagram



```text

&#x20;                   AWS

&#x20;                    |

&#x20;             +--------------+

&#x20;             |     EC2      |

&#x20;             | ATM-App-01   |

&#x20;             +--------------+

&#x20;                    |

&#x20;                    | Metrics / Logs

&#x20;                    v

&#x20;             +--------------+

&#x20;             |  CloudWatch  |

&#x20;             |              |

&#x20;             |   Metrics    |

&#x20;             |   Logs       |

&#x20;             |   Alarms     |

&#x20;             +--------------+

&#x20;                    |

&#x20;                    | Alert

&#x20;                    v

&#x20;             +--------------+

&#x20;             |     SNS      |

&#x20;             +--------------+

&#x20;                    |

&#x20;                    | Notification

&#x20;                    v

&#x20;             +--------------+

&#x20;             | Support Team |

&#x20;             +--------------+

