\# Git Add, Commit, Pull and Push – Day 124



\*\*Date:\*\* 04-Nov-2026  

\*\*Domain:\*\* Git \& GitHub  

\*\*Objective:\*\* Understand the purpose and practical usage of four essential Git commands.



\## 1. Introduction



Git is a version control system used to track changes in files and manage project history.



GitHub is a platform where Git repositories can be hosted and shared.



The four important commands are:



\- `git add`

\- `git commit`

\- `git pull`

\- `git push`



\## 2. Difference Between Commands



\### A. git add



\*\*Purpose:\*\* Moves selected file changes into the staging area.



Example:



`git add README.md`



Expected result: README.md is staged and ready to be committed.



\### B. git commit



\*\*Purpose:\*\* Saves staged changes as a commit in the local repository.



Example:



`git commit -m "Update README"`



Expected result: Git creates a new commit containing the staged changes.



\### C. git pull



\*\*Purpose:\*\* Fetches remote repository changes and integrates them into the current local branch.



Example:



`git pull origin main`



Expected result: Remote changes are integrated into the local main branch, provided the operation completes successfully.



\### D. git push



\*\*Purpose:\*\* Uploads local commits to the remote repository.



Example:



`git push origin main`



Expected result: Local commits are uploaded to the remote main branch, provided the push is accepted.



\## 3. Command Comparison



| Command | Main Purpose | Where It Works |

|---|---|---|

| git add | Stage changes | Local repository |

| git commit | Record changes | Local repository |

| git pull | Fetch and integrate remote changes | Remote to local |

| git push | Upload local commits | Local to remote |



\## 4. Example Input and Expected Output



\### Scenario



I updated a README.md file in my local project and want to upload the changes to GitHub.



\*\*Input – Step 1\*\*



`git status`



\*\*Expected output (illustrative):\*\*



```text

On branch main

Changes not staged for commit:

&#x20; modified: README.md

```



\*\*Input – Step 2\*\*



`git add README.md`



\*\*Expected output:\*\*



No output if successful.



\*\*Input – Step 3\*\*



`git commit -m "Update README"`



\*\*Expected output (illustrative):\*\*



```text

\[main abc1234] Update README

&#x20;1 file changed, 1 insertion(+)

```



\*\*Input – Step 4\*\*



`git push origin main`



\*\*Expected output (illustrative):\*\*



```text

To https://github.com/username/repository.git

&#x20;  oldcommit..newcommit  main -> main

```



Note: Commit IDs, file counts and remote messages are examples. Actual output depends on your repository.



\## 5. When Should I Use git pull?



Use `git pull` when:



\- Another team member has pushed changes.

\- GitHub contains commits that are not in your local branch.

\- You want to synchronize your local branch before starting work.



Example:



`git pull origin main`



Important: Review and commit or otherwise safely handle your own local changes before pulling. A pull can fail or require conflict resolution if local and remote changes overlap.



\## 6. When Should I Use git push?



Use `git push` when:



\- Your changes have been committed locally.

\- You want to publish your commits to GitHub.

\- You want your remote repository to contain your latest work.



Example:



`git push origin main`



\## 7. Practical Test Cases



\### Test Case 1 – Check working tree



Command:



`git status`



Expected result: Git displays the current branch and any modified or staged files.



\### Test Case 2 – Check commit history



Command:



`git log -5 --oneline`



Expected result: Git displays up to five recent commits.



\### Test Case 3 – Check remote configuration



Command:



`git remote -v`



Expected result: Git displays the configured remote repository URLs.



\### Test Case 4 – Check current branch



Command:



`git branch`



Expected result: Git displays local branches and marks the current branch with an asterisk.



\## 8. My Daily Git Workflow



1\. Check the repository using `git status`.

2\. Pull remote changes when required.

3\. Create or update project files.

4\. Test or review the changes.

5\. Stage selected files using `git add`.

6\. Save changes using `git commit`.

7\. Upload commits using `git push`.

8\. Verify the result using `git status` and `git log`.



\## 9. Learning Summary



\- `git add` prepares selected changes.

\- `git commit` records changes locally.

\- `git pull` brings remote changes into the local branch.

\- `git push` uploads local commits to the remote repository.



\*\*Day 124 Outcome:\*\* Understand the difference between staging, committing, pulling and pushing, and apply these commands in everyday GitHub work.

