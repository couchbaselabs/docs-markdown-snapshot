---
title: DELETE
description: DELETE immediately removes the specified document from your keyspace.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/delete.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/delete.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/delete.html)

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
delete ::= 'DELETE' 'FROM' target-keyspace use-keys-clause? where-clause?
            limit-clause? returning-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/delete.png) 

| target-keyspace  | [Delete Target](#delete-target)       |
| ---------------- | ------------------------------------- |
| use-keys-clause  | [Delete Hint](#delete-hint)           |
| where-clause     | [WHERE Clause](#where-clause)         |
| limit-clause     | [LIMIT Clause](#limit-clause)         |
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

You can use a `USE KEYS` hint on the delete target to specify the keys of the data items to be deleted. For details, refer to [USE KEYS Clause](hints.md#use-keys-clause).

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
> Please note that running the following examples will permanently delete your sample data. To restore your sample data, remove and reinstall the `travel-sample` bucket. Refer to [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for details.

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