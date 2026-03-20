---
title: DROP SCOPE
description: The DROP SCOPE statement enables you to delete a scope.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/dropscope.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:n1ql:n1ql-language-reference/dropscope.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/dropscope.html)

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

* For an overview of scopes and collections, see [Buckets, Scopes, and Collections](../../clusters/data-service/about-buckets-scopes-collections.md).
* For step-by-step management procedures, see [Manage Scopes and Collections](../../clusters/data-service/scopes-collections.md).
* To manage scopes and collections with the Management API, see [Buckets, Scopes, and Collections](../../management-api-reference/index.md#tag/Buckets-Scopes-and-Collections).
* To manage scopes and collections with the Couchbase Shell, see [Couchbase Shell Documentation](https://couchbase.sh/docs/).