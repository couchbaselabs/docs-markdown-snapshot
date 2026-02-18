---
title: Migrating from SDK2 to SDK3 API
description: This is the first release of the Couchbase Scala SDK -- you will
  not have any code based upon older API versions.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cxx-sdk/1.0/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating from SDK2 to SDK3 API

> This is the first release of the Couchbase Scala SDK — you will not have any code based upon older API versions. 

Couchbase C++ SDK 1.0 implements the Couchbase SDK 3.6 API. 1.x is the first release of the Couchbase Scala SDK, there are no releases implementing older APIs.

## [](#mixing-code-from-other-jvm-platforms)Mixing Code from Other JVM Platforms

Migration will only be a concern if you are mixing code from different JVM SDKs in your application — specifically the [Java SDK](../../../java-sdk/current/hello-world/overview.md) — in which case you will need to be using a supported 3.x Java SDK. If you have programmed Couchbase client software against the Java 2.x SDK previously, then you may want to read the [Java migration guide](../../../java-sdk/current/project-docs/migrating-sdk-code-to-3.n.md).

## [](#legacy-mapreduce-views)Legacy MapReduce Views

Note, if you are looking for information about Couchbase’s legacy MapReduce Views Service, MapReduce Views are deprecated in Couchbase Server, and will eventually be removed. Information on using MapReduce Views with the SDK can still be accessed in our [documentation archive](https://docs-archive.couchbase.com/scala-sdk/1.2/howtos/view-queries-with-sdk.html).

Views are the only service which does not benefit from [Multi-Dimensional Scaling](../../../server/7.6/learn/services-and-indexes/services/services.md#services-and-multi-dimensional-scaling), and is rarely the best choice over, say, [our Query service](../howtos/sqlpp-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for your use case](../concept-docs/querying-your-data.md) for querying your data.