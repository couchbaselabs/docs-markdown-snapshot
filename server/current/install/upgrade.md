---
title: Upgrade
description: To upgrade a Couchbase-Server cluster means to upgrade the version
  of Couchbase Server that's running on every node.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/upgrade.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/install/upgrade.html)

# Upgrade

> To upgrade a Couchbase-Server cluster means to upgrade the version of Couchbase Server that’s running on every node. 

> [!WARNING]
> Upgrading from Versions 7.1 or 7.2 to Versions 7.6.0 or 7.6.1
> 
> If there are index service nodes running in your cluster, you must use the swap rebalance method when upgrading from Couchbase Server 7.1 or 7.2 to Server 7.6.0 or 7.6.1.
> 
> See [Swap Rebalance](upgrade-procedure-selection.md#swap-rebalance) for more information about the swap rebalance method.

## [](#before-you-upgrade)Before You Upgrade

Before upgrading, consider the following version compatibility concerns.

### [](#8-0-storage-backend)New Default Storage Backend in Couchbase Server Version 8.0

After you have fully upgraded a cluster to Couchbase Server 8.0.x and later, the default storage backend for buckets is Magma with 128 vBuckets. Previous versions of Couchbase Server used Couchstore with 1024 vBuckets as the default storage backend.

This new default results in two behavior changes from previous versions:

* If you create a bucket and do not specify the storage backend, your bucket will use the Magma storage backend instead of the Couchstore backend.
* If you specify Magma as the storage backend but do not set the new `numVBuckets` parameter, the bucket will have 128 vBuckets instead of the prior default of 1024 vBuckets. Magma buckets with 128 vBuckets is a new feature in Couchbase Server 8.0 and later.

These behavior changes could cause issues if you rely on the prior behavior, especially if you use deployment scripts. If you have deployment scripts that create buckets, review them to determine if you need to make changes.

For example, suppose your deployment script does not specify the storage backend when it creates a bucket that you intend to use with the [views](../learn/views/views-intro.md) feature. On versions prior to Couchbase Server 8.0, your script created a Couchstore bucket with 1024 vBuckets, In version 8.0, due to change in the default backend, your script creates a bucket with the Magma storage backend with 128 vBuckets. Attempting to use MapReduce Views with this bucket results in errors, because Magma buckets do not support this feature.

> [!IMPORTANT]
> Views are deprecated in Couchbase Server 7.0 and later versions. Views support in Couchbase Server will be removed in a future release. Instead of views, use indexes and queries using the [Index Service](../learn/services-and-indexes/services/index-service.md) (GSI) and the [Query Service](../learn/services-and-indexes/services/query-service.md) (SQL++). Views will not run on the newer [Magma storage engine](../learn/buckets-memory-and-storage/storage-engines.md).

Another concern is that versions of Couchbase Server earlier than 8.0 do not support XDCR replication between buckets with different numbers of vBuckets. Therefore, you cannot replicate to a bucket you create with the new default backend setting from buckets on an earlier server version. To replicate from a bucket on an earlier version of Couchbase Server, explicitly set the new bucket’s storage backend to Couchstore or to Magma with 1024 vBuckets during creation.

For more information about storage backends, see [Storage Engines](../learn/buckets-memory-and-storage/storage-engines.md).

### [](#x86-avx2-requirement-for-couchbase-server-version-8-0-and-later)x86 AVX2 Requirement for Couchbase Server Version 8.0 and Later

When running on x86-64 processors, Couchbase Server 8.0 and later requires that the CPU support the AVX2 instruction set. Most Intel processors manufactured since 2013 and AMD processors manufactured since 2015 support AVX2\. If you attempt to run Couchbase Server 8.0 or later on a CPU that does not support AVX2, the server exits with an error. See [Instruction Set Requirements for x86 Processors](pre-install.md#avx2-requirement-for-x86-processors) for more information.

### [](#memcached-buckets-have-been-removed-in-couchbase-server-version-8-0-and-later)Memcached Buckets Have Been Removed in Couchbase Server Version 8.0 and Later

Memcached buckets have been removed in Couchbase Server 8.0 and later. The upgrade process exits with an error if you attempt to upgrade a cluster with Memcached buckets. If your cluster has Memcached buckets, you must replace them with ephemeral buckets before upgrading. See [Bucket Capabilities in the Version 6.6 documentation](https://docs-archive.couchbase.com/server/6.6/learn/buckets-memory-and-storage/buckets.html#bucket-capabilities) for a summary of the differences between Memcached and ephemeral buckets.

### [](#dotnet-sdk-upgrade-note)Upgrading to Version 7.x With Earlier Versions of .NET SDK

When upgrading from Couchbase 6.5 or 6.6 to 7.0 or later, determine if both of the following are true:

* You use a version of the .NET SDK prior to 3.2.9.
* Your cluster is in mixed mode networking where some nodes use IPv4 addressing and others use IPv6\. See [Changing Address Family](../manage/manage-nodes/manage-address-families.md#changing-address-family-to-IPv6) for steps to determine if your cluster is running in this mode.

Using a version of the .NET SDK prior to 3.2.9 with mixed mode network addressing can cause issues with write operations. Before upgrading, resolve the mixed-mode networking issue.

### [](#upgrading-from-pre-7-1-versions-of-couchbase-server)Upgrading from Pre-7.1 Versions of Couchbase Server

You cannot upgrade directly from a version of Couchbase Server earlier than 7.1 to version 7.2.4 or later.

For example, you can directly upgrade from version 6.6 to version 7.2.3.

You cannot directly upgrade from version 6.6 to version 7.2.4\. A compatibility issue with the Erlang version used by these earlier server versions prevents a direct upgrade to later versions of the server. To upgrade from server versions 6.5, 6.6, or 7.0 to version 7.6 or later, first upgrade to a version between 7.1 and 7.2.3\. Then upgrade to version 7.6 or later.

## [](#understanding-upgrade)Understanding Upgrade

To _upgrade_ a Couchbase-Server cluster means to upgrade the version of the server that’s running on every node. For example, modifying a cluster where all of its nodes are running Couchbase Server Enterprise Edition Version 6.6, so that each of its nodes subsequently runs Couchbase Server Enterprise Edition Version 7.6.x.

An _upgrade procedure_, like an _install_ procedure, involves both preparation routines and specific upgrade commands that are performed on each node. To be upgraded, a cluster must have each of its nodes individually upgraded in turn. The upgrade procedure for the cluster must be selected in regard to whether the cluster is required to continue serving data, or to cease serving data, during the cluster-upgrade. A review of the factors that determine the appropriateness of an upgrade-procedure is provided in [Upgrade Procedure-Selection](upgrade-procedure-selection.md).

## [](#supported-upgrade-paths)Upgrade Paths

An upgrade _path_ declares that the upgrade of one Couchbase Server version to another is _supported_. The tables in the following subsections list upgrade paths for Enterprise Edition and for Community Edition, respectively. Each instance of the \`→\` sign declares support for the upgrade of the server-version on the left of the sign to the server-version on the right.

All supported upgrades can be performed with the cluster either _offline_ or _online_.

> [!TIP]
> As far as is possible, you should aim to keep your cluster up to date with the latest version of Couchbase Server.

### [](#table-upgrade-enterprise)Enterprise Edition Upgrade Paths

| Starting Version | Path to Current Version                                                                |
| ---------------- | -------------------------------------------------------------------------------------- |
| 5.x              | Any 5.0.x / 5.1.x / 5.5.x → 6.6 → 7.2.3 → 8.0                                          |
| 6.x              | Any 6.0.x / 6.5.x → 6.6 → 7.2.3 → 8.0                                                  |
| 7.x              | Any 7.0.x / 7.1.x → 7.2.3 → 8.0[\[1\]](##erlang-8-0-footnote1) Any 7.2.x / 7.6.x → 8.0 |

1The upgrade to Erlang support in Couchbase Server 8.0 requires that you first upgrade Couchbase to version 7.2 before upgrading to version 8.0.

### [](#table-upgrade-community)Community Edition Upgrade Paths

| Starting Version | Path to Current Version                                                               |
| ---------------- | ------------------------------------------------------------------------------------- |
| 5.x              | Any 5.x → 6.6.0 → 7.2.2 → 8.0[\[1\]](#erlang-8-0-footnote1) →                         |
| 6.x              | Any 6.0.x / 6.5.x → 6.6.0 → 7.2.2 → 8.0[\[1\]](#erlang-8-0-footnote1)                 |
| 7.x              | Any 7.0.x / 7.1.x → 7.2.2 → 8.0[\[1\]](#erlang-8-0-footnote1) Any 7.2.x / 7.6.x → 8.0 |

1The upgrade to Erlang support in Couchbase Server 8.0 requires that you first upgrade Couchbase to version 7.2 before upgrading to version 8.0.

Important note when upgrading from 7.0.4 to 7.2.x on Windows 2019

Upgrading from version 7.0.4 → 7.2x on Windows Server 2019 may result in a missing `java` executable files.

The problem is caused by the way Windows handles upgrades when dealing with older files, resulting in files being removed from the Couchbase installation without being replaced.

The server can be fixed by invoking the Windows Repair operation on the Couchbase installation. This will restore the missing files.

## [](#how-to-upgrade-your-cluster)How to Upgrade Your Cluster

If you are upgrading several nodes at once, then the version of the software on each node must be kept in step throughout the upgrade process.  
For example, if you are upgrading three enterprise nodes (`**Node 1**`, `**Node 2**` and `**Node 3**`) from version 6.6.x to 8.0.x, then you would use the following sequence:

Example 1\. Upgrading from version 6.6.x to 8.0.x

| Step | Description                           | Upgrades                                                                         |
| ---- | ------------------------------------- | -------------------------------------------------------------------------------- |
| 1    | Upgrade all nodes from 6.6.x to 7.2.3 | **Node 1** ⇒ 6.6.x → 7.2.3 **Node 2** ⇒ 6.6.x → 7.2.3 **Node 3** ⇒ 6.6.x → 7.2.3 |
| 2    | Upgrade all nodes from 7.2.3 to 8.0.x | **Node 1** ⇒ 7.2.3 → 8.0.x **Node 2** ⇒ 7.2.3 → 8.0.x **Node 3** ⇒ 7.2.3 → 8.0.x |

> [!NOTE]
> Upgrading between non-adjacent version numbers is usually _not_ supported.
> 
> For example, to upgrade from **6.6.x** to **8.0.x**, then 2 upgrades must be performed (as shown in [Example 1](#upgrade-example)):
> 
> 1. First, from **6.6.x** to **7.2.3**.
> 2. Then, from **7.2.3** to **8.0.x**.

## [](#upgrade-community-enterprise)Upgrade from Community Edition to Enterprise

If you’re currently operating a Couchbase Server cluster on Community Edition, you can upgrade it to Enterprise Edition by way of a [rolling online upgrade](upgrade-procedure-selection.md#online-upgrade). This involves switching out the Community Edition nodes with fresh, net-new Enterprise Edition nodes. Both swap rebalance and remove and rebalance methods are supported. Delta Recovery is not supported since the new nodes must be fresh Enterprise Edition installations without any pre-existing Community Edition data remaining on them.

> [!NOTE]
> Rolling upgrades from CE to EE are not supported if there are index service nodes running in the cluster.

The Enterprise Edition nodes must be running the same version number of Couchbase Server as the Community Edition nodes that they are replacing, otherwise the upgrade may fail. This means you can’t upgrade to a newer version of Couchbase Server while also upgrading to Enterprise Edition during the same rolling upgrade.

If you want to upgrade from an older version of _Community Edition_ to a newer version of _Enterprise Edition_, you need to perform two separate upgrade procedures:

1. Upgrade the entire cluster to Enterprise Edition via a rolling online upgrade
2. Upgrade to the desired version number of Couchbase Server using any supported type of upgrade

For example, if you wanted to upgrade from Couchbase Server 6.6 Community Edition to Couchbase Server 7.6 Enterprise Edition, the process would look like the following:

![Example Upgrade Path from Community to Enterprise](_images/diag-0b1e6b61cc817ed288bd0b9e9db3f8e028e7181c.svg) 

Figure 1\. Example Upgrade Path from Community to Enterprise

Additional Notes about Upgrading from Community to Enterprise

* Couchbase Server clusters _must_ be run either entirely on Enterprise Edition nodes or entirely on Community Edition nodes.  
Once you’ve upgraded one node to Enterprise Edition, you must upgrade all the other nodes before the cluster is considered as being in a steady, supportable state.
* CE does not support index service rebalancing. So, when the cluster is running with one or more CE nodes, then the indexes hosted on nodes being removed may be lost.  
Users can create equivalent indexes (the same index with a different name) on different nodes to avoid loss of index functionality.
* If a rolling online upgrade to Enterprise Edition isn’t possible in your environment, contact Couchbase for assistance.

> [!IMPORTANT]
> Remember that Enterprise Edition is not free to run in production. If you’re interested in upgrading to Couchbase Server Enterprise Edition, check out the [editions page](https://www.couchbase.com/products/editions).

See [Upgrade Procedure-Selection](upgrade-procedure-selection.md) for a list of procedures that can be used when upgrading from Community Edition to Enterprise. Note, however, that _Graceful Failover_ for Data Service nodes, with _Delta Recovery_, is _not_ supported for such upgrades: instead, _removal_, _addition_, and _swap rebalance_ should be used; for all nodes.

## [](#node-naming-and-upgrade)Node-Naming and Upgrade

In Couchbase Enterprise Server Version 7.2 or later, the node-name _must_ be correctly identified in the node-certificate as a Subject Alternative Name. If the node-name is _not_ correctly identified, failure may occur during upgrade. For information, see [Node-Certificate Validation](../learn/security/certificates.md#node-certificate-validation).

## [](#downgrade)Downgrade

Once an upgrade of a Couchbase-Server cluster has started, _downgrading_ to an earlier version of Couchbase Server can be performed by using the _swap/rebalance_ method:

1. Remove the target node from the cluster, then perform a rebalance on the cluster.
2. Downgrade the target node (or create a new node using the earlier version of Couchbase).
3. Add the node to the cluster and rebalance.

Bear in mind that once all nodes are running the later version, downgrade can no longer be performed: therefore, once all nodes are running the later version, should application-support require the earlier version, an entirely new cluster must be created, running the earlier version.