---
title: MapReduce Views
description: You can use MapReduce views to create queryable indexes in
  Couchbase Data Platform.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.5/modules/howtos/pages/view-queries-with-sdk.adoc
  xref: xref:php-sdk:howtos:view-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/howtos/view-queries-with-sdk.html)

# MapReduce Views

> You can use MapReduce views to create queryable indexes in Couchbase Data Platform. 

> [!CAUTION]
> Views is deprecated from Couchbase Server 7.0, and will eventually move to unsupported status. MapReduce Views is not available in Capella Operational, only in self-managed Couchbase Server.
> 
> Use our [Query Service](n1ql-queries-with-sdk.md) if you are starting a fresh application, or see our discussion document on [the best service for you to use](../concept-docs/data-services.md). We will maintain support for Views in the SDKs for so long as it can be used with a supported version of Couchbase Server.
> 
> Note, if you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](#8.0.1@server:learn:buckets-memory-and-storage/storage-engines.adoc#couchstore) bucket_.

The normal CRUD methods allow you to look up a document by its ID. A MapReduce (_view_ query) allows you to lookup one or more documents based on various criteria. MapReduce views are comprised of a _map_ function that is executed once per document (this is done incrementally, so this is not run each time you query the view) and an optional _reduce_ function that performs aggregation on the results of the _map_ function. The _map_ and _reduce_ functions are stored on the server and written in JavaScript.

MapReduce queries can be further customized during query time to allow only a subset (or range) of the data to be returned.

> [!TIP]
> See the [Incremental MapReduce Views](../../../server/current/learn/views/views-writing.md) and [Querying Data with Views](../../../server/current/learn/views/views-querying.md) sections of the general documentation to learn more about views and their architecture.

You can find further information [in the API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-ViewResult.html).