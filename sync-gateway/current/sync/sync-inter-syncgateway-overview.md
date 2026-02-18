---
title: Inter-Sync Gateway Replication
description: Use inter-Sync Gateway replication to keep clusters in different
  mobile data centers in sync.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/sync/pages/sync-inter-syncgateway-overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/sync/sync-inter-syncgateway-overview.html)

# Inter-Sync Gateway Replication

> Use inter-Sync Gateway replication to keep clusters in different mobile data centers in sync.  
> _Inter-Sync Gateway_ replication supports resilient, secure, scalable bidirectional synchronization of data cloud-to-edge.

_Related topics_: [Overview](sync-inter-syncgateway-overview.md) | [Run](sync-inter-syncgateway-run.md) | [Manage](sync-inter-syncgateway-manage.md) | [Monitor](sync-inter-syncgateway-monitor.md) | [Conflict](sync-inter-syncgateway-conflict-resolution.md)

_Other Topics_: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) | [Admin REST API](../rest-api/rest-api-admin.md)

> [!IMPORTANT]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see the documentation for the appropriate release.

## [](#introduction)Introduction

Couchbase Sync Gateway’s _[Inter-Sync Gateway Replication![glossary icon](../images/icons/glossaryIconImage2.png)](../glossary.md#inter-sync-gateway-replication)_ feature supports _[cloud-to-edge![glossary icon](../images/icons/glossaryIconImage2.png)](../glossary.md#cloud-to-edge) synchronization_ use cases, where data changes must be synchronized between a centralized cloud cluster and a large number of edge clusters whilst still enforcing fine grained access control. This is an increasingly important enterprise-level requirement.

In the architecture diagram ([Figure 1](#icr-architecture)), the replicator on the active Sync Gateway node ensures that any database changes made to documents in either [Sync Gateway database![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#sync-gateway-database) instance are replicated to the other Sync Gateway instance, in accordance with the replication’s configuration — see [replications](../configuration/configuration-schema-database.md#database-replications-this%5Frep) for configuration details.

![icr replication overview](../_images/icr-replication-overview.svg) 

Figure 1\. Inter-Sync Gateway Replication architecture

## [](#use-cases)Use Cases

### [](#cloud-to-edge-synchronization)Cloud-to-edge synchronization

In this multi-cloud deployment mode large numbers of multiple edge clusters sync with one or more clusters in cloud data centers. Each edge can operate autonomously without network connectivity to the cloud data centers \[[1](#%5Ffootnotedef%5F1 "View footnote.")\].

A typical architecture for this use cases is shown in [Figure 2](#icr-cloud-to-edge)

![icr cloud to edge200712](../_images/icr-cloud-to-edge200712.svg) 

Figure 2\. Cloud-to-edge synchronization

### [](#active-to-active-mobile-synchronization)Active-to-active Mobile Synchronization

Inter-Sync Gateway replication replicates edge clusters containing Sync Gateway nodes between geographically separate cloud-based Sync Gateway deployments. This provides an ideal use-case for inter-Sync Gateway replication, which was designed to keep clusters in different data centers in sync.

Couchbase Server uses the Cross Data Center Replication API ([XDCR](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md)) similarly to replicate between Couchbase Server clusters. **However, inter-Sync Gateway replication feature is specifically designed for Sync Gateway deployments and must be used for replication between mobile clusters.** \[[2](#%5Ffootnotedef%5F2 "View footnote.")\]

[Figure 3](#icr-active-mobile) shows a typical architecture for this use case.

![icr active mobile sync200713](../_images/icr-active-mobile-sync200713.svg) 

Figure 3\. Active-to-active mobile synchronization

## [](#replication-characteristics)Replication Characteristics

### [](#context)Context

Sync Gateway supports the ability to run replications between Sync Gateway clusters using a new websockets based protocol, with the [active replicator![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#active-replicator) [synchronizing![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#sync-function) changes between two [Sync Gateway databases![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#sync-gateway-database).

All replications are based on a [replication definition![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#replication-definition) provided either to the Admin REST API or in Sync Gateway’s configuration file (JSON).

Replications always involve at least one local database. Sync Gateway does not enable replication between two _remote_ nodes, because replications are defined at database level and so at least one database will be local.

All replications take place at the document level (but see also, [Delta Sync](#delta-sync)).

Sync Gateway nodes can opt-out of participating in the replication process using the database-level parameter [sgreplicate\_enabled](../configuration/configuration-schema-database.md#database-sgreplicate%5Fenabled).

_Related configuration elements_: [Database Configuration](../configuration/configuration-schema-database.md) | [replications](../configuration/configuration-schema-database.md#database-replications-this%5Frep) | [remote](../configuration/configuration-schema-database.md#database-replications-this%5Frep-remote) | [sgreplicate\_enabled](../configuration/configuration-schema-database.md#database-sgreplicate%5Fenabled)  
For legacy versions see: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

### [](#protocol)Protocol

Inter-Sync Gateway replications are based on websockets. This is the exact same protocol that is used for replication with Couchbase Lite 2.x clients.

> [!NOTE]
> For users on releases prior to 2.8, SG Replicate provides a HTTP-based replication — see the appropriate release documentation.

The bi-directional, persistent, nature of websocket connections is ideal for applications such as a _continuous_ Sync Gateway replication, which is constantly waiting-for and synchronizing change events.

### [](#types-of-replication)Types of Replication

Replications are either: [adhoc replication![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#adhoc-replication) (REST API only) or [persistent replication![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#persistent-replication). They can also be configured to run in one of two-modes: [continuous![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#rep-continuous) or [one-shot![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#rep-oneshot).

* Persistent  
Persistent replications survive Sync Gateway node restarts and continue running automatically unless configured not to. They can be configured to run in either [continuous![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#rep-continuous) or [one-shot![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#rep-oneshot) mode.
* Ad hoc  
Ad hoc replications are transient, existing only for the period of the replication. They provide a convenient way to:

  * Run one off replications (for example, when troubleshooting)
  * Run on-demand replications after Sync Gateway is started. For instance a replication that needs to be to be run only periodically can be configured as an ad hoc replication by an automated script scheduled to run when needed.

_Related configuration elements_: [replications](../configuration/configuration-schema-database.md#database-replications-this%5Frep) | [continuous](../configuration/configuration-schema-database.md#database-replications-this%5Frep-continuous) | [adhoc](../configuration/configuration-schema-database.md#database-replications-this%5Frep-adhoc)

### [](#delta-sync)Delta Sync

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

With delta-sync enabled on the replication and both databases involved, only the changed data items are transferred.

You can configure replications to use delta-sync by:

* Setting `"enable_delta_sync": true` in the _replication definition_
* Setting `"delta-sync": { "enabled": true}` on both databases in their respective _database definitions_.

> [!NOTE]
> Push replications to pre-2.8 targets do not use Delta Sync

_Related configuration elements_: [Database Configuration](../configuration/configuration-schema-database.md) | [replications](../configuration/configuration-schema-database.md#database-replications-this%5Frep) | [database.delta\_sync](../configuration/configuration-schema-database.md#database-delta%5Fsync) | [enable\_delta\_sync](../configuration/configuration-schema-database.md#database-replications-this%5Frep-enable%5Fdelta%5Fsync)

### [](#collections-support)Collections Support

Inter-Sync Gateway replication supports named collections, including:

* Enabling or disabling collections replication.
* Limit replication to specific collections.
* Map local collections to differently named remote collections.

For detailed configuration of collections parameters (`collections_enabled`, `collections_local`, `collections_remote`), see [Run Inter-Sync Gateway Replication Configuration Schema](../configuration/configuration-schema-isgr.md#replication).

#### [](#collection-mapping)Collection Mapping

Collection mapping allows you to replicate local collections to differently named collections on the remote target. You configure this using two parallel arrays:

* `collections_local` \- specifies the collections to replicate from the source.
* `collections_remote` \- specifies the corresponding target collection names on the remote.

The mapping works positionally, where the first collection in `collections_local` maps to the first collection in `collections_remote`, the second to the second, and so on.

> [!NOTE]
> You must verify all specified collections exist in both source and target Sync Gateway database configurations before starting replication. Sync Gateway does not automatically create missing collections or sync new collections after replication begins.

This collection mapping capability adapts the mapping concept from XDCR for Sync Gateway deployments. For information about [Implicit Mapping](../../../server/current/learn/clusters-and-availability/xdcr-with-scopes-and-collections.md#implicit-mapping) and [Explicit Mapping](../../../server/current/learn/clusters-and-availability/xdcr-with-scopes-and-collections.md#explicit-mapping) in the XDCR documentation.

### [](#directionality)Directionality

Replications are bi-directional. You can _push_, _pull_ or _push and pull_ between the two database endpoints.

_Related configuration elements_: [replications](../configuration/configuration-schema-database.md#database-replications-this%5Frep) | [direction](../configuration/configuration-schema-database.md#database-replications-this%5Frep-direction)

### [](#security)Security

Transport level security is provided for. Use the appropriate prefix in URL (WSS for websockets).

#### [](#authentication)Authentication

Support for Basic Authentication using username and password credentials is provided

#### [](#access-control)Access Control

Data access control is provided by Sync Gateway’s [sync function![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#sync-function) and the username/password credentials. All replicated documents pass through this function ensuring that access permissions are adhered to.

_Related configuration elements_: [Database Configuration](../configuration/configuration-schema-database.md) | [database.sync](../configuration/configuration-schema-database.md#database-sync)

## [](#network-resilience)Network Resilience

Inter-Sync Gateway replications will automatically attempt to restart whenever the node restarts.

Network resiliency is built-in for _continuous_ replications. They respond to network issues such as lost connections, by applying a [persistent exponential backoff![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#persistent-exponential-backoff) policy to attempt reconnection.

The [max\_backoff\_time](../configuration/configuration-schema-database.md#database-replications-this%5Frep-max%5Fbackoff%5Ftime) determines the maximum wait time between retries. When the limit is reached retries are made every `max_backoff_time` minutes. Set `"max_backoff_time": 0` to prevent indefinite retries. Exponential backoff retries will be attempted for up to 5 minutes and then stop if the connection has not been re-established

  
_Related replication definition elements_: [max\_backoff\_time](../configuration/configuration-schema-database.md#database-replications-this%5Frep-max%5Fbackoff%5Ftime)

## [](#high-availability)High Availability

### [](#overview)Overview

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

* Enterprise
* Community

Inter-Sync Gateway Replication provides built-in High Availability (HA) support. It uses _node distribution_ to ensure all running replications are uniformly distributed across all available nodes, regardless of their originating node.

A replication runs on only one node at any given time. When a node fails, the system automatically distributes that node’s replications across any available alternative nodes (providing the replication has been configured on multiple nodes).

> [!TIP]
> To use high-availability, configure the same replication on at least two Sync Gateway nodes.

Even though automatic node-distribution is not available in [COMMUNITY EDITION](https://www.couchbase.com/products/editions), you can make your replications more highly-available.

Simply define the same replication on multiple nodes. They will then run on each of those nodes.

This redundancy provides some resiliency if a node fails. As, although no automatic distribution of replications is done,if the replication is running on multiple nodes then it will continue running on any surviving nodes.

See also: [Examples of Expected behavior](#examples-of-expected-behavior) below.

### [](#node-distribution)Node Distribution

The goal of node distribution is to maintain an optimal balance of replications across the cluster.,with any given replication runs on only one node at any give time.

To achieve this Sync Gateway automatically balances, as equally as possible, the number of replications running on each node.

Where multiple replications are configured on multiple nodes, Sync Gateway automatically distributes these replications across all the available nodes for which the replications are configured. It continually monitors and redistributes replications as the number of available nodes and the number of running replications in a cluster changes.

The nodes' processing load and bandwidth usage is minimized by ensuring that a replicator runs on only one node at any given time — even where it has been configured to run on multiple nodes. This avoids the redundant exchange of data arising from duplicate replication.

### [](#configuration-requirements)Configuration Requirements

To configure a replication to be highly available, include its database and replication definition in the sync gateway configuration on each node in the cluster that you want to be able to run it. _At least two nodes are required._

Node distribution will automatically elect an appropriate node to run them on and take care of redistributing them if a node fails.

_Related configuration elements_\`: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) | [Admin REST API](../rest-api/rest-api-admin.md)

### [](#expected-failure-behavior)Expected Failure Behavior

If a node fails, then Sync Gateway will take any replications configured on multiple nodes, redistribute them across all available remaining nodes and restart them. Node distribution will continually seek to maintain an optimal distribution of replications across available nodes.

#### [](#examples-of-expected-behavior)Examples of Expected behavior

This section provides examples of expected behavior in differing scenarios. It provides a comparison of how behavior differs between [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) and [COMMUNITY EDITION](https://www.couchbase.com/products/editions).

The following scenarios are covered, each involves a sync gateway cluster with multiple nodes:

* Homogenous configuration — see [Example 1](#homogenous-config)
* Homogenous configuration with non-replicating node — see [Example 2](#homogenous-non-rep-node)
* Heterogenous configuration — see [Example 3](#hetero-config)
* Adding more nodes — see [Example 4](#adding-more-nodes)
* Failing node — see [Example 5](#failing-node)

Example 1\. Homogenous configuration

Scenario

* The cluster comprises three Sync Gateway nodes
* The same sync gateway configuration is applied across all nodes
* All nodes are configured to run _Replication Id 1_

* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)
* [COMMUNITY EDITION](https://www.couchbase.com/products/editions)

* Sync Gateway automatically designates one of the three nodes to run _Replication Id 1_.
* If a node goes down, Sync Gateway elects one of the remaining nodes to continue _Replication Id 1_.

Sync Gateway runs _Replication Id 1_ on all nodes in the cluster.

Example 2\. Homogenous configuration with non-replicating node

Scenario

* The cluster comprises three Sync Gateway nodes.
* Each node has the same sync gateway configuration, with one exception. The configuration on _Node 3_ has opted out of replication (`sgreplicate_enabled=false`)
* All Three nodes are configured to run _Replication Id 1_.

* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)
* [COMMUNITY EDITION](https://www.couchbase.com/products/editions)

* Sync Gateway automatically designates either _Node 1_ or _Node 2_ to run the _Replication Id 1_.
* If either _Node 1_ or _Node 2_ fails, Sync Gateway elects the non-failing node.

* Sync Gateway runs _Replication Id 1_ on all nodes in cluster.
* The system ignores the opt-out flag (`sgreplicate_enabled`).

Example 3\. Heterogenous configuration

Scenario

* The cluster comprises three Sync Gateway nodes
* Both _Node 1_ and _Node 2_ are configured to run _Replication Id 1_
* _Node 3_ is configured to run _Replication Id 2_ but **not** _Replication Id 1_

* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)
* [COMMUNITY EDITION](https://www.couchbase.com/products/editions)

* Sync Gateway automatically distributes _Replication Id 1_ and _Replication Id 2_ so that each runs on **one** of _Node 1_, _Node 2_ or _Node 3_, with no node running both replications simultaneously.
* If any node fails whilst running either replication, Sync Gateway elects a non-failing node to continue that replication on. Where two nodes remain the node not running a replication will be chosen.

* Sync Gateway runs _Replication Id1_ on _Node 1_ and _Node 2_ in the cluster
* Sync Gateway runs _Replication Id 2_ on _Node 3_

Note:

* If _Node 3_ fails, then _Replication Id 2_ will not be continued on either of the remaining nodes as it is not configured on them
* Similarly, if either or both of the other nodes (_Node 1_ and _Node 2_) fails, _Node 3_ will not be a candidate to run the corresponding replication.

Example 4\. Adding more nodes

Scenario

* The cluster comprises a single Sync Gateway node
* _Node 1_ is configured to run _Replication Id 1_ and _Replication Id 2_
* LATER . . . _Node 2_ is added to the cluster to run _Replication Id 1_ and _Replication Id 2_.

* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)
* [COMMUNITY EDITION](https://www.couchbase.com/products/editions)

* Sync Gateway designates _Node 1_ run both _Replication Id 1_ and _Replication Id 2_
* LATER . . . when _Node 2_ is added . . .

  * Sync Gateway select one of the _Node 1_ replications to run on _Node 2_; let’s say it chooses _Replication Id 2_
  * Sync Gateway stops _Replication Id 2_ on _Node 1_
  * Sync Gateway starts _Replication Id 2_ on _Node 2_.

* Sync Gateway designates _Node 1_ to run both _Replication Id 1_ and _Replication Id 2_
* WHEN . . . _Node 2_ is added . . . Sync Gateway designates it to run both _Replication Id 1_ and _Replication Id 2_

Example 5\. Failing node

Scenario

* The cluster comprises three Sync Gateway nodes with a homogeneous configuration
* All three nodes are configured to run _Replication Id 1_, _Replication Id 2_ and _Replication Id 3_
* LATER . . . _Node 3_ goes down

* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)
* [COMMUNITY EDITION](https://www.couchbase.com/products/editions)

Sync Gateway automatically distributes the replications, one to each of the nodes

* Lets assume the following distribution:

  * _Node 1_ runs _Replication Id 1_
  * _Node 2_ runs _Replication Id 2_
  * _Node 3_ runs _Replication Id 3_

WHEN . . . _Node 3_ goes down . . . Sync Gateway elects either _Node 1_ or _Node 2_ to continue running _Replication Id 3_

Sync Gateway runs all three replications (_Replication Id 1_ , _Replication Id 2_ and _Replication Id 3_) on all three nodes in the cluster (_Node 1_, _Node 2_ and _Node 3_)

WHEN . . . _Node 3_ goes down . . . _Node 1_ and _Node 2_ continue to run _Replication Id 1_, _Replication Id 2_ and _Replication Id 3_

### [](#monitoring-node-distribution)Monitoring Node Distribution

Use the _\_replicationStatus_ endpoint to access information about which replications are running on which nodes — see: [/{db}/\_replicationStatus/{replicationid}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication/operation/get%5Fdb-%5FreplicationStatus-replicationid)| [/{db}/\_replicationStatus/{replicationid}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Replication/operation/put%5Fdb-%5FreplicationStatus-replicationid)

This information is also collected and available in the log files.

## [](#conflict-resolution)Conflict Resolution

Inter-Sync Gateway **pull** replications support automatic conflict resolution by default (no conflict mode).

In _Pull_ replications the _active_ Sync Gateway detects and resolves conflicts using Last Write Wins strategy in Sync Gateway 4.x+. For cross-version replication scenarios (4.x ↔ 3.x), the configured conflict resolver policy determines the winner or returns an error if it cannot resolve the conflict.

Conflicts are **not** resolved in **push** replications though. The passive end of the push simply detects and rejects any conflicting revisions (`409 Conflict` response).

Both approaches reflect the way conflicts are handled by Couchbase Lite clients. Not surprising since in both instances Couchbase Lite is acting like the active node in an inter-sync gateway exchange.

> [!NOTE]
> Conflicts are only resolved during a **pull** replication. If conflicts occur, you should configure a `pushAndPull` replication.
> 
> _Alternatively_: Run the replicator from the other side; flipping the direction (to `pull`) and the resolution policy (for example `localWins` becomes `remoteWins`).
> 
> See: [Document Conflicts & Resolution in Couchbase Mobile](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)

For [ENTERPRISE EDITION](https://www.couchbase.com/products/editions), a custom conflict resolver policy is available, providing additional flexibility by allowing users to provide their own conflict resolution logic — see: [Inter Sync Gateway Sync - Custom Conflict Resolution](sync-inter-syncgateway-conflict-resolution.md#custom-conflict-resolution-ee)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](sync-with-couchbase-server.md)

###### [](#-3)

Reference material …​

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)
* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Conflict Related Blogs

* [Automatic Conflict Resolution](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)
* [Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/)
* [Conflict Resolution (category)](https://blog.couchbase.com/tag/conflict-resolution/)

---

[1](#%5Ffootnoteref%5F1). This architecture is also known as ship-to-shore or hub-and-spoke. 

[2](#%5Ffootnoteref%5F2). If one-directional XDCR is used alongside Sync Gateway, then Sync Gateway cluster must be in read-only mode.