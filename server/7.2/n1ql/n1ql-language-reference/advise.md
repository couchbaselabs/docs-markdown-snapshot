---
title: ADVISE
description: The ADVISE statement provides index recommendations to optimize
  query response time.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/advise.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/advise.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/advise.html)

# ADVISE

> The ADVISE statement provides index recommendations to optimize query response time. 

## [](#purpose)Purpose

The ADVISE statement invokes the _index advisor_ to provide index recommendations for a single query. You can use the ADVISE statement with any of the following types of query:

* [SELECT](selectintro.md) queries
* [UPDATE](update.md) queries
* [DELETE](delete.md) queries
* [MERGE](merge.md) queries

The index advisor can recommend regular secondary indexes, partial indexes, and array indexes for the following predicates and conditions:

* Predicates in the WHERE clause
* Join conditions in the ON clause for INDEX JOIN, ANSI JOIN, ANSI NEST, INDEX NEST, and ANSI MERGE operations
* Predicates of elements in an UNNEST array
* Predicates with the ANY expression
* Predicates of subqueries in the FROM clause

The index advisor also suggests covering indexes and covering array indexes for queries in a single keyspace, including JOIN operations, ANY expressions, and UNNEST predicates.

The index advisor checks the indexes currently used by the query. If the query is already using the recommended indexes, the index advisor informs you, and does not recommend an index unnecessarily. Similarly, if the query is already using the optimal covering index, the index advisor informs you, and does not recommend a covering index.

## [](#prerequisites)Prerequisites

To execute the ADVISE statement, you must have the privileges required for the SQL++ statement for which you want advice. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
advise ::= 'ADVISE' 'INDEX'? ( select | update | delete | merge )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/advise.png) 

The statement consists of the `ADVISE` keyword, and optionally the `INDEX` keyword, followed by the query for which you want index advice — a [SELECT](selectintro.md) query, an [UPDATE](update.md) query, a [DELETE](delete.md) query, or a [MERGE](merge.md) query.

## [](#usage)Usage

When you run an ADVISE statement in the Query Workbench, you can use the **Table**, **JSON**, or **Tree** link to see the result, just like any other query. You can also use the **Advice** link in the Query Workbench to see the result of the ADVISE statement in graphical format.

## [](#return-value)Return Value

The ADVISE statement returns an object with the following properties.

| Name                     | Description                                       | Schema            |
| ------------------------ | ------------------------------------------------- | ----------------- |
| **#operator** _required_ | The name of the operator — in this case, Advise.  | string            |
| **advice** _required_    | An object giving advice returned by the operator. | [Advice](#advice) |
| **query** _required_     | The SQL++ query used to generate the advice.      | string            |

**Advice**

| Name                      | Description                                           | Schema                      |
| ------------------------- | ----------------------------------------------------- | --------------------------- |
| **#operator** _required_  | The name of the operator — in this case, IndexAdvice. | string                      |
| **adviseinfo** _required_ | An object giving index information.                   | [Information](#information) |

**Information**

| Name                                | Description                                                                                                                                                                                                                                      | Schema                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **current\_indexes** _required_     | An array of Index objects, each giving information about one of the indexes (primary or secondary) that is currently used by the query.                                                                                                          | < [Indexes](#indexes) \> array                |
| **recommended\_indexes** _required_ | If the index advisor recommends any indexes, this is an object giving information about the recommended indexes. If the index advisor cannot recommend any indexes, this is a string stating that there are no recommended indexes at this time. | [Recommended Indexes](#recommended%5Findexes) |

**Recommended Indexes**

| Name                             | Description                                                                                                                                                                                                                        | Schema                         |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **covering\_indexes** _optional_ | If there are any recommended covering indexes, this is an array of Index objects, each giving information about one of the recommended covering indexes. If there are no recommended covering indexes, this field does not appear. | < [Indexes](#indexes) \> array |
| **indexes** _required_           | An array of Index objects, each giving information about one of the recommended secondary indexes.                                                                                                                                 | < [Indexes](#indexes) \> array |

**Indexes**

| Name                              | Description                                                                                                                                                                                                                                                                                                                                 | Schema |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **index\_statement** _required_   | The SQL++ command used to define the index.                                                                                                                                                                                                                                                                                                 | string |
| **keyspace\_alias** _required_    | The keyspace to which the index belongs. If the query specifies an alias for this keyspace, the alias is appended to the keyspace name, joined by an underscore. This may help to distinguish the indexes for either side of a JOIN operation.                                                                                              | string |
| **index\_property** _optional_    | The [index pushdowns](#pushdown-properties) supported by the index. This field is only returned for covering indexes. If no index pushdowns are supported by the covering index, this field does not appear.                                                                                                                                | string |
| **index\_status** _optional_      | Information on the status of the index, stating whether the index is identical to the recommended index, or whether the index is an optimal covering index. This field is only returned for current indexes. If the index is not identical to the recommended index, or if it is not an optimal covering index, this field does not appear. | string |
| **recommending\_rule** _optional_ | The [rules](#recommendation-rules) used to generate the recommendation. This field is only returned for recommended indexes, or for current indexes if they are identical to the recommended index.                                                                                                                                         | string |
| **update\_statistics** _optional_ | The SQL++ command recommended for updating statistics on the index, for use by the cost-based optimizer. This field is only returned for indexes which are recommended by the cost-based optimizer, and only if optimizer statistics are missing for the index.                                                                             | string |

### [](#recommendation-rules)Recommendation Rules

The index advisor recommends secondary indexes based on the query predicate.

In Couchbase Server 7.0 and later, the index advisor initially makes use of the [cost-based optimizer](cost-based-optimizer.md). To do this, the cost-based optimizer must be enabled, and statistics for the keyspace must already exist. If these prerequisites are met, the cost-based optimizer analyzes the query predicate and attempts to recommend an index.

If the cost-based optimizer cannot recommend an index, the index advisor falls back on a rules-based approach. The rules are listed below in priority order. Within each recommended index, if there is more than one index key, they are sorted according to the priority order of these rules.

| Rule                                       | Description                                                                                                                                                                                                                                                                        | Recommendation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Leading array index for UNNEST             | The query uses a predicate which applies to individual elements in an unnested array. Example UNNEST schedule AS x WHERE x.day = 1                                                                                                                                                 | An [array index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#array-index), where the leading index key is an array expression indexing all elements in the unnested array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Equality / NULL / MISSING                  | The query has a predicate with an [equality](comparisonops.md), [IS NULL](comparisonops.md), or [IS MISSING](comparisonops.md) expression. Examples WHERE ANY v IN schedule SATISFIES v.utc = "19:00" END WHERE LOWER(name) = "john" WHERE id = 10                                 | If the predicate contains an [ANY](collectionops.md#collection-op-any) expression: an [array index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#array-index), where the index key is an array expression recursively indexing all elements referenced by the predicate expression. If the predicate contains an indexable function: a [functional index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#functional-index), where the index key contains the function referenced by the predicate expression. Otherwise: a [secondary index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#secondary-index), where one index key is the field referenced by the predicate expression. |
| IN predicates                              | The query has a predicate with an [IN](collectionops.md#collection-op-in) expression. Examples WHERE ANY v IN schedule SATISFIES v.utc IN \["19:00", "20:00"\] END WHERE LOWER(name) IN \["jo", "john"\] WHERE id IN \[10, 20\]                                                    | Refer to [Rule 2](#rule-2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Not less than / between / not greater than | The query has a predicate with a [<=](comparisonops.md), [BETWEEN](comparisonops.md), or [\>=](comparisonops.md) expression. Examples WHERE ANY v IN schedule SATISFIES v.utc BETWEEN "19:00" AND "20:00" END WHERE LOWER(name) BETWEEN "jo" AND "john" WHERE id BETWEEN 10 AND 25 | Refer to [Rule 2](#rule-2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Less than / greater than                   | The query has a predicate with a [<](comparisonops.md) or [\>](comparisonops.md) expression. Examples WHERE ANY v IN schedule SATISFIES v.utc > "19:00" END WHERE LOWER(name) > "jo" WHERE id > 10 AND id < 25                                                                     | Refer to [Rule 2](#rule-2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Derived join filter as leading key         | The query has a [join](join.md) using an ON clause which filters on the left-hand side keyspace. Example FROM route r JOIN airline a ON r.airlineid = META(a).id                                                                                                                   | A [secondary index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#secondary-index), where the leading index key is the field from the left-hand side keyspace in the ON clause.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| IS NOT NULL / MISSING / VALUED predicates  | The query has a predicate with [IS NOT NULL](comparisonops.md), [IS NOT MISSING](comparisonops.md), or [IS NOT VALUED](comparisonops.md). Examples WHERE ANY v IN schedule SATISFIES v.utc IS NOT NULL END WHERE LOWER(name) IS NOT NULL WHERE id IS NOT NULL                      | Refer to [Rule 2](#rule-2).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| LIKE predicates                            | The query has a predicate with a [LIKE](comparisonops.md) expression, where there is a % wildcard at the start of the match string. Example WHERE name LIKE "%base"                                                                                                                | A [secondary index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#secondary-index), where one index key is the field referenced by the predicate expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Non-static join predicate                  | The query has a [join](join.md) using an ON clause in which neither the left-hand side source object nor the right-hand side source object is static. Example FROM route r JOIN airline a ON r.airline = a.iata                                                                    | A [secondary index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#secondary-index), where one index key is the field from the right-hand side keyspace in the ON clause.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Flavor for partial index                   | The query includes filters on a particular [flavor](infer.md#schema-output) of document. Example WHERE type = "hotel"                                                                                                                                                              | A [partial index](../../learn/services-and-indexes/indexes/indexing-and-query-perf.md#partial-index) for that flavor of document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### [](#pushdown-properties)Pushdown Properties

The index advisor optimizes any covering indexes that it recommends, in order to support the following pushdowns:

* LIMIT pushdown
* OFFSET pushdown
* ORDER pushdown
* Partial GROUP BY and aggregates pushdown
* Full GROUP BY and aggregates pushdown

The GROUP BY and aggregate pushdowns support aggregation using the [MIN()](aggregatefun.md#min), [MAX()](aggregatefun.md#max), [SUM()](aggregatefun.md#sum), [COUNTN()](aggregatefun.md#countn), and [AVG()](aggregatefun.md#avg) functions, with the [DISTINCT](aggregatefun.md#aggregate-quantifier) aggregate quantifier if necessary.

The GROUP BY and aggregate pushdowns may be _full_ or _partial_. Full pushdown means the indexer handles the group aggregation fully, and the query engine can skip the entire operator. Partial pushdown means the indexer sends part of the group aggregation to the query, and the query engine merges the intermediate groups to create the final group and aggregation.

### [](#index-names)Index Names

The index advisor suggests a name for each index it recommends, starting with `adv_`, followed by the `DISTINCT` or `ALL` keyword for array indexes if applicable, and including the names of the fields referenced in the index definition, separated by underscores — for example, `adv_city_type_name`. Some field names may be truncated if they are too long.

> [!NOTE]
> The names that the index advisor suggests are not guaranteed to be unique. You should check the suggested index names and change any that are duplicates.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Recommended index only

Assume that the cost-based optimizer is enabled, and that statistics exist for the keyspace.

```sqlpp
ADVISE SELECT * FROM hotel a WHERE a.country = 'France';
```

Result

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [
          {
            "index_statement": "CREATE PRIMARY INDEX def_inventory_hotel_primary ON `default`:`travel-sample`.`inventory`.`hotel`",
            "keyspace_alias": "hotel_a"
          }
        ],
        "recommended_indexes": {
          "indexes": [
            {
              "index_statement": "CREATE INDEX adv_country ON `default`:`travel-sample`.`inventory`.`hotel`(`country`)",
              "keyspace_alias": "hotel_a",
              "recommending_rule": "Index keys follow cost-based order.", (1)
              "update_statistics": "UPDATE STATISTICS FOR `default`:`travel-sample`.`inventory`.`hotel`(`country`)" (2)
            }
          ]
        }
      }
    },
    "query": "SELECT * FROM `travel-sample`.inventory.hotel a WHERE a.country = 'France';"
  }
]
```

| **1** | Index is recommended by the cost-based optimizer |
| ----- | ------------------------------------------------ |
| **2** | Recommended command for updating statistics      |

Example 2\. Recommended index and covering index

```sqlpp
ADVISE SELECT airportname FROM airport
WHERE geo.alt NOT BETWEEN 0 AND 100;
```

Result

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [
          {
            "index_statement": "CREATE PRIMARY INDEX idx_airport_primary ON `default`:`travel-sample`.`inventory`.`airport`",
            "keyspace_alias": "airport"
          }
        ],
        "recommended_indexes": {
          "covering_indexes": [
            {
              "index_statement": "CREATE INDEX adv_geo_alt_airportname ON `default`:`travel-sample`.`inventory`.`airport`(`geo`.`alt`,`airportname`)",
              "keyspace_alias": "airport"
            }
          ],
          "indexes": [
            {
              "index_statement": "CREATE INDEX adv_geo_alt ON `default`:`travel-sample`.`inventory`.`airport`(`geo`.`alt`)",
              "keyspace_alias": "airport",
              "recommending_rule": "Index keys follow order of predicate types: 1. Common leading key for disjunction (5. less than/greater than)."
            }
          ]
        }
      }
    },
    "query": "SELECT airportname FROM `travel-sample`.inventory.airport WHERE geo.alt NOT BETWEEN 0 AND 100;"
  }
]
```

Example 3\. Current index is identical to the recommended index

```sqlpp
ADVISE SELECT * FROM landmark
WHERE city LIKE "Par%" OR city LIKE "Lon%";
```

Result

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [
          {
            "index_statement": "CREATE INDEX def_inventory_landmark_city ON `default`:`travel-sample`.`inventory`.`landmark`(`city`)",
            "index_status": "SAME TO THE INDEX WE CAN RECOMMEND",
            "keyspace_alias": "landmark",
            "recommending_rule": "Index keys follow order of predicate types: 1. Common leading key for disjunction (4. not less than/between/not greater than)."
          }
        ],
        "recommended_indexes": "No index recommendation at this time."
      }
    },
    "query": "SELECT * FROM `travel-sample`.inventory.landmark WHERE city LIKE \"Par%\" OR city LIKE \"Lon%\";"
  }
]
```

Example 4\. Current index is an optimal covering index

```sqlpp
ADVISE SELECT city FROM landmark
WHERE city LIKE "Par%" OR city LIKE "Lon%";
```

Result

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [
          {
            "index_statement": "CREATE INDEX def_inventory_landmark_city ON `default`:`travel-sample`.`inventory`.`landmark`(`city`)",
            "index_status": "THIS IS AN OPTIMAL COVERING INDEX.",
            "keyspace_alias": "landmark"
          }
        ],
        "recommended_indexes": "No index recommendation at this time."
      }
    },
    "query": "SELECT city FROM `travel-sample`.inventory.landmark WHERE city LIKE \"Par%\" OR city LIKE \"Lon%\";"
  }
]
```

Example 5\. No index can be recommended

```sqlpp
ADVISE SELECT * FROM landmark LIMIT 5;
```

Result

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [
          {
            "index_statement": "CREATE PRIMARY INDEX def_inventory_landmark_primary ON `default`:`travel-sample`.`inventory`.`landmark`",
            "keyspace_alias": "landmark"
          }
        ],
        "recommended_indexes": "No index recommendation at this time."
      }
    },
    "query": "SELECT * FROM `travel-sample`.inventory.landmark LIMIT 5;"
  }
]
```

## [](#related-links)Related Links

* The [Index Advisor](../../tools/query-workbench.md#index-advisor) in the Query Workbench
* The [ADVISOR](advisor.md) function
* Blog post: [Index Advisor for N1QL Query Statement](https://blog.couchbase.com/?p=7370&preview=true)