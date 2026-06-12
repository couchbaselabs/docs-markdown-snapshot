---
title: Cross Data Center Replication (XDCR)
description: Cross Data Center Replication (XDCR) allows data to be replicated
  across clusters in cloud environments or on-premises.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/xdcr/xdcr.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:clusters:xdcr/xdcr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/xdcr/xdcr.html)

# Cross Data Center Replication (XDCR)

> Cross Data Center Replication (XDCR) allows data to be replicated across clusters in cloud environments or on-premises. 

XDCR replicates data between clusters. XDCR can protect against data-center failures and provides high-performance access to data for globally distributed mission-critical applications. Replications, once established, continuously replicate data until they're paused or deleted.

## [](#replication-sources-and-destinations)Replication Sources and Destinations

XDCR replicates data from a specific bucket on a source cluster to a specific bucket on a destination (or target) cluster.

> [!NOTE]
> If the source and/or destination buckets are deactivated, the replication will be removed.

Data from the source bucket is pushed to the destination bucket using an XDCR agent, running on the source cluster, using the Cluster Change Protocol. Any bucket on a cluster can be specified as a source or a destination for one or more XDCR replications.

Replication sources and destinations can be on clusters in an organization. The source cluster can be in a different [project](../../projects/projects.md) from the destination cluster.

You can create replications for single node or multi-node clusters.

> [!IMPORTANT]
> You cannot [create a replication](manage-xdcr-replications.md#create-replication) between 2 Capella operational clusters that are within 2 different [cloud service providers](../../clouds/cloud-providers.md) (CSPs).

### [](#about-scopes-and-collections)About Scopes and Collections

All Capella clusters have the option to replicate data from a specific scope and collection on the source cluster to a specific scope and collection on a destination cluster. If identically named scopes and collections have been defined on the source and destination, data can optionally be replicated from each scope and collection on the source to each corresponding, identically named scope and collection on the destination. Alternatively, replication can be explicitly configured to occur between differently named scopes and collections.

### [](#intra-cluster-xdcr)About Intra-cluster XDCR

XDCR is traditionally used for inter-cluster replication: the source bucket and the destination bucket are on different clusters. However, Capella also supports **intra-cluster** XDCR — where the source bucket and the destination bucket are on the same cluster.

To set up intra-cluster XDCR, you will specify the source cluster as the destination cluster when creating a replication.

## [](#what-can-be-replicated)What Can Be Replicated

XDCR only replicates bucket data; it does not replicate indexes. Administrators must replicate indexes manually or through automated processes. When administrators push index-definitions to the destination cluster, the destination cluster regenerates the indexes.

When the source cluster encounters non-UTF-8 encoded document IDs, XDCR automatically filters them out of replication and does not transfer them to the destination cluster. For each such ID, the source cluster writes warning output to `xdcr_errors.*` log files.

### [](#active-active-xdcr-with-app-services)Active-Active XDCR with App Services

Couchbase Server 7.6.6 and App Services 4.0+ support bi-directional (active-active) XDCR replications between clusters that have App Services endpoints linked to their buckets. For more information, see [Active-Active XDCR with Sync Gateway](../../../server/current/learn/clusters-and-availability/xdcr-active-active-sgw.md) in the Couchbase Server documentation.

#### [](#requirements-for-active-active-xdcr-with-app-services)Requirements for Active-Active XDCR with App Services

To use active-active XDCR with App Services, you must have:

* Couchbase Server 7.6.6+
* App Services 4.0+ on both clusters
* Cross Cluster Versioning enabled on both source and target buckets (automatically configured when using [Active-Active XDCR with Sync Gateway](../../../server/current/learn/clusters-and-availability/xdcr-active-active-sgw.md))

#### [](#how-active-active-xdcr-with-app-services-works)How Active-Active XDCR with App Services Works

When you create a replication between clusters with App Services endpoints, Capella:

* Automatically enables Cross Cluster Versioning (CCV) on both source and target buckets if not already set.
* Automatically sets the `mobile` flag to `Active` for all legs of the replication.
* Stores Hybrid Logical Vector (HLV) metadata in document extended attributes to support conflict resolution.
* Enables bi-directional sync between App Services endpoints and the underlying buckets.

#### [](#previous-limitations-removed)Previous Limitations Removed

Earlier versions of App Services (before 4.0) prevented XDCR replications when App Services endpoints linked to buckets. App Services 4.0+ removes these limitations and now supports:

* Bi-directional replication between App Services clusters.
* Mixed replication topologies like some buckets with App Services and some without.
* Automatic conflict resolution for concurrent changes from both mobile clients and XDCR.

> [!WARNING]
> Bi-directional XDCR with App Services versions earlier than 4.0 can cause data corruption. Only use bi-directional replication when both clusters run Server 7.6.6+ and App Services 4.0+.

## [](#xdcr-direction)Replication Direction

XDCR can occur between source and destination clusters in either of the following ways:

Unidirectional (One Way)

XDCR replicates data from a specified source bucket to a specified destination bucket. Although applications could use the replicated data on the destination cluster for routine data serving, it serves principally as a backup to support disaster recovery.

Bidirectional (Two Way)

XDCR replicates data from a specified source bucket to a specified destination bucket, and simultaneously replicates data from the destination bucket back to the source bucket. This allows applications to use both buckets for serving data, which may provide faster data access for users and applications in remote geographies.

Technically, XDCR only performs unidirectional replication. XDCR creates a bidirectional topology by implementing two unidirectional replications, in opposite directions, between two clusters; such that a bucket on each cluster functions as both source and destination.

When creating a replication from one Capella cluster to another, you'll specify whether to make the replication bidirectional. If not specified, the replication is unidirectional from the source bucket to the destination bucket and appears under the **Replication** tab of the source cluster. If the replication is configured to be bidirectional, the replication will appear under the **Replication** tab of both the source cluster and the destination cluster.

When creating a replication from Capella to a self-managed cluster (which is a cluster established outside Capella), the replication can only be specified as unidirectional. This is because a replication from the self-managed cluster to Capella cannot be entirely configured on Capella: it needs partially to be configured on the self-managed cluster itself. For instructions, see [Create a Replication to Capella from a Self-Managed Cluster](manage-xdcr-replications.md#from-on-prem-to-capella).

Learn more about XDCR direction and topology in the [Couchbase Server documentation](../../../server/current/learn/clusters-and-availability/xdcr-overview.md#xdcr-direction-and-topology).

## [](#xdcr-advanced-filtering)Replication Filtering

XDCR filtering allows XDCR to replicate specified subsets of documents from the source bucket. A document can be included in or excluded from a filtered replication, based on the document's fields and values.

When a replication starts, the cluster examines the specified source bucket, and determines which documents to replicate:

* If XDCR filtering is not applied, XDCR replicates each document in the source bucket to the target.
* If XDCR filtering is applied, each document in the source bucket is examined; but XDCR only replicates those documents that meet the specified filtering criteria.

XDCR filters are configured when creating a replication. For more information on filters, see the [Couchbase Server documentation](../../../server/current/learn/clusters-and-availability/xdcr-filtering.md).

## [](#conflict-resolution)Conflict Resolution

In some cases, especially when bidirectionally replicated data is being modified by applications in different locations, conflicts may arise: meaning that the data of one or more documents have been differently modified more or less simultaneously, requiring resolution. XDCR provides two types of conflict resolution, based on either sequence number or timestamp, whereby conflicted data can be saved consistently on source and target.

Sequence Number

XDCR resolves conflicts by referring to documents' sequence numbers. Couchbase maintains sequence numbers per document and increments them during every document update. XDCR compares the sequence numbers of source and target documents, and the document with the higher sequence number prevails.

Timestamp

Timestamp-based conflict resolution uses the document timestamp (stored in the CAS) to resolve conflicts. XDCR compares the timestamps associated with the most recent updates of source and target documents. The document whose updates have the more recent timestamp prevails.

The conflict resolution policy configured on the source and destination buckets determines the type of conflict resolution that a given replication uses. Administrators configure conflict resolution on a per-bucket basis at [bucket creation time](../data-service/manage-buckets.md#add-bucket), and it cannot change later.

Learn more about XDCR conflict resolution in the [Couchbase Server documentation](../../../server/current/learn/clusters-and-availability/xdcr-conflict-resolution.md).

## [](#administering-replications)Administering Replications

For information on how to create, observe, pause, and delete replications, refer to [Manage Replications](manage-xdcr-replications.md).