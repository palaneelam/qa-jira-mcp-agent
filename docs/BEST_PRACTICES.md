# Best Practices

# QA Jira MCP Agent Framework

## Purpose

This document describes the engineering principles, coding standards, architectural guidelines, and development practices followed throughout the QA Jira MCP Agent Framework.

These best practices are based on real-world enterprise software engineering experience and are intended to make the project:

* Easy to understand
* Easy to maintain
* Easy to extend
* Production-ready
* Suitable for enterprise-scale applications

# Core Design Principles

The framework follows these software engineering principles.

## 1. Single Responsibility Principle (SRP)

Every module should perform **one responsibility only**.

### Good

```
jira_client.py

↓

Only communicates with Jira
```

```
excel_generator.py

↓

Only creates Excel workbooks
```

```
github_models_client.py

↓

Only communicates with GitHub Models
```

### Bad

```
main.py

↓

Read Jira

↓

Generate Prompt

↓

Call GPT

↓

Generate Excel

↓

Write Logs
```

A file doing five different things becomes difficult to maintain and test.


## 2. Separation of Concerns

Separate the application into logical layers.

```
Console UI

↓

MCP Client

↓

MCP Server

↓

Business Logic

↓

External Services
```

Each layer should know only about the layer directly below it.



## 3. Modular Design

Large applications should be divided into small reusable modules.

Instead of

```
main.py

↓

2000 lines
```

Use

```
main.py

↓

jira_client.py

↓

github_models_client.py

↓

excel_generator.py

↓

utils.py
```

Benefits

* Easier debugging
* Easier testing
* Easier code reviews



## 4. Reusability

Never duplicate code.

### Bad

```
Version 1

↓

jira_client.py

Version 2

↓

Copy jira_client.py

Version 3

↓

Copy again
```

### Good

```
shared/

↓

jira_client.py

↓

Used by every version
```

Whenever code is copied more than once, consider moving it into the shared folder.



## 5. Progressive Learning

Each version should introduce **one new concept only**.

Example roadmap

```
Version 1

↓

Single Story

Version 2

↓

Workbook

Version 3

↓

Multiple Stories

Version 4

↓

Sprint Agent

Version 5

↓

Release Agent

Version 6

↓

Execution Agent
```

Avoid introducing multiple new concepts in the same version.



# Project Structure Best Practices

## Keep Folder Structure Consistent

Every version should have the same layout.

```
main.py

mcp_client.py

mcp_servers/

output/

screenshots/
```

Consistency reduces the learning curve.



## Store Shared Logic Separately

Reusable code belongs in

```
shared/
```

Examples

* Jira Client
* GitHub Models Client
* Excel Styles
* Utilities
* Logger
* Configuration



## Keep Prompts Separate

Never embed large prompts directly inside Python code.

### Bad

```
main.py

↓

500-line prompt
```

### Good

```
prompts/

↓

story_prompt.py

↓

sprint_prompt.py

↓

regression_prompt.py
```

Benefits

* Easier prompt tuning
* Cleaner code
* Reusable prompts



# MCP Best Practices

## One Tool = One Responsibility

Each MCP tool should solve exactly one problem.

Good examples

```
read_jira_issue()

search_jira_issues()

generate_test_cases()

generate_workbook()
```

Avoid combining multiple operations into a single tool.



## Validate Inputs

Never trust user input.

Example

Instead of

```
generate(issue_key)
```

Validate

* Empty value
* Invalid Jira key
* Null values
* Incorrect data types



## Always Handle Exceptions

Bad

```
result = get_jira_issue(key)
```

Good

```
try

↓

Call Jira

↓

Return meaningful message

↓

Log error
```

Applications should never crash because of a recoverable error.



## Return Structured Data

Return dictionaries instead of plain strings.

Good

```
{
    "status": "success",
    "issues": [...]
}
```

Bad

```
"Success"
```

Structured responses are easier to consume by other tools.



# API Best Practices

## Never Hardcode Credentials

Bad

```
API_KEY = "abc123"
```

Good

```
.env

↓

API_KEY
```



## Validate API Responses

Do not assume the API always succeeds.

Check

* Status code
* Response body
* Error messages



## Handle Nullable Fields

Many Jira fields may be null.

Instead of

```
fields.get("assignee").get("displayName")
```

Use

```
assignee = fields.get("assignee") or {}

name = assignee.get("displayName", "Unassigned")
```



# LLM Best Practices

## Keep Prompts Deterministic

Prefer

```
temperature = 0.2
```

instead of

```
temperature = 1.0
```

for test case generation.



## Ask for Structured Output

Always request JSON.

Example

```
Return ONLY valid JSON.
```

Avoid parsing free-form text.



## Validate LLM Responses

Never assume the model returned valid JSON.

Always

* Clean markdown
* Parse JSON
* Handle parsing errors



## Keep Prompt Templates Versioned

Store prompts separately.

Example

```
prompts/

↓

v1_story_prompt.py

v2_workbook_prompt.py

v3_sprint_prompt.py
```

This allows prompt evolution without affecting previous versions.



# Python Best Practices

## Meaningful Function Names

Good

```
generate_test_cases_from_story()
```

Bad

```
process()
```



## Small Functions

Prefer

```
20–40 lines
```

instead of

```
300 lines
```

Small functions are easier to read and test.



## Type Hints

Always use type hints.

Good

```
def search_issues(
    jql: str,
    max_results: int
) -> list:
```



## Docstrings

Every public function should have a docstring.

Example

```
"""
Reads a Jira issue and returns structured information.
"""
```



# Excel Generation Best Practices

Separate

* Data
* Styling
* Formatting

Do not mix them together.

Example

```
Workbook

↓

Worksheet

↓

Write Data

↓

Apply Style

↓

Auto Size

↓

Freeze Panes

↓

Save
```



# Logging Best Practices

Replace print statements with proper logging.

Levels

```
INFO

WARNING

ERROR

CRITICAL
```

Store logs inside

```
logs/
```



# Error Handling

Always return useful messages.

Bad

```
Connection failed
```

Good

```
Failed to connect to Jira.

Possible reasons

• Invalid API Token

• Network unavailable

• Jira URL incorrect
```

Helpful errors reduce troubleshooting time.



# Configuration Best Practices

Keep configuration outside source code.

Examples

```
.env

config.py

constants.py
```

Avoid hardcoding

* URLs
* Tokens
* File paths
* Model names



# Version Control Best Practices

Commit frequently.

Recommended format

```
feat:

fix:

docs:

refactor:

test:
```

Example

```
feat: Added Sprint QA Workbook generation

fix: Handled null assignee field

docs: Added troubleshooting guide
```



# Testing Best Practices

Test each layer independently.

Recommended order

```
Jira Client

↓

GitHub Models

↓

Excel Generator

↓

MCP Server

↓

Main Application
```

Debugging is easier when each component is verified separately.



# Performance Best Practices

Avoid unnecessary API calls.

Reuse data where possible.

Batch operations whenever supported.

Keep prompts concise without sacrificing clarity.



# Security Best Practices

Never commit

* API Keys
* Tokens
* Passwords
* .env files

Always include

```
.env
```

inside

```
.gitignore
```

Rotate API keys periodically.

Use least-privilege access for Jira accounts.



# Documentation Best Practices

Every version should include

* README
* Architecture
* Troubleshooting
* Setup Guide
* Common Errors

Good documentation is part of the product—not an afterthought.


# Final Thoughts

The goal of this project is not simply to build AI agents.

The goal is to build AI agents using software engineering practices that can scale from a learning project to an enterprise-grade framework.

Following these best practices will help you write cleaner code, reduce defects, simplify maintenance, and build systems that are easier for teams to understand and extend.