import os
import sys
from pathlib import Path

from fastmcp import FastMCP

# Add project root and version folder to Python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
VERSION_DIR = os.path.dirname(CURRENT_DIR)
PROJECT_ROOT = os.path.abspath(os.path.join(VERSION_DIR, ".."))

if VERSION_DIR not in sys.path:
    sys.path.insert(0, VERSION_DIR)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from jira_client import get_jira_issue
from shared.github_models_client import call_github_models_json

mcp = FastMCP("QA Jira MCP Server")


@mcp.tool()
def read_jira_issue(issue_key: str):
    return get_jira_issue(issue_key)


@mcp.tool()
def generate_test_cases_from_jira(issue_key: str):
    try:
        issue = get_jira_issue(issue_key)

        prompt = f"""
You are a Senior QA Engineer.

Generate detailed manual test cases for this Jira issue:

{issue}

Return ONLY valid JSON in this exact format:

{{
  "test_cases": [
    {{
      "test_case_id": "TC001",
      "scenario": "",
      "preconditions": "",
      "steps": [
        "Step 1",
        "Step 2"
      ],
      "expected_result": "",
      "priority": "High"
    }}
  ]
}}
"""

        result = call_github_models_json(prompt)
        return result

    except Exception as e:
        return {
            "error": str(e),
            "message": "Failed while generating test cases from Jira issue"
        }


if __name__ == "__main__":
    mcp.run()