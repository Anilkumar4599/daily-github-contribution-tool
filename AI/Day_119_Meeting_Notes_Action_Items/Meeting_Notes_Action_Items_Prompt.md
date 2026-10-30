\# Day 119 — Meeting Notes to Action Items



\## 1. Objective



Create a reusable AI prompt that converts raw meeting notes into structured action items, clearly identifying decisions, responsibilities, deadlines, priorities, pending clarifications, and follow-up requirements.



The prompt is designed for procurement, supplier coordination, QA/QC, inventory, service operations, and management review meetings.



\## 2. Reusable AI Prompt



\### ROLE



Act as a Senior Project Coordinator and Management Reporting Analyst experienced in meeting documentation, procurement coordination, supplier follow-ups, quality management, service operations, and action tracking.



Your responsibility is to convert unstructured meeting notes into an accurate and professional action tracker.



\### CONTEXT



I will provide raw meeting notes. They may contain:



\- Meeting date and title

\- Participants

\- Discussion points

\- Decisions taken

\- Action items

\- Responsible persons

\- Target completion dates

\- Pending confirmations

\- Risks and dependencies

\- Supplier or customer commitments



The notes may be incomplete, informal, repetitive, or unclear.



\### TASK



\#### Step 1 — Review and understand the notes



Identify:



\- Main discussion topics

\- Decisions explicitly made

\- Actions explicitly requested or agreed

\- Responsible persons, if named

\- Deadlines, if mentioned

\- Pending information and clarifications

\- Risks, blockers, and dependencies



Do not treat a discussion point as an agreed action unless the notes support that interpretation.



\#### Step 2 — Extract action items



Convert each clear action into a specific task.



Each action should explain:



\- What needs to be done

\- Who is responsible, if identified

\- When it is due, if specified

\- What evidence will demonstrate completion, where appropriate



Use clear, professional, action-oriented language.



\#### Step 3 — Classify action status



Use these labels:



\- \*\*Assigned:\*\* An action is agreed and an owner is identified.

\- \*\*Owner Pending:\*\* An action is agreed, but no owner is identified.

\- \*\*Deadline Pending:\*\* An action is agreed, but no deadline is identified.

\- \*\*Clarification Required:\*\* The action or responsibility is unclear.

\- \*\*Completed:\*\* The notes explicitly confirm completion.

\- \*\*Not an Action:\*\* A discussion point or information item that does not require follow-up.



Do not mark an action completed just because it was discussed.



\#### Step 4 — Assign priority



Use:



\- \*\*High:\*\* Explicitly urgent, business-critical, or linked to a near-term commitment.

\- \*\*Medium:\*\* Important follow-up without evidence of immediate urgency.

\- \*\*Low:\*\* Routine or non-urgent follow-up.



If urgency cannot be established, use \*\*Priority Not Confirmed\*\* rather than guessing.



\#### Step 5 — Identify missing information



Highlight:



\- Actions without owners

\- Actions without deadlines

\- Unclear commitments

\- Conflicting dates or instructions

\- Dependencies and blockers

\- Decisions that require confirmation



Never invent a person's name, deadline, commitment, or meeting decision.



\#### Step 6 — Prepare follow-up recommendations



Recommend practical next steps, such as:



\- Confirming the action owner

\- Agreeing a target date

\- Obtaining supplier confirmation

\- Sharing missing documents

\- Escalating an unresolved blocker

\- Reviewing open actions in the next meeting



Clearly distinguish recommendations from decisions already made.



\### REQUIRED OUTPUT



\#### A. Meeting Summary



Provide:

\- Meeting title

\- Meeting date, if available

\- Participants, if available

\- Three to five key discussion highlights



\#### B. Decisions Taken



| No. | Decision | Supporting Meeting Note |

|---|---|---|



Include only decisions supported by the notes. If none are explicit, say so.



\#### C. Action Item Tracker



| ID | Action Item | Owner | Target Date | Priority | Status | Completion Evidence / Next Step |

|---|---|---|---|---|---|---|



Give each action a unique ID such as ACT-001.



Use "Not Specified" for missing owners or deadlines.



\#### D. Pending Clarifications



| No. | Clarification Required | Reason | Suggested Next Step |

|---|---|---|---|



\#### E. Risks and Blockers



| Risk / Blocker | Possible Impact | Evidence Available | Recommended Action |

|---|---|---|---|



Do not present a possible impact as a confirmed business loss.



\#### F. Management Attention Required



List only issues that genuinely require management support, a decision, or escalation.



\#### G. Next Meeting Follow-up



List the open actions that should be reviewed in the next meeting.



\### MANDATORY SAFEGUARDS



1\. Never invent an action owner.

2\. Never invent a target date or supplier commitment.

3\. Never convert a discussion point into a confirmed decision.

4\. Never mark an action completed without explicit evidence in the notes.

5\. Keep facts separate from assumptions and recommendations.

6\. Preserve important names, PO numbers, dates, quantities, and references exactly as provided.

7\. If two notes conflict, report the conflict for clarification.

8\. Do not create duplicate action items for the same commitment.

9\. If one discussion contains two independent tasks, separate them into two action items.

10\. Use professional, concise business language.

11\. If information is missing, state "Not Specified" or "Clarification Required."

12\. Do not expose confidential meeting information unnecessarily.



\## 3. Sample Meeting Notes



\*\*Meeting:\*\* Weekly Procurement and QC Review  

\*\*Date:\*\* 30 October 2026  

\*\*Participants:\*\* Procurement Manager, QC Manager, Service Manager



Raw notes:



\- PO-501 delivery is delayed. Procurement team to contact the supplier and obtain a revised delivery date by 31 October.

\- QC team reported that 3 DCUPS units failed testing. QC Manager to share the failure report with the hardware team.

\- Hardware team needs to investigate the DCUPS issue. No completion date was agreed.

\- Service Manager said that 5 customer complaints are pending review.

\- Team discussed improving the weekly supplier follow-up process.

\- Management agreed that the PO-501 delivery status should be reviewed in the next meeting.

\- One participant mentioned that an updated stock report may be required, but no owner was assigned.



\## 4. Example Expected Output



\### A. Meeting Summary



The weekly Procurement and QC Review was held on 30 October 2026. The discussion covered delayed PO delivery, DCUPS testing failures, pending customer complaints, and supplier follow-up improvements.



\### B. Decisions Taken



| No. | Decision | Supporting Meeting Note |

|---|---|---|

| 1 | Review PO-501 delivery status in the next meeting | Management agreed to review the status |



No other formal decisions are explicitly recorded in the sample notes.



\### C. Action Item Tracker



| ID | Action Item | Owner | Target Date | Priority | Status |

|---|---|---|---|---|---|

| ACT-001 | Contact the supplier and obtain a revised delivery date for PO-501 | Procurement Team | 31 Oct 2026 | High | Assigned |

| ACT-002 | Share the failure report for the 3 DCUPS units with the hardware team | QC Manager | Not Specified | Medium | Deadline Pending |

| ACT-003 | Investigate the DCUPS testing failures | Hardware Team | Not Specified | Medium | Deadline Pending |

| ACT-004 | Review the 5 pending customer complaints | Service Manager | Not Specified | Medium | Deadline Pending |

| ACT-005 | Review PO-501 delivery status in the next meeting | Owner Not Specified | Next meeting; date not specified | High | Owner Pending |

| ACT-006 | Confirm whether an updated stock report is required and assign responsibility | Owner Not Specified | Not Specified | Priority Not Confirmed | Clarification Required |



\### D. Pending Clarifications



| No. | Clarification | Reason | Suggested Next Step |

|---|---|---|---|

| 1 | Who will investigate the DCUPS issue? | Hardware team is mentioned, but no individual owner is named | Confirm the responsible engineer |

| 2 | What is the target date for the DCUPS investigation? | No deadline was agreed | Confirm a target date |

| 3 | Who will review the pending customer complaints and by when? | Deadline and detailed ownership are not specified | Confirm the review schedule |

| 4 | Who owns the stock report requirement? | No owner was assigned | Confirm whether the report is required and assign an owner |



\### E. Management Attention Required



\- Confirm the owner and target date for the hardware investigation if the issue requires management coordination.

\- Review PO-501 delivery status at the next meeting.



\### F. Next Meeting Follow-up



\- Revised supplier delivery commitment for PO-501.

\- Status of the DCUPS failure investigation.

\- Review status of the 5 pending customer complaints.

\- Confirmation of the stock report requirement.



\## 5. Test Cases



\### Test Case 1 — Missing owner



\*\*Input:\*\* "The stock report needs to be updated."



\*\*Expected:\*\* Create an action or clarification item with owner "Not Specified." Do not invent a responsible person.



\*\*Pass condition:\*\* No owner is fabricated.



\### Test Case 2 — Missing deadline



\*\*Input:\*\* "Hardware team to investigate the DCUPS failure."



\*\*Expected:\*\* Create an action assigned to the Hardware Team, with target date "Not Specified."



\*\*Pass condition:\*\* No deadline is invented.



\### Test Case 3 — Discussion is not a decision



\*\*Input:\*\* "The team discussed introducing a new supplier follow-up process."



\*\*Expected:\*\* Record this as a discussion point or potential follow-up, not as an approved decision.



\*\*Pass condition:\*\* The AI does not claim management approval.



\## 6. Completion Checklist



\- \[ ] Reusable prompt created.

\- \[ ] Sample meeting notes included.

\- \[ ] Expected output included.

\- \[ ] Test Case 1 checked.

\- \[ ] Test Case 2 checked.

\- \[ ] Test Case 3 checked.

\- \[ ] Missing owners and deadlines handled correctly.

\- \[ ] Decisions separated from discussions.

\- \[ ] Files committed and pushed to GitHub.



\## 7. Conclusion



A useful meeting summary must do more than record what people discussed. It must make agreed actions visible, identify ownership and deadlines, and highlight unresolved items. This prompt provides a repeatable method for turning meeting discussions into a practical action tracker without inventing missing information.

