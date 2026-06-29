## QA Jira MCP Agent Framework

# Purpose

This guide explains everything required to understand, configure, and use **Model Context Protocol (MCP)** within this project.

After reading this document, you will understand:

* What MCP is
* Why MCP was created
* MCP Architecture
* FastMCP fundamentals
* MCP Client
* MCP Server
* MCP Tools
* How this project uses MCP
* How to add new tools
* Common troubleshooting steps

This guide assumes no prior MCP knowledge.



# What is MCP?

**MCP (Model Context Protocol)** is an open protocol that allows AI models to securely communicate with external tools and data sources.

Think of MCP as:

> **USB-C for AI Applications**

Just as USB-C allows computers to connect to many different devices using a common interface, MCP allows AI assistants to connect to different tools using a standard protocol.

Instead of writing custom integrations for every application, MCP provides one common communication standard.



# Why was MCP Created?

Without MCP, every AI application requires custom integrations.

Example:

```text
ChatGPT

↓

Custom Jira API

↓

Custom Database API

↓

Custom GitHub API

↓

Custom Filesystem API

↓

Custom Slack API
```

Each integration must be written separately.

With MCP:

```text
AI Model

↓

MCP Client

↓

MCP Server

↓

Any Tool
```

The AI only understands MCP.

Every tool simply exposes itself through an MCP Server.



# Benefits of MCP

* Standard communication protocol
* Language independent
* Reusable tools
* Easier maintenance
* Extensible architecture
* Better separation of concerns
* Enterprise-friendly design



# MCP Architecture

```text
+-+
|     AI Assistant     |
+-+
            |
            |
            v
+-+
|      MCP Client      |
+-+
            |
            |
      JSON-RPC Messages
            |
            |
            v
+-+
|      MCP Server      |
+-+
            |
     Registered Tools
            |
            |
            v
+-+
| Jira / GitHub / LLM  |
| Database / Files     |
+-+
```



# Components Used in This Project

The framework consists of four major components.

## 1. Console Application

Responsible for:

* Menu
* User Input
* Displaying Results

File:

```text
main.py
```



## 2. MCP Client

Responsible for:

* Starting the MCP Server
* Sending tool requests
* Receiving responses

File:

```text
mcp_client.py
```



## 3. MCP Server

Responsible for:

* Registering tools
* Executing business logic
* Returning results

File:

```text
mcp_servers/jira_server.py
```



## 4. Business Layer

Responsible for:

* Jira communication
* LLM communication
* Excel generation

Examples:

```text
jira_client.py

github_models_client.py

excel_generator.py
```



# Project Flow

The following sequence occurs when generating test cases.

```text
User

↓

main.py

↓

MCP Client

↓

FastMCP

↓

Jira MCP Server

↓

Read Jira Issue

↓

GitHub Models

↓

Generate JSON

↓

Return JSON

↓

Excel Generator

↓

Workbook
```

Each component has one responsibility.



# FastMCP

This project uses **FastMCP**.

FastMCP simplifies:

* Creating MCP Servers
* Registering tools
* Managing communication
* Tool discovery
* JSON serialization

Without FastMCP, implementing the MCP protocol manually would require significant boilerplate.



# Creating an MCP Server

Every server starts with:

```python
from fastmcp import FastMCP

mcp = FastMCP("QA Jira MCP Server")
```

This creates the MCP application.



# Registering a Tool

Any Python function can become an MCP Tool.

Example:

```python
@mcp.tool()
def read_jira_issue(issue_key: str):
    return get_jira_issue(issue_key)
```

Once decorated, the function becomes available to every MCP Client.



# Starting the Server

Always finish with:

```python
if __name__ == "__main__":
    mcp.run()
```

This starts the MCP Server and listens for requests.



# Creating an MCP Client

The client launches the server using Python.

Example:

```python
transport = StdioTransport(
    command=sys.executable,
    args=[
        "-m",
        "v1_single_story_testcases.mcp_servers.jira_server"
    ],
    cwd=PROJECT_ROOT
)

client = Client(transport)
```



# Why Use StdioTransport?

This project communicates through **Standard Input / Standard Output (STDIO)**.

Advantages:

* Simple
* Local execution
* No network configuration
* Ideal for desktop applications
* Easy debugging



# Tool Discovery

Clients can list available tools.

Example:

```python
tools = await client.list_tools()
```

Output:

```text
read_jira_issue

generate_test_cases_from_jira
```



# Calling a Tool

Example:

```python
await client.call_tool(
    "read_jira_issue",
    {
        "issue_key": "SCRUM-9"
    }
)
```

The client does not know how Jira works.

It simply invokes a tool.



# Adding a New Tool

Step 1

Create a function.

```python
@mcp.tool()
def search_jira_issues():
```

Step 2

Restart the server.

Step 3

The client automatically discovers the tool.

No client-side protocol changes are required.



# Current MCP Tools

Version 1

* read_jira_issue
* generate_test_cases_from_jira

Version 2

* workbook generation

Version 3

* multiple story processing

Version 4

* search_issues_by_jql
* generate_sprint_workbook

Future versions may include:

* Regression Suite Generator
* Playwright Generator
* Automation Agent
* Bug Analysis Agent
* Test Data Generator



# Folder Structure

```text
v1_single_story_testcases/

│

├── main.py

├── mcp_client.py

│

├── mcp_servers/

│      jira_server.py

│

├── jira_client.py

├── excel_generator.py

└── prompts.py
```



# Communication Flow

```text
Client

↓

JSON Request

↓

Tool Name

↓

Arguments

↓

Server

↓

Python Function

↓

Response

↓

JSON

↓

Client
```



# Error Handling

Every tool should use exception handling.

Example:

```python
try:
    ...
except Exception as e:
    return {
        "error": str(e)
    }
```

Never allow an exception to terminate the MCP Server.



# Common Errors

## Connection Closed

Possible causes:

* Server crashed
* Import error
* Wrong module path
* Missing dependency
* Exception during startup

Solution:

Run the server directly.

```bash
python -m v1_single_story_testcases.mcp_servers.jira_server
```

If the server fails here, fix the startup error first.



## Tool Not Found

Possible causes:

* Missing `@mcp.tool()`
* Server not restarted
* Typo in tool name



## ModuleNotFoundError

Cause:

Running Python from the wrong directory or using script execution instead of module execution.

Correct:

```bash
python -m v1_single_story_testcases.main
```

Avoid:

```bash
python main.py
```

when using package imports.



## Connection Closed During Tool Execution

Common reasons:

* Unhandled exception inside the tool
* Import failure
* External API crash
* LLM exception
* Invalid return type

Always wrap tool logic with `try/except` and return structured error messages.



# Best Practices

* Keep each tool focused on a single responsibility.
* Return dictionaries or JSON-compatible objects.
* Never print to `stdout` inside an MCP tool (use `stderr` for debugging if necessary).
* Reuse business logic from shared modules.
* Keep the client thin; business logic belongs on the server.
* Use module execution (`python -m ...`) consistently.
* Validate all inputs before processing.



# Summary

MCP is the communication backbone of this project.

It cleanly separates:

* User Interface
* AI Logic
* Business Logic
* External Systems

Using FastMCP allows the QA Jira MCP Agent Framework to remain modular, scalable, and easy to extend. As new capabilities are added—such as regression testing, Playwright generation, sprint planning, or defect analysis—they can be exposed simply by registering additional MCP tools without changing the overall architecture.
