\# Git Cheat Sheet – Day 123



\*\*Date:\*\* 03-Nov-2026  

\*\*Learning Domain:\*\* Git \& GitHub  

\*\*Purpose:\*\* Personal reference for everyday Git operations.



\## 1. Git Basics



| Command | Purpose |

|---|---|

| `git --version` | Check Git version |

| `git config --list` | View Git configuration |

| `git status` | Check working tree status |

| `git help` | Open Git help |

| `pwd` | Check current directory |



\## 2. Repository Management



| Command | Purpose |

|---|---|

| `git init` | Initialize a new repository |

| `git clone URL` | Copy a remote repository |

| `git remote -v` | View remote repositories |

| `git remote add origin URL` | Add a remote repository |

| `git fetch origin` | Download remote updates without merging |

| `git pull` | Fetch and integrate remote changes |

| `git push` | Upload local commits |



\## 3. Daily Git Workflow



| Command | Purpose |

|---|---|

| `git status` | Check modified files |

| `git add filename` | Stage a specific file |

| `git add file1 file2` | Stage selected files |

| `git diff` | View unstaged changes |

| `git diff --cached` | View staged changes |

| `git diff --cached --check` | Check staged changes for whitespace errors |

| `git commit -m "message"` | Save staged changes |

| `git log --oneline` | View compact commit history |

| `git push origin main` | Push main branch to GitHub |



\*\*Best practice:\*\* Stage only the files you intend to commit. Avoid `git add .` when you have not reviewed all repository changes.



\## 4. Branch Management



| Command | Purpose |

|---|---|

| `git branch` | List local branches |

| `git branch -a` | List local and remote branches |

| `git switch -c feature/task-name` | Create and switch to a new branch |

| `git switch main` | Switch to main |

| `git branch -d branch-name` | Delete a merged local branch |

| `git push -u origin branch-name` | Push a branch and set upstream |

| `git push origin --delete branch-name` | Delete a remote branch |



\## 5. Merge Operations



| Command | Purpose |

|---|---|

| `git merge branch-name` | Merge another branch into current branch |

| `git merge --abort` | Abort an ongoing merge |

| `git status` | Check merge status |

| `git log --oneline --graph --all` | View branch and merge history |



\*\*Remember:\*\* Switch to the target branch (usually `main`) before merging a feature branch.



\## 6. Undo and Recovery



| Command | Purpose |

|---|---|

| `git restore filename` | Discard unstaged changes in a file |

| `git restore --staged filename` | Unstage a file |

| `git show HEAD` | View latest commit details |

| `git show HEAD\~1:filename` | View a file from the previous commit |

| `git revert commit-id` | Create a new commit that reverses an earlier commit |



\*\*Warning:\*\* `git restore filename` discards uncommitted changes to that file. Review your work before using it.



\## 7. Useful Inspection Commands



| Command | Purpose |

|---|---|

| `git log -5 --oneline` | View the last five commits |

| `git show --stat` | View latest commit summary |

| `git diff main..branch-name` | Compare two branches |

| `git status -sb` | Short branch and status view |

| `git ls-files` | List tracked files |



\## 8. Recommended Daily Git Workflow



1\. Navigate to the repository root.

2\. Run `git status`.

3\. Create or update your project files.

4\. Test your work.

5\. Run `git diff` or inspect the files.

6\. Stage only the required files.

7\. Run `git diff --cached --check`.

8\. Commit your changes.

9\. Push your commit to GitHub.

10\. Verify with `git status` and `git log -1 --oneline`.



\## 9. Practical Test Cases



\### Test Case 1 – Check repository status



Command:



`git status`



Expected result: Git displays the current branch and working tree status.



\### Test Case 2 – Check commit history



Command:



`git log -5 --oneline`



Expected result: Git displays up to five recent commits in compact format.



\### Test Case 3 – Check branch information



Command:



`git branch -a`



Expected result: Git displays available local and remote branches.



\### Test Case 4 – Check staged changes



Command:



`git diff --cached --check`



Expected result: No output when there are no staged whitespace errors. If no files are staged, this command also produces no output.



\## 10. My Learning Notes



\- Git is a version control system.

\- GitHub is a platform for hosting Git repositories.

\- A commit records staged changes.

\- A branch allows independent development.

\- A merge combines work from different branches.

\- A remote repository is a version hosted on a service such as GitHub.



\*\*Day 123 Goal:\*\* Build a personal Git reference that can be reused during daily project work.

