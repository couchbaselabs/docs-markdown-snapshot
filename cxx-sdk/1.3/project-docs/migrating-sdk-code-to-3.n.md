---
title: Migrating from SDK2 to SDK3 API
description: This is the first major release of the Couchbase C&#43;&#43; SDK --
  you will not have any code based upon older API versions.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
  xref: xref:1.3@cxx-sdk:project-docs:migrating-sdk-code-to-3.n.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.3/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating from SDK2 to SDK3 API

> This is the first major release of the Couchbase C++ SDK — you will not have any code based upon older API versions. 

Couchbase C++ SDK 1.3 implements the Couchbase SDK 3.9 API. 1.x is the first release of the Couchbase C++ SDK, there are no releases implementing older APIs.

## [](#legacy-mapreduce-views)Legacy MapReduce Views

Note, if you are looking for information about Couchbase's legacy MapReduce Views Service, MapReduce Views has been deprecated since Couchbase Server 7.0, and is unsupported in the current C++ SDK.

Use the SQL++ Query Service, which benefits from [Multi-Dimensional Scaling](../../../server/current/learn/services-and-indexes/services/services.md#services-and-multi-dimensional-scaling). See our discussion document on [the best service for your use case](../concept-docs/querying-your-data.md) for querying your data.