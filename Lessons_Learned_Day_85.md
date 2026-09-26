\# Day 85 — Lessons Learned



\## 1. Purpose



This document summarizes the important lessons learned during my recent

learning journey across Quality Control, Procurement, Power BI, AWS,

Git/GitHub, AI learning, and DevOps.



The objective is to record practical lessons, mistakes, improvements, and

next actions so that future learning becomes more structured and useful.



\---



\# 2. Learning Areas Covered



The major learning areas covered so far are:



1\. Quality Control and defect analysis

2\. Procurement and inventory analysis

3\. Power BI and dashboard development

4\. AWS and cloud concepts

5\. Git and GitHub

6\. AI-assisted learning and process analysis

7\. DevOps fundamentals



\---



\# 3. Lesson 1 — Documentation Is Not the Same as Practical Experience



\## What I Learned



Creating documentation helps understand concepts and creates a useful

reference, but documentation alone does not prove practical experience.



For example:



\- Writing about AWS EC2 is different from actually creating and testing an EC2 instance.

\- Writing about Power BI is different from building a working dashboard.

\- Writing about DevOps is different from executing a CI/CD pipeline.



\## Lesson



I should clearly distinguish between:



\*\*Learned / Documented\*\*



and



\*\*Practiced / Implemented / Tested\*\*



\## Improvement



For important technical subjects, learning should follow this pattern:



```text

Learn Concept

&#x20;    ↓

Document

&#x20;    ↓

Practice

&#x20;    ↓

Test

&#x20;    ↓

Record Result

4. Lesson 2 — Start Simple Before Automating
What I Learned

Automation should not be the first step.

Before automating a process, the existing process should be understood.

For example, for a QC defect process:

Current Process
     ↓
Identify Problem
     ↓
Improve Process
     ↓
Validate New Process
     ↓
Automate Stable Process
Lesson

If the existing process is not understood or standardized,
automation may simply make a bad process run faster.

Improvement

First create a simple manual process and validation checklist.
Then identify repetitive activities that can be automated.

5. Lesson 3 — Data Quality Comes Before Analysis
What I Learned

A dashboard or report is only as useful as the data behind it.

Important checks include:

Missing values
Duplicate records
Incorrect dates
Invalid quantities
Incorrect categories
Missing ownership
Incorrect status
Inconsistent naming
Lesson

Before calculating KPIs, the input data should be checked.

Example:

Raw Data
   ↓
Data Validation
   ↓
Data Cleaning
   ↓
Analysis
   ↓
Dashboard
Improvement

Create a standard data-validation checklist before building reports.

6. Lesson 4 — Evidence Is Important in QC
What I Learned

A defect should not be classified only from a short description.

Useful evidence can include:

Number of trials
Number of failures
Failure percentage
Reproduction steps
Logs
Screenshots
Videos
Test reports
Affected module
Business impact
Lesson

A statement such as:

"Camera is not working"

contains less information than:

10 trials
8 failures
80% failure rate
Camera interface affected
Reproducible
Live monitoring function blocked
Evidence attached
Improvement

Use structured defect fields before final classification or escalation.

7. Lesson 5 — Separate Facts From Assumptions
What I Learned

When information is missing, it is better to mark it as:

Unknown
Not Available
Not Tested
Not Confirmed

rather than creating an assumption and presenting it as a fact.

Lesson

Good analysis should clearly distinguish:

Actual data
Calculated values
Assumptions
Missing information
Conclusions
Improvement

Add an assumptions section to analysis documents whenever the available
information is incomplete.

8. Lesson 6 — GitHub Is Useful for Tracking Learning Progress
What I Learned

GitHub can be used not only for software development but also for maintaining
a structured learning portfolio.

A simple workflow is:

Create Work
    ↓
Review Work
    ↓
git add
    ↓
git commit
    ↓
git push
    ↓
GitHub History
Lesson

Regular commits create a history of what was learned and when it was completed.

Improvement

Continue maintaining daily learning files and meaningful commit messages.

9. Lesson 7 — Power BI Requires Hands-On Practice
What I Learned

Power BI concepts become easier to understand by actually creating:

Tables
Measures
KPI cards
Charts
Filters
Dashboards
Data models

For example:

Data
 ↓
Clean
 ↓
Model
 ↓
DAX Measures
 ↓
Visuals
 ↓
Dashboard
Lesson

Reading about Power BI is useful, but building a report provides a different
type of learning.

Improvement

Continue with practical Power BI exercises using QC and inventory datasets.

10. Lesson 8 — AWS Requires Controlled Practical Exercises
What I Learned

AWS concepts such as EC2, S3, RDS, IAM, and CloudWatch are easier to
understand when connected to a practical scenario.

However, cloud resources should not be created without understanding:

What the service does
Why it is needed
Possible charges
Security implications
How to test it
How to remove resources after testing
Lesson

A practical AWS exercise should follow:

Plan
 ↓
Check Cost
 ↓
Create
 ↓
Configure
 ↓
Test
 ↓
Capture Evidence
 ↓
Clean Up
Improvement

Use small, controlled AWS exercises instead of creating unnecessary
resources.

11. Lesson 9 — Process Improvement Should Be Measurable
What I Learned

A process improvement should ideally have a measurable objective.

For example:

Metric	Before	After
Manual steps	10	6
Missing fields	5	1
Processing time	30 min	15 min

These values are only examples.

Lesson

A process should not be called "improved" only because it looks better.
Actual results should be measured after implementation.

Improvement

Define a baseline before changing the process and compare the results after
implementation.

12. Lesson 10 — Test Cases Make Documentation Stronger
What I Learned

A process document becomes more useful when it includes test cases.

A simple test case contains:

Input
Action
Expected result
Actual result
Status

Example:

Test Case	Input	Expected Result
TC-01	Valid record	Record accepted
TC-02	Missing required field	Record rejected
TC-03	Invalid value	Record flagged
Lesson

Test cases help determine whether a proposed process behaves as expected.

13. Lesson 11 — AI Should Support Thinking, Not Replace It
What I Learned

AI can help with:

Structuring information
Creating templates
Generating test cases
Explaining technical concepts
Finding missing information
Preparing documentation
Summarizing data

However, the output should still be reviewed.

Lesson

AI-generated information should be checked against the actual business
requirement and available evidence.

Improvement

Use AI as an assistant:

Business Requirement
        ↓
AI Assistance
        ↓
Human Review
        ↓
Validation
        ↓
Final Output
14. Lesson 12 — Simple Solutions Are Easier to Maintain
What I Learned

A complicated solution is not automatically a better solution.

For a beginner project, a simple solution may be easier to:

Understand
Test
Troubleshoot
Explain
Maintain
Improve later
Lesson

Start with the smallest solution that solves the actual problem.

Then improve it gradually.

15. Common Mistakes to Avoid

The following mistakes should be avoided in future learning projects:

Mistake 1 — Assuming documentation equals implementation

Improvement: Clearly record whether something is documented, practiced,
tested, or implemented.

Mistake 2 — Automating before understanding the process

Improvement: Map the current process first.

Mistake 3 — Analyzing incomplete data without identifying gaps

Improvement: Create a missing-information list.

Mistake 4 — Creating cloud resources without checking cost and cleanup

Improvement: Plan the complete lifecycle before deployment.

Mistake 5 — Creating dashboards without validating source data

Improvement: Clean and validate data first.

Mistake 6 — Using AI output without verification

Improvement: Review important outputs against source data and business
requirements.

16. Simple Learning Framework

The lessons learned can be converted into one simple framework:

1. Understand
      ↓
2. Document
      ↓
3. Validate
      ↓
4. Practice
      ↓
5. Test
      ↓
6. Measure
      ↓
7. Improve
      ↓
8. Automate

This will be my basic approach for future technical and business-process
learning.

17. Next Learning Priorities

The next stage should focus more on practical work.

Priority 1 — Power BI

Build practical dashboards using QC and inventory data.

Priority 2 — AWS

Perform small, controlled AWS exercises with cost awareness and cleanup.

Priority 3 — Automation

Take one real repetitive procurement or QC process and create a small
automation prototype.

Priority 4 — DevOps

Gradually move from documentation into practical Linux, Git, CI/CD, Docker,
and cloud exercises.

18. Final Reflection

The biggest lesson from this learning journey is:

Learning becomes stronger when knowledge is converted into practice and
practice is validated with evidence.

Documentation provides the foundation.

Practical exercises provide experience.

Testing provides confidence.

Measurement provides evidence.

Continuous improvement connects everything together.

19. Final Summary
Learning Area	Main Lesson
QC	Evidence-based defect analysis is important
Procurement	Standardized processes improve visibility
Power BI	Data quality should come before visualization
AWS	Learn concepts and practice in controlled environments
Git/GitHub	Version history provides a useful learning record
DevOps	Theory should gradually move toward hands-on implementation
AI	AI should assist analysis while human review remains important
Automation	Understand and stabilize the process before automating

End of Day 85 — Lessons Learned


Save and close Notepad.

---

# Step 2: Review the document

First check that the file exists:

```bash
ls -l Lessons_Learned_Day_85.md