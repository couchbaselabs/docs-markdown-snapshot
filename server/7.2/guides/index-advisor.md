---
title: Index Advisor
description: How to use the Index Advisor to recommend indexes for your queries.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/index-advisor.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:guides:index-advisor.adoc[]
---

[View original HTML](/server/7.2/guides/index-advisor.html)

# Index Advisor

> How to use the Index Advisor to recommend indexes for your queries.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

You must create an index on a keyspace to be able to query that keyspace. You can improve the performance of your query by using a well-designed index. In Couchbase Server Enterprise Edition, the Index Advisor can analyze your queries and provide recommended indexes to optimize response times.

The Index Advisor works with [SELECT](../n1ql/n1ql-language-reference/selectintro.md), [UPDATE](../n1ql/n1ql-language-reference/update.md), [DELETE](../n1ql/n1ql-language-reference/delete.md), or [MERGE](../n1ql/n1ql-language-reference/merge.md) queries.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#advice-single)Advice for a Single Query

To get index recommendations for a single query, you can use the Index Advisor in the Query Workbench, the `ADVISE` statement, or the `ADVISOR()` function.

* Query Workbench
* ADVISE Statement
* ADVISOR() Function

To get index recommendations for a single query, do one of the following:

* Enter the query in the query editor and click **Index Advisor**.
* Alternatively, if the query has already been executed, click **Advice** in the **Results** area.

The **Results** area displays the details of any current indexes used by the query, and any indexes that the Index Advisor recommends.

If there are any recommended indexes, you can click **Create & Build Indexes** to create them.

Similarly, if there are any recommended covering indexes, you can click **Create & Build Covering Indexes** to create them.

![Index advice for the query](../tools/_images/query-workbench-result-advice.png) 

For more information, see [Index Advisor](../tools/query-workbench.md#index-advisor).

To get index recommendations for a single query, use the `ADVISE` statement, followed by the query for which you want advice.

The `ADVISE` statement returns a JSON object containing the details of any current indexes used by the query, and any indexes that the Index Advisor recommends, along with the reasons for recommendation. For each index, a SQL++ statement is provided: you can copy and run this index statement to create the recommended index.

---

The following example gets index advice for a single query.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

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

For more information, see [ADVISE](../n1ql/n1ql-language-reference/advise.md).

To get index recommendations for a single query, use the `ADVISOR()` function with a string argument, representing the query.

The `ADVISOR()` function returns a JSON object containing the details of any current indexes used by each query, and any indexes that the Index Advisor recommends. For each index, a SQL++ statement is provided: you can copy and run this index statement to create the recommended index.

---

The following example gets index advice for a single query.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT ADVISOR("SELECT * FROM landmark
WHERE activity = 'eat' AND city = 'Paris'") AS Single;
```

Result

```json
[
  {
    "Single": {
      "current_used_indexes": [
        {
          "index": "CREATE INDEX def_inventory_landmark_city ON `default`:`travel-sample`.`inventory`.`landmark`(`city`)",
          "statements": [
            {
              "run_count": 1,
              "statement": "SELECT * FROM `travel-sample`.inventory.landmark\nWHERE activity = 'eat' AND city = 'Paris'"
            }
          ]
        }
      ],
      "recommended_indexes": [
        {
          "index": "CREATE INDEX adv_city_activity ON `default`:`travel-sample`.`inventory`.`landmark`(`city`,`activity`)",
          "statements": [
            {
              "run_count": 1,
              "statement": "SELECT * FROM `travel-sample`.inventory.landmark\nWHERE activity = 'eat' AND city = 'Paris'"
            }
          ]
        }
      ]
    }
  }
]
```

For more information, see [ADVISOR(string)](../n1ql/n1ql-language-reference/advisor.md#advisor-string).

## [](#advisor-function-multiple)Advice for Multiple Queries

The `ADVISOR()` function also enables you to get index recommendations for multiple queries.

To get advice for multiple queries, use the `ADVISOR()` function with an array argument containing strings which represent each query.

> [!TIP]
> You can query the [system:completed\_requests](../manage/monitor/monitoring-n1ql-query.md#sys-completed-req) catalog to get a list of recently completed queries.

The following example gets index advice for recently completed queries.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT ADVISOR((SELECT RAW statement FROM system:completed_requests)) AS Recent;
```

Result

```json
[
  {
    "Recent": {
      "current_used_indexes": [
        {
          "index": "CREATE PRIMARY INDEX def_inventory_route_primary ON `default`:`travel-sample`.`inventory`.`route`",
          "statements": [
            {
              "run_count": 3,
              "statement": "SELECT * FROM `travel-sample`.inventory.route r JOIN `travel-sample`.inventory.airline a ON r.airlineid= META(a).id WHERE a.country = \"France\";"
            },
            {
              "run_count": 2,
              "statement": "SELECT d.id, d.destinationairport, RATIO_TO_REPORT(d.distance) OVER (PARTITION BY d.destinationairport) AS `distance-ratio` FROM `travel-sample`.inventory.route AS d LIMIT 7;"
            },
// ...
          ]
        },
        {
          "index": "CREATE PRIMARY INDEX def_inventory_airport_primary ON `default`:`travel-sample`.`inventory`.`airport`",
          "statements": [
            {
              "run_count": 1,
              "statement": "SELECT airportname FROM `travel-sample`.inventory.airport WHERE geo.alt NOT BETWEEN 0 AND 100;"
            }
          ]
        }
      ],
      "recommended_covering_indexes": [
        {
          "index": "CREATE INDEX adv_geo_alt_airportname ON `default`:`travel-sample`.`inventory`.`airport`(`geo`.`alt`,`airportname`)",
          "statements": [
            {
              "run_count": 1,
              "statement": "SELECT airportname FROM `travel-sample`.inventory.airport WHERE geo.alt NOT BETWEEN 0 AND 100;"
            }
          ]
        }
      ],
      "recommended_indexes": [
        {
          "index": "CREATE INDEX adv_geo_alt ON `default`:`travel-sample`.`inventory`.`airport`(`geo`.`alt`)",
          "statements": [
            {
              "run_count": 1,
              "statement": "SELECT airportname FROM `travel-sample`.inventory.airport WHERE geo.alt NOT BETWEEN 0 AND 100;"
            }
          ]
        },
        {
          "index": "CREATE INDEX adv_airlineid ON `default`:`travel-sample`.`inventory`.`route`(`airlineid`)",
          "statements": [
            {
              "run_count": 3,
              "statement": "SELECT * FROM `travel-sample`.inventory.route r JOIN `travel-sample`.inventory.airline a ON r.airlineid= META(a).id WHERE a.country = \"France\";"
            }
// ...
```

For more information, see [ADVISOR(array)](../n1ql/n1ql-language-reference/advisor.md#advisor-array).

## [](#advisor-function-session)Advice for a Session

The `ADVISOR()` function also enables you to get index recommendations for all the queries that you run in an Index Advisor session.

To run an Index Advisor session:

1. Use the `ADVISOR()` function with a start object argument to start the session. The object argument must contain the property `"action": "start"`, and must also contain a `"duration"` property, specifying the duration of the session.  
The query returns a session ID, which you must use to get the results for this session, and to perform other actions on this session.
2. Run all the queries for which you require index recommendations.
3. If you want to stop the session early, use the `ADVISOR()` function with a stop object argument. The object argument must contain the property `"action": "stop"`, and must also contain a `"session"` property, specifying the session ID.
4. When the session is complete, use the `ADVISOR()` function with a get object argument to get the index recommendations. The object argument must contain the property `"action": "get"`, and must also contain a `"session"` property, specifying the session ID.

> [!NOTE]
> You can also use the `ADVISOR()` function to abandon a session without recording any results; to list active and completed sessions; and to purge the results of an Index Advisor session.

The following example starts an Index Advisor session with a duration of 1 hour. All queries taking longer than 0 seconds will be collected.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT ADVISOR({"action": "start", "response": "0s", "duration": "1h"}) AS Collect;
```

Result

```json
[
  {
    "Collect": {
      "session": "0cd09ae4-a083-4a7e-86cd-85e42c140d60"
    }
  }
]
```

---

The following example stops the Index Advisor session early and saves the results.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT ADVISOR({"action": "stop", "session": "0cd09ae4-a083-4a7e-86cd-85e42c140d60"})
AS Stop;
```

Result

```json
[
  {
    "Stop": []
  }
]
```

---

The following example returns index recommendations for the queries in the Index Advisor session.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT ADVISOR({"action": "get", "session": "0cd09ae4-a083-4a7e-86cd-85e42c140d60"})
AS Get;
```

Result

```json
[
  {
    "Get": [
      [
        {
          "current_used_indexes": [
            {
              "index": "CREATE PRIMARY INDEX idx_airport_primary ON `default`:`travel-sample`.`inventory`.`airport`",
              "statements": [
                {
                  "run_count": 1,
                  "statement": "SELECT airportname FROM `travel-sample`.inventory.airport WHERE geo.alt NOT BETWEEN 0 AND 100;"
                }
              ]
// ...
            }
          ],
          "recommended_covering_indexes": [
            {
              "index": "CREATE INDEX adv_city_name ON `default`:`travel-sample`.`inventory`.`hotel`(`city`,`name`)",
              "statements": [
                {
                  "run_count": 1,
                  "statement": "SELECT h.name, h.city, a.airportname FROM `travel-sample`.inventory.hotel h JOIN `travel-sample`.inventory.airport a ON h.city = a.city LIMIT 5;"
                }
              ]
// ...
            }
          ],
          "recommended_indexes": [
            {
              "index": "CREATE INDEX adv_geo_alt ON `default`:`travel-sample`.`inventory`.`airport`(`geo`.`alt`)",
              "statements": [
                {
                  "run_count": 1,
                  "statement": "SELECT airportname FROM `travel-sample`.inventory.airport WHERE geo.alt NOT BETWEEN 0 AND 100;"
                }
              ]
            }
          ]
        }
      ]
    ]
  }
]
```

For more information, see [ADVISOR(start\_obj)](../n1ql/n1ql-language-reference/advisor.md#advisor-session-start).

## [](#related-links)Related Links

Reference and explanation:

* [Using Indexes](../learn/services-and-indexes/indexes/global-secondary-indexes.md)

Administrator guides:

* [Manage Indexes](../manage/manage-indexes/manage-indexes.md)
* [Monitor Indexes](../manage/monitor/monitoring-indexes.md)

Online Index Advisor tool:

* [Couchbase SQL++ Index Advisor](https://index-advisor.couchbase.com/indexadvisor/#1)

Indexes with SDKs:

* [C](../../../c-sdk/current/concept-docs/n1ql-query.md#indexes)| [C++](../../../cxx-sdk/current/concept-docs/n1ql-query.md#indexes)| [.NET](../../../dotnet-sdk/current/concept-docs/n1ql-query.md#indexes)| [Go](../../../go-sdk/current/concept-docs/n1ql-query.md#indexes)| [Java](../../../java-sdk/current/concept-docs/n1ql-query.md#indexes)| Kotlin | [Node.js](../../../nodejs-sdk/current/concept-docs/n1ql-query.md#indexes)| [PHP](../../../php-sdk/current/concept-docs/n1ql-query.md#indexes)| [Python](../../../python-sdk/current/concept-docs/n1ql-query.md#indexes)| [Ruby](../../../ruby-sdk/current/concept-docs/n1ql-query.md#indexes)| [Scala](../../../scala-sdk/current/concept-docs/n1ql-query.md#indexes)