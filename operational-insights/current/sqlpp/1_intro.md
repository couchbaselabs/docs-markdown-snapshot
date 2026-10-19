---
title: About SQL++
description: Operational Insights extends the grammar, statements, and
  capabilities of  SQL++ for Analytics used with the Analytics Service in
  Couchbase Server and Capella.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/1_intro.adoc
  xref: xref:enterprise-analytics:sqlpp:1_intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/1_intro.html)

# About SQL++

> Operational Insights extends the grammar, statements, and capabilities of SQL++ for Analytics used with the Analytics Service in Couchbase Server and Capella. This guide is a reference to the full syntax and semantics of the SQL++ query language that you use with Operational Insights. 

SQL++ for Operational Insights is a Couchbase implementation, focused on parallel data analysis, of a SQL-for-JSON query language specification called SQL++.

SQL++ for Operational Insights is similar to SQL. The differences between the languages are due to the differences in the data models that each language is designed to serve. SQL interacts with the flat, schematic world of relational databases, while SQL++ for Operational Insights interacts with the nested, schema-less or schema-optional world of NoSQL systems like Operational Insights. SQL++ for Operational Insights is designed to work with the JSON data model.

Grammar-guided explanations, diagrams, and examples of the SQL++ for Operational Insights language follow.

## [](#features)Features

This reference includes descriptions of features that extend SQL++ specifically for use with Operational Insights. These features include:

* An expanded entity hierarchy: see [Entities](1a%5Fentities.md).
* New syntax for creating standalone collections: see [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md).
* New DML statements:

  * [COPY INTO a standalone collection](5%5Fdml%5Fcopy%5Fin.md)
  * [DELETE from a standalone collection](5%5Fdml%5Fdelete.md)
  * [INSERT INTO a standalone collection](5%5Fdml%5Finsert.md)
  * [UPSERT INTO a standalone collection](5%5Fdml%5Fupsert.md)
  * [COPY TO External Data Store Statements](5%5Fdml%5Fcopy%5Fto%5Fexternal.md)
  * [COPY TO Couchbase Data Service Statements](5%5Fdml%5Fcopy%5Fto%5Fkv.md)
* A new DDL/DML statement to create a standalone collection and populate it with the results of a query: see [CREATE COLLECTION AS](5%5Fdml%5Fcreate%5Fas.md).

## [](#statements)Statements

SQL++ for Operational Insights statements fall into the following groups:

* Queries: [SELECT Statements](3%5Fquery.md).
* Data definition: [DDL Statements](5%5Fddl.md).
* Data manipulation: [DML Statements](5%5Fdml.md).
* Access control: [RBAC Statements](5%5Fddl%5Frbac%5Fstatement.md).
* Query optimization:

  * `ANALYZE` collects and drops the samples that the cost-based optimizer uses. See [Collecting Samples](5b%5Fcbo.md#Collecting%5Fsamples).
  * `ADVISE` returns index recommendations for a query. See [Index Advisor](5c-index-advisor.md).
  * `SET` overrides system parameters for a single request. See [Performance Tuning](appendix%5F2%5Fparameters.md).