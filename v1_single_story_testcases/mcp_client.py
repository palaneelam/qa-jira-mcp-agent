from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport


def get_server_path():
    return (
        Path(__file__).parent
        / "mcp_servers"
        / "jira_server.py"
    )


async def call_mcp_tool(tool_name, arguments=None):
    server_path = get_server_path()

    transport = PythonStdioTransport(
    script_path=str(server_path),
    env={
        "PYTHONIOENCODING": "utf-8",
        "PYTHONUTF8": "1"
        }
    )

    client = Client(transport)

    async with client:
        result = await client.call_tool(
            tool_name,
            arguments or {}
        )

        return result.data


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