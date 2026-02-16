[View original HTML](/server/current/learn/services-and-indexes/indexes/indexes.html)

> Couchbase Server uses indexes to improve the performance of queries and searches. Each index makes a specific subset of data available for searching. 

The Query Service uses indexes from the [Index Service](../services/index-service.md). The [Search](../services/search-service.md) and [Analytics Services](../services/analytics-service.md) create and use their own indexes.

Couchbase Server supports two classes of indexes: [Traditional Indexes](#traditional-indexes) and [Vector Indexes](#vector-indexes).

## [](#traditional-indexes)Traditional Indexes

You can use the following types of indexes for traditional scalar data:

Primary

The [Index Service](../services/index-service.md) provides primary indexes based on the unique key of each item in a collection. Couchbase Server maintains every primary index asynchronously. Use a primary index for basic queries without filters or predicates. For more information about primary indexes, see [Primary and Secondary Index Reference](../../../indexes/indexing-overview.md).

Secondary

The [Index Service](../services/index-service.md) provides secondary indexes based on attributes in a document. The attribute value can be a scalar, object, or array.

A secondary index is also called a Global Secondary Index (GSI). Most queries in Couchbase Server use GSIs with SQL++. For more information about Global Secondary Indexes, see [Primary and Secondary Index Reference](../../../indexes/indexing-overview.md).

Search

The [Search Service](../services/search-service.md) provides Search indexes that support text matching, geospatial, date-time, and numeric range searches. For text matching, you can add filters to remove unwanted characters from input and target text, such as punctuation marks or HTML tags. For more information about creating Search indexes, see [Create a Search Index](../../../search/create-search-indexes.md).

Analytics

The [Analytics Service](../services/analytics-service.md) provides analytics indexes for shadow data in an Analytics collection. Analytics indexes speed up selection and join queries in Analytics. When operational data changes, Couchbase Server updates analytics indexes automatically. For more information about using analytics indexes, see [Using Indexes](../../../analytics/7%5Fusing%5Findex.md).

Views

[Couchbase Views](../../views/views-intro.md) extract fields and information from documents to create their own index.

|  | Views were deprecated in Couchbase Server 7.0 and will be removed in a future release. |
|  | -------------------------------------------------------------------------------------- |

## [](#vector-indexes)Vector Indexes

Couchbase Server also supports indexes for vector search. These indexes let you perform semantic similarity searches that form the basis of AI applications. See [Use Vector Indexes for AI Applications](../../../vector-index/vectors-and-indexes-overview.md) for more information about using vector indexes.

Hyperscale Vector Indexes

The Index Service provides [Hyperscale Vector Indexes](../../../vector-index/hyperscale-vector-index.md) which index a single vector column. They offer the highest performance of any index when it comes to vector data. These indexes can scale up to a billion documents containing vectors with a large number of dimensions.

Composite Vector Indexes

The Index Service provides [Composite Vector Indexes](../../../vector-index/composite-vector-index.md) which are Global Secondary Indexes (GSIs) with a single vector column. These indexes let your application use searches for scalar, array, and object index entries to pre-filter the dataset before performing a vector similarity search.

Search Vector Indexes

The Search Service provides [Search Vector Indexes](../../../vector-search/vector-search.md) that support a single vector column. You can use Search Vector Indexes for tasks such as Retrieval Augmented Generation (RAG) with a Large Language Model (LLM).