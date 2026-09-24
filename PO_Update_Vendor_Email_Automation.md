\# Day 83 — PO Update to Vendor Email Automation



\## 1. Automation Idea



\*\*Idea Name:\*\* PO Update in Excel → Automatically Prepare and Send Vendor Email



\*\*Department:\*\* Procurement



\*\*Business Area:\*\* Purchase Order Management



\*\*Automation Type:\*\* Email notification based on updated procurement data



\*\*Status:\*\* Proposed — documentation and test-case design only



\---



\## 2. Business Problem



Procurement teams regularly update Purchase Order (PO) information and

communicate changes to vendors.



The current process may involve:



1\. Opening the PO tracking Excel file.

2\. Updating the PO quantity, delivery date, or other details.

3\. Identifying which vendor needs to be informed.

4\. Manually drafting an email.

5\. Checking the email details.

6\. Sending the email to the vendor.

7\. Updating the communication record.



Manual communication can take time and may lead to missed updates,

incorrect email details, or delays in informing vendors.



\---



\## 3. Proposed Automation



Create an automation that detects an eligible PO update in an Excel

tracking file and prepares a vendor notification.



After the required validation and approval checks, the automation can

send the email and record the communication status.



\### Proposed Workflow



1\. Procurement updates a PO record in Excel.

2\. The automation identifies the updated record.

3\. It validates mandatory fields.

4\. It checks whether the change requires vendor notification.

5\. It retrieves the approved vendor email address.

6\. It prepares an email containing the relevant PO details.

7\. If approval is required, the email waits for authorized approval.

8\. Once approved, the email is sent.

9\. The system records the email status, date, and PO reference.

10\. Failed or invalid records are flagged for manual review.



\---



\## 4. Required Input Data



| Field | Description | Mandatory |

|---|---|---|

| PO Number | Unique purchase order reference | Yes |

| Vendor Name | Name of the supplier | Yes |

| Vendor Email | Approved email address for the supplier | Yes |

| Item Description | Description of the ordered item | Yes |

| Quantity | Ordered quantity | Yes |

| Revised Delivery Date | Updated expected delivery date | Yes |

| Change Type | Type of PO change | Yes |

| Approval Status | Whether required approval has been obtained | Yes |

| Notification Status | Whether the vendor has already been notified | Yes |



\---



\## 5. Sample Input Dataset



The following data is fictional and is intended only for testing the

proposed workflow.



| PO Number | Vendor | Vendor Email | Item | Quantity | Revised Delivery Date | Change Type | Approval Status | Notification Status |

|---|---|---|---|---:|---|---|---|---|

| PO-1001 | ABC Electronics | abc@example.com | Camera Module | 20 | 2026-10-05 | Delivery Date Change | Approved | Not Sent |

| PO-1002 | XYZ Systems | xyz@example.com | Router | 10 | 2026-10-08 | Quantity Change | Pending | Not Sent |

| PO-1003 | Secure Devices Ltd | secure@example.com | NVR | 5 | 2026-10-12 | Delivery Date Change | Approved | Sent |



Note: The example.com addresses are illustrative and must not be treated

as actual vendor contact details.



\---



\## 6. Sample Email Template



\*\*Subject:\*\* PO Update Notification — \[PO Number]



Dear \[Vendor Name],



Please note the following update to our Purchase Order.



PO Number: \[PO Number]



Item Description: \[Item Description]



Updated Quantity: \[Quantity]



Revised Delivery Date: \[Revised Delivery Date]



Change Type: \[Change Type]



Kindly review the updated information and confirm receipt.



Regards,



Procurement Team



\---



\## 7. Input Validation Rules



Before preparing or sending an email, the automation should validate:



1\. PO Number must not be blank.

2\. Vendor Name must not be blank.

3\. Vendor Email must not be blank and must follow the configured email format.

4\. Item Description must not be blank.

5\. Quantity must be a positive number.

6\. Revised Delivery Date must be a valid date.

7\. Change Type must be selected from an approved list.

8\. Approval Status must be Approved if approval is required.

9\. A PO update already notified to the vendor must not trigger a duplicate email.

10\. Invalid or incomplete records must be flagged for manual review.



\---



\## 8. Test Cases



\### Test Case 1 — Valid Approved PO Update



\*\*Input:\*\*

\- PO Number: PO-1001

\- Vendor Email: abc@example.com

\- Quantity: 20

\- Revised Delivery Date: 2026-10-05

\- Approval Status: Approved

\- Notification Status: Not Sent



\*\*Expected Result:\*\*

\- Record passes validation.

\- Email is prepared with the correct PO details.

\- Email is eligible to be sent according to the configured workflow.

\- Notification status is updated after successful sending.



\*\*Purpose:\*\* Verify the normal successful workflow.



\---



\### Test Case 2 — Missing Vendor Email



\*\*Input:\*\*

\- PO Number: PO-1004

\- Vendor Email: Blank

\- Approval Status: Approved

\- Notification Status: Not Sent



\*\*Expected Result:\*\*

\- Record fails validation.

\- No email is sent.

\- The record is flagged for manual correction.



\*\*Purpose:\*\* Prevent notifications from being sent without a valid recipient.



\---



\### Test Case 3 — Approval Pending



\*\*Input:\*\*

\- PO Number: PO-1002

\- Vendor Email: xyz@example.com

\- Approval Status: Pending

\- Notification Status: Not Sent



\*\*Expected Result:\*\*

\- Record is identified as awaiting approval.

\- Email is not sent while required approval is pending.

\- The record remains available for follow-up.



\*\*Purpose:\*\* Ensure approval controls are respected.



\---



\### Test Case 4 — Duplicate Notification



\*\*Input:\*\*

\- PO Number: PO-1003

\- Approval Status: Approved

\- Notification Status: Sent



\*\*Expected Result:\*\*

\- Automation identifies that the notification has already been sent.

\- No duplicate email is sent for the same change.

\- Existing communication history is retained.



\*\*Purpose:\*\* Avoid unnecessary repeated vendor notifications.



\---



\### Test Case 5 — Invalid Quantity



\*\*Input:\*\*

\- PO Number: PO-1005

\- Vendor Email: vendor@example.com

\- Quantity: -5

\- Approval Status: Approved

\- Notification Status: Not Sent



\*\*Expected Result:\*\*

\- Record fails quantity validation.

\- No email is sent.

\- The record is flagged for correction.



\*\*Purpose:\*\* Prevent invalid PO data from being communicated.



\---



\## 9. Expected Benefits



Potential benefits of implementing this automation include:



\- Reduced manual email preparation.

\- Faster communication of approved PO changes.

\- More consistent email formatting.

\- Fewer missed vendor notifications.

\- Better tracking of communication status.

\- Improved visibility of failed or pending notifications.



These are expected benefits, not measured results. They would need to be

verified after implementation.



\---



\## 10. Risks and Controls



| Risk | Proposed Control |

|---|---|

| Incorrect vendor email | Use an approved vendor master and validate recipient details. |

| Incorrect PO information | Validate mandatory fields and compare with the approved PO record. |

| Unauthorized communication | Apply approval requirements before sending. |

| Duplicate email | Track notification status and use a unique change reference. |

| Email delivery failure | Record failures and provide a manual follow-up process. |

| Accidental disclosure | Include only the information required by the vendor and follow company policy. |



\---



\## 11. Assumptions



1\. Excel is used as the source for PO tracking.

2\. Vendor contact details are maintained in an approved source.

3\. Only authorized personnel can approve PO changes where approval is required.

4\. The automation can reliably identify a new or changed PO record.

5\. Each notification can be associated with a unique PO change reference.

6\. Email sending will use a company-approved email service.

7\. The sample records and email addresses are fictional.

8\. No actual email has been sent as part of this documentation exercise.

9\. No time or cost savings have been measured.

10\. The final implementation method will depend on company systems, security,

&#x20;   approval rules, and available tools.



\---



\## 12. Possible Implementation Approach



A future implementation could use:



\- Excel as the PO tracking source.

\- Power Automate or an approved automation platform to detect changes.

\- An approved email service to send notifications.

\- An approval step for changes requiring authorization.

\- A log or tracking table to record notification results.



The selected tools and integration method must be confirmed before

implementation.



\---



\## 13. Conclusion



This automation idea proposes a controlled process for notifying vendors

about eligible Purchase Order updates.



Input validation, approval checks, duplicate prevention, and communication

logging are important controls.



The current deliverable is a documented proposal with sample data and

test cases. Practical implementation and testing remain future activities.



\*\*End of Day 83 documentation.\*\*

