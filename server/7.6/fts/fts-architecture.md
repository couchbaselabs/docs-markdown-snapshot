---
title: Search Service Architecture
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-architecture.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:fts:fts-architecture.adoc[]
---

[View original HTML](/server/7.6/fts/fts-architecture.html)

# Search Service Architecture

The _Search_ Service provides extensive capabilities for natural-language querying. These include:

* _Language-aware_ searching; allowing users to search for, say, the word `traveling`, and additionally obtain results for `travel` and `traveler`.
* _Scoring_ determines the relevancy of the documents. Scoring helps order the results. The size of the result set is controlled independently.
* _Fast indexes_, which support a wide range of possible text-searches.

The indexes that the Search Service creates and uses are entirely separate from and different from those of the Index Service.

However, if the Index and Query Services are also deployed on the cluster, the facilities of the Search Service can be called on by means of the _N1QL_ language — which provides the principal interface to the Query and Index Services. See [Accessing the Search Service with N1QL](../learn/services-and-indexes/services/search-service.md#search%5Fvia%5Fquery), below.

Under the hood, the search service has several key elements as shown in the architecture diagram below:

![searchServiceArchitecture2](../learn/_images/services-and-indexes/services/searchServiceArchitecture2.png) 

It shows the following:

* The _Data Service_ uses the DCP protocol to stream data-mutations as batches, from the producer to multiple consumers (_vBuckets_), instantiated across the search nodes.
* When a _search index_ is created by means of the _Search Service_, search-index data-handling for the vBuckets is divided equally among the established search-index partitions.

For example, when the number of vBuckets is 1024, and the number of search-index partitions chosen is 6, each search-index partition holds data for \~171 vBuckets.

All available Search Service nodes in the cluster are individually searchable. When one particular Search Service node is chosen for a search request, it assumes the role of _coordinator_; and is thereby responsible for applying the search request to the other Search Service nodes and for gathering and returning results.

How the search service operates is illustrated in the following diagram:

![searchServiceOperation](../learn/_images/services-and-indexes/services/searchServiceOperation.png) 

The diagram shows the following:

* How the application makes a search request to a specific Search Service node (here, _Node 1_). This node assumes the role of coordinator.
* How the coordinator scatters the search request to all other search-index partitions (here, _Node 2_ and _Node 3_) in the cluster.

Once all the returned data is gathered, the coordinator applies filters appropriately and returns the final results to the user.

For more detailed information on how to use the search service, see [Full Text Search: Fundamentals](../search/search.md#fundamentals-of-full-text-search).