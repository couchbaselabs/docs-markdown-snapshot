---
title: EXPLAIN FUNCTION
description: Use EXPLAIN FUNCTION to expose the execution plan for the SQL++
  subqueries or embedded statements that a specified user-defined function
  contains.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/explainfunction.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/explainfunction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/explainfunction.html)

# EXPLAIN FUNCTION

> Use EXPLAIN FUNCTION to expose the execution plan for the SQL++ subqueries or embedded statements that a specified user-defined function contains. 

## [](#purpose)Purpose

You can request the execution plan for an inline or external user-defined function.

* Inline functions are defined using SQL++ expressions. For an inline function, EXPLAIN FUNCTION returns the query plans for all of the subqueries present in the function body.
* External functions are defined using JavaScript. For an external function, EXPLAIN FUNCTION returns the query plans for all embedded SQL++ queries inside the referenced JavaScript body, or the line number on which a N1QL() call appears. Line numbers are calculated from the beginning of the JavaScript function definition.

The following constraints apply:

* If a user-defined function itself contains other, nested user-defined function executions, EXPLAIN FUNCTION generates the query plan for the specified function only, and not for its nested SQL++ queries.
* If an external function defines an alias for a N1QL() call, EXPLAIN FUNCTION cannot return its line number.

## [](#prerequisites)Prerequisites

| To execute EXPLAIN FUNCTION on …​ | You must have …​                                                                               |
| --------------------------------- | ---------------------------------------------------------------------------------------------- |
| Global inline functions           | **Execute Global Functions** role.                                                             |
| Scoped inline functions           | **Execute Scope Functions** role, with permissions on the specified bucket and scope.          |
| Global external functions         | **Execute Global External Functions** role.                                                    |
| Scoped external functions         | **Execute Scope External Functions** role, with permissions on the specified bucket and scope. |

You must also have the necessary privileges required for the SQL++ statements inside the function.

For more information about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
explain-function ::= 'EXPLAIN' 'FUNCTION' function
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/explain-function.png) 

| function | [Function Name](#name) |
| -------- | ---------------------- |

### [](#name)Function Name

```ebnf
function ::= ( namespace ':' ( bucket '.' scope '.' )? )? identifier
```

![Syntax diagram](../_images/n1ql-language-reference/function.png) 

The name of the function. This is usually an unqualified identifier, such as `func1` or `` `func-1` ``. In this case, the path to the function is determined by the current [query context](../n1ql-intro/queriesandresults.md#query-context).

To get the plan for a global function in a particular namespace, the function name must be a qualified identifier with a namespace, such as `default:func1`. Similarly, to get the plan for a scoped function in a particular scope, the function name must be a qualified identifier with the full path to a scope, such as `` default:`travel-sample`.inventory.func1 ``. For more information, see [Global Functions and Scoped Functions](createfunction.md#context).

> [!NOTE]
> The name of a user-defined function is case-sensitive, unlike that of a built-in function. You must get the plan for the user-defined function using the same case that was used when it was created.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Inline Function Example

In this example, you create an inline function named `func1` and then request the plan for its subquery.

```sqlpp
CREATE FUNCTION func1() {
  (SELECT * FROM default:`travel-sample`.inventory.route)};

EXPLAIN FUNCTION func1;
```

Results

```json
[
  {
    "function": "default:travel-sample.inventory.func1",
    "plans": [
      {
        "cardinality": 24024,
        "cost": 33346.763562464446,
        "plan": {
          "#operator": "Sequence",
          "~children": [
            {
              "#operator": "PrimaryScan3",
              "bucket": "travel-sample",
              "index": "def_inventory_route_primary",
              "index_projection": {
                "primary_key": true
              },
              "keyspace": "route",
              "namespace": "default",
              "optimizer_estimates": {
                "cardinality": 24024,
                "cost": 4108.612246388904,
                "fr_cost": 12.170521655277593,
                "size": 11
              },
              "scope": "inventory",
              "using": "gsi"
            },
            {
              "#operator": "Fetch",
              "bucket": "travel-sample",
              "keyspace": "route",
              "namespace": "default",
              "optimizer_estimates": {
                "cardinality": 24024,
                "cost": 32773.70177195316,
                "fr_cost": 25.36320769946525,
                "size": 569
              },
              "scope": "inventory"
            },
            {
              "#operator": "Parallel",
              "~child": {
                "#operator": "Sequence",
                "~children": [
                  {
                    "#operator": "InitialProject",
                    "discard_original": true,
                    "optimizer_estimates": {
                      "cardinality": 24024,
                      "cost": 33346.763562464446,
                      "fr_cost": 25.387061420349003,
                      "size": 569
                    },
                    "result_terms": [
                      {
                        "expr": "self",
                        "star": true
                      }
                    ]
                  }
                ]
              }
            }
          ]
        },
        "statement": "select self.* from `default`:`travel-sample`.`inventory`.`route`"
      }
    ]
  }
]
```

Example 2\. External Function Example

This example assumes that you have defined a JavaScript library in the current query context named `lib1`.

Add a JavaScript function named `function1` to that library:

```javascript
function function1() {
    SELECT * FROM default:`travel-sample`; (1)
    N1QL("SELECT 100");                    (2)
}
```

| **1** | An embedded SQL++ statement.                   |
| ----- | ---------------------------------------------- |
| **2** | A N1QL() call that executes a SQL++ statement. |

Then create the corresponding SQL++ user-defined function for that JavaScript function, named `jsfunction1`, and request the plan information for the statements within the function definition:

```sqlpp
CREATE FUNCTION jsfunction1() 
  LANGUAGE JAVASCRIPT 
  AS "function1" AT "lib1";

EXPLAIN FUNCTION jsfunction1;
```

Results

```json
[
    {
      "function": "default:travel-sample.inventory.jsfunction1",
      "line_numbers": [
        3                                            (1)
      ],
      "plans": [                                     (2)
        {
          "cardinality": 31591,
          "cost": 47086.49704894546,
          "plan": {
            "#operator": "Authorize",
            "privileges": {
              "List": [
                {
                  "Target": "default:travel-sample",
                  "Priv": 7,
                  "Props": 0
                }
              ]
            },
            "~child": {
              "#operator": "Sequence",
              "~children": [
                {
                  "#operator": "Sequence",
                  "~children": [
                    {
                      "#operator": "PrimaryScan3",
                      "index": "def_primary",
                      "index_projection": {
                        "primary_key": true
                      },
                      "keyspace": "travel-sample",
                      "namespace": "default",
                      "optimizer_estimates": {
                        "cardinality": 31591,
                        "cost": 5402.279801258844,
                        "fr_cost": 12.170627071041082,
                        "size": 11
                      },
                      "using": "gsi"
                    },
                    {
                      "#operator": "Fetch",
                      "keyspace": "travel-sample",
                      "namespace": "default",
                      "optimizer_estimates": {
                        "cardinality": 31591,
                        "cost": 46269.39474997121,
                        "fr_cost": 25.46387878667884,
                        "size": 669
                      }
                    },
                    {
                      "#operator": "Parallel",
                      "~child": {
                        "#operator": "Sequence",
                        "~children": [
                          {
                            "#operator": "InitialProject",
                            "discard_original": true,
                            "optimizer_estimates": {
                              "cardinality": 31591,
                              "cost": 47086.49704894546,
                              "fr_cost": 25.489743820991595,
                              "size": 669
                            },
                            "preserve_order": true,
                            "result_terms": [
                              {
                                "expr": "self",
                                "star": true
                              }
                            ]
                          }
                        ]
                      }
                    }
                  ]
                },
                {
                  "#operator": "Stream",
                  "optimizer_estimates": {
                    "cardinality": 31591,
                    "cost": 47086.49704894546,
                    "fr_cost": 25.489743820991595,
                    "size": 669
                  },
                  "serializable": true
                }
              ]
            }
          },
          "statement": "SELECT * FROM default:`travel-sample` ;"
        }
      ]
    }
  ]
```

| **1** | The line number in the JavaScript function that includes a N1QL() call. |
| ----- | ----------------------------------------------------------------------- |
| **2** | The query plan for the embedded SQL++ statement.                        |

## [](#related-links)Related Links

* For an introduction to user-defined functions, see [User-Defined Functions for Queries](../../guides/javascript-udfs.md).
* For more information about JavaScript functions, see [JavaScript Functions for Query Reference](../../javascript-udfs/javascript-functions-with-couchbase.md).
* To manage JavaScript libraries, see [Query Functions REST API](../../n1ql-rest-functions/index.md).
* To create user-defined functions, see [CREATE FUNCTION](createfunction.md).
* To execute a user-defined function, see [EXECUTE FUNCTION](execfunction.md).
* To include a user-defined function in an expression, see [User-Defined Functions](userfun.md).
* To monitor user-defined functions, see [Monitor Functions](../n1ql-intro/sysinfo.md#sys-functions).
* To drop a user-defined function, see [DROP FUNCTION](dropfunction.md).