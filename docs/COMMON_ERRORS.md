# Common Errors and Fixes

## Error 1: Running file directly

### Wrong

```bash
python v1_single_story_testcases/main.py
````

### Correct

```bash
python -m v1_single_story_testcases.main
```

---

## Error 2: Missing `__init__.py`

### Fix

Create empty files:

```text
v1_single_story_testcases/__init__.py
v1_single_story_testcases/mcp_servers/__init__.py
shared/__init__.py
```

---

## Error 3: Invalid import

### Error

```text
ImportError: cannot import name 'generate_test_cases'
```

### Cause

The function does not exist in the imported file.

### Fix

Check actual function name.

Example:

```python
from shared.github_models_client import call_github_models_json
```

---

## Error 4: MCP Server Connection Closed

### Fix Checklist

Check:

```text
- Is the server file running?
- Are imports correct?
- Are .env values available?
- Is the server run using python -m?
- Is mcp.run() present?
```

Server must end with:

```python
if __name__ == "__main__":
    mcp.run()
```

---

## Error 5: JQL Syntax Error

### Wrong

```sql
SCRUM ORDER BY created DESC
```

### Correct

```sql
project = SCRUM ORDER BY created DESC
```

---

## Error 6: NoneType error from Jira fields

### Wrong

```python
fields.get("assignee").get("displayName")
```

### Correct

```python
assignee = fields.get("assignee") or {}
assignee.get("displayName", "Unassigned")
```

---

## Error 7: Tool returns None

### Wrong

```python
def list_files():
    files = os.listdir("requirements")
```

### Correct

```python
def list_files():
    return os.listdir("requirements")
```

---

## Error 8: Await used on normal function

### Error

```text
TypeError: object list can't be used in 'await' expression
```

### Fix

Remove `await`.

### Wrong

```python
files = await list_files()
```

### Correct

```python
files = list_files()
```
