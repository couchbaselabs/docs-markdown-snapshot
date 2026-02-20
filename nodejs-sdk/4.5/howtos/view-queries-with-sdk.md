---
title: MapReduce Views
description: You can use MapReduce views to create queryable indexes in
  Couchbase Data Platform.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.5/modules/howtos/pages/view-queries-with-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.5@nodejs-sdk:howtos:view-queries-with-sdk.adoc[]
---

[View original HTML](/nodejs-sdk/4.5/howtos/view-queries-with-sdk.html)

# MapReduce Views

> You can use MapReduce views to create queryable indexes in Couchbase Data Platform. 

> [!CAUTION]
> Although still maintained and supported for legacy use, Views date from the earliest days of Couchbase Server development, and as such are rarely the best choice over, say, [our Query service](n1ql-queries-with-sdk.md) if you are starting a fresh application. See our discussion document on [the best service for you to use](../concept-docs/data-services.md).
> 
> Note, if you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](#7.6.6@server:learn:buckets-memory-and-storage/storage-engines.adoc#couchstore) bucket_.

The normal CRUD methods allow you to look up a document by its ID. A MapReduce (_view_ query) allows you to lookup one or more documents based on various criteria. MapReduce views are comprised of a _map_ function that is executed once per document (this is done incrementally, so this is not run each time you query the view) and an optional _reduce_ function that performs aggregation on the results of the _map_ function. The _map_ and _reduce_ functions are stored on the server and written in JavaScript.

MapReduce queries can be further customized during query time to allow only a subset (or range) of the data to be returned.

> [!TIP]
> See the [Incremental MapReduce Views](#7.1@server:learn:views/views-writing.adoc) and [Querying Data with Views](#7.1@server:learn:views/views-querying.adoc) sections of the general documentation to learn more about views and their architecture.

## [](#by-name-views)By Name Views

The following example is the definition of a `by_name` view in a _"beer"_ design document. This view checks whether a document is a beer and has a name. If it does, it emits the beer’s name into the index. This view allows beers to be queried for by name. For example, it’s now possible to ask the question "What beers start with A?"

```javascript
var result = bucket.viewQuery('beers', 'by_name', {
  range: { start: 'A' },
  limit: 10,
})
```

The following example is the definition of a `by_name` view in a _"landmarks"_ design document in the _"travel-sample"_ sample dataset. This view checks whether a document is a landmark and has a name. If it does, it emits the landmark’s name into the index. This view allows landmarks to be queried for by its _"name"_ field.

```javascript
var result = await bucket.viewQuery('landmarks', 'by_name', {
  key: 'landmark_10019',
})
```

A Spatial View can instead be queried with a `range` or _bounding box_. For example, let’s imagine we have stored landmarks with coordinates for their home city (eg. Paris, Vienna, Berlin and New York) under `geo`, and each city’s coordinates is represented as two attributes, `lon` and `lat`. The following spatial view map function could be used to find landmarks within Europe, as a _"by\_location"_ view in a _"spatial"_ design document:

```javascript
function (doc, meta) {
    if (doc.type && doc.type == 'landmark' && doc.geo) {
        emit([doc.geo.lon, doc.geo.lat], null);
    }
}
```