---
title: EXPLAIN
description: The EXPLAIN statement when used before any SQL++ statement,
  provides information about the execution plan for the statement.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/explain.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:n1ql:n1ql-language-reference/explain.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/explain.html)

# EXPLAIN

> The EXPLAIN statement when used before any SQL++ statement, provides information about the execution plan for the statement. 

## [](#prerequisites)Prerequisites

To execute the EXPLAIN statement, you must have the privileges required for the SQL++ statement that is being explained. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

RBAC Examples 

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

To execute the following statement, you must have the _Query Insert_ privilege on the `landmark` keyspace and the _Query Select_ privilege on the `` `beer-sample` `` keyspace.

```sqlpp
EXPLAIN INSERT INTO landmark (KEY foo, VALUE bar)
        SELECT META(doc).id AS foo, doc AS bar
        FROM `beer-sample` AS doc WHERE type = "brewery";
```

To execute the following statement, you must have the _Query Insert_, _Query Update_, and _Query Select_ privileges on the `testbucket` keyspace.

```sqlpp
EXPLAIN UPSERT INTO testbucket VALUES ("key1", { "a" : "b" }) RETURNING meta().cas;
```

## [](#syntax)Syntax

```ebnf
explain ::= 'EXPLAIN' statement
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/explain.png) 

The statement consists of the `EXPLAIN` keyword, followed by the query whose execution plan you want to see.

## [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

```sqlpp
EXPLAIN SELECT title, activity, hours
FROM landmark
ORDER BY title;
```

Results

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
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
                    "result_terms": [
                      {
                        "expr": "(`landmark`.`title`)"
                      },
                      {
                        "expr": "(`landmark`.`activity`)"
                      },
                      {
                        "expr": "(`landmark`.`hours`)"
                      }
                    ]
                  }
                ]
              }
            }
          ]
        },
        {
          "#operator": "Order",
          "sort_terms": [
            {
              "expr": "(`landmark`.`title`)"
            }
          ]
        }
      ]
    },
    "text": "SELECT title, activity, hours FROM landmark ORDER BY title;"
  }
]
```