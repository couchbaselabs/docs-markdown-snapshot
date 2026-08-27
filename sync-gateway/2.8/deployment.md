---
title: Deployment
description: This article covers different aspects of using Sync Gateway and
  Couchbase Server during production.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/deployment.adoc
  xref: xref:2.8@sync-gateway::deployment.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/deployment.html)

# Deployment

When deploying your application for production use you will need to use Sync Gateway and Couchbase Server. This article covers different aspects of using Sync Gateway and Couchbase Server during production.

## [](#where-to-host)Where to Host

Whether hosting on-premise, or in the cloud, you will want to have your Sync Gateway and Couchbase Server sit closely to each other for optimal performance between these two systems. In a production environment, they are expected to be deployed on separate machines. This is because the Sync Gateway is typically deployed to be internet facing and sits in the "Application tier" whilst Couchbase Server is deployed in the "Database tier".

## [](#sizing-and-scaling)Sizing and Scaling

Your physical machine, containers or VMs determines how many active, concurrent users you can comfortably support for a single Sync Gateway.

Alternatively, instead of scaling vertically, you can also scale horizontally by running Sync Gateway nodes as a cluster. (In general, you will want to have at least two Sync Gateway nodes to ensure high-availability in case one should fail.) This means running multiple instances of Sync Gateway on each of several machines, and load-balancing them by directing each incoming HTTP request to a random node.

The Sync Gateway nodes in a cluster have a homogeneous configuration with the exception of import node and replicator nodes.

Import node

Under [convergence/shared bucket access](sync-with-couchbase-server.md), it is recommended that one Sync Gateway node in a cluster be configured for handling document import processing. For high availability, you can configure more than one Sync Gateway node in your cluster to be the import node, although it is strongly discouraged for multiple Sync Gateway nodes in the cluster to be configured for import processing. The configuration of the Sync Gateway import node is slightly different than the "regular" or "non-import" Sync Gateway nodes (see [databases.$db.import\_docs](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-import%5Fdocs)).

Replicator node

if you are using SG Replicate then there will be one designated replicator node whose configuration is different than the rest of the nodes — see [SG-Replicate](#sync-gateway::legacy-sg-replicate.adoc).

Sync Gateway nodes are "shared-nothing," so they don't need to coordinate any state or even know about each other. With multiple Sync Gateways, we recommend placing this cluster behind a load balancer server to coordinate connection requests in clients (see the [Load Balancer](load-balancer.md) guide).

## [](#channel-and-revision-cache)Channel and Revision Cache

Up until Sync Gateway 2.6, the size of channel cache will grew unbounded with the number of channels, regardless of the number of active channels. A properly sized Sync Gateway can scale to deployments with a small to moderate number of channels (in the order of hundreds to tens of thousands of channels). However, since the channel cache can grow unbounded, the Sync Gateway can hit vertical scaling limits, especially as deployments grow in size, in the order of millions of channels.

In Sync Gateway 2.6, the [cache configuration](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-cache) provides more options to tune Sync Gateway caching, enabling the Sync Gateway to vertically scale without potentially running into Out-of-Memory issues.

> [!IMPORTANT]
> Enterprise Edition only
> 
> Tuning the channel and revision cache is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. The Community Edition is configured with default values, and will ignore any of those properties in the configuration file.

There are two categories of settings:

* [Channel cache](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-cache-channel%5Fcache): applies to cases where the number of channels can potentially grow unbounded.
* [Revision cache](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-cache-rev%5Fcache): applies to cases with large document sizes.

## [](#performance-considerations)Performance Considerations

Keep in mind the following notes on performance:

* Sync Gateway nodes don't keep any local state, so they don't require any disk.
* Sync Gateway nodes maintain a channel and revision metadata cache in RAM. Tuning the cache values in the configuration file can speed up the performance (see [Channel and Revision Cache](#channel-and-revision-cache)).
* Sync Gateway is designed for multiprocessing. It uses lightweight threads and asynchronous I/O. Therefore, adding more CPU cores to a Sync Gateway node can speed it up.
* As is typical with databases, writes are going to put a greater load on the system than reads. In particular, every write operation gets processed by the [Sync Function](../current/access-control/sync-function/sync-function.md) and triggers notifications to other clients with read access, who then perform reads to get the new data.
* Each client running a continuous replication has an open socket to be notified of changes, these sockets remain idle most of the time (unless documents are being modified at a very high rate), so the actual data traffic is low — the issue is just managing that many sockets. We recommend developers to optimize how many connections they need to open to the sync tier (see the [OS Level Tuning](os-level-tuning.md) guide).
* In a Sync Gateway deployment with [GSI/N1QL indexing](indexing.md), the resources allocated to the Couchbase Server index node must be sufficient to support Sync Gateway operations.
* As Sync Gateway is optimized to use RAM, performance can be gained (or at minimum not lost) by changing the Linux swappiness value to 0 (see the [Swap Space and Kernel Swappiness](../../server/current/install/install-swap-space.md) guide).