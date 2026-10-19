---
title: Feature Availability During Upgrade
description: While an online upgrade is in progress, the cluster runs the query
  engine of the Enterprise Analytics version it started on, and new Operational
  Insights features are not available.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-feature-availability.adoc
  xref: xref:enterprise-analytics:install:upgrade-feature-availability.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-feature-availability.html)

# Feature Availability During Upgrade

> While an online upgrade is in progress, the cluster runs the query engine of the Enterprise Analytics version it started on, and new Operational Insights features are not available. 

## [](#understanding-feature-availability)Understanding Feature Availability

During an online upgrade, the cluster runs in _mixed mode_: some nodes run Enterprise Analytics, and others run Operational Insights.

In mixed mode, every node runs the query engine of the Enterprise Analytics version the cluster started on, including the Operational Insights nodes. The cluster behaves as that Enterprise Analytics version, and none of the features introduced in Operational Insights 3.0 can be used, on any node.

Shortly after the last Enterprise Analytics node leaves the cluster, the cluster moves to Operational Insights 3.0\. The Analytics Service restarts on every node to switch to the new version, and requests that are running at that moment fail and can be retried. From then on, all Operational Insights 3.0 features are available.

To check whether the cluster has moved to Operational Insights 3.0, read the compatibility version that each node reports, which is `3.0.0` once the upgrade is complete:

```console
curl -s -u ${USERNAME}:${PASSWORD} http://${CLUSTER_NODE}:8091/pools/default \
  | jq -r '.nodes[].prodCompatVersion'
```

An offline upgrade has no mixed-mode period: the cluster comes back online as Operational Insights 3.0.

## [](#features)Operational Insights 3.0 Features

The following features become available only when the upgrade is complete. For details of each, see [Operational Insights Release Notes](../release-notes/release-notes.md).

| Feature                                                                                                         | Usable in Mixed Mode |
| --------------------------------------------------------------------------------------------------------------- | -------------------- |
| [Vector indexes](../sqlpp/5%5Fddl%5Fvector%5Findex.md) and [vector functions](../sqlpp/8%5Fbuiltin%5Fvector.md) | No                   |
| [CLUSTER BY clause](../sqlpp/3%5Fquery.md#Cluster%5FBy%5Fclauses)                                               | No                   |
| [Python user-defined functions](../sqlpp/9b%5Fpython%5Fudf.md)                                                  | No                   |
| [Multi-statement requests](../reference/multi-statement-requests.md)                                            | No                   |
| [Query plan cache](../sqlpp/5d-query-plan-cache.md)                                                             | No                   |
| Sampling without a full scan, for [ANALYZE COLLECTION](../sqlpp/5b%5Fcbo.md)                                    | No                   |
| [Hash-based distinct count](../sqlpp/appendix%5F2%5Fparameters.md#Hash%5Fbased%5Fdistinct%5Fcount%5Fparameters) | No                   |

## [](#topology-changes)Adding Nodes During and After an Upgrade

While the upgrade is in progress, you can add both Enterprise Analytics and Operational Insights nodes to the cluster.

After the cluster has moved to Operational Insights 3.0, Enterprise Analytics nodes can no longer be added to it.