---
title: Statements
description: "Statements are the commands that make up a SQL++ query. They can
  be categorized into three main groups: data definition language, data control
  language, and data manipulation language."
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/statements.adoc
  xref: xref:server:n1ql:n1ql-language-reference/statements.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/statements.html)

# Statements

> Statements are the commands that make up a SQL++ query. They can be categorized into three main groups: data definition language, data control language, and data manipulation language. 

## [](#ddl)Data Definition Language

Data definition language (DDL) statements enable you to create and modify database objects, such as users, buckets, and indexes.

[ALTER BUCKET](alterbucket.md)  
[ALTER GROUP](altergroup.md)  
[ALTER INDEX](alterindex.md)  
[ALTER SEQUENCE](altersequence.md)  
[ALTER USER](alteruser.md)  
[ALTER VECTOR INDEX](altervectorindex.md)  
[BUILD INDEX](build-index.md)  
[CREATE BUCKET](createbucket.md)  
[CREATE COLLECTION](createcollection.md)  
[CREATE FUNCTION](createfunction.md)  
[CREATE GROUP](creategroup.md)  
[CREATE INDEX](createindex.md)  
[CREATE PRIMARY INDEX](createprimaryindex.md)  
[CREATE SEQUENCE](createsequence.md)  
[CREATE SCOPE](createscope.md)  
[CREATE USER](createuser.md)  
[CREATE VECTOR INDEX](createvectorindex.md)  
[DROP BUCKET](dropbucket.md)  
[DROP COLLECTION](dropcollection.md)  
[DROP FUNCTION](dropfunction.md)  
[DROP GROUP](dropgroup.md)  
[DROP INDEX](dropindex.md)  
[DROP PRIMARY INDEX](dropprimaryindex.md)  
[DROP SEQUENCE](dropsequence.md)  
[DROP SCOPE](dropscope.md)  
[DROP USER](dropuser.md)  
[DROP VECTOR INDEX](dropvectorindex.md)

## [](#dcl)Data Control Language

Data control language (DCL) statements enable you to control which users or groups have access to data, and what they're permitted to do with that data.

[GRANT](grant.md)  
[REVOKE](revoke.md)

## [](#dml)Data Manipulation Language

Data manipulation language (DML) statements enable you to create, read, update, and delete data. Some DML statements may be further categorized as data query language, transaction control language, or utility statements.

[DELETE](delete.md)  
[INSERT](insert.md)  
[MERGE](merge.md)  
[UPDATE](update.md)  
[UPSERT](upsert.md)

### [](#dql)Data Query Language

Data query language (DQL) statements enable you to read and filter data and manipulate the results.

[SELECT](selectintro.md)

### [](#tcl)Transaction Control Language

Transaction control language (TCL) statements enable you to work with Couchbase transactions.

[BEGIN TRANSACTION](begin-transaction.md)  
[COMMIT TRANSACTION](commit-transaction.md)  
[ROLLBACK TRANSACTION](rollback-transaction.md)  
[SAVEPOINT](savepoint.md)  
[SET TRANSACTION](set-transaction.md)

### [](#utility)Utility Statements

Utility statements do not manipulate data directly, but support other operations. For example, you can create and execute prepared statements, see query plans, get advice on query or index creation, and so on.

[ADVISE](advise.md)  
[EXECUTE](execute.md)  
[EXECUTE FUNCTION](execfunction.md)  
[EXPLAIN](explain.md)  
[EXPLAIN FUNCTION](explainfunction.md)  
[INFER](infer.md)  
[PREPARE](prepare.md)  
[UPDATE STATISTICS](updatestatistics.md)  
[USING AI](using-ai.md)