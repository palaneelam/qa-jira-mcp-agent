## Project Structure Guide


# Purpose

This document explains the complete folder structure of the QA Jira MCP Agent Framework and the purpose of every directory and major file.

The project has been intentionally organized to mimic a real enterprise software project rather than a small demo application.

Understanding the structure will help you:

* Navigate the project easily
* Locate business logic quickly
* Add new features without confusion
* Reuse existing components
* Follow enterprise development practices



# Repository Overview

```text
QA_JIRA_MCP_AGENT/
│
├── .venv/
├── docs/
├── output/
├── shared/
│
├── v1_single_story_testcases/
├── v2_single_story_workbook/
├── v3_multiple_stories_workbook/
├── v4_sprint_qa_agent/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

The repository is divided into two major parts:

* Shared reusable components
* Independent learning versions



# Root Directory

The root directory contains project-level configuration and documentation.

```text
QA_JIRA_MCP_AGENT/
```

This is the entry point of the repository.

It contains:

* Documentation
* Dependencies
* Shared utilities
* Version folders



# .venv

```text
.venv/
```

Contains the Python Virtual Environment.

Purpose:

* Isolates project dependencies
* Prevents package conflicts
* Ensures reproducible environments

Never commit this folder to Git.



# docs

```text
docs/
```

Contains complete project documentation.

Typical documents include:

```text
Architecture.md

Best_Practices.md

Troubleshooting.md

Project_Structure.md

GitHub_Models_Setup.md

MCP_Setup.md
```

The goal is to make the project self-explanatory.



# output

```text
output/
```

Stores generated artifacts.

Examples:

```text
Sprint Workbook.xlsx

Generated Test Cases.xlsx

Requirement Summary.xlsx
```

Output files are generated dynamically while running the application.



# shared

```text
shared/
```

One of the most important folders in the project.

Contains reusable components shared across every version.

Example:

```text
shared/

│

├── github_models_client.py

├── excel_styles.py

└── utils.py
```

Benefits:

* No code duplication
* Easier maintenance
* Centralized updates
* Consistent behavior across versions



# github_models_client.py

Responsible for:

* Connecting to GitHub Models
* Sending prompts
* Receiving AI responses
* Parsing JSON

Every version uses this client.



# excel_styles.py

Contains reusable Excel formatting.

Examples:

* Header styles
* Fonts
* Borders
* Cell colors
* Freeze panes
* Auto-sizing columns

Separating styling from workbook generation keeps the code clean.



# utils.py

Contains common helper functions.

Examples:

* JSON formatting
* File handling
* Date formatting
* Common validations

Any reusable utility belongs here.



# Versioned Learning Modules

Instead of creating one large application, the project is divided into progressive versions.

Each version introduces one new concept.



# Version 1

```text
v1_single_story_testcases/
```

Goal:

Generate test cases for a single Jira Story.

Introduces:

* FastMCP
* MCP Client
* MCP Server
* Jira Integration
* GitHub Models
* JSON Output

Key files:

```text
main.py

jira_client.py

mcp_client.py

excel_generator.py

prompts.py
```



# Version 2

```text
v2_single_story_workbook/
```

Goal:

Generate a professional QA workbook from a single Jira Story.

New concepts:

* Multiple worksheets
* Better Excel formatting
* Improved reporting
* Workbook generation



# Version 3

```text
v3_multiple_stories_workbook/
```

Goal:

Generate QA artifacts for multiple Jira Stories.

Introduces:

* Batch processing
* Story iteration
* Workbook consolidation
* Improved scalability



# Version 4

```text
v4_sprint_qa_agent/
```

Goal:

Generate an entire Sprint QA Workbook.

Introduces:

* JQL Search
* Sprint Processing
* Multiple Stories
* AI Workbook Generation
* Enterprise QA Planning

This version resembles a production-ready QA Assistant.



# Common Folder Structure

Every version follows the same internal layout.

```text
version/

│

├── main.py

├── jira_client.py

├── mcp_client.py

├── prompts.py

├── excel_generator.py

│

├── mcp_servers/

├── output/

└── screenshots/
```

Maintaining the same layout across versions makes navigation intuitive.



# main.py

Acts as the application's entry point.

Responsibilities:

* Display menus
* Accept user input
* Call MCP Client
* Display results

No business logic should be implemented here.



# jira_client.py

Responsible only for Jira communication.

Typical operations:

* Read issue
* Search issues
* Retrieve sprint data

It should never contain AI logic.



# mcp_client.py

Responsible for:

* Starting the MCP Server
* Calling MCP Tools
* Returning responses

Acts as the bridge between the console application and the server.



# mcp_servers

```text
mcp_servers/
```

Contains FastMCP servers.

Example:

```text
jira_server.py
```

Responsibilities:

* Register MCP tools
* Execute business logic
* Return structured responses

The server exposes project functionality through MCP.



# prompts.py

Contains AI prompts used by GitHub Models.

Separating prompts from code provides:

* Better maintainability
* Easier prompt engineering
* Cleaner Python files



# excel_generator.py

Responsible only for Excel creation.

Typical responsibilities:

* Create workbook
* Add worksheets
* Write data
* Apply formatting
* Save workbook

Business logic should not be implemented here.



# screenshots

Contains screenshots from terminal 



# Version Independence

Every version can be executed independently.

Example:

```text
Version 1

↓

Single Story

↓

Version 2

↓

Workbook

↓

Version 3

↓

Multiple Stories

↓

Version 4

↓

Sprint QA Agent
```

This allows learners to understand one concept before moving to the next.



# Why Use a Shared Folder?

Without a shared folder:

```text
Version 1

↓

jira_client.py

Version 2

↓

Copy jira_client.py

Version 3

↓

Copy jira_client.py

Version 4

↓

Copy jira_client.py
```

This leads to duplicated code and inconsistent fixes.

With a shared folder:

```text
shared/

↓

github_models_client.py

↓

excel_styles.py

↓

utils.py

↓

Used by Every Version
```

A change in one place benefits all versions.



# Recommended Future Structure

As the project grows, additional shared modules can be added.

```text
shared/

├── github_models_client.py

├── jira_client.py

├── excel_styles.py

├── logger.py

├── config.py

├── constants.py

├── prompt_loader.py

└── utils.py
```

This keeps version folders lightweight.

# Design Principles

The project structure follows several software engineering principles:

* Single Responsibility Principle
* Separation of Concerns
* DRY (Don't Repeat Yourself)
* Progressive Learning
* Modular Design
* Reusability
* Enterprise Scalability

These principles make the framework easier to maintain and extend.