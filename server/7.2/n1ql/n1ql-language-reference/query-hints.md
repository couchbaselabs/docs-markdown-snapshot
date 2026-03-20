---
title: Query Block Hints
description: Query block hints are hints that apply to an entire query block.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/query-hints.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/query-hints.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/query-hints.html)

# Query Block Hints

> Query block hints are hints that apply to an entire query block. 

A query hint is a type of [optimizer hint](optimizer-hints.md). Currently SQL++ supports only one query block hint: ORDERED.

There are two possible formats for each optimizer hint: simple syntax and JSON syntax. Note that you cannot mix simple syntax and JSON syntax in the same hint comment.

## [](#ordered)ORDERED

If present, this hint directs the optimizer to order any joins just as they are ordered in the query. If not specified, the optimizer determines the optimal join order.

### [](#simple-syntax)Simple Syntax

```ebnf
ordered-hint-simple ::= 'ORDERED'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/ordered-hint-simple.png) 

With the simple syntax, this hint takes no arguments. You may only use this hint once within the hint comment.

### [](#json-syntax)JSON Syntax

```ebnf
ordered-hint-json ::= '"ordered"' ':' 'true'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/ordered-hint-json.png) 

With the JSON syntax, this hint takes the form of an `ordered` property. You may only use this property once within the hint comment. The value of this property must be set to `true`.

### [](#ordered-examples)Examples

For the examples in this section, it is assumed that the cost-based optimizer is active, and all optimizer statistics are up-to-date.

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Optimized join ordering

Consider the following query, which does not contain an ordering hint.

Query

```sqlpp
SELECT a.airportname AS source, r.id AS route, l.name AS airline
FROM airport AS a
JOIN route AS r (1)
  ON r.sourceairport = a.faa
JOIN airline AS l (2)
  ON r.airlineid = META(l).id
WHERE l.name = "40-Mile Air";
```

| **1** | Join the airport keyspace to the route keyspace.    |
| ----- | --------------------------------------------------- |
| **2** | Join the resulting dataset to the airline keyspace. |

If you examine the plan for this query, you can see that with no hint specified, the optimizer has re-ordered the joins.

![Query plan with optimized join order](../_images/join-order-optimize.png) 

| **1** | Join the airline keyspace to the route keyspace.    |
| ----- | --------------------------------------------------- |
| **2** | Join the resulting dataset to the airport keyspace. |

ORDERED hint — simple syntax

This example is equivalent to the one in the [Optimized join ordering](#ex-ordered-opt) example, but includes an ordering hint using simple syntax.

Query

```sqlpp
SELECT /*+ ORDERED */
       a.airportname AS source, r.id AS route, l.name AS airline
FROM airport AS a
JOIN route AS r (1)
  ON r.sourceairport = a.faa
JOIN airline AS l (2)
  ON r.airlineid = META(l).id
WHERE l.name = "40-Mile Air";
```

| **1** | Join the airport keyspace to the route keyspace.    |
| ----- | --------------------------------------------------- |
| **2** | Join the resulting dataset to the airline keyspace. |

If you examine the plan for this query, you can see that the joins are ordered just as they were written.

![Query plan with ORDERED hint](../_images/join-order-hint.png) 

| **1** | Join the airport keyspace to the route keyspace.    |
| ----- | --------------------------------------------------- |
| **2** | Join the resulting dataset to the airline keyspace. |

ORDERED hint — JSON syntax

This example is equivalent to the one in the [Optimized join ordering](#ex-ordered-opt) example, but includes an ordering hint using JSON syntax.

Query

```sqlpp
SELECT /*+ {"ordered": true} */
       a.airportname AS source, r.id AS route, l.name AS airline
FROM airport AS a
JOIN route AS r (1)
  ON r.sourceairport = a.faa
JOIN airline AS l (2)
  ON r.airlineid = META(l).id
WHERE l.name = "40-Mile Air";
```

| **1** | Join the airport keyspace to the route keyspace.    |
| ----- | --------------------------------------------------- |
| **2** | Join the resulting dataset to the airline keyspace. |

If you examine the plan for this query, you can see that the joins are ordered just as they were written, just like the query in the previous example.

### [](#legacy-equivalent)Legacy Equivalent

There is no legacy clause equivalent to this hint.

## [](#related-links)Related Links

* [Cost-Based Optimizer](cost-based-optimizer.md)
* [Optimizer Hints](optimizer-hints.md)
* [Keyspace Hints](keyspace-hints.md)