#!/usr/bin/env python3
"""
Daily GitHub Contribution Tool
A small, honest daily practice system for building useful GitHub activity.

Usage:
    python daily_github.py
    python daily_github.py --status
    python daily_github.py --complete
    python daily_github.py --open
"""

from pathlib import Path
from datetime import date
import argparse
import json
import subprocess

ROOT = Path(__file__).resolve().parent
TASKS_FILE = ROOT / "tasks.json"
LOG_FILE = ROOT / "daily_log.json"


def load_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path, data):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def today_task(tasks, log):
    today = date.today().isoformat()
    if today in log:
        return log[today]["task_id"]
    # Rotate through the 200-task bank by calendar day.
    day_number = date.today().toordinal()
    return ((day_number - 1) % len(tasks)) + 1


def show_status(tasks, log):
    today = date.today().isoformat()
    tid = today_task(tasks, log)
    task = tasks[tid - 1]
    done = today in log and log[today].get("completed", False)

    print("\n=== DAILY GITHUB CONTRIBUTION ===")
    print(f"Date   : {today}")
    print(f"Task   : #{task['id']}")
    print(f"Domain : {task['domain']}")
    print(f"Work   : {task['task']}")
    print(f"Check  : {task['quality_check']}")
    print(f"Status : {'COMPLETED' if done else 'NOT COMPLETED'}")
    print("\nSuggested workflow:")
    print("  1. Create/update a file for today's work.")
    print("  2. Test it or review the result.")
    print("  3. git add .")
    print('  4. git commit -m "Day: daily learning task"')
    print("  5. git push")
    print()


def complete_task(tasks, log):
    today = date.today().isoformat()
    tid = today_task(tasks, log)
    task = tasks[tid - 1]
    log[today] = {
        "task_id": tid,
        "domain": task["domain"],
        "task": task["task"],
        "completed": True
    }
    save_json(LOG_FILE, log)
    print(f"Marked today's task #{tid} as complete.")
    print("Now commit the actual work to GitHub when ready.")


def run_git(args):
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False
        )
        print(result.stdout or result.stderr)
    except FileNotFoundError:
        print("Git was not found. Install Git and make sure 'git' works in Git Bash.")


def main():
    parser = argparse.ArgumentParser(description="Daily GitHub Contribution Tool")
    parser.add_argument("--status", action="store_true", help="Show today's task")
    parser.add_argument("--complete", action="store_true", help="Mark today's task complete")
    parser.add_argument("--open", action="store_true", help="Show Git status")
    args = parser.parse_args()

    tasks = load_json(TASKS_FILE, [])
    log = load_json(LOG_FILE, {})

    if not tasks:
        print("tasks.json is missing or empty.")
        return

    if args.complete:
        complete_task(tasks, log)
    elif args.open:
        run_git(["status"])
    else:
        show_status(tasks, log)


if __name__ == "__main__":
    main()
