\# Day 121 — Git Branching Strategy



\## 1. Objective



Document a simple Git branching strategy for managing changes safely in a GitHub repository.



The strategy explains how to use the main branch, feature branches, commits, merging, and branch cleanup.



The example is based on a personal learning repository used for daily Python, AI, Automation, AWS, and Git projects.



\## 2. What Is Git Branching?



A Git branch is a separate line of development.



It allows a developer to work on new changes without directly modifying the stable main branch.



For example:



\- `main`: Contains stable and approved project work.

\- `feature/day-121-branching-strategy`: Contains today's new documentation.

\- `feature/day-122-example-task`: Represents a future learning task.



\## 3. Recommended Branching Strategy



For this learning repository, use a simple feature-branch workflow.



| Branch | Purpose | Usage |

|---|---|---|

| main | Stable project branch | Store completed and approved work |

| feature/day-121-branching-strategy | New feature or task | Create today's Git branching documentation |

| feature/day-122-example-task | Future task | Example of a separate task branch |



\### Branching Rules



1\. Keep the `main` branch stable.

2\. Create a separate feature branch for new work.

3\. Make changes and test them on the feature branch.

4\. Commit changes with meaningful messages.

5\. Review the changes before merging.

6\. Merge approved changes into `main`.

7\. Push the updated `main` branch to GitHub.

8\. Delete temporary feature branches after successful merging, when no longer required.



\## 4. Git Branching Workflow



\### Step 1 — Check the current branch



Command:



`git branch`



Purpose:



Displays local branches and identifies the current branch.



\### Step 2 — Create a feature branch



Command:



`git switch -c feature/day-121-branching-strategy`



Purpose:



Creates a new branch and switches to it.



\### Step 3 — Check the active branch



Command:



`git branch`



Expected:



The active branch should be:



`feature/day-121-branching-strategy`



\### Step 4 — Create and test project files



Create the README file and review the content.



\### Step 5 — Stage and commit changes



Commands:



`git add Git/Day\_121\_Git\_Branching\_Strategy/README.md`



`git commit -m "Add Day 121 Git branching strategy documentation"`



\### Step 6 — Push the feature branch



Command:



`git push -u origin feature/day-121-branching-strategy`



Purpose:



Uploads the feature branch to GitHub.



\### Step 7 — Merge into main



After reviewing and testing the changes:



`git switch main`



`git pull origin main`



`git merge feature/day-121-branching-strategy`



\### Step 8 — Push the updated main branch



Command:



`git push origin main`



\### Step 9 — Clean up the feature branch



After confirming the merge:



`git branch -d feature/day-121-branching-strategy`



Optional remote cleanup:



`git push origin --delete feature/day-121-branching-strategy`



\## 5. Sample Branch Dataset



The following fictional example demonstrates how a development team might organise three tasks.



| Task ID | Task Name | Branch Name | Status |

|---|---|---|---|

| TASK-001 | Git Branching Strategy Documentation | feature/day-121-branching-strategy | In Progress |

| TASK-002 | Python CSV Analyzer Improvement | feature/csv-analyzer-improvement | Planned |

| TASK-003 | Procurement Report Enhancement | feature/procurement-report-enhancement | Planned |



\### Dataset Assumptions



1\. The example represents a single learning repository.

2\. The `main` branch is the stable branch.

3\. Each feature branch is created for a separate task.

4\. The sample task statuses are illustrative, not actual GitHub branch statuses.

5\. Only reviewed and approved changes should be merged into `main`.

6\. Branch names are examples and do not mean the branches already exist.



\## 6. Simple Branching Diagram



```text

main

&#x20; |

&#x20; |---- feature/day-121-branching-strategy

&#x20; |             |

&#x20; |             |---- Create README

&#x20; |             |---- Review documentation

&#x20; |             |---- Commit changes

&#x20; |             |

&#x20; |-------------|---- Merge into main

&#x20; |

&#x20; |---- feature/csv-analyzer-improvement

&#x20; |

&#x20; |---- feature/procurement-report-enhancement

```



\## 7. Benefits of This Strategy



\- Protects the stable main branch.

\- Allows independent work on different tasks.

\- Makes changes easier to review.

\- Helps track individual features.

\- Makes it easier to identify and correct mistakes.

\- Provides a clear development history.



\## 8. Important Git Commands



| Command | Purpose |

|---|---|

| `git branch` | List local branches |

| `git branch -a` | List local and remote-tracking branches |

| `git switch main` | Switch to main |

| `git switch -c branch-name` | Create and switch to a new branch |

| `git status` | Check working-tree status |

| `git add filename` | Stage a specific file |

| `git commit -m "message"` | Save a commit |

| `git merge branch-name` | Merge another branch into the current branch |

| `git push` | Upload commits |

| `git pull` | Fetch and integrate remote changes |

| `git branch -d branch-name` | Delete a merged local branch |



\## 9. Best Practices



1\. Use meaningful branch names.

2\. Keep each feature branch focused on one task.

3\. Commit changes regularly.

4\. Review changes before merging.

5\. Avoid committing incomplete work directly to `main`.

6\. Pull the latest main branch before starting new work.

7\. Do not delete a branch until its work has been merged or safely preserved.

8\. Never commit passwords, access keys, or confidential information.



\## 10. Completion Checklist



\- \[ ] Understand the purpose of Git branches.

\- \[ ] Understand the difference between main and feature branches.

\- \[ ] Create a feature branch.

\- \[ ] Create and commit the README.

\- \[ ] Push the feature branch to GitHub.

\- \[ ] Merge the feature branch into main.

\- \[ ] Verify the merge.

\- \[ ] Document the sample dataset and assumptions.



\## 11. Conclusion



A simple feature-branch strategy helps manage development work in a controlled and organised way.



For this learning repository, the recommended approach is to maintain `main` as the stable branch and create separate feature branches for new tasks.



This provides practical experience with the Git workflow commonly used in software development teams.

