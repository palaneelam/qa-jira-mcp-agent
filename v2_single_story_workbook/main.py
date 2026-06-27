import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

sys.path.insert(0, str(CURRENT_DIR))
sys.path.insert(0, str(PROJECT_ROOT))

import asyncio

from mcp_client import (
    show_available_tools,
    read_jira_issue_from_mcp,
    generate_test_cases_from_mcp,
    generate_scenarios_from_mcp,
    generate_rtm_from_mcp,
    generate_risks_from_mcp,
    generate_test_data_from_mcp,
    generate_complete_workbook_from_mcp
)

from excel_generator import (
    export_test_cases,
    export_complete_workbook
)

async def option_show_tools():
    await show_available_tools()


async def option_read_jira_issue():
    issue_key = input("\nEnter Jira Issue Key: ")

    issue = await read_jira_issue_from_mcp(issue_key)

    print("\nJira Issue Details:")
    print(issue)


async def option_generate_test_cases():
    issue_key = input("\nEnter Jira Issue Key: ")

    print("\nGenerating test cases from Jira issue...")

    test_cases = await generate_test_cases_from_mcp(issue_key)

    if isinstance(test_cases, dict) and test_cases.get("error"):
        print("\nError:")
        print(test_cases)
        return

    print("\nTest Cases Object:")
    print(test_cases)
    print("Type:", type(test_cases))

    export_test_cases(
        test_cases,
        issue_key
    )


async def main():
    while True:
        print("\n")
        print("=" * 60)
        print("QA Jira MCP Agent")
        print("=" * 60)

        print("1. Show Available MCP Tools")
        print("2. Read Jira Issue")
        print("3. Generate Test Cases from Jira Issue")
        print("4. Generate Complete QA Workbook from Jira Issue")
        print("0. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            await option_show_tools()

        elif choice == "2":
            await option_read_jira_issue()

        elif choice == "3":
            await option_generate_test_cases()

        elif choice == "4":
            await option_generate_complete_workbook()

        elif choice == "0":
            print("\nExiting QA Jira MCP Agent.")
            break

        else:
            print("\nInvalid option. Please try again.")

async def option_generate_complete_workbook():
    issue_key = input("\nEnter Jira Issue Key: ")

    print("\nGenerating complete QA workbook from Jira issue...")

    workbook_data = await generate_complete_workbook_from_mcp(issue_key)

    if isinstance(workbook_data, dict) and workbook_data.get("error"):
        print("\nError:")
        print(workbook_data)
        return

    export_complete_workbook(
        workbook_data,
        issue_key
    )

if __name__ == "__main__":
    asyncio.run(main())