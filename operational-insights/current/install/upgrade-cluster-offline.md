---
title: Upgrade an Offline Cluster
description: The simplest way to upgrade a multi-node cluster is with the
  cluster offline, during a maintenance window in which it serves no requests.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: procedure
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-cluster-offline.adoc
  xref: xref:enterprise-analytics:install:upgrade-cluster-offline.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-cluster-offline.html)

# Upgrade an Offline Cluster

> The simplest way to upgrade a multi-node cluster is with the cluster offline, during a maintenance window in which it serves no requests. 

## [](#understanding-offline-cluster-upgrade)Understanding Offline Cluster Upgrade

In an offline upgrade, all application access to the cluster stops, and each node is upgraded in turn. Each node keeps its identity, its configuration, and its data, so no rebalance is needed. When every node has been upgraded, the cluster is brought back online.

Offline upgrade is available from every Enterprise Analytics release, including 2.0.x.

The procedure has three stages.

## [](#prepare-the-cluster)Stage One: Prepare the Cluster

1. Stop all applications that send requests to the cluster.
2. Disable auto-failover, so that no node is failed over while it stops communicating with the rest of the cluster during its upgrade. You only need to do this once, on any node:  
```console  
/opt/enterprise-analytics/bin/couchbase-cli setting-autofailover \
  -c ${CLUSTER_NODE}:8091 -u ${USERNAME} -p ${PASSWORD} \
  --enable-auto-failover 0  
```  
For more information, see [setting-autofailover](../cli/couchbase-cli-setting-autofailover.md).
3. Record each node's UUID and data path, which you use to verify the node after its upgrade. The per-node procedure in the next stage describes how.

## [](#upgrade-each-individual-node)Stage Two: Upgrade Each Individual Node

Upgrade each node in turn, by following the per-node procedure for how the node is installed:

* For a node installed from an `.rpm` or `.deb` package, follow [Offline Upgrade from Enterprise Analytics to Operational Insights](upgrade-ea-to-oi.md).
* For a node that runs in a Docker container, follow [Offline Upgrade of a Docker Cluster from Enterprise Analytics to Operational Insights](upgrade-docker-cluster-offline.md).

Each procedure moves the node from Enterprise Analytics to Operational Insights while keeping the node's state. Follow every step: a node that starts without its state initializes itself as a new, empty node.

Verify each node, as the procedure describes, before you move on to the next.

## [](#bring-the-cluster-back-online)Stage Three: Bring the Cluster Back Online

1. Confirm that every node is active, on the **Servers** screen of the Operational Insights Web Console, or with the following command:  
```console  
/opt/couchbase/bin/couchbase-cli server-list \
  -c ${CLUSTER_NODE}:8091 -u ${USERNAME} -p ${PASSWORD}  
```
2. Enable auto-failover again, with the settings the cluster used before the upgrade:  
```console  
/opt/couchbase/bin/couchbase-cli setting-autofailover \
  -c ${CLUSTER_NODE}:8091 -u ${USERNAME} -p ${PASSWORD} \
  --enable-auto-failover 1 --auto-failover-timeout ${TIMEOUT}  
```
3. Restart the applications that send requests to the cluster.

The upgrade is complete.