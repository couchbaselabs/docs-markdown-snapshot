[View original HTML](/server/current/n1ql/n1ql-language-reference/from.html)

> The `FROM` clause specifies the documents to be used as the input for a query. 

## [](#purpose)Purpose

The `FROM` clause is used within a [SELECT](selectclause.md) query or [subquery](subqueries.md). It specifies the documents to be used as the input for a query.

## [](#prerequisites)Prerequisites

For you to select data from keyspace or expression, you must have the `query_select` privilege on that keyspace. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
from-clause ::= 'FROM' from-terms
```

![Syntax diagram](../_images/n1ql-language-reference/from-clause.png) 

### [](#section%5Fnkd%5F3nx%5F1db)FROM Terms

```ebnf
from-terms ::= ( from-keyspace | from-subquery | from-generic )
               ( join-clause | nest-clause | unnest-clause )* comma-separated-join*
```

![Syntax diagram](../_images/n1ql-language-reference/from-terms.png) 

The first FROM term may be any of the following:

* A [keyspace reference](#sec%5Ffrom-keyspace)
* A [subquery](#select-expr) (such as derived tables)
* A [generic expression](#generic-expr) (nested paths, `CURL()`, or other expressions)

This may be followed by further FROM terms, each of which may be one of the following:

* A [JOIN](join.md) clause and conditions
* A [NEST](nest.md) clause and conditions
* An [UNNEST](unnest.md) clause and conditions

You may additionally include one or more [comma-separated joins](comma.md).

|  | JOIN clauses, NEST clauses, UNNEST clauses, and comma-separated joins each have a _left-hand side_ and a _right-hand side_. The left-hand side is defined by the preceding FROM term; the right-hand side is defined by the FROM term itself. When you chain multiple FROM terms together, the right-hand side of one FROM term acts as the left-hand side of the following FROM term. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#limitations)Limitations

* When the FROM term is an expression, `USE KEYS` or `USE INDEX` clauses are not allowed.
* When using a lookup `JOIN` clause, an index `JOIN` clause, a `NEST` clause, or an `UNNEST` clause, the left-hand side of the join may be a keyspace identifier, an expression, or a subquery; but the right-hand side may only be a keyspace identifier.
* When using an ANSI `JOIN` clause, the right-hand side of the join may also be a keyspace identifier, an expression, or a subquery, similar to the left-hand side.
* You can chain comma-separated joins with ANSI `JOIN` clauses, ANSI `NEST` clauses, and `UNNEST` clauses. However, you cannot chain comma-separated joins with lookup `JOIN` and `NEST` clauses, or index `JOIN` and `NEST` clauses.
* The right-hand side of a comma-separated join can only be a keyspace identifier, a subquery, or a generic expression. This means that comma-separated joins must come _after_ any `JOIN`, `NEST`, or `UNNEST` clauses.

## [](#sec%5Ffrom-keyspace)FROM Keyspace

The FROM keyspace specifies a keyspace to query from: either a specific keyspace or a constant expression.

### [](#syntax-2)Syntax

```ebnf
from-keyspace ::= keyspace-ref ( 'AS'? alias )? use-clause?
```

![Syntax diagram](../_images/n1ql-language-reference/from-keyspace.png) 

| keyspace-ref | [Keyspace Reference](#from-keyspace-ref) |
| ------------ | ---------------------------------------- |
| alias        | [AS Alias](#from-keyspace-alias)         |
| use-clause   | [USE Clause](#from-keyspace-hints)       |

#### [](#from-keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram](../_images/n1ql-language-reference/keyspace-ref.png) 

| keyspace-path    | [Keyspace Path](#keyspace-path)       |
| ---------------- | ------------------------------------- |
| keyspace-partial | [Keyspace Partial](#keyspace-partial) |

Keyspace reference of the data source. The identifiers that make up the keyspace reference are not available as [variables in scope of a subquery](subqueries.md#section%5Fonz%5F3tj%5Fmz).

|  | If there is a hyphen (-) inside any part of the keyspace reference, you must wrap that part of the keyspace reference in backticks (\` \`). Refer to the examples below. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

#### [](#keyspace-path)Keyspace Path

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram](../_images/n1ql-language-reference/keyspace-path.png) 

If the keyspace is a named collection, or the default collection in the default scope within a bucket, the keyspace reference may be a keyspace path. In this case, the [query context](../n1ql-intro/queriesandresults.md#query-context) should not be set.

namespace

(Optional) An [identifier](identifiers.md) that refers to the [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. Currently, only the `default` namespace is available. If the namespace name is omitted, the default namespace in the current session is used.

bucket

(Required) An [identifier](identifiers.md) that refers to the [bucket name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.

scope

(Optional) An [identifier](identifiers.md) that refers to the [scope name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the bucket’s default scope is used.

collection

(Optional) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace. If omitted, the default collection in the bucket’s default scope is used.

For example, `` default:`travel-sample` `` indicates the default collection in the default scope in the `travel-sample` bucket in the `default` namespace.

Similarly, `` default:`travel-sample`.inventory.airline `` indicates the `airline` collection in the `inventory` scope in the `travel-sample` bucket in the `default` namespace.

#### [](#keyspace-partial)Keyspace Partial

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram](../_images/n1ql-language-reference/keyspace-partial.png) 

Alternatively, if the keyspace is a named collection, the keyspace reference may be just the collection name with no path. In this case, you must set the [query context](../n1ql-intro/queriesandresults.md#query-context) to indicate the required namespace, bucket, and scope.

collection

(Required) An [identifier](identifiers.md) that refers to the [collection name](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the keyspace.

For example, `airline` indicates the `airline` collection, assuming the query context is set.

#### [](#from-keyspace-alias)AS Alias

Assigns another name to the FROM keyspace. For details, see [AS Clause](#section%5Fax5%5F2nx%5F1db).

Assigning an alias is optional for the FROM keyspace. If you assign an alias to the FROM keyspace, the `AS` keyword may be omitted.

#### [](#from-keyspace-hints)USE Clause

Enables you to specify that the query should use particular keys, or a particular index. For details, see [USE clause](hints.md).

### [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

The simplest type of FROM keyspace clause specifies a single keyspace.

Example 1\. Use a single keyspace

Select four unique landmarks from the `landmark` keyspace.

```sqlpp
SELECT DISTINCT name
FROM landmark
LIMIT 4;
```

Results

```JSON
[
  {
    "name": "Royal Engineers Museum"
  },
  {
    "name": "Hollywood Bowl"
  },
  {
    "name": "Thai Won Mien"
  },
  {
    "name": "Spice Court"
  }
]
```

## [](#select-expr)FROM Subquery

Specifies a SQL++ `SELECT` expression of input objects.

### [](#syntax-3)Syntax

```ebnf
from-subquery ::= subquery-expr 'AS'? alias
```

![Syntax diagram](../_images/n1ql-language-reference/from-subquery.png) 

| subquery-expr | [Subquery Expression](#select-expr-clause) |
| ------------- | ------------------------------------------ |
| alias         | [AS Alias](#select-expr-alias)             |

#### [](#select-expr-clause)Subquery Expression

```ebnf
subquery-expr ::= '(' select ')'
```

![Syntax diagram](../_images/n1ql-language-reference/subquery-expr.png) 

Use parentheses to specify a subquery.

For more details and examples, see [SELECT Clause](selectclause.md) and [Subqueries](subqueries.md).

#### [](#select-expr-alias)AS Alias

Assigns another name to the subquery. For details, see [AS Clause](#section%5Fax5%5F2nx%5F1db).

Assigning an alias is required for subqueries in the FROM term. However, when you assign an alias to the subquery, the `AS` keyword may be omitted.

### [](#examples-2)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 2\. A `SELECT` clause inside a `FROM` clause.

List all `Gillingham` landmark names from a subset of all landmark eating places.

```sqlpp
SELECT name, city
FROM (SELECT id, name, address, city
      FROM landmark
      WHERE activity = "eat") AS l
WHERE city = "Gillingham";
```

Results

```JSON
[
  {
    "city": "Gillingham",
    "name": "Hollywood Bowl"
  },
  {
    "city": "Gillingham",
    "name": "Thai Won Mien"
  },
  {
    "city": "Gillingham",
    "name": "Spice Court"
  },
  {
    "city": "Gillingham",
    "name": "Beijing Inn"
  },
  {
    "city": "Gillingham",
    "name": "Ossie's Fish and Chips"
  }
]
```

Example 3\. Subquery Example

For each country, find the number of airports at different altitudes and their corresponding cities.

In this case, the inner query finds the first level of grouping of different altitudes by country and corresponding number of cities. Then the outer query builds on the inner query results to count the number of different altitude groups for each country and the total number of cities.

```sqlpp
SELECT t1.country, num_alts, total_cities
FROM (SELECT country, geo.alt AS alt,
             count(city) AS num_cities
      FROM airport
      GROUP BY country, geo.alt) t1
GROUP BY t1.country
LETTING num_alts = count(t1.alt), total_cities = sum(t1.num_cities);
```

Results

```JSON
[
  {
    "country": "United States",
    "num_alts": 946,
    "total_cities": 1560
  },
  {
    "country": "United Kingdom",
    "num_alts": 128,
    "total_cities": 187
  },
  {
    "country": "France",
    "num_alts": 196,
    "total_cities": 221
  }
]
```

This is equivalent to blending the results of the following two queries by country, but the subquery in the `from-term` above simplified it.

```sqlpp
SELECT country,count(city) AS num_cities
FROM airport
GROUP BY country;
```

```sqlpp
SELECT country, count(distinct geo.alt) AS num_alts
FROM airport
GROUP BY country;
```

## [](#generic-expr)FROM Generic Expression

Generic [expressions](index.md) in the FROM term may include SQL++ functions, operators, path expressions, language constructs on constant expressions, variables, and subqueries. This adds huge flexibility by enabling just about any FROM clause imaginable.

### [](#syntax-4)Syntax

```ebnf
from-generic ::= expr ( 'AS' alias )?
```

![Syntax diagram](../_images/n1ql-language-reference/from-generic.png) 

| expr  | A SQL++ expression generating JSON documents or objects. |
| ----- | -------------------------------------------------------- |
| alias | [AS Alias](#generic-expr-alias)                          |

#### [](#generic-expr-alias)AS Alias

Assigns another name to the generic expression. For details, see [AS Clause](#section%5Fax5%5F2nx%5F1db).

Assigning an alias is optional for generic expressions in the FROM term. However, when you assign an alias to the expression, the `AS` keyword is required.

### [](#examples-3)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 4\. Independent Constant Expression

The expression may include JSON scalar values, static JSON literals, objects, or SQL++ functions.

```sqlpp
SELECT * FROM [1, 2, "name", { "type" : "airport", "id" : "SFO"}] AS ks1;
```

```sqlpp
SELECT CURL("https://maps.googleapis.com/maps/api/geocode/json",
           {"data":"address=Half+Moon+Bay" , "request":"GET"} );
```

Note that functions such as [CURL()](curl.md) can independently produce input data objects for the query. Similarly, other SQL++ functions can also be used in the expressions.

Example 5\. Variable SQL++ Expression

The expression may refer to any [variables in scope](subqueries.md#section%5Fonz%5F3tj%5Fmz) for the query.

```sqlpp
SELECT count(*)
FROM airport t
LET x = t.geo
WHERE (SELECT RAW y.alt FROM x y)[0] > 6000;
```

The `FROM x` clause is an expression that refers to the outer query. This is applicable to only subqueries because the outermost level query cannot use any variables in its own `FROM` clause. This makes the subquery correlated with outer queries, as explained in the [Subqueries](subqueries.md) section.

## [](#section%5Fax5%5F2nx%5F1db)AS Clause

To use a shorter or clearer name anywhere in the query, like SQL, SQL++ allows you to assign an alias to any FROM term in the `FROM` clause.

### [](#syntax-5)Syntax

The `AS` keyword is required when assigning an alias to a generic expression.

The `AS` keyword is optional when assigning an alias to the FROM keyspace, a subquery, the JOIN clause, the NEST clause, or the UNNEST clause.

### [](#arguments)Arguments

alias

String to assign an alias.

|  | Since the original name may lead to referencing wrong data and wrong results, you must use the alias name throughout the query instead of the original keyspace name. In the FROM clause, the renaming appears only in the projection and not the fields themselves. When no alias is used, the keyspace or last field name of an expression is given as the implicit alias. When an alias conflicts with a keyspace or field name in the same scope, the identifier always refers to the alias. This allows for consistent behavior in scenarios where an identifier only conflicts in some documents. For more information on aliases, see [Identifiers](identifiers.md). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#examples-4)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

The following `FROM` clauses are equivalent, with and without the `AS` keyword.

| FROM airport AS t                                             | FROM airport t                                          |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| FROM hotel AS h INNER JOIN landmark AS l ON (h.city = l.city) | FROM hotel h INNER JOIN landmark l ON (h.city = l.city) |

## [](#related-links)Related Links

* [USE Clause](hints.md)
* [JOIN Clause](join.md)
* [NEST Clause](nest.md)
* [UNNEST Clause](unnest.md)
* [Comma-Separated Join](comma.md)