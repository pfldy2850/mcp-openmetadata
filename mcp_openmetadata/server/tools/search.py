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
        index: str = "table_search_index",
        deleted: bool = False,
        from_: int = 0,
        size: int = 10,
        search_after: str = None,
        sort_field: str = "_score",
        sort_order: str = "desc",
        track_total_hits: bool = False,
        query_filter: str = None,
        post_filter: str = None,
        fetch_source: bool = True,
        include_source_fields: list = None,
        get_hierarchy: bool = False,
        explain: bool = False,
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
            index (str): Default: "table_search_index"
                ElasticSearch Index name, defaults to table_search_index
            deleted (boolean): Default: false
                Filter documents by deleted param. By default deleted is false
            from_ (int): Default: 0
                From field to paginate the results
            size (int): Default: 10
                Size field to limit the no.of results returned
            search_after (str): Default: None
                When paginating, specify the search_after values. Use it as search_after=,...
            sort_field (str): Default: "_score"
                Sort the search results by field, available fields to sort weekly_stats, daily_stats, monthly_stats, last_updated_timestamp
            sort_order (str): Default: "desc"
                Sort order asc for ascending or desc for descending
            track_total_hits (boolean): Default: false
                Track Total Hits
            query_filter (str): Default: None
                Elasticsearch query that will be combined with the query_string query generator from the query argument
            post_filter (str): Default: None
                Elasticsearch query that will be used as a post_filter
            fetch_source (boolean): Default: true
                Get document body for each hit
            include_source_fields (list): Default: None
                Get only selected fields of the document body for each hit. Empty value will return all fields
            get_hierarchy (boolean): Default: false
                Fetch search results in hierarchical order of children elements
            explain (boolean): Default: false
                Explain the results of the query. Only for debugging purposes
        """

        response = session.get(
            "/api/v1/search/query",
            params={
                "q": q,
                "index": index,
                "deleted": deleted,
                "from": from_,
                "size": size,
                "search_after": search_after,
                "sort_field": sort_field,
                "sort_order": sort_order,
                "track_total_hits": track_total_hits,
                "query_filter": query_filter,
                "post_filter": post_filter,
                "fetch_source": fetch_source,
                "include_source_fields": include_source_fields,
                "get_hierarchy": get_hierarchy,
                "explain": explain,
            },
        )
        response.raise_for_status()
        return response.json()
