[View original HTML](/server/7.6/n1ql/n1ql-language-reference/optimizer-hints.html)

> Optimizer hints enable you to supply directives to the optimizer. 

You can use optimizer hints to request that the [optimizer](cost-based-optimizer.md) should consider specific indexes, join methods, join ordering, and so on, when creating the plan for a query. This may be useful in situations where the optimizer is not able to come up with the preferred plan, due to lack of optimizer statistics, high level of skew in data, data correlations, and so on.

Generally speaking, you should rely on the optimizer to generate the query plan.

Examples on this Page

To use the examples on this page, you must set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

## [](#syntax)Syntax

```ebnf
hint-comment ::= block-hint-comment | line-hint-comment
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/hint-comment.png) 

```ebnf
block-hint-comment ::= '/*+' hints '*/'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/block-hint-comment.png) 

```ebnf
line-hint-comment ::= '--+' hints
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/line-hint-comment.png) 

You can supply hints to the operator within a specially-formatted _hint comment_. The hint comment may be a block comment or a line comment. There must be a plus sign `+` immediately after the start of the comment; this is the distinguishing delimiter of the hint comment.

Note that a line comment includes all text up to the end of the line. Therefore, if the hint comment is a line comment, the next part of the query must start on the following line.

Example 1\. Block hint comment

Query

```sqlpp
SELECT /*+ INDEX(airport def_inventory_airport_city) */ airportname
FROM airport
WHERE city = "San Francisco";
```

Example 2\. Line hint comment

Equivalent to [Example 1](#ex-block-hint)

```sqlpp
SELECT --+ INDEX(airport def_inventory_airport_city)
       airportname
FROM airport
WHERE city = "San Francisco";
```

## [](#placement)Placement

Currently, a hint comment is only supported in the `SELECT` statement. The hint comment must be located immediately after the `SELECT` keyword. For details, refer to [SELECT Clause](selectclause.md).

There can only be one hint comment in a query block. If there is more than one hint comment, a syntax error is generated. However, the hint comment may contain one or more hints.

Example 3\. Multiple hint comments

Incorrect query

```sqlpp
SELECT /*+ USE_HASH(r) */
       /*+ INDEX(a def_inventory_airport_city) */
       a.airportname, r.airline
FROM airport a
JOIN route r
ON a.faa = r.sourceairport
WHERE a.city = "San Francisco";
```

This query generates a syntax error, as it contains multiple hint comments.

## [](#format)Format

```ebnf
hints ::= simple-hint-sequence | json-hint-object
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/hints.png) 

```ebnf
simple-hint-sequence ::= simple-hint+
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/simple-hint-sequence.png) 

```ebnf
json-hint-object ::= '{' json-hint (',' json-hint )* '}'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/json-hint-object.png) 

Internally, the hint comment may take one of two equivalent formats:

* The _simple_ syntax is a plain text format, similar to the type of hint comment found in many relational databases.
* Alternatively, you may supply optimizer hints using _JSON_ syntax. In this case, the hint comment contains a single top-level hint object.

You cannot mix the simple syntax and the JSON syntax within the same hint comment; each hint comment must use one syntax or the other exclusively.

To use multiple hints with the simple syntax, simply specify the hints one after another within the hint comment. To use multiple hints with the JSON syntax, specify each hint as a property within the top-level hint object.

Example 4\. Simple hint

Query

```sqlpp
SELECT /*+ INDEX(airport def_inventory_airport_city) */
       airportname, faa
FROM airport
WHERE city = "San Francisco";
```

Example 5\. JSON hint

Equivalent to [Example 4](#ex-simple-hint)

```sqlpp
SELECT /*+ {"index": {"keyspace": "airport",
                      "indexes": "def_inventory_airport_city"}} */
       airportname, faa
FROM airport
WHERE city = "San Francisco";
```

Example 6\. Multiple simple hints

Query

```sqlpp
SELECT /*+ INDEX(a def_inventory_airport_city) USE_HASH(r) */
       a.airportname, r.airline
FROM airport a
JOIN route r
ON a.faa = r.sourceairport
WHERE a.city = "San Francisco";
```

Example 7\. Multiple JSON hints

Equivalent to [Example 6](#ex-multi-simple)

```sqlpp
SELECT /*+ {"index": {"keyspace": "a",
                      "indexes": "def_inventory_airport_city"},
            "use_hash": {"keyspace": "r"}} */
       a.airportname, r.airline
FROM airport a
JOIN route r
ON a.faa = r.sourceairport
WHERE a.city = "San Francisco";
```

## [](#legacy-equivalents)Legacy Equivalents

Many optimizer hints have an equivalent legacy syntax using the `USE` clause. Details of these are given on the pages for individual optimizer hints, and in the pages describing the `USE` clause. For details, refer to [USE INDEX Clause](hints.md#use-index-clause)and [ANSI JOIN Hints](join.md#ansi-join-hints).

Note that you cannot use a hint comment and the `USE` clause to specify optimizer hints on the same keyspace. If you do this, the hint comment and the `USE` clause are marked as erroneous and ignored by the optimizer.

Example 8\. Legacy hint

Legacy equivalent to [Example 4](#ex-simple-hint)

```sqlpp
SELECT airportname, faa
FROM airport
USE INDEX (def_inventory_airport_city)
WHERE city = "San Francisco";
```

## [](#explain-plans)Explain Plans

When optimizer hints are specified for a query, the explain plan reports the status of each hint: that is, whether the hint was followed or not followed by the optimizer in choosing the query plan. Invalid hints are also reported. Specific error messages are given for any hint that is not followed, or invalid.

Example 9\. Simple hint explain plan

When the optimizer follows a simple hint, the hint is shown in the explain plan.

Explain plan for [Example 4](#ex-simple-hint)

```sqlpp
EXPLAIN SELECT /*+ INDEX(airport def_inventory_airport_city) */
               airportname, faa
FROM airport
WHERE city = "San Francisco";
```

Result

```json
[
  {
    "optimizer_hints": {
      "hints_followed": [
        "INDEX(airport def_inventory_airport_city)"
      ]
    },
// ...
  }
]
```

Example 10\. JSON hint explain plan

When the optimizer follows a JSON hint, the hint is shown in the explain plan in JSON format.

Explain plan for [Example 5](#ex-json-hint)

```sqlpp
EXPLAIN SELECT /*+ {"index": {"keyspace": "airport",
                              "indexes": "def_inventory_airport_city"}} */
               airportname, faa
FROM airport
WHERE city = "San Francisco";
```

Result

```json
[
  {
    "optimizer_hints": {
      "hints_followed": [
        "hint": "{\"index\":{\"indexes\":[\"def_inventory_airport_city\"],\"keyspace\":\"airport\"}}"
      ]
    },
// ...
  }
]
```

Example 11\. Multiple hint explain plan

When the optimizer follows multiple hints, all the followed hints are shown in the explain plan.

Explain plan for [Example 6](#ex-multi-simple)

```sqlpp
EXPLAIN SELECT /*+ USE_HASH(r) INDEX(a def_inventory_airport_city) */
               a.airportname, r.airline
FROM airport a
JOIN route r
ON a.faa = r.sourceairport
WHERE a.city = "San Francisco";
```

Result

```json
[
  {
    "optimizer_hints": {
      "hints_followed": [
        "USE_HASH(r)",
        "INDEX(a def_inventory_airport_city)"
      ]
    },
// ...
  }
]
```

Example 12\. Legacy hint explain plan

When the optimizer follows a hint specified using the legacy `USE` clause, the hint is likewise shown in the explain plan.

Explain plan for [Example 8](#ex-legacy-hint)

```sqlpp
EXPLAIN SELECT airportname, faa
FROM airport
USE INDEX (def_inventory_airport_city)
WHERE city = "San Francisco";
```

Result

```json
[
  {
    "optimizer_hints": {
      "hints_followed": [
        "INDEX(airport def_inventory_airport_city)"
      ]
    },
// ...
  }
]
```

Example 13\. Unused hint explain plan

When the optimizer cannot follow a hint, any hints that cannot be followed are shown in the explain plan.

Explain plan

```sqlpp
EXPLAIN SELECT /*+ USE_HASH(r) INDEX(a def_inventory_airport_city) */
               a.airportname, r.airline
FROM airport a
JOIN route r
ON a.faa = r.sourceairport
WHERE a.city IS MISSING;
```

Result

```json
[
  {
    "optimizer_hints": {
      "hints_followed": [
        "USE_HASH(r)"
      ],
      "hints_not_followed": [
        "INDEX(a def_inventory_airport_city): INDEX hint cannot be followed"
      ]
    },
// ...
  }
]
```

Example 14\. Invalid hint explain plan

When you specify an invalid hint, any invalid hints are shown in the explain plan.

Explain plan

```sqlpp
EXPLAIN SELECT /*+ USE_HASH(r) INDEX_SS(a def_inventory_airport_city) */
               a.airportname, r.airline
FROM airport a
JOIN route r
ON a.faa = r.sourceairport
WHERE a.city = "San Francisco";
```

Result

```json
[
  {
    "optimizer_hints": {
      "hints_followed": [
        "USE_HASH(r)"
      ],
      "invalid_hints": [
        "INDEX_SS(a def_inventory_airport_city): Invalid hint name"
      ]
    },
// ...
  }
]
```

## [](#further-details)Further Details

Refer to the following pages for details of individual optimizer hints:

* [Query Block Hints](query-hints.md) apply to an entire query block.
* [Keyspace Hints](keyspace-hints.md) apply to a specific keyspace.

## [](#related-links)Related Links

* [Cost-Based Optimizer](cost-based-optimizer.md)