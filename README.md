# QA Jira MCP Agent

> **Build Intelligent AI-Powered QA Agents using MCP (Model Context Protocol), Python, GitHub Models API, and Jira Cloud.**

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastMCP](https://img.shields.io/badge/FastMCP-3.4.2-green.svg)
![GitHub Models](https://img.shields.io/badge/GitHub-Models-black.svg)
![Jira](https://img.shields.io/badge/Jira-Cloud-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

# 📖 Overview

This repository demonstrates how to build AI-powered QA agents using the **Model Context Protocol (MCP)**.

The project progressively evolves from generating test cases for a single Jira story to generating a complete Sprint QA Workbook.

This project is designed for:

* QA Engineers
* Manual Testers
* Automation Engineers
* SDETs
* QA Architects
* AI Engineers
* Students learning MCP
* Anyone interested in Agentic AI for Software Testing

---

# Project Versions

## Version 1

Single Jira Story → Test Cases

```
Jira Story

↓

Read Story

↓

GitHub Models

↓

Generate Test Cases

↓

Excel
```

---

## Version 2

Single Jira Story → Complete QA Workbook

Generates

* Test Scenarios
* Test Cases
* RTM
* Risks
* Test Data

---

## Version 3

Multiple Jira Stories

Input

```
SCRUM-8,SCRUM-9,SCRUM-10
```

Output

Complete QA Workbook containing all stories.

---

## Version 4

Sprint QA Agent

Input

```
JQL Query
```

Example

```
project = SCRUM ORDER BY created DESC
```

Output

Complete Sprint QA Workbook.

---

# Architecture

```
              +-----------------------+
              |      User / QA        |
              +-----------+-----------+
                          |
                          |
                          ▼
                 Python Application
                          |
                          |
                FastMCP Client
                          |
             MCP Transport (STDIO)
                          |
                FastMCP Server
                          |
        +-----------------+----------------+
        |                                  |
        ▼                                  ▼
   Jira REST API                  GitHub Models API
        |                                  |
        +-----------------+----------------+
                          |
                          ▼
                  Generated QA Artifacts
                          |
                          ▼
                      Excel Workbook
```

---

# Repository Structure

```
QA_JIRA_MCP_Agent/

│
├── shared/
│
├── v1_single_story_testcases/
│
├── v2_single_story_workbook/
│
├── v3_multiple_stories_workbook/
│
├── v4_sprint_qa_agent/
│
├── .env
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Technologies

* Python
* FastMCP 3.4.2
* GitHub Models API
* Jira Cloud REST API
* OpenPyXL
* Pandas

---

# Prerequisites

Install

* Python 3.11+
* VS Code
* Git
* GitHub Account
* Jira Cloud Account

---

# Clone Repository

```
git clone https://github.com/<username>/QA_JIRA_MCP_Agent.git

cd QA_JIRA_MCP_Agent
```

---

# Create Virtual Environment

Windows

```
python -m venv .venv

.venv\Scripts\activate
```

Mac/Linux

```
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

```
pip install -r requirements.txt
```

---

# GitHub Models API Setup

## Step 1

Open

https://github.com/marketplace/models

Enable GitHub Models.

---

## Step 2

Generate GitHub Personal Access Token

Scopes

```
models
```

Copy the token.

---

# Jira Cloud Setup

Create a free Jira Cloud account.

Create a project.

Example

```
Project Name

QA Demo

Project Key

SCRUM
```

---

# Generate Jira API Token

Open

https://id.atlassian.com/manage-profile/security/api-tokens

Click

```
Create API Token
```

Copy the generated token.

---

# Create Sample Stories

Create the following Stories.

```
SCRUM-8

Online Payment using Credit Card
```

```
SCRUM-9

Apply Discount Coupon
```

```
SCRUM-10

Order Confirmation
```

---

# Configure Environment Variables

Create

```
.env
```

```
GITHUB_TOKEN=xxxxxxxxxxxxxxxx

JIRA_BASE_URL=https://yourcompany.atlassian.net

JIRA_EMAIL=your_email@gmail.com

JIRA_API_TOKEN=xxxxxxxxxxxx
```

---

# Run Version 1

```
cd v1_single_story_testcases

python main.py
```

---

# Run Version 2

```
cd ..

cd v2_single_story_workbook

python main.py
```

---

# Run Version 3

```
cd ..

cd v3_multiple_stories_workbook

python main.py
```

Input

```
SCRUM-8,SCRUM-9,SCRUM-10
```

---

# Run Version 4

```
cd ..

cd v4_sprint_qa_agent

python main.py
```

Input

```
project = SCRUM ORDER BY created DESC
```

---

# Output

Version 1

```
TestCases.xlsx
```

Version 2

```
QA_Workbook.xlsx
```

Version 3

```
Multiple_Stories_QA_Workbook.xlsx
```

Version 4

```
Sprint_QA_Workbook.xlsx
```

---

# Generated QA Artifacts

* Test Scenarios
* Test Cases
* RTM
* Risks
* Test Data
* Sprint Summary
* Cross Story Risks

---

# Common JQL Queries

All stories

```
project = SCRUM
```

Latest stories

```
project = SCRUM ORDER BY created DESC
```

Only To Do

```
project = SCRUM AND status="To Do"
```

High Priority

```
project = SCRUM AND priority=High
```

---

Or for only stories:

project = SCRUM AND issuetype = Story ORDER BY created DESC

Or for current sprint:

project = SCRUM AND sprint in openSprints() ORDER BY created DESC

# ❗ Troubleshooting

## ModuleNotFoundError

```
No module named 'shared'
```

Solution

Run the application from the project root.

---

## MCP Connection Closed

Usually indicates the MCP server crashed.

Verify

```
python mcp_servers/jira_server.py
```

---

## 429 Rate Limit

GitHub Models free tier has daily request limits.

Wait for the quota to reset or reduce the number of AI calls.

---

## Jira 404

```
Issue does not exist
```

Verify:

* Jira Issue Key
* API Token
* Email
* Project Permissions

---

## Blank Excel

Usually indicates the AI returned empty JSON.

Print the raw AI response and validate the JSON structure.

---

## FileNotFoundError

Ensure the folder structure matches the repository layout and the MCP server path in `mcp_client.py` points to the correct version folder.

---

## Unicode / ₹ Character Error

```
'charmap' codec can't encode character
```

Set:

```
PYTHONUTF8=1
PYTHONIOENCODING=utf-8
```

and replace unsupported Unicode characters if necessary.

---

# Future Roadmap

* Playwright MCP Agent
* Browser Automation Agent
* Database Validation Agent
* Requirement Analysis Agent
* API Testing Agent
* AI Bug Triage Agent
* Sprint Planning Agent
* End-to-End QA Agent Framework

---

# Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Create a Pull Request.

---

# License

MIT License.

---

# If You Like This Project

If you found this repository useful:

⭐ Star the repository

🍴 Fork it

💬 Share it with fellow QA Engineers

Happy Learning!
