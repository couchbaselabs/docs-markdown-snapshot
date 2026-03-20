---
title: SQL++ for Enterprise Analytics
description: Enterprise Analytics extends the grammar, statements, and
  capabilities of  SQL++ for Analytics used with the Analytics Service in
  Couchbase Server and Capella.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/1_intro.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:sqlpp:1_intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/1_intro.html)

# SQL++ for Enterprise Analytics

> Enterprise Analytics extends the grammar, statements, and capabilities of SQL++ for Analytics used with the Analytics Service in Couchbase Server and Capella. This guide is a reference to the full syntax and semantics of the SQL++ query language that you use with Enterprise Analytics. 

SQL++ for Enterprise Analytics is a Couchbase implementation, focused on parallel data analysis, of a SQL-for-JSON query language specification called SQL++.

SQL++ for Enterprise Analytics is similar to SQL. The differences between the languages are due to the differences in the data models that each language is designed to serve. SQL interacts with the flat, schematic world of relational databases, while SQL++ for Enterprise Analytics interacts with the nested, schema-less or schema-optional world of NoSQL systems like Enterprise Analytics. SQL++ for Enterprise Analytics is designed to work with the JSON data model.

Grammar-guided explanations, diagrams, and examples of the SQL++ for Enterprise Analytics language follow.

For an introduction to SQL++, on which SQL++ for Enterprise Analytics is based, see [SQL++ For SQL Users: A Tutorial](https://www.couchbase.com/analytics-data) by Don Chamberlin.

## [](#features)Features

This reference includes descriptions of features that extend SQL++ specifically for use with Enterprise Analytics. These features include:

* An expanded entity hierarchy: see [Entities in Enterprise Analytics](1a%5Fentities.md).
* New syntax for creating standalone collections: see [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md).
* New DML statements:

  * [COPY INTO a standalone collection](5%5Fdml%5Fcopy%5Fin.md)
  * [DELETE from a standalone collection](5%5Fdml%5Fdelete.md)
  * [INSERT INTO a standalone collection](5%5Fdml%5Finsert.md)
  * [UPSERT INTO a standalone collection](5%5Fdml%5Fupsert.md)
  * [COPY TO External Data Store Statements](5%5Fdml%5Fcopy%5Fto%5Fexternal.md)
  * [COPY TO Couchbase Data Service Statements](5%5Fdml%5Fcopy%5Fto%5Fkv.md)
* A new DDL/DML statement to create a standalone collection and populate it with the results of a query: see [CREATE COLLECTION AS](5%5Fdml%5Fcreate%5Fas.md).