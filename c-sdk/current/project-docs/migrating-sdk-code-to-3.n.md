---
title: Migrating from SDK2 to SDK3 API
description: The 3.0 API breaks the existing 2.0 APIs in order to provide a
  number of improvements. Collections and Scopes are introduced.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:c-sdk:project-docs:migrating-sdk-code-to-3.n.adoc[]
---

[View original HTML](/c-sdk/current/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating from SDK2 to SDK3 API

> The 3.0 API breaks the existing 2.0 APIs in order to provide a number of improvements. Collections and Scopes are introduced. The Document class and structure has been completely removed from the API, and the returned value is now `Result`. Retry behaviour is more proactive, and lazy bootstrapping moves all error handling to a single place. Individual behavior changes across services are explained here. 

## [](#fundamentals)Fundamentals

Before this guide dives into the language-specific technical component of the migration, it is important to understand the high level changes first. As a migration guide, this document assumes you are familiar with the previous generation of the SDK and does not re-introduce SDK API 2 concepts. We recommend familiarizing yourself with the new SDK first by reading at least the [getting started guide](../hello-world/start-using-sdk.md), and browsing through the other chapters a little.

### [](#terminology)Terminology

The concept of a `Cluster` and a `Bucket` remain the same, but a fundamental new layer is introduced into the API: `Collections` and their `Scopes`. Collections are logical data containers inside a Couchbase bucket that let you group similar data just like a _Table_ does in a relational database — although documents inside a collection do not need to have the same structure. Scopes allow the grouping of collections into a namespace, which is very usfeul when you have multilpe tenants acessing the same bucket. Couchbase Server includes support for collections as a [developer preview](#6.5@server:developer-preview:preview-mode.adoc) in version 6.5, and as a first class concept of the programming model from [version 7.0.](../../../server/current/learn/data/scopes-and-collections.md)

Note that the SDKs include the feature from SDK 3.0, to allow easier migration.

In the previous SDK generation, particularly with the `KeyValue` API, the focus has been on the codified concept of a `Document`. Documents were read and written and had a certain structure, including the `id`/`key`, content, expiry (`ttl`), and so forth. While the server still operates on the logical concept of documents, we found that this model in practice didn’t work so well for client code in certain edge cases. As a result we have removed the `Document` class/structure completely from the API. The new API follows a clear scheme: each command takes required arguments explicitly, and an option block for all optional values. The returned value is always of type `Result`. This avoids method overloading bloat in certain languages, and has the added benefit of making it easy to grasp APIs evenly across services.

Since documents also fundamentally handled the serialization aspects of content, two new concepts are introduced: the `Serializer` and the `Transcoder`. Out of the box the SDKs ship with a JSON serializer which handles the encoding and decoding of JSON. You’ll find the serializer exposes the options for methods like SQL++ queries and KeyValue subdocument operations,.

The KV API extends the concept of the serializer to the `Transcoder`. Since you can also store non-JSON data inside a document, the `Transcoder` allows the writing of binary data as well. It handles the object/entity encoding and decoding, and if it happens to deal with JSON makes uses of the configured `Serializer` internally. See the _Serialization and Transcoding_ section below for details.

### [](#what-to-look-out-for)What to look out for

The SDKs are more proactive in retrying with certain errors and in certain situations, within the timeout budget given by the user — as an example, temporary failures or locked documents are now being retried by default — making it even easier to program against certain error cases. This behavior is customizable in a `RetryStrategy`, which can be overridden on a per operation basis for maximum flexibility if you need it.

Note, most of the bootstrap sequence is now lazy (happening behind the scenes). For example, opening a bucket is not raising an error anymore, but it will only show up once you perform an actual operation. The reason behind this is to spare the application developer the work of having to do error handling in more places than needed. A bucket can go down 2ms after you opened it, so you have to handle request failures anyway. By delaying the error into the operation result itself, there is only one place to do the error handling. There will still be situations why you want to check if the resource you are accessing is available before continuing the bootstrap; for this, we have the diagnostics and ping commands at each level which allow you to perform those checks eagerly.

## [](#next-steps)Next Steps

Information on the new API is to be found in the [libcouchbase API pages](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/index.html).

## [](#comparing-older-documentation)Comparing Older Documentation

You may want to visit documentation for older versions of the SDK, to help to understand application code that you are migrating. Versions that have reached end of life can be found in the [archive](https://docs-archive.couchbase.com/home/index.html). In the release notes pages of these older docs, you will also find links to the API reference for each no-longer-supported release.