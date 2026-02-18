---
title: SQL++ for Capella Analytics
description: Capella Analytics extends the grammar, statements, and capabilities
  of  SQL++ for Analytics used with the Analytics Service in Couchbase Server
  and Capella.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/1_intro.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/sqlpp/1_intro.html)

# SQL++ for Capella Analytics

> Capella Analytics extends the grammar, statements, and capabilities of SQL++ for Analytics used with the Analytics Service in Couchbase Server and Capella. This guide is a reference to the full syntax and semantics of the SQL++ query language that you use with Capella Analytics services. 

SQL++ for Capella Analytics is a Couchbase implementation, focused on parallel data analysis, of a SQL-for-JSON query language specification called SQL++.

SQL++ for Capella Analytics is similar to SQL. The differences between the languages are due to the differences in the data models that each language is designed to serve. SQL interacts with the flat, schematic world of relational databases, while SQL++ for Capella Analytics interacts with the nested, schema-less or schema-optional world of NoSQL systems like Capella Analytics. SQL++ for Capella Analytics is designed to work with the JSON data model.

Grammar-guided explanations, diagrams, and examples of the SQL++ for Capella Analytics language follow.

For an introduction to SQL++, on which SQL++ for Capella Analytics is based, see [SQL++ For SQL Users: A Tutorial](https://www.couchbase.com/analytics-data) by Don Chamberlin.

## [](#features)Features

This reference includes descriptions of features that extend SQL++ specifically for use with Capella Analytics. These features include:

* An expanded entity hierarchy: see [Entities in Capella Analytics Services](1a%5Fentities.md).
* New syntax for creating standalone collections: see [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md).
* New DML statements:

  * [COPY INTO a standalone collection](5%5Fdml%5Fcopy%5Fin.md)
  * [DELETE from a standalone collection](5%5Fdml%5Fdelete.md)
  * [INSERT INTO a standalone collection](5%5Fdml%5Finsert.md)
  * [UPSERT INTO a standalone collection](5%5Fdml%5Fupsert.md)
  * [COPY TO External Data Store Statements](5%5Fdml%5Fcopy%5Fto%5Fexternal.md)
  * [COPY TO Couchbase Data Service Statements](5%5Fdml%5Fcopy%5Fto%5Fkv.md)
* A new DDL/DML statement to create a standalone collection and populate it with the results of a query: see [CREATE COLLECTION AS](5%5Fdml%5Fcreate%5Fas.md).