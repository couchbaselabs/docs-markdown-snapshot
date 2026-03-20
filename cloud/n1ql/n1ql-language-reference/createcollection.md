---
title: CREATE COLLECTION
description: The CREATE COLLECTION statement enables you to create a named
  collection within a scope.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/createcollection.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:n1ql:n1ql-language-reference/createcollection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/createcollection.html)

# CREATE COLLECTION

> The `CREATE COLLECTION` statement enables you to create a named collection within a scope. 

## [](#syntax)Syntax

```ebnf
create-collection ::= 'CREATE' 'COLLECTION' ( ( namespace ':' )? bucket '.' scope '.' )?
                      collection ( 'IF' 'NOT' 'EXISTS' )? ( 'WITH' expr )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/create-collection.png) 

| namespace  | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket in which you want to create the collection. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Optional) An [identifier](identifiers.md) that refers to the bucket in which you want to create the collection.                                                                                                                                                                                                                      |
| scope      | (Optional) An [identifier](identifiers.md) that refers to the scope in which you want to create the collection.                                                                                                                                                                                                                       |
| collection | (Required) An [identifier](identifiers.md) that refers to the name of the collection that you want to create. Refer to [Naming for Scopes and Collections](../../../server/current/learn/data/scopes-and-collections.md#naming-for-scopes-and-collections) for restrictions on collection names.                                      |

> [!NOTE]
> If there is a hyphen (-) inside the bucket name, the scope name, or the collection name, you must wrap that part of the path in backticks (\` \`). For example, `` default:`travel-sample` `` indicates the `travel-sample` keyspace in the `default` namespace.

### [](#location)Specifying the Location

To specify the location of the collection, you may do one of the following:

* Include its _full path_, containing the namespace, bucket, and scope, followed by the collection name;
* Include a _relative path_, containing just the bucket and scope, followed by the connection name;
* Specify just the collection name without a path.

When you specify a collection name without a path, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope. If you specify a collection name by itself without setting a valid query context, an error is generated.

### [](#if-not-exists)IF NOT EXISTS Clause

The optional `IF NOT EXISTS` clause enables the statement to complete successfully when the specified collection already exists. If a collection with the same name already exists within the specified scope, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

### [](#with)WITH Clause

In clusters using Couchbase Server 7.6 and later, you can use the optional `WITH` clause to specify additional options for the collection.

| expr | An object representing the options to be set for the collection. Only the maxTTL attribute is valid; any other attributes generate an error. |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------- |

 Object

| Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Schema  |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **maxTTL** _required_ | The maximum time-to-live for any item in the collection. May have any of the following values. 0 or unspecified: The collection inherits the maximum time-to-live setting from the bucket which contains it. Positive integer: By default, items in the collection expire after this many seconds. Overrides the maximum time-to-live set by the bucket. \-1: By default, items in the collection never expire. Overrides the maximum time-to-live set by the bucket. | integer |

## [](#usage)Usage

It is important to note that the scope must exist before you can create the collection, whether the scope is specified in the statement itself or implied by the query context. If the scope does not exist, an error is generated. You cannot create the scope and the collection in a single statement.

## [](#examples)Examples

Example 1\. Create collection with full path

This statement creates a collection called `city` in the `inventory` scope within the `travel-sample` bucket.

```sqlpp
CREATE COLLECTION `travel-sample`.inventory.city
```

Example 2\. Create collection with query context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Assuming that the query context is set, this statement creates a collection called `country` in the `inventory` scope within the `travel-sample` bucket.

```sqlpp
CREATE COLLECTION country;
```

Example 3\. Create collection if it doesn’t exist

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Assuming that the query context is set, this statement creates a collection called `country` in the `inventory` scope within the `travel-sample` bucket.

If the `country` collection already exists, the statement does nothing and no error is generated.

```sqlpp
CREATE COLLECTION country IF NOT EXISTS;
```

Example 4\. Create collection with maximum time-to-live

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Assuming that the query context is set, this statement creates a collection called `country` in the `inventory` scope within the `travel-sample` bucket.

The maximum time-to-live for the collection is set to `123456` seconds, overriding the maximum time-to-live specified by the bucket.

```sqlpp
CREATE COLLECTION country IF NOT EXISTS WITH {"maxTTL": 123456};
```

## [](#related-links)Related Links

* For an overview of scopes and collections, see [Buckets, Scopes, and Collections](../../clusters/data-service/about-buckets-scopes-collections.md).
* For step-by-step management procedures, see [Manage Scopes and Collections](../../clusters/data-service/scopes-collections.md).
* To manage scopes and collections with the Management API, see [Buckets, Scopes, and Collections](../../management-api-reference/index.md#tag/Buckets-Scopes-and-Collections).
* To manage scopes and collections with the Couchbase Shell, see [Couchbase Shell Documentation](https://couchbase.sh/docs/).
* For information about bucket and collection time-to-live, see [Expiration](../../../server/current/learn/data/expiration.md).