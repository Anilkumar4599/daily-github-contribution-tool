\# Day 116 — Procurement Risk Analysis Prompt



\## Project Overview



A reusable AI prompt for identifying procurement risks from PO and supplier data while handling missing information transparently.



\## Business Applications



\- Overdue purchase orders

\- Supplier delivery follow-up

\- Potential stock shortages

\- QC and receiving exceptions

\- Supplier risk review

\- Procurement management reporting



\## Project Files



\- `Procurement\_Risk\_Analysis\_Prompt.md` — Prompt, sample data, assumptions, expected output, and three test cases.

\- `README.md` — Project overview and usage instructions.



\## How to Use



1\. Provide the purchase-order dataset and reporting date.

2\. Validate the input data.

3\. Run the reusable prompt with the available records.

4\. Separate confirmed exceptions from potential risks and unknowns.

5\. Verify important dates, quantities, and values.

6\. Follow up on missing information.

7\. Share the final report only after appropriate review.



\## Three Test Cases



1\. Identify an overdue PO and calculate overdue days correctly.

2\. Flag a missing due date without inventing overdue days.

3\. Identify a potential stock gap without claiming an unconfirmed stock-out.



\## Key Safeguard



Never invent supplier explanations, stock quantities, delivery commitments, business impact, or financial losses.



\## Completion Checklist



\- \[ ] Prompt file created.

\- \[ ] README created.

\- \[ ] Sample assumptions documented.

\- \[ ] All three test cases reviewed.

\- \[ ] Files committed and pushed.

\- \[ ] Daily tracker updated.



\## Limitations



The sample data is fictional. AI recommendations are decision support and must be checked against actual procurement, inventory, supplier, and receiving records.



