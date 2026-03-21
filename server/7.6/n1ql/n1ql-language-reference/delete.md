---
title: DELETE
description: DELETE immediately removes the specified document from your keyspace.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/delete.adoc
pubDate: 2026-03-21T03:36:33.505Z
link: xref:7.6@server:n1ql:n1ql-language-reference/delete.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/delete.html)

# DELETE

DELETE immediately removes the specified document from your keyspace.

## [](#prerequisites)Prerequisites

### [](#rbac-privileges)RBAC Privileges

To execute the DELETE statement, you must have the _Query Delete_ privilege granted on the target keyspace. If the statement has any RETURNING clauses that need data read, then the _Query Select_ privilege is also required on the keyspaces referred in the respective clauses. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

RBAC Examples 

| Delete Query Contains | Query Delete Permissions Needed | Query Select Permissions Needed | Example          |
| --------------------- | ------------------------------- | ------------------------------- | ---------------- |
| WHERE clause          | Yes                             | No                              | [Example 1](#Q1) |
| Subquery              | Yes                             | Yes                             | [Example 2](#Q2) |
| RETURNING clause      | Yes                             | Yes                             | [Example 3](#Q3) |

## [](#syntax)Syntax

```ebnf
delete ::= 'DELETE' 'FROM' target-keyspace use-clause? where-clause?
            limit-clause? offset-clause? returning-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/delete.png) 

| target-keyspace  | [Delete Target](#delete-target)       |
| ---------------- | ------------------------------------- |
| use-clause       | [Delete Hint](#delete-hint)           |
| where-clause     | [WHERE Clause](#where-clause)         |
| limit-clause     | [LIMIT Clause](#limit-clause)         |
| offset-clause    | [OFFSET Clause](#offset-clause)       |
| returning-clause | [RETURNING Clause](#returning-clause) |

### [](#delete-target)Delete Target

```ebnf
target-keyspace ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/target-keyspace.png) 

Specifies the data source from which to delete the document.

| keyspace-ref | [Keyspace Reference](#keyspace-ref) |
| ------------ | ----------------------------------- |
| alias        | [AS Alias](#delete-alias)           |

#### [](#keyspace-ref)Keyspace Reference

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

Keyspace reference for the delete target. For more details, refer to [Keyspace Reference](from.md#from-keyspace-ref).

#### [](#delete-alias)AS Alias

Assigns another name to the keyspace reference. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

### [](#delete-hint)Delete Hint

You can use a `USE` clause to provide hints for the delete target.

The clause supports the following hints:

* `USE KEYS`: Specifies the keys of the data items to delete.
* `USE INDEX`: Specifies the index to use for the delete operation.

For more information, see [USE Clause](hints.md).

### [](#where-clause)WHERE Clause

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/where-clause.png) 

Specifies the condition that needs to be met for data to be deleted. Optional.

### [](#limit-clause)LIMIT Clause

```ebnf
limit-clause ::= 'LIMIT' expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/limit-clause.png) 

Specifies the greatest number of objects that can be deleted. This clause must have a non-negative integer as its upper bound. Optional.

### [](#offset-clause)OFFSET Clause

```ebnf
offset-clause ::= 'OFFSET' expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/offset-clause.png) 

Like the [OFFSET clause](offset.md) for a SELECT query, you can include an OFFSET clause in a DELETE statement to specify a number of objects to skip before beginning the deletion. This option can be useful for parallelizing a large delete operation.

You can include the OFFSET clause either before or after the optional LIMIT clause. The position has no effect on the result.

The expression for this clause must be a non-negative integer. Optional.

### [](#returning-clause)RETURNING Clause

```ebnf
returning-clause ::= 'RETURNING' (result-expr (',' result-expr)* |
                    ('RAW' | 'ELEMENT' | 'VALUE') expr)
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/returning-clause.png) 

Specifies the information to be returned by the operation as a query result. For more details, refer to [RETURNING Clause](insert.md#returning-clause).

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

> [!WARNING]
> Be aware that running the following examples will permanently delete your sample data. To restore your sample data, remove and reinstall the `travel-sample` bucket. Refer to [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for details.

Example 1\. Delete query containing a WHERE clause

This example requires the _Query Delete_ privilege on `hotel`.

```sqlpp
DELETE FROM hotel;
```

Example 2\. Delete queries containing a subquery

This example requires the _Query Delete_ privilege on `airport` and the _Query Select_ privilege on `` `beer-sample` ``.

```sqlpp
DELETE FROM airport
WHERE city IN (SELECT raw city FROM `beer-sample` WHERE city IS NOT MISSING)
RETURNING airportname;
```

This example requires the _Query Delete_ and _Query Select_ privileges on `airport`.

```sqlpp
DELETE FROM airport
WHERE city IN (SELECT RAW MAX(t.city) FROM airport AS t)
RETURNING airportname;
```

Example 3\. Delete queries containing a RETURNING clause

These examples require the _Query Delete_ and _Query Select_ privileges on `hotel`.

```sqlpp
DELETE FROM hotel RETURNING *;
```

```sqlpp
DELETE FROM hotel
WHERE city = "San Francisco"
RETURNING meta().id;
```

Example 4\. Delete by key

This example deletes the document `airline_4444`.

```sqlpp
DELETE FROM airline k
USE KEYS "airline_4444"
RETURNING k
```

Results

```json
[
  {
    "k": {
      "callsign": "MY-AIR",
      "country": "United States",
      "iata": "Z1",
      "icao": "AQZ",
      "name": "80-My Air",
      "id": "4444",
      "type": "airline"
    }
  }
]
```

Example 5\. Delete by filter

This example deletes the airline with the callsign "AIR-X".

```sqlpp
DELETE FROM airline f
WHERE f.callsign = "AIR-X"
RETURNING f.id
```

Results

```json
[
  {
    "id": "4445"
  }
]
```

Example 6\. Delete with LIMIT and OFFSET

This example deletes a subset of the airlines with a country of "France'. First, you query to get a list of the airlines in France.

```sqlpp
SELECT id FROM airline 
WHERE country="France";
```

There are 21 documents in this collection with `country="France"`.

Results

```text
[
    {
      "id": 1191
    },
    {
      "id": 1203
    },
    {
      "id": 137
    },
    {
      "id": 139
    },
    {
      "id": 13947
    },
    {
      "id": 1523
    },
    {
      "id": 16837
    },
    {
      "id": 1908
    },
    {
      "id": 1909
    },
    {
      "id": 21     (1)
    },
    {
      "id": 225
    },
    {
      "id": 2704
    },
    {
      "id": 2757
    },
    {
      "id": 4299
    },
    {
      "id": 477
    },
    {
      "id": 4965
    },
    {
      "id": 547
    },
    {
      "id": 5479
    },
    {
      "id": 551
    },
    {
      "id": 567    (2)
    },
    {
      "id": 8745
    }
  ]
```

| **1** | The 10th document’s id. |
| ----- | ----------------------- |
| **2** | The 20th document’s id. |

Next, you specify that you want to delete up to 10 documents, after skipping the first 10.

```sqlpp
DELETE FROM airline 
WHERE country="France"
LIMIT 10 OFFSET 10;

SELECT id FROM airline 
WHERE country="France";
```

Now there are 11 documents in this collection with `country="France"`.

Results

```text
[
    {
      "id": 1191
    },
    {
      "id": 1203
    },
    {
      "id": 137
    },
    {
      "id": 139
    },
    {
      "id": 13947
    },
    {
      "id": 1523
    },
    {
      "id": 16837
    },
    {
      "id": 1908
    },
    {
      "id": 1909
    },
    {
      "id": 21   (1)
    },
    {
      "id": 8745 (2)
    }
  ]
```

| **1** | Documents with the first 10 ids—​the offset—​remain in the airline collection.     |
| ----- | ---------------------------------------------------------------------------------- |
| **2** | After deleting 10 documents—​the limit—​1 more document remains in the collection. |

Example 7\. Delete query with a USE INDEX clause

The following query hints the Query Service to use the index, `def_inventory_hotel_city`.

```sqlpp
DELETE FROM `hotel`
USE INDEX (def_inventory_hotel_city)
WHERE city = "San Francisco";
```

If you examine the plan for this query, you can see that the query uses the suggested index.

Results

```json
"index": "def_inventory_hotel_city",
"index_id": "c31e7f44f9ff274c",
"keyspace": "hotel",
"namespace": "default",
```