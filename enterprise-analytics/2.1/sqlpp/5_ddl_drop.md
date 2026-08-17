---
title: DROP Statements
description: This topic describes how you use <code>DROP</code> statements to
  delete Enterprise Analytics objects.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_drop.adoc
  xref: xref:2.1@enterprise-analytics:sqlpp:5_ddl_drop.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/5_ddl_drop.html)

# DROP Statements

> This topic describes how you use `DROP` statements to delete Enterprise Analytics objects. 

A `DROP` statement is the inverse of a `CREATE` statement.

> [!NOTE]
> `DROP` statements cannot execute while the cluster is in a scaling state. The evaluation of such DDL statements fails. You can reattempt the action after scaling is complete.

## [](#syntax)Syntax

**DropStmnt EBNF** 

```EBNF
DropStmnt ::= DropDatabase
            | DropScope
            | DropCollection
            | DropSynonym
            | DropIndex
            | DropFunction
            | DropView
```

See [Drop Function](9%5Fudf.md#dropfunction) and [Drop View](5a%5Fviews.md#dropview) for information about dropping functions and views. To drop links you use the UI. See [Remove Link](../sources/delete-entity.md#remove-link).

**DropStmnt Diagram** 

![DropDatabase | DropScope | DropCollection | DropSynonym | DropIndex | DropFunction | DropView](_images/DropStmnt.png) 

### [](#drop-database)DROP Database

When you drop a database, all of the scopes and other database\_object entities in that database are also dropped.

You cannot drop a database if any other databases exist that use entities belonging to that database.

**DropDatabase Diagram** 

![DROP](_images/DropDatabase.png) 

DropDatabase

### [](#drop-scope)DROP Scope

When you drop a scope, the system also drops any user-defined functions in that scope. However, you cannot drop a scope if there are any user-defined functions or views in **other scopes** that depend on user-defined functions or collections or views within the scope you attempt to drop.

**Show DropScope Diagram** 

!["DROP" "SCOPE" DatabaseAndScopeName ("IF" "EXISTS")?](_images/DropScope.png) 

DropScope

### [](#drop-collection)DROP Collection

You cannot drop a collection if a dependency such as a user-defined function or view in the same or a different scope uses it.

**Show DropCollection Diagram** 

!["DROP" "COLLECTION" QualifiedName ("IF" "EXISTS")?](_images/DropCollection.png) 

DropCollection

### [](#drop-synonym)DROP Synonym

**Show DropSynonym Diagram** 

!["DROP" "SYNONYM" QualifiedName ("IF" "EXISTS")?](_images/DropSynonym.png) 

DropSynonym

### [](#drop-index)DROP Index

**Show DropIndex Diagram** 

!["DROP" "INDEX" ("IF" "EXISTS")?](_images/DropIndex.png) 

DropIndex

## [](#examples)Examples

This example drops the `remoteCapella.remoteBeer` scope, if it already exists. Dropping a scope also drops any collections contained in it and disconnects any remote links associated with those collections.

```SQL++
 DROP SCOPE remoteCapella.remoteBeer IF EXISTS;
```

**Show additional examples** 

This example removes individual collections and all of the data they contain.

```SQL++
 DROP COLLECTION remoteCapella.remoteBeer.brewBelgium;
 DROP COLLECTION remoteCapella.remoteBeer.brewGermany;
 DROP COLLECTION remoteCapella.remoteBeer.brewUS;
```

The following example drops the synonym.

```SQL++
 DROP SYNONYM remoteCapella.remoteBeer.h;
```

The following example drops the indexes.

```SQL++
 DROP INDEX remoteCapella.remoteBeer.brewBelgium.beer_name_idx;
 DROP INDEX remoteCapella.remoteBeer.brewBelgium.brewery_name_idx;
 DROP INDEX remoteCapella.remoteBeer.brewBelgium.brewery_loc_idx;
```