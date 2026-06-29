# Troubleshooting Guide - QA Jira MCP Agent

This guide covers common issues faced while running the QA Jira MCP Agent project.

## 1. ModuleNotFoundError

### Error

```text
ModuleNotFoundError: No module named 'v1_single_story_testcases'
````

### Cause

The Python file is being run directly instead of running it as a module.

### Wrong Command

```bash
python .\v1_single_story_testcases\main.py
```

### Correct Command

```bash
python -m v1_single_story_testcases.main
```

Always run commands from the project root folder.

---

## 2. MCP Error: Connection Closed

### Error

```text
mcp.shared.exceptions.McpError: Connection closed
```

### Cause

The MCP server crashed before the client could connect.

Common reasons:

* Wrong import path
* Missing environment variables
* Server file has runtime error
* MCP server is being started as a direct script instead of module
* Missing function import

### Fix

First test the server directly:

```bash
python -m v1_single_story_testcases.mcp_servers.jira_server
```

If the server starts silently, it is working.

Then run the main app:

```bash
python -m v1_single_story_testcases.main
```

---

## 3. Jira JQL Error

### Error

```text
Expecting operator but got 'ORDER'
```

### Cause

Invalid JQL syntax.

### Wrong JQL

```sql
SCRUM ORDER BY created DESC
```

### Correct JQL

```sql
project = SCRUM ORDER BY created DESC
```

For active sprint:

```sql
project = SCRUM AND sprint in openSprints() ORDER BY created DESC
```

---

## 4. NoneType Object Has No Attribute Get

### Error

```text
'NoneType' object has no attribute 'get'
```

### Cause

Jira returned a field as `null`.

Common nullable fields:

* assignee
* priority
* reporter
* description
* sprint
* parent

### Fix

Use safe access:

```python
assignee = fields.get("assignee") or {}
priority = fields.get("priority") or {}

assignee_name = assignee.get("displayName", "Unassigned")
priority_name = priority.get("name", "Unknown")
```

---

## 5. GitHub Models Token Missing

### Error

```text
GITHUB_TOKEN is missing in .env file
```

### Cause

The `.env` file does not contain GitHub Models token.

### Fix

Create `.env` in project root:

```env
GITHUB_TOKEN=your_github_token_here
```

No quotes. No spaces.

---

## 6. Jira Authentication Failed

### Error

```text
401 Unauthorized
```

### Cause

Invalid Jira email or API token.

### Fix

Check `.env`:

```env
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your_jira_api_token
```

---

## 7. Jira Project Not Found

### Error

```text
Project does not exist or you do not have permission
```

### Cause

Wrong project key or insufficient permission.

### Fix

Check project key in Jira URL.

Example:

```text
SCRUM-9
```

Project key is:

```text
SCRUM
```

Use:

```sql
project = SCRUM ORDER BY created DESC
```

---

## 8. FastMCP Tool Not Found

### Error

```text
Tool not found
```

### Cause

Tool function is not decorated with `@mcp.tool()`.

### Fix

```python
@mcp.tool()
def read_jira_issue(issue_key: str):
    return get_jira_issue(issue_key)
```

Restart the app after adding the tool.

---

## 9. Excel File Not Generated

### Cause

Possible reasons:

* Output folder does not exist
* Excel generator function not called
* LLM response format is incorrect
* Test cases key missing from JSON

### Fix

Ensure output folder exists:

```python
os.makedirs("outputs", exist_ok=True)
```

Check expected JSON format:

```json
{
  "test_cases": []
}
```

---

## 10. Debugging Rule

When MCP fails, always debug in this order:

```text
1. Run server directly
2. Run main app
3. Show tools
4. Run simple Jira read
5. Run LLM call separately
6. Run workbook generation
```