# Installation and Execution Guide

# QA Jira MCP Agent Framework

This guide explains how to clone the repository, install dependencies, configure environment variables, and run each version of the QA Jira MCP Agent.

# 1. Prerequisites

Before running this project, install:

* Python 3.11 or above
* Git
* VS Code
* Jira Cloud account
* Jira API token
* GitHub Models token

# 2. Clone the Repository

Open VS Code Terminal or PowerShell.

```bash
cd C:\GIT\qa_mcp_series
```

Clone the repository:

```bash
git clone https://github.com/palaneelam/qa-jira-mcp-agent.git
```

Move inside the project:

```bash
cd QA_JIRA_MCP_Agent
```


# 3. Open Project in VS Code

Open manually:

```text
File → Open Folder → QA_JIRA_MCP_Agent
```

# 4. Create Virtual Environment

From project root:

```bash
python -m venv .venv
```

Activate virtual environment:

```bash
.venv\Scripts\activate
```

Expected terminal:

```text
(.venv) PS C:\GIT\qa_mcp_series\QA_JIRA_MCP_Agent>
```

# 5. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

# 6. Create `.env` File

Create a file named:

```text
.env
```

Place it in the project root.

Add:

```env
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your_jira_api_token
GITHUB_TOKEN=your_github_models_token
```

Important:

* Do not add quotes.
* Do not add spaces around `=`.
* Do not commit `.env` to GitHub.

# 7. Recommended Execution Rule

Always run every version using:

```bash
python -m folder_name.main
```

Do not run:

```bash
python folder_name/main.py
```

Wrong:

```bash
python .\v1_single_story_testcases\main.py
```

Correct:

```bash
python -m v1_single_story_testcases.main
```

# 8. Version 1 - Single Story Test Case Generator

## Purpose

Version 1 reads one Jira story and generates test cases.

## Run Command

```bash
python -m v1_single_story_testcases.main
```

Expected menu:

```text
QA Jira MCP Agent

1. Show Available MCP Tools
2. Read Jira Issue
3. Generate Test Cases from Jira Issue
0. Exit
```
## Step 1: Show Available MCP Tools

Select:

```text
1
```

Expected output:

```text
Available MCP Tools:
- read_jira_issue
- generate_test_cases_from_jira
```

## Step 2: Read Jira Issue

Select:

```text
2
```

Enter issue key:

```text
SCRUM-9
```

Expected output:

```text
Jira Issue Details:
{
  "issue_key": "SCRUM-9",
  "summary": "...",
  "description": "...",
  "status": "...",
  "priority": "..."
}
```

## Step 3: Generate Test Cases

Select:

```text
3
```

Enter issue key:

```text
SCRUM-9
```

Expected output:

```text
Generating test cases from Jira issue...
Test cases generated successfully.
```

Generated file location:

```text
v1_single_story_testcases/output/
```

# 9. Version 2 - Single Story QA Workbook

## Purpose

Version 2 generates a complete workbook for one Jira story.

Workbook may include:

* Story details
* Test scenarios
* Test cases
* Positive cases
* Negative cases
* Boundary cases

## Run Command

```bash
python -m v2_single_story_workbook.main
```

Expected menu:

```text
QA Jira MCP Agent - Version 2

1. Show Available MCP Tools
2. Read Jira Issue
3. Generate Story QA Workbook
0. Exit
```

## Generate Workbook

Select:

```text
3
```

Enter Jira Issue Key:

```text
SCRUM-9
```

Expected output:

```text
Generating QA workbook...
Workbook generated successfully.
```

Generated file location:

```text
v2_single_story_workbook/output/
```

# 10. Version 3 - Multiple Stories Workbook

## Purpose

Version 3 processes multiple Jira stories and generates a combined QA workbook.

## Run Command

```bash
python -m v3_multiple_stories_workbook.main
```

Expected menu:

```text
QA Jira MCP Agent - Version 3

1. Show Available MCP Tools
2. Search Jira Issues by JQL
3. Generate Multiple Stories Workbook
0. Exit
```

## Search Jira Issues

Select:

```text
2
```

Enter JQL:

```sql
project = SCRUM ORDER BY created DESC
```

Max results:

```text
5
```

Expected output:

```text
SCRUM-9 - Apply Discount Coupon During Checkout
SCRUM-8 - ...
SCRUM-7 - ...
```

## Generate Workbook

Select:

```text
3
```

Enter JQL:

```sql
project = SCRUM ORDER BY created DESC
```

Max results:

```text
5
```

Expected output:

```text
Generating workbook for multiple stories...
Workbook generated successfully.
```

Generated file location:

```text
v3_multiple_stories_workbook/output/
```

# 11. Version 4 - Sprint QA Agent

## Purpose

Version 4 generates a Sprint QA Workbook using Jira JQL.

It can search sprint stories and generate QA artifacts for the complete sprint.

## Run Command

```bash
python -m v4_sprint_qa_agent.main
```

Expected menu:

```text
QA Jira MCP Agent - Version 4

1. Show Available MCP Tools
2. Search Jira Issues by JQL
3. Generate Sprint QA Workbook
0. Exit
```

## Step 1: Show Available Tools

Select:

```text
1
```

Expected output:

```text
Available MCP Tools:
- search_issues_by_jql
- generate_sprint_qa_workbook
```

## Step 2: Search Sprint Issues

Select:

```text
2
```

Enter JQL:

```sql
project = SCRUM AND sprint in openSprints() ORDER BY created DESC
```

Max results:

```text
5
```

Expected output:

```text
SCRUM-9 - Apply Discount Coupon During Checkout
SCRUM-8 - ...
SCRUM-7 - ...
```

## Step 3: Generate Sprint QA Workbook

Select:

```text
3
```

Enter JQL:

```sql
project = SCRUM AND sprint in openSprints() ORDER BY created DESC
```

Max results:

```text
5
```

Expected output:

```text
Generating Sprint QA Workbook...
Workbook generated successfully.
```

Generated file location:

```text
v4_sprint_qa_agent/output/
```

# 12. Useful JQL Examples

All issues from project:

```sql
project = SCRUM ORDER BY created DESC
```

Only stories:

```sql
project = SCRUM AND issuetype = Story ORDER BY created DESC
```

Open sprint:

```sql
project = SCRUM AND sprint in openSprints() ORDER BY created DESC
```

Specific status:

```sql
project = SCRUM AND status = "To Do" ORDER BY created DESC
```

Specific assignee:

```sql
project = SCRUM AND assignee is not EMPTY ORDER BY created DESC
```



# 13. Screenshot Checklist

Add these screenshots to your documentation:

```text
docs/screenshots/
│
├── clone-repository.png
├── open-project-vscode.png
├── activate-venv.png
├── install-requirements.png
├── env-file.png
│
├── v1-main-menu.png
├── v1-show-tools.png
├── v1-read-jira-issue.png
├── v1-generate-testcases.png
│
├── v2-main-menu.png
├── v2-generate-workbook.png
│
├── v3-main-menu.png
├── v3-search-jira-issues.png
├── v3-generate-workbook.png
│
├── v4-main-menu.png
├── v4-show-tools.png
├── v4-search-sprint.png
└── v4-generate-sprint-workbook.png
```



# 14. How to Take VS Code Terminal Screenshots

Recommended approach:

1. Open VS Code.
2. Open Terminal.
3. Run the required command.
4. Make sure the command and output are visible.
5. Use Windows Snipping Tool.
6. Save the image inside:

```text
docs/screenshots/
```

Use clear file names.

Example:

```text
v4-search-sprint.png
```


# 15. Common Execution Mistakes

## Mistake 1: Running main.py Directly

Wrong:

```bash
python .\v1_single_story_testcases\main.py
```

Correct:

```bash
python -m v1_single_story_testcases.main
```



## Mistake 2: Running from Wrong Folder

Always run from project root:

```text
QA_JIRA_MCP_Agent
```



## Mistake 3: Virtual Environment Not Activated

Expected prompt:

```text
(.venv) PS C:\GIT\qa_mcp_series\QA_JIRA_MCP_Agent>
```



## Mistake 4: Wrong JQL

Wrong:

```sql
SCRUM ORDER BY created DESC
```

Correct:

```sql
project = SCRUM ORDER BY created DESC
```



# 16. Final Verification Checklist

Before execution, confirm:

```text
[ ] Python is installed
[ ] Virtual environment is activated
[ ] Dependencies are installed
[ ] .env file exists
[ ] Jira credentials are correct
[ ] GitHub token is correct
[ ] Running from project root
[ ] Using python -m command
[ ] Correct JQL is used
```



# 17. Recommended First-Time Execution Order

Use this order when running the project for the first time:

```text
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Create .env file
5. Run Version 1
6. Show MCP tools
7. Read one Jira issue
8. Generate single story test cases
9. Run Version 4
10. Search sprint stories
11. Generate sprint workbook
```

This gives confidence that both Jira and GitHub Models are working correctly.



# Summary

This project is designed as a progressive QA MCP learning framework.

Each version builds on the previous version:

```text
Version 1 → Single Story Test Cases
Version 2 → Single Story Workbook
Version 3 → Multiple Stories Workbook
Version 4 → Sprint QA Agent
```

Always run commands from the project root using:

```bash
python -m version_folder.main
```