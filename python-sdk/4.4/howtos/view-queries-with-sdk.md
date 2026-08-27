---
title: MapReduce Views
description: You can use MapReduce views to create queryable indexes in
  Couchbase Data Platform.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/howtos/pages/view-queries-with-sdk.adoc
  xref: xref:4.4@python-sdk:howtos:view-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.4/howtos/view-queries-with-sdk.html)

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

## [](#querying-views)Querying Views

Once you have a view defined, it can be queried from the Python SDK by using the `view_query` method on a `Bucket` instance.

The following example is the definition of a `by_country` view in a _landmarks-by-country_ design document. This view checks whether a document is a landmark and has a country. If it does, it emits the landmark's country into the index. This view allows landmarks to be queried for by country. For example, it's now possible to ask the question "What countries start with U?"

```python
result = bucket.view_query("landmarks-by-country",
                           "by_country",
                           ViewOptions(startkey="U",
                                       limit=10,
                                       namespace=DesignDocumentNamespace.DEVELOPMENT,
                                       scan_consistency=ViewScanConsistency.REQUEST_PLUS))
```

The following example is the definition of a `by_name` view in a _landmarks-by-name_ design document in the _travel-sample_ sample dataset. This view checks whether a document is a landmark and has a name. If it does, it emits the landmark's name into the index. This view allows landmarks to be queried for by its _name_ field.

```python
result = bucket.view_query("landmarks-by-name",
                           "by_name",
                           ViewOptions(key="Circle Bar",
                                       namespace=DesignDocumentNamespace.PRODUCTION))
```

Once a view result is obtained then it can be iterated over and the ID, keys and values extracted.

```python
for row in result.rows():
    print("Landmark named {} has documentID: {}".format(row.key, row.id))
```