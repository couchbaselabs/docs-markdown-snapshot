---
title: Deployment
description: When deploying your application for production use you will need to
  use Sync Gateway and Couchbase Server.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/deploy/pages/deployment.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.3/deploy/deployment.html)

# Deployment

> When deploying your application for production use you will need to use Sync Gateway and Couchbase Server.  
> This article covers different aspects of using Sync Gateway and Couchbase Server during production.

## [](#where-to-host)Where to Host

Whether hosting on-premise or in the cloud, you will want to have your Sync Gateway and Couchbase Server sit close to each other for optimal performance between these two systems. In a production environment, they are expected to be deployed on separate machines. This is because the Sync Gateway is typically deployed to be internet-facing and sits in the "Application tier" whilst Couchbase Server is deployed in the "Database tier".

## [](#sizing-and-scaling)Sizing and Scaling

Your physical machine, container or VM, determines how many active concurrent users you can comfortably support for a single Sync Gateway.

Alternatively, instead of scaling vertically, you can also scale horizontally by running Sync Gateway nodes as a cluster. (In general, you will want to have at least two Sync Gateway nodes to ensure high-availability in case one should fail.) This means running multiple instances of Sync Gateway on each of several machines, and load-balancing them by directing each incoming HTTP request to a random node.

The Sync Gateway nodes in a cluster have a homogeneous configuration with the exception of import node and replicator nodes.

Import node

An import node is a node designated to handle document import processing. You can have zero, one or more of these nodes in a cluster \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]. Use the [database.import\_docs](../configuration/configuration-schema-database.md#import%5Fdocs) \[[2](#%5Ffootnotedef%5F2 "View footnote.")\]property to configure an import node — see also: [Sync with Couchbase Server](../sync/sync-with-couchbase-server.md)

It is recommended that one Sync Gateway node in a cluster be configured for handling document import processing. For high availability, you can configure more than one Sync Gateway node in your cluster to be the import node, although it is strongly discouraged for multiple Sync Gateway nodes in the cluster to be configured for import processing. The configuration of the Sync Gateway import node is slightly different than the "regular" or "non-import" Sync Gateway nodes — see [database.import\_docs](../configuration/configuration-schema-database.md#import%5Fdocs).

Replicator node

If you are using inter-Sync Gateway replication then you will have a designated replicator node whose configuration is different than the rest of the nodes — see [Inter Sync Gateway Sync - Overview](../sync/sync-inter-syncgateway-overview.md).

Sync Gateway nodes are "shared-nothing," so they don’t need to coordinate any state or even know about each other. With multiple Sync Gateways, we recommend placing this cluster behind a load balancer server to coordinate connection requests in clients (see the [Load Balancer](load-balancer.md) guide).

## [](#channel-and-revision-caches)Channel and Revision Caches

> [!IMPORTANT]
> Enterprise Edition only
> 
> Tuning the channel and revision cache is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.  
> The Community Edition is configured with default values. Changing these values has no effect.

* _Channel_  
Applies to cases where the number of channels can potentially grow unbounded — see: [database.cache.channel\_cache](../configuration/configuration-schema-database.md#database-cache-channel%5Fcache)The size of channel cache will grow unbounded with the number of channels, regardless of the number of active channels.  
A properly sized Sync Gateway can scale to deployments with a small to moderate number of channels (in the order of hundreds to tens of thousands of channels). However, since the channel cache can grow unbounded, the Sync Gateway can hit vertical scaling limits, especially as deployments grow in size, in the order of millions of channels.
* _Revision_  
Applies to cases with large document sizes — see: [database.cache.rev\_cache](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache).

## [](#performance-considerations)Performance Considerations

Keep in mind the following notes on performance:

* Sync Gateway nodes don’t keep any local state, so they don’t require any disk.
* Sync Gateway nodes maintain a channel and revision metadata cache in RAM. Tuning the cache values in the configuration file can speed up the performance (see [Channel and Revision Cache](#channel-and-revision-cache)).
* Sync Gateway is designed for multiprocessing. It uses lightweight threads and asynchronous I/O. Therefore, adding more CPU cores to a Sync Gateway node can speed it up.
* As is typical with databases, writes are going to put a greater load on the system than reads. In particular, every write operation gets processed by the [Sync Function](../access-control/sync-function/sync-function.md) and triggers notifications to other clients with read access, who then perform reads to get the new data.
* Each client running a continuous replication has an open socket to be notified of changes. These sockets remain idle most of the time (unless documents are modified at a very high rate), so the actual data traffic is low — the issue is just managing that many sockets. We recommend developers to optimize how many connections they need to open to the sync tier (see the [OS Level Tuning](os-level-tuning.md) guide).
* In a Sync Gateway deployment with [GSI/SQL++ indexing](indexing.md), the resources allocated to the Couchbase Server index node must be sufficient to support Sync Gateway operations.
* As Sync Gateway is optimized to use RAM, performance can be gained (or at minimum not lost) by changing the Linux swappiness value to 0 (see the [Swap Space and Kernel Swappiness](../../../server/current/install/install-swap-space.md) guide).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](../start-here/get-started-prepare.md)
* [Install](../start-here/get-started-install.md)
* [Verify](../start-here/get-started-verify-install.md)

###### [](#-3)

Product Information

* [Release Notes](../product-notes/release-notes.md)
* [Compatibility Matrix](../product-notes/compatibility.md)
* [Supported OS](../product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). Since 2.7 

[2](#%5Ffootnoteref%5F2). For Pre-3.0 legacy configuration see: [Configuration Properties (legacy Pre3.0)](../configuration/configuration-properties-legacy.md)