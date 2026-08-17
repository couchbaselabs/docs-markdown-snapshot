---
title: MapReduce Views
description: Our legacy MapReduce Views Service is best replaced by the scalable
  Query Service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.8/modules/howtos/pages/view-queries-with-sdk.adoc
  xref: xref:3.8@java-sdk:howtos:view-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.8/howtos/view-queries-with-sdk.html)

# MapReduce Views

> Our legacy MapReduce Views Service is best replaced by the scalable Query Service. 

[MapReduce Views](../../../server/7.6/learn/views/views-intro.md) date from the earliest days of Couchbase and although still maintained and supported for legacy use, they are deprecated in Couchbase Server, and will eventually be removed.

Views are the only service which does not benefit from [Multi-Dimensional Scaling](../../../server/7.6/learn/services-and-indexes/services/services.md#services-and-multi-dimensional-scaling), and is rarely the best choice over, say, [our Query service](sqlpp-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for you to use](../concept-docs/querying-your-data.md).

> [!CAUTION]
> If you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](../../../server/7.6/learn/buckets-memory-and-storage/storage-engines.md#couchstore) bucket_.

We will maintain support for Views in the SDKs for so long as it can be used with a supported version of Couchbase Server.

Information on using MapReduce Views with the SDK can still be accessed in our [documentation archive](https://docs-archive.couchbase.com/java-sdk/3.1/howtos/view-queries-with-sdk.html).