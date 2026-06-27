import sys
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()

VERSION_DIR = CURRENT_FILE.parent.parent
PROJECT_ROOT = VERSION_DIR.parent

sys.path.insert(0, str(VERSION_DIR))
sys.path.insert(0, str(PROJECT_ROOT))

from fastmcp import FastMCP
from jira_client import get_jira_issue
from shared.github_models_client import call_github_models_json
from prompts import (
    scenario_prompt,
    test_case_prompt,
    rtm_prompt,
    risk_prompt,
    test_data_prompt
)

mcp = FastMCP("QA Jira MCP Server")


@mcp.tool()
def read_jira_issue(issue_key: str):
    """
    Reads a Jira issue by issue key.
    """

    return get_jira_issue(issue_key)


@mcp.tool()
def generate_test_scenarios_from_jira(issue_key: str):
    jira_issue = get_jira_issue(issue_key)

    if jira_issue.get("error"):
        return jira_issue

    result = call_github_models_json(
        scenario_prompt(jira_issue)
    )

    return result


@mcp.tool()
def generate_test_cases_from_jira(issue_key: str):
    jira_issue = get_jira_issue(issue_key)

    if jira_issue.get("error"):
        return jira_issue

    result = call_github_models_json(
        test_case_prompt(jira_issue)
    )

    return result


@mcp.tool()
def generate_rtm_from_jira(issue_key: str):
    jira_issue = get_jira_issue(issue_key)

    if jira_issue.get("error"):
        return jira_issue

    result = call_github_models_json(
        rtm_prompt(jira_issue)
    )

    return result


@mcp.tool()
def generate_risks_from_jira(issue_key: str):
    jira_issue = get_jira_issue(issue_key)

    if jira_issue.get("error"):
        return jira_issue

    result = call_github_models_json(
        risk_prompt(jira_issue)
    )

    return result


@mcp.tool()
def generate_test_data_from_jira(issue_key: str):
    jira_issue = get_jira_issue(issue_key)

    if jira_issue.get("error"):
        return jira_issue

    result = call_github_models_json(
        test_data_prompt(jira_issue)
    )

    return result


@mcp.tool()
def generate_complete_qa_workbook_from_jira(issue_key: str):
    jira_issue = get_jira_issue(issue_key)

    if jira_issue.get("error"):
        return jira_issue

    scenarios = call_github_models_json(
        scenario_prompt(jira_issue)
    )

    test_cases = call_github_models_json(
        test_case_prompt(jira_issue)
    )

    rtm = call_github_models_json(
        rtm_prompt(jira_issue)
    )

    risks = call_github_models_json(
        risk_prompt(jira_issue)
    )

    test_data = call_github_models_json(
        test_data_prompt(jira_issue)
    )

    return {
        "scenarios": scenarios.get("scenarios", []),
        "test_cases": test_cases.get("test_cases", []),
        "rtm": rtm.get("rtm", []),
        "risks": risks.get("risks", []),
        "test_data": test_data.get("test_data", [])
    }


if __name__ == "__main__":
    mcp.run()