---
title: New in 3.2
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/ROOT/pages/cbl-whatsnew.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.2@couchbase-lite::cbl-whatsnew.adoc[]
---

[View original HTML](/couchbase-lite/3.2/cbl-whatsnew.html)

# New in 3.2

> [!NOTE]
> Couchbase Lite 3.0 introduces some breaking changes.  
> If you’re upgrading from 2.x, refer to the appropriate upgrade page — see: [Upgrading](#lbl-upgrade).  
> You should be able to upgrade from 3.0.x to 3.1.x without manual intervention.

## [](#release-3-2-4-june-2025)Release 3.2.4 (June 2025)

Couchbase Lite Release 3.2.4 introduces fixes and enhancements for:

[Android](android/releasenotes.md#maint-latest)| [C](c/releasenotes.md#maint-latest)| [.NET](csharp/releasenotes.md#maint-latest)| [Java](java/releasenotes.md#maint-latest)| [Objective-C](objc/releasenotes.md#maint-latest)| [Swift](swift/releasenotes.md#maint-latest)

## [](#release-3-2-3-april-2025)Release 3.2.3 (April 2025)

### [](#new-features)New Features

#### [](#swift-api-enhancements)Swift API Enhancements

Couchbase Lite 3.2.3 introduces Reactive APIs in Swift. The Reactive APIs enable you map Couchbase Lite documents directly to Swift models, and then bind a model to a view representing the user interface. The user interface is automatically updated when the underlying data changes. The new Reactive APIs provide the following benefits:

* Native adherence to Swift’s Codable protocol, enabling automatic encoding and decoding between Couchbase Lite documents and Swift codable model objects. You can retrieve documents from the collection as decodable model objects. You can also save, delete, and purge model objects encoded as documents in the collection.
* The ability to decode Couchbase SQL++ query results directly into model objects. This makes queries observable, so that you can refresh the application automatically as the results change.
* Access to the Combine framework and the Observation framework, enabling you to publish change notifications whenever a query result changes, or documents in a collection change, or a replicator’s status changes.

For more information about Reactive APIs in Swift, see:

* [Reactive APIs](swift/reactive.md)

#### [](#peer-to-peer-synchronization-in-c)Peer-to-Peer Synchronization in C

Couchbase Lite 3.2.3 introduces peer-to-peer synchronization in C. Couchbase Lite C supports peer-to-peer synchronization over IP using the WebSocket protocol via URLEndpointListener, but does not support custom transports through MessageEndpointListener.

For more information about peer-to-peer synchronization in C, see:

* [Data Sync Peer-to-Peer](c/p2psync-websocket.md)
* [Passive Peer](c/p2psync-websocket-using-passive.md)
* [Active Peer](c/p2psync-websocket-using-active.md)

## [](#release-3-2-2-march-2025)Release 3.2.2 (March 2025)

> [!IMPORTANT]
> Deprecation Notice
> 
> From Couchbase Lite version 3.2.2, the current Logging API is deprecated and will be removed in a future release.
> 
> Use of the deprecated and new Logging API at the same time is not supported.
> 
> See the following links for information about migrating to the new Logging API:
> 
> * [Android](android/new-logging-api.md)
> * [C](c/new-logging-api.md)
> * [.NET](csharp/new-logging-api.md)
> * [Java](java/new-logging-api.md)
> * [Objective-C](objc/new-logging-api.md)
> * [Swift](swift/new-logging-api.md)

### [](#new-features-2)New Features

#### [](#new-logging-api)New Logging API

Couchbase Lite 3.2.2 introduces a new Logging API. The new Logging API has the following benefits:

* Log sinks are now thread safe, removing risk of inconsistent states during initialization.
* Simplified API and reduced implementation complexity.

For more information about migrating to the new Logging API, see:

* [Android - New Logging API](android/new-logging-api.md)
* [C - New Logging API](c/new-logging-api.md)
* [.NET - New Logging API](csharp/new-logging-api.md)
* [Java - New Logging API](java/new-logging-api.md)
* [Objective-C - New Logging API](objc/new-logging-api.md)
* [Swift - New Logging API](swift/new-logging-api.md)

#### [](#partial-index)Partial Index

Couchbase Lite 3.2.2 introduces support for Partial Index - Partial Value and Partial Full-Text Indexes. The Partial Index can create a smaller index, potentially improving index and query performance. You can use Partial Index to specify a `WHERE` clause in your index configuration. If a where clause is specified, the database will index a document only when the where clause condition is met.

For more information about Partial Index, see:

* [Android - Partial Index](android/indexing.md#partial-index)
* [C - Partial Index](c/indexing.md#partial-index)
* [.NET - Partial Index](csharp/indexing.md#partial-index)
* [Java - Partial Index](java/indexing.md#partial-index)
* [Objective-C - Partial Index](objc/indexing.md#partial-index)
* [Swift - Partial Index](swift/indexing.md#partial-index)

## [](#release-3-2-1-november-2024)Release 3.2.1 (November 2024)

### [](#new-features-3)New Features

#### [](#array-unnest-and-the-array-index)Array UNNEST and the Array Index

You can use UNNEST in queries to unpack arrays within a document into individual rows. This capability makes it possible to join them with their parent object in the query.

You can use UNNEST within the FROM clause. You can chain UNNEST to perform multi-level UNNEST.

You can also use a new type of index, the Array Index, to allow querying with UNNEST more efficiently.

For more information about Array UNNEST, see:

* [Android - Array UNNEST](android/query-n1ql-mobile.md#lbl-unnest)
* [C - Array UNNEST](c/query-n1ql-mobile.md#lbl-unnest)
* [.NET - Array UNNEST](csharp/query-n1ql-mobile.md#lbl-unnest)
* [Java - Array UNNEST](java/query-n1ql-mobile.md#lbl-unnest)
* [Objective-C - Array UNNEST](objc/query-n1ql-mobile.md#lbl-unnest)
* [Swift - Array UNNEST](swift/query-n1ql-mobile.md#lbl-unnest)

For more information about Array indexes, see:

* [Android - Array Indexing](android/indexing.md#array-indexing)
* [C - Array Indexing](c/indexing.md#array-indexing)
* [.NET - Array Indexing](csharp/indexing.md#array-indexing)
* [Java - Array Indexing](java/indexing.md#array-indexing)
* [Objective-C - Array Indexing](objc/indexing.md#array-indexing)
* [Swift - Array Indexing](swift/indexing.md#array-indexing)

## [](#release-3-2-0-august-2024)Release 3.2.0 (August 2024)

> [!IMPORTANT]
> Databases upgraded from 3.1.x to 3.2.x cannot be downgraded.

### [](#new-features-4)New Features

#### [](#vector-search)Vector Search

> [!IMPORTANT]
> Vector Search is available only for 64-bit architectures and Intel processors that support the Advanced Vector Extensions 2 (AVX2) instruction set. To verify whether your device supports the AVX2 instructions set, [follow these instructions.](https://www.intel.com/content/www/us/en/support/articles/000090473/processors/intel-core-processors.html)

Vector Search is now available on Couchbase Lite for all platforms. Vector Search is a sophisticated data retrieval technique that focuses on matching the contextual meanings of search queries and data entries, rather than simple text matching. Vectors are represented by arrays of numbers known as embeddings, which are generated by Large Language Models (LLMs) to represent objects such as text, images, and audio. You can use Vector Search to efficiently find similar items or content based on the similarity of their vector representations. This is useful for reducing the cost per query, performing semantic or similarity search, providing recommendations among others.

Read more at:

* [Vector Search - Android](android/vector-search.md)

  * [Installation Instructions](android/gs-install.md)
  * [Use Vector Search](android/working-with-vector-search.md)
* [Vector Search - C](c/vector-search.md)

  * [Downloads Page](#gs-downloads.adoc#vs-release-1-0-0-beta.3)
  * [Installation Instructions](c/gs-install.md)
  * [Use Vector Search](c/working-with-vector-search.md)
* [Vector Search - .Net](csharp/vector-search.md)

  * [Installation Instructions](csharp/gs-install.md)
  * [Use Vector Search](csharp/working-with-vector-search.md)
* [Vector Search - Java Desktop](java/vector-search.md)

  * [Installation Instructions](java/gs-install.md)
  * [Use Vector Search](java/working-with-vector-search.md)
* [Vector Search - Objective-C](objc/vector-search.md)

  * [Installation Instructions](objc/gs-install.md)
  * [Use Vector Search](objc/working-with-vector-search.md)
* [Vector Search - Swift](swift/vector-search.md)

  * [Installation Instructions](swift/gs-install.md)
  * [Use Vector Search](swift/working-with-vector-search.md)

#### [](#extended-datetime-functionality)Extended Date/Time Functionality

Six new DateTime functions have been added to Couchbase Lite N1QL:

* `STR_TO_TZ()`
* `MILLIS_TO_TZ()`
* `DATE_DIFF_STR()`
* `DATE_DIFF_MILLIS()`
* `DATE_ADD_STR()`
* `DATE_ADD_MILLIS()`

Read more at:

* [Android Date and Time Functions](android/query-n1ql-mobile.md#lbl-func-date)
* [C Date and Time Functions](c/query-n1ql-mobile.md#lbl-func-date)
* [.NET Date and Time Functions](csharp/query-n1ql-mobile.md#lbl-func-date)
* [Java Date and Time Functions](java/query-n1ql-mobile.md#lbl-func-date)
* [Objective-C Date and Time Functions](objc/query-n1ql-mobile.md#lbl-func-date)
* [Swift Date and Time Functions](swift/query-n1ql-mobile.md#lbl-func-date)

## [](#see-also)See also

[What’s new in previous version 3.1](#3.1@couchbase-lite:ROOT:cbl-whatsnew.adoc)

### [](#couchbase-lite-release-notes)Couchbase Lite Release Notes

[Android](android/releasenotes.md)| [C](c/releasenotes.md)| [.NET](csharp/releasenotes.md)| [Java](java/releasenotes.md)| [Objective-C](objc/releasenotes.md)| [Swift](swift/releasenotes.md)

### [](#vector-search-release-notes)Vector Search Release Notes

[Android](android/vs-releasenotes.md)| [C](c/vs-releasenotes.md)| [.NET](csharp/vs-releasenotes.md)| [Java](java/vs-releasenotes.md)| [Objective-C](objc/vs-releasenotes.md)| [Swift](swift/vs-releasenotes.md)

## [](#lbl-upgrade)Upgrading

[Android](android/upgrade.md)| [C](c/upgrade.md)| [.NET](csharp/upgrade.md)| [Java](java/upgrade.md)| [Objective-C](objc/upgrade.md)| [Swift](swift/upgrade.md)