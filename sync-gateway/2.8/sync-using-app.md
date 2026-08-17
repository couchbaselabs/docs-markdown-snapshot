---
title: Sync with Couchbase Lite
description: Use Sync Gateway to sync with Couchbase Lite apps.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/sync-using-app.adoc
  xref: xref:2.8@sync-gateway::sync-using-app.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/sync-using-app.html)

# Sync with Couchbase Lite

> Use Sync Gateway to sync with Couchbase Lite apps.  

## [](#syncing-with-couchbase-lite-apps)Syncing with Couchbase Lite Apps

Couchbase Lite client applications use a Replicator process to synchronize their local database, through a Sync Gateway database, to a remote Couchbase Server database (server- or cloud-based) — see: [\[fig-sync-diag\]](#fig-sync-diag).

![svr sgw cbl](_images/svr-sgw-cbl.png) 

Figure 1\. Sync from Cloud/Server to Edge

Pull Replication

This is the process by which clients running Couchbase Lite download database changes from the remote (server) source database to the local target database

Push Replication

This is the process by which clients running Couchbase Lite upload database changes from the local source database to the remote (server) target database

For more on how to build applications using Sync Gateway replication see the Couchbase Lite documentation set for the appropriate language:

Related Couchbase Lite content

[Android](#2.8@couchbase-lite:android:learn/replication.adoc#starting-a-replication) | [C#](#2.8@couchbase-lite:csharp:learn/replication.adoc#starting-a-replication) | [Java](#2.8@couchbase-lite:java:learn/replication.adoc#starting-a-replication) | [Objective-C](#2.8@couchbase-lite:objc:learn/replication.adoc#starting-a-replication) | [Swift](#2.8@couchbase-lite:swift:learn/replication.adoc#starting-a-replication)

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)