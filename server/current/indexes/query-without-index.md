---
title: Query without Indexes
description: Sequential scans enable you to query a keyspace, even if the
  keyspace has no indexes.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/indexes/pages/query-without-index.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:indexes:query-without-index.adoc[]
---

[View original HTML](/server/current/indexes/query-without-index.html)

# Query without Indexes

> Sequential scans enable you to query a keyspace, even if the keyspace has no indexes. 

Examples on this Page

The examples in this topic use the travel-sample dataset which is shipped with Couchbase Server. For instructions on how to install the sample bucket, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).

## [](#sequential-scans)Sequential Scans

If a keyspace does not have any suitable primary or secondary indexes for a query, the Query Service can fall back on a sequential scan of the data to retrieve the document keys. A sequential scan uses an underlying mechanism known as a K/V range scan.

Sequential scans are intended for easy access to data, and are not intended as a high performance solution.

Sequential scans are best suited to small collections where key order is unimportant, or where the overhead of maintaining an index cannot be justified. For larger collections and greater performance, define the appropriate indexes to speed up your queries. For ordered document key operations, a primary index provides the same functionality, and will outperform a sequential scan.

> [!NOTE]
> Sequential scans are unavailable on ephemeral buckets.

## [](#use-sequential-scans)Use Sequential Scans

To query an index using sequential scan, run the query as usual.

If there is a primary index or any suitable secondary index available for the keyspace, the Query Service uses that in preference to sequential scan.

### [](#prerequisites)Prerequisites

##### RBAC Privileges

Users must have the **Query Use Sequential Scans** role on the keyspace to be able to execute a request with a sequential scan. For more information about user roles, see [Authorization](../learn/security/authorization-overview.md).

### [](#examples)Examples

To try the examples in this section, set the query context to the `tenant_agent_01` scope in the travel sample dataset. For more information, see [Query Context](../n1ql/n1ql-intro/queriesandresults.md#query-context).

Example 1\. Check that a collection has no indexes

Query

```sqlpp
SELECT * FROM system:indexes
WHERE scope_id = "tenant_agent_01"
  AND keyspace_id = "users";
```

Result

```json
{
  "results": []
}
```

You should see that collection has no primary or secondary indexes.

Example 2\. Run a query without indexes

Query

```sqlpp
SELECT name FROM users;
```

Result

```json
[
  {
    "name": "Haley Rohan"
  },
  {
    "name": "Johnnie Lind"
  },
  {
    "name": "Verdie Jaskolski"
  },
  {
    "name": "Marc Mills"
  },
  {
    "name": "Valentine Funk"
  },
  {
    "name": "Jocelyn Wuckert"
  },
  {
    "name": "Gretchen Auer"
  },
  {
    "name": "Meghan Homenick"
  },
  {
    "name": "Kraig Hilll"
  },
  {
    "name": "Destini Turcotte"
  },
  {
    "name": "Sienna Cummerata"
  }
]
```

The query returns 11 documents. Notice that the query takes one or more seconds.

Example 3\. Check explain plan for query without index

Query

```sqlpp
EXPLAIN SELECT name FROM users;
```

Result

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "PrimaryScan3",
          "bucket": "travel-sample",
          "index": "#sequentialscan",
          "index_projection": {
            "primary_key": true
          },
          "keyspace": "users",
          "namespace": "default",
          "scope": "tenant_agent_01",
          "using": "sequentialscan"
        },
        {
          "#operator": "Fetch",
          "bucket": "travel-sample",
          "early_projection": [
            "name"
          ],
          "keyspace": "users",
          "namespace": "default",
          "scope": "tenant_agent_01"
        },
        {
          "#operator": "Parallel",
          "~child": {
            "#operator": "Sequence",
            "~children": [
              {
                "#operator": "InitialProject",
                "discard_original": true,
                "preserve_order": true,
                "result_terms": [
                  {
                    "expr": "(`users`.`name`)"
                  }
                ]
              }
            ]
          }
        }
      ]
    },
    "text": "SELECT name FROM users;"
  }
]
```

The explain plan includes a primary scan operator, using `sequentialscan` rather than `gsi.`

The explain plan reports that the primary scan operator uses an index called `#sequentialscan`. This name is a placeholder — in reality there is no index.

## [](#monitor-sequential-scans)Monitor Sequential Scans

You can monitor sequential scans using the `system:completed_requests` catalog.

* Completed requests which used sequential scan include a `primaryScan.Seq` property within the request’s `phaseCounts`, `phaseOperators`, and `phaseTimes`, in addition to the `primaryScan` property.
* In contrast, queries which used a primary index include a `primaryScan.GSI` property within the request’s `phaseCounts`, `phaseOperators`, and `phaseTimes`, in addition to the `primaryScan` property.

The `system:completed_requests` catalog also includes a `~qualifier` field, which indicates the reason why any request was captured. A completed requests qualifier automatically captures any requests where more than 10000 keys have been returned by sequential scans. In most cases, this indicates that you should create an index to support the request.

Statistics on sequential scan usage are also available in request profiling information.

For more information, see [Manage and Monitor Queries](../n1ql/n1ql-manage/monitoring-n1ql-query.md).

### [](#examples-2)Examples

Example 4\. Get completed requests which used sequential scan

Query

```sqlpp
SELECT * FROM system:completed_requests
WHERE phaseCounts.`primaryScan.Seq` IS NOT MISSING;
```

You must wrap the property name `primaryScan.Seq` in backquotes, because the property name contains a period. The period after `phaseCounts` is a separator between nested property names, whereas the period within `primaryScan.Seq` is actually part of the property name.

Result

```json
[
  {
    "completed_requests": {
      "clientContextID": "4eb44ea6-170a-4700-ae79-e22f57100e43",
      "cpuTime": "820.464µs",
      "elapsedTime": "4.728840089s",
      "errorCount": 0,
      "errors": [],
      "n1qlFeatCtrl": 76,
      "node": "127.0.0.1:8091",
      "phaseCounts": {
        "fetch": 11,
        "primaryScan": 11,
        "primaryScan.Seq": 11
      },
      "phaseOperators": {
        "authorize": 1,
        "fetch": 1,
        "primaryScan": 1,
        "primaryScan.Seq": 1,
        "project": 1,
        "stream": 1
      },
      "phaseTimes": {
        "authorize": "8.471µs",
        "fetch": "107.915507ms",
        "instantiate": "19.769µs",
        "parse": "870.813µs",
        "plan": "293.479µs",
        "plan.index.metadata": "17.998µs",
        "plan.keyspace.metadata": "7.601µs",
        "primaryScan": "4.72730895s",
        "primaryScan.Seq": "4.72730895s",
        "project": "161.687µs",
        "run": "4.727550611s",
        "stream": "234.174µs"
      },
      "queryContext": "default:travel-sample.tenant_agent_01",
      "remoteAddr": "127.0.0.1:43164",
      "requestId": "d80b0d08-1794-4932-8188-af7e7e57b7b3",
      "requestTime": "2024-02-09T15:05:09.343Z",
      "resultCount": 11,
      "resultSize": 435,
      "scanConsistency": "unbounded",
      "serviceTime": "4.728754078s",
      "state": "completed",
      "statement": "SELECT name FROM users;",
      "statementType": "SELECT",
      "useCBO": true,
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0",
      "users": "builtin:Administrator",
      "~qualifier": "threshold"
    }
  },
  // ...
]
```

The query returns details of completed requests using a sequential scan, if any are logged.

## [](#manage-sequential-scans)Manage Sequential Scans

In Couchbase Server, sequential scans are switched on globally by default. Administrators must grant the **Query Use Sequential Scans** role to users before users can access the feature, as described under [Prerequisites](#prerequisites) above.

To turn sequential scans off or on globally, use the N1QL Feature Controller setting. (This setting is usually reserved for support purposes.) You must have administrator privileges to change this setting.

You can get or set the N1QL Feature Controller setting in any of the following ways.

__Table 1\. How to get or set the N1QL Feature Controller__
| Method                | At            | See                                                                                                                    | Name of option              |
| --------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| Couchbase Web Console | Cluster-level | [Configure General Settings with the UI: Query Settings](../manage/manage-settings/general-settings.md#query-settings) | **N1QL Feature Controller** |
| CLI                   | Cluster-level | [couchbase-cli setting-query](../cli/cbcli/couchbase-cli-setting-query.md)                                             | \--n1ql-feature-control     |
| REST API              | Cluster-level | [Query Settings REST API](../n1ql-rest-settings/index.md)                                                              | queryN1QLFeatCtrl           |
| REST API              | Node-level    | [Query Admin REST API: Settings Endpoint](../n1ql-rest-admin/index.md#tag-Settings)                                    | n1ql-feat-ctrl              |

To switch off sequential scans globally:

1. Get the current value of N1QL Feature Controller.
2. Find the result of a bitwise OR operation on the current value and the sequential scan control bit `16384` (hex `0x4000`).
3. Set N1QL Feature Controller to the resulting value.

To switch on sequential scans globally:

1. Get the current value of N1QL Feature Controller.
2. Find the result of a bitwise XOR operation on the current value and the sequential scan control bit `16384` (hex `0x4000`).
3. Set N1QL Feature Controller to the resulting value.

The [INFER](../n1ql/n1ql-language-reference/infer.md) command also uses K/V range scan, the mechanism that underlies sequential scan. If you turn off sequential scan globally, then INFER can no longer use sequential scan either.

### [](#examples-3)Examples

Example 5\. Switch Off Sequential Scan Globally

Assuming that the current value of the N1QL Feature Controller is `76`:

OR operation

```sh
echo $(( 76 | 16384 ))
```

Result

```console
16460
```

Set the N1QL Feature Controller to `16460`, using any of the methods described in [Table 1](#n1ql-feat-ctrl).

Example 6\. Switch On Sequential Scan Globally

Assuming that the current value of the N1QL Feature Controller is `16460`:

XOR operation

```sh
echo $(( 16460 ^ 16384 ))
```

Result

```console
76
```

Set the N1QL Feature Controller to `76`, using any of the methods described in [Table 1](#n1ql-feat-ctrl).