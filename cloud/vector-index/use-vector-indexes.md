---
title: Choose the Right Vector Index
description: Use Couchbase Capella's vector indexes to find documents based on
  content similarity or semantic meaning.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/vector-index/pages/use-vector-indexes.adoc
  xref: xref:cloud:vector-index:use-vector-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/vector-index/use-vector-indexes.html)

# Choose the Right Vector Index

> Use Couchbase Capella's vector indexes to find documents based on content similarity or semantic meaning. 

Couchbase Capella supports three types of vector indexes. You store vectors as attributes in your documents and index them using one of the three types of vector indexes. You can then find relevant data by executing queries of the vector attributes which use the index to find similar vectors.

As with other data types in Couchbase Capella, indexes make searching for similar vectors much faster. Using indexes for vector searches is especially important due to the size of vector data. Vectors contain hundreds to thousands of dimensions. Using indexes reduces the resources needed to perform vector searches.

If you're unfamiliar with vectors and vector indexing, see [Use Vector Indexes for AI Applications](vectors-and-indexes-overview.md) for an overview.

The three types of Couchbase Capella vector indexes are:

Hyperscale Vector Indexes

* Specifically designed for vector searches.
* Perform vector similarity and semantic searches faster than the other types of indexes.
* Designed to scale to billions of vectors.
* Most of the index resides in a highly optimized format on disk.
* High accuracy even for vectors with a large number of dimensions.
* Supports concurrent searches and inserts for datasets that are constantly changing.

Use this type of index when you want to primarily query vector values with a low memory footprint. In general, Hyperscale Vector indexes are the best choice for most applications that use vector searches.

See [Vector Search Using Hyperscale Vector Indexes](hyperscale-vector-index.md) for more information.

Composite Vector Indexes

* Combine a standard [Global Secondary index (GSI)](../guides/create-index.md#creating-a-secondary-index) with a single vector column.
* Designed for searches using a single vector value along with standard scalar values that filter out large portions of the dataset. The scalar attributes in a query reduce the number of vectors the Couchbase Capella has to compare when performing a vector search to find similar vectors.
* Consume a moderate amount of memory and can index billions of documents.
* Work well for cases where your queries are highly selective — returning a small number of results from a large dataset.

Use Composite Vector indexes when you want to perform searches of documents using both scalars and a vector where the scalar values filter out large portions of the dataset.

To learn how to use Composite Vector indexes, see [Filtered Search Using Composite Vector Indexes](composite-vector-index.md).

Search Vector Indexes

* Combine a Couchbase Capella Search index with a single vector column.
* Allow hybrid searches that combine vector searches with Full-Text Search (FTS) and geospatial searches.
* Can index millions of documents.

Use this index type when you need to perform hybrid searches that combine vectors with full-text or geospatial searches.

To learn how to use Search Vector Indexes, see [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md).

## [](#choosing-the-right-index-type)Choosing the Right Index Type

When choosing which type of index to use, you must consider:

* The size of your dataset.
* Whether you need to perform hybrid searches that combine scalar value or text searches along with the vector search.
* The performance requirements of your application.

The following table summarizes the differences between the three types of vector indexes:

|                                | Hyperscale Vector Index                                                                                                                                                                                                                                        | Composite Vector Index                                                                                                                                                                                                                                                             | Search Vector Index                                                                                                                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **First Available in Version** | 8.0                                                                                                                                                                                                                                                            | 8.0                                                                                                                                                                                                                                                                                | 7.6                                                                                                                                                                                                      |
| **Dataset Size**               | Tens of millions to billions of documents                                                                                                                                                                                                                      | Tens of millions to billion                                                                                                                                                                                                                                                        | Tens of millions                                                                                                                                                                                         |
| **Uses**                       | Pure vector searches Content discovery or recommendations                                                                                                                                                                                                      | Searches combining vector and scalar values where scalar values are less selective (20% or less) Searches where scalars should exclude vectors, such as compliance uses                                                                                                            | Hybrid searches combining vector and keywords or geospatial                                                                                                                                              |
| **Strengths**                  | High performance for pure vector searches Higher accuracy at lower quantizations (fewer bits per vector) Low memory footprint Lowest TCO for huge datasets Best option for concurrent updates and searches Scalars and vector values compared at the same time | Scalar values pre-filter data to reduce the scope of vector searches Efficient when scalar values have low selectivity (exclude less than 20% of dataset) Can restrict searches based on scalars for use cases such as compliance Based on familiar Global Secondary Indexes (GSI) | Combines semantic and Full-Text Search and geospatial search in a single pass Uses familiar Search indexes                                                                                               |
| **Limitations**                | Indexing can take longer relative to other index types                                                                                                                                                                                                         | Lower accuracy than Hyperscalar when using lower quantizations (fewer bits per vector) Scalar values filter data before vector search, potentially missing relevant results (see [note](#scalar-handling))                                                                         | Not as efficient as Composite Vector indexes if the search includes purely numeric or scalar values Does not scale to the extent of the other index types Limited to approximately 100 million documents |

> [!NOTE]
> A key difference between Hyperscale and Composite Vector indexes is how they handle scalar values in queries. Hyperscale Vector indexes compare vectors and scalar values at the same time. Composite Vector indexes always apply scalar filters first, and only perform vector searches on the results. This behavior means Composite Index searches can exclude relevant vectors from the search result. However, it's useful for cases where you must exclude some vectors (even the nearest neighbors) based on scalar values. For example, it's useful when meeting compliance requirements.

When choosing which type of index to use, consider the following:

* In most cases, test using a Hyperscale Vector index. If you find that the performance is not what you need, you can try using one of the other index types.
* If your dataset will not grow beyond 100 million documents and you need to perform hybrid searches that combine vector searches with other Search Service features, such as text or geospatial search, use a Search Vector Index.

## [](#applications-for-vector-indexes)Applications for Vector Indexes

Each type of index works best for different types of applications. The following sections explain several common applications for each type of vector index. They also describe the workflow your application follows when using each type of index.

### [](#hyperscale-vector-index-applications)Hyperscale Vector Index Applications

Hyperscale Vector indexes contain a single vector column. They excel at indexing huge datasets that can scale into the billions of documents. They're optimized for pure vector searches, such as content discovery or recommendations.

The Hyperscale Vector index works well for applications such as:

Reverse image searches

Embedded vectors for images often contain up to thousands of dimensions, which Hyperscale Vector indexes handle better than other index types.

Chatbot context matching

Chatbot context for workflows like retreival-augmented generation (RAG) requires a huge dataset for accurate results. The large dataset gives the chatbot a depth of knowledge that's not necessary in simpler applications.

Anomaly detection

Anomaly detection applications, such as those used in Internet of Things (IoT) sensor networks, require huge datasets to find deviations from expected patterns. Hyperscale Vector indexes can handle the large datasets and perform these vector searches fast.

### [](#hyperscale-vector-index-application-workflow)Hyperscale Vector Index Application Workflow

To create and use a Hyperscale Vector index, your application follows the workflow shown in the following diagram:

![Application Workflow with Hyperscale Vector Indexes](_images/hyperscale-vector-app-workflow-fe0d68b4ed3afd21a92d9aa98940afc6faba8259.svg) 

Figure 1\. Application Workflow with Hyperscale Vector Indexes

The steps shown in the diagram are:

1. When your application loads data with a complex data field it wants to search semantically, it calls an embedding model to generate a vector for it.
2. It sends the data, including the vector, to Couchbase Capella for storage.
3. The Data Service sends the embedded vector to the Indexing Service for inclusion in the Hyperscale Vector index.
4. When your application needs to search for documents related to a complex piece of data, it uses the same embedding model to generate a vector for the search value.
5. It sends the vector as part of the query to the Couchbase Capella Query Service.
6. The Query Service sends a request to the Index Service for an index scan.
7. The Index Service performs an index scan in the Hyperscale Vector index to find similar vectors to the search vector. It sends the results of the scan back to the Query Service.
8. The Query Service returns query results to your application.

See [Vector Search Using Hyperscale Vector Indexes](hyperscale-vector-index.md) for more information about Hyperscale Vector indexes.

### [](#composite-vector-index-applications)Composite Vector Index Applications

Composite Vector indexes contain a single vector column and one or more scalar columns. They apply scalar filters before performing a vector similarity search. This is ideal for workflows where you want to exclude large portions of the dataset to reduce the number of vectors that the vector search has to compare. Composite Vector indexes work well for applications such as:

Content recommendations

Viewers often want hard constraints on their searches, such as genre, language, or favorites actors or directors. Composite Vector indexes can filter using these constraints before performing a vector similarity search on fields such as the plot description or reviews.

Job searches

Job seekers often want to filter jobs based on location, salary, or job title. Composite Vector indexes can filter using these constraints before performing a vector similarity search on fields such as the job description or required skills.

Supply chain management

Supply chain management applications often need to query based on product type, supplier, or location. Vector similarity searches can be added to these searches to find similar demand patterns.

### [](#composite-vector-index-application-workflow)Composite Vector Index Application Workflow

To create and use a Composite Vector index, your application follows the workflow shown in the following diagram:

![Application Workflow with Composite Vector Indexes](_images/composite-vector-app-workflow-658f3a05c4d4c29fa54eb78dea77ae69c7d477cb.svg) 

Figure 2\. Application Workflow with Composite Vector Indexes

The steps shown in the diagram are:

1. When your application loads data with a complex data field it wants to search semantically, it calls an embedding model to generate a vector for it.
2. It sends the data, including the vector, to Couchbase Capella for storage.
3. The Data Service sends the embedded vector along with scalar fields to the Indexing Service for inclusion in the Composite Vector index.
4. When your application needs to perform a query that includes a vector, it uses the same embedding model to generate a vector for the search value.
5. It sends the vector and scalar values as part of a query to the Couchbase Capella Query Service.
6. The Query Service requests index scans for the scalar values and a vector similarity search from the Indexing Service.
7. The Indexing Service performs an index scan in the Composite Vector index to find documents that match the scalar fields. It then performs the vector similarity search on the results of the scalar index scan. Finally, it sends the results of the similarity search back to the Query Service.
8. The Query Service returns the query results to your application.

See [Filtered Search Using Composite Vector Indexes](composite-vector-index.md) for more information about Composite Vector indexes.

### [](#fts)Search Vector Index Applications

Search Vector Indexes contain a single vector column in addition to a Full-Text Search index. Some of the applications for Search Vector Indexes include:

E-Commerce product recommendations

E-Commerce applications can use scalar, text, and vector searches to find products that match a customer's search. For example, a customer could search for red sneakers (text) that cost less than $100 (scalar) and are similar to an uploaded image of a sneaker (vector).

Travel recommendations

Users often want to search for hotels using multiple criteria:

* Limiting searches to a specific area (for example, "walking distance to the Louvre") which relies on geospatial data.
* Specific keywords for features they want, such as "quiet", "romantic", or "gym", which requires Full-Text Search.
* Semantic searches of descriptions and reviews for searches that do not rely on literal text matches, such as "modern beach resort with chic décor," which requires vector searches.

A Search Vector Index can combine geospatial, keyword, and semantic searches into a single index.

Real estate searches

Real estate applications can use Search Vector Indexes to find properties within a search region and have floor plan similar to an uploaded image.

### [](#search-vector-index-application-workflow)Search Vector Index Application Workflow

To create and use a Search Vector Index, your application follows the workflow shown in the following diagram:

![Application Workflow with Search Vector Indexes](_images/fts-app-workflow-8a4286d6c01260f86e1bf1716e1833084383902c.svg) 

Figure 3\. Application Workflow with Search Vector Indexes

The steps shown in the diagram are:

1. When your application loads data it wants to search semantically, it calls an embedding model to generate a vector for it.
2. It sends the data and the vector to Couchbase Capella for storage.
3. The Data Service sends the embedded vector along with scalar fields to the Search Service for inclusion in the Search Vector Index.
4. When your application needs to perform a search that includes a vector, it uses the same embedding model to generate a vector for the search value.
5. It sends the search vector and text, geospatial, and other search values as part of a search request to the Couchbase Capella Search Service.
6. The Search Service performs an index scan in the Search Vector Index to find documents that match the text or geospatial portions of the query. Then it performs a vector similarity search on the results using the search vector.
7. The Search Service returns results to your application.