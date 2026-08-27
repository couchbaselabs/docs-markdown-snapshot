---
title: Entities in Capella Analytics Services
description: This topic describes how Capella Analytics organizes entities into
  a hierarchy and resolves the entity names in a statement or query.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/1a_entities.adoc
  xref: xref:analytics:sqlpp:1a_entities.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sqlpp/1a_entities.html)

# Entities in Capella Analytics Services

> This topic describes how Capella Analytics organizes entities into a hierarchy and resolves the entity names in a statement or query. 

For additional context about how you use these entities in Capella Analytics, see [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md).

## [](#entity-hierarchy)Entity Hierarchy

Capella Analytics organizes entities into a hierarchy with these levels:

Database
  |-- Scope
    |-- Collection
    |-- Collection
    |-- View
    |-- Synonym
    |-- User-defined Function
    ...
  |-- Scope
    |-- Collection
    |-- Collection
    ...
Database
...

Collections, views, user-defined functions, and synonyms are all at the same level of the hierarchy. To fully qualify one of these database objects in your queries, you prefix that entity's identifier with those of its database and scope in the format `database_name.scope_name.database_object_name`.

SQL++ for Capella Analytics stores indexes for individual collections: `database.scope.collection.index`. For more information about indexes, see [Using Indexes](#sqlpp:7%5Fusing%5Findex).

Examples of statements that create a database, a scope, and a collection follow, with a simplified example of `CREATE COLLECTION`. For details about the complete syntax for these statements, see [CREATE Statements](5%5Fddl%5Fcreate.md).

Entity Hierarchy Example

```SQL++
  -- create a database named music:
  CREATE DATABASE music;

  -- create a scope named myPlaylist in database music:
  CREATE SCOPE music.myPlaylist;

  -- create a collection named countrySongs in scope myPlaylist in database music (simplified):
  CREATE COLLECTION music.myPlaylist.countrySongs;
```

> [!TIP]
> Database and scope names cannot themselves include a dot (.) character. See [Requirements for Identifiers](#names).

Capella Analytics provides a Default database with a Default scope. If you do not specify the database for a scope, or the database and scope for a database\_object, Capella Analytics creates the entity in the Default database or the Default database and scope.

```SQL++
  CREATE SCOPE myPlaylist;
  -- creates the Default.myPlaylist scope

  CREATE COLLECTION countrySongs;
  -- creates the Default.Default.countrySongs collection (statement simplfied)
```

For additional examples of how Capella Analytics resolves statements in which names are not fully qualified, see [Resolving Names](#resolve). For complete `CREATE` statement syntax, see [CREATE Statements](5%5Fddl%5Fcreate.md).

## [](#metadata)Metadata Storage

Capella Analytics stores entity metadata in the internal `System` database's `Metadata` scope. In the `System.Metadata` scope, a different collection stores metadata for entities at each hierarchical level:

System database
  |-- Metadata scope
    |-- Database (metadata for databases)
    |-- Dataverse (metadata for scopes)
    |-- Dataset (metadata for database_objects)

> [!TIP]
> The terms dataverse and dataset are earlier synonyms for the terms scope and collection.

In the [entity hierarchy example](#hierarchy), you created a database, a scope, and a collection. For these entities, Capella Analytics adds metadata as follows:

```JSON
  -- New entry for the database in Metadata.Database
  {"DatabaseName": "music", ...}

  -- New entry for the scope in Metadata.Dataverse
  {"DatabaseName": "music", "DataverseName": "myPlaylist", ...}

  -- New entry for the collection in Metadata.Dataset
  {"DatabaseName": "music", "DataverseName": "myPlaylist", "DatasetName": "countrySongs", ...}
```

You can query metadata, but you cannot directly create or manipulate entities in the `System.Metadata` scope. For information about metadata for other database objects and about querying metadata, see [Querying Metadata](5%5Fddl%5Fmetadata.md).

## [](#names)Requirements for Identifiers

Names for databases, scopes, and other entities in Capella Analytics must meet the following requirements:

* Start with a letter (A-Z, a-z).
* Contain only upper- and lower-case letters (A-Z, a-z), numbers (0-9), and the underscore (\_) and dash (-) characters.  
> [!NOTE]  
> You cannot use a dot (.) character in a database or scope name.
* Be from 1 to 251 characters in length.

Also, keep the following constraints in mind:

* Identifiers are case sensitive.
* Dash (-) characters are also used as an [operator](2%5Fexpr.md#Operator%5Fexpressions). To use an identifier that includes a dash in a query, you must escape that identifier with backtick (``` `` ```) characters.
* Reserved keywords have a defined meaning in SQL++ syntax or Capella Analytics processing. To use an identifier that's the same as a [reserved keyword](reserved%5Fkeywords.md) in a query, you must escape that identifier with backtick (``` `` ```) characters.

> [!TIP]
> You may also need to escape identifiers that originate outside of Capella Analytics, and that are therefore not subject to these requirements. For example, to identify a primary key that has a space character in it, such as "Employee ID", you enter it as ```` `` `Employee ID ``` ````.

### [](#system-supplied-database-and-scope-identifiers)System-Supplied Database and Scope Identifiers

Capella Analytics automatically creates a set of databases in each cluster that you create. You cannot create a database in Capella Analytics with one of these names:

* **System**: the System database contains the Metadata scope and its collections.
* **Default**: the Default database contains the Default scope and provides a starting point for your work in a cluster.
* **Metadata**: this name is invalid for use as a database identifier.

Capella Analytics automatically creates scopes in system-supplied databases. You cannot create a scope with one of the following names in any Capella Analytics database:

* **Metadata**: in the System database, the Metadata scope contains a set of collections with details about each of the entities you create in Capella Analytics.
* **Default**: in the Default database, the Default scope provides a starting point for your work.

For a list of reserved words, see [Reserved Keywords](reserved%5Fkeywords.md). For more information about querying entity metadata, see [Querying Metadata](5%5Fddl%5Fmetadata.md).

## [](#resolve)Resolving Names

When a statement identifies the complete hierarchy for a database\_object, including its database and scope, the entity is fully qualified. The system does not need to resolve the name. Similarly, if you provide a `USE` statement to define the current database and scope, the system does not need to resolve the name.

If a statement includes no qualification or incomplete qualification, Capella Analytics resolves names as follows.

### [](#no-qualification)No Qualification

When a statement identifies only a database\_object, and does not include its database and scope, Capella Analytics resolves the name to the Default database and Default scope.

```SQL++
  -- no database or scope specified:
  SELECT * FROM countrySongs;
  -- resolves to:
  SELECT * FROM Default.Default.countrySongs;
```

Similarly, if your query refers to a scope and you do not include the database, Capella Analytics resolves the name to the Default database.

```SQL++
  -- no database specified:
  CREATE SCOPE myPlaylist;
  -- resolves to:
  CREATE SCOPE Default.myPlaylist;
```

### [](#incomplete-qualification)Incomplete Qualification

The name of a database\_object is incompletely qualified when you specify only its scope. Such names are missing the database name. Capella Analytics resolves the database name to the Default database except when the supplied scope is the Metadata scope. In this case, the database name resolves to the System database.

```SQL++
  SELECT * FROM music.countrySongs;
  -- resolves to:
  SELECT * FROM Default.music.countrySongs;

  SELECT * FROM Metadata.`Database`;
  -- resolves to:
  SELECT * FROM System.Metadata.`Database`;

  USE myPlaylist;
  -- resolves to:
  USE Default.myPlaylist;

  USE Metadata;
  -- resolves to:
  USE System.Metadata;

  USE Default;
  -- resolves to:
  USE Default.Default;
```

> [!TIP]
> To query an entity with a name that's the same as a [reserved keyword](reserved%5Fkeywords.md), like Database, you must escape the name with backtick (``` `` ```) characters.

## [](#see-also)See Also

* [Querying Metadata](5%5Fddl%5Fmetadata.md)
* [Reserved Keywords](reserved%5Fkeywords.md)
* [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md)