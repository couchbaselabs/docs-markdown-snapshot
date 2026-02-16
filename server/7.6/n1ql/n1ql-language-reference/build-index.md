[View original HTML](/server/7.6/n1ql/n1ql-language-reference/build-index.html)

> The BUILD INDEX statement enables you to build one or more GSI indexes that are marked for deferred building all at once. 

By default, CREATE INDEX starts building the created index after the creation stage is complete. However for more efficient building of multiple indexes, CREATE INDEX can mark indexes for deferred building using the `defer_build:true` option. BUILD INDEX is capable of building multiple indexes at once, and can utilize a single scan of documents in the keyspace to feed many index build operations.

BUILD INDEX is an asynchronous operation. BUILD INDEX creates a task to build the primary or secondary GSI indexes and returns as soon as the task is queued for execution. The full index build operation happens in the background.

Index metadata provides a state field. The index state may be `scheduled for creation`, `deferred`, `building`, `pending`, `online`, `offline`, or `abridged`. This state field and other index metadata can be queried using [system:indexes](../n1ql-intro/sysinfo.md#querying-indexes). You can also monitor the index state using the Couchbase Web Console.

If you attempt to build an index which is still scheduled for background creation, the request fails.

|  | If you kick off multiple index build operations concurrently, then you may sometimes see transient errors similar to the following. \[   {     "code": 5000,     "msg": "GSI CreateIndex() - cause: Encountered transient error.  Index creation will be retried in background.  Error: Index ... will retry building in the background for reason: Build Already In Progress. Keyspace ...",     "query": "..."   } \] To work around this issue, wait for index building to complete (that is, for all indexes to get to the online state), then issue the BUILD INDEX command again. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

BUILD INDEX is also idempotent. On execution, the statement only builds indexes which have not already been built. If any of the indexes specified by BUILD INDEX have already been built, BUILD INDEX skips those indexes.

When building an index which has automatic index replicas, all of the replicas are also built as part of the BUILD INDEX statement, without having to manually specify them.

## [](#prerequisites)Prerequisites

##### RBAC Privileges

User executing the BUILD INDEX statement must have the _Query Manage Index_ privilege granted on the keyspace. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
build-index ::= 'BUILD' 'INDEX' 'ON' keyspace-ref '(' index-term (',' index-term)* ')'
                index-using?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/build-index.png) 

| keyspace-ref | (Required) Specifies the keyspace where the indexes are built. Refer to [Keyspace Reference](#keyspace-ref) below. |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| index-term   | (Required) Specifies the indexes to build. Refer to [Index Term](#index-term) below.                               |
| index-using  | (Optional) Specifies the index type. Refer to [USING Clause](#index-using) below.                                  |

### [](#keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

The simple name or fully-qualified name of the keyspace on which to build the index. Refer to the [CREATE INDEX](createindex.md#keyspace-ref) statement for details of the syntax.

### [](#index-term)Index Term

```ebnf
index-term ::= index-name | index-expr | subquery-expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-term.png) 

You can specify one index term, or multiple index terms separated by commas. An index term must be specified for each index to be built.

Each index term may be an [index name](#index-name), an [index expression](#index-expr), or a [subquery expression](#subquery-expr). The BUILD INDEX clause may contain a mixture of the different types of index term.

#### [](#index-name)Index Name

```ebnf
index-name ::= identifier
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-name.png) 

An [identifier](identifiers.md) that refers to the name of an index.

```sqlpp
BUILD INDEX ON keyspace(ix1, ix2, ix3);
```

#### [](#index-expr)Index Expression

```ebnf
index-expr ::= string | array
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-expr.png) 

An [expression](index.md) that may be a string, or an array of strings, each referring to the name of an index.

```sqlpp
BUILD INDEX ON keyspace('ix1', 'ix2', 'ix3');
BUILD INDEX ON keyspace(['ix1', 'ix2', 'ix3']);
BUILD INDEX ON keyspace('ix1', ['ix2', 'ix3'], ['ix4']);
```

|  | Arrays of identifiers are _not_ permitted. BUILD INDEX ON keyspace(\[ix1, ix2, ix3\]); BUILD INDEX ON keyspace(\[ix1\], \[ix2, ix3\]); |
|  | -------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#subquery-expr)Subquery Expression

```ebnf
subquery-expr ::= '(' select ')'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/subquery-expr.png) 

Use parentheses to specify a subquery.

The subquery must return an array of strings, each string representing the name of an index. See [Example 4](#ex-build-idx-all) for details.

For more details and examples, see [SELECT Clause](selectclause.md) and [Subqueries](subqueries.md).

### [](#index-using)USING Clause

```ebnf
index-using ::= 'USING' 'GSI'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-using.png) 

The index type for a deferred index build must be Global Secondary Index (GSI). The `USING GSI` keywords are optional and may be omitted.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Create deferred indexes

Create a set of primary and secondary indexes in the `landmark` keyspace with the `defer_build` option.

```sqlpp
CREATE INDEX idx_landmark_country
  ON landmark(country)
  USING GSI
  WITH {"defer_build":true};
```

```sqlpp
CREATE INDEX idx_landmark_name 
  ON landmark(name)
  USING GSI
  WITH {"defer_build":true};
```

```sqlpp
CREATE PRIMARY INDEX idx_landmark_primary
  ON landmark
  USING GSI
  WITH {"defer_build":true};
```

Example 2\. Check deferred index status

Query `system:indexes` for the status of an index.

```sqlpp
SELECT * FROM system:indexes WHERE name="idx_landmark_country";
```

Results

```json
[
  {
    "indexes": {
      "bucket_id": "travel-sample",
      "datastore_id": "http://127.0.0.1:8091",
      "id": "d079aec40eb0c6cc",
      "index_key": [
        "`country`"
      ],
      "keyspace_id": "landmark",
      "name": "idx_landmark_country",
      "namespace_id": "default",
      "scope_id": "inventory",
      "state": "deferred", (1)
      "using": "gsi"
    }
  }
]
```

| **1** | Note that the index is in the deferred state. |
| ----- | --------------------------------------------- |

Example 3\. Build a named index

Kick off a deferred build using the index name.

```sqlpp
BUILD INDEX ON landmark(idx_landmark_country) USING GSI;
```

Example 4\. Build all indexes

Alternatively, kick off all deferred builds in the keyspace, using a subquery to find the deferred builds.

```sqlpp
BUILD INDEX ON landmark (( (1)
  SELECT RAW name (2)
  FROM system:indexes
  WHERE keyspace_id = 'landmark'
    AND scope_id = 'inventory'
    AND bucket_id = 'travel-sample'
    AND state = 'deferred' ));
```

| **1** | One set of parentheses delimits the whole group of index terms, and another set of parentheses delimits the subquery. In this case there is a double set of parentheses, as the subquery is the only index term. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The RAW keyword forces the subquery to return a flattened array of strings, each of which refers to an index name.                                                                                               |

Note that it is only possible to kick off all deferred builds in a single collection — it is not possible to kick off all deferred builds in all collections in all scopes within a bucket.

Example 5\. Check online index status

Query `system:indexes` for the status of an index.

```sqlpp
SELECT * FROM system:indexes WHERE name="idx_landmark_country";
```

Results

```json
[
  {
    "indexes": {
      "bucket_id": "travel-sample",
      "datastore_id": "http://127.0.0.1:8091",
      "id": "d079aec40eb0c6cc",
      "index_key": [
        "`country`"
      ],
      "keyspace_id": "landmark",
      "name": "idx_landmark_country",
      "namespace_id": "default",
      "scope_id": "inventory",
      "state": "online", (1)
      "using": "gsi"
    }
  }
]
```

| **1** | Note that the index has now been created. |
| ----- | ----------------------------------------- |