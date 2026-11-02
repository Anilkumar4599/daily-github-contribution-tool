\# Day 122 — Git Feature Branch Validation



\## 1. Project Overview



This project demonstrates a simple Git branch-name validation program using Python.



The program checks whether a proposed branch name follows the recommended naming convention before the user creates the branch.



\## 2. Branch Naming Convention



Accepted formats:



\- `feature/task-name`

\- `bugfix/issue-name`

\- `docs/documentation-name`

\- `hotfix/fix-name`



Rules:



1\. Use lowercase letters.

2\. Use a supported prefix.

3\. Separate words with hyphens.

4\. Do not leave the task name empty.

5\. Do not use spaces or special characters.



\## 3. Project Files



| File | Purpose |

|---|---|

| branch\_validator.py | Validates a user-provided branch name |

| test\_branch\_validator.py | Tests valid and invalid branch names |

| README.md | Documents the project and Git commands |



\## 4. How to Run



From the project folder:



```bash

python branch\_validator.py

```



Example input:



```text

feature/day-122-branch-validation

```



Expected output:



```text

Valid branch name.

Accepted branch: feature/day-122-branch-validation

```



\## 5. Run the Tests



```bash

python -m unittest -v test\_branch\_validator.py

```



Expected result: All five tests pass.



\## 6. Git Feature Branch Workflow



\### Step 1 — Check the current branch



```bash

git branch

```



\### Step 2 — Create a feature branch



```bash

git switch -c feature/day-122-branch-validation

```



\### Step 3 — Stage the project files



```bash

git add Git/Day\_122\_Feature\_Branch\_Validation/branch\_validator.py

git add Git/Day\_122\_Feature\_Branch\_Validation/test\_branch\_validator.py

git add Git/Day\_122\_Feature\_Branch\_Validation/README.md

```



\### Step 4 — Commit the changes



```bash

git commit -m "Add Day 122 feature branch validation"

```



\### Step 5 — Push the feature branch



```bash

git push -u origin feature/day-122-branch-validation

```



\### Step 6 — Merge into main



```bash

git switch main

git pull origin main

git merge feature/day-122-branch-validation

git push origin main

```



\### Step 7 — Delete the local feature branch



```bash

git branch -d feature/day-122-branch-validation

```



\## 7. Assumptions and Limitations



\- The program validates branch names against a simple naming convention.

\- It does not check whether a branch already exists in the repository.

\- It does not create, switch, push, or merge Git branches automatically.

\- Branch names are checked locally without accessing GitHub.

\- The five tests cover basic valid and invalid inputs.



\## 8. Learning Outcome



Learned how to validate user input in Python and practise a feature-branch workflow using Git commands.



The project combines basic Python programming, input validation, testing, documentation, and Git version control.

