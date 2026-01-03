from google.adk.agents import LlmAgent
from google.adk.apps.app import App
from google.adk.models import Gemini
from google.genai import types
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

import os
import google.auth

from .tools.web_search import web_search

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

# yfinance MCP
yfinance_tools = McpToolset(
    connection_params=StdioConnectionParams(
        server_params = StdioServerParameters(
            command="uv",
            args=[
                "--directory",
                os.path.abspath("app/yfinance-mcp-server"),
                "run",
                "server.py"
            ],
        ),
    ),
    # tool_filter=[]
)

root_agent = LlmAgent(
    name="root_agent",
    model=Gemini(
        model="gemini-3-flash-preview",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=[yfinance_tools, web_search],
)

app = App(root_agent=root_agent, name="app")
