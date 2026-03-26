---
title: DROP COLLECTION
description: The DROP COLLECTION statement enables you to delete a named
  collection from a scope.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/dropcollection.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:n1ql:n1ql-language-reference/dropcollection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/dropcollection.html)

# DROP COLLECTION

> The `DROP COLLECTION` statement enables you to delete a named collection from a scope. 

## [](#syntax)Syntax

```ebnf
drop-collection ::= 'DROP' 'COLLECTION' ( ( namespace ':' )? bucket '.' scope '.' )?
                    collection ( 'IF' 'EXISTS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-collection.png) 

| namespace  | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket which contains the collection you want to delete. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Optional) An [identifier](identifiers.md) that refers to the bucket which contains the collection you want to delete.                                                                                                                                                                                                                      |
| scope      | (Optional) An [identifier](identifiers.md) that refers to the scope which contains the collection you want to delete.                                                                                                                                                                                                                       |
| collection | (Required) An [identifier](identifiers.md) that refers to the name of the collection that you want to delete.                                                                                                                                                                                                                               |

> [!NOTE]
> If there is a hyphen (-) inside the bucket name, the scope name, or the collection name, you must wrap that part of the path in backticks (\` \`). For example, `` default:`travel-sample` `` indicates the `travel-sample` keyspace in the `default` namespace.

### [](#location)Specifying the Location

To specify the location of the collection, you may do one of the following:

* Include its _full path_, containing the namespace, bucket, and scope, followed by the collection name;
* Include a _relative path_, containing just the bucket and scope, followed by the connection name;
* Specify just the collection name without a path.

When you specify a collection name without a path, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope. If you specify a collection name by itself without setting a valid query context, an error is generated.

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified collection doesn't exist. If the collection does not exist within the specified scope, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#examples)Examples

Example 1\. Delete collection with full path

This statement deletes a collection called `city` in the `inventory` scope within the `travel-sample` bucket.

```sqlpp
DROP COLLECTION `travel-sample`.inventory.city
```

Example 2\. Delete collection with query context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Assuming that the query context is set, this statement deletes a collection called `country` in the `inventory` scope within the `travel-sample` bucket.

```sqlpp
DROP COLLECTION country;
```

## [](#related-links)Related Links

* An overview of scopes and collections is provided in [Scopes and Collections](../../learn/data/scopes-and-collections.md).
* Step-by-step procedures for management are provided in [Manage Scopes and Collections](../../manage/manage-scopes-and-collections/manage-scopes-and-collections.md).
* Refer to [Scopes and Collections API](../../rest-api/scopes-and-collections-api.md) to manage scopes and collections with the REST API.
* Refer to the reference page for the [collection-manage](../../cli/cbcli/couchbase-cli-collection-manage.md) command to manage scopes and collections with the CLI.