---
title: DROP PRIMARY INDEX
description: The DROP PRIMARY INDEX statement allows you to drop an unnamed primary index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/dropprimaryindex.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/dropprimaryindex.html)

# DROP PRIMARY INDEX

The DROP PRIMARY INDEX statement allows you to drop an unnamed primary index.

> [!IMPORTANT]
> Named primary indexes that are created using CREATE PRIMARY INDEX can only be dropped using the DROP INDEX command.

## [](#prerequisites)Prerequisites

##### RBAC Privileges

User executing the DROP PRIMARY INDEX statement must have the _Query Manage Index_ privilege granted on the keyspace. For more details about user roles, see [Roles](../../learn/security/roles.md).

## [](#syntax)Syntax

```ebnf
drop-primary-index ::= 'DROP' 'PRIMARY' 'INDEX' ( 'IF' 'EXISTS' )? 'ON' keyspace-ref
                       index-using?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-primary-index.png) 

keyspace-ref

\[Required\] Specifies the keyspace where the index is located. Refer to [Keyspace Reference](#keyspace-ref) below.

index-using

\[Optional\] Specifies the index type. Refer to [USING Clause](#index-using) below.

### [](#if-exists)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified primary index doesn’t exist. If the primary index does not exist within the specified keyspace, then:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

### [](#keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

Specifies the keyspace for the primary index to drop. The keyspace reference may be a [keyspace path](#keyspace-path) or a [keyspace partial](#keyspace-partial).

> [!NOTE]
> If there is a hyphen (-) inside any part of the keyspace reference, you must wrap that part of the keyspace reference in backticks (\` \`). Refer to the examples below.

#### [](#keyspace-path)Keyspace Path

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

If the keyspace is a named collection, or the default collection in the default scope within a bucket, the keyspace reference may be a keyspace path. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

namespace

(Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/sysinfo.md#logical-hierarchy) of the keyspace. Currently, only the `default` namespace is available. If the namespace name is omitted, the default namespace in the current session is used.

bucket

(Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/sysinfo.md#logical-hierarchy) of the keyspace.

scope

(Optional) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/sysinfo.md#logical-hierarchy) of the keyspace. If omitted, the bucket’s default scope is used.

collection

(Optional) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/sysinfo.md#logical-hierarchy) of the keyspace. If omitted, the default collection in the bucket’s default scope is used.

For example, `` default:`travel-sample` `` indicates the default collection in the default scope in the `travel-sample` bucket in the `default` namespace.

Similarly, `` default:`travel-sample`.inventory.airline `` indicates the `airline` collection in the `inventory` scope in the `travel-sample` bucket in the `default` namespace.

#### [](#keyspace-partial)Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the keyspace reference may be just the collection name with no path. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

collection

(Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/sysinfo.md#logical-hierarchy) of the keyspace.

For example, `airline` indicates the `airline` collection, assuming the query context is set.

### [](#index-using)USING Clause

```ebnf
index-using ::= 'USING' 'GSI'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-using.png) 

In Couchbase Server 6.5 and later, the index type for a primary index must be Global Secondary Index (GSI). The `USING GSI` keywords are optional and may be omitted.

## [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Drop unnamed primary index

Create an unnamed primary index on the `airline` keyspace. Once the index creation statement comes back, query `system:indexes` for status of the index.

```sqlpp
CREATE PRIMARY INDEX ON airline;
SELECT * FROM system:indexes WHERE name = '#primary';
```

Subsequently, drop the unnamed primary index with the following statement so that it is no longer reported in the `system:indexes` output.

```sqlpp
DROP PRIMARY INDEX ON airline;
SELECT * FROM system:indexes WHERE name = '#primary';
```