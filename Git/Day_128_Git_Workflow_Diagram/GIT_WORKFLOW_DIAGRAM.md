\# Git Workflow Diagram – Day 128



\*\*Date:\*\* 08-Nov-2026  

\*\*Domain:\*\* Git \& GitHub



\## 1. Objective



Create a visual Git workflow diagram using Markdown and Mermaid.



\## 2. Basic Git Workflow



The following diagram explains how changes move from a local working directory to GitHub.



```mermaid

flowchart TD

&#x20;   A\[Working Directory] --> B\[git add]

&#x20;   B --> C\[Staging Area]

&#x20;   C --> D\[git commit]

&#x20;   D --> E\[Local Repository]

&#x20;   E --> F\[git push]

&#x20;   F --> G\[Remote Repository - GitHub]

```



\## 3. Git Pull Workflow



Use git pull to retrieve and integrate remote changes into your local branch.



```mermaid

flowchart TD

&#x20;   A\[GitHub Remote Repository] --> B\[git pull]

&#x20;   B --> C\[Local Repository]

&#x20;   C --> D\[Working Directory]

```



\## 4. Complete Team Collaboration Workflow



```mermaid

flowchart TD

&#x20;   A\[Start] --> B\[Check git status]

&#x20;   B --> C\[Create or Modify Files]

&#x20;   C --> D\[Review Changes]

&#x20;   D --> E\[git add]

&#x20;   E --> F\[git commit]

&#x20;   F --> G\[git push]

&#x20;   G --> H\[GitHub Repository]

&#x20;   H --> I{Remote Updates Available?}

&#x20;   I -->|Yes| J\[git pull]

&#x20;   I -->|No| K\[Continue Development]

&#x20;   J --> K

```



\## 5. Command Reference



| Command | Purpose |

|---|---|

| git status | Check repository changes |

| git add | Stage selected files |

| git commit | Record changes locally |

| git push | Upload commits to GitHub |

| git pull | Fetch and integrate remote changes |

| git log | View commit history |



\## 6. Practical Test Cases



\### Test Case 1 – Markdown file exists



Command:



`ls -l GIT\_WORKFLOW\_DIAGRAM.md`



Expected result: The Markdown file is displayed.



\### Test Case 2 – Mermaid diagrams exist



Command:



grep -c '^```mermaid$' GIT_WORKFLOW_DIAGRAM.md


Expected result:



`3`



\### Test Case 3 – Required Git commands are documented



Command:



`grep -E 'git add|git commit|git push|git pull' GIT\_WORKFLOW\_DIAGRAM.md`



Expected result: The four Git commands appear in the documentation.



\### Test Case 4 – Markdown headings exist



Command:



`grep '^## ' GIT\_WORKFLOW\_DIAGRAM.md`



Expected result: The document sections are displayed.



\## 7. Learning Summary



\- A Git workflow diagram visually explains the movement of code changes.

\- Mermaid allows diagrams to be written using text.

\- Markdown makes technical documentation easy to maintain.

\- Git workflow documentation is useful for developers and DevOps teams.



\*\*Day 128 Outcome:\*\* Create and maintain a reusable Git workflow diagram in Markdown.

