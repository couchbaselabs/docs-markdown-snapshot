---
title: EXPLAIN
description: The EXPLAIN statement when used before any SQL++ statement,
  provides information about the execution plan for the statement.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/explain.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:cloud:n1ql:n1ql-language-reference/explain.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/explain.html)

# EXPLAIN

> The EXPLAIN statement when used before any SQL++ statement, provides information about the execution plan for the statement. 

## [](#prerequisites)Prerequisites

To execute this statement, your client must have the same privileges required to run the query being explained. The required privileges depend on your [cluster access credential type](../../clusters/cluster-rbac.md#cluster-access-credential-types).

For example, to explain an `INSERT` statement, your client must have:

| Credential Type | Privilege                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------- |
| Basic           | [Write](../../clusters/cluster-rbac.md#basic-access-credentials)                          |
| Advanced        | [Query Insert](../../clusters/cluster-rbac.md#privileges-for-advanced-access-credentials) |

RBAC Examples 

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

To execute the following statement, your client must have the `Write` / `Query Insert` privilege on `landmark` and the `Read` / `Query Read` privilege on `beer-sample`.

```sqlpp
EXPLAIN INSERT INTO landmark (KEY foo, VALUE bar)
        SELECT META(doc).id AS foo, doc AS bar
        FROM `beer-sample` AS doc WHERE type = "brewery";
```

To execute the following statement, your client must have `Write` / `Query Update` and `Read` / `Query Read` privileges on `landmark`.

```sqlpp
EXPLAIN UPDATE landmark
        USE KEYS "landmark_10090"
        SET nickname = "Squiggly Bridge"
        RETURNING landmark.nickname;
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