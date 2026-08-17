---
title: Peer-to-Peer Device Sync
description: Introducing Couchbase Lite's Peer-to-Peer Synchronization feature
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/landing-p2psync.adoc
  xref: xref:2.8@couchbase-lite:objc:landing-p2psync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/landing-p2psync.html)

# Peer-to-Peer Device Sync

## [](#peer-to-peer-synchronization)Peer-to-Peer Synchronization

###### [](#)

Couchbase Lite's Peer-to-Peer Synchronization solution offers secure storage and bidirectional synchronization of data between edge devices without the need for a centralized cloud-based control point.

Two Couchbase Lite instances can directly synchronize with each other, rather than with a Sync Gateway instance, by using a listener to interact with a Couchbase Lite replicator.

###### [](#-2)

![docs listener diagram](../_images/docs-listener-diagram.png) 

Couchbase Lite provides two options for implementing the required listener in IP-based networks; an out-of-the-box listener implementation or a framework to custom build your own listener.

## [](#-3)

###### [](#-4)

Out-of-the-box Listener

* Simplify development — sync with just a few lines of code
* Optimize bandwidth — built-in Delta-Sync support
* Sync securely — built-in TLS encryption and authentication support
* Efficiently manage conflicts — built-in conflict resolution support.
* [Peer-to-Peer Data Sync](../../current/objc/p2psync-websocket.md)

###### [](#-5)

Custom Build Listener

* A flexible framework enabling you to custom build a listener to meet your own requirements.
* [Peer-to-Peer Synchronization (custom)](../../current/objc/p2psync-custom.md)