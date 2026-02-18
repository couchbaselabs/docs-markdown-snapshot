---
title: CREATE SCOPE
description: The <code>CREATE SCOPE</code> statement enables you to create a scope.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/createscope.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/n1ql/n1ql-language-reference/createscope.html)

# CREATE SCOPE

> The `CREATE SCOPE` statement enables you to create a scope. 

## [](#syntax)Syntax

```ebnf
create-scope ::= 'CREATE' 'SCOPE' ( namespace ':' )? bucket '.' scope ( 'IF' 'NOT' 'EXISTS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/create-scope.png) 

| namespace | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket in which you want to create the scope. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket    | (Required) An [identifier](identifiers.md) that refers to the bucket in which you want to create the scope.                                                                                                                                                                                                                      |
| scope     | (Required) An [identifier](identifiers.md) that refers to the name of the scope that you want to create. Refer to [Naming for Scopes and Collections](../../learn/data/scopes-and-collections.md#naming-for-scopes-and-collections) for restrictions on scope names.                                                             |

> [!NOTE]
> If there is a hyphen (-) inside the bucket name or the scope name, you must wrap that part of the path in backticks (\` \`). For example, `` default:`travel-sample` `` indicates the `travel-sample` keyspace in the `default` namespace.

### [](#if-not-exists)IF NOT EXISTS Clause

The optional `IF NOT EXISTS` clause enables the statement to complete successfully when the specified scope already exists. If a scope with the same name already exists within the specified bucket, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#example)Example

This statement creates a scope called `events` in the `travel-sample` bucket.

```sqlpp
CREATE SCOPE `travel-sample`.events
```

## [](#related-links)Related Links

* An overview of scopes and collections is provided in [Scopes and Collections](../../learn/data/scopes-and-collections.md).
* Step-by-step procedures for management are provided in [Manage Scopes and Collections](../../manage/manage-scopes-and-collections/manage-scopes-and-collections.md).
* Refer to [Scopes and Collections API](../../rest-api/scopes-and-collections-api.md) to manage scopes and collections with the REST API.
* Refer to the reference page for the [collection-manage](../../cli/cbcli/couchbase-cli-collection-manage.md) command to manage scopes and collections with the CLI.