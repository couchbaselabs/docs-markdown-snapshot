---
title: Upgrade a Full-Capacity, Online Cluster
description: You can upgrade a cluster from Enterprise Analytics to Operational
  Insights while it stays online and at full capacity, by using one spare
  machine.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: procedure
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-cluster-online-full-capacity.adoc
  xref: xref:enterprise-analytics:install:upgrade-cluster-online-full-capacity.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-cluster-online-full-capacity.html)

# Upgrade a Full-Capacity, Online Cluster

> You can upgrade a cluster from Enterprise Analytics to Operational Insights while it stays online and at full capacity, by using one spare machine. 

## [](#online-upgrade-with-full-capacity)Understanding Full-Capacity Upgrade

This procedure replaces each Enterprise Analytics node with a freshly installed Operational Insights node, using _swap rebalance_, so that the cluster keeps the same number of nodes throughout. For the background, including how swap rebalance works and why each node is reinstalled rather than upgraded in place, see [Upgrade Procedure Selection](upgrade-procedure-selection.md).

The procedure assumes that:

* The cluster must continue to serve requests throughout the upgrade.
* One spare machine is available, which is not part of the cluster. It meets the [system requirements](system-requirements.md), and can reach the cluster's nodes on the [required ports](cb-operational-insights-ports.md).
* The cluster runs Enterprise Analytics 2.1.x (other than 2.1.0-MP3) or 2.2.x. For other versions, see [Upgrade Paths](upgrade.md#supported-upgrade-paths).
* Nodes are replaced one at a time.

The procedure has six stages.

## [](#prepare-a-spare-node)Stage One: Prepare the Spare Node

Install Operational Insights 3.0 on the spare machine. Follow [Install on Red Hat Enterprise](red-hat-installation.md) or [Install on Ubuntu and Debian](ubuntu-debian-install.md), as appropriate for the platform.

Do not initialize the new node, or create a cluster on it. The node is configured when you add it to the cluster.

If you use Python UDFs, also install the [Python UDF add-on](install-udf-addon.md) on the spare machine.

## [](#prepare-the-cluster)Stage Two: Prepare the Cluster

1. Confirm that the cluster is healthy: every node is active, and no rebalance is running or needed.
2. Plan the upgrade for a time when brief pauses in ingestion are acceptable. Each rebalance suspends ingestion from the cluster's links until it completes. After each rebalance, queries against the partitions that changed hands run with higher latency until the nodes that took them over have cached their data, which they do lazily, on first access. See [Swap Rebalance](upgrade-procedure-selection.md#swap-rebalance).
3. Record the cluster's configuration, so that you can compare it after the upgrade. This includes the databases, scopes, collections, and links, and the settings you have changed from their defaults.

## [](#add-and-remove-a-node)Stage Three: Swap the Spare Node In

Add the Operational Insights node to the cluster, and remove one Enterprise Analytics node, in a single rebalance. Because the number of nodes added equals the number removed, Operational Insights performs a _swap rebalance_.

Every Operational Insights node runs the same fixed set of services. Do not specify services when you add the node: `couchbase-cli` rejects the `--services` option for Operational Insights and Enterprise Analytics clusters.

Run the commands against a node that remains in the cluster, rather than the node you're removing. On an Enterprise Analytics node, `couchbase-cli` is in `/opt/enterprise-analytics/bin`. On an Operational Insights node, it's in `/opt/couchbase/bin`.

1. Add the Operational Insights node. It's not yet part of the cluster, and has no credentials of its own, so the values of `--server-add-username` and `--server-add-password` are placeholders:  
```console  
couchbase-cli server-add -c ${CLUSTER_NODE}:8091 \
  -u ${USERNAME} -p ${PASSWORD} \
  --server-add https://${NEW_NODE}:18091 \
  --server-add-username Administrator \
  --server-add-password password  
```
2. Rebalance, removing the Enterprise Analytics node that's being replaced. The rebalance adds the pending node and removes the outgoing node together:  
```console  
couchbase-cli rebalance -c ${CLUSTER_NODE}:8091 \
  -u ${USERNAME} -p ${PASSWORD} \
  --server-remove ${OUTGOING_NODE}:8091  
```
3. Wait for the rebalance to complete before you continue. If it fails, resolve the cause and run the rebalance again: until it completes, the Enterprise Analytics node is still part of the cluster.

You can perform the same operation in the Web Console: on the **Servers** screen, click **ADD SERVER** to add the new node, click **Remove** on the outgoing node, then click **Rebalance**. For details of each method, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md) and [Remove a Node and Rebalance](../manage/manage-nodes/remove-node-and-rebalance.md).

The cluster now has the same number of nodes as before, one of which runs Operational Insights.

## [](#upgrade-the-removed-node)Stage Four: Reinstall the Removed Machine

Prepare the machine whose Enterprise Analytics node has just left the cluster, by proceeding as follows:

1. Confirm that the rebalance that removed the node has completed successfully. The node is no longer listed on the **Servers** screen of the Operational Insights Web Console.  
> [!IMPORTANT]  
> Do not continue on a machine whose node is still part of the cluster. The following steps delete the node's local state.
2. Stop Enterprise Analytics on the machine:  
```console  
systemctl stop enterprise-analytics  
```
3. Uninstall Enterprise Analytics, including its configuration files:

  * Red Hat-based distributions
  * Ubuntu & Debian  
```console  
dnf remove -y enterprise-analytics  
```  
If the package is held, release the hold first:  
```console  
apt-mark unhold enterprise-analytics  
```  
Then remove the package:  
```console  
apt-get purge -y enterprise-analytics  
```
4. Delete the files that the package leaves behind. These belong to a node that's no longer part of the cluster, and are not used again:  
```console  
rm -rf /opt/enterprise-analytics  
```  
If the node's data directory was outside `/opt/enterprise-analytics`, delete that directory too.  
Operational Insights installs to `/opt/couchbase`. If that directory exists on the machine, for example because the node's data directory was configured under it, delete it as well, so that the new installation starts empty:  
```console  
rm -rf /opt/couchbase  
```
5. Install Operational Insights 3.0 on the machine. Follow [Install on Red Hat Enterprise](red-hat-installation.md) or [Install on Ubuntu and Debian](ubuntu-debian-install.md), as appropriate for the platform.  
Do not initialize the new node, or create a cluster on it. The node is configured when you add it to the cluster in the next stage.
6. If you use Python UDFs, install the [Python UDF add-on](install-udf-addon.md) on the machine. Python UDFs are not available until the upgrade is complete, but installing the add-on now means that the node is ready when it is.
7. Optionally, _hold_ the package, so that no further upgrade occurs on the node until you choose to perform one. If you installed the Python UDF add-on, hold `operational-insights-udf` as well, as described in [Upgrade the Add-on](install-udf-addon.md#upgrade):

  * Red Hat-based distributions
  * Ubuntu & Debian  
Add the package name to the `exclude` line of `/etc/dnf/dnf.conf` (or `/etc/yum.conf`):  
```console  
exclude=operational-insights  
```  
```console  
apt-mark hold operational-insights  
```
8. Confirm that Operational Insights is running:  
```console  
systemctl status operational-insights  
```

## [](#repeat-stages-three-and-four)Stage Five: Repeat Stages Three and Four

Swap the newly installed Operational Insights node in for the next Enterprise Analytics node, as described in [Stage Three: Swap the Spare Node In](#add-and-remove-a-node). Then reinstall the machine that node ran on, as described in [Stage Four: Reinstall the Removed Machine](#upgrade-the-removed-node).

Continue until no Enterprise Analytics node remains in the cluster. One machine, the last one removed, is left outside the cluster, with Operational Insights installed.

## [](#add-back-the-last-node)Stage Six: Finish the Upgrade

1. Confirm that the cluster has finished its upgrade. Shortly after the last Enterprise Analytics node leaves the cluster, the cluster moves to Operational Insights 3.0, and the Analytics Service restarts on every node to switch to the new version. Requests that are running at that moment fail, and can be retried.  
To check, read the cluster's compatibility version, which each node reports as `3.0.0` when the upgrade is complete:  
```console  
curl -s -u ${USERNAME}:${PASSWORD} http://${CLUSTER_NODE}:8091/pools/default \
  | jq -r '.nodes[].prodCompatVersion'  
```
2. Compare the cluster's configuration with the record you made in [Stage Two: Prepare the Cluster](#prepare-the-cluster).
3. Repurpose the machine that remains outside the cluster, or uninstall Operational Insights from it. See [Uninstall](uninstall.md).

The upgrade is complete. New features of Operational Insights 3.0 are now available. See [Feature Availability During Upgrade](upgrade-feature-availability.md).