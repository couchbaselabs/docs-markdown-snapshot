---
title: Manage and Monitor Queries
description: Monitoring and profiling SQL++ queries, Query Service nodes, and
  corresponding system resources is important for smoother operational
  performance and efficiency of the system.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-manage/monitoring-n1ql-query.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-manage/monitoring-n1ql-query.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-manage/monitoring-n1ql-query.html)

# Manage and Monitor Queries

> Monitoring and profiling SQL++ queries, Query Service nodes, and corresponding system resources is important for smoother operational performance and efficiency of the system. In fact, often it’s vital for diagnosing and troubleshooting issues such as query performance, resource bottlenecks, and overloading of various services. 

System keyspaces provide various monitoring details and statistics about individual queries and the Query Service. When running on a cluster with multiple query nodes, stats about all queries on all query nodes are collected in the Query management and monitoring system keyspaces.

For example, this can help identify:

* The top 10 slow or fast queries running on a particular query node or the cluster.
* Resource usage statistics of the Query Service, or resources used for a particular query.
* Details about the active, completed, and prepared queries.
* Find long running queries that are running for more than 2 minutes.

These system keyspaces are transient in nature, and are not persisted to disk or permanent storage. Hence, the information in the keyspaces pertains to the current instantiation of the Query Service.

You can access the Query management and monitoring system keyspaces using any of the following:

* SQL++ from the cbq shell or the Query tab
* A monitoring SDK

Using SQL++ enables you to obtain further insights from the keyspaces.

## [](#authentication-and-client-privileges)Authentication and Client Privileges

Users must have permission to access restricted system keyspaces. For information about cluster credentials, see [Manage Cluster Access Credentials](../../clusters/manage-database-users.md).

## [](#examples-on-this-page)Examples on this Page

In the REST API examples:

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

## [](#vitals)Monitor System Vitals

The `system:vitals` catalog provides data about the running state and health of the query nodes, such as number of logical cores, active threads, queued threads, CPU utilization, memory usage, network utilization, garbage collection percentage, and so on. This information can be useful to assess the current workload and performance characteristics of a query node.

### [](#sys-vitals-get)Get System Vitals

To view system vitals, use a SQL++ query.

* SQL++

To view system vitals with SQL++:

```sqlpp
SELECT * FROM system:vitals;
```

### [](#sys-vital-examples)System Vitals Details

Getting system vitals, as described in [Get System Vitals](#sys-vitals-get), returns results similar to the following.

```json
{
  "uptime": "7h39m32.668577197s",
  "local.time": "2021-04-30 18:42:39.517208807 +0000 UTC m=+27573.945319668",
  "version": "7.0.0-N1QL",
  "total.threads": 191,
  "cores": 2,
  "gc.num": 669810600,
  "gc.pause.time": "57.586373ms",
  "gc.pause.percent": 0,
  "memory.usage": 247985184,
  "memory.total": 11132383704,
  "memory.system": 495554808,
  "cpu.user.percent": 0,
  "cpu.sys.percent": 0,
  "request.completed.count": 140,
  "request.active.count": 0,
  "request.per.sec.1min": 0.0018,
  "request.per.sec.5min": 0.0055,
  "request.per.sec.15min": 0.0033,
  "request_time.mean": "536.348163ms",
  "request_time.median": "54.065567ms",
  "request_time.80percentile": "981.869933ms",
  "request_time.95percentile": "2.543128455s",
  "request_time.99percentile": "4.627922799s",
  "request.prepared.percent": 0
}
```

This catalog contains the following attributes:

| Property                               |                                                                                                                                                                                                    | Schema            |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **bucket.IO.stats**optional            | The number of reads and retries for each bucket.                                                                                                                                                   | Object            |
| **uptime**optional                     | The uptime of the query engine.                                                                                                                                                                    | String (duration) |
| **local.time**optional                 | The local time of the query engine.                                                                                                                                                                | Date (date-time)  |
| **version**optional                    | The version of the query engine.                                                                                                                                                                   | String            |
| **total.threads**optional              | The number of active threads used by the query engine.                                                                                                                                             | Integer           |
| **cores**optional                      | The maximum number of logical cores available to the query engine.                                                                                                                                 | Integer           |
| **ffdc.total**optional                 | The total number of times FFDC has been invoked since the last restart.                                                                                                                            | Integer           |
| **gc.num**optional                     | The target heap size of the next garbage collection cycle.                                                                                                                                         | Long (int64)      |
| **gc.pause.time**optional              | The total time spent pausing for garbage collection since the query engine started (ns).                                                                                                           | String (duration) |
| **gc.pause.percent**optional           | The percentage of time spent pausing for garbage collection since the last time the statistics were checked.                                                                                       | Long (int64)      |
| **healthy**optional                    | False when either the unbounded or plus request queues are full; true otherwise.                                                                                                                   | Boolean           |
| **host.memory.free**optional           | Amount of free memory on the host.                                                                                                                                                                 | Long (int64)      |
| **host.memory.quota**optional          | The host memory quota. This reflects the node-quota setting.                                                                                                                                       | Long (int64)      |
| **host.memory.total**optional          | Total memory on the host.                                                                                                                                                                          | Long (int64)      |
| **host.memory.value\_quota**optional   | This the total document memory quota on the node.                                                                                                                                                  | Long (int64)      |
| **load**optional                       | A calculation for how busy the server is.                                                                                                                                                          | Integer           |
| **loadfactor**optional                 | The moving 15 minute average of the load calculation.                                                                                                                                              | Integer           |
| **memory.usage**optional               | The amount of memory allocated for heap objects (bytes). This increases as heap objects are allocated, and decreases as objects are freed.                                                         | Long (int64)      |
| **memory.total**optional               | The cumulative amount of memory allocated for heap objects (bytes). This increases as heap objects are allocated, but does not decrease when objects are freed.                                    | Long (int64)      |
| **memory.system**optional              | The total amount of memory obtained from the operating system (bytes). This measures the virtual address space reserved by the query engine for heaps, stacks, and other internal data structures. | Long (int64)      |
| **node**optional                       | The name or IP address and port of the node.                                                                                                                                                       | String            |
| **node.allocated.values**optional      | The total number of values allocated to contain documents or computations around documents. (This is only of relevance internally.)                                                                | Integer           |
| **node.memory.usage**optional          | The currently allocated document memory on the node.                                                                                                                                               | Integer           |
| **cpu.user.percent**optional           | CPU usage. The percentage of time spent executing user code since the last time the statistics were checked.                                                                                       | Long (int64)      |
| **cpu.sys.percent**optional            | CPU usage. The percentage of time spent executing system code since the last time the statistics were checked.                                                                                     | Long (int64)      |
| **process.memory.usage**optional       | Current process memory use.                                                                                                                                                                        | Integer           |
| **process.percore.cpupercent**optional | Average CPU usage per core.                                                                                                                                                                        | BigDecimal        |
| **process.rss**optional                | Process RSS (bytes)                                                                                                                                                                                | Integer           |
| **process.service.usage**optional      | The number of active servicers for the dominant workload — unbound queue servicers or plus queue servicers.                                                                                        | Integer           |
| **request.completed.count**optional    | Total number of completed requests.                                                                                                                                                                | Integer           |
| **request.active.count**optional       | Total number of active requests.                                                                                                                                                                   | Integer           |
| **request.per.sec.1min**optional       | Number of query requests processed per second. 1-minute exponentially weighted moving average.                                                                                                     | BigDecimal        |
| **request.per.sec.5min**optional       | Number of query requests processed per second. 5-minute exponentially weighted moving average.                                                                                                     | BigDecimal        |
| **request.per.sec.15min**optional      | Number of query requests processed per second. 15-minute exponentially weighted moving average.                                                                                                    | BigDecimal        |
| **request.queued.count**optional       | Number of queued requests.                                                                                                                                                                         | Integer           |
| **request.quota.used.hwm**optional     | High water mark for request quota use.                                                                                                                                                             | Integer           |
| **request\_time.mean**optional         | End-to-end time to process a query. The mean value.                                                                                                                                                | String (duration) |
| **request\_time.median**optional       | End-to-end time to process a query. The median value.                                                                                                                                              | String (duration) |
| **request\_time.80percentile**optional | End-to-end time to process a query. The 80th percentile.                                                                                                                                           | String (duration) |
| **request\_time.95percentile**optional | End-to-end time to process a query. The 95th percentile.                                                                                                                                           | String (duration) |
| **request\_time.99percentile**optional | End-to-end time to process a query. The 99th percentile.                                                                                                                                           | String (duration) |
| **request.prepared.percent**optional   | Percentage of requests that are prepared statements.                                                                                                                                               | Integer           |
| **servicers.paused.count**optional     | Number of servicers temporarily paused due to memory pressure. (Applies to serverless environments only.)                                                                                          | Integer           |
| **servicers.paused.total**optional     | Number of times servicers have been temporarily paused. (Applies to serverless environments only.)                                                                                                 | Integer           |
| **temp.hwm**optional                   | High water mark for temp space use directly by query. (Doesn't include use by the GSI and Search clients.)                                                                                         | Integer           |
| **temp.usage**optional                 | Current Query temp space use. (Doesn't include use by the GSI and Search clients.)                                                                                                                 | Integer           |

## [](#sys-active-req)Monitor and Manage Active Requests

The `system:active_requests` catalog lists all currently executing active requests or queries.

### [](#sys-active-get)Get Active Requests

To view active requests, use a SQL++ query.

* SQL++

To view active requests with SQL++:

```sqlpp
SELECT * FROM system:active_requests;
```

To get the query plan for active requests, include `meta().plan` in a SQL++ query. See [Query Profiling](#query-monitoring-settings).

* SQL++

To view active requests with SQL++, including the query plan:

```sqlpp
SELECT *, meta().plan FROM system:active_requests;
```

### [](#sys-active-delete)Terminate an Active Request

To terminate an active request, for instance, a non-responding or a long-running query, use a SQL++ query.

* SQL++

To terminate an active request `uuid` with SQL++:

```sqlpp
DELETE FROM system:active_requests WHERE requestId = "uuid";
```

### [](#sys-active-examples)Active Request Details

Getting active requests, as described in [Get Active Requests](#sys-active-get), returns results similar to the following.

```json
[
  {
    "active_requests": {
        "clientContextID": "8c169ed1-9e1a-486a-a1b9-1c2ac8e327a4",
        "cpuTime": "22.915µs",
        "elapsedTime": "30.092625ms",
        "executionTime": "30.012ms",
        "ioTime": "8.366709ms",
        "memoryQuota": 1152921504606846976,
        "n1qlFeatCtrl": 76,
        "node": "127.0.0.1:8091",
        "phaseOperators": {
            "authorize": 1,
            "fetch": 1,
            "primaryScan": 1,
            "project": 1,
            "stream": 1
        },
        "phaseTimes": {
            "authorize": "7.584µs",
            "fetch": "5.708µs",
            "instantiate": "15.708µs",
            "parse": "266.875µs",
            "plan": "13.737208ms",
            "plan.index.metadata": "13.577125ms",
            "plan.keyspace.metadata": "45.915µs",
            "primaryScan": "8.370458ms",
            "project": "666ns",
            "queued": "1.459µs",
            "setup": "62.375µs",
            "stream": "2.542µs"
        },
        "queryContext": "default:travel-sample.inventory",
        "remoteAddr": "127.0.0.1:34064",
        "requestId": "9860351c-d837-4b42-ad2f-a5b3cbcfeb4b",
        "requestTime": "2025-06-05T10:31:34.423Z",
        "scanConsistency": "unbounded",
        "state": "running",
        "statement": "SELECT * FROM system:active_requests;",
        "statementType": "SELECT",
        "useCBO": true,
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "users": "builtin:Administrator",
        "waitTime": "8.376917ms"
    }
  }
]
```

This catalog contains the following attributes:

| Property                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Schema            |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **clientContextID**optional | The opaque ID or context provided by the client. Refer to the [request-level](query-settings.html#client%5Fcontext%5Fid) client\_context\_id parameter for more information.                                                                                                                                                                                                                                                                                                                                            | String            |
| **cpuTime**optional         | The total sum of [execTime](../n1ql-rest-query/index.html#exec%5Ftime) across all operators. **Example:** "90.734075ms"                                                                                                                                                                                                                                                                                                                                                                                                 | String (duration) |
| **elapsedTime**optional     | The time taken from when the request was acknowledged by the service to when the request was completed. It includes the time taken by the service to schedule the request.                                                                                                                                                                                                                                                                                                                                              | String (duration) |
| **errorCount**optional      | Total number of errors encountered while executing the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer           |
| **ioTime**optional          | The total sum of [servTime](../n1ql-rest-query/index.html#serv%5Ftime) across all operators. **Example:** "752.858519ms"                                                                                                                                                                                                                                                                                                                                                                                                | String (duration) |
| **memoryQuota**optional     | The memory quota for the request, in MB. This property is only returned if a memory quota is set for the query.                                                                                                                                                                                                                                                                                                                                                                                                         | Integer           |
| **node**optional            | IP address and port number of the node where the query is executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String            |
| **phaseCounts**optional     | Count of documents processed at selective phases involved in the query execution, such as authorize, index scan, fetch, parse, plan, run, etc. For active requests, this property is dynamic, depending on the documents processed by various phases up to this moment in time. Polling the active requests again may return different values. **Example:** {"fetch":16,"indexScan":187}                                                                                                                                | Object            |
| **phaseOperators**optional  | Indicates the numbers of each kind of query operator involved in different phases of the query processing. For instance, a non-covering index path might involve one index scan and one fetch operator. A join would probably involve two or more fetches, one per keyspace. A union select would have twice as many operator counts, one per each branch of the union. **Example:** {"authorize":1,"fetch":1,"indexScan":2}                                                                                            | Object            |
| **phaseTimes**optional      | Cumulative execution times for various phases involved in the query execution, such as authorize, index scan, fetch, parse, plan, run, etc. For active requests, this property is dynamic, depending on the documents processed by various phases up to this moment in time. Polling the active requests again may return different values. **Example:** {"authorize":"823.631µs","fetch":"656.873µs","indexScan":"29.146543ms","instantiate":"236.221µs","parse":"826.382µs","plan":"11.831101ms","run":"16.892181ms"} | Object            |
| **remoteAddr**optional      | IP address and port number of the client application, from where the query is received.                                                                                                                                                                                                                                                                                                                                                                                                                                 | String            |
| **requestId**optional       | Unique request ID internally generated for the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | UUID (uuid)       |
| **requestTime**optional     | Timestamp when the query is received.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Date (date-time)  |
| **resultCount**optional     | Total number of documents returned in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer           |
| **resultSize**optional      | Total number of bytes returned in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer           |
| **scanConsistency**optional | The value of the query setting Scan Consistency used for the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String            |
| **serviceTime**optional     | Total amount of calendar time taken to complete the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String (duration) |
| **sessionMemory**optional   | The memory session size for the request, in bytes. Each request has a dedicated memory session. When a query requires a document or value, memory is allocated from this session based on the size of the document or value. Once the document or value is processed, the allocated memory is returned back to the session, enabling it to be reused by the request. This metric is available only when node-quota and node-quota-val-percent are configured for the node.                                              | Integer (bytes)   |
| **state**optional           | The state of the query execution, such as completed, running, cancelled. Note that the completed state means that the request was started and completed by the Query service, but it does not mean that it was necessarily successful. The request could have been successful, or completed with errors. To find requests that were successful, use this field in conjunction with the errorCount field: search for requests whose state is completed and whose error count is 0.                                       | String            |
| **statement**optional       | The query statement being executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String            |
| **useCBO**optional          | Whether the cost-based optimizer is enabled for the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean           |
| **usedMemory**optional      | The amount of document memory used to execute the request. This property is only returned if a memory quota is set for the query.                                                                                                                                                                                                                                                                                                                                                                                       | Integer           |
| **userAgent**optional       | Name of the client application or program that issued the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String            |
| **users**optional           | Username with whose privileges the query is run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String            |
| **waitTime**optional        | The total sum of [kernTime](../n1ql-rest-query/index.html#kern%5Ftime) across all operators. **Example:** "1.201307s"                                                                                                                                                                                                                                                                                                                                                                                                   | String (duration) |
| **\~analysis**optional      | An array of text phrases that provide a basic analysis of the request execution. These phrases highlight notable aspects of the execution, such as high document counts during primary scans or warnings related to memory and resource usages. **Example:** \["High IO time","High primary scan document count"\]                                                                                                                                                                                                      | String array      |

For query plan field names and meanings, see [Query Profiling Details](#monitor-profile-details).

## [](#sys-prepared)Monitor and Manage Prepared Statements

The `system:prepareds` catalog provides data about the known prepared statements and their state in a query node’s prepared statement cache. For each prepared statement, this catalog provides information such as name, statement, query plan, last use time, number of uses, and so on.

A prepared statement is created and stored relative to the current [query context](../n1ql-intro/queriesandresults.md#query-context). You can create multiple prepared statements with the same name, each stored relative to a different query context. This enables you to run multiple instances of the same application against different datasets.

When there are multiple prepared statements with the same name in different query contexts, the name of the prepared statement in the `system:prepareds` catalog includes the associated query context in brackets.

### [](#sys-prepared-get)Get Prepared Statements

To get a list of all known prepared statements, use a SQL++ query.

* SQL++

To get a list of all known prepared statements with a SQL++ query:

```sqlpp
SELECT * FROM system:prepareds;
```

To get information about a specific prepared statement, use a SQL++ query.

* SQL++

To get information about a specific prepared statement `example1` with a SQL++ query:

```sqlpp
SELECT * FROM system:prepareds WHERE name = "example1";
```

To get the query plan for prepared statements, include `meta().plan` in a SQL++ query. See [Query Profiling](#query-monitoring-settings).

* SQL++

To view prepared statements with SQL++, including the query plan:

```sqlpp
SELECT *, meta().plan FROM system:prepareds;
```

### [](#sys-prepared-delete)Delete Prepared Statements

To delete a specific prepared statement, use a SQL++ query.

* SQL++

To delete a prepared statement `p1` with a SQL++ query:

```sqlpp
DELETE FROM system:prepareds WHERE name = "p1";
```

To delete all the known prepared statements, use a SQL++ query.

* SQL++

To delete all known prepared statements:

```sqlpp
DELETE FROM system:prepareds;
```

### [](#sys-prepared-examples)Prepared Statement Details

To try the examples in this section, first create a couple of prepared statements.

Create a prepared statement with default query context

For this example, unset the query context. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
PREPARE p1 AS SELECT * FROM `travel-sample`.inventory.airline WHERE iata = "U2";
```

Create a prepared statement with specified query context

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
PREPARE p1 AS SELECT * FROM airline WHERE iata = "U2";
```

Getting prepared statements, as described in [Get Prepared Statements](#sys-prepared-get), returns results similar to the following.

```json
{
  "requestID": "d976e59a-d74e-4350-b0df-fa137099d594",
  "signature": {
    "*": "*",
    "plan": "json"
  },
  "results": [
    {
      "prepareds": {
        "encoded_plan": "H4sIAAAAAAAA/6RTUW/TPBT9K9H5XrbJ30QBMcmIhzJ1AjG0qh3wwKbEJLedmWt71061UIXfjpxkndYhENpbYt97z7nn+GxAtnQVVbk3ykICAgtSsWY6djayMwHy6JWAthXdjr3+TBy0s5Avh7N5qewHaoJXJQXIDSpaqNpEGVmtyfwf1MobOtR2TTY6bg6VZqMtQS6UCdQKWLUiSPgR+u9uFOTdIAg4T6yi4zT+v/sfjOt45Vj/IAh41mttaNmTONUhQn7d4FzxkuL9tL/SEpiyXkMepQ/nA+Sz9rIV+FleaVPtMpjTTU22TG19AZPtcP+5aMp6pbhJcr6AwLe6vO54P+CLQfR+n3zLPh/Y576fcleXe3bfqYydYxsMt/k1NZCR66T+9eAdJO4l+L0NoXQ+nWxhIVAHbZeQWAaNVjxc6YRiefWnXZ6EvYs2VayMIYMneXWiTSSGQOlspXvhsLdXDPyKw0KrqIr97E12gU/PL7D/iMh7q6NWZtpLDwGmUJuYR+JV6ADp1qfCQGaRVouKBzsu28s2vbYd4pFJrZDuBFJOtyE8Go0EbmriJqWVbmOfYKab86aTaz45nRyfJxC9tF2skyoHkDhAKzC0TGeT6Xg2yfwoG8+zvic7yE5mZx+z4oFpxePEZF/eTWaTLMmyFeV19zLo+O3ZsNivAAAA//+q+jhuaAQAAA==",
        "featuresControl": 76,
        "indexApiVersion": 4,
        "indexScanKeyspaces": {
          "default:travel-sample.inventory.airline": false
        },
        "name": "p1", (1)
        "namespace": "default",
        "node": "127.0.0.1:8091",
        "statement": "PREPARE p1 AS SELECT * FROM `travel-sample`.inventory.airline WHERE iata = \"U2\";",
        "uses": 0
      }
    },
    {
      "prepareds": {
        "encoded_plan": "H4sIAAAAAAAA/6STT28TMRDFv8rqcWkrExFAVDLiEKpUIIoaJQUOtNqY3Ulq6tju2Bt1iZbPjry7TWmKQKg3/xnPvPk9zwZkC1dSmXujLCQgsCAVK6YjZyM7EyAPXwloW9LNyOvPxEE7C/myP5sVyn6gOnhVUIDcoKSFqkyUkdWazNOgVt7QQNs12ei4HijNRluCXCgTqBGwakWQ8EN06zYV5G0iCDhPrKLjlP7J3QajKl461j8IAp71WhtadiJOdIiQXzc4U7ykeJftn7IEJqzXkIdp4XyAfNZcNAI/i0ttyl0FM7quyBbpWRfAZNu6/x00Yb1SXCecLyDwrSquWt339KKH3vWTb9Xnvfrcd1lu43LP7jsVsXVsg/42v6IaMnKV6F/13kHiDsGfbQiF8+lkWxYCVdB2CYll0GjE/ZaOKRaXf+vlUbV3q00UK2PI4FFeHWsTiSFQOFvqDhz29ua9vvlgrlVU8/3sTXaOT8/Psf9AyHuro1Zm0qGHAFOoTMwj8Sq0BenGp8BAZpFai4p7Oy6aiyb9th3hkUmtkO4E0pxuh/BwOBS4rojrNK108wDy4HevmK7P6pbibHwyPjpLtfXSttOeYB1A4gCNQJ9pMh1PRtNx5ofZaJZ1b7KD7Hh6+jHreWRf3o2n4ywx2RJ53X4LOnp72nf1KwAA////9+bsZQQAAA==",
        "featuresControl": 76,
        "indexApiVersion": 4,
        "indexScanKeyspaces": {
          "default:travel-sample.inventory.airline": false
        },
        "name": "p1(travel-sample.inventory)", (2)
        "namespace": "default",
        "node": "127.0.0.1:8091",
        "statement": "PREPARE p1 AS SELECT * FROM airline WHERE iata = \"U2\";",
        "uses": 0
      }
    }
  ],
  "status": "success",
  "metrics": {
    "elapsedTime": "25.323496ms",
    "executionTime": "25.173646ms",
    "resultCount": 2,
    "resultSize": 7891,
    "serviceLoad": 12
  }
}
```

In this example, the names of the prepared statements are identical, but they’re associated with different query contexts.

| **1** | The name of the prepared statement for the default query context        |
| ----- | ----------------------------------------------------------------------- |
| **2** | The name of the prepared statement showing the associated query context |

This catalog contains the following attributes:

| Property                    |                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **encoded\_plan**required   | The full prepared statement in encoded format.                                                                                                                                                                                                                                                                                                                                                                      | String            |
| **featureControls**optional | This property is provided for technical support only. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                                                                                                                                               | Integer           |
| **indexApiVersion**optional | This property is provided for technical support only. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                                                                                                                                               | Integer           |
| **name**required            | The name of the prepared statement. This may be a UUID that was assigned automatically, or a name that was user-specified when the statement was created.                                                                                                                                                                                                                                                           | String            |
| **namespace**optional       | The namespace in which the prepared statement is stored. Currently, only the default namespace is available.                                                                                                                                                                                                                                                                                                        | String            |
| **node**optional            | The node on which the prepared statement is stored.                                                                                                                                                                                                                                                                                                                                                                 | String            |
| **statement**required       | The text of the query.                                                                                                                                                                                                                                                                                                                                                                                              | String            |
| **uses**required            | The count of times the prepared statement has been executed.                                                                                                                                                                                                                                                                                                                                                        | Integer           |
| **avgElapsedTime**optional  | The mean time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.    | String (duration) |
| **avgServiceTime**optional  | The mean amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                           | String (duration) |
| **lastUse**optional         | Date and time of last use. This property is only returned when the prepared statement has been executed.                                                                                                                                                                                                                                                                                                            | Date (date-time)  |
| **maxElapsedTime**optional  | The maximum time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements. | String (duration) |
| **maxServiceTime**optional  | The maximum amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                        | String (duration) |
| **minElapsedTime**optional  | The minimum time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements. | String (duration) |
| **minServiceTime**optional  | The minimum amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                        | String (duration) |

For query plan field names and meanings, see [Query Profiling Details](#monitor-profile-details).

## [](#sys-completed-req)Monitor and Manage Completed Requests

By default, the `system:completed_requests` catalog maintains a list of the most recent completed requests that have run longer than a predefined threshold of time. (You can also log completed requests that meet other conditions that you define.)

For each completed request, this catalog maintains information such as requestId, statement text, prepared name (if prepared statement), request time, service time, and so on. This information provides a general insight into the health and performance of the query node and the cluster.

### [](#sys-completed-get)Get Completed Requests

To get a list of all logged completed requests, use a SQL++ query.

* SQL++

To get a list of all logged completed requests using SQL++:

```sqlpp
SELECT * FROM system:completed_requests;
```

The `completed` state means that the request was started and completed by the Query Service, but it does not mean that it was necessarily successful. The request could have been successful, or completed with errors.

To find requests that completed successfully, search for completed requests whose `state` is `completed` and whose `errorCount` field has the value `0`.

* SQL++

To get a list of all logged completed requests, including only successful requests:

```sqlpp
SELECT * FROM system:completed_requests
WHERE state = "completed" AND errorCount = 0;
```

To get the query plan for completed requests, include `meta().plan` in a SQL++ query. See [Query Profiling](#query-monitoring-settings).

* SQL++

To view completed requests with SQL++, including the query plan:

```sqlpp
SELECT *, meta().plan FROM system:completed_requests;
```

### [](#sys-completed-delete)Purge the Completed Requests

To purge a specific completed request, use a SQL++ query.

* SQL++

To purge a completed request `uuid` with SQL++:

```sqlpp
DELETE FROM system:completed_requests WHERE requestId = "uuid";
```

To purge completed requests for a given time period, use a SQL++ query.

* SQL++

To purge the completed requests for a given time period:

```sqlpp
DELETE FROM system:completed_requests WHERE requestTime LIKE "2015-09-09%";
```

### [](#sys-completed-examples)Completed Request Details

To try the examples in this section, first run a query which takes at least 1000 ms (the default value of the `completed-threshold` query setting) to get registered in the `system:completed_requests` keyspace.

Run a long query

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
SELECT * FROM route ORDER BY sourceairport LIMIT 5;
```

Getting completed requests, as described in [Get Completed Requests](#sys-completed-get), returns results similar to the following.

```json
[
  {
    "completed_requests": {
        "clientContextID": "99c776c2-438e-449e-b3f5-7585f2c41b62",
        "cpuTime": "912.042µs",
        "elapsedTime": "10.237875ms",
        "errorCount": 0,
        "errors": [],
        "ioTime": "5.338667ms",
        "memoryQuota": 1152921504606846976,
        "n1qlFeatCtrl": 76,
        "namedArgs": {},
        "phaseCounts": {
            "fetch": 5,
            "indexScan": 5,
            "indexScan.GSI": 5
          },
        "phaseOperators": {
            "authorize": 1,
            "fetch": 1,
            "indexScan": 1,
            "indexScan.GSI": 1,
            "project": 1,
            "stream": 1
          },
        "phaseTimes": {
            "authorize": "19.084µs",
            "fetch": "1.1245ms",
            "indexScan": "4.312417ms",
            "indexScan.GSI": "4.312417ms",
            "instantiate": "233.666µs",
            "parse": "1.087875ms",
            "plan": "1.453375ms",
            "plan.index.metadata": "149.833µs",
            "plan.keyspace.metadata": "13.543µs",
            "project": "49.541µs",
            "queued": "417ns",
            "run": "6.39025ms",
            "setup": "913.667µs",
            "stream": "696µs"
          },
        "queryContext": "default:travel-sample.inventory",
        "remoteAddr": "127.0.0.1:34066",
        "requestId": "73fcdccc-da70-40e9-95f6-f8566acb671c",
        "requestTime": "2025-06-05T10:38:32.904Z",
        "resultCount": 5,
        "resultSize": 17714,
        "scanConsistency": "unbounded",
        "serviceTime": "9.305625ms",
        "sqlID": "4c7b735499e4f5e84d031c1ee327d66e",
        "sessionMemory": 1048576,
        "state": "completed",
        "statement": "SELECT * FROM route ORDER BY sourceairport LIMIT 5;",
        "statementType": "SELECT",
        "useCBO": true,
        "usedMemory": 13374,
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "users": "builtin:Administrator",
        "waitTime": "9.836667ms",
        "~analysis": [
            "High IO time"
          ],
        "~qualifier": "threshold"
     }
  }
]
```

For field names and meanings, see [Active Request Details](#sys-active-examples).

For query plan field names and meanings, see [Query Profiling Details](#monitor-profile-details).

## [](#query-monitoring-settings)Query Profiling

Query profiling enables you to obtain more detailed monitoring information and finer execution timings for any query. You can set query profiling to the following levels:

* `off` — query profiling is disabled.
* `phases` — query profiling is enabled, including information about the phases of query execution.
* `timings` — query profiling is enabled, including information about the phases of query execution, and detailed timing information.

You can set query profiling:

* At the [request level](#enable-settings-per-session-or-per-query), for individual queries.

For more information about Query settings and parameters, see [Configure Queries](query-settings.md).

### [](#enable-settings-per-session-or-per-query)Enable Query Profiling for a Request

To activate profiling at the request level, you can:

* Specify the `profile` setting using the [Data API](../../data-api-guide/data-api-intro.md) (Query Service passthrough).
* Specify the `profile` setting using the [cbq](../n1ql-intro/cbq.md) command line tool.

* REST API
* SQL++

To set query settings using the Data API, specify the parameters in the request body.

---

The following statement sets the profiling to phases:

```sh
curl $BASEURL/_p/query/query/service -u $USER:$PASSWORD \
  -d 'profile=phases&statement=SELECT * FROM `travel-sample`.inventory.airline LIMIT 1'
```

The following statement sets the profiling to timings:

```sh
curl $BASEURL/_p/query/query/service -u $USER:$PASSWORD \
  -d 'profile=timings&statement=SELECT * FROM `travel-sample`.inventory.airline LIMIT 1'
```

To set query settings using the cbq shell, use the `\SET` command.

---

The following statement sets the profiling to phases:

```sqlpp
\set -profile "phases";
SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
```

The following statement sets the profiling to timings:

```sqlpp
\set -profile "timings";
SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
```

The Query tab automatically enables Query profiling, with detailed timing information. To disable or enable Query profiling with the Query tab, specify the **Collect query timings** option using the [Query Settings](../../clusters/query-service/query-workbench.md#query-settings).

## [](#monitor-profile-details)Query Profiling Details

You can access the profiling information:

* In the [query responses](#profile).
* In the [system catalogs](#plan).

When a query executes a user-defined function, profiling information is available for the SQL++ queries within the user-defined function as well.

### [](#profile)Profiling Details in Query Responses

When profiling is enabled:

* If you’re using the Data API or the cbq shell, query profiling information is returned with the query results.
* If you’re using the Query tab, query profiling information is not returned with the query results.

Phases Profile

If you’re using the Data API or the cbq shell, the following statistics are returned when `profile` is set to `phases`:

```json
{
  "requestID": "06d6c1c2-1a8a-4989-a856-7314f9eddee5",
  "signature": {
    "*": "*"
  },
  "results": [
    {
      "airline": {
        "callsign": "MILE-AIR",
        "country": "United States",
        "iata": "Q5",
        "icao": "MLA",
        "id": 10,
        "name": "40-Mile Air",
        "type": "airline"
      }
    }
  ],
  "status": "success",
  "metrics": {
    "elapsedTime": "12.77927ms",
    "executionTime": "12.570648ms",
    "resultCount": 1,
    "resultSize": 254,
    "serviceLoad": 12
  },
  "profile": {
    "phaseTimes": {
      "authorize": "19.629µs",
      "fetch": "401.997µs",
      "instantiate": "147.686µs",
      "parse": "4.545234ms",
      "plan": "409.364µs",
      "primaryScan": "6.103775ms",
      "run": "6.699056ms"
    },
    "phaseCounts": {
      "fetch": 1,
      "primaryScan": 1
    },
    "phaseOperators": {
      "authorize": 1,
      "fetch": 1,
      "primaryScan": 1
    },
    "requestTime": "2021-04-30T18:37:56.394Z",
    "servicingHost": "127.0.0.1:8091"
  }
}
```

Timings Profile

If you’re using the Data API or the cbq shell, the following statistics are returned when `profile` is set to `timings`:

```json
{
  "requestID": "268a1240-6864-43a2-af13-ccb8d1e50abf",
  "signature": {
    "*": "*"
  },
  "results": [
    {
      "airline": {
        "callsign": "MILE-AIR",
        "country": "United States",
        "iata": "Q5",
        "icao": "MLA",
        "id": 10,
        "name": "40-Mile Air",
        "type": "airline"
      }
    }
  ],
  "status": "success",
  "metrics": {
    "elapsedTime": "2.915245ms",
    "executionTime": "2.755355ms",
    "resultCount": 1,
    "resultSize": 254,
    "serviceLoad": 12
  },
  "profile": {
    "phaseTimes": {
      "authorize": "18.096µs",
      "fetch": "388.122µs",
      "instantiate": "31.702µs",
      "parse": "646.157µs",
      "plan": "120.427µs",
      "primaryScan": "1.402918ms",
      "run": "1.936852ms"
    },
    "phaseCounts": {
      "fetch": 1,
      "primaryScan": 1
    },
    "phaseOperators": {
      "authorize": 1,
      "fetch": 1,
      "primaryScan": 1
    },
    "requestTime": "2021-04-30T18:40:13.239Z",
    "servicingHost": "127.0.0.1:8091",
    "executionTimings": {
      "#operator": "Authorize",
      "#stats": {
        "#phaseSwitches": 4,
        "execTime": "1.084µs",
        "servTime": "17.012µs"
      },
      "privileges": {
        "List": [
          {
            "Target": "default:travel-sample.inventory.airline",
            "Priv": 7,
            "Props": 0
          }
        ]
      },
      "~child": {
        "#operator": "Sequence",
        "#stats": {
          "#phaseSwitches": 1,
          "execTime": "2.474µs"
        },
        "~children": [
          {
            "#operator": "PrimaryScan3",
            "#stats": {
              "#itemsOut": 1,
              "#phaseSwitches": 7,
              "execTime": "18.584µs",
              "kernTime": "8.869µs",
              "servTime": "1.384334ms"
            },
            "bucket": "travel-sample",
            "index": "def_inventory_airline_primary",
            "index_projection": {
              "primary_key": true
            },
            "keyspace": "airline",
            "limit": "1",
            "namespace": "default",
            "scope": "inventory",
            "using": "gsi"
          },
          {
            "#operator": "Fetch",
            "#stats": {
              "#itemsIn": 1,
              "#itemsOut": 1,
              "#phaseSwitches": 10,
              "execTime": "25.64µs",
              "kernTime": "1.427752ms",
              "servTime": "362.482µs"
            },
            "bucket": "travel-sample",
            "keyspace": "airline",
            "namespace": "default",
            "scope": "inventory"
          },
          {
            "#operator": "InitialProject",
            "#stats": {
              "#itemsIn": 1,
              "#itemsOut": 1,
              "#phaseSwitches": 9,
              "execTime": "6.006µs",
              "kernTime": "1.825917ms"
            },
            "result_terms": [
              {
                "expr": "self",
                "star": true
              }
            ]
          },
          {
            "#operator": "Limit",
            "#stats": {
              "#itemsIn": 1,
              "#itemsOut": 1,
              "#phaseSwitches": 4,
              "execTime": "2.409µs",
              "kernTime": "2.094µs"
            },
            "expr": "1"
          },
          {
            "#operator": "Stream",
            "#stats": {
              "#itemsIn": 1,
              "#itemsOut": 1,
              "#phaseSwitches": 6,
              "execTime": "46.964µs",
              "kernTime": "1.844828ms"
            }
          }
        ]
      },
      "~versions": [
        "7.0.0-N1QL",
        "7.0.0-4960-enterprise"
      ]
    }
  }
}
```

The `profile` object contains the following attributes:

| Property                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema                                    |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **requestTime**required      | Timestamp when the query was received.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Date (date-time)                          |
| **servicingHost**required    | IP address and port number of the node where the query was executed.                                                                                                                                                                                                                                                                                                                                                                                                                                           | String                                    |
| **phaseCounts**required      | Count of documents processed at selective phases involved in the query execution, such as authorize, index scan, fetch, parse, plan, run, etc. **Example:** {"fetch":16,"indexScan":187}                                                                                                                                                                                                                                                                                                                       | Object                                    |
| **phaseOperators**required   | Indicates the numbers of each kind of query operator involved in different phases of the query processing. For instance, a non-covering index path might involve one index scan and one fetch operator. A join would probably involve two or more fetches, one per keyspace. A union select would have twice as many operator counts, one per each branch of the union. This is in essence the count of all the operators in the executionTimings object. **Example:** {"authorize":1,"fetch":1,"indexScan":2} | Object                                    |
| **phaseTimes**required       | Cumulative execution times for various phases involved in the query execution, such as authorize, index scan, fetch, parse, plan, run, etc. **Example:** {"authorize":"823.631µs","fetch":"656.873µs","indexScan":"29.146543ms","instantiate":"236.221µs","parse":"826.382µs","plan":"11.831101ms","run":"16.892181ms"}                                                                                                                                                                                        | Object                                    |
| **executionTimings**optional | Present only if profile was set to "timings" in the request parameters. The execution details for various phases involved in the query execution, such as kernel and service execution times, number of documents processed at each query operator in each phase, and number of phase switches.                                                                                                                                                                                                                | [Execution Timings](#Execution%5FTimings) |
| **ioTime**optional           | The total sum of [servTime](#serv%5Ftime) across all operators. **Example:** "752.858519ms"                                                                                                                                                                                                                                                                                                                                                                                                                    | String (duration)                         |
| **waitTime**optional         | The total sum of [kernTime](#kern%5Ftime) across all operators. **Example:** "1.201307s"                                                                                                                                                                                                                                                                                                                                                                                                                       | String (duration)                         |
| **cpuTime**optional          | The total sum of [execTime](#exec%5Ftime) across all operators. **Example:** "90.734075ms"                                                                                                                                                                                                                                                                                                                                                                                                                     | String (duration)                         |
| **\~analysis**optional       | An array of text phrases that provide a basic analysis of the request execution. These phrases highlight notable aspects of the execution, such as high document counts during primary scans or warnings related to memory and resource usages. **Example:** \["High IO time","High primary scan document count"\]                                                                                                                                                                                             | String array                              |

**Execution Timings**

| Property              |                                                                  | Schema                    |
| --------------------- | ---------------------------------------------------------------- | ------------------------- |
| **#operator**required | Name of the operator. **Example:** "Fetch"                       | String                    |
| **#stats**required    | Statistics collected for the operator.                           | [Statistics](#Statistics) |
| **\~child**optional   | Further nested operators, each with their own execution timings. | Object                    |

**Statistics**

| Property                   |                                                                                                                                                                                                         | Schema            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **#itemsIn**optional       | Number of input documents to the operator. **Example:** 187                                                                                                                                             | Integer (int32)   |
| **#itemsOut**optional      | Number of output documents after the operator processing. **Example:** 16                                                                                                                               | Integer (int32)   |
| **#phaseSwitches**optional | Number of switches between executing, waiting for services, or waiting for the goroutine scheduler. **Example:** 413                                                                                    | Integer (int32)   |
| **execTime**optional       | Time spent executing the operator code inside SQL++ query engine. **Example:** "128.434µs"                                                                                                              | String (duration) |
| **kernTime**optional       | Time spent waiting to be scheduled for CPU time. **Example:** "15.027879ms"                                                                                                                             | String (duration) |
| **servTime**optional       | Time spent waiting for another service, such as index or data. For index scan, it is time spent waiting for GSI/indexer. For fetch, it is time spent waiting on the KV store. **Example:** "1.590934ms" | String (duration) |

> [!TIP]
> The `kernTime`, `servTime`, and `execTime` statistics can be helpful in troubleshooting query performance issues. For example:
> 
> * A high `servTime` for a low number of items processed is an indication that the indexer or KV store is stressed.
> * A high `kernTime` means there is a downstream issue in the query plan or the query server having many requests to process, so the scheduled waiting time will be more for CPU time.

### [](#plan)Profiling Details in System Catalogs

The [system:active\_requests](#sys-active-req) and [system:completed\_requests](#sys-completed-req) system catalogs always return profiling information regarding query phases: namely, phase times, phase counts, and phase operators.

The [system:active\_requests](#sys-active-req), [system:completed\_requests](#sys-completed-req), and [system:prepareds](#sys-prepared) system catalogs also support the `meta().plan` virtual attribute. This captures the whole query plan, and includes profiling information regarding execution timings.

To get execution timing information from these system catalogs, you must explicitly specify `meta().plan` in the projection list for the SELECT query.

Within these system catalogs, not all statements have a `meta().plan` attribute.

* With [system:active\_requests](#sys-active-req) and [system:completed\_requests](#sys-completed-req), the `meta().plan` attribute is only available for statements that you run when profile is set to `timings`.
* With [system:prepareds](#sys-prepared), the `meta().plan` attribute is available for all statements.

> [!NOTE]
> When request profiling is set to `timings`, profiling information is likely to use 100KB+ per entry in the `system:completed_requests` keyspace.
> 
> * Due to the added overhead of running both profiling and [logging](../../clusters/monitoring/monitoring.md#activity-logs), turn on both of them only when needed. Running only one of them continuously has no noticeable affect on performance.
> * Profiling does not carry any extra cost beyond memory for completed requests, so it’s fine to run it continuously.

Plan Details

Getting the plan for a statement that you ran when the profile was set to `timings` returns results similar to the following.

```json
[
  {
  // ...
    "plan": {
      "#operator": "Authorize",
      "#stats": {
        "#phaseSwitches": 4,
        "execTime": "1.725µs",
        "servTime": "21.312µs"
      },
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
        "#stats": {
          "#phaseSwitches": 2,
          "execTime": "1.499µs"
        },
        "~children": [
          {
            "#operator": "PrimaryScan3",
            "#stats": {
              "#heartbeatYields": 6,
              "#itemsOut": 24024,
              "#phaseSwitches": 96099,
              "execTime": "84.366121ms",
              "kernTime": "3.021901421s",
              "servTime": "69.320752ms"
            },
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
            "#stats": {
              "#heartbeatYields": 7258,
              "#itemsIn": 24024,
              "#itemsOut": 24024,
              "#phaseSwitches": 99104,
              "execTime": "70.34694ms",
              "kernTime": "142.630196ms",
              "servTime": "3.021959695s"
            },
            "bucket": "travel-sample",
            "keyspace": "route",
            "namespace": "default",
            "scope": "inventory"
          },
          {
            "#operator": "InitialProject",
            "#stats": {
              "#itemsIn": 24024,
              "#itemsOut": 24024,
              "#phaseSwitches": 96100,
              "execTime": "15.331951ms",
              "kernTime": "3.219612458s"
            },
            "result_terms": [
              {
                "expr": "self",
                "star": true
              }
            ]
          },
          {
            "#operator": "Order",
            "#stats": {
              "#itemsIn": 24024,
              "#itemsOut": 24024,
              "#phaseSwitches": 72078,
              "execTime": "147.889352ms",
              "kernTime": "3.229055752s"
            },
            "sort_terms": [
              {
                "expr": "(`route`.`sourceairport`)"
              }
            ]
          },
          {
            "#operator": "Stream",
            "#stats": {
              "#itemsIn": 24024,
              "#itemsOut": 24024,
              "#phaseSwitches": 24025,
              "execTime": "11.851634134s"
            }
          }
        ]
      },
      "~versions": [
        "7.0.0-N1QL",
        "7.0.0-4960-enterprise"
      ]
    }
  }
]
```

For field names and meanings, see [Execution Timings](#Execution%5FTimings).

## [](#query-profiling-summary)Query Profiling Summary

The following table summarizes Query profiling behavior.

| Profile is …​ | Query returns …​   | Catalog includes …​ |                 |                    |                       |                        |
| ------------- | ------------------ | ------------------- | --------------- | ------------------ | --------------------- | ---------------------- |
|               | **Queryworkbench** | **cbq**             | **Data API**    | **ActiveRequests** | **CompletedRequests** | **PreparedStatements** |
| off           | —                  | —                   | —               | phases             | phases                | timings                |
| phases        | —                  | phases              | phases          | phases             | phases                | timings                |
| timings       | —                  | phases  timings     | phases  timings | phases  timings    | phases  timings       | timings                |

## [](#related-links)Related Links

* For more information on the system namespace, see [Getting System Information](../n1ql-intro/sysinfo.md).