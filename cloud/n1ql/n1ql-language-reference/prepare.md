---
title: PREPARE
description: The PREPARE statement prepares a query for repeated execution.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/prepare.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:n1ql:n1ql-language-reference/prepare.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/prepare.html)

# PREPARE

> The PREPARE statement prepares a query for repeated execution. 

## [](#purpose)Purpose

Building plans for SQL++ requests may be expensive, in particular where a cluster has many indexes. Sometimes planning may take more time than actually executing a request.

If you know that a statement text will be executed repeatedly, you can request the SQL++ service to prepare the execution plan beforehand, and then request to execute the prepared plan as many times as needed, thereby avoiding the cost of repeated planning.

## [](#prerequisites)Prerequisites

### [](#authorization)RBAC Privileges

The client executing the PREPARE statement must have the RBAC privileges of the statement being prepared. For more details about cluster access privileges, refer to [Manage Cluster Access Credentials](../../clusters/manage-database-users.md).

RBAC Examples 

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

To execute the following statement, user must have the _Query Select_ privilege on both keyspaces `airport` and `landmark`.

```sqlpp
PREPARE SELECT * FROM airport
WHERE city = (SELECT RAW city FROM landmark)
```

To execute the following statement, user must have the _Query Update_ and _Query Select_ privileges on `hotel`.

```sqlpp
PREPARE UPDATE hotel
SET city = "San Francisco" WHERE lower(city) = "sanfrancisco"
RETURNING *
```

### [](#query-context)Query Context

A prepared statement is created and stored relative to the current _query context_. You can create multiple prepared statements with the same name, each stored relative to a different query context. This enables you to run multiple instances of the same application against different datasets.

To execute a prepared statement, the query context must be the same as it was when the prepared statement was created; otherwise the prepared statement will not be found.

You must therefore set the required query context, or unset the query context if necessary, before creating the prepared statement. If you do not set the query context, it defaults to the empty string.

For further information, refer to [Query Context](../n1ql-intro/queriesandresults.md#query-context).

## [](#syntax)Syntax

```ebnf
prepare ::= 'PREPARE' 'FORCE'? ( name ( 'FROM' | 'AS' ) )? statement
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/prepare.png) 

statement

The full text of the SQL++ statement to prepare. The SQL++ statement may contain parameters. For more details, refer to [Parameters](#parameters) below.

### [](#force)FORCE

\[Optional\] The FORCE keyword forces the query engine to create the prepared statement again, even if a matching prepared statement already exists in the cache. For more details, refer to [Statement Cache](#cache) below.

The FORCE keyword does _not_ enable you to assign a new prepared statement to an existing name.

### [](#from-as-clause)FROM / AS Clause

\[Optional\] The FROM or AS clause enables you to specify a name for the prepared statement.

name

A local name for the prepared statement. If you do not specify a local name for the prepared statement, the query engine generates a UUID from the statement text. For more details, refer to [Result](#result) below.

## [](#parameters)Parameters

A prepared statement may contain parameters. These are replaced by a supplied value when the statement is executed. Parameters may be _named parameters_ or _positional parameters_.

Named parameters are specified by name when the prepared statement is executed. To refer to a named parameter in a statement, use `$` followed by the name of the parameter, e.g. `$city`. See [Example 2](#ex-prepare-names).

Positional parameters are specified by the position of each supplied parameter when the statement is executed. To refer to a positional parameter in a statement, use `$` followed by the position of the supplied parameter. So `$1` refers to the first supplied parameter, `$2` refers to the second supplied parameter, etc. See [Example 3](#ex-prepare-numbers).

You may also use `?` to refer to a positional parameter in a statement. In this case, the order of parameters in the statement must exactly match the order of parameters when the statement is executed. So the first `?` refers to the first supplied parameter, the second `?` refers to the second supplied parameter, etc. See [Example 4](#ex-prepare-positions).

## [](#result)Result

A JSON object that contains the following properties:

name

The full name of the prepared statement. This has the format `[host:port]local-name-or-UUID`, and consists of:

* The host and port of the node where you created the prepared statement, enclosed in square brackets.
* The local name you specified for the prepared statement, or a UUID that was generated from the statement text.

You can use this name to execute a prepared statement without resending the entire statement text. When executing a prepared statement by its name:

* The Query Service first checks whether the executing node contains the prepared statement.
* If not found, the service uses the host information in the name to retrieve the prepared statement from the node where you originally created it.
* If the service cannot find the prepared statement on the original node either, it returns an error.

operator

The execution plan of the statement being prepared.

signature

The signature of the statement being prepared.

text

The full PREPARE statement text.

encoded\_plan

The full prepared statement in encoded format. This is included for backward compatibility.

## [](#cache)Statement Cache

Prepared statements are stored in the prepared statement cache until you restart the Couchbase Server.

In Couchbase Capella, the query engine uses the prepared statement cache to speed up the creation of prepared statements.

When you create a prepared statement with a local name:

* The query engine checks whether a prepared statement with that name already exists.

  * If it does not, the prepared statement is created.
  * If it does, the query engine checks whether the text of your SQL++ statement matches the SQL++ statement associated with the existing prepared statement.

    * If it does not match, a duplicate name error is generated.
    * If it matches, the existing prepared statement is returned. However, if the FORCE keyword is present, the prepared statement is created again.

When you create an anonymous prepared statement, i.e. a prepared statement without a local name:

* The query engine generates a UUID from the statement text.
* The query engine then searches the prepared cache to see if the UUID is already listed.

  * If not found, the statement is created and added to the prepared cache.
  * If found, the existing prepared statement is returned. However, if the FORCE keyword is present, the prepared statement is created again.

> [!NOTE]
> When you create an anonymous prepared statement, if there is a named prepared statement in the cache with identical statement text, the named prepared statement is not returned. The anonymous prepared statement is added to the cache in addition to the named prepared statement.

## [](#auto-reprepare)Manual Reprepare

Couchbase Server 8.0

If no indexes exist when you prepare a statement, then the prepared plan uses a sequential scan. If you create a primary index or a secondary index later, the statement still continues to use the sequential scan and does not automatically benefit from the new indexes.

To manually reprepare a statement, update [system:prepareds](../n1ql-manage/monitoring-n1ql-query.md#sys-prepared) and unset the `planPreparedTime` field for the statement.

For example, to reprepare a prepared statement named `NumParam` on a node with the IP address `127.0.0.1` and port `8091`, use the following query:

```sqlpp
UPDATE system:prepareds USE KEYS ["[127.0.0.1:8091]NumParam"] UNSET planPreparedTime;
```

You can repeat this operation after creating each relevant index to refresh the prepared statement’s plan.

## [](#auto-execute)Auto-Execute

When the _auto-execute_ feature is active, a prepared statement is executed automatically as soon as it is created. This saves you from having to make two separate SQL++ requests in cases where you want to prepare a statement and execute it immediately.

When this feature is active, a SQL++ request to prepare a statement returns the [result of the execution step](../n1ql-intro/queriesandresults.md#results). It does not return the full [result of the preparation step](#result), such as the execution plan. However, the output of the SQL++ request does include a `prepared` field, which contains the full name of the prepared statement. You can use this when you need to execute the prepared statement again.

The auto-execute feature is inactive by default. You can turn the auto-execute feature on or off using the `auto_execute` request-level query setting. For more details, refer to [Configure Queries](../n1ql-manage/query-settings.md#auto%5Fexecute).

## [](#propagation)Statement Propagation

When prepared, new statements are distributed to all query nodes.

In Couchbase Capella, when a query node is started or restarted, the prepared statement cache is primed from another node.

If it is not possible to prime the statement cache from another node, you must prepare the statements again before you can execute them.

## [](#example)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Prepared statement

Query

```sqlpp
PREPARE SELECT * FROM route
WHERE airline = "FL";
```

Result

```JSON
[
  {
    "encoded_plan": "H4sIAAAAAAAA/wEAAP//AAAAAAAAAAA=",
    "featureControls": 12,
    "indexApiVersion": 4,
    "indexScanKeyspaces": {
      "default:travel-sample.inventory.route": false
    },
    "name": "[127.0.0.1:8091]26898aa0-04b2-518c-aa11-2fd13cd377b1",
    "namespace": "default",
    "operator": {
      "#operator": "Authorize",
      "privileges": {
        "List": [
          {
            "Priv": 7,
            "Props": 0,
            "Target": "default:travel-sample.inventory.route"
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
                "bucket": "travel-sample",
                "index": "def_inventory_route_primary",
                "index_projection": {
                  "primary_key": true
                },
                "keyspace": "route",
                "namespace": "default",
                "scope": "inventory",
                "using": "gsi"
              },
              {
                "#operator": "Fetch",
                "bucket": "travel-sample",
                "keyspace": "route",
                "namespace": "default",
                "scope": "inventory"
              },
              {
                "#operator": "Parallel",
                "~child": {
                  "#operator": "Sequence",
                  "~children": [
                    {
                      "#operator": "Filter",
                      "condition": "((`route`.`airline`) = \"FL\")"
                    },
                    {
                      "#operator": "InitialProject",
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
            "#operator": "Stream"
          }
        ]
      }
    },
    "queryContext": "",
    "signature": {
      "*": "*"
    },
    "text": "PREPARE SELECT * FROM route\nWHERE airline = \"FL\";",
    "useCBO": true
  }
]
```

Example 2\. Prepared statement with named parameters

```sqlpp
PREPARE NameParam AS
SELECT * FROM hotel
WHERE city=$city AND country=$country;
```

Example 3\. Prepared statement with numbered parameters

```sqlpp
PREPARE NumParam AS
SELECT * FROM hotel
WHERE city=$1 AND country=$2;
```

Example 4\. Prepared statement with positional parameters

```sqlpp
PREPARE NumParam AS
SELECT * FROM hotel
WHERE city=? AND country=?;
```

## [](#related)Related

* For information on executing the prepared statement, refer to [EXECUTE](execute.md).
* For information on using prepared statements with the `cbq` command line shell, refer to [cbq: The Command Line Shell for SQL++](../n1ql-intro/cbq.md).
* For information on using prepared statements with the Data API (Query Service passthrough), refer to [Manage Data with the Data API](../../data-api-guide/data-api-intro.md).
* For information on using prepared statements with an SDK, refer to [Prepared Statements for Query Optimization](../../../java-sdk/current/concept-docs/n1ql-query.md#prepared-statements-for-query-optimization) and [Parameterized Queries](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md#parameterized-queries).