import os
import sys
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

def clean_text(text):
    if not text:
        return ""

    replacements = {
        "₹": "INR",
        "–": "-",
        "—": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text

def get_jira_issue(issue_key: str):
    if not JIRA_BASE_URL or not JIRA_EMAIL or not JIRA_API_TOKEN:
        raise ValueError("Jira environment variables are missing in .env file")

    # url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
    
    print(f"Calling Jira URL: {url}", file=sys.stderr, flush=True)
    print(f"Using email: {JIRA_EMAIL}", file=sys.stderr, flush=True)
    response = requests.get(
        url,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={
            "Accept": "application/json"
        }
    )

    if response.status_code != 200:
        return {
            "error": True,
            "status_code": response.status_code,
            "message": response.text
        }

    data = response.json()
    fields = data.get("fields", {})

    return {
        "issue_key": issue_key,
        "summary": clean_text(fields.get("summary", "")),
        "description": clean_text(extract_adf_text(fields.get("description"))),
        "issue_type": fields.get("issuetype", {}).get("name", ""),
        "status": fields.get("status", {}).get("name", ""),
        "priority": fields.get("priority", {}).get("name", ""),
        "assignee": (
            fields.get("assignee", {}).get("displayName")
            if fields.get("assignee")
            else "Unassigned"
        )
    }


def extract_adf_text(description):
    """
    Jira Cloud description is often stored in Atlassian Document Format.
    This function extracts readable plain text.
    """

    if not description:
        return ""

    text_parts = []

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "text":
                text_parts.append(node.get("text", ""))

            for value in node.values():
                walk(value)

        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(description)

    return " ".join(text_parts)

def search_jira_issues_by_jql(jql: str, max_results: int = 10):
    if not JIRA_BASE_URL or not JIRA_EMAIL or not JIRA_API_TOKEN:
        raise ValueError("Jira environment variables are missing in .env file")

    url = f"{JIRA_BASE_URL}/rest/api/3/search/jql"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
        params={
            "jql": jql,
            "maxResults": max_results,
            "fields": "summary,description,status,issuetype,priority,assignee"
        }
    )

    if response.status_code != 200:
        return {
            "error": True,
            "status_code": response.status_code,
            "message": response.text
        }

    data = response.json()
    issues = []

    for issue in data.get("issues", []):
        fields = issue.get("fields", {})

        issues.append({
            "issue_key": issue.get("key", ""),
            "summary": clean_text(fields.get("summary", "")),
            "description": clean_text(extract_adf_text(fields.get("description"))),
            "issue_type": fields.get("issuetype", {}).get("name", ""),
            "status": fields.get("status", {}).get("name", ""),
            "priority": fields.get("priority", {}).get("name", ""),
            "assignee": (
                fields.get("assignee", {}).get("displayName")
                if fields.get("assignee")
                else "Unassigned"
            )
        })

    return issues