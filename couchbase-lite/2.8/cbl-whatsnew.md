---
title: What&#8217;s New
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/ROOT/pages/cbl-whatsnew.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite::cbl-whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/cbl-whatsnew.html)

# What&#8217;s New

## [](#couchbase-lite-release-2-8)Couchbase Lite Release 2.8

In addition to significant performance and resilience enhancements Couchbase Lite 2.8 introduces enhanced support for peer-to-peer synchronization.

### [](#new-features)New Features

#### [](#peer-to-peer-synchronization)Peer-to-Peer Synchronization

Using Couchbase Lite's Peer-to-Peer Synchronization solution, you can build offline-first applications on edge devices that directly collaborate in secure bi-directional database synchronization without depending on centralized cloud-based control.

The solution provides an out-of-the-box implementation of a websocket based listener for use in peer-to-peer applications communicating over in IP-based networks.

Read More . . . [Swift](#couchbase-lite:swift:learn/swift-landing-p2psync.adoc) | [Objective-C](#couchbase-lite:objc:learn/objc-landing-p2psync.adoc) | [Java](#couchbase-lite:java:learn/java-landing-p2psync.adoc) | [Android](#couchbase-lite:android:learn/java-android-landing-p2psync.adoc) | [C#.Net](#couchbase-lite:csharp:learn/csharp-landing-p2psync.adoc)

### [](#other-changes)Other Changes

The API has been enhanced with the following changes:

* The _Database Close_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _Database Delete_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _Replicator Is Document Pending_ method checks whether or not the document with the given ID has any pending revisions to push
* The _Replicator Get Pending Document_ method gets the Ids of all documents currently pending push
* _Meta Revision ID_ property is now available as a metadata property, which can be accessed directly in queries

Release Notes

[Swift](#couchbase-lite:swift:release-notes.adoc) | [Objective-C](#couchbase-lite:objc:release-notes.adoc) | [Java](#couchbase-lite:java:release-notes.adoc) | [Android](#couchbase-lite:android:release-notes.adoc) | [C#.Net](#couchbase-lite:csharp:release-notes.adoc)