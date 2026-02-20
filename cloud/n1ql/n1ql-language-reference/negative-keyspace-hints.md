---
title: Negative Keyspace Hints
description: Negative hints direct the optimizer not to use certain indexes or join methods.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/negative-keyspace-hints.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-language-reference/negative-keyspace-hints.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/negative-keyspace-hints.html)

# Negative Keyspace Hints

> Negative hints direct the optimizer not to use certain indexes or join methods. 

A negative hint is a type of [optimizer hint](optimizer-hints.md) that applies to a specific keyspace. Unlike [positive keyspace hints](keyspace-hints.md), which direct the optimizer to use specific indexes or join methods, negative hints instruct it what not to use.

Negative hints are of two types: index hints and join hints. Index hints direct optimizer not to use specific indexes, and join hints direct it not to use specific join methods.

For each negative hint, you must specify the keyspace or keyspaces that the hint applies to. If a keyspace is given an explicit alias in the query, then the hint must refer to the explicit alias, not the keyspace name. This is to avoid confusion in situations where the same keyspace can be used multiple times (with different aliases) in the same query.

If the keyspace is not given an explicit alias in the query, the hint must refer to the keyspace using the keyspace name. (If the keyspace name is a dotted path, the hint must refer to the keyspace using its implicit alias, which is the last component in the keyspace path.)

Negative hints support two prefixes: `NO_` and `AVOID_`. You can specify them using either simple syntax or JSON syntax, but you cannot mix the two in the same hint comment.

## [](#no%5Findex)NO\_INDEX

This hint is the negative equivalent of the [INDEX hint](keyspace-hints.md#index). It directs the optimizer not to use a specific secondary index for a keyspace. You can add one or more secondary indexes in the hint. If you do not specify this hint, the optimizer selects the optimal available index.

### [](#simple-syntax)Simple Syntax

```ebnf
no-gsi-hint-simple ::= ( 'NO_INDEX' | 'AVOID_INDEX' ) '(' keyspace index* ')'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-gsi-hint-simple.png) 

With the simple syntax, this hint specifies a single keyspace expression along with zero, one, or more indexes to avoid. You can either use `NO_INDEX` or `AVOID_INDEX` as the hint keyword. You can also use this hint multiple times within a hint comment to apply it to more than one keyspace.

> [!NOTE]
> For this hint to work effectively, you must specify at least one index. The optimizer ignores the hint if you do not specify any indexes.

#### [](#arguments)Arguments

keyspace

The keyspace or alias to which this hint applies.

index

A secondary index that the optimizer must not use for the given keyspace. This argument is optional. However, you must specify at least one index. Otherwise, the optimizer ignores the hint.

### [](#json-syntax)JSON Syntax

```ebnf
no-gsi-hint-json ::= ( '"no_index"' | '"avoid_index"' ) ':' ( index-array | index-object )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-gsi-hint-json.png) 

With the JSON syntax, this hint takes the form of a `no_index` or `avoid_index` property. You can only use this property once within a hint comment. The value of this property can be an [Index Array](#index-array) or an [Index Object](#index-object).

#### [](#index-array)Index Array

```ebnf
index-array ::= '[' index-object ( ',' index-object )* ']'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-array.png) 

Use this array to specify indexes for multiple keyspaces. Each element must be an [Index Object](#index-object).

#### [](#index-object)Index Object

```ebnf
index-object ::= '{' keyspace-property ',' indexes-property '}'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-object.png) 

Use this object to specify indexes for a single keyspace. It must contain a [Keyspace Property](#keyspace-property) and an [Indexes Property](#indexes-property). The order of the properties within the object is not significant.

#### [](#keyspace-property)Keyspace Property

```ebnf
keyspace-property ::= ( '"keyspace"' | '"alias"' ) ':' '"' keyspace '"'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-property.png) 

Synonym for `"keyspace"`: `"alias"`

The value of this property is the keyspace or alias to which this hint applies.

#### [](#indexes-property)Indexes Property

```ebnf
indexes-property ::= '"indexes"' ':' ( 'null'
                                     | '"' index '"'
                                     | '[' '"' index '"' ( ',' '"' index '"' )* ']' )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/indexes-property.png) 

The value of this property can be:

| null                      | The optimizer ignores the hint when the value is null. For the hint to work effectively, you must specify at least one index. |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| An index string           | A secondary index that the optimizer must not use for the given keyspace.                                                     |
| An array of index strings | An array of secondary indexes that the optimizer must not use for the given keyspace.                                         |

### [](#no-index-examples)Examples

For the examples in this section, it’s assumed that the cost-based optimizer is active, and all optimizer statistics are up-to-date.

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Query without any hints

The following query does not include an index hint.

Query

```sqlpp
SELECT id
FROM route
WHERE sourceairport = "SFO"
LIMIT 1;
```

If you examine the plan for this query, you can see that the optimizer has selected the index `def_inventory_route_sourceairport`, which is installed with the travel sample dataset.

Explain plan

```json
{
  "#operator": "IndexScan3",
  "bucket": "travel-sample",
  "index": "def_inventory_route_sourceairport",
```

Example 2\. Query with the NO\_INDEX hint

The following query hints the optimizer to avoid using the index `def_inventory_route_sourceairport` for the keyspace `route`.

Query

```sqlpp
SELECT /*+ NO_INDEX (route def_inventory_route_sourceairport) */ id
FROM route
WHERE sourceairport = "SFO"
LIMIT 1;
```

If you examine the plan for this query, you can see that the query omits the specified index, forcing the optimizer to consider other available indexes.

Explain plan

```json
"scan": {
    "#operator": "IndexScan3",
    "bucket": "travel-sample",
    "index": "def_inventory_route_route_src_dst_day",
```

## [](#no%5Findex%5Ffts)NO\_INDEX\_FTS

This hint is the negative equivalent of the [INDEX\_FTS hint](keyspace-hints.md#index%5Ffts). It directs the optimizer not to use a specific full-text index for a keyspace. You can add one or more full-text indexes in the hint. If you do not specify this hint, the optimizer selects the optimal available index.

### [](#simple-syntax-2)Simple Syntax

```ebnf
no-fts-hint-simple ::= ( 'NO_INDEX_FTS' | 'AVOID_INDEX_FTS' ) '(' keyspace index* ')'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-fts-hint-simple.png) 

With the simple syntax, this hint specifies a single keyspace expression along with zero, one, or more indexes. You can either use `NO_INDEX_FTS` or `AVOID_INDEX_FTS` as the hint keyword. You can also use this hint multiple times within a hint comment to apply it to more than one keyspace.

> [!NOTE]
> For this hint to work effectively, you must specify at least one index. The optimizer ignores the hint if you do not specify any indexes.

#### [](#arguments-2)Arguments

keyspace

The keyspace or alias to which this hint applies.

index

A full-text index that the optimizer must not use for the given keyspace. This argument is optional. However, you must specify at least one index. Otherwise, the optimizer ignores the hint.

### [](#json-syntax-2)JSON Syntax

```ebnf
no-gsi-hint-json ::= ( '"no_index"' | '"avoid_index"' ) ':' ( index-array | index-object )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-gsi-hint-json.png) 

With the JSON syntax, this hint takes the form of a `no_index_fts` or `avoid_index_fts` property. You can only use this property once within the hint comment. The value of this property can be an [Index Array](#index-array-no-fts) or an [Index Object](#index-object-no-fts).

#### [](#index-array-no-fts)Index Array

```ebnf
index-array ::= '[' index-object ( ',' index-object )* ']'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-array.png) 

Use this array to specify indexes for multiple keyspaces. Each element must be an [Index Object](#index-object-no-fts).

#### [](#index-object-no-fts)Index Object

```ebnf
index-object ::= '{' keyspace-property ',' indexes-property '}'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-object.png) 

Use this object to specify indexes for a single keyspace. It must contain a [Keyspace Property](#keyspace-property-no-fts) and an [Indexes Property](#indexes-property-no-fts). The order of the properties within the object is not significant.

#### [](#keyspace-property-no-fts)Keyspace Property

```ebnf
keyspace-property ::= ( '"keyspace"' | '"alias"' ) ':' '"' keyspace '"'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-property.png) 

Synonym for `"keyspace"`: `"alias"`

The value of this property is the keyspace or alias to which this hint applies.

#### [](#indexes-property-no-fts)Indexes Property

```ebnf
indexes-property ::= '"indexes"' ':' ( 'null'
                                     | '"' index '"'
                                     | '[' '"' index '"' ( ',' '"' index '"' )* ']' )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/indexes-property.png) 

The value of this property can be:

| null                      | The optimizer ignores the hint when the value is null. For the hint to work effectively, you must specify at least one index. |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| An index string           | A full-text index that the optimizer must not use for the given keyspace.                                                     |
| An array of index strings | An array of full-text indexes that the optimizer must not use for the given keyspace.                                         |

### [](#no-index-fts-examples)Examples

Example 3\. NO\_INDEX\_FTS hint

This example specifies that the optimizer should not use the FTS index `hotel_state_fts_index`. To qualify for this query, you must have this FTS index on `state` and `type`, using the keyword analyzer. (Or alternatively, the FTS index on `state`, with a custom type mapping on `hotel`.)

Query

```sqlpp
SELECT /*+ NO_INDEX_FTS (hotel hotel_state_fts_index) */
       META().id
FROM hotel
WHERE state = "Corse" OR state = "California";
```

The optimizer omits the `hotel_state_fts_index` index from the query plan. If a qualified FTS index is available, it’s selected for the query. If none of the available FTS indexes are qualified, the available GSI indexes are considered instead.

## [](#no%5Fuse%5Fnl)NO\_USE\_NL

This hint is the negative equivalent of the [USE\_NL hint](keyspace-hints.md#use%5Fnl). It directs the optimizer not to use a nested loop join for a specified keyspace. This hint must be specified on the keyspace on the right-hand side of the join. If not specified, the optimizer selects the optimal join method.

> [!NOTE]
> This hint is only available in [SELECT](selectclause.md) and [MERGE](merge.md) statements.

### [](#simple-syntax-3)Simple Syntax

```ebnf
no-nl-hint-simple ::= ( 'NO_USE_NL' | 'AVOID_NL' ) '(' ( keyspace )+ ')'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-nl-hint-simple.png) 

With the simple syntax, this hint specifies one or more keyspaces. You can either use `NO_USE_NL` or `AVOID_NL` as the hint keyword. You can also use this hint multiple times within the hint comment.

#### [](#arguments-3)Arguments

keyspace

The keyspace or alias to which this hint applies.

### [](#json-syntax-3)JSON Syntax

```ebnf
no-nl-hint-json ::= ( '"no_use_nl"' | '"avoid_nl"') ':' ( keyspace-array | keyspace-object )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-nl-hint-json.png) 

With the JSON syntax, this hint takes the form of a `no_use_nl` or `avoid_nl` property. You can only use this property once within the hint comment. The value of this property can be a [Keyspace Array](#keyspace-array-no-nl) or a [Keyspace Object](#keyspace-object-no-nl).

#### [](#keyspace-array-no-nl)Keyspace Array

```ebnf
keyspace-array ::= '[' keyspace-object ( ',' keyspace-object )* ']'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-array.png) 

Use this array to apply the hint to multiple keyspaces. Each element must be a [Keyspace Object](#keyspace-object-no-nl).

#### [](#keyspace-object-no-nl)Keyspace Object

```ebnf
keyspace-object ::= '{' keyspace-property '}'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-object.png) 

Use this object to apply the hint to a single keyspace. It must contain a [Keyspace Property](#keyspace-property-no-nl).

#### [](#keyspace-property-no-nl)Keyspace Property

```ebnf
keyspace-property ::= ( '"keyspace"' | '"alias"' ) ':' '"' keyspace '"'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-property.png) 

Synonym for `"keyspace"`: `"alias"`

The value of this property is the keyspace or alias to which this hint applies.

### [](#no-use-nl-examples)Examples

Example 4\. Query without a join hint

The following query does not include a join hint.

Query

```sqlpp
SELECT a.airportname AS airport, r.id AS route
FROM route AS r,
     airport AS a
WHERE a.faa = r.sourceairport
  AND r.sourceairport = "SFO"
LIMIT 4;
```

If you examine the plan for this query, you can see that the optimizer has selected the nested-loop join method.

Explain plan

```json
{
    "#operator": "NestedLoopJoin",
    "alias": "a",
    "filter": "((`a`.`faa`) = (`r`.`sourceairport`))",
    "on_clause": "(((`a`.`faa`) = (`r`.`sourceairport`)))",
```

Example 5\. NO\_USE\_NL hint

The following query hints the optimizer to avoid using a nested-loop join.

Query

```sqlpp
SELECT /*+ NO_USE_NL (a) */ 
       a.airportname AS airport, r.id AS route
FROM route AS r,
     airport AS a
WHERE a.faa = r.sourceairport
  AND r.sourceairport = "SFO"
LIMIT 4;
```

If you examine the plan for this query, you can see that the optimizer avoids using a nested-loop join and considers other join methods. In this case, the optimizer has selected the hash join method.

Explain plan

```json
{
    "#operator": "HashJoin",
    "build_aliases": [
        "r"
    ],
```

## [](#no%5Fuse%5Fhash)NO\_USE\_HASH

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

This hint is the negative equivalent of the [USE\_HASH hint](keyspace-hints.md#use%5Fhash). It directs the optimizer not to use a hash join for a specified keyspace. This hint must be specified on the keyspace on the right-hand side of the join. If you do not specify this hint, the optimizer selects the optimal join method.

Unlike [USE\_HASH](keyspace-hints.md#use%5Fhash), this hint does not allow you to specify whether the keyspace should appear on the build or probe side of the hash join. Instead, you can only specify the keyspace name or alias to which this hint applies.

> [!NOTE]
> This hint is only available in [SELECT](selectclause.md) and [MERGE](merge.md) statements.

### [](#simple-syntax-4)Simple Syntax

```ebnf
no-hash-hint-simple ::= ( 'NO_USE_HASH' | 'AVOID_HASH' ) '(' ( keyspace )+ ')'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-hash-hint-simple.png) 

With the simple syntax, this hint specifies one or more keyspaces. You can either use `NO_USE_HASH` or `AVOID_HASH` as the hint keyword. You may also use this hint multiple times within a hint comment.

#### [](#arguments-4)Arguments

keyspace

The keyspace or alias to which this hint applies.

### [](#json-syntax-4)JSON Syntax

```ebnf
no-hash-hint-json ::= ( '"no_use_hash"' | '"avoid_hash"' ) ':'
                      ( keyspace-array | keyspace-object )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/no-hash-hint-json.png) 

With the JSON syntax, this hint takes the form of a `no_use_hash` or `avoid_hash` property. You can only use this property once within a hint comment. The value of this property can be a [Keyspace Array](#keyspace-array-no-hash) or a [Keyspace Object](#keyspace-object-no-hash).

#### [](#keyspace-array-no-hash)Keyspace Array

```ebnf
keyspace-array ::= '[' keyspace-object ( ',' keyspace-object )* ']'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-array.png) 

Use this array to apply the hint to multiple keyspaces. Each element must be a [Keyspace Object](#keyspace-object-no-hash).

#### [](#keyspace-object-no-hash)Keyspace Object

```ebnf
keyspace-object ::= '{' keyspace-property '}'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-object.png) 

Use this object to apply the hint to a single keyspace. It must contain a [Keyspace Property](#keyspace-property-no-hash).

#### [](#keyspace-property-no-hash)Keyspace Property

```ebnf
keyspace-property ::= ( '"keyspace"' | '"alias"' ) ':' '"' keyspace '"'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-property.png) 

Synonym for `"keyspace"`: `"alias"`

The value of this property is the keyspace or alias to which this hint applies.

### [](#no-use-hash-examples)Examples

For the examples in this section, it’s assumed that the cost-based optimizer is active, and all optimizer statistics are up-to-date.

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 6\. Query without a join hint

The following query does not include a join hint.

Query

```sqlpp
SELECT COUNT(1) AS Total_Count
FROM route rte
INNER JOIN airline aline
ON rte.airlineid = META(aline).id;
```

If you examine the plan for this query, you can see that the optimizer has selected to use the hash join method.

Explain plan

```json
{
  "#operator": "HashJoin",
  "build_aliases": [
    "aline"
  ],
  "build_exprs": [
    "cover ((meta(`aline`).`id`))"
  ],
  "on_clause": "(((`rte`.`airlineid`) = cover ((meta(`aline`).`id`))))",
// ...
  "probe_exprs": [
    "(`rte`.`airlineid`)"
  ],
```

Example 7\. Query with the NO\_USE\_HASH hint

The following query hints the optimizer to avoid using a hash join for the keyspace `aline`.

Query

```sqlpp
SELECT /*+ NO_USE_HASH(aline) */
       COUNT(1) AS Total_Count
FROM route rte
INNER JOIN airline aline
ON rte.airlineid = META(aline).id;
```

If you examine the plan for this query, you can see that the optimizer avoids using a hash join and considers other join methods. In this case, the optimizer has selected the lookup join method.

Explain plan

```json
{
    "#operator": "Join",
    "as": "aline",
    "bucket": "travel-sample",
    "keyspace": "airline",
    "namespace": "default",
    "on_keys": "(`rte`.`airlineid`)",
    "optimizer_estimates": {
        "cardinality": 44924.88,
        "cost": 343011.9112140067,
        "fr_cost": 343011.9112140067,
        "size": 800
    },
    "scope": "inventory"
},
```

## [](#legacy-equivalent)Legacy Equivalent

Unlike [positive keyspace hints](keyspace-hints.md), negative hints do not have legacy equivalents. However, you cannot specify a negative hint and the `USE` clause on the same keyspace. If you do this, the negative hint and the `USE` clause are both marked as erroneous and ignored by the optimizer.

## [](#interaction-between-positive-and-negative-hints)Interaction between Positive and Negative Hints

As a best practice, avoid using positive and negative hints of the same type on the same keyspace. This can create conflicts and may cause the optimizer to ignore both hints.

### [](#join-hints)Join Hints

You can only specify one join hint per keyspace or alias. This can be either a positive ([USE HASH](keyspace-hints.md#use%5Fhash), [USE\_NL](keyspace-hints.md#use%5Fnl)) or a negative ([NO\_USE\_HASH](#no%5Fuse%5Fhash), [NO\_USE\_NL](#no%5Fuse%5Fnl)) join hint.

### [](#index-hints)Index Hints

You can specify both positive ([INDEX](keyspace-hints.md#index), [INDEX\_FTS](keyspace-hints.md#index%5Ffts)) and negative ([NO\_INDEX](#no%5Findex), [NO\_INDEX\_FTS](#no%5Findex%5Ffts)) index hints on the same keyspace or alias, provided the list of indexes are non-overlapping.

If an index is included in both the positive and negative hint lists, the optimizer ignores both hints. Similarly, omitting the index list in either a positive or negative hint may result in conflicts, causing the hints to be ignored.

## [](#related-links)Related Links

* [Understand the Cost-Based Optimizer for Queries](cost-based-optimizer.md)
* [Optimizer Hints](optimizer-hints.md)
* [Keyspace Hints](keyspace-hints.md)
* [Query Block Hints](query-hints.md)