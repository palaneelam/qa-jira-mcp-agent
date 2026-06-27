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

@mcp.tool()
def generate_complete_qa_workbook_for_multiple_stories(issue_keys: str):
    """
    Accepts comma-separated Jira issue keys and generates QA artifacts for all stories.
    Example: SCRUM-8,SCRUM-9,SCRUM-10
    """

    keys = [
        key.strip()
        for key in issue_keys.split(",")
        if key.strip()
    ]

    all_scenarios = []
    all_test_cases = []
    all_rtm = []
    all_risks = []
    all_test_data = []

    for issue_key in keys:
        jira_issue = get_jira_issue(issue_key)

        if jira_issue.get("error"):
            continue

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

        all_scenarios.extend(
            scenarios.get("scenarios", [])
        )

        all_test_cases.extend(
            test_cases.get("test_cases", [])
        )

        all_rtm.extend(
            rtm.get("rtm", [])
        )

        all_risks.extend(
            risks.get("risks", [])
        )

        all_test_data.extend(
            test_data.get("test_data", [])
        )

    return {
        "scenarios": all_scenarios,
        "test_cases": all_test_cases,
        "rtm": all_rtm,
        "risks": all_risks,
        "test_data": all_test_data
    }

if __name__ == "__main__":
    mcp.run()