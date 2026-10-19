---
title: Upgrade Procedures
description: Step-by-step procedures are provided for upgrading an Operational
  Insights cluster, online or offline.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-procedures.adoc
  xref: xref:enterprise-analytics:install:upgrade-procedures.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-procedures.html)

# Upgrade Procedures

> Step-by-step procedures are provided for upgrading an Operational Insights cluster, online or offline. 

This section provides step-by-step instructions for upgrading a multi-node cluster from Enterprise Analytics to Operational Insights. Each procedure suits a particular situation. To choose between them, see [Upgrade Procedure Selection](upgrade-procedure-selection.md).

## [](#upgrading-multi-node-clusters)Upgrading Multi-Node Clusters

* [Upgrade an Offline Cluster](upgrade-cluster-offline.md). This is the simplest procedure, and works from every Enterprise Analytics release, but it needs cluster downtime. Each node follows a per-node procedure: [Offline Upgrade from Enterprise Analytics to Operational Insights](upgrade-ea-to-oi.md) for nodes installed from packages, or [Offline Upgrade of a Docker Cluster from Enterprise Analytics to Operational Insights](upgrade-docker-cluster-offline.md) for nodes that run in Docker containers.
* [Upgrade an Online Cluster](upgrade-cluster-online.md). The cluster continues to serve requests throughout. Three procedures are provided:

  * [Upgrade a Reduced-Capacity, Online Cluster](upgrade-cluster-online-reduced-capacity.md). If no spare machine is available, the cluster can be upgraded with its own machines, provided that it can serve its workload with one node fewer during the upgrade.
  * [Upgrade a Full-Capacity, Online Cluster](upgrade-cluster-online-full-capacity.md). If a spare machine is available, the cluster stays at full capacity throughout.
  * [Upgrade an Online Docker Cluster, Full Capacity](upgrade-docker-cluster-online-full-capacity.md). For a cluster that runs in Docker containers.

## [](#upgrading-developer-clusters)Upgrading Single-Node Clusters

Single-node clusters are often used for development, and are not supported for production. For their limitations, see [Single-Node and Two-Node Clusters](single-two-node-clusters.md).

A single-node cluster has no other node to take over its work, so upgrade it offline: follow [Upgrade an Offline Cluster](upgrade-cluster-offline.md). Because there is only one node, you do not need to disable and re-enable auto-failover.