---
title: Views Reference
description: Couchbase views enable indexing and querying of data.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/views/views-intro.adoc
  xref: xref:7.2@server:learn:views/views-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/learn/views/views-intro.html)

# Views Reference

> Couchbase views enable indexing and querying of data. 

> [!NOTE]
> Views are deprecated in Couchbase Server 7.0+. Views support in Couchbase Server will be removed in a future release only when the core functionality of the View engine is covered by other services. Views will not run on the newer [Magma storage engine](../buckets-memory-and-storage/storage-engines.md).

A view creates an index on the data according to the defined format and structure. The view consists of specific fields and information extracted from the objects in Couchbase.

Views are eventually consistent compared to the underlying stored documents. Documents are included in views when the document data is persisted to disk. Documents with expiry times are removed from indexes when the expiration pager operates to remove the document from the database.

Views are used for a number of reasons, including:

* Indexing and querying data from stored objects
* Producing lists of data on specific object types
* Producing tables and lists of information based on your stored data
* Extracting or filtering information from the database
* Calculating, summarizing or reducing the information on a collection of stored data

Multiple views can be created which provides multiple indexes and routes into the stored data. By exposing specific fields from the stored information, views enable the following:

* Creating and querying stored data
* Performing queries and selection on the data
* Paginating through the view output

The View Builder provides an interface for creating views within the web console. Views can be accessed by using a Couchbase client library to retrieve matching records.

> [!NOTE]
> In Couchbase Server 6.0+, Spatial Views are no longer supported. See the 5.5 documentation, [Writing Spatial Views](https://docs-archive.couchbase.com/server/5.5/understanding-couchbase/views/sv-writing-views.html).