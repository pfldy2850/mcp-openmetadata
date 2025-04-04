# Table organizes data in rows and columns and is defined in a Database Schema.
import httpx
from fastmcp import FastMCP


def get_list_of_tables(mcp: FastMCP, session: httpx.Client):
    # https://docs.open-metadata.org/swagger.html#operation/listTables
    @mcp.tool(
        name="get_list_of_tables",
        description="Get a list of tables, optionally filtered by database it belongs to. Use fields parameter to get only necessary fields. Use cursor-based pagination to limit the number entries in the list using limit and before or after query params.",
    )
    def _get_list_of_tables(
        limit: int = 10,
        before: str = None,
        after: str = None,
    ):
        """
        Get a list of tables, optionally filtered by database it belongs to. Use fields parameter to get only necessary fields. Use cursor-based pagination to limit the number entries in the list using limit and before or after query params.
        """
        response = session.get("/api/v1/tables", params={
            "limit": limit,
            "before": before,
            "after": after,
        })
        response.raise_for_status()
        response_json = response.json()

        tables = response_json.get("data", [])
        return [
            {
                "id": table.get("id"),
                "name": table.get("name"),
                "fullyQualifiedName": table.get("fullyQualifiedName"),
                "description": table.get("description"),
                "href": table.get("href"),
            }
            for table in tables
        ]

# Example: fields=tableConstraints,tablePartition,usageSummary,owners,customMetrics,columns,tags,followers,joins,schemaDefinition,dataModel,extension,testSuite,domain,dataProducts,lifeCycle,sourceHash


def _get_table_by_fqn_response(session: httpx.Client, fully_qualified_name: str):
    response = session.get(f"/api/v1/tables/name/{fully_qualified_name}")
    response.raise_for_status()
    return response.json()


def get_table_by_fqn(mcp: FastMCP, session: httpx.Client):
    # https://docs.open-metadata.org/swagger.html#operation/getTableByFQN
    @mcp.tool(
        name="get_table_by_fqn",
        description="Get a table by fully qualified table name.",
    )
    def _get_table_by_fqn(fully_qualified_name: str):
        """
        Get a table by fully qualified table name.

        Args:
            fully_qualified_name (str): Fully qualified name of the table
        """
        response = _get_table_by_fqn_response(session, fully_qualified_name)

        return {
            "id": response.get("id"),
            "name": response.get("name"),
            "fullyQualifiedName": response.get("fullyQualifiedName"),
            "description": response.get("description"),
            "href": response.get("href"),
        }


def get_table_columns_by_fqn(mcp: FastMCP, session: httpx.Client):
    @mcp.tool(
        name="get_table_columns_by_fqn",
        description="Get a table columns by fully qualified table name.",
    )
    def _get_table_columnsby_fqn(fully_qualified_name: str):
        """
        Get a table by fully qualified table name.

        Args:
            fully_qualified_name (str): Fully qualified name of the table
        """

        response = _get_table_by_fqn_response(session, fully_qualified_name)

        return {
            "id": response.get("id"),
            "name": response.get("name"),
            "fullyQualifiedName": response.get("fullyQualifiedName"),
            "description": response.get("description"),
            "href": response.get("href"),
            "columns": response.get("columns"),
        }


def get_table_owners_by_fqn(mcp: FastMCP, session: httpx.Client):
    @mcp.tool(
        name="get_table_owners_by_fqn",
        description="Get a table owners by fully qualified table name.",
    )
    def _get_table_owners_by_fqn(fully_qualified_name: str):
        """
        Get a table by fully qualified table name.

        Args:
            fully_qualified_name (str): Fully qualified name of the table
        """

        response = _get_table_by_fqn_response(session, fully_qualified_name)

        return {
            "id": response.get("id"),
            "name": response.get("name"),
            "fullyQualifiedName": response.get("fullyQualifiedName"),
            "description": response.get("description"),
            "href": response.get("href"),
            "owners": response.get("owners"),
        }


def get_sample_data(mcp: FastMCP, session: httpx.Client):
    # https://docs.open-metadata.org/swagger.html#operation/getSampleData
    @mcp.tool(
        name="get_sample_data",
        description="Get sample data from a table.",
    )
    def _get_sample_data(id: str, offset: int = 0, limit: int = 1):
        """
        Get sample data from a table.

        Args:
            id (str): table Id
        """
        response = session.get(f"/api/v1/tables/{id}/sampleData")
        response.raise_for_status()

        response_json = response.json()
        sample_data = response_json.get("sampleData", {})
        
        columns = sample_data.get("columns", [])
        rows = sample_data.get("rows", [])
        rows = rows[offset:offset+limit]

        return [
            { column: row for column, row in zip(columns, row) } for row in rows
        ]
