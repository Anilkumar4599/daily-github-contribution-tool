\# Day 73 - Simple EC2 Monitoring Project



\## 1. Project Objective



The objective of this project is to document a simple monitoring solution for an Amazon EC2 instance.



The monitoring solution should help the support team identify server performance problems and receive alerts when important thresholds are exceeded.



This is a documentation and learning project.



No actual AWS infrastructure is created as part of this exercise.



\---



\## 2. Business Scenario



Assume a company is running an application on an AWS EC2 instance.



The application is important for business operations and needs to remain available.



The support team wants to monitor the EC2 server for:



\- High CPU utilization

\- High memory utilization

\- High disk utilization

\- Server availability

\- Application errors



When a monitored value crosses a defined threshold, an alert should be generated.



\---



\## 3. Proposed Architecture



The simple architecture is:



```text

&#x20;                AWS Cloud

&#x20;                    |

&#x20;                    v

&#x20;             +--------------+

&#x20;             |     EC2      |

&#x20;             | App Server    |

&#x20;             +--------------+

&#x20;                    |

&#x20;                    | Metrics / Logs

&#x20;                    v

&#x20;             +--------------+

&#x20;             |  CloudWatch  |

&#x20;             +--------------+

&#x20;                    |

&#x20;                    | Threshold

&#x20;                    v

&#x20;             +--------------+

&#x20;             | CloudWatch   |

&#x20;             |    Alarm     |

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

4. AWS Services Used
Amazon EC2

EC2 provides the virtual server where the application is assumed to be running.

Example:

Instance Name: ATM-App-Server-01
Environment: Production
Application: ATM Surveillance Application
Amazon CloudWatch

CloudWatch is used to monitor the EC2 instance.

Example metrics:

CPU utilization
Network traffic
Instance status
Application logs
Custom metrics where required
CloudWatch Alarm

A CloudWatch Alarm evaluates a metric against a defined threshold.

Example:

CPU utilization > 80%

If the configured alarm conditions are satisfied, an alert is generated.

Amazon SNS

SNS is used as the notification mechanism.

Example:

CloudWatch Alarm
↓
SNS
↓
Email Notification
↓
Support Team

5. Monitoring Requirements

The following monitoring requirements are assumed.

No.	Metric	Threshold	Expected Action
1	CPU Utilization	> 80%	Generate alert
2	Memory Utilization	> 80%	Generate alert
3	Disk Utilization	> 85%	Generate alert
4	Application Errors	> 5	Generate alert
5	Instance Availability	Unavailable	Critical alert

These thresholds are examples for learning purposes.

Actual production thresholds should be defined based on application requirements and operational experience.

6. Sample EC2 Monitoring Data

The following sample data is used to test the monitoring logic.

Time	Instance	CPU %	Memory %	Disk %	Errors	Instance Status
10:00	ATM-App-01	42	50	60	0	Running
10:05	ATM-App-01	55	58	62	1	Running
10:10	ATM-App-01	72	65	68	2	Running
10:15	ATM-App-01	84	70	70	3	Running
10:20	ATM-App-01	92	82	72	10	Running
10:25	ATM-App-01	89	81	73	8	Running
10:30	ATM-App-01	60	64	74	1	Running
10:35	ATM-App-01	45	52	75	0	Stopped
7. Expected Monitoring Result

Based on the thresholds:

Time	CPU	Memory	Errors	Status	Expected Result
10:00	42%	50%	0	Running	Healthy
10:05	55%	58%	1	Running	Healthy
10:10	72%	65%	2	Running	Healthy
10:15	84%	70%	3	Running	CPU Alert
10:20	92%	82%	10	Running	Critical Alert
10:25	89%	81%	8	Running	Critical Alert
10:30	60%	64%	1	Running	Healthy
10:35	45%	52%	0	Stopped	Availability Alert
8. Alert Severity

A simple severity model is used.

Healthy

All monitored values are within the defined thresholds.

Warning

One important metric exceeds its threshold.

Example:

CPU = 84%

Critical

Multiple important thresholds are exceeded or the instance becomes unavailable.

Example:

CPU = 92%

Memory = 82%

Errors = 10

Availability Alert

The EC2 instance is not running or is otherwise unavailable.

9. Example Alert
Alert ID

AWS-EC2-001

Instance

ATM-App-01

Metric

CPU Utilization

Current Value

92%

Threshold

80%

Severity

Critical

Time

10:20

Expected Action

The support team should investigate the EC2 instance and application performance.

Possible investigation areas:

Application load
Running processes
Resource consumption
Recent application changes
Network activity
Application logs
10. End-to-End Monitoring Flow

The complete process is:

Application runs on EC2.
EC2 generates monitoring information.
CloudWatch collects available metrics and logs.
CloudWatch evaluates monitoring conditions.
CloudWatch Alarm checks configured thresholds.
Alarm enters the appropriate state when conditions are met.
SNS sends the notification.
Support team receives the alert.
Support team investigates the problem.
Corrective action is taken.
Monitoring continues.
11. Test Cases
Test Case 1 - Normal CPU
Input

CPU = 60%

Threshold = 80%

Expected Result

No CPU alert should be generated.

Actual Result

CPU is below the threshold.

Status

PASS

Test Case 2 - High CPU
Input

CPU = 84%

Threshold = 80%

Expected Result

CPU alert should be generated if the configured alarm evaluation conditions are satisfied.

Actual Result

CPU exceeds the threshold.

Status

PASS

Test Case 3 - High CPU and Memory
Input

CPU = 92%

Memory = 82%

Expected Result

The monitoring solution should identify abnormal resource utilization.

Actual Result

Both CPU and memory exceed their example thresholds.

Status

PASS

Test Case 4 - Application Errors
Input

Application Errors = 10

Threshold = 5

Expected Result

Application error alert should be generated.

Actual Result

Error count exceeds the threshold.

Status

PASS

Test Case 5 - EC2 Availability
Input

Instance Status = Stopped

Expected Result

Availability alert should be generated.

Actual Result

The instance is not running.

Status

PASS

12. Validation Summary
Test Case	Scenario	Expected Result	Status
TC01	Normal CPU	No alert	PASS
TC02	CPU > 80%	CPU alert	PASS
TC03	CPU + Memory high	Resource alert	PASS
TC04	Errors > 5	Error alert	PASS
TC05	Instance stopped	Availability alert	PASS

Total Test Cases: 5

Passed: 5

Failed: 0

Overall Result: PASS

13. Assumptions

The following assumptions are used:

The application is running on an EC2 instance.
CloudWatch is used for monitoring.
CloudWatch Alarms are configured for important metrics.
SNS is used for example notifications.
Email is used as the example notification method.
CPU > 80% is considered an alert condition.
Memory > 80% is considered an alert condition.
Disk > 85% is considered an alert condition.
Application errors > 5 are considered an alert condition.
A stopped instance is treated as an availability problem.
Thresholds are examples and must be reviewed before production implementation.
The project is a documentation exercise and does not create actual AWS resources.
14. Possible Improvements

The project can be expanded later with:

Multiple EC2 instances
CloudWatch dashboards
CloudWatch Logs
Custom application metrics
Auto Scaling
Load Balancer monitoring
Automated incident creation
Automated remediation
Additional notification channels
Production-specific thresholds
15. Key Learning

The most important concept is:

EC2
  ↓
CloudWatch
  ↓
Alarm
  ↓
SNS
  ↓
Support Team

EC2 runs the application.

CloudWatch monitors the environment.

CloudWatch Alarm detects abnormal conditions.

SNS sends notifications.

The support team investigates and takes action.

16. Day 73 Conclusion

A simple EC2 monitoring project was documented.

The project includes:

AWS architecture
EC2 monitoring requirements
CloudWatch monitoring
CloudWatch alarms
SNS notification flow
Sample monitoring dataset
Expected monitoring output
Five test cases
Validation results
Project assumptions
Possible future improvements

Final Validation:

PASS