---
title: Upgrade Enterprise Analytics
description: To upgrade Enterprise Analytics, you need to upgrade the version of
  Enterprise Analytics running on each node in your cluster.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/upgrade.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:install:upgrade.adoc[]
---

[View original HTML](/enterprise-analytics/current/install/upgrade.html)

# Upgrade Enterprise Analytics

> To upgrade Enterprise Analytics, you need to upgrade the version of Enterprise Analytics running on each node in your cluster. 

Upgrading Enterprise Analytics, just like installing, involves preparing your cluster and running specific upgrade commands on each node.

You must upgrade each node in a cluster individually. You can choose how you want to upgrade your cluster based on whether you want to continue serving data during the upgrade. For more information, see [Choose an Upgrade Procedure](upgrade-procedure-selection.md).

## [](#upgrade-paths)Upgrade Paths

You can use the following upgrade paths to determine how to upgrade from 1 version of Enterprise Analytics to another. You can follow any upgrade path with your cluster online or offline.

Couchbase recommends keeping your cluster up to date with the latest version of Enterprise Analytics.

| Starting Version | Path to Current Version |
| ---------------- | ----------------------- |
| 2.0.x            | 2.0.x → 2.1             |

## [](#how-to-upgrade-your-cluster)How to Upgrade Your Cluster

For more information about the different upgrade methods for Enterprise Analytics, see [install/upgrade-procedure-selection.adoc](#install/upgrade-procedure-selection.adoc).

## [](#downgrade)Downgrade

If you have started an upgrade on your Enterprise Analytics cluster, you can downgrade to an earlier version using the swap/rebalance method:

1. Remove the target node from the cluster, then perform a rebalance on the cluster.
2. Downgrade the target node (or create a new node using the earlier version of Enterprise Analytics).
3. Add the node to the cluster and rebalance.

After all nodes in a cluster are running a later version of Enterprise Analytics, you cannot downgrade your cluster. If you need to return to an earlier version of Enterprise Analytics, you must create a new cluster with the earlier version installed.