---
title: Scatter Gather Operation
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-architecture-scatter-gather.adoc
  xref: xref:7.6@server:fts:fts-architecture-scatter-gather.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-architecture-scatter-gather.html)

# Scatter Gather Operation

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

All available Search Service nodes in the cluster are individually searchable.

When one particular Search Service node is chosen for a search request, it assumes the role of _coordinator_; and is thereby responsible for applying the search request to the other Search Service nodes and for gathering and returning results.

The following illustration depicts this _scatter-gather_ execution of a search request:

![searchServiceOperation](../learn/_images/services-and-indexes/services/searchServiceOperation.png) 

This illustration shows how:

* The application makes a search request to a specific Search Service node (here, `Node 1`). This node assumes the role of coordinator.
* The coordinator scatters the search request to all other search-index partitions (here, `Node 2` and `Node 3`) in the cluster.
* Once all the returned data is gathered, the coordinator applies filters as appropriate and returns the final results to the user.