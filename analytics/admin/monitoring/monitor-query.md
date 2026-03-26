---
title: Use Queries to Monitor a Capella Analytics Cluster
description: Monitor your Capella Analytics cluster by obtaining information
  about query requests that are actively running or that have already been
  completed.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/monitoring/monitor-query.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:analytics:admin:monitoring/monitor-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/monitoring/monitor-query.html)

# Use Queries to Monitor a Capella Analytics Cluster

> Monitor your Capella Analytics cluster by obtaining information about query requests that are actively running or that have already been completed. 

You can use SQL++ queries to monitor and analyze these requests and improve your cluster's performance and efficiency.

## [](#monitor-active-requests)Monitor Active Requests

To view active requests:

1. In your Capella Analytics cluster, to go **Workbench**.
2. Enter the following query in the query editor:  
```sqlpp  
SELECT VALUE r FROM active_requests() AS r;  
```  
The query returns all requests that are active and currently running. See [query results](#query-results) for more information.

## [](#monitor-completed-requests)Monitor Completed Requests

To view completed requests:

1. In your Capella Analytics cluster, to go **Workbench**.
2. Enter the following query in the query editor:  
```sqlpp  
SELECT VALUE r FROM completed_requests() AS r;  
LIMIT 5;  
```  
The query returns five logged completed requests. See [query results](#query-results) for more information.

The `completed` state of a request means that it was started and completed by the Query Service. It does not necessarily mean that it was successful.

To find only requests that were completed successfully, you can search for requests with an `errorCount` field of value `0`:

```sqlpp
SELECT VALUE r FROM completed_requests() AS r;
WHERE state = "completed" AND errorCount = 0;
```

### [](#completed-request-example)Completed Request Example

For this example of a completed request, set the query context to the `inventory` scope in the `travel-sample` dataset.

Query

```sqlpp
SELECT VALUE COUNT(*) FROM airline;
SELECT VALUE al FROM airline al WHERE al.name = '40-Mile Air';
```

Result

```json
[
    {
        "cancellable": true,
        "clientContextID": "e6cf320e-c9a3-4422-ba43-7f094b8b580b",
        "elapsedTime": 0.016,
        "jobCreateTime": "2024-04-25T20:09:30.361",
        "jobEndTime": "2024-04-25T20:09:30.365",
        "jobId": "JID:0.12",
        "jobQueueTime": 0,
        "jobRequiredCPUs": 2,
        "jobRequiredMemory": 688128,
        "jobStartTime": "2024-04-25T20:09:30.361",
        "jobStatus": "TERMINATED",
        "node": "127.0.0.1:9600",
        "plan": "",
        "remoteAddr": "127.0.0.1:55857",
        "requestTime": "2024-04-25T20:09:30.349",
        "scanConsistency": "not_bounded",
        "state": "completed",
        "statement": "SELECT VALUE COUNT(*) FROM airline;",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
        "users": "couchbase",
        "uuid": "2b78e0f1-f27c-4501-8cd0-f88ea688d2a6"
    },
    {
        "cancellable": true,
        "clientContextID": "b58848c3-b267-4711-90a2-2ff1dd300e4a",
        "elapsedTime": 0.022,
        "jobCreateTime": "2024-04-25T20:09:36.389",
        "jobEndTime": "2024-04-25T20:09:36.392",
        "jobId": "JID:0.13",
        "jobQueueTime": 0,
        "jobRequiredCPUs": 2,
        "jobRequiredMemory": 524288,
        "jobStartTime": "2024-04-25T20:09:36.389",
        "jobStatus": "TERMINATED",
        "node": "127.0.0.1:9600",
        "plan": "",
        "remoteAddr": "127.0.0.1:55857",
        "requestTime": "2024-04-25T20:09:36.370",
        "scanConsistency": "not_bounded",
        "state": "completed",
        "statement": "SELECT VALUE al FROM airline al WHERE al.name = '40-Mile Air';",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
        "users": "couchbase",
        "uuid": "2e60af04-9bbc-4876-a2ff-0eebacca6b58"
    }
]
```

## [](#analyze-with-queries)Analyze with Queries

The following queries can help you further analyze your cluster:

* To find the top five slowest queries, use the `elapsedTime` field to sort the array elements.

```sqlpp
SELECT VALUE r FROM completed_requests() AS r
ORDER BY r.elapsedTime DESC LIMIT 5;
```

* To find all queries that take longer than a specific number of minutes to run, filter the array elements where the `elapsedTime` field is less than or equal to X minutes.

```sqlpp
SELECT VALUE r FROM completed_requests() AS r
WHERE r.elapsedTime / 60 > 5;
```

* To find queries that take specific resources like CPU and memory, use the `jobRequiredCPUs` and `jobRequiredMemory` fields to filter the array elements.

```sqlpp
SELECT VALUE r FROM completed_requests() AS r
WHERE r.jobRequiredMemory > 1000000000;
```

## [](#query-results)Query Results

The following information is captured in the query results:

| Name              | Description                                                                                                                                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| statement         | The query's statement.                                                                                                                                                                                                                                                                                                |
| plan              | The query's plan. This only becomes available once the query is completed. If the profiling option is enabled, the plan contains each operator's execution time.                                                                                                                                                      |
| requestTime       | The time at which the request is received.                                                                                                                                                                                                                                                                            |
| state             | The state of the request. One of: received, when the request has been received but the query's job has not been created yet. running, when the query's job has been created and started running. cancelled, when the query has been cancelled. completed, when the query has been completed with or without failures. |
| jobId             | The ID of the job.                                                                                                                                                                                                                                                                                                    |
| jobStatus         | The job status. One of: PENDING, when the job is in the waiting queue. RUNNING, when the job is running. TERMINATED, when the job has finished without failures. FAILURE, when the job has finished with failures. FAILURE\_BEFORE\_EXECUTION, when the job has failed before starting execution.                     |
| jobCreateTime     | The time at which the job for the query is created.                                                                                                                                                                                                                                                                   |
| jobStartTime      | The time at which the job starts execution.                                                                                                                                                                                                                                                                           |
| jobEndTime        | The time at which the job finishes execution.                                                                                                                                                                                                                                                                         |
| jobQueueTime      | The time spent in the waiting queue before the job is executed.                                                                                                                                                                                                                                                       |
| elapsedTime       | The time elapsed between when the request is received and when the job is finished.                                                                                                                                                                                                                                   |
| jobRequiredCPUs   | The number of CPU cores required to run the job.                                                                                                                                                                                                                                                                      |
| jobRequiredMemory | The memory required to run the job.                                                                                                                                                                                                                                                                                   |
| node              | The node that has received the request.                                                                                                                                                                                                                                                                               |
| remoteAddr        | The client IP address.                                                                                                                                                                                                                                                                                                |

## [](#see-also)See Also

* [View Metrics for a Cluster](view-metrics.md)
* [Metrics Reference](#reference:metrics.adoc)