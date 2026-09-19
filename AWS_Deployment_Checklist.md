\# Day 78 – AWS Deployment Checklist



\## 1. Objective



Create a simple checklist for deploying an application to AWS.



The checklist covers:



\- Pre-deployment preparation

\- Security and access checks

\- Deployment activities

\- Post-deployment validation

\- Rollback preparation

\- Test cases



This checklist is intended for learning and can be adapted for a real project after technical and business review.



\---



\## 2. Example Project



Project: ATM Surveillance Monitoring Application



Deployment environment: AWS test environment



Application purpose:



\- Receive ATM monitoring information.

\- Display device health information.

\- Help the support team identify failures.

\- Generate alerts for selected abnormal conditions.



Assumption:



This is a sample project. No production ATM data or customer-sensitive information is used.



\---



\## 3. Deployment Overview



```text

Deployment Preparation

&#x20;       |

&#x20;       v

Security and Access Review

&#x20;       |

&#x20;       v

Infrastructure Readiness

&#x20;       |

&#x20;       v

Application Deployment

&#x20;       |

&#x20;       v

Post-Deployment Testing

&#x20;       |

&#x20;       v

Business / QA Validation

&#x20;       |

&#x20;       v

Deployment Closure

```



If a critical validation fails, stop the deployment or follow the approved rollback procedure.



\---



\## 4. Pre-Deployment Checklist



| No. | Checkpoint | Expected Result | Status |

|---|---|---|---|

| 1 | Deployment requirement is documented | Requirement approved | Not Started |

| 2 | Application version is confirmed | Correct version identified | Not Started |

| 3 | Deployment date and time are confirmed | Approved deployment window | Not Started |

| 4 | Required AWS resources are identified | Resource list available | Not Started |

| 5 | Required configuration is reviewed | Configuration verified | Not Started |

| 6 | Dependencies are checked | Required dependencies available | Not Started |

| 7 | Backup or recovery approach is reviewed | Recovery plan documented | Not Started |

| 8 | Rollback procedure is documented | Rollback steps available | Not Started |

| 9 | Responsible team members are identified | Owners confirmed | Not Started |

| 10 | Communication plan is ready | Stakeholders informed | Not Started |



\---



\## 5. Security and Access Checklist



| No. | Checkpoint | Expected Result | Status |

|---|---|---|---|

| 1 | IAM permissions are reviewed | Minimum required permissions granted | Not Started |

| 2 | Administrator access is restricted | No unnecessary administrator access | Not Started |

| 3 | Application secrets are protected | No credentials stored in source files | Not Started |

| 4 | Network access is reviewed | Only required access permitted | Not Started |

| 5 | Security groups are reviewed | Rules match approved requirements | Not Started |

| 6 | Logging requirements are reviewed | Required logs can be collected | Not Started |



Do not place passwords, access keys, tokens, or other secrets in this checklist or in GitHub.



\---



\## 6. Deployment Checklist



| No. | Activity | Expected Result | Status |

|---|---|---|---|

| 1 | Confirm approval to begin deployment | Approval recorded | Not Started |

| 2 | Confirm target environment | Correct environment selected | Not Started |

| 3 | Verify application package | Approved package identified | Not Started |

| 4 | Verify configuration values | Correct values confirmed | Not Started |

| 5 | Deploy the application | Deployment completes without unexpected errors | Not Started |

| 6 | Review deployment logs | No unresolved deployment errors | Not Started |

| 7 | Verify application startup | Application starts successfully | Not Started |

| 8 | Record deployment version and time | Deployment record updated | Not Started |



\---



\## 7. Post-Deployment Validation Checklist



| No. | Validation | Expected Result | Status |

|---|---|---|---|

| 1 | Application health check | Application responds as expected | Not Started |

| 2 | Login or access test | Authorized user can access the application | Not Started |

| 3 | Permission test | Unauthorized actions are rejected | Not Started |

| 4 | Monitoring test | Required metrics or logs are available | Not Started |

| 5 | Alert test | Configured test alert is received | Not Started |

| 6 | Functional test | Main business function works | Not Started |

| 7 | Error-log review | No unresolved critical errors | Not Started |

| 8 | Stakeholder confirmation | QA/support validation recorded | Not Started |



\---



\## 8. Rollback Checklist



Rollback may be required if the deployment causes a critical issue.



| No. | Checkpoint | Expected Result |

|---|---|---|

| 1 | Rollback trigger is defined | Conditions for rollback are documented |

| 2 | Previous stable version is identified | Recovery version is available |

| 3 | Responsible owner is identified | Rollback decision owner is known |

| 4 | Recovery steps are documented | Steps have been reviewed |

| 5 | Rollback result is validated | Application returns to an acceptable state |

| 6 | Stakeholders are informed | Deployment status is communicated |



Rollback should follow the organization's approved change-management process.



\---



\## 9. Sample Dataset



This small dataset is fictional and is used to demonstrate deployment validation.



| Test ID | Scenario | Expected Result |

|---|---|---|

| TC01 | Application starts after deployment | Application is available |

| TC02 | Authorized support user logs in | Login succeeds |

| TC03 | Unauthorized user attempts restricted action | Access is denied |

| TC04 | Monitoring event is generated | Event is recorded |

| TC05 | Application health check is performed | Health check succeeds |



\---



\## 10. Test Cases



\### Test Case 1 – Application Availability



Test ID: TC01



Input:



```text

Application deployment completed.

Perform an application health check.

```



Expected result:



```text

Application responds successfully.

No startup failure is reported.

```



Pass criteria:



The application is reachable and the health check succeeds.



\---



\### Test Case 2 – Authorized Access



Test ID: TC02



Input:



```text

An authorized support user attempts to log in.

```



Expected result:



```text

The authorized user can access the permitted application functions.

```



Pass criteria:



Login succeeds and the user can access only the functions allowed by their role.



\---



\### Test Case 3 – Unauthorized Access



Test ID: TC03



Input:



```text

A user without the required permission attempts a restricted action.

```



Expected result:



```text

The restricted action is denied.

```



Pass criteria:



The action is blocked and the event is recorded where applicable.



\---



\### Test Case 4 – Monitoring Validation



Test ID: TC04



Input:



```text

Generate a sample monitoring event.

Check the configured monitoring destination.

```



Expected result:



```text

The event is recorded and can be reviewed by the support team.

```



Pass criteria:



The monitoring event is visible in the expected location.



\---



\### Test Case 5 – Rollback Readiness



Test ID: TC05



Input:



```text

Review the documented rollback procedure.

Confirm that the previous stable version and recovery owner are identified.

```



Expected result:



```text

Rollback steps, recovery version, and responsible owner are documented.

```



Pass criteria:



The deployment team can identify the approved recovery process.



Note: This documentation check does not execute an actual rollback.



\---



\## 11. Deployment Completion Record



| Field | Value |

|---|---|

| Project | ATM Surveillance Monitoring Application |

| Environment | Test |

| Application Version | To be recorded |

| Deployment Date/Time | To be recorded |

| Deployment Owner | To be recorded |

| QA Validation Owner | To be recorded |

| Deployment Result | Pending |

| Rollback Required | Pending |

| Remarks | To be recorded |



\---



\## 12. Assumptions and Limitations



1\. This checklist is a learning example, not an approved production procedure.

2\. The sample application and test data are fictional.

3\. No AWS resources are created as part of this exercise.

4\. The checklist assumes that application requirements and deployment approvals are handled separately.

5\. Actual AWS services and deployment steps depend on the application architecture.

6\. Security, backup, monitoring, and rollback requirements must be reviewed for the target environment.

7\. Production deployment must follow the organization's change-management and security processes.

8\. Test cases must be adapted to the application's actual requirements.



\---



\## 13. Key Learning



A deployment is not complete just because the application package has been installed.



A controlled deployment includes:



```text

Prepare

&#x20; ↓

Review

&#x20; ↓

Deploy

&#x20; ↓

Validate

&#x20; ↓

Record

&#x20; ↓

Close or Roll Back

```



The team should verify application functionality, access control, monitoring, and recovery readiness.



\---



\## 14. Day 78 Summary



Task: #78 – Create an AWS deployment checklist



Domain: AWS



Deliverable: AWS\_Deployment\_Checklist.md



Included:



\- Pre-deployment checklist

\- Security and access checklist

\- Deployment checklist

\- Post-deployment validation

\- Rollback checklist

\- Five sample test cases

\- Assumptions and limitations



Status: Complete after review and GitHub commit.

