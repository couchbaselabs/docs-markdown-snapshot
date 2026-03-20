---
title: TRUNCATE Statements
description: This topic describes how you use <code>TRUNCATE</code> statements
  to delete all the data in a collection in Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_dml_truncate.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:sqlpp:5_dml_truncate.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_dml_truncate.html)

# TRUNCATE Statements

> This topic describes how you use `TRUNCATE` statements to delete all the data in a collection in Enterprise Analytics. 

The `TRUNCATE` statement is used to immediately remove all data from a collection in Enterprise Analytics. Upon execution, all associated data files are deleted from storage, and the space is instantly reclaimed.

This differs from the `DELETE` statement, which marks records for deletion and only reclaims space during a later compaction process.

`TRUNCATE` is supported only for standalone and remote collections and is not available for external collections or views.

When executed on a remote collection with a connected link, the link is temporarily disconnected, the `TRUNCATE` operation is performed, and the link is reconnected.

## [](#syntax)Syntax

**Truncate EBNF** 

```EBNF
Truncate ::=  "TRUNCATE" "ANALYTICS"? "COLLECTION" QualifiedName ("IF" "EXISTS")?
```

**Truncate Diagram** 

![TRUNCATE](_images/Truncate.png) 

The first `QualifiedName` resolves to a remote collection, a standalone collection or a synonym.

## [](#examples)Examples

This example deletes all the data in a standalone collection named `Orders`:

```SQL++
  TRUNCATE COLLECTION database_name.scope_name.Orders;
```