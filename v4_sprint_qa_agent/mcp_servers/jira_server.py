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

from jira_client import (
    get_jira_issue,
    search_jira_issues_by_jql
)

from prompts import (
    scenario_prompt,
    test_case_prompt,
    rtm_prompt,
    risk_prompt,
    test_data_prompt,
    cross_story_risk_prompt,
    sprint_summary_prompt
)
from prompts import complete_qa_artifacts_prompt

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

        artifacts = call_github_models_json(
            complete_qa_artifacts_prompt(jira_issue)
        )

        all_scenarios.extend(artifacts.get("scenarios", []))
        all_test_cases.extend(artifacts.get("test_cases", []))
        all_rtm.extend(artifacts.get("rtm", []))
        all_risks.extend(artifacts.get("risks", []))
        all_test_data.extend(artifacts.get("test_data", []))

    return {
        "scenarios": all_scenarios,
        "test_cases": all_test_cases,
        "rtm": all_rtm,
        "risks": all_risks,
        "test_data": all_test_data
    }

@mcp.tool()
def search_issues_by_jql(jql: str, max_results: int = 10):
    try:
        response = search_jira_issues_by_jql(jql, max_results)

        if not response:
            return []

        if response.get("error"):
            return response

        issues = []

        for issue in response.get("issues", []):
            if not issue:
                continue

            fields = issue.get("fields") or {}

            issue_type = fields.get("issuetype") or {}
            status = fields.get("status") or {}
            priority = fields.get("priority") or {}
            assignee = fields.get("assignee") or {}
            reporter = fields.get("reporter") or {}

            issues.append({
                "issue_key": issue.get("key", ""),
                "summary": fields.get("summary") or "",
                "description": fields.get("description") or "",
                "issue_type": issue_type.get("name", "Unknown"),
                "status": status.get("name", "Unknown"),
                "priority": priority.get("name", "Unassigned"),
                "assignee": assignee.get("displayName", "Unassigned"),
                "reporter": reporter.get("displayName", "Unknown")
            })

        return issues

    except Exception as e:
        return {
            "error": True,
            "message": str(e)
        }


@mcp.tool()
def generate_sprint_qa_workbook(jql: str, max_results: int = 10):
    """
    Generate sprint-level QA workbook from Jira issues found by JQL.
    """

    jira_issues = search_jira_issues_by_jql(
        jql,
        max_results
    )

    if isinstance(jira_issues, dict) and jira_issues.get("error"):
        return jira_issues

    all_scenarios = []
    all_test_cases = []
    all_rtm = []
    all_risks = []
    all_test_data = []

    for jira_issue in jira_issues:
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

    cross_story_risks = call_github_models_json(
        cross_story_risk_prompt(jira_issues)
    )

    sprint_summary = call_github_models_json(
        sprint_summary_prompt(jira_issues)
    )

    return {
        "issues": jira_issues,
        "scenarios": all_scenarios,
        "test_cases": all_test_cases,
        "rtm": all_rtm,
        "risks": all_risks,
        "test_data": all_test_data,
        "cross_story_risks": cross_story_risks.get("cross_story_risks", []),
        "sprint_summary": sprint_summary.get("sprint_summary", [])
    }

if __name__ == "__main__":
    mcp.run()