---
title: Scatter Gather Operation
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-architecture-scatter-gather.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/fts/fts-architecture-scatter-gather.html)

# Scatter Gather Operation

All available Search Service nodes in the cluster are individually searchable.

When one particular Search Service node is chosen for a search request, it assumes the role of _coordinator_; and is thereby responsible for applying the search request to the other Search Service nodes and for gathering and returning results.

The following illustration depicts this _scatter-gather_ execution of a search request:

![searchServiceOperation](../learn/_images/services-and-indexes/services/searchServiceOperation.png) 

This illustration shows how:

* The application makes a search request to a specific Search Service node (here, `Node 1`). This node assumes the role of coordinator.
* The coordinator scatters the search request to all other search-index partitions (here, `Node 2` and `Node 3`) in the cluster.
* Once all the returned data is gathered, the coordinator applies filters as appropriate and returns the final results to the user.