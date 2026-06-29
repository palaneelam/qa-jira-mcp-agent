# Project Structure

# QA Jira MCP Agent

This project is built as a **progressive learning framework**.

Instead of building one large application, each version introduces one new capability while reusing concepts from the previous versions.

This makes it ideal for:

- Learning MCP (Model Context Protocol)
- Understanding Agentic AI architecture
- Building production-ready AI agents
- Learning Prompt Engineering
- Learning Jira Automation
- Learning Python project architecture

---

# High Level Architecture

```
QA_JIRA_MCP_AGENT
│
├── docs/
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
├── .venv/
│
├── requirements.txt
│
└── README.md
```

---

# Folder Explanation

---

## docs/

Contains complete project documentation.

```
docs/
```

Includes

- Installation Guide
- Architecture
- Troubleshooting
- Best Practices
- Setup Guides
- Common Errors
- Project Roadmap

Purpose

Help new developers understand the project without watching the course.

---

## shared/

Contains reusable code shared across every MCP Agent.

```
shared/
│
├── github_models_client.py
├── excel_styles.py
└── utils.py
```

### github_models_client.py

Responsible for communicating with GitHub Models.

Responsibilities

- GPT-4.1 connection
- JSON mode
- Response cleanup
- Error handling

Every version uses this module.

---

### excel_styles.py

Contains reusable Excel formatting.

Examples

- Header Style
- Cell Colors
- Borders
- Font Styles
- Conditional Formatting

Keeps workbook generation consistent.

---

### utils.py

General helper methods.

Examples

- File utilities
- Folder creation
- Date formatting
- JSON helpers
- Common validations

---

# Version Folders

Every version is an independent learning milestone.

Each version has its own

- MCP Server
- MCP Client
- Main Application
- Prompts
- Jira Client
- Excel Generator

This allows every version to run independently.

---

# Version 1

```
v1_single_story_testcases/
```

Goal

Generate test cases for a single Jira Story.

Architecture

```
User

↓

Main.py

↓

MCP Client

↓

MCP Server

↓

Jira

↓

LLM

↓

JSON

↓

Excel
```

Files

```
main.py
```

Entry point.

Shows console menu.

---

```
mcp_client.py
```

Responsible for

- Starting MCP server
- Calling MCP tools
- Returning results

---

```
mcp_servers/
```

Contains

```
jira_server.py
```

Registers MCP tools.

Example

```
read_jira_issue()

generate_test_cases_from_jira()
```

---

```
jira_client.py
```

Responsible for

- Jira REST API
- Story retrieval

---

```
excel_generator.py
```

Creates

```
Generated_TestCases.xlsx
```

---

```
prompts.py
```

Contains LLM prompts.

Keeping prompts separate improves maintainability.

---

```
requirements/
```

Sample requirement documents.

Useful when Jira is unavailable.

---

```
screenshots/
```

Contains screenshots used in

- Documentation
- README
- Course

---

```
output/
```

Generated Excel files.

---

# Version 2

```
v2_single_story_workbook/
```

Goal

Generate complete QA Workbook for a single Story.

Workbook includes

- Story Details
- Test Cases
- Positive Scenarios
- Negative Scenarios
- Boundary Cases

---

# Version 3

```
v3_multiple_stories_workbook/
```

Goal

Generate one workbook covering multiple Jira Stories.

New Concepts

- JQL
- Multi-story processing
- Workbook aggregation
- AI summarization

---

# Version 4

```
v4_sprint_qa_agent/
```

Goal

Generate complete Sprint QA Workbook.

Capabilities

- Search Sprint
- Read Stories
- AI Test Case Generation
- Workbook Generation

Architecture

```
Sprint

↓

JQL

↓

Jira

↓

Stories

↓

LLM

↓

Workbook
```

---

# Common File Structure

Every version follows the same architecture.

```
Version

│

├── main.py

├── mcp_client.py

├── jira_client.py

├── prompts.py

├── excel_generator.py

├── output/

├── screenshots/

└── mcp_servers/
```

This consistency makes future versions easy to understand.

---

# MCP Server Folder

```
mcp_servers/
```

Contains

```
jira_server.py
```

Responsibilities

- Register MCP tools
- Receive requests
- Call business logic
- Return structured results

Example

```
@mcp.tool()

↓

Read Jira

↓

Generate Workbook

↓

Search Stories
```

---

# Output Folder

```
output/
```

Stores generated files.

Examples

```
Sprint_Workbook.xlsx

Generated_TestCases.xlsx

Story_Workbook.xlsx
```

This folder can be cleaned safely.

---

# Screenshots Folder

Contains screenshots from terminal after execution

---

# Python Virtual Environment

```
.venv/
```

Contains installed Python packages.

Never modify manually.

Never commit to Git.

---

# Design Principles

The project follows these principles.

## Single Responsibility Principle

Every file performs one task.

Example

```
jira_client.py

↓

Only Jira
```

---

```
excel_generator.py

↓

Only Excel
```

---

```
github_models_client.py

↓

Only LLM
```

---

## Separation of Concerns

UI

↓

MCP Client

↓

MCP Server

↓

Business Logic

↓

External APIs

---

## Reusability

Shared functionality lives inside

```
shared/
```

instead of being copied across versions.

---

## Progressive Learning

Every version introduces exactly one major concept.

```
V1

↓

Single Story

↓

V2

↓

Workbook

↓

V3

↓

Multiple Stories

↓

V4

↓

Sprint

↓

V5

↓

Release

↓

V6

↓

Execution Agent
```

# Learning Journey

```
Python

↓

REST API

↓

Jira

↓

MCP

↓

Prompt Engineering

↓

GitHub Models

↓

Excel Automation

↓

AI Agents

↓

QA Automation

↓

Production Framework