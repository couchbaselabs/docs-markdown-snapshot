---
title: List of Architecture Diagrams
description: A quick reference to some of the architecture diagrams in Couchbase
  documentation.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/architecture-diagrams.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/learn/architecture-diagrams.html)

# List of Architecture Diagrams

> A quick reference to some of the architecture diagrams in Couchbase documentation. 

Throughout the Couchbase documentation-set, explanations of the architecture of Couchbase Server are supported diagrammatically. Each diagram is co-located with its textual description. This page provides a quick-reference, whereby some of the most important diagrams can be directly accessed.

Diagrams are provided for the following topics. Click on the thumbnails or other links to access the full-size diagrams and accompanying, detailed descriptions.

## [](#multidimensional-scaling)Multidimensional Scaling

Couchbase Server supports _multidimensional scaling_, whereby services can be distributed and resourced with the greatest flexibility, across the designated nodes of a cluster.

[![cbClusterWithServicesProduction](_images/services-and-indexes/services/cbClusterWithServicesProduction.png)](services-and-indexes/services/services.md#setting-up-services)

This is explained in [Setting Up Services](services-and-indexes/services/services.md#setting-up-services).

## [](#data-service)Data Service

The Couchbase _Data Service_ is the most fundamental of all Couchbase services, providing access to data in memory and on disk.

[![dataServiceArchitecture](_images/services-and-indexes/services/dataServiceArchitecture.png)](services-and-indexes/services/data-service.md)

See [Data Service](services-and-indexes/services/data-service.md) for a description of the Data Service' architecture, and the interactions of its inner components.

## [](#data-service-rebalance-stages)Data-Service Rebalance Stages

_Rebalance_ redistributes data, indexes, event processing and query processing among available nodes. Data is moved in stages, the progress through which is observable, allowing rates of progress to be determined.

[![replicaVbucketMove](_images/clusters-and-availability/replicaVbucketMove.png)](clusters-and-availability/rebalance.md#data-service-rebalance-stages)

See [Rebalance](clusters-and-availability/rebalance.md), for an overview of rebalance and its significance to different services.

## [](#durability)Durability

Couchbase Server provides _durability_, which ensures the greatest likelihood of data-writes surviving unexpected anomalies, such as node-outages.

[![durabilityDiagram](_images/data/durabilityDiagram.png)](data/durability.md)

See [Durability](data/durability.md) for a full description, including the _protection guarantees_ provided.

## [](#alternate-addresses)Alternate Addresses

Couchbase Server allows an _alternate address_ to be assigned to any individual cluster-node, and an _alternate port number_ to be assigned to any service running on that node.

[![externalAddressDiagram01](_images/clusters-and-availability/externalAddressDiagram01.png)](clusters-and-availability/connectivity.md#alternate-addresses)

For information on use cases and pointers to procedures for applying alternate addresses, see [Alternate Addresses](clusters-and-availability/connectivity.md#alternate-addresses).

## [](#query-service)Query Service

The Couchbase _Query Service_ supports the querying of data by means of the N1QL query language.

[![queryServiceArchitecture](_images/services-and-indexes/services/queryServiceArchitecture.png)](services-and-indexes/services/query-service.md)

Its architecture and the query processing-sequence it supports are explained in [Query Service](services-and-indexes/services/query-service.md).

## [](#index-service)Index Service

The Couchbase _Index Service_ supports the creation of primary and secondary indexes on items stored within Couchbase Server.

[![indexServiceArchitecture](_images/services-and-indexes/services/indexServiceArchitecture.png)](services-and-indexes/services/index-service.md)

Components essential for the Index Service reside not only on each node to which the Index Service is assigned, but also on each node to which the Data Service is assigned, as shown by the illustration in [Index Service](services-and-indexes/services/index-service.md).

## [](#search-service)Search Service

The Couchbase _Search Service_ supports the creation of specially purposed indexes for _Full Text Search_.

[![searchServiceArchitecture2](_images/services-and-indexes/services/searchServiceArchitecture2.png)](services-and-indexes/services/search-service.md)

When a _Search Index_ is created by means of the Search Service, its handling of data for the vBuckets is divided equally among the established search-index partitions, as shown by the illustration in [Search Service](services-and-indexes/services/search-service.md).

## [](#backup-service)Backup Service

The Couchbase _Backup Service_ supports the scheduling of full and incremental data backups, either for specific individual buckets, or for all buckets on the cluster. This includes specifying _time windows_, for the automated merging of backups that have been previously accomplished.

[![mergeDiagram](_images/services-and-indexes/services/mergeDiagram.png)](services-and-indexes/services/backup-service.md#specifying-merge-offsets)

For more information, see [Backup Service](services-and-indexes/services/backup-service.md).

## [](#cluster-manager)Cluster Manager

The Couchbase _Cluster Manager_ runs on all the nodes of a cluster, maintaining essential per-node processes, and coordinating cluster-wide operations.

[![clusterManagerArchitecture2](_images/clusters-and-availability/clusterManagerArchitecture2.png)](clusters-and-availability/cluster-manager.md)

Its architecture is explained in [Cluster Manager](clusters-and-availability/cluster-manager.md).

This page also provides a detailed diagram for the most important component of the Cluster Manager, [ns-server](clusters-and-availability/cluster-manager.md#ns-server).

## [](#intra-cluster-replication)Intra-Cluster Replication

The Couchbase _replication architecture_ keeps cluster-data highly available, by replicating data across the nodes of a cluster, using the _Database Change Protocol_.

[![vBucketReplication](_images/clusters-and-availability/vBucketReplication.png)](clusters-and-availability/intra-cluster-replication.md)

This is explained in [Intra-Cluster Replication](clusters-and-availability/intra-cluster-replication.md).

## [](#cross-data-center-replication-xdcr)Cross Data Center Replication (XDCR)

_Cross Data Center Replication_ (XDCR) is the process whereby data can be replicated to a remote cluster.

[![unidirectional xdcr](_images/xdcr/unidirectional-xdcr.png)](clusters-and-availability/xdcr-overview.md#xdcr-direction-and-topology)

The topographical options for XDCR set-up are shown by the diagrams in [XDCR Direction and Topology](clusters-and-availability/xdcr-overview.md#xdcr-direction-and-topology).

## [](#xdcr-advanced-filtering)XDCR Advanced Filtering

XDCR Advanced Filtering allows specified subsets of documents to be replicated from the source bucket.

[![filter replication diagram 2 v2](_images/xdcr/filter-replication-diagram-2-v2.png)](clusters-and-availability/xdcr-filtering.md)

Information on the available options for document-selection is provided in [XDCR Advanced Filtering](clusters-and-availability/xdcr-filtering.md).

## [](#xdcr-with-scopes-and-collections)XDCR with Scopes and Collections

XDCR allows documents to be mapped between different source and target collections.

[![xdcr implicit mapping diagram](_images/clusters-and-availability/xdcr-implicit-mapping-diagram.png)](clusters-and-availability/xdcr-with-scopes-and-collections.md)

Detailed information is provided in [XDCR with Scopes and Collections](clusters-and-availability/xdcr-with-scopes-and-collections.md).

## [](#server-group-awareness)Server Group Awareness

_Server Group Awareness_ allows individual server-nodes to be assigned to specific _groups_, within a Couchbase Cluster. This allows active vBuckets and indexes to be maintained on groups other than those of their corresponding replica vBuckets and index replicas; so that if a group goes offline, vBuckets and indexes remain available on other groups.

[![groups two equal](_images/clusters-and-availability/groups-two-equal.png)](clusters-and-availability/groups.md)

Possible group layouts, and the effects of failover, are illustrated diagrammatically in [Server Group Awareness](clusters-and-availability/groups.md).

## [](#data-size-limits)Data Size Limits

A data-item stored by Couchbase Server has multiple inner components, each of which has a fixed size limit.

[![item maximum sizes](_images/data/item-maximum-sizes.png)](data/data.md#size-limits)

Components and their sizes are described in [Data Size Limits](data/data.md#size-limits).

## [](#data-model)Data Model

The Couchbase _Data Model_ is based on using JSON documents to store data items.

[![jsonDataModel](_images/data/jsonDataModel.png)](data/document-data-model.md#documents-versus-tables)

The [Relational and JSON](data/document-data-model.md#documents-versus-tables) data models have fundamental differences, explained here graphically.

## [](#vbuckets)vBuckets

Couchbase _buckets_, which are used to group data-items logically, are mapped to underlying shards on disk, known as vBuckets.

[![vbucketToNodeMapping](_images/buckets-memory-and-storage/vbucketToNodeMapping.png)](buckets-memory-and-storage/vbuckets.md#understanding-vbuckets)

This is explained in [Understanding vBuckets](buckets-memory-and-storage/vbuckets.md#understanding-vbuckets).

## [](#compression)Compression

_Compression_ is used by Couchbase Server to maximize resources and heighten performance.

[![compressionDiagram](_images/buckets-memory-and-storage/compressionDiagram.png)](buckets-memory-and-storage/compression.md#where-data-compression-can-be-used)

The communication-paths that benefit are listed and explained in [Where Compression is Used](buckets-memory-and-storage/compression.md#where-data-compression-can-be-used).

## [](#saving-new-items)Saving New Items

When Couchbase Server receives new data from a client, it saves to disk, and also replicates across nodes.

[![createDocSequence3](_images/buckets-memory-and-storage/createDocSequence3.png)](buckets-memory-and-storage/memory-and-storage.md#saving-new-items)

A sequence of diagrams is provided to show the memory and storage architecture whereby Couchbase Server handles [Saving New Items](buckets-memory-and-storage/memory-and-storage.md#saving-new-items).

## [](#memory-quotas)Memory Quotas

Couchbase Server monitors the memory used by buckets with respect to fixed _memory quotas_. If watermarks are exceeded, automated management action is taken, to ensure that the data items most needed are retained in memory, and those less needed removed.

[![tunableMemory](_images/buckets-memory-and-storage/tunableMemory.png)](buckets-memory-and-storage/memory.md#ejection)

This is explained in detail, and the relations of memory quotas represented graphically, in [Ejection](buckets-memory-and-storage/memory.md#ejection).

## [](#multiple-root-certificates)Multiple Root Certificates

Couchbase Server supports use of multiple CA (or _root_) certificates, for a single cluster. This allows an individual node either to use a CA that is also used by one or more other nodes; or to use a CA that is used by no other node. This may be used during CA certificate rotation: a new CA is uploaded, node certificates are changed one by one, and finally, the old CA is removed.

[![clusterWithCerts](_images/security/clusterWithCerts.png)](security/using-multiple-cas.md#illustration)

For detailed information, see [Using Multiple Root Certificates](security/using-multiple-cas.md).