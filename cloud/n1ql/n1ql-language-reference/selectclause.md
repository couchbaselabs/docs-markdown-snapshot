---
title: SELECT Clause
description: The SELECT clause determines the result set.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/selectclause.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-language-reference/selectclause.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/selectclause.html)

# SELECT Clause

> The `SELECT` clause determines the result set. 

## [](#section%5FPurpose)Purpose

In a `SELECT` statement, the `SELECT` clause determines the projection (result set).

## [](#section%5FPrerequisites)Prerequisites

To select data from a document or keyspace, your client must have the `query_select` privilege on the document or keyspace. For more details about cluster access privileges, see [Manage Cluster Access Credentials](../../clusters/manage-database-users.md).

## [](#section%5FSyntax)Syntax

```ebnf
select-clause ::= 'SELECT' hint-comment? projection exclude-clause?
```

![Syntax diagram](../_images/n1ql-language-reference/select-clause.png) 

| hint-comment   | [Optimizer Hints](#hint-comment)       |
| -------------- | -------------------------------------- |
| projection     | [Projection](#sec%5FArguments)         |
| exclude-clause | [EXCLUDE Clause](#sec%5FExcludeClause) |

### [](#hint-comment)Optimizer Hints

In Couchbase Capella, you can supply hints to the optimizer within a specially-formatted hint comment. For further details, refer to [Optimizer Hints](optimizer-hints.md).

### [](#sec%5FArguments)Projection

```ebnf
projection ::= ( 'ALL' | 'DISTINCT' )? ( result-expr ( ',' result-expr )* |
               ( 'RAW' | 'ELEMENT' | 'VALUE' ) expr ( 'AS'? alias )? )
```

![Syntax diagram](../_images/n1ql-language-reference/projection.png) 

The projection consists of an optional `ALL` or `DISTINCT` [quantifier](#all-distinct), followed by one of the following alternatives:

* One or more [result expressions](#result-expr), separated by commas.
* A single [raw expression](#raw-element-value), including a [select expression](#field-expr) and an optional [alias](#alias).

#### [](#all-distinct)ALL / DISTINCT

(Optional; default is ALL.)

SELECT ALL retrieves all of the data specified and will result in all of the specified columns, including all duplicates.

SELECT DISTINCT removes duplicate result objects from the query’s result set.

> [!NOTE]
> The DISTINCT clause is not blocking in nature, since it streams the input and produces the output in parallel, while consuming less memory.

In general, `SELECT ALL` results in more returned documents than `SELECT DISTINCT` due to `DISTINCT`'s extra step of removing duplicates. Since `DISTINCT` is purely run in memory, it executes quickly, making the overhead of removing duplicates more noticeable as your recordset gets larger. Refer to [Example 4](#ex-all-distinct).

#### [](#result-expr)Result Expression

```ebnf
result-expr ::= ( path '.' )? '*' | expr ( 'AS'? alias )?
```

![Syntax diagram](../_images/n1ql-language-reference/result-expr.png) 

```ebnf
path ::= identifier ( '[' expr ']' )* ( '.' identifier ( '[' expr ']' )* )*
```

![Syntax diagram](../_images/n1ql-language-reference/path.png) 

The result expression may contain one of the following alternatives:

* A [star expression](#keyspace-name), preceded by an optional path.
* A [select expression](#field-expression), including an optional [alias](#alias).

#### [](#raw-element-value)RAW / ELEMENT / VALUE

(Optional; RAW and ELEMENT and VALUE are synonyms.)

When you specify one or more [result expressions](#result-expr) in the query projection, each result is wrapped in an object, and an implicit or explicit [alias](#alias) is given for each result expression. This extra layer might not be desirable, since it requires extra output parsing.

SELECT RAW reduces the amount of data returned by eliminating the field attribute. The RAW qualifier specifies that the expression that follows should not be wrapped in an object, and the alias for that expression should be suppressed, as shown in [Example 6](#ex-raw-expr) and [Example 7](#ex-raw-field).

The RAW qualifier only enables you to specify a single [select expression](#field-expression). You cannot use the RAW qualifier with a [star expression](#keyspace-name) or with multiple select expressions.

#### [](#keyspace-name)Star Expression (\*)

The star expression `*` enables you to select _all_ the fields from the source specified by the [FROM clause](from.md).

The star expression may be preceded by a [path](nestedops.md), to select all the nested fields from within an array.

> [!NOTE]
> Omitting the keyspace name before a star expression adds the keyspace name to the result set; whereas if you include the keyspace name before a star expression, the keyspace name will not appear in the result set. Refer to [Example 10](#ex-star).

#### [](#field-expression)Select Expression

The select expression is any expression that evaluates to a field to be included in the query’s result set. At its simplest, this may be the name of a field in the data source, such as `id`, `airline`, or `stops`. Refer to [Example 1](#ex-field).

The select expression may include a [path](nestedops.md), to select a nested field from within an array, such as `schedule[0].day`. Refer to [Example 2](#ex-path).

If no field name is specified, the select expression allows you to perform calculations, such as `SELECT 10+20 AS Total;` or any other SQL++ expression. For details with examples, see [SQL++ Expressions](index.md#N1QL%5FExpressions).

#### [](#alias)AS Alias

```ebnf
alias ::= identifier
```

![Syntax diagram](../_images/n1ql-language-reference/alias.png) 

A temporary name of a keyspace name or field name to make names more readable or unique. Refer to [Example 3](#ex-alias).

If you do not explicitly give a field an alias, it is given an _implicit alias_.

* For a field, the implicit alias is the same as the name of the field in the input.
* For a nested path, the implicit alias is defined as the last component in the path.
* For any expression which does not refer to a field, the implicit alias is a dollar sign followed by a number, based on the position of the expression in the projection; for example, `$1`, `$2`, and so on.

An implicit or explicit alias is returned in the result set, unless you suppress it using the [RAW keyword](#raw-element-value).

### [](#sec%5FExcludeClause)EXCLUDE Clause

Couchbase Server 8.0

```ebnf
exclude-clause ::= 'EXCLUDE' exclude-term ( ',' exclude-term )*
```

![Syntax diagram](../_images/n1ql-language-reference/exclude-clause.png) 

The EXCLUDE clause removes specific fields from your query’s result set.

Instead of listing every field you want to include in the SELECT statement, use EXCLUDE to specify only the ones you want to omit. This is particularly useful when you use the star expression (`*`) to select all fields, but want to exclude a few.

The clause consists of one or more [EXCLUDE terms](#exclude-term), separated by commas.

#### [](#exclude-term)EXCLUDE Term

```ebnf
exclude-term ::= identifier | string-expression
```

![Syntax diagram](../_images/n1ql-language-reference/exclude-term.png) 

An EXCLUDE term is a field that you want to exclude from the final projection. It must exactly match the field name or alias as it appears in the projection. Refer to [Example 11](#ex-exclude-clause).

An EXCLUDE term can be:

* An identifier, such as `hotel.name`.
* A string expression with one or more fields separated by commas, such as `"hotel.name, address"`.

> [!NOTE]
> * If the field has an alias, you must use the alias as the term.
> * When your query includes only one FROM term, fields are automatically qualified with it. You can use the field name without the full identifier. For example, `name` instead of `hotel.name`.

## [](#sec%5FBestPractices)Best Practices

When possible, explicitly list all fields you want in your result set instead of using a star expression `*` to select all fields, since the `*` requires an extra trip over your network — one to get the list of field names and one to select the fields.

## [](#sec%5FExamples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Select fields by name

Query

```sqlpp
SELECT id, airline, stops FROM route LIMIT 1;
```

Result

```json
[
  {
    "airline": "AF",
    "id": 10000,
    "stops": 0
  }
]
```

Example 2\. Select field with path

Query

```sqlpp
SELECT schedule[0].day FROM route;
```

Result

```json
[
  {
    "day": 0
  }
]
```

Example 3\. Select field with explicit alias

Query

```sqlpp
SELECT schedule[0].day AS Weekday FROM route LIMIT 1;
```

Result

```json
[
  {
    "Weekday": 0
  }
]
```

Example 4\. SELECT ALL and SELECT DISTINCT

Note that the queries in this example may take some time to run.

| Query 1 SELECT ALL city FROM landmark; slightly slower | Query 2 SELECT DISTINCT city FROM landmark; slightly faster |
| ------------------------------------------------------ | ----------------------------------------------------------- |

When used on a field such as `city`, which contains non-unique values, `SELECT DISTINCT` reduces the recordset to a small fraction of its original size; and while removing so many of the documents takes time, projecting the remaining small fraction is actually slightly faster than the overhead of removing duplicates.

| Query 3 SELECT ALL META().id FROM landmark; much faster | Query 4 SELECT DISTINCT META().id FROM landmark; much slower |
| ------------------------------------------------------- | ------------------------------------------------------------ |

On the other extreme, when used on a field such as `META().id` which contains only unique values, `SELECT DISTINCT` does not reduce the recordset at all, and the overhead of looking for duplicates is wasted effort. In this case, `SELECT DISTINCT` takes about twice as long to execute as `SELECT ALL`.

Example 5\. Query plan using the `DISTINCT` operator

Query

```sqlpp
EXPLAIN SELECT DISTINCT city FROM landmark;
```

Results

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "PrimaryScan3",
          "bucket": "travel-sample",
          "index": "def_inventory_landmark_primary",
          "index_projection": {
            "primary_key": true
          },
          "keyspace": "landmark",
          "namespace": "default",
          "scope": "inventory",
          "using": "gsi"
        },
        {
          "#operator": "Fetch",
          "bucket": "travel-sample",
          "keyspace": "landmark",
          "namespace": "default",
          "scope": "inventory"
        },
        {
          "#operator": "Parallel",
          "~child": {
            "#operator": "Sequence",
            "~children": [
              {
                "#operator": "InitialProject",
                "distinct": true,
                "result_terms": [
                  {
                    "expr": "(`landmark`.`city`)"
                  }
                ]
              },
              {
                "#operator": "Distinct" (1)
              }
            ]
          }
        },
        {
          "#operator": "Distinct" (1)
        }
      ]
    },
    "text": "SELECT DISTINCT city FROM landmark;"
  }
]
```

| **1** | Lines using the DISTINCT operator |
| ----- | --------------------------------- |

Example 6\. SELECT and SELECT RAW with a simple expression

| Query SELECT {"a":1, "b":2};                                               | Query SELECT RAW {"a":1, "b":2};                     |
| -------------------------------------------------------------------------- | ---------------------------------------------------- |
| Results \[   {     "$1": { **(1)**       "a": 1,       "b": 2     }   } \] | Results \[   { **(2)**     "a": 1,     "b": 2   } \] |

| **1** | Added implicit alias |
| ----- | -------------------- |
| **2** | No implicit alias    |

Example 7\. SELECT, SELECT RAW, and SELECT DISTINCT RAW with a field

| Query SELECT city FROM airport ORDER BY city LIMIT 5;                                                                                                                        | Query SELECT RAW city FROM airport ORDER BY city LIMIT 5;                          | Query SELECT DISTINCT RAW city FROM airport ORDER BY city LIMIT 5;                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Results \[   {     "city": "Abbeville"   },   {     "city": "Aberdeen"   },   {     "city": "Aberdeen"   },   {     "city": "Aberdeen"   },   {     "city": "Abilene"   } \] | Results \[   "Abbeville",   "Aberdeen",   "Aberdeen",   "Aberdeen",   "Abilene" \] | Results \[   "Abbeville",   "Aberdeen",   "Abilene",   "Adak Island",   "Addison" \] |

Example 8\. Select all the fields of 1 document from the `airline` keyspace

Query

```sqlpp
SELECT * FROM airline LIMIT 1;
```

Results

```json
[
  {
    "airline": {
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "name": "40-Mile Air",
      "type": "airline"
    }
  }
]
```

Example 9\. Select all the fields of 1 document from the `landmark` keyspace

Query

```sqlpp
SELECT * FROM landmark LIMIT 1;
```

Results

```json
[
  {
    "landmark": {
      "activity": "see",
      "address": "Prince Arthur Road, ME4 4UG",
      "alt": null,
      "city": "Gillingham",
      "content": "Adult - £6.99 for an Adult ticket that allows you to come back for further visits within a year (children's and concessionary tickets also available). Museum on military engineering and the history of the British Empire. A quite extensive collection that takes about half a day to see. Of most interest to fans of British and military history or civil engineering. The outside collection of tank mounted bridges etc can be seen for free. There is also an extensive series of themed special event weekends, admission to which is included in the cost of the annual ticket.",
      "country": "United Kingdom",
      "directions": null,
      "email": null,
      "geo": {
        "accuracy": "RANGE_INTERPOLATED",
        "lat": 51.39184,
        "lon": 0.53616
      },
      "hours": "Tues - Fri 9.00am to 5.00pm, Sat - Sun 11.30am - 5.00pm",
      "id": 10019,
      "image": null,
      "name": "Royal Engineers Museum",
      "phone": "+44 1634 822839",
      "price": null,
      "state": null,
      "title": "Gillingham (Kent)",
      "tollfree": null,
      "type": "landmark",
      "url": "http://www.remuseum.org.uk"
    }
  }
]
```

Example 10\. Star expressions and select expressions with path

Query A

```sqlpp
SELECT * FROM hotel LIMIT 5;
```

Results

```json
[
  {
    "hotel": { (1)
      "address": "Capstone Road, ME7 3JE",
      "alias": null,
      "checkin": null,
// ...
    }
  }
]
```

| **1** | As the star expression does not include the keyspace name, the results are wrapped in an extra object, and the keyspace name is added to each result. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |

Query B

```sqlpp
SELECT hotel.* FROM hotel LIMIT 5;
```

Results

```json
[
  { (1)
    "address": "Capstone Road, ME7 3JE",
    "alias": null,
    "checkin": null,
// ...
  }
]
```

| **1** | As the star expression includes the keyspace name, the keyspace name is not added to the results. |
| ----- | ------------------------------------------------------------------------------------------------- |

Query C

```sqlpp
SELECT meta().id, email, city, phone, hotel.reviews[0].ratings
FROM hotel LIMIT 5;
```

Results

```json
[
  { (1)
    "city": "Medway",
    "email": null,
    "id": "hotel_10025",
    "phone": "+44 870 770 5964",
    "ratings": {
      "Cleanliness": 5,
      "Location": 4,
      "Overall": 4,
      "Rooms": 3,
      "Service": 5,
      "Value": 4
    }
  },
// ...
]
```

| **1** | With a select expression, you may optionally include the keyspace name; in either case, the keyspace name is not added to the results. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------- |

Example 11\. SELECT with an EXCLUDE clause

Query

```sqlpp
SELECT * EXCLUDE reviews,h.public_likes,"geo,description"
FROM `travel-sample`.inventory.hotel h
ORDER BY meta().id LIMIT 1;
```

Results

```json
[
  {
    "h": {
      "address": "Capstone Road, ME7 3JE",
      "alias": null,
      "checkin": null,
      "checkout": null,
      "city": "Medway",
      "country": "United Kingdom",
      "directions": null,
      "email": null,
      "fax": null,
      "free_breakfast": true,
      "free_internet": false,
      "free_parking": true,
      "id": 10025,
      "name": "Medway Youth Hostel",
      "pets_ok": true,
      "phone": "+44 870 770 5964",
      "price": null,
      "state": null,
      "title": "Gillingham (Kent)",
      "tollfree": null,
      "type": "hotel",
      "url": "http://www.yha.org.uk",
      "vacancy": true
    }
  }
]
```

## [](#sec%5FRelatedLinks)Related Links

* [FROM clause](from.md)
* [USE clause](hints.md)
* [LET Clause](let.md)
* [WHERE Clause](where.md)
* [GROUP BY Clause](groupby.md)
* [UNION, INTERSECT, and EXCEPT Clause](union.md)