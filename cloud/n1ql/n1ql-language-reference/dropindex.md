---
title: DROP INDEX
description: The DROP INDEX statement allows you to drop a secondary index, a
  Composite Vector index, or a Hyperscale Vector index.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/dropindex.adoc
  xref: xref:cloud:n1ql:n1ql-language-reference/dropindex.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/dropindex.html)

# DROP INDEX

The DROP INDEX statement allows you to drop a secondary index, a Composite Vector index, or a Hyperscale Vector index. Dropping an index that has replicas will drop all of the replica indexes too.

The [DROP VECTOR INDEX](dropvectorindex.md) statement is a synonym for the DROP INDEX statement. Both statements have the same functionality.

> [!NOTE]
> To drop a primary index, use the [DROP PRIMARY INDEX](dropprimaryindex.md) statement. For compatibility with legacy versions of Couchbase Server, you can also use DROP INDEX or DROP VECTOR INDEX to drop a named primary index.

## [](#prerequisites)Prerequisites

To execute this statement, your client must have necessary privileges on the keyspace that contains the index. The required privilege depends on your [cluster access credential type](../../clusters/cluster-rbac.md#cluster-access-credential-types).

| Credential Type | Privilege                                                                                |
| --------------- | ---------------------------------------------------------------------------------------- |
| Basic           | [Write](../../clusters/cluster-rbac.md#basic-access-credentials)                         |
| Advanced        | [Query Index](../../clusters/cluster-rbac.md#privileges-for-advanced-access-credentials) |

## [](#syntax)Syntax

```ebnf
drop-index ::= 'DROP' 'INDEX' ( index-path-and-name | index-name-on-keyspace )
               index-using?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/drop-index.png) 

The DROP INDEX statement provides two possible syntaxes for specifying the index and the keyspace where the index is located.

| index-path-and-name    | (Optional) One possible syntax for specifying the index and keyspace. See [Index Path and Name](#index-path-and-name).                       |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| index-name-on-keyspace | (Optional) The other possible syntax for specifying the index and keyspace. See [Index Name ON Keyspace Reference](#index-name-on-keyspace). |
| index-using            | (Optional) Specifies the index type. See [USING Clause](#index-using).                                                                       |

### [](#index-path-and-name)Index Path and Name

```ebnf
index-path-and-name ::= index-path '.' index-name ( 'IF' 'EXISTS' )? |
                        'IF' 'EXISTS' index-path '.' index-name
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-path-and-name.png) 

You can use a dotted notation to specify the index and the keyspace on which the index is built. This syntax provides compatibility with legacy versions of Couchbase Server.

| index-name | (Required) A unique name that identifies the index. |
| ---------- | --------------------------------------------------- |
| index-path | (Required) See [Index Path](#index-path).           |

> [!NOTE]
> If there is a hyphen (-) inside the index name or any part of the index path, you must wrap the index name or that part of the index path in backticks (\` \`). See the examples on this page.

#### [](#index-path)Index Path

```ebnf
index-path ::= keyspace-full | keyspace-prefix | keyspace-partial
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-path.png) 

The index path may be a [full keyspace path](#keyspace-full-index), a [keyspace prefix](#keyspace-prefix-index), or a [keyspace partial](#keyspace-partial-index).

##### [](#keyspace-full-index)Index Path: Full Keyspace

```ebnf
keyspace-full ::= namespace ':' bucket '.' scope '.' collection
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-full.png) 

If the index is built on a named collection, the index path may be a full keyspace path, including namespace, bucket, scope, and collection, followed by the index name. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) is ignored.

| namespace  | (Required) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                   |
| scope      | (Required) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                    |
| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                               |

For example, `` default:`travel-sample`.inventory.airline.`idx-name` `` indicates the `idx-name` index on the `airline` collection in the `inventory` scope in the `` default:`travel-sample` `` bucket.

##### [](#keyspace-prefix-index)Index Path: Keyspace Prefix

```ebnf
keyspace-prefix ::= ( namespace ':' )? bucket
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-prefix.png) 

If the index is built on the default collection in the default scope within a bucket, the index path may be just an optional namespace and the bucket name, followed by the index name. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

| namespace | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket    | (Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.                                                                                                                                           |

For example, `` default:`travel-sample`.def_type `` indicates the `def_type` index on the default collection in the default scope in the `` default:`travel-sample` `` bucket.

##### [](#keyspace-partial-index)Index Path: Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the index path may be just the collection name, followed by the index name. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |

For example, `` airline.`idx-name` `` indicates the `idx-name` index on the `airline` collection, assuming that the query context is set.

### [](#index-name-on-keyspace)Index Name ON Keyspace Reference

```ebnf
index-name-on-keyspace ::= ( index-name ( 'IF' 'EXISTS' )? | 'IF' 'EXISTS' index-name )
                           'ON' keyspace-ref
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-name-on-keyspace.png) 

You can use the index name with the `ON` keyword and a keyspace reference to specify the index and the keyspace on which the index is built.

| index-name   | (Required) A unique name that identifies the index. |
| ------------ | --------------------------------------------------- |
| keyspace-ref | (Required) See [Keyspace Reference](#keyspace-ref). |

> [!NOTE]
> If there is a hyphen (-) inside the index name or any part of the keyspace reference, you must wrap the index name or that part of the keyspace reference in backticks (\` \`). See the examples on this page.

#### [](#keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

The keyspace reference may be a [keyspace path](#keyspace-path) or a [keyspace partial](#keyspace-partial).

##### [](#keyspace-path)Keyspace Reference: Keyspace Path

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

For example, `` def_type ON default:`travel-sample` `` indicates the `def_type` index on the default collection in the default scope in the `` default:`travel-sample` `` bucket.

Similarly, `` `idx-name` ON default:`travel-sample`.inventory.airline `` indicates the `idx-name` index on the `airline` collection in the `inventory` scope in the `` default:`travel-sample` `` bucket.

##### [](#keyspace-partial)Keyspace Reference: Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the keyspace reference may be just the collection name. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

| collection | (Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |

For example, `` `idx-name` ON airline `` indicates the `idx-name` index on the `airline` collection, assuming the query context is set.

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified index does not exist. If the index does not exist within the specified keyspace, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

### [](#index-using)USING Clause

```ebnf
index-using ::= 'USING' 'GSI'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/index-using.png) 

The index type for a secondary index must be Global Secondary Index (GSI). The `USING GSI` keywords are optional and may be omitted.

## [](#usage)Usage

When using memory-optimized indexes, DROP INDEX is an expensive operation and may take a few minutes to complete.

If you drop an index with replicas while one of the index nodes is failed over, then only the replicas in the active index nodes are dropped. If the failed-over index node is recovered, then the orphan replica will be dropped when this failed-over indexer is added back to cluster.

If you drop an index with replicas when one of the index nodes is unavailable but not failed over, the drop index operation may fail.

If you drop an index which is scheduled for background creation, a warning message is generated, but the drop index operation succeeds.

> [!IMPORTANT]
> Attention
> 
> Do not drop (or create) secondary indexes, Composite Vector indexes, or Hyperscale Vector indexes when any Index service node is down, as this may result in duplicate index names.

## [](#examples)Examples

To try the examples in this section, you must set the query context as described in each example.

Example 1\. Drop index from the default collection in the default scope

This example drops an index from the default collection in the default scope within the `travel-sample` bucket. For this example, unset the query context. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

First create a secondary index on the default collection in the default scope in the `travel-sample` bucket. Once the index creation statement comes back, query `system:indexes` for the status of the index.

```sqlpp
CREATE INDEX `idx-callsign` ON `travel-sample`(callsign) USING GSI;
SELECT * FROM system:indexes WHERE name="idx-callsign";
```

Subsequently, drop the index and check that it's no longer reported in the `system:indexes` output.

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

## [](#related-links)Related Links

* [Primary and Secondary Index Reference](../../indexes/indexing-overview.md)
* [Filtered Search Using Composite Vector Indexes](../../vector-index/composite-vector-index.md)
* [Vector Search Using Hyperscale Vector Indexes](../../vector-index/hyperscale-vector-index.md)
* [CREATE PRIMARY INDEX](createprimaryindex.md)| [CREATE INDEX](createindex.md)| [CREATE VECTOR INDEX](createvectorindex.md)
* [BUILD INDEX](build-index.md)
* [ALTER INDEX](alterindex.md)| [ALTER VECTOR INDEX](altervectorindex.md)
* [DROP PRIMARY INDEX](dropprimaryindex.md)| [DROP VECTOR INDEX](dropvectorindex.md)