from .utils import setup_logger
from .x_api import ClientX
from typing import Any
import asyncio
import httpx
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server, stdio_server
from pydantic import BaseModel, Field, AnyUrl


logger = setup_logger()
server = Server("mcp-x")
client_x = ClientX(logger=logger)


class ToolModel(BaseModel):
    @classmethod
    def as_tool(cls):
        return types.Tool(
            name="x_" + cls.__name__,
            description=cls.__doc__,
            inputSchema=cls.model_json_schema()
        )


class PostTweet(ToolModel):
    """Post a tweet using the X API"""
    tweet_content: str = Field(description="Content of the tweet")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """
    logger.info("Listing available tools")
    tools = [
        PostTweet.as_tool()
    ]
    logger.info(f"Available tools: {[tool.name for tool in tools]}")
    return tools


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle tool execution requests."""
    logger.info(f"Tool called: {name} with arguments: {arguments}")
    assert name[:2] == "x_", f"Invalid tool name: {name}"
    if name[2:] == "PostTweet":
        msg = client_x.create_tweet(arguments["tweet_content"])
        return [types.TextContent(
            type="text",
            text=msg
        )]


async def main():
    logger.info("Starting MCP X server")
    try:
        options = server.create_initialization_options()
        async with stdio_server() as (read_stream, write_stream):
            logger.info("Server initialized successfully")
            await server.run(
                read_stream,
                write_stream,
                options
            )
    except Exception as e:
        logger.error(f"Server error occurred: {str(e)}", exc_info=True)
        raise
