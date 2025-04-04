from mcp_openmetadata.server.app import OpenMetadataMCPServer


def main():
    server = OpenMetadataMCPServer()
    server.run()


if __name__ == "__main__":
    main()
