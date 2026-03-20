---
title: Upgrade
description: To upgrade a Couchbase-Server cluster means to upgrade the version
  of Couchbase Server that is running on every node.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/upgrade.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:install:upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/upgrade.html)

# Upgrade

> To upgrade a Couchbase-Server cluster means to upgrade the version of Couchbase Server that is running on every node. 

> [!WARNING]
> Upgrading from Versions 7.1 or 7.2 to Versions 7.6.0 or 7.6.1
> 
> If there are index service nodes running in your cluster, you must use the swap rebalance method when upgrading from Couchbase Server 7.1 or 7.2 to Server 7.6.0 or 7.6.1\. See [Swap Rebalance](upgrade-procedure-selection.md#swap-rebalance) for more information about the swap rebalance method.

> [!WARNING]
> Upgrading to Version 7.x with older versions of .NET SDK
> 
> If you are upgrading from Couchbase **6.5/6.6** to **7.x+** while using a version of .NET SDK prior to 3.2.9, then make sure your cluster is **not** running in `mixed mode`. (i.e. some nodes are using IPv4 addressing while some are using IPv6).

## [](#understanding-upgrade)Understanding Upgrade

To _upgrade_ a Couchbase-Server cluster means to upgrade the version of the server that is running on every node. For example, modifying a cluster where all of its nodes are running Couchbase Server Enterprise Edition Version 6.6, so that each of its nodes subsequently runs Couchbase Server Enterprise Edition Version 7.2.

An _upgrade procedure_, like an _install_ procedure, involves both preparation routines and specific upgrade commands that are performed on each node. To be upgraded, a cluster must have each of its nodes individually upgraded in turn; and the upgrade procedure for the cluster must therefore be selected in regard to whether the cluster is required to continue serving data, or to cease serving data, during the cluster-upgrade. A review of the factors that determine the appropriateness of an upgrade-procedure is provided in [Upgrade Procedure-Selection](upgrade-procedure-selection.md).

## [](#supported-upgrade-paths)Upgrade Paths

An upgrade _path_ declares that the upgrade of one version of Couchbase Server to another is _supported_. The tables in the following subsections list upgrade paths for Enterprise Edition and for Community Edition, respectively. Each instance of the \`→\` sign declares support for the upgrade of the server-version on the left of the sign to the server-version on the right.

All supported upgrades can be performed with the cluster either _offline_ or _online_.

> [!TIP]
> As far as is possible, you should aim to keep your cluster up to date with the latest version of Couchbase Server.

## [](#how-to-upgrade-your-cluster)How to Upgrade Your Cluster

If you are upgrading several nodes at once, then the version of the software on each node must be kept in step throughout the upgrade process.  
For example, if you are upgrading three enterprise nodes (`**Node 1**`, `**Node 2**` and `**Node 3**`) from version 5.1x to 7.2.4, then you would use the following sequence:

Example 1\. Upgrading from version `5.1x` to `7.2.4`

| Step | Description                           | Upgrades                                                                         |
| ---- | ------------------------------------- | -------------------------------------------------------------------------------- |
| 1    | Upgrade all nodes from 5.1x to 6.0    | **Node 1** ⇒ 5.1x → 6.6 **Node 2** ⇒ 5.1x → 6.6 **Node 3** ⇒ 5.1x → 6.6          |
| 2    | Upgrade all nodes from 6.6 to 7.2.3   | **Node 1** ⇒ 6.6 → 7.2.3 **Node 2** ⇒ 6.6 → 7.2.3 **Node 3** ⇒ 6.6 → 7.2.3       |
| 3    | Upgrade all nodes from 7.2.3 to 7.2.4 | **Node 1** ⇒ 7.2.3 → 7.2.4 **Node 2** ⇒ 7.2.3 → 7.2.4 **Node 3** ⇒ 7.2.3 → 7.2.4 |

> [!NOTE]
> Upgrading between non-adjacent version numbers is usually _not_ supported.
> 
> For example, to upgrade from **5.1.x** to **7.2.4**, then _three_ upgrades must be performed (as shown in [Example 1](#upgrade-example)):  
> first, from **5.1.x** to **6.6**,  
> then, from **6.6** to **7.2.3**  
> and finally, from **7.2.3** to **7.2.4**.

### [](#table-upgrade-enterprise)Enterprise Edition Upgrade Paths

| Starting Version | Path to Current Version                                               |
| ---------------- | --------------------------------------------------------------------- |
| 5.0.x            | 5.0.x and 5.1.x → 6.6 → 7.2.3 → 7.2.4[\[1\]](#erlang-7-2-4-footnote1) |
| 5.5x             | 5.5.0+ → 6.6 → 7.2.3 → 7.2.4[\[1\]](#erlang-7-2-4-footnote1)          |
| 6.x              | 6.0 → 6.6 → 7.2.3 → 7.2.4[\[1\]](#erlang-7-2-4-footnote1)             |
| 7.x              | 7.0 → 7.1 → 7.2.4[\[1\]](#erlang-7-2-4-footnote1)                     |

1The upgrade to Erlang support in Couchbase server 7.2.4 requires that you first upgrade Couchbase to version 7.1.0 or later before upgrading to version 7.2.4

### [](#table-upgrade-community)Community Edition Upgrade Paths

| Starting Version | Path to Current Version                                   |
| ---------------- | --------------------------------------------------------- |
| 5.x              | 5.x → 6.6 → 7.2.2 → 7.2.4[\[1\]](#erlang-7-2-4-footnote2) |
| 6.x              | 6.0 → 6.6 → 7.2.2 → 7.2.4[\[1\]](#erlang-7-2-4-footnote2) |
| 7.x              | 7.0 → 7.1 → 7.2.4[\[1\]](#erlang-7-2-4-footnote2)         |

1The upgrade to Erlang support in Couchbase server 7.2.4 requires that you first upgrade Couchbase to version 7.1.0 or later before upgrading to version 7.2.4

Important note when upgrading from 7.0.4 to 7.2.x on Windows 2019

Upgrading from version 7.0.4 → 7.2x on Windows Server 2019 may result in a missing `java` executable files.

The problem is caused by the way Windows handles upgrades when dealing with older files, resulting in files being removed from the Couchbase installation without being replaced.

The server can be fixed by invoking the Windows Repair operation on the Couchbase installation. This will restore the missing files.

## [](#upgrade-community-enterprise)Upgrade from Community Edition to Enterprise

If you’re currently operating a Couchbase Server cluster on Community Edition, you can upgrade it to Enterprise Edition by way of a [rolling online upgrade](upgrade-procedure-selection.md#online-upgrade). This involves switching out the Community Edition nodes with fresh, net-new Enterprise Edition nodes. Both 'swap rebalance' and 'remove and reblance' methods are supported. (Delta Recovery is not supported since the new nodes must be fresh Enterprise Edition installations without any pre-existing Community Edition data remaining on them.)

> [!NOTE]
> Rolling upgrades from CE to EE are not supported if there are index service nodes running in the cluster.

The Enterprise Edition nodes must be running the same version number of Couchbase Server as the Community Edition nodes that they are replacing, otherwise the upgrade may fail. This means you can’t upgrade to a newer version of Couchbase Server while also upgrading to Enterprise Edition during the same rolling upgrade.

If you want to upgrade from an older version of _Community Edition_ to a newer version of _Enterprise Edition_, you need to perform two separate upgrade procedures:

1. Upgrade the entire cluster to Enterprise Edition via a rolling online upgrade
2. Upgrade to the desired version number of Couchbase Server using any supported type of upgrade

For example, if you wanted to upgrade from Couchbase Server 6.6 Community Edition to Couchbase Server 7.2.4 Enterprise Edition, the process would look like the following:

![Example Upgrade Path from Community to Enterprise](_images/diag-343990ded15015a1c1ce908d77fb3826e4ecfae5.svg) 

Figure 1\. Example Upgrade Path from Community to Enterprise

Additional Notes about Upgrading from Community to Enterprise

* Couchbase Server clusters _must_ be run either entirely on Enterprise Edition nodes, or entirely on Community Edition nodes.  
Once you’ve upgraded one node to Enterprise Edition, you must upgrade all the other nodes before the cluster is considered as being in a steady, supportable state.
* CE does not support index service rebalancing. So, when the cluster is running with one or more CE nodes, then the indexes hosted on nodes being removed may be lost.  
Users can create equivalent indexes (same index with different name) on different nodes, to avoid loss of index functionality.
* If a rolling online upgrade to Enterprise Edition isn’t possible in your environment, contact Couchbase for assistance.

> [!IMPORTANT]
> Remember that Enterprise Edition is not free to run in production. If you’re interested in upgrading to Couchbase Server Enterprise Edition, check out the [editions page](https://www.couchbase.com/products/editions).

See [Upgrade Procedure-Selection](upgrade-procedure-selection.md), for a list of procedures that can be used when upgrading from Community Edition to Enterprise. Note, however, that _Graceful Failover_ for Data Service nodes, with _Delta Recovery_, is _not_ supported for such upgrades: instead, _removal_, _addition_, and _swap rebalance_ should be used; for all nodes.

## [](#node-naming-and-upgrade)Node-Naming and Upgrade

In Couchbase Enterprise Server Version 7.2 or later, the node-name _must_ be correctly identified in the node-certificate as a Subject Alternative Name. If the node-name is _not_ correctly identified, failure may occur during upgrade. For information, see [Node-Certificate Validation](../learn/security/certificates.md#node-certificate-validation).

## [](#downgrade)Downgrade

Once an upgrade of a Couchbase-Server cluster has started, _downgrade_ to the earlier version of Couchbase Server can be performed, as long as one node continues to run the earlier version. To downgrade an existing node, you must first remove the existing Linux package installer, then install an earlier version. However, once all nodes are running the later version, downgrade can no longer be performed: therefore, once all nodes are running the later version, should application-support require the earlier version, an entirely new cluster must be created, running the earlier version.