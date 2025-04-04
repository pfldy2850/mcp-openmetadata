# MCP OpenMetadata

[![PyPI version](https://badge.fury.io/py/mcp-openmetadata.svg)](https://badge.fury.io/py/mcp-openmetadata)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

MCP server providing OpenMetadata APIs - A FastMCP integration for OpenMetadata services.

## Features

- OpenMetadata API integration with FastMCP
- Easy-to-use interface for metadata management
- Support for table metadata, sample data, and ownership information

## Installation

### from PyPi (Cursor)

Install it to Cursor with (uv):
```sh
uv pip install mcp-openmetadata

uv run python -m mcp-openmetadata.hosts.cursor \
  -e OPENMETADATA_URI=<YOUR OPENMETADATA URI> \
  -e OPENMETADATA_JWT_TOKEN=<YOUR OPENMETADATA JWT TOKEN>
```

Install it to Cursor with (pip):
```sh
pip install mcp-openmetadata

python -m mcp-openmetadata.hosts.cursor \
  -e OPENMETADATA_URI=<YOUR OPENMETADATA URI> \
  -e OPENMETADATA_JWT_TOKEN=<YOUR OPENMETADATA JWT TOKEN>
```

### from configuration
```json
{
    "mcpServers": {
        "OpenMetadata": {
            "command": "uv",
            "args": [
                "run",
                "--with",
                "fastmcp",
                "--with",
                "httpx",
                "--with",
                "mcp-openmetadata",
                "python",
                "-m",
                "mcp_openmetadata.server"
            ],
            "env": {
                "OPENMETADATA_URI": "http://localhost:8585",
                "OPENMETADATA_JWT_TOKEN": "awesome_jwt_token"
            }
        }
    }
}
```



## Environment Variables

### Authorization
mcp-openmetadata provides token auth and basic auth:

**Token Auth**
```
OPENMETADATA_URI=http://localhost:8585
OPENMETADATA_JWT_TOKEN=<YOUR OPENMETADATA JWT TOKEN>
```

**Basic Auth**
```
OPENMETADATA_URI=http://localhost:8585
OPENMETADATA_USERNAME=<YOUR OPENMETADATA USERNAME>
OPENMETADATA_PASSWORD=<YOUR OPENMETADATA PASSWORD>
```


## API list
mcp-openmetadata does not provide all APIs available in OpenMetadata.
Please refer to [Supported APIs](https://github.com/pfldy2850/mcp-openmetadata/blob/main/README-API.md) for the list of available APIs.

Since using the original API directly contains too much unnecessary data that is difficult to fit into the model context, we are working on returning somewhat organized results.


## License

This project is open source software [licensed as MIT](https://opensource.org/licenses/MIT).