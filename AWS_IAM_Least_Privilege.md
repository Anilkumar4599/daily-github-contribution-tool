\# Day 75 – AWS IAM Least-Privilege Principles



\## 1. Objective



Document the AWS IAM least-privilege principle in simple terms.



The objective is to understand how to provide users, applications, and services only the permissions they actually need.



This reduces the risk of accidental or unauthorized access.



\---



\## 2. What is AWS IAM?



IAM stands for Identity and Access Management.



AWS IAM is used to control:



\- Who can access AWS resources

\- What actions they can perform

\- Which resources they can access



Examples of IAM identities:



\- Users

\- Groups

\- Roles

\- Applications and AWS services



\---



\## 3. What is Least Privilege?



Least privilege means:



> Give only the minimum permissions required to perform a specific job.



For example:



A person who only needs to read files from an S3 bucket should not automatically receive permission to:



\- Delete files

\- Create buckets

\- Modify IAM users

\- Access unrelated AWS services



The user should receive only the required read permissions.



\---



\## 4. Simple Real-World Example



Assume an organization has an AWS S3 bucket:



`company-qc-reports`



The QC reporting application only needs to read QC reports.



Required access:



\- Read objects from the bucket



Not required:



\- Delete objects

\- Upload objects

\- Create buckets

\- Modify IAM policies

\- Access EC2

\- Access RDS



Therefore, the application should receive only the required S3 read permission.



\---



\## 5. Least-Privilege Logic



The basic logic is:



```text

Business Requirement

&#x20;       ↓

Identify Required Resource

&#x20;       ↓

Identify Required Action

&#x20;       ↓

Give Minimum Required Permission

&#x20;       ↓

Test the Permission

&#x20;       ↓

Remove Unnecessary Permission



Example:



Requirement:

QC application needs to read reports.



Resource:

S3 bucket – company-qc-reports



Required action:

Read objects



Permission:

Read-only access to required S3 objects



Unnecessary permissions:

Delete / Modify / IAM administration / EC2 administration

6\. IAM Permission Components



An IAM policy generally defines:



Effect



Whether the action is:



Allow

Deny

Action



What the identity can do.



Examples:



Read

Write

Delete

Create

List

Resource



Which AWS resource the permission applies to.



Example:



S3 bucket: company-qc-reports

Condition



Optional rules that further restrict when access is allowed.



7\. Simple Permission Example



Example requirement:



A reporting application needs to read objects from one S3 bucket.



Conceptual permission:



Effect:

Allow



Action:

Read objects



Resource:

company-qc-reports



Purpose:

Allow the application to retrieve QC reports.



The application does not need administrative permissions.



8\. Least Privilege vs Excessive Permission

Excessive Permission

Application

&#x20;   ↓

Administrator Access

&#x20;   ↓

All AWS Services



Risk:



The application may be able to access or modify resources that it does not need.



Least Privilege

Application

&#x20;   ↓

Required Permission

&#x20;   ↓

Required AWS Resource



Benefit:



The application has only the access necessary for its function.



9\. IAM Best Practices

1\. Give only required permissions



Do not provide broad permissions when a smaller permission set is sufficient.



2\. Avoid unnecessary administrator access



Administrator permissions should not be used for normal application or operational activities.



3\. Restrict access to required resources



Where possible, specify the exact resource instead of allowing access to all resources.



4\. Review permissions regularly



Permissions should be reviewed when:



Job responsibilities change

Applications change

AWS resources change

Old access is no longer required

5\. Remove unused permissions



If access is no longer required, remove it.



6\. Use roles for applications and AWS services



Applications and AWS services should generally use IAM roles rather than embedding long-term access credentials.



7\. Separate responsibilities



Different users or teams should receive permissions appropriate to their responsibilities.



10\. Example – ATM Surveillance Environment



Consider an ATM surveillance monitoring application running in AWS.



The application needs to:



Send monitoring data

Read required configuration

Write application logs



It does not need to:



Create IAM users

Delete databases

Modify network configuration

Shut down unrelated EC2 instances

Change security policies



Therefore, the application should receive only the permissions required for monitoring and logging.



Example:



ATM Monitoring Application

&#x20;         ↓

&#x20;     IAM Role

&#x20;         ↓

&#x20; Required Permissions

&#x20;         ↓

Monitoring / Logging Resources

11\. Permission Review Checklist

Check	Question	Expected Result

1	Is the user/application identified?	Yes

2	Is the business requirement documented?	Yes

3	Is the required AWS resource identified?	Yes

4	Are required actions identified?	Yes

5	Are unnecessary actions removed?	Yes

6	Is administrator access avoided where unnecessary?	Yes

7	Are permissions reviewed periodically?	Yes

8	Is unused access removed?	Yes

12\. Example Input

User:

QC\_Report\_User



Business Requirement:

Read QC reports from S3.



Required Resource:

company-qc-reports



Required Action:

Read report objects



Unnecessary Actions:

Delete objects

Create buckets

Modify IAM

Access EC2

Access RDS

13\. Expected Output

IAM Access Decision:



Allow:

Read access to required QC report objects.



Do Not Allow:

Delete

Create

IAM administration

EC2 administration

RDS administration



Reason:

The user only needs to read QC reports.

14\. Validation Test Cases

Test Case 1 – Required Read Access



Input:



User requests access to read QC reports.



Expected:



Read access is allowed.



Result:



PASS

Test Case 2 – Delete Access



Input:



User attempts to delete a QC report.



Expected:



Delete access is denied.



Result:



PASS

Test Case 3 – IAM Administration



Input:



QC reporting application attempts to modify IAM permissions.



Expected:



IAM administration access is denied.



Result:



PASS

Test Case 4 – Unrelated AWS Resource



Input:



QC reporting user attempts to access an unrelated RDS database.



Expected:



Access is denied.



Result:



PASS

Test Case 5 – Permission Review



Input:



User no longer works with QC reports.



Expected:



QC report access is reviewed and removed if no longer required.



Result:



PASS

15\. Simple IAM Decision Matrix

User/Application	Requirement	Access

QC Report User	Read QC reports	Read

QC Report User	Delete QC reports	Deny

Monitoring Application	Write monitoring data	Write

Monitoring Application	Modify IAM	Deny

Support User	View monitoring information	Read

Support User	Delete AWS resources	Deny

16\. Key Learning



The most important IAM principle is:



Need → Identify → Restrict → Test → Review



Before granting permission, ask:



What does this user/application need to do?

Which AWS resource is required?

Which action is required?

Can the permission be made more specific?

Are any unnecessary permissions included?

17\. Final Summary



AWS IAM least privilege means providing only the minimum permissions required to perform a specific task.



Example:



Need:

Read QC reports



Resource:

S3 QC report bucket



Permission:

Read



Unnecessary:

Delete / Admin / IAM / EC2 / RDS



Result:

Limited access with reduced risk



Least privilege should be reviewed regularly because business requirements, applications, and responsibilities can change.



18\. Day 75 Completion



Task:



\#75 – Document IAM least-privilege principles



Domain:



AWS



Status:



Completed after documentation review and GitHub commit.



\---



\# 2. Save and close Notepad



After pasting:



\*\*Ctrl + S\*\*



Then close Notepad.



\---



\# 3. Check the file



Back in Git Bash:



```bash

ls -l AWS\_IAM\_Least\_Privilege.md

