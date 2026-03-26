---
title: DROP INDEX
description: The DROP INDEX statement allows you to drop a named primary index
  or a secondary index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/dropindex.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.6@server:n1ql:n1ql-language-reference/dropindex.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/dropindex.html)

# DROP INDEX

The DROP INDEX statement allows you to drop a named primary index or a secondary index. Dropping an index that has replicas will also drop all of the replica indexes too. You can drop unnamed primary indexes using the [DROP PRIMARY INDEX](dropprimaryindex.md) statement.

## [](#prerequisites)Prerequisites

##### RBAC Privileges

User executing the DROP INDEX statement must have the _Query Manage Index_ privilege granted on the keyspace/bucket. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
drop-index ::= 'DROP' 'INDEX' ( index-path '.' index-name ( 'IF' 'EXISTS' )? |
                index-name ( 'IF' 'EXISTS' )? 'ON' keyspace-ref ) index-using?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-index.png) 

The DROP INDEX statement provides two possible syntaxes for specifying the index and the keyspace where the index is located.

| index-name   | (Required) A unique name that identifies the index.                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| index-path   | (Optional) One possible syntax for specifying the the keyspace. Refer to [Index Path](#index-path) below.                           |
| keyspace-ref | (Optional) The other possible syntax for specifying the keyspace. Refer to [Index Name ON Keyspace Reference](#keyspace-ref) below. |
| index-using  | Specifies the index type. (Optional) Refer to [USING Clause](#index-using) below.                                                   |

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified index doesn't exist. If the index does not exist within the specified keyspace, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

### [](#index-path)Index Path

```ebnf
index-path ::= keyspace-full | keyspace-prefix | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-path.png) 

You can use a dotted notation to specify the index and the keyspace on which the index is built. This syntax provides compatibility with legacy versions of Couchbase Server. The index path may be a [full keyspace path](#keyspace-full-index), a [keyspace prefix](#keyspace-prefix-index), or a [keyspace partial](#keyspace-partial-index).

> [!NOTE]
> If there is a hyphen (-) inside the index name or any part of the index path, you must wrap the index name or that part of the index path in backticks (\` \`). Refer to the examples below.

#### [](#keyspace-full-index)Index Path: Full Keyspace

```ebnf
keyspace-full ::= namespace ':' bucket '.' scope '.' collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-full.png) 

If the index is built on a named collection, the index path may be a full keyspace path, including namespace, bucket, scope, and collection, followed by the index name. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) is ignored.

| namespace  | (Required) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                   |
| scope      | (Required) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                    |
| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                               |

For example, `` default:`travel-sample`.inventory.airline.`idx-name` `` indicates the `idx-name` index on the `airline` collection in the `inventory` scope in the `` default:`travel-sample` `` bucket.

#### [](#keyspace-prefix-index)Index Path: Keyspace Prefix

```ebnf
keyspace-prefix ::= ( namespace ':' )? bucket
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-prefix.png) 

If the index is built on the default collection in the default scope within a bucket, the index path may be just an optional namespace and the bucket name, followed by the index name. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

| namespace | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket    | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                                                                                                           |

For example, `` default:`travel-sample`.def_type `` indicates the `def_type` index on the default collection in the default scope in the `` default:`travel-sample` `` bucket.

#### [](#keyspace-partial-index)Index Path: Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the index path may be just the collection name, followed by the index name. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |

For example, `` airline.`idx-name` `` indicates the `idx-name` index on the `airline` collection, assuming that the query context is set.

### [](#keyspace-ref)Index Name ON Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

You can use the index name with the `ON` keyword and a keyspace reference to specify the keyspace on which the index is built. The keyspace reference may be a [keyspace path](#keyspace-path) or a [keyspace partial](#keyspace-partial).

> [!NOTE]
> If there is a hyphen (-) inside the index name or any part of the keyspace reference, you must wrap the index name or that part of the keyspace reference in backticks (\` \`). Refer to the examples below.

#### [](#keyspace-path)Keyspace Reference: Keyspace Path

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

If the keyspace is a named collection, or the default collection in the default scope within a bucket, the keyspace reference may be a keyspace path. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

| namespace  | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                                                                                                           |
| scope      | (Optional) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the bucket's default scope is used.                                                                                            |
| collection | (Optional) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the default collection in the bucket's default scope is used.                                                             |

For example, `` def_type ON default:`travel-sample` `` indicates the `def_type` index on the default collection in the default scope in the `` default:`travel-sample` `` bucket.

Similarly, `` `idx-name` ON default:`travel-sample`.inventory.airline `` indicates the `idx-name` index on the `airline` collection in the `inventory` scope in the `` default:`travel-sample` `` bucket.

#### [](#keyspace-partial)Keyspace Reference: Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the keyspace reference may be just the collection name. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |

For example, `` `idx-name` ON airline `` indicates the `idx-name` index on the `airline` collection, assuming the query context is set.

### [](#index-using)USING Clause

```ebnf
index-using ::= 'USING' 'GSI'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-using.png) 

The index type for a secondary index must be Global Secondary Index (GSI). The `USING GSI` keywords are optional and may be omitted.

## [](#usage)Usage

When using memory-optimized indexes, DROP INDEX is an expensive operation and may take a few minutes to complete.

If you drop an index with replicas while one of the index nodes is failed over, then only the replicas in the active index nodes are dropped. If the failed-over index node is recovered, then the orphan replica will be dropped when this failed-over indexer is added back to cluster.

If you drop an index with replicas when one of the index nodes is unavailable but not failed over, the drop index operation may fail.

If you drop an index which is scheduled for background creation, a warning message is generated, but the drop index operation succeeds.

> [!IMPORTANT]
> We recommend that you do not drop (or create) secondary indexes when any node with a secondary index role is down as this may result in duplicate index names.

## [](#examples)Examples

To try the examples in this section, you must set the query context as described in each example.

Example 1\. Drop index from the default collection in the default scope

This example drops an index from the default collection in the default scope within the `travel-sample` bucket. For this example, unset the query context. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

First create a secondary index on the default collection in the default scope in the `travel-sample` bucket. Once the index creation statement comes back, query `system:indexes` for the status of the index.

```sqlpp
CREATE INDEX `idx-callsign` ON `travel-sample`(callsign) USING GSI;
SELECT * FROM system:indexes WHERE name="idx-callsign";
```

Subsequently, drop the index and check that it is no longer reported in the `system:indexes` output.

```sqlpp
DROP INDEX `travel-sample`.`idx-callsign` USING GSI;
SELECT * FROM system:indexes WHERE name="idx-callsign";
```

The following command would drop the index in exactly the same way, but uses alternative syntax.

```sqlpp
DROP INDEX `idx-callsign` ON `travel-sample` USING GSI;
```

Example 2\. Drop index from a named collection with path

This example drops an index from the `airline` collection. For this example, the path to the required keyspace is specified by the query, so you do not need to set the query context.

First create an index called `idx-name` in the `airline` collection.

```sqlpp
CREATE INDEX `idx-name` ON `travel-sample`.inventory.airline(name) USING GSI;
```

Drop the index `idx-name` from the `airline` collection.

```sqlpp
DROP INDEX `idx-name` ON `travel-sample`.inventory.airline;
```

Example 3\. Drop index from a named collection with query context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Create an index called `idx-name` in the `airline` collection.

```sqlpp
CREATE INDEX `idx-name` ON airline(name);
```

Drop the index `idx-name` from the `airline` collection.

```sqlpp
DROP INDEX `idx-name` ON airline;
```

The following command would drop the index in exactly the same way, but uses alternative syntax.

```sqlpp
DROP INDEX airline.`idx-name`;
```