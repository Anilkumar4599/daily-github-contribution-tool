\# Day 127 – Git Recovery Practice



\## Objective



Understand how to recover from accidental local changes using Git and validate recovery inputs using Python.



\## Files



\- `git\_recovery\_helper.py` – Input validation helper.

\- `test\_git\_recovery\_helper.py` – Automated unit tests.

\- `recovery\_demo.txt` – Sample file used for Git restore practice.

\- `README.md` – Project documentation.



\## Git Commands Covered



| Command | Purpose |

|---|---|

| `git status` | Identify changes |

| `git diff` | Inspect modifications |

| `git restore filename` | Discard unstaged modifications |

| `git restore --staged filename` | Unstage a file |

| `git revert commit-id` | Safely reverse an earlier commit |



\## Input Validation



The Python helper validates:



1\. Supported recovery action.

2\. Empty action.

3\. Empty filename.

4\. Folder paths entered instead of a filename.



\## Test Cases



Five automated tests:



\- Valid restore action.

\- Valid unstage action.

\- Invalid recovery action.

\- Empty filename.

\- Folder path rejection.



\## Practical Git Recovery



1\. Commit an original sample file.

2\. Modify the file accidentally.

3\. Inspect the changes using `git diff`.

4\. Restore the file using `git restore`.

5\. Verify that the original committed content is recovered.



\## Assumptions



\- The practice is performed in a Git repository.

\- The sample file has already been committed.

\- The demonstration covers unstaged changes.

\- `git restore` discards the specified unstaged changes.

\- The Python helper validates inputs only; it does not execute Git commands.



\## Learning Outcome



Understand how to inspect, validate and safely recover accidental local changes using Git.



\*\*Day 127 – Git Recovery Practice\*\*

