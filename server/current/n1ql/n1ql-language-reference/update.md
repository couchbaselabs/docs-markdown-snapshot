---
title: UPDATE
description: UPDATE replaces a document that already exists with updated values.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/update.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/n1ql/n1ql-language-reference/update.html)

# UPDATE

> UPDATE replaces a document that already exists with updated values. 

> [!WARNING]
> Please note that the examples on this page will alter the data in your sample buckets. To restore your sample data, remove and reinstall the `travel-sample` bucket. Refer to [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for details.

## [](#prerequisites)Prerequisites

### [](#rbac-privileges)RBAC Privileges

User executing the UPDATE statement must have the _Query Update_ privilege on the target keyspace. If the statement has any clauses that needs data read, such as SELECT clause, or RETURNING clause, then _Query Select_ privilege is also required on the keyspaces referred in the respective clauses. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

> [!NOTE]
> A user with the _Data Writer_ privilege may set documents to expire. When the document expires, the data service deletes the document, even though the user may not have the _Query Delete_ privilege.

RBAC Examples 

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

To execute the following statement, you must have the _Query Update_ privilege on `airport`.

```sqlpp
UPDATE airport SET foo = 5;
```

To execute the following statement, you must have the _Query Update_ privilege on `airport` and _Query Select_ privilege on `` `beer-sample` ``.

```sqlpp
UPDATE airport
SET foo = 9
WHERE city IN (SELECT RAW city FROM `beer-sample` WHERE type = "brewery");
```

To execute the following statement, you must have the _Query Update_ and _Query Select_ privileges on `airport`.

```sqlpp
UPDATE airport
SET city = "San Francisco"
WHERE lower(city) = "san francisco"
RETURNING *;
```

## [](#syntax)Syntax

```ebnf
update ::= 'UPDATE' hint-comment? target-keyspace use-keys? set-clause? unset-clause?
            where-clause? limit-clause? returning-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/update.png) 

| hint-comment     | [Optimizer Hints](#hint-comment)      |
| ---------------- | ------------------------------------- |
| target-keyspace  | [Update Target](#update-target)       |
| use-keys         | [USE KEYS Clause](#update-hint)       |
| set-clause       | [SET Clause](#set-clause)             |
| unset-clause     | [UNSET Clause](#unset-clause)         |
| where-clause     | [WHERE Clause](#where-clause)         |
| limit-clause     | [LIMIT Clause](#limit-clause)         |
| returning-clause | [RETURNING Clause](#returning-clause) |

### [](#hint-comment)Optimizer Hints

Couchbase Server 8.0

You can supply hints to the optimizer within a specially formatted hint comment. For more information, see [Optimizer Hints](optimizer-hints.md).

> [!NOTE]
> UPDATE statements support only index hints. Other hints, such as join hints and ORDERED hints, are not supported. For an example of using an optimizer hint, see [Example 12](#example-12).

### [](#update-target)Update Target

```ebnf
target-keyspace ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/target-keyspace.png) 

The update target is the keyspace which you want to update.

| keyspace-ref | [Keyspace Reference](#keyspace-ref) |
| ------------ | ----------------------------------- |
| alias        | [AS Alias](#update-alias)           |

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

Keyspace reference for the update target. For more details, refer to [Keyspace Reference](from.md#from-keyspace-ref).

#### [](#update-alias)AS Alias

Assigns another name to the keyspace reference. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

### [](#update-hint)USE KEYS Clause

You can use a `USE KEYS` hint on the update target to specify the keys of the data items to be updated. For details, refer to [USE KEYS Clause](hints.md#use-keys-clause).

> [!NOTE]
> You cannot specify a hint for the same update target using both the USE KEYS clause and an [optimizer hint](#hint-comment). If you do this, the USE KEYS clause and the [optimizer hint](#hint-comment) are both marked as erroneous and ignored by the optimizer.

### [](#set-clause)SET Clause

```ebnf
set-clause ::= 'SET' ( path '=' expr update-for? | meta '=' ( expiration | xattrs ) )
               ( ',' ( path '=' expr update-for? | meta '=' ( expiration | xattrs ) ) )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/set-clause.png) 

Specifies the value for an attribute to be changed.

| path       | A [path](#path) specifying the attribute to be changed.                                                          |
| ---------- | ---------------------------------------------------------------------------------------------------------------- |
| expr       | The value may be a generic expression term, a subquery, or an expression that resolves to nested array elements. |
| update-for | [FOR Clause](#update-for)                                                                                        |

The SET clause also supports alternative arguments which enable you to set the expiration and extended attributes of the document.

| meta | A META() expression specifying the document metadata. To set the expiration property, use [META().expiration](metafun.md#meta). To set extended attributes (XATTR), use [META().xattrs.<attribute>\[.<path>\]](metafun.md#meta) expiration An integer, or an expression resolving to an integer, representing the [document expiration](../../../../java-sdk/current/howtos/kv-operations.md#document-expiration) in seconds. If the document expiration is not specified, the document expiration is set according to the request-level [preserve\_expiry](../n1ql-manage/query-settings.md#preserve%5Fexpiry) parameter. If this is true, the existing document expiration is preserved; if false, the document expiration defaults to 0, meaning the document expiration is the same as the [bucket or collection expiration](../../learn/data/expiration.md). xattrs An object containing one or more extended attribute (XATTR) names as top-level keys and their corresponding JSON values. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#unset-clause)UNSET Clause

```ebnf
unset-clause ::= 'UNSET' ( path update-for? | meta-xattr ) ( ',' ( path update-for? | meta-xattr ) )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/unset-clause.png) 

Removes the specified attribute from the document.

| path       | A [path](#path) specifying the attribute to be removed.                                                                                                                                                                                                                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| update-for | [FOR Clause](#update-for)                                                                                                                                                                                                                                                                                                                                                       |
| meta-xattr | An expression specifying the extended attribute (XATTR) to be removed. The format is [META().xattrs.<attribute>\[.<path>\]](metafun.md#meta), where: <attribute> is a top-level attribute name or key of the XATTR object. <path> is an optional subpath within that attribute. You can directly reference individual fields in composite XATTR values through the nested path. |

> [!NOTE]
> You cannot use the UNSET clause to unset the document expiration. To unset the document expiration, set the document expiration to `0`. Alternatively, if the request-level [preserve\_expiry](../n1ql-manage/query-settings.md#preserve%5Fexpiry) parameter is set to `false`, simply update the document without specifying the document expiration.

### [](#update-for)FOR Clause

```ebnf
update-for ::= ('FOR' (name-var ':')? var ('IN' | 'WITHIN') path
               (','   (name-var ':')? var ('IN' | 'WITHIN') path)* )+
               ('WHEN' cond)? 'END'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/update-for.png) 

```ebnf
path ::= identifier ( '[' expr ']' )* ( '.' identifier ( '[' expr ']' )* )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/path.png) 

Uses the FOR statement to iterate over a nested array to SET or UNSET the given attribute for every matching element in the array. The FOR clause can evaluate functions and expressions, and the UPDATE statement supports multiple nested FOR expressions to access and update fields in nested arrays. Additional array levels are supported by chaining the FOR clauses.

### [](#where-clause)WHERE Clause

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/where-clause.png) 

Specifies the condition that needs to be met for data to be updated. Optional.

### [](#limit-clause)LIMIT Clause

```ebnf
limit-clause ::= 'LIMIT' expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/limit-clause.png) 

Specifies the greatest number of objects that can be updated. This clause must have a non-negative integer as its upper bound. Optional.

### [](#returning-clause)RETURNING Clause

```ebnf
returning-clause ::= 'RETURNING' (result-expr (',' result-expr)* |
                    ('RAW' | 'ELEMENT' | 'VALUE') expr)
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/returning-clause.png) 

Specifies the information to be returned by the operation as a query result. For more details, refer to [RETURNING Clause](insert.md#returning-clause).

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

> [!NOTE]
> For some of these examples, the Query Workbench may warn you that the query has no WHERE clause and will update all documents. In this case, you can ignore the warning: the USE KEYS hint in these examples ensures that the query updates only one document.

Example 1\. Set an attribute

The following statement sets the nickname of the landmark "Tradeston Pedestrian Bridge" to "Squiggly Bridge".

```sqlpp
UPDATE landmark
USE KEYS "landmark_10090"
SET nickname = "Squiggly Bridge"
RETURNING landmark.nickname;
```

```json
[
  {
    "nickname": "Squiggly Bridge"
  }
]
```

Example 2\. Unset an attribute

This statement removes the `nickname` attribute from the `landmark` keyspace for the document with the key `landmark_10090`.

```sqlpp
UPDATE landmark
USE KEYS "landmark_10090"
UNSET nickname
RETURNING landmark.name;
```

```json
[
  {
    "name": "Tradeston Pedestrian Bridge"
  }
]
```

Example 3\. Set attributes in an array

This statement sets the `codeshare` attribute for each element in the `schedule` array for document `route_10003` in the `route` keyspace.

```sqlpp
UPDATE route t
USE KEYS "route_10003"
SET s.codeshare = NULL FOR s IN schedule END
RETURNING t;
```

```json
[
  {
    "t": {
      "airline": "AF",
      "airlineid": "airline_137",
      "destinationairport": "ATL",
      "distance": 654.9546621929924,
      "equipment": "757 739",
      "id": 10003,
      "schedule": [
        {
          "codeshare": null,
          "day": 0,
          "flight": "AF986",
          "utc": "22:26:00"
        },
        {
          "codeshare": null,
          "day": 0,
          "flight": "AF962",
          "utc": "04:25:00"
        },
// ...
      ],
      "sourceairport": "TPA",
      "stops": 0,
      "type": "route"
    }
  }
]
```

Example 4\. Set nested array elements

```sqlpp
UPDATE hotel AS h USE KEYS "hotel_10025"
SET i.ratings = OBJECT_ADD(i.ratings, "new", "new_value" ) FOR i IN reviews END
RETURNING h.reviews[*].ratings;
```

```json
[
  {
    "ratings": [
      {
        "Cleanliness": 5,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 5,
        "Value": 4,
        "new": "new_value"
      },
      {
        "Business service (e.g., internet access)": 4,
        "Check in / front desk": 4,
        "Cleanliness": 4,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 3,
        "Value": 5,
        "new": "new_value"
      }
    ]
  }
]
```

Example 5\. Access nested arrays

Query

```sqlpp
UPDATE hotel AS h USE KEYS "hotel_10025"
UNSET i.new FOR i IN
  (ARRAY j.ratings FOR j IN reviews END)
END
RETURNING h.reviews[*].ratings;
```

Result

```json
[
  {
    "ratings": [
      {
        "Cleanliness": 5,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 5,
        "Value": 4
      },
      {
        "Business service (e.g., internet access)": 4,
        "Check in / front desk": 4,
        "Cleanliness": 4,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 3,
        "Value": 5
      }
    ]
  }
]
```

Example 6\. Update a document with the results of a subquery

Query

```sqlpp
UPDATE airport AS a
SET hotels =
  (SELECT  h.name, h.id
  FROM  hotel AS h
  WHERE h.city = "Nice")
WHERE a.faa ="NCE"
RETURNING a;
```

Result

```json
[
  {
    "a": {
      "airportname": "Cote D\\'Azur",
      "city": "Nice",
      "country": "France",
      "faa": "NCE",
      "geo": {
        "alt": 12,
        "lat": 43.658411,
        "lon": 7.215872
      },
      "hotels": [
        {
          "id": 20419,
          "name": "Best Western Hotel Riviera Nice"
        },
        {
          "id": 20420,
          "name": "Hotel Anis"
        },
        {
          "id": 20421,
          "name": "NH Nice"
        },
        {
          "id": 20422,
          "name": "Hotel Suisse"
        },
        {
          "id": 20423,
          "name": "Gounod"
        },
        {
          "id": 20424,
          "name": "Grimaldi Hotel Nice"
        },
        {
          "id": 20425,
          "name": "Negresco"
        }
      ],
      "icao": "LFMN",
      "id": 1354,
      "type": "airport",
      "tz": "Europe/Paris"
    }
  }
]
```

Example 7\. Update a document and set expiration

Update a document and set the expiration to 1 week.

Query

```sqlpp
UPDATE route t USE KEYS "route_10003"
SET meta(t).expiration = 7*24*60*60,
s.codeshare = NULL FOR s IN schedule END;
```

Example 8\. Update a document and preserve expiration

Query

```sqlpp
UPDATE route t USE KEYS "route_10003"
SET meta(t).expiration = meta(t).expiration,
s.codeshare = NULL FOR s IN schedule END;
```

Note that it is possible to preserve the document expiration using the request-level [preserve\_expiry](../n1ql-manage/query-settings.md#preserve%5Fexpiry) parameter.

Example 9\. Update a document and unset expiration

Set the document expiration to 0 to unset the document expiration. (In this case, the document expiration defaults to be the same as the bucket or collection expiration.)

Query

```sqlpp
UPDATE route t USE KEYS "route_10003"
SET meta(t).expiration = 0,
s.codeshare = NULL FOR s IN schedule END;
```

Alternatively, if the request-level [preserve\_expiry](../n1ql-manage/query-settings.md#preserve%5Fexpiry) parameter is set to `false`, and you update the document without specifying the document expiration, the document expiration defaults to 0.

Query

```sqlpp
UPDATE route t USE KEYS "route_10003"
SET s.codeshare = NULL FOR s IN schedule END;
```

Example 10\. Update a document and set an extended attribute (XATTR)

Query

```sqlpp
UPDATE airport AS a
SET META(a).xattrs.metadata = {
    "lastUpdatedBy": "Admin",
    "reviewed": true,
    "notes": "Updated terminal info"
}
WHERE a.faa = "SFO"
RETURNING a;
```

Result

```json
[{
  "a": {
      "airportname": "San Francisco Intl",
      "city": "San Francisco",
      "country": "United States",
      "faa": "SFO",
      "geo": {
          "alt": 13,
          "lat": 37.618972,
          "lon": -122.374889
      },
      "icao": "KSFO",
      "id": 3469,
      "type": "airport",
      "tz": "America/Los_Angeles"
  }
}]
```

Example 11\. Update a document and unset an extended attribute (XATTR)

Query

```sqlpp
UPDATE airport AS a
UNSET META(a).xattrs.metadata
WHERE a.faa = "SFO";
```

Example 12\. Update with an optimizer hint

The following query hints the optimizer to use the index `def_inventory_airport_city` for the keyspace `airport`.

```sqlpp
UPDATE /*+ INDEX(airport def_inventory_airport_city) */ airport 
SET updated = true 
WHERE city = "San Jose";
```

If you examine the plan for this query, you can see that it uses the suggested index.

Result

```json
"#operator": "IndexScan3",
"bucket": "travel-sample",
"index": "def_inventory_airport_city",
"index_id": "34798b782a732137",
```