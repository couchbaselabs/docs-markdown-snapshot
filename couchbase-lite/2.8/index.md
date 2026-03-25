---
title: Introduction
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/ROOT/pages/index.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/index.html)

# Introduction

# Introducing Couchbase Lite

###### 

Couchbase Lite is an embedded, NoSQL JSON Document Style database for your mobile apps.

You can use Couchbase Lite as a standalone embedded database within your mobile apps, or with Sync Gateway and Couchbase Server to provide a complete cloud to edge synchronized solution

###### 

![get the agility of sql and the flexibility of json](_images/get-the-agility-of-sql-and-the-flexibility-of-json.svg) 

##### Work locally . . .

* Couchbase Lite is designed to work with data stored locally and includes

  * The ability to write queries with semantics based on SQL.
  * _Full-Text Search_ queries on documents stored locally.
  * The ability to store document attachments (blobs), for example images or PDF files.

##### Sync at the edge . . .

* It manages data sync automatically through:

  * A replication protocol built over WebSockets to synchronize data with Sync Gateway.
  * A Peer-to-Peer sync implementation to synchronize data between Couchbase Lite clients without dependency upon centralized control.