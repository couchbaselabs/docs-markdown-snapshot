---
title: Access and Organize Data in Enterprise Analytics
description: This topic introduces the database objects that you use to view and
  organize data in Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/database-objects.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/sources/database-objects.html)

# Access and Organize Data in Enterprise Analytics

> This topic introduces the database objects that you use to view and organize data in Enterprise Analytics. 

## [](#sources-of-data)Sources of Data

Data sources include:

* Remote Couchbase operational databases, which are typically subject to rapid, ongoing modification. Enterprise Analytics connects to Couchbase Server and Couchbase Capella operational clusters.
* Kafka distributed streaming platform to stream data from other data sources such as databases.
* External data stores, logs, and archives to support analyses of historical data. Enterprise Analytics can query data residing in supported [object storage](../install/supported-platform.md#supported-object-storage-solutions). This data remains at the source and is not copied into Enterprise Analytics collections. Supported formats are JSON, CSV, TSV, Avro and Parquet.
* Data Lakes such as `delta lake`, residing in S3 buckets.

## [](#database-objects)Database Objects

To support your analytical queries and manage access to data sources, you add the following objects:

* [Indexes](#indexes)
* [Views](#views)
* [User Defined Functions (UDFs)](#userdefinedfunctions)
* [Scopes](#scopes)
* [Collections](#collections)
* [Links](#links)

![Diagram](_images/diag-9b62d13f16a436b0010ace32e9ad32fb64e026f3.svg) 

### [](#indexes)Indexes

Indexes are used by certain services, such as Query, Analytics, and Search, as targets for search-routines. Each index makes a predefined subset of data available for the search. Indexes, when well-designed, provide significant enhancements to the performance of search-operations.

### [](#views)Views

Views are functions written in JavaScript that can serve several purposes in your application. You can use them to:

* find all the documents in your database
* create a copy of data in a document and present it in a specific order
* create an index to efficiently find documents by a particular value or by a particular structure in the document
* represent relationships between documents
* perform calculations on data contained in documents.

### [](#userdefinedfunctions)User Defined Functions (UDFs)

User-defined functions have the same syntax as built-in functions, with brackets () to contain any arguments. When you have created a user-defined function, you can call it in any expression, just like a built-in function.

The name of the function is usually an unqualified identifier, such as func1 or `func-1`. In this case, the path to the function is determined by the current query context.

> [!NOTE]
> The name of a user-defined function is case-sensitive, unlike that of a built-in function. You must call the user-defined function using the same case that you used when you created it.

### [](#scopes)Scopes

Scopes are intermediary containers that exist within a database to group related objects like collections, indexes, and functions.

When you create a cluster, Enterprise Analytics automatically creates a scope named `Default` in the database named `Default`. You can add more scopes as needed using the [UI](manage-scopes.md) or a SQL++ [CREATE SCOPE statement](../sqlpp/5%5Fddl%5Fscope.md).

You must make scope names unique within a database, but you can use the same scope name across different databases.

### [](#collections)Collections

Collections are containers that can contain metadata and data that you can query and manipulate. You can add a standalone collection using [UI](manage-collections.md) or a [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fstandalone.md) SQL++ statement.

You must make collection names unique within a scope but you can use the same collection name across different scopes, either in the same database or across different databases.

Enterprise Analytics has 3 types of collections:

* **Remote collections** contain a shadow or mirror copy of data streamed from a remote data source. The remote data source can be a Kafka pipeline or a Couchbase database. A remote collection is associated with a [link](#links) that provides authentication and connection information for the remote data source. When the link is connected to the remote source, Enterprise Analytics streams data from the remote source into the collection. This streaming means that the remote collection has a local replica of the data in the data source. When the link is disconnected, the collection retains the data as it was when the link disconnected. Queries on remote collections are efficient because of the local shadow copy of the streamed data.  
The remote collection also contains metadata about the data format of the remote source as well as optional data filters.  
You can use the Enterprise Analytics [UI](manage-remote.md) or the SQL++ [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fremote.md) statement to add a remote collection.
* **External collections** let you query data stored in an S3 bucket. Like remote collections, they’re associated with a [link](#links). Unlike remote collections, Enterprise Analytics does not copy data from the external data source into the external collection. Instead, every query reads data from the external storage location. The external collection contains just the metadata necessary to read data from the S3 bucket. As a result, Enterprise Analytics cannot index external collections.  
You can use the Enterprise Analytics [UI](manage-external.md) or a [CREATE EXTERNAL COLLECTION](../sqlpp/5%5Fddl%5Fexternal.md) SQL++ statement to add an external collection.
* **Standalone collections** allow you to assemble and manipulate groups of documents on an as-needed basis. These are stored, manipulated, and managed locally. Standalone collections do not use links.  
You populate these collections with data by importing data files or by using SQL++ statements to [INSERT](../sqlpp/5%5Fdml%5Finsert.md), [COPY INTO](../sqlpp/5%5Fdml%5Fcopy%5Fin.md), and otherwise add and update documents in a purpose-built collection.  
You can use the Enterprise Analytics [UI](manage-collections.md) or a [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fstandalone.md) SQL++ statement to add a standalone collection.

### [](#links)Links

A link is a metadata store for the authorization and authentication credentials that Enterprise Analytics uses when connecting to a remote or external data source. You can associate multiple collections in different scopes across different databases, with a single link.

Links are categorized into 2 types:

* **Remote links** have connected and disconnected states. When connected, the link provides continuous, real-time updates to the data shadowed in its associated Enterprise Analytics remote collections.  
You incur charges when you connect a remote link.
* **External links** contain the credentials Enterprise Analytics needs to view an external storage location. These links do not have connected or disconnected states. Instead, each time you query an associated external collection, Enterprise Analytics connects to the external data storage to read its data.

You use the Enterprise Analytics UI to add links. See [Stream Data from Remote Sources](manage-remote.md) or [Set Up an External Data Source](manage-external.md).

### [](#other-objects)Other Objects

At the same hierarchical level as collections—​within a database and scope—​you create views and tabular views, synonyms, and user-defined indexes and functions.

* To create views and tabular views, you can use the Enterprise Analytics [CREATE VIEW](../sqlpp/5a%5Fviews.md) SQL++ statement.
* You use SQL++ statements to create [synonyms](../sqlpp/5%5Fddl%5Fsynonym.md) and [user-defined functions](../sqlpp/9%5Fudf.md).
* You also create indexes on individual remote and standalone collections with SQL++ statements. See [Indexes](../sqlpp/7%5Fusing%5Findex.md).

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [SQL++ for Enterprise Analytics](../sqlpp/1%5Fintro.md)