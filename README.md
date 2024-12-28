# mcp-x MCP server

MCP project to connect Claude with X API. Built on top of [X API v2](https://developer.x.com/en/docs/x-api)

# Demo
![video-demo](https://github.com/Lyonsupernova/mcp-x/blob/main/media/demo.mp4)

# Supported Features
- Post tweets

# Configuration

## Getting Started with X
- Go to [X Developer Platform](https://developer.x.com/en) and login with your X account
- Start with Basic plan
- Store the Access Token, Secret, Client ID, Client Secret and Bearer token
Docs: [x-api-start](https://developer.x.com/en/docs/x-api/getting-started/getting-access-to-the-x-api)

## Set up 
- On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%/Claude/claude_desktop_config.json`


```json
{
  "mcpServers": {
    "x": {
      "command": "uv",
      "args": [
        "--directory",
        "PROJECT_PATH/src/mcp_x",
        "run",
        "mcp-x"
      ],
      "env": {
        "X_API_KEY": "YOUR_API_KEY",
        "X_API_KEY_SECRET": "YOUR_API_KEY_SECRET",
        "X_ACCESS_TOKEN": "YOUR_ACCESS_TOKEN",
        "X_ACCESS_TOKEN_SECRET": "YOUR_ACCESS_TOKEN_SECRET",
        "X_BEARER_TOKEN": "YOUR_BEARER_TOKEN",
        "LOGGING_PATH": "PROJECT_PATH/src/mcp_x/logs"
      }
    }
  }
}
```

## TODO

- Tests
- Add Get tweets
- Add Delete tweets
- ...

## Deployment

(todo)

### Building and Publishing

To prepare the package for distribution:

1. Sync dependencies and update lockfile:
```bash
uv sync
```

2. Build package distributions:
```bash
uv build
```

This will create source and wheel distributions in the `dist/` directory.
