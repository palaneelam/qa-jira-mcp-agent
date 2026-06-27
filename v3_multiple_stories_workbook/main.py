import asyncio
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

sys.path.insert(0, str(CURRENT_DIR))
sys.path.insert(0, str(PROJECT_ROOT))

from mcp_client import (
    show_available_tools,
    generate_multiple_stories_workbook_from_mcp
)

from excel_generator import export_multiple_stories_workbook


async def option_show_tools():
    await show_available_tools()


async def option_generate_multiple_story_workbook():
    issue_keys = input(
        "\nEnter Jira Issue Keys separated by comma: "
    )

    print("\nGenerating QA workbook for multiple Jira stories...")

    workbook_data = await generate_multiple_stories_workbook_from_mcp(
        issue_keys
    )

    export_multiple_stories_workbook(
        workbook_data
    )


async def main():
    while True:
        print("\n")
        print("=" * 60)
        print("QA Jira MCP Agent - Version 3")
        print("=" * 60)

        print("1. Show Available MCP Tools")
        print("2. Generate QA Workbook for Multiple Jira Stories")
        print("0. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            await option_show_tools()

        elif choice == "2":
            await option_generate_multiple_story_workbook()

        elif choice == "0":
            print("\nExiting Version 3.")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    asyncio.run(main())