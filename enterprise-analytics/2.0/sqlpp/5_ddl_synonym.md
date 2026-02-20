---
title: CREATE SYNONYM Statements
description: This topic describes how you can use <code>CREATE</code> statements
  to create synonyms for your Enterprise Analytics collections.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_ddl_synonym.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:sqlpp:5_ddl_synonym.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_synonym.html)

# CREATE SYNONYM Statements

> This topic describes how you can use `CREATE` statements to create synonyms for your Enterprise Analytics collections. 

## [](#syntax)Syntax

**CreateSynonym EBNF** 

```EBNF
CreateSynonym ::= "CREATE" "ANALYTICS"? "SYNONYM" QualifiedName ("IF" "NOT" "EXISTS")? "FOR" QualifiedName
```

**CreateSynonym Diagram** 

!["CREATE" "SYNONYM" QualifiedName ("IF" "NOT" "EXISTS")? "FOR" QualifiedName](_images/CreateSynonym.png) 

The first `QualifiedName` is the full name of the synonym.

## [](#examples)Examples

This example sets `h` to be a synonym in the scope `travel-sample.inventory` for the collection `hotel`.

```SQL++
  CREATE SYNONYM `travel-sample`.inventory.h FOR `travel-sample`.inventory.hotel;
```

**Show additional examples** 

This example creates a database, scope, and collection, and then creates a synonym with a shorter name for the collection.

```SQL++
  CREATE DATABASE db1;
  CREATE SCOPE db1.scope1;
  CREATE COLLECTION db1.scope1.a_very_very_very_long_collection_name PRIMARY KEY (id:int);
  CREATE SYNONYM db1.scope1.coll1 FOR db1.scope1.a_very_very_very_long_collection_name;

  USE db1.scope1;
  SELECT COUNT(*) FROM coll1;
```

The next example creates a reference to an object that belongs to a different database or scope so that you do not have to fully qualify it.

```SQL++
  CREATE database db1;
  CREATE scope db1.scope1;
  CREATE collection db1.scope1.coll1 PRIMARY KEY (id:int);

  CREATE database db2;
  CREATE scope db2.scope2;
  CREATE synonym db2.scope2.coll1_from_db1 FOR db1.scope1.coll1;
```

To access db1.scope1.col1 from the context of db2.scope2:

```SQL++
  USE db2.scope2;
  SELECT COUNT(*) FROM coll1_from_db1;
```

## [](#arguments)Arguments

FOR

The **`FOR`** clause specifies the target of the synonym. The `QualifiedName` in this clause is the fully qualified name of a collection.

For information about how Enterprise Analytics organizes entities into a `database.scope.database_object` hierarchy and resolves names, see [Entities in Enterprise Analytics](1a%5Fentities.md).