---
title: Manage Scopes and Collections
description: Scopes and collections allow you to organize your documents within a database.
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/c/pages/scopes-collections-manage.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite:c:scopes-collections-manage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/c/scopes-collections-manage.html)

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

* C
* C++

```c
CBLError err = {};
CBLDatabase_CreateCollection(db, FLSTR("collA"), FLSTR("scopeA"), &err);
```

```cpp
db.createCollection("collA", "scopeA");
```

In the example above, you can see that `db.createCollection()` can take two parameters. The first is the scope assigned to the created collection, if this parameter is omitted then a collection of the given name will be assigned to the `_default` scope. In this case, creating a collection called `Verlaine`.

The second parameter is the name of the collection you want to create, in this case `Verlaine`. In the second section of the example you can see `db.createCollection("Television", "Verlaine")`. This creates the collection `Verlaine` and then checks to see if the scope `Television` exists. If the scope `Television` exists, the collection `Verlaine` is assigned to the scope `Television`. If not, a new scope, `Television` is created and then the collection `Verlaine` is assigned to it.

> [!NOTE]
> You cannot create an empty user-defined scope. A scope is implicitly created in the `db.createCollection()` method.

## [](#index-a-collection)Index a Collection

Example 2\. Index a Collection

* C
* C++

```c
CBLValueIndexConfiguration config = {};
config.expressionLanguage = kCBLN1QLLanguage;
config.expressions = FLSTR("type, name");

CBLError err = {};
CBLCollection_CreateValueIndex(collection, FLSTR("TypeNameIndex"), config, &err);
```

```cpp
cbl::ValueIndexConfiguration config{};
config.expressionLanguage = kCBLN1QLLanguage;
config.expressions = "type, name";

collection.createValueIndex("TypeNameIndex", config);
```

## [](#drop-a-collection)Drop a Collection

Example 3\. Drop a Collection

* C
* C++

```c
CBLError err = {};
CBLDatabase_DeleteCollection(db, FLSTR("collA"), FLSTR("scopeA"), &err);
```

```cpp
db.deleteCollection("collA", "scopeA");
```

> [!NOTE]
> There is no need to drop a user-defined scope. User-defined scopes are dropped when the collections associated with them contain no documents.

## [](#list-scopes-and-collections)List Scopes and Collections

Example 4\. List Scopes and Collections

* C
* C++

```c
CBLError err = {};

// Get Scopes
FLMutableArray scopes = CBLDatabase_ScopeNames(db, &err);
// Get default Scope
CBLScope *scope = CBLDatabase_DefaultScope(db, &err);
// Get specific Scope named scopeA
CBLScope *scopeA = CBLDatabase_Scope(db, FLSTR("scopeA"), &err);
// Get Collections of a specific Scope named scopeA
FLMutableArray collections = CBLDatabase_CollectionNames(db, FLSTR("scopeA"), &err);
// Get default Collection
CBLCollection *collection = CBLDatabase_DefaultCollection(db, &err);
// Get specific Collection named collA of a specific Scope named scopeA
CBLCollection *collA = CBLDatabase_Collection(db, FLSTR("collA"), FLSTR("scopeA"), &err);
```

```cpp
// Get Scope names
fleece::MutableArray scopes = db.getScopeNames();
// Get Collection names of a specific Scope named scopeA
fleece::MutableArray collections = db.getCollectionNames("scopeA");
// Get default Collection
cbl::Collection collection = db.getDefaultCollection();
// Get specific Collection named collA of a specific Scope named scopeA
cbl::Collection collA = db.getCollection("collA", "scopeA");
// Get the Scope name of a Collection
std::string scopeName = collA.scopeName();
```