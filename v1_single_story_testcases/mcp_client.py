import os
import sys

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

# ==========================================================
# Project Configuration
# ==========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


def get_client():
    """
    Creates a new MCP client instance.

    A new client is created for every request.
    This avoids stale sessions and 'Connection closed' errors.
    """

    transport = StdioTransport(
        command=sys.executable,
        args=[
            "-m",
            "v1_single_story_testcases.mcp_servers.jira_server"
        ],
        cwd=PROJECT_ROOT
    )

    return Client(transport)


# ==========================================================
# Generic MCP Caller
# ==========================================================

async def call_mcp_tool(tool_name: str, arguments: dict | None = None):
    """
    Calls any MCP Tool.
    """

    try:

        client = get_client()

        async with client:

            result = await client.call_tool(
                tool_name,
                arguments or {}
            )

            # FastMCP generally returns .data
            return result.data

    except Exception as ex:

        print(f"\nMCP Tool Error ({tool_name})")
        print(ex)

        raise


# ==========================================================
# Utility Functions
# ==========================================================

async def show_available_tools():

    try:

        client = get_client()

        async with client:

            tools = await client.list_tools()

            print("\nAvailable MCP Tools:")

            for tool in tools:
                print(f"- {tool.name}")

    except Exception as ex:

        print("\nUnable to retrieve MCP tools")
        print(ex)

        raise


# ==========================================================
# Jira Tools
# ==========================================================

async def read_jira_issue_from_mcp(issue_key: str):

    return await call_mcp_tool(
        "read_jira_issue",
        {
            "issue_key": issue_key
        }
    )


async def generate_test_cases_from_mcp(issue_key: str):

    return await call_mcp_tool(
        "generate_test_cases_from_jira",
        {
            "issue_key": issue_key
        }
    )