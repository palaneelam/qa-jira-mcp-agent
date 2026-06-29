# Runbook - QA Jira MCP Agent

Follow this checklist every time you run the project.

## 1. Activate Virtual Environment

```bash
.venv\Scripts\activate
````

---

## 2. Confirm Project Root

You should be inside:

```text
QA_JIRA_MCP_Agent
```

Check:

```bash
pwd
```

---

## 3. Check Environment File

`.env` should exist in project root.

Required values:

```env
JIRA_BASE_URL=
JIRA_EMAIL=
JIRA_API_TOKEN=
GITHUB_TOKEN=
```

---

## 4. Test Jira Server

For Version 1:

```bash
python -m v1_single_story_testcases.mcp_servers.jira_server
```

For Version 4:

```bash
python -m v4_sprint_qa_agent.mcp_servers.jira_server
```

If it waits silently, press `Ctrl + C`.

---

## 5. Run Main App

Version 1:

```bash
python -m v1_single_story_testcases.main
```

Version 4:

```bash
python -m v4_sprint_qa_agent.main
```

---

## 6. First Test

Choose:

```text
1. Show Available MCP Tools
```

Expected:

```text
Available MCP Tools:
- read_jira_issue
- generate_test_cases_from_jira
```

---

## 7. Test Jira Search

Use:

```sql
project = SCRUM ORDER BY created DESC
```

For active sprint:

```sql
project = SCRUM AND sprint in openSprints() ORDER BY created DESC
```

---

## 8. Test Single Jira Issue

Use a valid Jira key:

```text
SCRUM-9
```

---

## 9. Generate Workbook

Choose workbook option and provide valid JQL.

Recommended JQL:

```sql
project = SCRUM AND sprint in openSprints() ORDER BY created DESC
```

---

## 10. Check Output Folder

Generated files should appear in:

```text
outputs/
```

