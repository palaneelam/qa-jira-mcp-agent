import asyncio
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

sys.path.insert(0, str(CURRENT_DIR))
sys.path.insert(0, str(PROJECT_ROOT))

from mcp_client import (
    show_available_tools,
    search_issues_by_jql_from_mcp,
    generate_sprint_workbook_from_mcp
)

from excel_generator import export_sprint_workbook


async def option_show_tools():
    await show_available_tools()


async def option_search_issues():
    jql = input("\nEnter Jira JQL: ")
    max_results = int(input("Max results: "))

    issues = await search_issues_by_jql_from_mcp(
        jql,
        max_results
    )

    print("\nRaw MCP Response:")
    print(issues)

    if issues is None:
        print("\nNo response received from MCP tool.")
        return

    if isinstance(issues, dict) and issues.get("error"):
        print("\nJira Error:")
        print(issues)
        return

    if not isinstance(issues, list):
        print("\nUnexpected response format:")
        print(type(issues))
        print(issues)
        return

    print("\nJira Issues Found:")

    for issue in issues:
        print(
            f"{issue.get('issue_key')} | "
            f"{issue.get('summary')} | "
            f"{issue.get('status')}"
        )


async def option_generate_sprint_workbook():
    jql = input("\nEnter Jira JQL: ")
    max_results = int(input("Max results: "))

    print("\nGenerating Sprint QA Workbook...")

    workbook_data = await generate_sprint_workbook_from_mcp(
        jql,
        max_results
    )

    if isinstance(workbook_data, dict) and workbook_data.get("error"):
        print("\nError:")
        print(workbook_data)
        return

    export_sprint_workbook(
        workbook_data
    )


async def main():
    while True:
        print("\n")
        print("=" * 60)
        print("QA Jira MCP Agent - Version 4")
        print("=" * 60)

        print("1. Show Available MCP Tools")
        print("2. Search Jira Issues by JQL")
        print("3. Generate Sprint QA Workbook")
        print("0. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            await option_show_tools()

        elif choice == "2":
            await option_search_issues()

        elif choice == "3":
            await option_generate_sprint_workbook()

        elif choice == "0":
            print("\nExiting Version 4.")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    asyncio.run(main())