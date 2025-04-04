# APIs related to search and suggest.
import httpx
from fastmcp import FastMCP


def search_entities_with_query(mcp: FastMCP, session: httpx.Client):
    # https://docs.open-metadata.org/swagger.html#operation/searchEntitiesWithQuery
    @mcp.tool(
        name="search_entities_with_query",
        description="Search entities using query test. Use query params from and size for pagination. Use sort_field to sort the results in sort_order.",
    )
    def _search_entities_with_query(
        q: str = "*",
    ):
        """
        Search entities using query test. Use query params from and size for pagination. Use sort_field to sort the results in sort_order.

        Args:
            q (str): Default: "*"
                Search Query Text, Pass text for substring match; Pass without wildcards for exact match.
                1. For listing all tables or topics pass q=*
                2. For search tables or topics pass q=search_term
                3. For searching field names such as search by columnNames pass q=columnNames:address , for searching deleted entities, use q=deleted:true
                4. For searching by tag names pass q=tags.tagFQN:user.email
                5. When user selects a filter pass q=query_text AND q=tags.tagFQN:user.email AND platform:MYSQL
                6. Search with multiple values of same filter q=tags.tagFQN:user.email AND tags.tagFQN:user.address
                7. Search by service version and type q=service.type:databaseService AND version:0.1
                8. Search Tables with Specific Constraints q=tableConstraints.constraintType.keyword:PRIMARY_KEY AND NOT tier.tagFQN:Tier.Tier1
                9. Search with owners q=owner.displayName.keyword:owner_name
                NOTE: logic operators such as AND, OR and NOT must be in uppercase
        """

        response = session.get(
            "/api/v1/search/query",
            params={
                "q": q,
            },
        )
        response.raise_for_status()

        response_json = response.json()

        hits = response_json.get("hits", {}).get("hits", [])
        sources = [hit.get("_source", {}) for hit in hits]
        sources = [
            {
                "id": source.get("id"),
                "name": source.get("name"),
                "fullyQualifiedName": source.get("fullyQualifiedName"),
                "description": source.get("description"),
                "owners": source.get("owners"),
            }
            for source in sources
        ]

        return sources
