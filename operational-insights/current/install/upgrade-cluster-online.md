---
title: Upgrade an Online Cluster
description: You can upgrade a cluster from Enterprise Analytics to Operational
  Insights while it continues to serve requests.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-cluster-online.adoc
  xref: xref:enterprise-analytics:install:upgrade-cluster-online.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-cluster-online.html)

# Upgrade an Online Cluster

> You can upgrade a cluster from Enterprise Analytics to Operational Insights while it continues to serve requests. 

## [](#online-upgrade-at-reduced-and-full-capacity)Online Upgrade at Reduced and Full Capacity

An online upgrade replaces each Enterprise Analytics node with a freshly installed Operational Insights node, using _swap rebalance_. The cluster serves requests throughout.

If a spare machine is available, the cluster can stay at full capacity for the whole upgrade. If not, the cluster serves requests with one node fewer, until the last node is added back.

Each step of the upgrade includes a rebalance:

A rebalance in Operational Insights reassigns which nodes serve each storage partition. It does not move data: the data stays in object storage, so a rebalance takes no longer for a cluster that holds more data. While a rebalance runs, ingestion from the cluster's links is suspended, and it resumes when the rebalance completes.

Each node caches data files from object storage on its local disk lazily, on first access. A node that has taken over a partition in a rebalance therefore starts with none of that partition's data cached, and the first queries that read it fetch the data from object storage, with higher latency than usual. Latency returns to normal as the node's cache warms. This applies to the default `selective` cache policy and to `lazy`. With the `eager` policy, a node caches all of its data when it starts. For more information, see [Memory and Caching](../reference/query-performance.md#%5Fmemory%5Fand%5Fcaching) and [Scaling](../intro/architecture-overview.md#%5Fscaling).

Choose the procedure that fits your cluster:

* [Upgrade a Reduced-Capacity, Online Cluster](upgrade-cluster-online-reduced-capacity.md)
* [Upgrade a Full-Capacity, Online Cluster](upgrade-cluster-online-full-capacity.md)
* [Upgrade an Online Docker Cluster, Full Capacity](upgrade-docker-cluster-online-full-capacity.md)

Online upgrade is available from Enterprise Analytics 2.1.x and 2.2.x, except 2.1.0-MP3\. For Enterprise Analytics 2.0.x, see [Upgrade Paths](upgrade.md#supported-upgrade-paths).

## [](#during-the-upgrade)While the Cluster Is Part-Way Through an Upgrade

Until the last Enterprise Analytics node leaves the cluster, every node, including each Operational Insights node, runs the query engine of the Enterprise Analytics version that the cluster started on. New Operational Insights 3.0 features are not available until the upgrade is complete. See [Feature Availability During Upgrade](upgrade-feature-availability.md).

Shortly after the last Enterprise Analytics node leaves the cluster, the cluster moves to Operational Insights 3.0, and the Analytics Service restarts on every node to switch to the new version. Requests that are running at that moment fail, and can be retried.

After that point, an Enterprise Analytics node can no longer be added to the cluster.

### [](#mixed-product-names)Product Names in a Part-Upgraded Cluster

Each node reports the product name of the software it runs. While both products are present in the cluster, the Operational Insights Web Console and the REST API show the product name of the node you're connected to, for every node in the cluster. For example, `/pools/default` can list a node whose `version` names Enterprise Analytics next to a `prodName` of `Operational Insights`.

Scripts and tools that need to identify the product should read the `prod` field, which is `analytics` for both products, rather than `prodName`.