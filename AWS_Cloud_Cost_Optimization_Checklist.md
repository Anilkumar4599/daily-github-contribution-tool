\# Day 74 - AWS Cloud Cost Optimization Checklist



\## 1. Objective



The objective of this checklist is to identify simple opportunities to reduce unnecessary AWS cloud costs while maintaining application performance, availability, and business requirements.



Cost optimization should be performed without blindly reducing resources.



The objective is:



\*\*Right Resource + Right Size + Right Usage + Right Cost\*\*



\---



\## 2. Why Cloud Cost Optimization Is Important



Cloud resources can generate costs when they are:



\- Over-sized

\- Under-utilized

\- Running when they are not required

\- Duplicated

\- Not properly monitored

\- Using unnecessary storage

\- Missing appropriate lifecycle policies



Regular cost reviews help the organization control spending.



\---



\## 3. Simple Cost Optimization Checklist



| No. | Area | Check | Expected Action |

|---|---|---|---|

| 1 | EC2 | Check CPU utilization | Identify under-utilized instances |

| 2 | EC2 | Check instance size | Consider right-sizing |

| 3 | EC2 | Check unused instances | Stop or remove after business validation |

| 4 | EC2 | Check non-production servers | Stop when not required |

| 5 | Storage | Check unused storage | Remove after validation |

| 6 | S3 | Check old objects | Apply lifecycle/retention rules |

| 7 | Database | Check database utilization | Review sizing |

| 8 | Network | Review data transfer | Identify unnecessary transfer |

| 9 | Monitoring | Review cost alerts | Configure budget monitoring |

| 10 | Tags | Check resource tagging | Improve cost tracking |

| 11 | Reserved capacity | Review stable workloads | Evaluate appropriate pricing options |

| 12 | Auto Scaling | Review demand | Match capacity with workload |

| 13 | Backup | Review old backups | Remove only according to retention policy |

| 14 | Billing | Review monthly spend | Identify unexpected increases |

| 15 | Governance | Review ownership | Ensure every resource has an owner |



\---



\# 4. EC2 Cost Optimization



EC2 instances can generate significant costs.



Review:



\- Instance type

\- CPU utilization

\- Memory utilization

\- Running hours

\- Production/non-production status

\- Number of instances

\- Auto Scaling configuration

\- Ownership



\### Example



If an EC2 instance is continuously running but has very low utilization, investigate whether a smaller instance is appropriate.



Do not resize or stop production resources without validating the business requirement.



\---



\# 5. Storage Cost Optimization



Review storage resources regularly.



Check:



\- Unused volumes

\- Old snapshots

\- Old S3 objects

\- Duplicate files

\- Backup retention

\- Storage lifecycle rules



\### Example



Old non-required files may be moved to a lower-cost storage class according to business and retention requirements.



\---



\# 6. Database Cost Optimization



Review:



\- Database instance size

\- Utilization

\- Storage consumption

\- Backup retention

\- Number of database instances

\- Development/test database schedules



A database should not be resized or deleted only because utilization is low.



The application requirement and performance impact must be reviewed first.



\---



\# 7. Non-Production Environment



Development and testing environments may not need to run continuously.



Example:



```text

Development Server

Monday-Friday

09:00-19:00



8\. Resource Tagging



Resources should have meaningful tags.



Example:



Tag	Example Value

Application	ATM-Surveillance

Environment	Production

Department	QA

Owner	IT Operations

CostCenter	CC1001

Project	Central-Monitoring



Tags help identify ownership and support cost analysis.



9\. Monitoring and Budget Control



Cost optimization should include continuous monitoring.



Review:



Monthly AWS spending

Daily spending trends

Unexpected increases

Service-wise cost

Project-wise cost

Environment-wise cost



Example:



Monthly Budget = ₹50,000



Actual Spend = ₹42,000



Remaining Budget = ₹8,000



If spending increases unexpectedly, investigate the reason.



10\. Example Input



Assume the following AWS resources are currently running:



Resource	Environment	Monthly Cost	Utilization	Status

EC2-01	Production	₹15,000	70%	Required

EC2-02	Production	₹14,000	20%	Required

EC2-03	Development	₹8,000	5%	Not required after office hours

EBS-01	Production	₹3,000	80%	Required

EBS-02	Old Test	₹2,000	0%	Unused

S3-01	Backup	₹5,000	60%	Required



Total Monthly Cost:



₹47,000



11\. Example Analysis

EC2-01



Utilization:



70%



Status:



Required



Action:



No immediate cost reduction recommended.



EC2-02



Utilization:



20%



Status:



Required



Action:



Review instance sizing.



Possible right-sizing opportunity.



Business validation required before making changes.



EC2-03



Utilization:



5%



Environment:



Development



Action:



Review whether the server needs to run outside working hours.



Possible scheduling opportunity.



EBS-02



Utilization:



0%



Environment:



Old Test



Action:



Confirm that the volume is no longer required.



If confirmed and retention requirements are satisfied, remove it.



S3-01



Utilization:



60%



Status:



Required



Action:



Review storage lifecycle and retention policy.



Do not delete required backup data.



12\. Expected Output

Resource	Finding	Recommended Action	Priority

EC2-01	Normal utilization	No immediate action	Low

EC2-02	Low utilization	Review right-sizing	Medium

EC2-03	Very low development usage	Review scheduled shutdown	High

EBS-01	Required storage	No immediate action	Low

EBS-02	Unused test volume	Validate and remove if approved	High

S3-01	Required backup storage	Review lifecycle policy	Medium

13\. Expected Cost Optimization Logic



The objective is not:



"Delete anything that costs money."



The correct approach is:



Identify Cost

&#x20;     ↓

Check Usage

&#x20;     ↓

Check Business Requirement

&#x20;     ↓

Check Performance Impact

&#x20;     ↓

Identify Optimization Opportunity

&#x20;     ↓

Obtain Approval

&#x20;     ↓

Implement Change

&#x20;     ↓

Monitor Result

14\. Example Expected Savings



Assume the following approved actions:



EC2-03



Current monthly cost:



₹8,000



Estimated optimized cost:



₹3,000



Potential saving:



₹5,000/month



EBS-02



Current monthly cost:



₹2,000



If confirmed unused and approved for removal:



Potential saving:



₹2,000/month



Total Potential Saving

₹5,000 + ₹2,000 = ₹7,000/month



Estimated annualized opportunity:



₹7,000 × 12 = ₹84,000/year



These are example figures for learning only.



Actual savings must be calculated using real AWS billing data.



15\. Test Cases

Test Case 1 - Under-utilized EC2



Input:



EC2 utilization = 20%



Expected:



Flag for right-sizing review.



Status:



PASS



Test Case 2 - Unused Storage



Input:



EBS utilization = 0%



Expected:



Flag for business validation and possible removal.



Status:



PASS



Test Case 3 - Development Server



Input:



Development EC2 utilization = 5%



Expected:



Review scheduled shutdown outside working hours.



Status:



PASS



Test Case 4 - Required Production Resource



Input:



Production EC2 utilization = 70%



Expected:



Do not recommend deletion merely to reduce cost.



Status:



PASS



Test Case 5 - Required Backup



Input:



S3 backup storage is actively required.



Expected:



Do not delete the backup. Review lifecycle and storage-class optimization instead.



Status:



PASS



16\. Cost Optimization Priority



Use the following simple priority model:



High



Potentially significant saving with low business risk after validation.



Example:



Unused development resource.



Medium



Requires analysis or configuration change.



Example:



Right-sizing an under-utilized EC2 instance.



Low



No immediate action required.



Example:



A properly utilized production resource.



17\. Important Safety Rule



Cost optimization must not compromise:



Production availability

Data security

Data retention

Application performance

Backup requirements

Compliance requirements

Disaster recovery

Business continuity



Always validate before stopping, resizing, or deleting a resource.



18\. Simple Monthly Cost Review



A monthly review can follow this process:



Export or review AWS cost information.

Group cost by service.

Group cost by application.

Group cost by environment.

Identify high-cost resources.

Check resource utilization.

Identify unused resources.

Review optimization opportunities.

Obtain business/technical approval.

Implement approved changes.

Compare cost before and after optimization.

19\. Management Summary Example

Current Monthly Cost



₹47,000



Potential Optimization Opportunity



₹7,000/month



Potential Annualized Opportunity



₹84,000/year



Main Opportunities

Review development EC2 scheduling.

Review under-utilized production EC2 sizing.

Validate unused test storage.

Review S3 lifecycle policies.

Continue monthly cost monitoring.

20\. Day 74 Learning Summary



The main cost optimization principles are:



Right-size resources

Remove unused resources after validation

Schedule non-production resources

Review storage

Review database sizing

Monitor network costs

Use resource tags

Monitor budgets

Review backups

Continuously monitor spending



Most important rule:



Optimize cost without compromising business requirements.



21\. Final Validation



Example input was analyzed and an expected output was created.



Five test cases were completed.



Test Cases:



5



Passed:



5



Failed:



0



Overall Result:



PASS



22\. Day 74 Conclusion



A beginner-friendly AWS cloud cost optimization checklist was created.



The checklist includes:



EC2 cost review

Storage cost review

Database review

Non-production scheduling

Resource tagging

Budget monitoring

Example input

Expected output

Cost-saving calculation

Five test cases

Business validation rules



Final Result:



PASS





Save and close Notepad.



\---



\# Step 2 — Validate the file



Run:



```bash

ls -l AWS\_Cloud\_Cost\_Optimization\_Checklist.md

