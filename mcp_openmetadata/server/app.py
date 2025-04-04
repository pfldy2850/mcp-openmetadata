import httpx
from fastmcp import FastMCP

from mcp_openmetadata.server import tools
from mcp_openmetadata.server.settings import Settings


class OpenMetadataMCPServer:
    def __init__(self):
        self.mcp = FastMCP("OpenMetadata", dependencies=["httpx"])
        self.settings = Settings()

        self.session = self._create_session()

        self.mount_tools()

    def _create_session(self):
        session = httpx.Client(
            base_url=self.settings.openmetadata_uri, headers=self.settings.authorization
        )
        return session

    def mount_tools(self):
        if self.settings.tools:
            for tool in self.settings.tools.split(","):
                self.mcp.mount(f"openmetadata_{tool}", getattr(tools, f"{tool}_tool"))

                if hasattr(tools, tool):
                    register_tool = getattr(tools, tool)
                    register_tool(self.mcp, self.session)
                else:
                    raise ValueError(f"Tool {tool} not found")
        else:
            raise ValueError("No tools to mount")

    def run(self):
        self.mcp.run()
