from pathlib import Path
from typing import Optional

import click

from mcp_openmetadata.server import OpenMetadataMCPServer
from mcp_openmetadata.utils import update_mcp_config


def get_cursor_mcp_config_path() -> Path | None:
    """Get the Cursor MCP config directory based on platform."""
    path = Path(Path.home(), ".cursor")

    if path.exists():
        return path
    return None


@click.command()
@click.option("--env", "-e", help="Environment variables to set for the server.")
def main(env: Optional[str] = None):
    server = OpenMetadataMCPServer()

    config_dir = get_cursor_mcp_config_path()

    update_mcp_config(
        config_dir=config_dir,
        server_name=server.mcp.name,
        env_vars=env,
    )


if __name__ == "__main__":
    main()
