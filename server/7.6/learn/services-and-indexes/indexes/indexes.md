[View original HTML](/server/7.6/learn/services-and-indexes/indexes/indexes.html)

> Couchbase Server indexes enhance the performance of query and search operations. 

_Indexes_ are used by certain services, such as _Query_, _Analytics_, and _Search_, as targets for search-routines. Each index makes a predefined subset of data available for the search.

The _Query_ service relies on indexes provided by the _Index_ service. The _Search_ and _Analytics_ services both provide their own indexes, internally.

Indexes, when well-designed, provide significant enhancements to the performance of search-operations.

## [](#indexes)Indexes

The following forms of index are available:

Primary

Provided by the [Index Service](../services/index-service.md), this is based on the unique key of every item in a specified collection. Every primary index is maintained asynchronously. A primary index is intended to be used for simple queries, which have no filters or predicates. For information on primary indexes, see [Using Indexes](global-secondary-indexes.md).

Secondary

Provided by the [Index Service](../services/index-service.md), this is based on an attribute _within_ a document. The value associated with the attribute can be of any type: scalar, object, or array.

A Secondary Index is frequently referred to as a _Global Secondary Index_, or _GSI_. This is the kind of index used most frequently in Couchbase Server, for queries performed with SQL++. For information on Global Secondary Indexes, see [Using Indexes](global-secondary-indexes.md).

Search

Provided by the [Search Service](../services/search-service.md), this is a specially purposed index, which contains targets derived from the contents of documents within one or more specified keyspaces. Search indexes support text matching, geospatial, date-time, numeric range searches, and more. For text matching, you can add filters to remove undesirable characters from input and target text values, such as punctuation marks or HTML tags. For information on how to create Search indexes, see [Create a Search Index](../../../search/create-search-indexes.md).

Vector Search

Provided by the [Search Service](../services/search-service.md), this is a type of Search index which supports vector embeddings. Use Vector Search indexes to run searches with the Search service using vector comparisons. You can use Vector Search indexes for Retrieval Augmented Generation (RAG) with an existing Large Language Model (LLM). To create Vector Search indexes, see [Create a Vector Search Index with the Server Web Console](../../../vector-search/create-vector-search-index-ui.md) or [Create a Vector Search Index with the REST API and curl/HTTP](../../../vector-search/create-vector-search-index-rest-api.md).

Analytics

Provided by the [Analytics Service](../services/analytics-service.md), this is a materialized access path for the shadow data in an Analytics collection. Analytics indexes can be used to speed up Analytics selection queries and join queries. If changes in operational data result in corresponding modifications to shadow data, Analytics indexes are updated automatically. See the section on [Using Indexes](../../../analytics/7%5Fusing%5Findex.md) in Couchbase Analytics.

View

Supports [Couchbase Views](../../views/views-intro.md), with fields and information extracted from documents. Views are deprecated in Couchbase Server 7.0, and will be removed in a future release.