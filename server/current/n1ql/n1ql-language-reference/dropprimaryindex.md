---
title: DROP PRIMARY INDEX
description: The DROP PRIMARY INDEX statement allows you to drop a primary index.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/dropprimaryindex.adoc
  xref: xref:server:n1ql:n1ql-language-reference/dropprimaryindex.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/dropprimaryindex.html)

# DROP PRIMARY INDEX

The DROP PRIMARY INDEX statement allows you to drop a primary index.

> [!NOTE]
> For compatibility with legacy versions of Couchbase Server, you can also use the DROP INDEX or DROP VECTOR INDEX statement to drop a named primary index.

## [](#prerequisites)Prerequisites

##### RBAC Privileges

To execute the DROP PRIMARY INDEX statement, you must have the `Query Manage Index` privilege granted on the keyspace. For more information about user roles, see [Roles](../../learn/security/roles.md).

## [](#syntax)Syntax

```ebnf
drop-primary-index ::= 'DROP' 'PRIMARY' 'INDEX' ( index-name? ( 'IF' 'EXISTS' )? |
                       'IF' 'EXISTS' index-name ) 'ON' keyspace-ref index-using?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/drop-primary-index.png) 

| index-name   | (Optional) A unique name that identifies the index. If you do not specify a name, the index with the default name of #primary is deleted. |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| keyspace-ref | (Required) Specifies the keyspace where the index is located. See [Keyspace Reference](#keyspace-ref).                                    |
| index-using  | (Optional) Specifies the index type. See [USING Clause](#index-using).                                                                    |

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified primary index does not exist. If the primary index does not exist within the specified keyspace, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

### [](#keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

Specifies the keyspace for the primary index to drop. The keyspace reference may be a [keyspace path](#keyspace-path) or a [keyspace partial](#keyspace-partial).

> [!NOTE]
> If there is a hyphen (-) inside any part of the keyspace reference, you must wrap that part of the keyspace reference in backticks (\` \`). See the examples on this page.

#### [](#keyspace-path)Keyspace Path

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

If the keyspace is a named collection, or the default collection in the default scope within a bucket, the keyspace reference may be a keyspace path. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

| namespace  | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                                                                                                           |
| scope      | (Optional) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the bucket's default scope is used.                                                                                            |
| collection | (Optional) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the default collection in the bucket's default scope is used.                                                             |

For example, `` default:`travel-sample` `` indicates the default collection in the default scope in the `travel-sample` bucket in the `default` namespace.

Similarly, `` default:`travel-sample`.inventory.airline `` indicates the `airline` collection in the `inventory` scope in the `travel-sample` bucket in the `default` namespace.

#### [](#keyspace-partial)Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the keyspace reference may be just the collection name with no path. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |

For example, `airline` indicates the `airline` collection, assuming the query context is set.

### [](#index-using)USING Clause

```ebnf
index-using ::= 'USING' 'GSI'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-using.png) 

The index type for a primary index must be Global Secondary Index (GSI). The `USING GSI` keywords are optional and may be omitted.

## [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Drop unnamed primary index

Create an unnamed primary index on the `airline` keyspace. Once the index creation statement comes back, query `system:indexes` for status of the index.

```sqlpp
CREATE PRIMARY INDEX ON airline;
SELECT * FROM system:indexes WHERE name = '#primary';
```

Subsequently, drop the unnamed primary index with the following statement so that it's no longer reported in the `system:indexes` output.

```sqlpp
DROP PRIMARY INDEX ON airline;
SELECT * FROM system:indexes WHERE name = '#primary';
```

## [](#related-links)Related Links

* [Primary and Secondary Index Reference](../../indexes/indexing-overview.md)
* [Filtered Search Using Composite Vector Indexes](../../vector-index/composite-vector-index.md)
* [Vector Search Using Hyperscale Vector Indexes](../../vector-index/hyperscale-vector-index.md)
* [CREATE PRIMARY INDEX](createprimaryindex.md)| [CREATE INDEX](createindex.md)| [CREATE VECTOR INDEX](createvectorindex.md)
* [BUILD INDEX](build-index.md)
* [ALTER INDEX](alterindex.md)| [ALTER VECTOR INDEX](altervectorindex.md)
* [DROP INDEX](dropindex.md)| [DROP VECTOR INDEX](dropvectorindex.md)