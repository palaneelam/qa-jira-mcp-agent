def test_case_prompt(jira_issue):
    return f"""
You are a Senior QA Engineer.

Read the Jira story below and generate detailed manual test cases.

Return ONLY valid JSON in this format:

{{
  "test_cases": [
    {{
      "TC_ID": "TC001",
      "Issue_Key": "{jira_issue.get("issue_key", "")}",
      "Scenario": "Verify successful user action",
      "Precondition": "User has valid access",
      "Steps": "1. Open application\\n2. Perform action\\n3. Submit",
      "Expected_Result": "System should behave as expected",
      "Priority": "High"
    }}
  ]
}}

Jira Issue Details:

Issue Key:
{jira_issue.get("issue_key", "")}

Issue Type:
{jira_issue.get("issue_type", "")}

Summary:
{jira_issue.get("summary", "")}

Description:
{jira_issue.get("description", "")}

Priority:
{jira_issue.get("priority", "")}

Status:
{jira_issue.get("status", "")}
"""