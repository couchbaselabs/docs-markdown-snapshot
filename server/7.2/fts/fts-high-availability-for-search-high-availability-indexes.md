---
title: High Availability Indexes
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-high-availability-for-search-high-availability-indexes.adoc
  xref: xref:7.2@server:fts:fts-high-availability-for-search-high-availability-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-high-availability-for-search-high-availability-indexes.html)

# High Availability Indexes

High availability indexes help users prevent downtime caused by unplanned incidents and enhance the overall system availability. It is achieved through Replica and Failover mechanisms with Search Service.

Replica for the index is not automatically enabled. The user must explicitly configure the required number of replicas for the index partitions according to their availability needs during the index creation step. Refer [Index Replicas](fts-index-replicas.md) to the index replica section during index creation. They could also update the replica count without rebuilding the primary partitions or live traffic for an existing index.

Server Groups/Rack zone awareness - a Server Group is a logical group of nodes. It can be based on their physical location in the network. Server Group awareness ensures that active and replica partitions are automatically assigned to different server groups(racks). So that, if a physical rack fails, the replica partition remains safe and available in another rack. Starting with Couchbase Server release 7.0.2, the Search service supports Server Groups/Rack zone aware replica placements.