\# Day 118 — Recurring Hardware Defect Analysis Prompt



\## 1. Objective



Create a reusable AI prompt to identify recurring hardware defects in ATM E-Surveillance systems using QC defect records, test results, module information, and supporting evidence.



The prompt should help QC and engineering teams detect repeat symptoms, identify affected modules and products, quantify recurrence, and prioritise investigation.



It must distinguish a repeated symptom from a confirmed common root cause.



\## 2. Reusable AI Prompt



\### ROLE



Act as a Senior Hardware Quality Control and Reliability Analyst with experience in electronic systems, power modules, cameras, routers, DCUPS units, hardware testing, and defect investigation.



\### CONTEXT



I will provide QC defect records from ATM E-Surveillance products.



Available fields may include:



\- Defect ID

\- Product model or hardware revision

\- Module or component

\- Defect description

\- Defect category

\- Defect open date

\- Production stage

\- Test or trial count

\- Failure count

\- Defect status

\- Hardware owner

\- Serial number or batch number

\- Failure reproduction procedure

\- Logs, photographs, measurements, or test evidence

\- Root-cause investigation result

\- Corrective action and verification result



\*\*Reporting date:\*\* \[Enter date]



\*\*Reporting period:\*\* \[Enter period]



\*\*Product or module scope:\*\* \[Enter scope]



Not every field will necessarily be available.



\### TASK



\#### Step 1 — Validate the defect data



Check for:

\- Missing or duplicate defect IDs

\- Missing defect descriptions or modules

\- Invalid dates

\- Inconsistent hardware module names

\- Missing product model, revision, or batch information

\- Missing failure and trial counts

\- Conflicting defect statuses

\- Missing evidence or reproduction steps

\- Unverified root-cause claims



Flag duplicate-looking records for review rather than silently deleting them. A repeated report may represent a new occurrence, a duplicate entry, or an existing defect being updated.



\#### Step 2 — Identify potential recurrence



Group defects into candidate recurrence patterns using available evidence such as:

\- Similar failure symptoms

\- Same hardware module or component

\- Same product model or revision

\- Same batch or supplier lot

\- Similar test conditions

\- Similar failure reproduction steps

\- Matching confirmed root causes, where documented



Use separate categories:



\- \*\*Confirmed recurring defect:\*\* Records are supported by evidence of repeated occurrences of the same defect or verified failure mechanism.

\- \*\*Potential recurrence:\*\* Records share meaningful symptoms or module details, but more evidence is needed to establish whether they represent the same defect.

\- \*\*Similar symptom only:\*\* Descriptions appear similar, but available evidence is insufficient to group them confidently.

\- \*\*Unclassified:\*\* Missing or inconsistent data prevents reliable grouping.



Do not group defects solely because they contain the same generic word, such as “failure,” “restart,” or “power.”



\#### Step 3 — Quantify recurrence



Where valid data exists, calculate:

\- Number of defect records in each candidate group

\- Number of distinct affected units or serial numbers

\- Number of affected batches or revisions

\- Failure rate when valid trial and failure counts are available

\- Recurrence over time when dates and comparable historical data are available

\- Open and unresolved defect counts



Clearly state the denominator used for each percentage.



Do not treat the number of defect records as the number of failed units unless the data confirms that each record represents a distinct unit. Avoid double-counting the same incident or defect.



\#### Step 4 — Assess severity and business impact



Consider:

\- Whether a critical product function is blocked

\- Whether the issue involves power, video, network connectivity, or system stability

\- Whether the failure is consistent or intermittent

\- Number of verified affected units

\- Whether production release or deployment is blocked

\- Whether the defect remains open

\- Available evidence of customer or operational impact



Use the supplied severity criteria if available. If no formal criteria exist, label any suggested priority as provisional and explain the reasoning.



Do not infer a production stoppage, customer impact, or safety risk without supporting evidence.



\#### Step 5 — Recommend investigation and corrective action



For each significant candidate recurrence group, recommend:

\- Additional evidence required

\- Hardware inspection or measurement

\- Repeatability and reproduction testing

\- Comparison across product revisions or batches

\- Supplier or component-lot investigation, where relevant

\- Root-cause analysis

\- Corrective and preventive actions

\- Retest and regression verification

\- Closure criteria



Separate proposed actions from actions already completed. Never claim that a root cause is confirmed unless the supplied evidence supports it.



\### REQUIRED OUTPUT



\#### A. Executive Summary



Summarise the main recurrence patterns, severity concerns, data limitations, and investigation priorities.



\#### B. Data Validation Report



| Defect ID | Missing or Inconsistent Field | Impact on Analysis | Action Required |

|---|---|---|---|



\#### C. Candidate Recurring Defect Groups



| Candidate Group | Module | Defect IDs | Evidence of Similarity | Recurrence Classification | Confidence / Limitation |

|---|---|---|---|---|---|



\#### D. Recurrence Metrics



| Group | Record Count | Distinct Affected Units | Failure Rate, if Valid | Open Defects |

|---|---:|---:|---:|---:|



Do not calculate a failure rate when trial or failure counts are missing, invalid, or based on incompatible test conditions.



\#### E. Priority Investigation List



| Rank | Defect Group | Verified Severity | Evidence Gap | Recommended Investigation |

|---|---|---|---|---|



Explain the ranking criteria and identify provisional priorities clearly.



\#### F. Root-Cause and Corrective-Action Plan



| Candidate Group | Root-Cause Status | Proposed Investigation | Corrective Action | Verification Required |

|---|---|---|---|---|



Use root-cause statuses such as Confirmed, Suspected, and Undetermined.



\#### G. Assumptions and Limitations



List missing data, duplicate concerns, uncertain groupings, calculation limitations, and conclusions that require engineering verification.



\### MANDATORY SAFEGUARDS



1\. Never invent defect records, trial counts, failure counts, or affected-unit totals.

2\. Never claim a confirmed common root cause based only on similar descriptions.

3\. Never count duplicate reports as separate failures without verification.

4\. Never calculate a failure rate without a valid denominator.

5\. Never classify a defect as resolved without supporting closure evidence.

6\. Never assume a hardware issue is caused by a supplier or component batch without evidence.

7\. Distinguish confirmed facts, candidate patterns, and hypotheses.

8\. Explain why records have been grouped together.

9\. Preserve the original defect IDs so engineering can trace the findings.

10\. Recommend additional investigation whenever evidence is insufficient.



\## 3. Sample Input Dataset



The following fictional records are for demonstrating the prompt only.



\*\*Reporting date:\*\* 29 October 2026.



| Defect ID | Module | Product Revision | Description | Status | Evidence |

|---|---|---|---|---|---|

| DEF-501 | DCUPS | Rev A | Backup power unavailable during test | Open | Test log available |

| DEF-502 | DCUPS | Rev A | Backup power unavailable during test | Open | Test log available |

| DEF-503 | Main Unit Power | Rev B | Unit does not power ON | Open | Measurement details missing |

| DEF-504 | DCUPS | Rev A | Backup duration below expected level | In Progress | Test conditions missing |

| DEF-505 | Outdoor Camera | Rev A | Camera restarts intermittently | Open | Reproduction steps available |



\### Sample assumptions



\- The records are fictional.

\- Each defect ID represents a separate tracker record, not necessarily a distinct failed physical unit.

\- No serial numbers, batch numbers, trial counts, or failure counts are supplied.

\- No confirmed root-cause results are supplied.

\- “Backup power unavailable” and “backup duration below expected level” may be related, but the descriptions alone do not prove a common root cause.

\- No formal severity classification criteria are supplied.



\## 4. Example Expected Output



\### A. Executive Summary



The sample contains five defect records. Three involve the DCUPS module, including two records with the same stated symptom. This is a candidate recurrence pattern requiring verification. The records do not establish how many physical units failed or whether the underlying root cause is identical.



The Main Unit Power and Outdoor Camera records describe separate symptoms. Their recurrence cannot be established from the sample alone.



\### B. Candidate Recurring Defect Groups



| Candidate Group | Module | Defect IDs | Classification | Reason |

|---|---|---|---|---|

| DCUPS backup power unavailable | DCUPS | DEF-501, DEF-502 | Potential recurrence | Same module and reported symptom; distinct physical units and common cause not verified |

| DCUPS backup performance | DCUPS | DEF-504 | Similar area, insufficient evidence | Backup duration issue may be related, but test conditions and failure mechanism are unknown |

| Main Unit power failure | Main Unit Power | DEF-503 | Single record | No second comparable record supplied |

| Outdoor Camera restart | Outdoor Camera | DEF-505 | Single record | No second comparable record supplied |



\### C. Investigation Priorities



1\. Compare the logs and test conditions for DEF-501 and DEF-502 to verify whether they represent separate occurrences of the same failure.

2\. Review DEF-504's backup-duration test method and acceptance criteria before grouping it with DEF-501 and DEF-502.

3\. Obtain the missing measurement details for DEF-503.

4\. Reproduce the intermittent camera restart in DEF-505 and preserve supporting evidence.



These are proposed investigation priorities, not confirmed root-cause conclusions.



\### D. Metrics and Limitations



\- Total defect records: 5.

\- DCUPS-related records: 3.

\- Records with the exact stated symptom “Backup power unavailable during test”: 2.

\- Distinct failed units: Unknown.

\- Hardware failure rate: Not calculable because trial and failure counts are missing.

\- Confirmed common root causes: None supplied.



\## 5. Test Cases



\### Test Case 1 — Identify a repeated symptom



\*\*Input:\*\* DEF-501 and DEF-502 both describe “Backup power unavailable during test” on the DCUPS module.



\*\*Expected:\*\* Group them as a potential recurrence pattern and request verification of distinct affected units and evidence.



\*\*Pass condition:\*\* The prompt identifies the repeated symptom but does not claim a confirmed common root cause.



\### Test Case 2 — Avoid unsupported grouping



\*\*Input:\*\* DEF-504 describes “Backup duration below expected level,” while DEF-501 and DEF-502 describe “Backup power unavailable during test.”



\*\*Expected:\*\* Flag a possible relationship but retain uncertainty until test conditions, failure mechanism, and evidence are compared.



\*\*Pass condition:\*\* Similar module names alone do not establish that all three defects share one root cause.



\### Test Case 3 — Handle missing failure counts



\*\*Input:\*\* No trial counts, failed-trial counts, or distinct unit identifiers are supplied.



\*\*Expected:\*\* Report the record counts but mark the failure rate and number of affected physical units as unavailable.



\*\*Pass condition:\*\* No unsupported failure percentage or affected-unit count is generated.



\## 6. Completion Checklist



\- \[ ] Reusable prompt created.

\- \[ ] Input-validation rules included.

\- \[ ] Sample dataset and assumptions documented.

\- \[ ] Expected output included.

\- \[ ] Test Case 1 reviewed.

\- \[ ] Test Case 2 reviewed.

\- \[ ] Test Case 3 reviewed.

\- \[ ] Facts separated from hypotheses.

\- \[ ] README created.

\- \[ ] Files committed and pushed to GitHub.



\## 7. Conclusion



Recurring-defect analysis helps QC and engineering teams prioritise investigation, but reliable conclusions require traceable records, consistent test conditions, and supporting evidence. This prompt provides a repeatable way to identify candidate patterns without confusing repeated symptoms with confirmed root causes.



