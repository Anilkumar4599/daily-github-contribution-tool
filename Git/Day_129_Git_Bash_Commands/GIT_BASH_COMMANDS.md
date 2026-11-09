# 10 Useful Git Bash Commands – Day 129



**Date:** 09-Nov-2026  

**Domain:** Git Bash



## Objective



Document 10 useful Git Bash commands with practical examples and expected outputs.



## 1. pwd – Display Current Directory



**Purpose:** Displays the current working directory.



**Example:**

```bash

pwd

```



**Expected output:**



Displays the full path of the current folder, ending with:



`/Git/Day_129_Git_Bash_Commands`



The exact path depends on the computer.



## 2. ls -la – List Files and Directories



**Purpose:** Displays files and folders, including hidden entries.



**Example:**

```bash

ls -la

```



**Expected output:**



A directory listing containing entries such as:



```text

GIT_BASH_COMMANDS.md

README.md

sample_workspace/

```



File permissions, sizes and timestamps may vary.



## 3. cd – Change Directory



**Purpose:** Moves from the current directory to another directory.



**Example:**

```bash

cd sample_workspace

pwd

```



**Expected output:**



The displayed path ends with:



`/Day_129_Git_Bash_Commands/sample_workspace`



## 4. mkdir -p – Create a Directory



**Purpose:** Creates a directory and any missing parent directories.



**Example:**

```bash

mkdir -p reports

ls -d reports

```



**Expected output:**

```text

reports

```



## 5. touch – Create an Empty File



**Purpose:** Creates a new empty file if it does not exist.



**Example:**

```bash

touch empty.txt

ls -l empty.txt

```



**Expected output:**



The file is displayed with a size of zero bytes.



Exact permissions and timestamps may vary.



## 6. cat – Display File Contents



**Purpose:** Displays the contents of a text file.



**Example:**

```bash

cat notes.txt

```



**Expected output:**

```text

PO follow-up required

Supplier confirmation pending

Dispatch date: 12-Nov-2026

```



## 7. cp – Copy a File



**Purpose:** Creates a copy of an existing file.



**Example:**

```bash

cp notes.txt notes_backup.txt

ls notes_backup.txt

```



**Expected output:**

```text

notes_backup.txt

```



The original file remains unchanged.



## 8. mv – Move or Rename a File



**Purpose:** Moves a file or changes its name.



**Example:**

```bash

mv notes_backup.txt archive_notes.txt

ls archive_notes.txt

```



**Expected output:**

```text

archive_notes.txt

```



The original backup filename is no longer present.



## 9. grep -n – Search Text with Line Numbers



**Purpose:** Searches for a specific word or phrase inside a file and displays matching line numbers.



**Example:**

```bash

grep -n "PO" notes.txt

```



**Expected output:**

```text

1:PO follow-up required

```



## 10. find – Search for Files



**Purpose:** Finds files and directories within a specified location.



**Example:**

```bash

find . -type f

```



**Expected output:**



```text

./notes.txt

./empty.txt

./archive_notes.txt

```



The order of the results may vary.



## Important Notes



\- `cp` and `mv` can overwrite an existing destination file. Check before running them.

\- `touch` updates the timestamp if the file already exists.

\- `mkdir -p` does not report an error if the directory already exists.

\- `find . -type f` searches recursively for files under the current directory.

\- Git Bash supports many familiar Unix/Linux commands on Windows.



## Learning Summary



Today I practised 10 useful Git Bash commands that help with:



1\. Navigating folders.

2\. Creating files and directories.

3\. Reading and searching files.

4\. Copying and renaming files.

5\. Locating files in a project.



**Day 129 Outcome:** Created a reusable Git Bash command reference with practical examples and expected outputs.

