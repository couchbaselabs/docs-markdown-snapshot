---
title: Data Sync
description: Introducing Couchbase Lite's Peer-to-Peer Synchronization feature
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/objc/pages/landing-replications.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/current/objc/landing-replications.html)

# Data Sync

## [](#data-sync)Data Sync

### [](#)

Couchbase Lite for Objective-C supports the flexible and secure replication and synchronization of data locally, centrally or at the edge.

### [](#-2)

![docs listener diagram](../_images/docs-listener-diagram.png) 

### [](#-3)

#### [](#locally)Locally

You can replicate local databases _on-device_ — see: [Intra-Device](dbreplica.md)

#### [](#centrally)Centrally

You can sync with a centralized Couchbase Server database using Sync Gateway — see: [Remote Sync Gateway](replication.md)

#### [](#at-the-edge)At the edge

You can sync directly with other edge devices, peer-to-peer, using a listener to interact with the Couchbase Lite replicator — see: [Peer-to-Peer Sync](#objc:landing-p2psync.adoc)