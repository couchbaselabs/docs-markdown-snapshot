[View original HTML](/server/7.2/search/run-searches.html)

> Run a Search query to search and return the contents of a Search index. 

|  | You must [create a Search index](create-search-indexes.md) before you can run a search with the Search Service. |
|  | --------------------------------------------------------------------------------------------------------------- |

You can run a search against a Search index with:

* The [Couchbase Server Web Console](#ui).
* The [Search Service REST API with curl and HTTP](#api).
* A [SQL++ query](#sql).
* The Couchbase SDKs:  
[.NET](../../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md)| [Go](../../../go-sdk/current/howtos/full-text-searching-with-sdk.md)| [Java](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/full-text-search.md)| [Node.js](../../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/full-text-searching-with-sdk.md)| [Python](../../../python-sdk/current/howtos/full-text-searching-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/full-text-searching-with-sdk.md)

## [](#ui)Run a Search with the Web Console

You can use the Web Console to test your Search index before you integrate search into your application.

You can enter a basic search query in the Web Console, or use a [query object](search-request-params.md#query) and other JSON properties for a more complex search.

For more information about how to run a search with the Web Console, see [Run A Simple Search with the Web Console](simple-search-ui.md).

For more information about how to configure a Search index and search for geospatial data, see [Run a Geospatial Search Query with the Web Console](geo-search-ui.md).

## [](#sql)Run a Search with a SQL++ Query

Use the [Query tab](../tools/query-workbench.md) to search using natural-language search and SQL++ features in the same query.

For more information about how to use the Search Service from a SQL++ query, see [Search Functions](../n1ql/n1ql-language-reference/searchfun.md).

## [](#api)Run a Search with the REST API

You can also use the REST API, curl, and HTTP to run a search.

Use a [Search request JSON payload](search-request-params.md) to control how the Search Service returns results.

For more information about how to run a search with the REST API, see [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).

For more information about how to configure a Search index and search for geospatial data, see [Run a Geospatial Search Query with the REST API and curl/HTTP](geo-search-rest-api.md).