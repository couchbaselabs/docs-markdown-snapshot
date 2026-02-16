[View original HTML](/nodejs-sdk/current/howtos/view-queries-with-sdk.html)

> You can use MapReduce views to create queryable indexes in Couchbase Data Platform. 

|  | Views is deprecated from Couchbase Server 7.0, and will eventually move to unsupported status. MapReduce Views is not available in Capella Operational, only in self-managed Couchbase Server. Use our [Query Service](n1ql-queries-with-sdk.md) if you are starting a fresh application, or see our discussion document on [the best service for you to use](../concept-docs/data-services.md). We will maintain support for Views in the SDKs for so long as it can be used with a supported version of Couchbase Server. Note, if you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](#8.0.0@server:learn:buckets-memory-and-storage/storage-engines.adoc#couchstore) bucket_. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The normal CRUD methods allow you to look up a document by its ID. A MapReduce (_view_ query) allows you to lookup one or more documents based on various criteria. MapReduce views are comprised of a _map_ function that is executed once per document (this is done incrementally, so this is not run each time you query the view) and an optional _reduce_ function that performs aggregation on the results of the _map_ function. The _map_ and _reduce_ functions are stored on the server and written in JavaScript.

MapReduce queries can be further customized during query time to allow only a subset (or range) of the data to be returned.

|  | See the [Incremental MapReduce Views](../../../server/current/learn/views/views-writing.md) and [Querying Data with Views](#7.1@server:learn:views/views-querying.adoc) sections of the general documentation to learn more about views and their architecture. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

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

A Spatial View can instead be queried with a `range` or _bounding box_. For example, let’s imagine we have stored landmarks with coordinates for their home city (eg. Paris, Vienna, Berlin, and New York) under `geo`, and each city’s coordinates is represented as two attributes, `lon` and `lat`. The following spatial view map function could be used to find landmarks within Europe, as a _"by\_location"_ view in a _"spatial"_ design document:

```javascript
function (doc, meta) {
    if (doc.type && doc.type == 'landmark' && doc.geo) {
        emit([doc.geo.lon, doc.geo.lat], null);
    }
}
```