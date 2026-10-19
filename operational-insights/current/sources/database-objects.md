---
title: Data Model &amp; Hierarchy
description: This topic introduces the database objects that make up the data
  model hierarchy in Operational Insights.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sources/pages/database-objects.adoc
  xref: xref:enterprise-analytics:sources:database-objects.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sources/database-objects.html)

# Data Model &amp; Hierarchy

> This topic introduces the database objects that make up the data model hierarchy in Operational Insights. 

![An Operational Insights cluster containing 2 databases, each divided into scopes that contain collections. Diagram.](_images/database-objects.svg) 

Operational Insights organizes your data in a hierarchy: each database contains one or more scopes, and each scope contains collections and other database objects. To support your analytical queries and manage access to data sources, you add the following objects:

* [Database](#database)
* [Scopes](#scopes)
* [Collections](#collections)
* [Links](#links)
* [Synonyms](#synonyms)
* [User-Defined Functions](#userdefinedfunctions)

## [](#database)Database

A database is the top-level container for organizing related information in an Operational Insights cluster. When you create a cluster, Operational Insights automatically creates a database named `Default`. You can add more databases using the [UI](manage-databases.md) or a SQL++ [CREATE DATABASE statement](../sqlpp/5%5Fddl%5Fdatabase.md).

## [](#scopes)Scopes

Scopes are intermediary containers that exist within a database to group related objects like collections, indexes, and functions.

When you create a cluster, Operational Insights automatically creates a scope named `Default` in the database named `Default`. You can add more scopes as needed using the [UI](manage-scopes.md) or a SQL++ [CREATE SCOPE statement](../sqlpp/5%5Fddl%5Fscope.md).

You must make scope names unique within a database, but you can use the same scope name across different databases.

## [](#collections)Collections

Collections are containers that can contain metadata and data that you can query and manipulate. You can add a standalone collection using [UI](manage-collections.md) or a [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fstandalone.md) SQL++ statement.

You must make collection names unique within a scope but you can use the same collection name across different scopes, either in the same database or across different databases.

Operational Insights has 3 types of collections:

* **Remote collections** contain a shadow or mirror copy of data streamed from a remote data source. The remote data source can be a Kafka pipeline or a Couchbase database. A remote collection is associated with a [link](#links) that provides authentication and connection information for the remote data source. When the link is connected to the remote source, Operational Insights streams data from the remote source into the collection. This streaming means that the remote collection has a local replica of the data in the data source. When the link is disconnected, the collection retains the data as it was when the link disconnected. Queries on remote collections are efficient because of the local shadow copy of the streamed data.  
The remote collection also contains metadata about the data format of the remote source as well as optional data filters.  
You can use the Operational Insights [UI](manage-remote.md) or the SQL++ [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fremote.md) statement to add a remote collection.
* **External collections** let you query data stored in an S3 bucket. Like remote collections, they're associated with a [link](#links). Unlike remote collections, Operational Insights does not copy data from the external data source into the external collection. Instead, every query reads data from the external storage location. The external collection contains just the metadata necessary to read data from the S3 bucket. As a result, Operational Insights cannot index external collections.  
You can use the Operational Insights [UI](manage-external.md) or a [CREATE EXTERNAL COLLECTION](../sqlpp/5%5Fddl%5Fexternal.md) SQL++ statement to add an external collection.
* **Standalone collections** allow you to assemble and manipulate groups of documents on an as-needed basis. These are stored, manipulated, and managed locally. Standalone collections do not use links.  
You populate these collections with data by importing data files or by using SQL++ statements to [INSERT](../sqlpp/5%5Fdml%5Finsert.md), [COPY INTO](../sqlpp/5%5Fdml%5Fcopy%5Fin.md), and otherwise add and update documents in a purpose-built collection.  
You can use the Operational Insights [UI](manage-collections.md) or a [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fstandalone.md) SQL++ statement to add a standalone collection.

## [](#links)Links

A link is a metadata store for the authorization and authentication credentials that Operational Insights uses when connecting to a remote or external data source. You can associate multiple collections in different scopes across different databases, with a single link.

Links are categorized into 2 types:

* **Remote links** have connected and disconnected states. When connected, the link provides continuous, real-time updates to the data shadowed in its associated Operational Insights remote collections.  
You incur charges when you connect a remote link.
* **External links** contain the credentials Operational Insights needs to view an external storage location. These links do not have connected or disconnected states. Instead, each time you query an associated external collection, Operational Insights connects to the external data storage to read its data.

You use the Operational Insights UI to add links. See [Stream Data from Remote Sources](manage-remote.md) or [Set Up an External Data Source](manage-external.md).

## [](#synonyms)Synonyms

A synonym is an alternative name that you can use to refer to a database object, without changing the underlying object itself. You use SQL++ statements to create [synonyms](../sqlpp/5%5Fddl%5Fsynonym.md).

## [](#userdefinedfunctions)User-Defined Functions

User-defined functions have the same syntax as built-in functions, with brackets () to contain any arguments. When you have created a user-defined function, you can call it in any expression, just like a built-in function.

The name of the function is usually an unqualified identifier, such as func1 or `func-1`. In this case, the path to the function is determined by the current query context.

> [!NOTE]
> The name of a user-defined function is case-sensitive, unlike that of a built-in function. You must call the user-defined function using the same case that you used when you created it.

You use SQL++ statements to create [user-defined functions](../sqlpp/9%5Fudf.md).

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [About SQL++](../sqlpp/1%5Fintro.md)
* [Entities](../sqlpp/1a%5Fentities.md)