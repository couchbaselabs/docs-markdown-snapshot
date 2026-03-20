---
title: UPSERT
description: UPSERT is used to insert a new record or update an existing one.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/upsert.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:n1ql:n1ql-language-reference/upsert.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/upsert.html)

# UPSERT

> UPSERT is used to insert a new record or update an existing one. If the document doesn’t exist it will be created. UPSERT is a combination of INSERT and UPDATE. 

> [!WARNING]
> Please note that the examples on this page will alter the data in your sample buckets. To restore your sample data, remove and reinstall the `travel-sample` bucket. Refer to [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for details.

## [](#prerequisites)Prerequisites

### [](#rbac-privileges)RBAC Privileges

User executing the UPSERT statement must have the _Query Update_ and _Query Insert_ privileges on the target keyspace. If the statement has any RETURNING clauses, then the _Query Select_ privilege is also required on the keyspaces referred in the respective clauses. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

> [!NOTE]
> A user with the _Data Writer_ privilege may set documents to expire. When the document expires, the data service deletes the document, even though the user may not have the _Query Delete_ privilege.

RBAC Examples 

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

To execute the following statement, you must have the _Query Update_ and _Query Insert_ privileges on `hotel`.

```sqlpp
UPSERT INTO hotel (KEY, VALUE)
VALUES ("key1", { "type" : "hotel", "name" : "new hotel" });
```

To execute the following statement, you must have the _Query Update_ and _Query Insert_ privileges on `hotel` and the _Query Select_ privilege on `hotel` also (for RETURNING clause).

```sqlpp
UPSERT INTO hotel (KEY, VALUE)
VALUES ("key1", { "type" : "hotel", "name" : "new hotel" })
RETURNING *;
```

Result

```json
[
  {
    "hotel": {
      "name": "new hotel",
      "type": "hotel"
    }
  }
]
```

To execute the following statement, you must have the _Query Update_ and _Query Insert_ privileges on `landmark` and _Query Select_ privilege on `` `beer-sample` ``.

```sqlpp
UPSERT INTO landmark (KEY foo, VALUE bar)
SELECT META(doc).id AS foo, doc AS bar FROM `beer-sample` AS doc WHERE type = "brewery";
```

## [](#syntax)Syntax

```ebnf
upsert ::= 'UPSERT' 'INTO' target-keyspace ( insert-values | insert-select )
            returning-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/upsert.png) 

| target-keyspace  | [Insert Target](#insert-target)       |
| ---------------- | ------------------------------------- |
| insert-values    | [Insert Values](#insert-values)       |
| insert-select    | [Insert Select](#insert-select)       |
| returning-clause | [RETURNING Clause](#returning-clause) |

### [](#insert-target)Insert Target

```ebnf
target-keyspace ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/target-keyspace.png) 

Specifies the keyspace into which to upsert documents.

| keyspace-ref | [Keyspace Reference](#insert-target-ref) |
| ------------ | ---------------------------------------- |
| alias        | [AS Alias](#insert-target-alias)         |

#### [](#insert-target-ref)Keyspace Reference

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

Keyspace reference for the insert target. For more details, refer to [Keyspace Reference](from.md#from-keyspace-ref).

#### [](#insert-target-alias)AS Alias

Assigns another name to the keyspace reference. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

### [](#insert-values)Insert Values

```ebnf
insert-values ::= ( '(' 'PRIMARY'? 'KEY' ',' 'VALUE' ( ',' 'OPTIONS' )? ')' )? values-clause
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/insert-values.png) 

Specifies one or more documents to be upserted using the VALUES clause. For details, refer to [Insert Values](insert.md#insert-values).

| values-clause | [VALUES Clause](#values-clause) |
| ------------- | ------------------------------- |

#### [](#values-clause)VALUES Clause

```ebnf
values-clause ::= 'VALUES'  '(' key ',' value ( ',' options )? ')'
            ( ',' 'VALUES'? '(' key ',' value ( ',' options )? ')' )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/values-clause.png) 

Specify the values as well-formed JSON. Also enables you to set the [expiration](../../../../java-sdk/current/howtos/kv-operations.md#document-expiration) of the upserted documents. For details, refer to [VALUES Clause](insert.md#values-clause).

> [!NOTE]
> * When updating a document, if the document expiration is not specified, the document expiration is set according to the request-level [preserve\_expiry](../n1ql-manage/query-settings.md#preserve%5Fexpiry) parameter. If this is `true`, the existing document expiration is preserved; if `false`, the document expiration defaults to `0`, meaning the document expiration is the same as the [bucket or collection expiration](../../learn/data/expiration.md).
> * When adding or updating extended attributes (XATTRs), you must provide the complete value for each attribute. You cannot specify or update individual nested fields, as each attribute is updated as a whole. For example, if an existing XATTR named `a` has the value `{"b":1}`, an UPSERT operation with the option `{"xattrs":{"a":{"c":1}}}` completely replaces the value of `a` with `{"c":1}`.

### [](#insert-select)Insert Select

```ebnf
insert-select ::= '(' 'PRIMARY'? 'KEY' key ( ',' 'VALUE' value )?
                   ( ',' 'OPTIONS' options )? ')' select
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/insert-select.png) 

Specifies the documents to be upserted as a SELECT statement. Also enables you to set the [expiration](../../../../java-sdk/current/howtos/kv-operations.md#document-expiration) of the upserted documents. For details, refer to [Insert Select](insert.md#insert-select).

> [!NOTE]
> * When updating a document, if the document expiration is not specified, the document expiration is set according to the request-level [preserve\_expiry](../n1ql-manage/query-settings.md#preserve%5Fexpiry) parameter. If this is `true`, the existing document expiration is preserved; if `false`, the document expiration defaults to `0`, meaning the document expiration is the same as the [bucket or collection expiration](../../learn/data/expiration.md).
> * When adding or updating extended attributes (XATTRs), you must provide the complete value for each attribute. You cannot specify or update individual nested fields, as each attribute is updated as a whole. For example, if an existing XATTR named `a` has the value `{"b":1}`, an UPSERT operation with the option `{"xattrs":{"a":{"c":1}}}` completely replaces the value of `a` with `{"c":1}`.

### [](#returning-clause)RETURNING Clause

```ebnf
returning-clause ::= 'RETURNING' (result-expr (',' result-expr)* |
                    ('RAW' | 'ELEMENT' | 'VALUE') expr)
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/returning-clause.png) 

Specifies the fields that must be returned as part of the results object.

| result-expr | [Result Expression](#result-expr) |
| ----------- | --------------------------------- |

#### [](#result-expr)Result Expression

```ebnf
result-expr ::= ( path '.' )? '*' | expr ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/result-expr.png) 

Specifies an expression on the data you upserted, to be returned as output. For details, refer to [Result Expression](insert.md#result-expr).

## [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

The following statement upserts documents with type `landmark-pub` into the `landmark` keyspace.

Query

```sqlpp
UPSERT INTO landmark (KEY, VALUE)
VALUES ("upsert-1", { "name": "The Minster Inn", "type": "landmark-pub"}),
("upsert-2", {"name": "The Black Swan", "type": "landmark-pub"})
RETURNING VALUE name;
```

Result

```json
[
  "The Minster Inn",
  "The Black Swan"
]
```