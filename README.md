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


## Tool list
mcp-openmetadata does not provide all APIs available in OpenMetadata.
Please refer to [Supported APIs](https://github.com/pfldy2850/mcp-openmetadata/blob/main/README-API.md) for the list of available APIs.

Since using the original API directly contains too much unnecessary data that is difficult to fit into the model context, we are working on returning somewhat organized results.

### Search Tools
- `search_entities_with_query`: Search entities using query text. Supports pagination and sorting. Useful for:
  - Listing all tables/topics (q=*)
  - Searching by field names (e.g., q=columnNames:address)
  - Searching by tags (e.g., q=tags.tagFQN:user.email)
  - Complex queries with AND/OR operators
  - Filtering by service type, constraints, owners, etc.

### Table Tools
- `get_list_of_tables`: Get a paginated list of tables with basic information
- `get_table_by_fqn`: Get detailed table information by fully qualified name
- `get_table_columns_by_fqn`: Get table columns information by fully qualified name
- `get_table_owners_by_fqn`: Get table ownership information by fully qualified name
- `get_sample_data`: Get sample data from a specified table

Each tool returns optimized responses with relevant fields to ensure compatibility with model context limits while providing essential metadata information.




## License

This project is open source software [licensed as MIT](https://opensource.org/licenses/MIT).