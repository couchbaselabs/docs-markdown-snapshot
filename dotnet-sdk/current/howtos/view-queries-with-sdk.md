---
title: MapReduce Views
description: You can use MapReduce views to create queryable indexes in
  Couchbase Data Platform.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.9/modules/howtos/pages/view-queries-with-sdk.adoc
  xref: xref:dotnet-sdk:howtos:view-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/howtos/view-queries-with-sdk.html)

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

## [](#by-name-views)By Name Views

The following example is the definition of a `by_name` view in a _"beer"_ design document. This view checks whether a document is a beer and has a name. If it does, it emits the beer's name into the index. This view allows beers to be queried for by name. For example, it's now possible to ask the question "What beers start with A?"

```csharp
var result = await bucket.ViewQueryAsync("beers", "by_name", options => {
    options.WithStartKey("A");
    options.WithLimit(10);
});
```

The following example is the definition of a `by_name` view in a _"landmarks"_ design document in the _"travel-sample"_ sample dataset. This view checks whether a document is a landmark and has a name. If it does, it emits the landmark's name into the index. This view allows landmarks to be queried for by its _"name"_ field.

```csharp
var result = await bucket.ViewQueryAsync("landmarks", "by_name", options => {
    options.WithKey("<landmark-name>");
});
```

## [](#querying-views-through-the-net-sdk)Querying Views through the .NET SDK

Once you have a view defined, it can be queried from the .NET SDK by using the `ViewQuery` method on a Bucket instance.

Here is an example:

```csharp
var result = await bucket.ViewQueryAsync<Type>("design-doc", "view-name", options =>
{
	options.WithLimit(10);
});

foreach (var row in result.Rows)
{
	var id = row.Id;
	var key = row.Key<string[]>();
	var value = row.Value<Type>();
}
```