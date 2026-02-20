---
title: Index Partitioning
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-index-partitions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-index-partitions.adoc[]
---

[View original HTML](/server/7.2/fts/fts-index-partitions.html)

# Index Partitioning

_Index Partitioning_ increases query performance by dividing and spreading a large index of documents across multiple nodes. This feature is available only in Couchbase Server Enterprise Edition.

The benefits include:

* The ability to scale out horizontally as index size increases.
* Transparency to queries, requiring no change to existing queries.
* Reduction of query latency for large, aggregated queries; since partitions can be scanned in parallel.
* Provision of a low-latency range query while allowing indexes to be scaled out as needed.

## [](#index-partitions)Index Partitions

The **Index Partitions** interface provides a section to enter the number of partitions the index is to be split into:

![fts index partitions interface](_images/fts-index-partitions-interface.png) 

The default option for this setting is 1\. Note that this number represents the number of active partitions for an index, and the active partitions are distributed across all the nodes in the cluster where the search service is running.

> [!NOTE]
> The type of index is saved in its JSON definition, which can be previewed in the _Index Definition Preview_ panel, at the right-hand side.

See [Using the Index Definition Preview](fts-creating-index-from-UI-classic-editor.md#using-the-index-definition-preview).

```javascript
"planParams": {
  "numReplicas": 0,
  "indexPartitions": 6
},
```