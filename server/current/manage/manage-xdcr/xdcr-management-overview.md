---
title: XDCR Management Overview
description: Cross Datacenter Replication (XDCR) provides an easy way to
  replicate data from one cluster to another.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-xdcr/xdcr-management-overview.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:manage:manage-xdcr/xdcr-management-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-xdcr/xdcr-management-overview.html)

# XDCR Management Overview

> Cross Datacenter Replication (XDCR) provides an easy way to replicate data from one cluster to another. 

## [](#xdcr-summary)What is XDCR?

Cross Data Center Replication (XDCR) replicates data between clusters: this provides protection against data-center failure, and also provides high-performance data-access for globally distributed, mission-critical applications.

Note that Couchbase has modified the license restrictions to its Couchbase Server Community Edition package, for version 7.0 and higher: in consequence, XDCR is promoted to a commercial-only feature of Enterprise Edition. See [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/), for more information on the license restrictions; and see [XDCR and Community Edition](#xdcr-and-community-edition), below, for information on how the new restrictions affect the experience of Community-Edition administrators.

XDCR replicates data from a specific bucket on the source cluster to a specific bucket on the target cluster. Any bucket (Couchbase or Ephemeral) on any cluster can be specified as a source or a target for one or more XDCR definitions. _Scopes_ and _collections_, within source and target buckets, can also be specified. Data from the source is pushed to the target bucket by means of an XDCR agent, running on the source cluster, using the Database Change Protocol.

Note that XDCR can only be established between clusters whose numbers of vBuckets are equal: all supported platforms have _1024_ vBuckets except _MacOS_, which has _64_. For more information, see [vBuckets](../../learn/buckets-memory-and-storage/vbuckets.md).

A complete architectural description of XDCR is provided in [Cross Data Center Replication (XDCR)](../../learn/clusters-and-availability/xdcr-overview.md). You may wish to familiarize yourself with the information provided there, before performing the routines provided in this section.

For information on scopes and collections, see [Scopes and Collections](../../learn/data/scopes-and-collections.md).

## [](#what-xdcr-tasks-can-be-performed)What XDCR Tasks Can Be Performed?

Management of XDCR includes the following:

* _Preparation_: Make sure that you have appropriate permissions for managing XDCR. Check platform sizes, configurations, and ports. Details are provided in [Prepare for XDCR](prepare-for-xdcr.md).
* _Reference_ management: Remote clusters must be registered as targets for XDCR. This requires appropriate administration credentials for the remote cluster, and the existence on that cluster of one or more buckets that can be specified as recipients of replicated data. Information on establishing references is provided in [Create a Reference](create-xdcr-reference.md); and information on deleting them in [Delete a Reference](delete-xdcr-reference.md).
* _Replication_ management: Once a reference has been registered on the local cluster, it can be specified as the target for a _replication_. This requires that an existing source and an existing target bucket also be specified. Optionally, filters can be established, so that only documents with matching ids, fields, values, or extended attributes are replicated. Additionally, advanced settings can be configured, to ensure optimal performance. Information on establishing replications is provided in [Create a Replication](create-xdcr-replication.md); and information on deleting them in [Delete a Replication](delete-xdcr-replication.md).  
Note that replications can be configured to occur between specific _scopes_ and _collections_; as described in [Replicate Using Scopes and Collections](replicate-using-scopes-and-collections.md).
* _Pausing_ and _Resuming_ replications: Once started, a replication is continuous; mutations on the source being constantly transmitted to the target. Occasionally, for purposes of system maintenance, it may be desirable manually to pause a replication, and then resume it. Information is provided in [Pause a Replication](pause-xdcr-replication.md); and [Resume a Replication](resume-xdcr-replication.md).
* _Recovering Data_: In the event of data-loss, the **cbrecovery** tool can be used to restore data. The tool accesses remotely replicated buckets, previously created with XDCR, and copies appropriate subsets of their data back onto the original source-cluster. Information is provided in [Recover Data with XDCR](recover-data-with-xdcr.md).

## [](#how-to-use-xdcr-management-section)How to Use This Section

This section is divided into multiple subsections, each of which presents step-by-step examples of how to perform a particular XDCR management task. In most subsections, three examples are provided, showing how to perform the same task with Couchbase Web Console, CLI, and REST API respectively. The subsections are arranged in a sequence, to make it easy to start from the first example, [Prepare for XDCR](prepare-for-xdcr.md), and proceed to the last.

## [](#xdcr-and-community-edition)XDCR and Community Edition

Couchbase has modified the license restrictions to its Couchbase Server Community Edition package, for version 7.0 and higher: in consequence, XDCR is promoted to a commercial-only feature of Enterprise Edition.

Consequently, prior to any attempt to add a remote cluster, the **XDCR** screen displays the following message:

![xdcr screen ce](../_images/manage-xdcr/xdcr-screen-ce.png) 

The provided link takes the reader to detailed information on the new license restrictions, at [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/).

Attempts to establish replications cause the following console message to be displayed:

![xdcr console message ce](../_images/manage-xdcr/xdcr-console-message-ce.png) 

Community-Edition adminstrators who wish to upgrade to version 7.0 or later, and wish to use XDCR, are recommended to consult [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/), for guidance.