---
title: Migrating from Relational Databases
description: Migration guidelines for relational database users. In this
  section, we use MySQL as an example relational database.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/migrate-mysql.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:install:migrate-mysql.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/migrate-mysql.html)

# Migrating from Relational Databases

> Migration guidelines for relational database users. In this section, we use MySQL as an example relational database. 

When migrating from MySQL to Couchbase Server, there are several things that you might want to think about, starting with the data model, data types, and feature set differences.

## [](#data-modelmapping-from-mysql-to-couchbase-server)Data Model — Mapping from MySQL to Couchbase Server

Data modeling for RDBMS has been a well-defined discipline for many years. Professionals, including novice users, have been practicing techniques such as logical to physical mapping and normalization / de-normalization. However, the old-school RDBMS data modeling techniques still play a meaningful role for those who are new to the NoSQL technology.

__Table 1\. Concept mapping between MySQL and Couchbase Server__
| MySQL        | Couchbase Server    |
| ------------ | ------------------- |
| Database     | Bucket              |
| Table        | Bucket(s)/Keyspaces |
| Row          | Document            |
| Column       | Field               |
| Fixed schema | Flexible schema     |

__Table 2\. Datatype mapping between MySQL and Couchbase Server__
| Data type      | MySQL            | Couchbase Server          |
| -------------- | ---------------- | ------------------------- |
| Case sensitive | Yes/No           | Yes                       |
| Numbers        | Yes              | Yes                       |
| String         | Yes              | Yes                       |
| Boolean        | Yes (as tinyint) | Yes                       |
| Date time      | Yes              | Yes (as a string in JSON) |
| Spatial data   | Yes              | Yes                       |
| MISSING        | No               | Yes                       |
| NULL           | Yes              | Yes                       |
| Object/Arrays  | No               | Yes                       |
| Blobs          | Yes              | Yes                       |

## [](#feature-set)Feature Set

Like MySQL, Couchbase Server offers a rich set of features and functionality far beyond those offered in simple key-value stores.

With Couchbase Server, you also get an expressive SQL-like query language and query engine called [SQL++](../n1ql/n1ql-language-reference/index.md), which is combined with a new powerful indexing mechanism — [Global Secondary Indexes](../learn/services-and-indexes/indexes/global-secondary-indexes.md).

__Table 3\. Feature differences between MySQL and Couchbase Server__
| Feature              | Key difference                                                                                                                                                                                                                                                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Keys/Indexes         | Primary keys on keys of (key, value) pair                                                                                                                                                                                                                                                                      |
| SQL statements       | The result is set in JSON instead of rows and columns. NEST, UNNEST Operations on datetime fields require datetime functions in SQL++. JSON-induced functions in SQL++: JSON, Object, and array functions. Type and comparison functions. JOIN, sub-query format differences. USING KEYS and ON KEYS functions |
| Explain and metadata | Variation in command and results (JSON).                                                                                                                                                                                                                                                                       |

## [](#etl-tools)ETL Tools

You might have a spectrum of relational, operational, and analytical data sources in your environment. You might also need more sophistication applied to a data movement situation, such as more than just simple extract-load. Various tools are available, but the most common use cases are best served by combining our [JDBC drivers](../connectors/odbc-jdbc-drivers.md) with our [Java SDK](../../../java-sdk/current/hello-world/start-using-sdk.md).