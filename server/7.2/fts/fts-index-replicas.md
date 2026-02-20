---
title: Index Replicas
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-index-replicas.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-index-replicas.adoc[]
---

[View original HTML](/server/7.2/fts/fts-index-replicas.html)

# Index Replicas

Index Replicas support availability: if an Index Service-node is lost from the cluster, its indexes may exist as replicas on another cluster-node that runs the Index Service.

If an active index is lost, a replica is promoted to active status, and use of the index is uninterrupted.

The **Index Replicas** interface allows up to three index replicas to be selected, from a pull-down menu:

![fts index replicas interface](_images/fts-index-replicas-interface.png) 

Each replica partition exists on a node, separate from its active counterpart and from any other replica of that active partition. The user cannot add more than the permitted number of replicas by the current cluster configuration. If the user tries to add more replicas it will result in an error message.

![fts index replicas error message](_images/fts-index-replicas-error-message.png) 

The above error implies that there are not enough search nodes in the cluster to support the configured number of replicas.