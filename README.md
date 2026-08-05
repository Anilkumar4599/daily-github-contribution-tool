# Daily GitHub Contribution Tool

A simple Python-based system to help you build **consistent, meaningful GitHub activity** while learning Python, AI, automation, QC, inventory, Power BI, AWS and Git.

## What it does

Every day it gives you one practical task from a 200-task bank.

The goal is not to create fake commits. The goal is:

**Learn → Build something small → Test/review → Commit → Push**

## Folder

Keep this project as a GitHub repository, for example:

`daily-github-contribution-tool`

## Requirements

- Python 3
- Git
- GitHub account
- Git Bash on Windows is fine

No Python packages are required.

## First run

Open Git Bash in this folder:

```bash
python daily_github.py
```

You will see today's task.

## Useful commands

Show today's task:

```bash
python daily_github.py
```

Mark today's task complete:

```bash
python daily_github.py --complete
```

Check Git status:

```bash
python daily_github.py --open
```

## Recommended daily Git workflow

After completing the task:

```bash
git status
git add .
git commit -m "Day: daily learning task"
git push
```

## Recommended repository structure

```text
daily-github-contribution-tool/
│
├── daily_github.py
├── tasks.json
├── daily_log.json
└── README.md
```

The `daily_log.json` file is created automatically after the first completion.

## Suggested GitHub portfolio repositories

As you progress, separate your work into focused repositories:

- python-automation
- ai-learning
- ai-prompts
- procurement-automation
- qc-automation
- inventory-automation
- powerbi-projects
- aws-projects

This makes your contribution history useful as a portfolio rather than just a green graph.

## Important

Do not create empty commits just to increase the contribution count.

A small genuine activity is enough: a script improvement, README update, test, data analysis, prompt collection, documentation update, or mini-project.

## 30-minute daily rule

If you are busy:

- 5 min — read the task
- 20 min — build
- 5 min — test/document/commit

Consistency matters more than complexity.
