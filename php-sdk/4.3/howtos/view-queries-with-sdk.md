[View original HTML](/php-sdk/4.3/howtos/view-queries-with-sdk.html)

> You can use MapReduce views to create queryable indexes in Couchbase Data Platform. 

|  | Although still maintained and supported for legacy use, Views date from the earliest days of Couchbase Server development, and as such are rarely the best choice over, say, [our Query service](n1ql-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for you to use](../concept-docs/data-services.md). Note, if you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](#7.6.6@server:learn:buckets-memory-and-storage/storage-engines.adoc#couchstore) bucket_. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The normal CRUD methods allow you to look up a document by its ID. A MapReduce (_view_ query) allows you to lookup one or more documents based on various criteria. MapReduce views are comprised of a _map_ function that is executed once per document (this is done incrementally, so this is not run each time you query the view) and an optional _reduce_ function that performs aggregation on the results of the _map_ function. The _map_ and _reduce_ functions are stored on the server and written in JavaScript.

MapReduce queries can be further customized during query time to allow only a subset (or range) of the data to be returned.

|  | See the [Incremental MapReduce Views](#7.1@server:learn:views/views-writing.adoc) and [Querying Data with Views](#7.1@server:learn:views/views-querying.adoc) sections of the general documentation to learn more about views and their architecture. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

You can find further information [in the API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-ViewResult.html).