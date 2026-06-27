import sys
from pathlib import Path
from unittest import result
from unittest import result

from fastmcp import FastMCP

BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from v1_single_story_testcases.jira_client import get_jira_issue
from shared.github_models_client import call_github_models_json
from v1_single_story_testcases.prompts import test_case_prompt

mcp = FastMCP("QA Jira MCP Server")


@mcp.tool()
def read_jira_issue(issue_key: str):
    """
    Reads a Jira issue by issue key.
    """

    return get_jira_issue(issue_key)


@mcp.tool()
def generate_test_cases_from_jira(issue_key: str):
    """
    Reads Jira issue and generates test cases.
    """

    jira_issue = get_jira_issue(issue_key)

    if jira_issue.get("error"):
        return jira_issue

    result = call_github_models_json(
        test_case_prompt(jira_issue)
    )
    
    print(f"AI Result: {result}", file=sys.stderr, flush=True)
    print(result)

    return result


if __name__ == "__main__":
    mcp.run()