---
title: Upgrade
description: To upgrade to Operational Insights, you move every node in your
  cluster to the new version, either while the cluster continues to serve
  requests or during a maintenance window.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade.adoc
  xref: xref:enterprise-analytics:install:upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade.html)

# Upgrade

> To upgrade to Operational Insights, you move every node in your cluster to the new version, either while the cluster continues to serve requests or during a maintenance window. 

Operational Insights 3.0 is the successor to Enterprise Analytics. An upgrade from Enterprise Analytics is also a change of product name, and the name change affects how you upgrade each node. Read [What Changes with the Product Name](#what-changes) before you choose a procedure.

You upgrade a cluster one node at a time. You can keep the cluster online and serving requests throughout, or take it offline for a maintenance window. To decide which approach suits your cluster, see [Upgrade Procedure Selection](upgrade-procedure-selection.md).

## [](#supported-upgrade-paths)Upgrade Paths

Use the following table to find the upgrade path for your starting version.

| Starting Version           | Online Upgrade                                                                                            | Offline Upgrade                  |
| -------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------- |
| Enterprise Analytics 2.0.x | Not supported directly. Upgrade to Enterprise Analytics 2.2.x first, then follow the path for 2.2.x.      | 2.0.x → Operational Insights 3.0 |
| Enterprise Analytics 2.1.x | 2.1.x → Operational Insights 3.0, except 2.1.0-MP3 (build 2.1.0-1396), which can only be upgraded offline | 2.1.x → Operational Insights 3.0 |
| Enterprise Analytics 2.2.x | 2.2.x → Operational Insights 3.0                                                                          | 2.2.x → Operational Insights 3.0 |

During an online upgrade, the Operational Insights nodes you add run the same query engine version as the Enterprise Analytics nodes they join, until the last Enterprise Analytics node leaves the cluster. Operational Insights 3.0 carries the engine versions for the Enterprise Analytics releases listed as online upgrade sources above, so a cluster running any other version, such as Enterprise Analytics 2.0.x, refuses to rebalance an Operational Insights node in.

Couchbase recommends keeping your cluster up to date with the latest version of Operational Insights.

## [](#what-changes)What Changes with the Product Name

Operational Insights installs under different names and paths from Enterprise Analytics:

| Item                         | Enterprise Analytics 2.x       | Operational Insights 3.0       |
| ---------------------------- | ------------------------------ | ------------------------------ |
| Package name (.deb and .rpm) | enterprise-analytics           | operational-insights           |
| systemd service              | enterprise-analytics           | operational-insights           |
| Install directory            | /opt/enterprise-analytics      | /opt/couchbase                 |
| Docker image                 | couchbase/enterprise-analytics | couchbase/operational-insights |

Because the package name changes, a package manager treats Operational Insights as an unrelated product rather than a newer version of Enterprise Analytics:

* `apt upgrade`, `yum update`, and `dnf upgrade` do not move a node from Enterprise Analytics to Operational Insights. The node stays on Enterprise Analytics, and no error is shown.
* The `operational-insights` package refuses to install while the `enterprise-analytics` package is installed on the same machine.

The upgrade procedures account for this:

* An **online** upgrade never upgrades a package in place. You add freshly installed Operational Insights nodes to the cluster, and rebalance the Enterprise Analytics nodes out. A machine whose node has left the cluster can be uninstalled, reinstalled with Operational Insights, and added back as a new node.
* An **offline** upgrade keeps each node's identity and data, by following a per-node procedure that carries the node's state across the package change. See [Offline Upgrade from Enterprise Analytics to Operational Insights](upgrade-ea-to-oi.md) for nodes installed from packages, and [Offline Upgrade of a Docker Cluster from Enterprise Analytics to Operational Insights](upgrade-docker-cluster-offline.md) for nodes that run in Docker containers.

Neither procedure moves or modifies your data in object storage.

## [](#how-to-upgrade)How to Upgrade Your Cluster

1. Choose a procedure, using [Upgrade Procedure Selection](upgrade-procedure-selection.md).
2. Follow the steps for that procedure, listed in [Upgrade Procedures](upgrade-procedures.md).
3. Review which features you can use while the cluster is part-way through an online upgrade, in [Feature Availability During Upgrade](upgrade-feature-availability.md).

## [](#downgrade)Downgrade

While an online upgrade is in progress, and at least one Enterprise Analytics node remains in the cluster, you can return the cluster to Enterprise Analytics with the same swap rebalance technique you used to upgrade it: add Enterprise Analytics nodes, and rebalance the Operational Insights nodes out.

After the last Enterprise Analytics node leaves the cluster, the cluster switches to Operational Insights 3.0, and Enterprise Analytics nodes can no longer join it. From that point you cannot downgrade the cluster. To return to Enterprise Analytics, create a new Enterprise Analytics cluster.

An offline upgrade from Enterprise Analytics to Operational Insights cannot be rolled back.