---
title: Data Sync
description: Introducing Couchbase Lite's Peer-to-Peer Synchronization feature
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/java/pages/landing-replications.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:java:landing-replications.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/java/landing-replications.html)

# Data Sync

## [](#data-sync)Data Sync

###### [](#)

Couchbase Lite for Java provides functionality that supports the flexible and secure replication and synchronization of data whether locally, centrally or at the edge.

###### [](#-2)

![docs listener diagram](../_images/docs-listener-diagram.png) 

## [](#-3)

### [](#locally)Locally

You can replicate local databases _on-device_ — see: [Intra-device Data Sync](../../current/java/dbreplica.md)

### [](#centrally)Centrally

You can sync with a centralized Couchbase Server database using Sync Gateway — see: [Remote Sync using Sync Gateway](../../current/java/replication.md)

### [](#at-the-edge)At the edge

You can sync directly with other edge devices, peer-to-peer, using a listener to interact with the Couchbase Lite replicator — see: [Landing P2Psync](#couchbase-lite:java:landing-p2psync.adoc)