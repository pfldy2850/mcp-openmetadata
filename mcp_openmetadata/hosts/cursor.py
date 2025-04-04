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
@click.option("--editable", is_flag=True, help="Use editable mode")
@click.option(
    "--env", "-e", multiple=True, help="Environment variables to set for the server. Can be used multiple times."
)
def main(editable: bool, env: Optional[tuple[str, ...]] = None):
    config_dir = get_cursor_mcp_config_path()

    server = OpenMetadataMCPServer()

    env_dict: Optional[dict[str, str]] = None
    if env:
        env_dict = {}
        for env_var in env:
            key, value = env_var.split("=", 1)
            env_dict[key.strip()] = value.strip()

    update_mcp_config(
        config_dir=config_dir,
        server_name=server.mcp.name,
        with_packages=server.mcp.dependencies,
        with_editable=Path(__file__).parent.parent.parent if editable else None,
        env_vars=env_dict,
    )


if __name__ == "__main__":
    main()
