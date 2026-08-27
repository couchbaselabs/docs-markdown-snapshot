---
title: Data Sync
description: Introducing Couchbase Lite's Peer-to-Peer Synchronization feature
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/objc/pages/landing-replications.adoc
  xref: xref:3.2@couchbase-lite:objc:landing-replications.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.2/objc/landing-replications.html)

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