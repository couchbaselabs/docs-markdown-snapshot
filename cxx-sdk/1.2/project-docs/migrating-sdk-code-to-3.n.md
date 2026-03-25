---
title: Migrating from SDK2 to SDK3 API
description: This is the first major release of the Couchbase C&#43;&#43; SDK --
  you will not have any code based upon older API versions.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.2/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:1.2@cxx-sdk:project-docs:migrating-sdk-code-to-3.n.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.2/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating from SDK2 to SDK3 API

> This is the first major release of the Couchbase C++ SDK — you will not have any code based upon older API versions. 

Couchbase C++ SDK 1.2 implements the Couchbase SDK 3.8 API. 1.x is the first release of the Couchbase C++ SDK, there are no releases implementing older APIs.

## [](#legacy-mapreduce-views)Legacy MapReduce Views

Note, if you are looking for information about Couchbase’s legacy MapReduce Views Service, MapReduce Views are deprecated in Couchbase Server, and will eventually be removed. Information on using MapReduce Views with the SDK can still be accessed in our [documentation archive](https://docs-archive.couchbase.com/scala-sdk/1.2/howtos/view-queries-with-sdk.html).

Views are the only service which does not benefit from [Multi-Dimensional Scaling](../../../server/current/learn/services-and-indexes/services/services.md#services-and-multi-dimensional-scaling), and is rarely the best choice over, say, [our Query service](../howtos/sqlpp-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for your use case](../concept-docs/querying-your-data.md) for querying your data.