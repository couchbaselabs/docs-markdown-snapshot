---
title: Access and Organize Data in Capella Analytics Services
description: This topic introduces the database objects that you use to access
  and organize data in Capella Analytics.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/database-objects.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:sources:database-objects.adoc[]
---

[View original HTML](/analytics/sources/database-objects.html)

# Access and Organize Data in Capella Analytics Services

> This topic introduces the database objects that you use to access and organize data in Capella Analytics. 

## [](#sources-of-data)Sources of Data

All of the data that you use Capella Analytics to query originates from some other source. Data sources include:

* Remote operational databases, which are typically subject to rapid, ongoing modification. Capella Analytics connects to Couchbase Capella operational and Couchbase Server databases.
* Kafka distributed streaming platform to stream data from other data sources such as databases.
* External data stores, logs, and archives to support analyses of historical data. Capella Analytics can query data stored in [Amazon S3](external-s3.md) and [GCP](external-gcs.md). This data remains with the cloud provider. ​Capella Analytics does not copy it into a collection. Supported formats are JSON, CSV, TSV, Parquet, or Avro files.
* Data Lakes such as `delta`, residing in S3 buckets, can be queried.

## [](#database-objects)Database Objects

To support your analytical queries and manage access to data sources, you add the following objects:

* [Clusters](#clusters)
* [Databases](#databases)
* [Scopes](#scopes)
* [Collections](#collections)

![Diagram](_images/diag-3ee08c76d47a3ce16ffcc80ace7ae51e8363e580.svg) 

You also create [links](#links), which store the credentials for accessing data sources outside of Capella Analytics.

### [](#clusters)Clusters

A Capella Analytics cluster is an analytical database set in a cloud environment. It can ingest large volumes of data from a Couchbase database, or other data sources, enabling it to run complex queries.

Within a Capella organization, set up [projects](../admin/prepare-project.md#projects-and-clusters) and add 1 or more Capella Analytics clusters. Add clusters to a project as needed using the [UI](../admin/prepare-project.md#cluster).

When you create a cluster, you can choose your compute and node configuration options.

### [](#databases)Databases

In a Capella Analytics cluster, a database is the top-level container for organizing related information.

When you create a cluster, Capella Analytics automatically creates a database named `Default`. You can add more databases as needed using the [UI](manage-databases.md) or a SQL++ [CREATE DATABASE statement](../sqlpp/5%5Fddl%5Fdatabase.md).

### [](#scopes)Scopes

Scopes are intermediary containers that exist within a database to group related objects like collections, indexes, links, and functions.

When you create a cluster, Capella Analytics automatically creates a scope named `Default` in the database named `Default`.

You can add more scopes as needed using the [UI](manage-scopes.md) or a SQL++ [CREATE SCOPE statement](../sqlpp/5%5Fddl%5Fscope.md).

You must make scope names unique within a database, but you can use the same scope name across different databases.

### [](#collections)Collections

Collections are containers that can contain metadata and data that you can query and manipulate.

You must make collection names unique within a scope. Collections with the same name can exist in different scopes, either in the same database or across different databases.

Capella Analytics has three types of collections:

* **Remote collections** contain a shadow or mirror copy of data streamed from a remote data source. The remote data source can be a Kafka pipeline or a Couchbase database. A remote collection is associated with a [link](#links) that provides authentication and connection information for the remote data source. When the link is connected to the remote source, Capella Analytics streams data from the remote source into the collection. This streaming means that the remote collection has a local replica of the data in the data source. When the link is disconnected, the collection retains the data as it was when the link disconnected. Queries on remote collections are efficient because of the local shadow copy of the streamed data.  
The remote collection also contains metadata about the data format of the remote source as well as optional data filters.  
You can use the Capella Analytics [UI](manage-remote.md) or the SQL++ [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fremote.md) statement to add a remote collection.
* **External collections** let you query data stored in an S3 bucket. Like remote collections, they are associated with a [link](#links). Unlike remote collections, Capella Analytics does not copy data from the external data source into the external collection. Instead, every query reads data from the external storage location. The external collection contains just the metadata necessary to read data from the S3 bucket. As a result, Capella Analytics cannot index external collections.  
You can use the Capella Analytics [UI](manage-external.md) or a [CREATE EXTERNAL COLLECTION](../sqlpp/5%5Fddl%5Fexternal.md) SQL++ statement to add an external collection.
* **Standalone collections** allow you to assemble and manipulate groups of documents on an as-needed basis. These are stored, manipulated, and managed locally. Standalone collections do not use links.  
You populate these collections with data by importing data files or by using SQL++ statements to [INSERT](../sqlpp/5%5Fdml%5Finsert.md), [COPY INTO](../sqlpp/5%5Fdml%5Fcopy%5Fin.md), and otherwise add and update documents in a purpose-built collection.  
You can use the Capella Analytics [UI](#sources:manage-Capella Analytics.adoc) or a [CREATE COLLECTION](../sqlpp/5%5Fddl%5Fstandalone.md) SQL++ statement to add a standalone collection.

### [](#links)Links

A link is a metadata store for the authorization and authentication credentials that Capella Analytics uses when connecting to a remote or external data source. Links exist outside of the database > scope > collection hierarchy in a Capella Analytics cluster. You can associate multiple collections in different scopes with a single link.

There are two types of links:

* **Remote links** have connected and disconnected states. When connected, the link provides continuous, real-time updates to the data shadowed in its associated Capella Analytics remote collections.  
You incur charges when you connect a remote link.
* **External links** contain the credentials Capella Analytics needs to access an external storage location. These links do not have connected or disconnected states. Instead, each time you query an associated external collection, Capella Analytics connects to the external data storage to read its data.

You use the Capella Analytics UI to add links. See [Stream Data from Remote Sources](manage-remote.md) or [Set Up an External Data Source](manage-external.md).

### [](#other-objects)Other Objects

At the same hierarchical level as collections—​within a database and scope—​you create views and tabular views, synonyms, and user-defined indexes and functions.

* To create views and tabular views, you can use the Capella Analytics [UI](../query/views-tavs.md) or a [CREATE VIEW](../sqlpp/5a%5Fviews.md) SQL++ statement.
* You use SQL++ statements to create [synonyms](../sqlpp/5%5Fddl%5Fsynonym.md) and [user-defined functions](../sqlpp/9%5Fudf.md).
* You also create indexes on individual remote and standalone collections with SQL++ statements. See [Indexes](../sqlpp/7%5Fusing%5Findex.md).

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [SQL++ for Capella Analytics](../sqlpp/1%5Fintro.md)