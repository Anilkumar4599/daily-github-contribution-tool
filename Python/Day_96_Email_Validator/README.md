\# Day 96 - Email Address Validator



\## Objective



Create a simple Python function that validates email addresses using basic string rules.



\## Business Use Case



Email validation can be useful in:



\- Procurement systems

\- Vendor master data

\- Customer databases

\- Service management systems

\- Employee records

\- Automated email notification systems



For example, before sending a purchase order update to a vendor, an application can check whether the email address follows basic formatting rules.



\## Validation Rules



The program checks the following:



1\. Input must be a string.

2\. Email must not be empty.

3\. Email must not contain spaces.

4\. Email must contain exactly one `@` symbol.

5\. There must be text before `@`.

6\. There must be text after `@`.

7\. The domain must contain a dot.

8\. The domain must not start or end with a dot.



\## Sample Input



```text

anil@example.com

procurement@apar.com

qa.manager@company.co.in

invalid-email

user@

@example.com

user example@gmail.com

user@@example.com

user@example

