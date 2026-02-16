[View original HTML](/cloud/n1ql/n1ql-language-reference/createscope.html)

> The `CREATE SCOPE` statement enables you to create a scope. 

## [](#syntax)Syntax

```ebnf
create-scope ::= 'CREATE' 'SCOPE' ( namespace ':' )? bucket '.' scope ( 'IF' 'NOT' 'EXISTS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/create-scope.png) 

| namespace | (Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket in which you want to create the scope. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket    | (Required) An [identifier](identifiers.md) that refers to the bucket in which you want to create the scope.                                                                                                                                                                                                                      |
| scope     | (Required) An [identifier](identifiers.md) that refers to the name of the scope that you want to create. Refer to [Naming for Scopes and Collections](../../../server/current/learn/data/scopes-and-collections.md#naming-for-scopes-and-collections) for restrictions on scope names.                                           |

|  | If there is a hyphen (-) inside the bucket name or the scope name, you must wrap that part of the path in backticks (\` \`). For example, default:\`travel-sample\` indicates the travel-sample keyspace in the default namespace. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

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

* For an overview of scopes and collections, see [Buckets, Scopes, and Collections](../../clusters/data-service/about-buckets-scopes-collections.md).
* For step-by-step management procedures, see [Manage Scopes and Collections](../../clusters/data-service/scopes-collections.md).
* To manage scopes and collections with the Management API, see [Buckets, Scopes, and Collections](../../management-api-reference/index.md#tag/Buckets-Scopes-and-Collections).
* To manage scopes and collections with the Couchbase Shell, see [Couchbase Shell Documentation](https://couchbase.sh/docs/).