---
title: DML Statements
description: This section describes the SQL++ for Enterprise Analytics Data
  Manipulation Language (DML) statements you use to query and manipulate data in
  collections.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_dml.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:sqlpp:5_dml.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_dml.html)

# DML Statements

> This section describes the SQL++ for Enterprise Analytics Data Manipulation Language (DML) statements you use to query and manipulate data in collections. 

You use [SELECT Statements](3%5Fquery.md) to query your Enterprise Analytics collections. You use [DESCRIBE LINK Statements](5%5Fdml%5Fdescribe.md) to get information about remote and external links.

You use the following statements to populate and update standalone collections:

* [COPY INTO Statements](5%5Fdml%5Fcopy%5Fin.md)
* [INSERT INTO Statements](5%5Fdml%5Finsert.md)
* [UPSERT INTO Statements](5%5Fdml%5Fupsert.md)
* [DELETE Statements](5%5Fdml%5Fdelete.md)
* [CREATE COLLECTION AS Statements](5%5Fdml%5Fcreate%5Fas.md)

You use the following statement to write data out to an external store such as Amazon S3:

* [COPY TO External Data Store Statements](5%5Fdml%5Fcopy%5Fto%5Fexternal.md)

You use the following statement to write data out to a Couchbase data service:

* [COPY TO Couchbase Data Service Statements](5%5Fdml%5Fcopy%5Fto%5Fkv.md)

You use the following statement to delete all the data in a collection:

* [TRUNCATE Statements](5%5Fdml%5Ftruncate.md)