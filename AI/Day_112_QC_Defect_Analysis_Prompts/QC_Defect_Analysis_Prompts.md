# Day 112 — QC Defect Analysis Prompt Library

## 1. Objective

Create a reusable library of 10 AI prompts to support Quality Control (QC) defect analysis for ATM E-Surveillance systems.

The prompts help a QC manager classify defects, identify business risks, validate missing information, prioritise fixes, and prepare management reports.

## 2. Business Context

The company supplies ATM E-Surveillance systems across India. The QC team tests hardware, software, power systems, cameras, network devices, and related modules before dispatch or deployment.

AI should assist the QC team, not replace engineering investigation, physical testing, or final approval by authorised personnel.

## 3. Input Validation Rules

Before analysing any defect tracker, validate the following:

| Field | Validation requirement |
|---|---|
| Defect ID | Must be present and unique |
| Open Date | Must be a valid date |
| Defect Description | Must not be blank |
| Priority | Must be Critical, High, Medium, or Low, or explicitly marked Unknown |
| Stage | Must identify Pre-production, Post-production, or Unknown |
| Module | Must identify the affected module or be marked Unknown |
| Owner | Must identify HW, SW, EDGE, HW+SW, or Unknown |
| Status | Must be Open, In Progress, Resolved, or Cancelled |
| Blocking Function | Must be Yes, No, or Unknown |
| Failure Pattern | Must be Consistent, Intermittent, or Unknown |
| Evidence | Record logs, screenshots, test results, or state that evidence is missing |
| Business Impact | Must be described or marked Unknown |

### Validation behaviour

1. Never invent missing defect details.
2. Report missing or invalid fields before making a final assessment.
3. Identify duplicate defect IDs and invalid dates.
4. Distinguish confirmed facts from assumptions.
5. Do not classify an issue as resolved without supporting evidence.
6. Flag safety, power, security, and critical operational failures for appropriate engineering review.
7. If evidence is insufficient, recommend additional testing instead of claiming a confirmed root cause.

## 4. Ten Reusable QC Defect Analysis Prompts

### Prompt 1 — Defect Severity Classification

Act as a Senior QC Manager with 20 years of experience in ATM E-Surveillance systems.

Analyse the supplied defect tracker and classify each defect as Critical, High, Medium, or Low.

Consider functional impact, affected modules, production stage, failure frequency, customer impact, and whether the defect blocks a critical function.

**Output:**
- Defect ID and description
- Current priority and recommended priority
- Reason for classification
- Business impact
- Evidence required
- Recommended next action

Do not change the priority without explaining the reason. Flag missing information.

### Prompt 2 — Hardware, Software, and EDGE Ownership

Analyse the defect tracker and classify each issue as Hardware (HW), Software (SW), EDGE, HW+SW, or Unknown.

Use the symptoms, affected module, logs, reproduction procedure, and available test evidence.

**Output:**
- Defect ID
- Affected module
- Recommended ownership
- Technical justification
- Supporting evidence
- Team responsible for the next investigation
- Whether joint HW/SW investigation is required

Do not assign ownership based only on assumptions. Mark uncertain cases as Unknown.

### Prompt 3 — Top Five Show-Stopper Defects

Identify the five defects that pose the greatest risk to product functionality, production release, or ATM site operations.

Prioritise complete system failures, power failures, loss of critical camera feeds, serious network failures, and other verified critical-function blockers.

**Output:**
- Rank and defect ID
- Affected module
- Failure description
- Confirmed blocking function
- Business or operational impact
- Responsible team
- Immediate containment action
- Evidence needed to verify closure

If fewer than five defects meet the criteria, report only the qualifying defects. Do not invent additional show-stoppers.

### Prompt 4 — Missing Information and Data Quality Audit

Audit the QC tracker before technical analysis.

Check for missing defect IDs, invalid dates, blank descriptions, unknown ownership, missing reproduction steps, missing evidence, unclear failure frequency, and incomplete business-impact statements.

**Output a table with:**
- Defect ID
- Missing or invalid field
- Why the information matters
- Action required
- Suggested owner
- Priority for completing the information

Identify duplicate IDs and inconsistent records. Do not assume a blank field means that the defect has passed testing.

### Prompt 5 — Recurring Defect and Pareto Analysis

Analyse the supplied QC defect data to identify recurring defect categories and modules with the highest defect counts.

Group similar defects only when the descriptions support that grouping. Calculate category counts and percentages using the valid records supplied.

**Output:**
- Total valid defects analysed
- Defect count by category
- Percentage contribution by category
- Top three recurring categories
- Cumulative percentage for Pareto analysis
- Recommended corrective actions

State the denominator used in each percentage. Do not claim a trend over time unless dates and comparable historical data are available.

### Prompt 6 — Root Cause Analysis (RCA)

Act as an experienced QC and engineering problem-solving lead.

For each selected defect, analyse the observed symptom, reproduction procedure, test results, logs, environmental conditions, and previous corrective actions.

Use a structured 5 Whys approach where the evidence supports it.

**Output:**
- Problem statement
- Confirmed facts
- Potential causes and supporting evidence
- Five Whys analysis, where appropriate
- Root cause status: Confirmed, Suspected, or Undetermined
- Corrective action
- Preventive action
- Verification test
- Closure evidence required

Never present a suspected cause as a confirmed root cause.

### Prompt 7 — Intermittent vs Consistent Failure Analysis

Analyse the failure pattern for each defect.

Use the number of trials, number of failures, test conditions, logs, and reproduction results where available.

**Output:**
- Defect ID and affected module
- Total trials
- Failed trials
- Calculated failure rate, where the counts are valid
- Failure pattern: Consistent, Intermittent, or Unknown
- Confidence and evidence limitations
- Additional tests required

Calculate failure rate as failed trials divided by total valid trials, multiplied by 100. If total trials are zero, missing, or invalid, do not calculate the rate.

Do not label a defect intermittent merely because the description uses uncertain wording.

### Prompt 8 — Defect Aging and Escalation

Calculate how long each open defect has remained unresolved using a clearly stated report date.

Identify overdue issues, long-pending Critical or High defects, missing owners, and defects blocking production or deployment.

**Output:**
- Defect ID
- Open date
- Age in days
- Priority and status
- Blocking function
- Assigned team
- Recommended escalation
- Required completion action

Exclude Resolved and Cancelled defects from the open-defect escalation list. Explain any ageing threshold used and flag invalid dates.

### Prompt 9 — Corrective Action and Retesting Plan

Prepare a corrective-action and retesting plan for the selected defects.

Use the defect description, affected module, failure pattern, reproduction steps, logs, and engineering findings.

**Output:**
- Defect ID
- Containment action
- Proposed corrective action
- Responsible team
- Retest procedure
- Expected result
- Regression tests required
- Evidence to collect
- Closure criteria

Clearly separate proposed actions from approved engineering decisions. Do not mark a defect closed until the defined retest has passed and the required evidence is available.

### Prompt 10 — QC Management Executive Report

Prepare a concise management report from the validated defect tracker.

**Required sections:**
1. Executive summary
2. Total valid defects analysed
3. Defect count by Critical, High, Medium, and Low priority
4. Defects grouped by HW, SW, EDGE, HW+SW, and Unknown ownership
5. Top show-stopper defects
6. Open and overdue defect risks
7. Recurring defect categories
8. Missing information and evidence gaps
9. Decisions required from management
10. Recommended actions for the next 24–48 hours

Separate verified figures from estimates and assumptions. State the report date and data limitations. Do not fabricate counts, deadlines, owners, or technical conclusions.

## 5. Sample Input Dataset

Use this small fictional dataset to test the prompts. It is illustrative and does not represent actual company defect records.

| Defect ID | Module | Description | Priority | Owner | Status | Blocking | Failure pattern |
|---|---|---|---|---|---|---|---|
| DEF-001 | Main Unit | Unit does not power ON | Critical | HW | Open | Yes | Consistent |
| DEF-002 | Lobby Camera | No video output | Critical | Unknown | Open | Yes | Unknown |
| DEF-003 | Network Router | Network disconnects intermittently | High | SW | In Progress | No | Intermittent |
| DEF-004 | Outdoor Camera | Camera restarts intermittently | High | HW+SW | Open | No | Intermittent |
| DEF-005 | DCUPS | Backup power unavailable | Critical | HW | Open | Yes | Consistent |

### Sample data limitations

- The open dates are not supplied.
- Trial counts and failure counts are not supplied.
- Logs, screenshots, and reproduction procedures are not supplied.
- Ownership and severity require verification against actual engineering evidence.
- The sample is too small to establish a reliable long-term trend.

The prompts should identify these gaps rather than manufacture missing information.

## 6. Success Criteria

The prompt library is ready for use when:

- All 10 prompts are present.
- Each prompt specifies a clear task and expected output.
- Input validation and missing-data handling are documented.
- The sample dataset is clearly labelled as fictional.
- The prompts distinguish evidence from assumptions.
- No prompt encourages fabricated technical findings or unsupported closure decisions.

## 7. Conclusion

This prompt library provides a repeatable starting point for AI-assisted QC analysis. Actual defect prioritisation, root-cause confirmation, corrective action approval, and final closure remain subject to engineering evidence and the organisation's QC process.
