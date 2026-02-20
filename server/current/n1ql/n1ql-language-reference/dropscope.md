---
title: DROP SCOPE
description: The <code>DROP SCOPE</code> statement enables you to delete a scope.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/dropscope.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:n1ql:n1ql-language-reference/dropscope.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-language-reference/dropscope.html)

# DROP SCOPE

> The `DROP SCOPE` statement enables you to delete a scope. 

## [](#syntax)Syntax

```ebnf
drop-scope ::= 'DROP' 'SCOPE' ( namespace ':' )? bucket '.' scope ( 'IF' 'EXISTS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-scope.png) 

| namespace | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket which contains the scope you want to delete. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket    | (Required) An [identifier](identifiers.md) that refers to the bucket which contains the scope you want to delete.                                                                                                                                                                                                                      |
| scope     | (Required) An [identifier](identifiers.md) that refers to the name of the scope that you want to delete.                                                                                                                                                                                                                               |

> [!NOTE]
> If there is a hyphen (-) inside the bucket name or the scope name, you must wrap that part of the path in backticks (\` \`). For example, `` default:`travel-sample` `` indicates the `travel-sample` keyspace in the `default` namespace.

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified scope doesn’t exist. If the scope does not exist within the specified bucket, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#usage)Usage

When you delete a scope, any collections within that scope are deleted also.

## [](#example)Example

This statement deletes a scope called `events` in the `travel-sample` bucket.

```sqlpp
DROP SCOPE `travel-sample`.events
```

## [](#related-links)Related Links

* An overview of scopes and collections is provided in [Scopes and Collections](../../learn/data/scopes-and-collections.md).
* Step-by-step procedures for management are provided in [Manage Scopes and Collections](../../manage/manage-scopes-and-collections/manage-scopes-and-collections.md).
* Refer to [Scopes and Collections API](../../rest-api/scopes-and-collections-api.md) to manage scopes and collections with the REST API.
* Refer to the reference page for the [collection-manage](../../cli/cbcli/couchbase-cli-collection-manage.md) command to manage scopes and collections with the CLI.