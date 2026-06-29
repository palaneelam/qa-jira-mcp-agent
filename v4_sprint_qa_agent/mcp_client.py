# from pathlib import Path

# from fastmcp import Client
# from fastmcp.client.transports import PythonStdioTransport

# import json

import json
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SERVER_PATH = os.path.join(
    BASE_DIR,
    "mcp_servers",
    "jira_server.py"
)

transport = PythonStdioTransport(
    script_path=SERVER_PATH,
    python_cmd="python",
    cwd=os.path.dirname(BASE_DIR)
)

client = Client(transport)

def get_server_path():
    return (
        Path(__file__).parent
        / "mcp_servers"
        / "jira_server.py"
    )

def create_transport():
    server_path = get_server_path()

    print("MCP Server Path:", server_path)
    print("MCP Server Exists:", server_path.exists())

    return PythonStdioTransport(
        script_path=str(server_path),
        env={
            "PYTHONIOENCODING": "utf-8",
            "PYTHONUTF8": "1"
        }
    )

async def call_mcp_tool(tool_name, arguments=None):
    transport = create_transport()
    client = Client(transport)

    async with client:
        result = await client.call_tool(
            tool_name,
            arguments or {}
        )

        print("\nRAW FASTMCP RESULT:")
        print(result)
        print("RESULT TYPE:", type(result))

        if result is None:
            return None

        if hasattr(result, "data") and result.data is not None:
            return result.data

        if hasattr(result, "structured_content") and result.structured_content is not None:
            return result.structured_content

        if hasattr(result, "content") and result.content:
            first_content = result.content[0]

            if hasattr(first_content, "text"):
                text = first_content.text

                try:
                    return json.loads(text)
                except Exception:
                    return text

        return result


async def show_available_tools():
    server_path = get_server_path()

    transport = PythonStdioTransport(
        script_path=str(server_path)
    )

    client = Client(transport)

    async with client:
        tools = await client.list_tools()

        print("\nAvailable MCP Tools:")

        for tool in tools:
            print(f"- {tool.name}")


async def read_jira_issue_from_mcp(issue_key):
    return await call_mcp_tool(
        "read_jira_issue",
        {
            "issue_key": issue_key
        }
    )


async def generate_test_cases_from_mcp(issue_key):
    return await call_mcp_tool(
        "generate_test_cases_from_jira",
        {
            "issue_key": issue_key
        }
    )

async def generate_scenarios_from_mcp(issue_key):
    return await call_mcp_tool(
        "generate_test_scenarios_from_jira",
        {
            "issue_key": issue_key
        }
    )


async def generate_rtm_from_mcp(issue_key):
    return await call_mcp_tool(
        "generate_rtm_from_jira",
        {
            "issue_key": issue_key
        }
    )


async def generate_risks_from_mcp(issue_key):
    return await call_mcp_tool(
        "generate_risks_from_jira",
        {
            "issue_key": issue_key
        }
    )


async def generate_test_data_from_mcp(issue_key):
    return await call_mcp_tool(
        "generate_test_data_from_jira",
        {
            "issue_key": issue_key
        }
    )


async def generate_complete_workbook_from_mcp(issue_key):
    return await call_mcp_tool(
        "generate_complete_qa_workbook_from_jira",
        {
            "issue_key": issue_key
        }
    )

async def generate_multiple_stories_workbook_from_mcp(issue_keys):
    return await call_mcp_tool(
        "generate_complete_qa_workbook_for_multiple_stories",
        {
            "issue_keys": issue_keys
        }
    )

async def search_issues_by_jql_from_mcp(jql, max_results=10):
    return await call_mcp_tool(
        "search_issues_by_jql",
        {
            "jql": jql,
            "max_results": max_results
        }
    )


async def generate_sprint_workbook_from_mcp(jql, max_results=10):
    return await call_mcp_tool(
        "generate_sprint_qa_workbook",
        {
            "jql": jql,
            "max_results": max_results
        }
    )