---
title: MapReduce Views
description: Our legacy MapReduce Views Service is best replaced by the scalable
  Query Service.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/howtos/pages/view-queries-with-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.11@go-sdk:howtos:view-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.11/howtos/view-queries-with-sdk.html)

# MapReduce Views

> Our legacy MapReduce Views Service is best replaced by the scalable Query Service. 

[MapReduce Views](../../../server/current/learn/views/views-intro.md) date from the earliest days of Couchbase and although still maintained and supported for legacy use, they are deprecated in Couchbase Server, and will eventually be removed.

Views are the only service which does not benefit from [Multi-Dimensional Scaling](../../../server/current/learn/services-and-indexes/services/services.md#services-and-multi-dimensional-scaling), and is rarely the best choice over, say, [our Query service](n1ql-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for you to use](../concept-docs/data-services.md).

> [!CAUTION]
> If you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](../../../server/current/learn/buckets-memory-and-storage/storage-engines.md#couchstore) bucket_.

We will maintain support for Views in the SDKs for so long as it can be used with a supported version of Couchbase Server.

Information on using MapReduce Views with the SDK can still be accessed in our [documentation archive](https://docs-archive.couchbase.com/go-sdk/2.2/howtos/view-queries-with-sdk.html).