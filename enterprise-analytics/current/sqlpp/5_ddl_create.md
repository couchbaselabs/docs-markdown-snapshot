---
title: CREATE Statements
description: This topic introduces how you use <code>CREATE</code> statements to
  create different Enterprise Analytics objects.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_ddl_create.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_create.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_create.html)

# CREATE Statements

> This topic introduces how you use `CREATE` statements to create different Enterprise Analytics objects. 

You can use `CREATE` statements to create the following Enterprise Analytics objects:

* [Databases](5%5Fddl%5Fdatabase.md)
* [Scopes](5%5Fddl%5Fscope.md)
* [Remote](5%5Fddl%5Fremote.md), [external](5%5Fddl%5Fexternal.md), and [standalone](5%5Fddl%5Fstandalone.md) collections
* [Synonyms](5%5Fddl%5Fsynonym.md)
* [Indexes](5%5Fddl%5Findex.md)
* [Functions](9%5Fudf.md)
* [Views and tabular views](5a%5Fviews.md)

To create links to remote or external data sources, you use the Enterprise Analytics UI. See [Stream Data from Remote Sources](../sources/manage-remote.md) or [Set Up an External Data Source](../sources/manage-external.md).

> [!NOTE]
> `CREATE` statements cannot execute while the cluster is in a scaling state. The evaluation of such DDL statements fails. You can reattempt the action after scaling is complete.

## [](#syntax)Syntax

**CreateStmnt EBNF** 

```EBNF
CreateStmnt ::= CreateDatabase
              | CreateScope
              | CreateCollection
              | CreateSynonym
              | CreateIndex
              | CreateFunction
              | CreateView
              | CreateTabularView
```

**CreateStmnt Diagram** 

![CreateDatabase | CreateScope | CreateCollection | CreateSynonym | CreateIndex | CreateFunction | CreateView | CreateTabularView](_images/CreateStmnt.png)