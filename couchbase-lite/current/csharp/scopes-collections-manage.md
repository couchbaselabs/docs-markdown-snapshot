---
title: Manage Scopes and Collections
description: Scopes and collections allow you to organize your documents within a database.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/csharp/pages/scopes-collections-manage.adoc
  xref: xref:couchbase-lite:csharp:scopes-collections-manage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/csharp/scopes-collections-manage.html)

# Manage Scopes and Collections

> Scopes and collections allow you to organize your documents within a database. 

At a glance

**Use collections to organize your content in a database**

For example, if your database contains travel information, airport documents can be assigned to an airports collection, hotel documents can be assigned to a hotels collection, and so on.

* Document names must be unique within their collection.

**Use scopes to group multiple collections**

Collections can be assigned to different scopes according to content-type or deployment-phase (for example, test versus production).

* Collection names must be unique within their scope.

## [](#default-scopes-and-collections)Default Scopes and Collections

Every database you create contains a default scope and a default collection named \_default.

If you create a document in the database and don't specify a specific scope or collection, it is saved in the default collection, in the default scope.

If you upgrade from a version of Couchbase Lite prior to 3.1, all existing data is automatically placed in the default scope and default collection.

The default scope and collection cannot be dropped.

## [](#create-a-scope-and-collection)Create a Scope and Collection

In addition to the default scope and collection, you can create your own scope and collection when you create a document.

Naming conventions for collections and scopes:

* Must be between 1 and 251 characters in length.
* Can only contain the characters `A-Z`, `a-z`, `0-9`, and the symbols `_`, `-`, and `%`.
* Cannot start with `_` or `%`.
* Scope names must be unique in databases.
* Collection names must be unique within a scope.

> [!NOTE]
> Scope and collection names are case sensitive.

Example 1\. Create a scope and collection

```C#
var collectionWithDefaultScope = Database!.CreateCollection("colA");
var collection = database.CreateCollection("colA", "scopeA"); // Scope with named scopeA will be created if it's not existed. There is no public API to create a Scope.
```

In the example above, you can see that `db.createCollection()` can take two parameters. The first is the scope assigned to the created collection, if this parameter is omitted then a collection of the given name will be assigned to the `_default` scope. In this case, creating a collection called `Verlaine`.

The second parameter is the name of the collection you want to create, in this case `Verlaine`. In the second section of the example you can see `db.createCollection("Television", "Verlaine")`. This creates the collection `Verlaine` and then checks to see if the scope `Television` exists. If the scope `Television` exists, the collection `Verlaine` is assigned to the scope `Television`. If not, a new scope, `Television` is created and then the collection `Verlaine` is assigned to it.

> [!NOTE]
> You cannot create an empty user-defined scope. A scope is implicitly created in the `db.createCollection()` method.

## [](#index-a-collection)Index a Collection

Example 2\. Index a Collection

```C#
string[] indexProperties = ["type", "name"];
var config = new ValueIndexConfiguration(indexProperties);
collection.CreateIndex("TypeNameIndex", config);
```

## [](#drop-a-collection)Drop a Collection

Example 3\. Drop a Collection

```C#
database.DeleteCollection("colA", "scopeA"); // Scope with named scopeA will be deleted if there is no collections in the scope after the last collection is deleted via this API. There is no public API to remove a Scope.
```

> [!NOTE]
> There is no need to drop a user-defined scope. User-defined scopes are dropped when the collections associated with them contain no documents.

## [](#list-scopes-and-collections)List Scopes and Collections

Example 4\. List Scopes and Collections

```C#
// Get Scopes
var scopes = Database!.GetScopes();
// Get Collections of a Scope named scopeA
var scopeA = database.GetScope("scopeA");
Debug.Assert(scopeA != null);
var collectionsInScopeA = scopeA.GetCollections();
```