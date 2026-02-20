---
title: USE Clause
description: The USE clause enables you to specify that the query should use
  particular keys, or a particular index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/hints.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-language-reference/hints.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/hints.html)

# USE Clause

> The `USE` clause enables you to specify that the query should use particular keys, or a particular index. 

## [](#purpose)Purpose

The `USE` clause is used within the [FROM](from.md) clause. It enables you to provide a hint to the query service, specifying that the query should use particular keys, or a particular index.

> [!TIP]
> You can also supply an index hint within a specially-formatted [hint comment](optimizer-hints.md). Note that you cannot specify an index hint for the same keyspace using both the `USE` clause and a hint comment. If you do this, the `USE` clause and the hint comment are both marked as erroneous and ignored by the optimizer.

## [](#prerequisites)Prerequisites

To select data from a document or keyspace, your client must have the `query_select` privilege on the document or keyspace. For more details about cluster access privileges, see [Manage Cluster Access Credentials](../../clusters/manage-database-users.md).

## [](#syntax)Syntax

```ebnf
use-clause ::= use-keys-clause | use-index-clause
```

![Syntax diagram](../_images/n1ql-language-reference/use-clause.png) 

| use-keys-clause  | [USE KEYS Clause](#use-keys-clause)   |
| ---------------- | ------------------------------------- |
| use-index-clause | [USE INDEX clause](#use-index-clause) |

## [](#use-keys-clause)USE KEYS Clause

### [](#purpose-2)Purpose

You can refer to a document’s unique document key by using the `USE KEYS` clause. Only documents having those document keys will be included as inputs to a query.

There is no optimizer hint equivalent to this clause.

### [](#syntax-2)Syntax

```ebnf
use-keys-clause ::= 'USE' use-keys-term
```

![Syntax diagram](../_images/n1ql-language-reference/use-keys-clause.png) 

```ebnf
use-keys-term ::= 'PRIMARY'? 'KEYS' expr
```

![Syntax diagram](../_images/n1ql-language-reference/use-keys-term.png) 

Synonym: `USE KEYS` and `USE PRIMARY KEYS` are synonyms.

| expr | String of a document key or an array of comma-separated document keys. |
| ---- | ---------------------------------------------------------------------- |

### [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Select a single document by its document key

```sqlpp
SELECT *
FROM airport
USE KEYS "airport_1254";
```

Results

```JSON
[
  {
    "travel-sample": {
      "airportname": "Calais Dunkerque",
      "city": "Calais",
      "country": "France",
      "faa": "CQF",
      "geo": {
        "alt": 12,
        "lat": 50.962097,
        "lon": 1.954764
      },
      "icao": "LFAC",
      "id": 1254,
      "type": "airport",
      "tz": "Europe/Paris"
    }
  }
]
```

Example 2\. Select multiple documents by their document keys

```sqlpp
SELECT *
FROM airport
USE KEYS ["airport_1254","airport_1255"];
```

Results

```JSON
[
  {
    "travel-sample": {
      "airportname": "Calais Dunkerque",
      "city": "Calais",
      "country": "France",
      "faa": "CQF",
      "geo": {
        "alt": 12,
        "lat": 50.962097,
        "lon": 1.954764
      },
      "icao": "LFAC",
      "id": 1254,
      "type": "airport",
      "tz": "Europe/Paris"
    }
  },
  {
    "travel-sample": {
      "airportname": "Peronne St Quentin",
      "city": "Peronne",
      "country": "France",
      "faa": null,
      "geo": {
        "alt": 295,
        "lat": 49.868547,
        "lon": 3.029578
      },
      "icao": "LFAG",
      "id": 1255,
      "type": "airport",
      "tz": "Europe/Paris"
    }
  }
]
```

## [](#use-index-clause)USE INDEX clause

### [](#purpose-3)Purpose

Use the `USE INDEX` clause to specify the index or indexes to be used as part of the query execution. The query engine attempts to use a specified index if the index is applicable for the query.

If necessary, you can omit the index name and just specify the index type. In this case, the query service considers all the available indexes of the specified type.

This clause is equivalent to the `INDEX` and `INDEX_FTS` optimizer hints. For more details, refer to [Keyspace Hints](keyspace-hints.md).

If you attempt to use an index which is still scheduled for background creation, the request fails.

### [](#syntax-3)Syntax

```ebnf
use-index-clause ::= 'USE' use-index-term
```

![Syntax diagram](../_images/n1ql-language-reference/use-index-clause.png) 

```ebnf
use-index-term ::= 'INDEX' '(' index-ref ( ',' index-ref )* ')'
```

![Syntax diagram](../_images/n1ql-language-reference/use-index-term.png) 

```ebnf
index-ref ::= index-name? index-type?
```

![Syntax diagram](../_images/n1ql-language-reference/index-ref.png) 

| index-name | \[Optional\] String or expression representing an index to be used for the query. This argument is optional; if omitted, the query engine considers all available indexes of the specified index type. |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| index-type | [USING clause](#index-type)                                                                                                                                                                            |

#### [](#index-type)USING clause

```ebnf
index-type ::= 'USING' ( 'GSI' | 'FTS' )
```

![Syntax diagram](../_images/n1ql-language-reference/index-type.png) 

Specifies which index form to use.

`USING GSI`

A Global Secondary Index, which lives on an index node and can possibly be separate from a data node.

`USING FTS`

A Full Text Search index, for use with queries containing [Search functions](searchfun.md). You can use this hint to specify that the query is a [Flex Index](flex-indexes.md) query using a Full Text Search index.

This clause is optional; if omitted, the default is `USING GSI`.

### [](#examples-2)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 3\. Use a specified Global Secondary Index

This example uses the index `def_inventory_route_route_src_dst_day`, which is installed with the `travel-sample` bucket.

The following query hints that the optimizer should select the specified index for the keyspace `route`.

INDEX hint

```sqlpp
SELECT id FROM route
USE INDEX (def_inventory_route_route_src_dst_day USING GSI)
WHERE sourceairport = "SFO"
LIMIT 1;
```

Example 4\. Use any suitable Full Text Search index

Specify that the query service should prefer an FTS index, without specifying the index by name. To qualify for this query, there must be an FTS index on state and type, using the keyword analyzer. (Or alternatively, an FTS index on state, with a custom type mapping on "hotel".)

```sqlpp
SELECT META().id
FROM hotel USE INDEX (USING FTS)
WHERE state = "Corse" OR state = "California";
```

All FTS indexes are considered. If a qualified FTS index is available, it is selected for the query. If none of the available FTS indexes are qualified, the available GSI indexes are considered instead.

## [](#related-links)Related Links

* [ANSI JOIN Hints](join.md#ansi-join-hints)
* [Optimizer Hints](optimizer-hints.md)