---
title: Query Service Metrics
description: A list of the metrics provided by the Query Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/metrics-reference/pages/query-service-metrics.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/metrics-reference/query-service-metrics.html)

# Query Service Metrics

> A list of the metrics provided by the Query Service. 

The following Query Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

As a brief introduction however, this is how you would go about building a REST command for the `n1ql_active_requests` metric.

---

Using CURL to retrieve Query Service metrics

Run the following command from your shell console to get the total number of active requests.

```shell
curl -X GET --location "http://localhost:8091/pools/default/stats/range/n1ql_active_requests" \
    --basic --user Administrator:password
```

---

See [Query Service Metrics Cross Reference](query-service-metrics-cross-reference.md) if you are looking for a metric name you know from an alternative supported or legacy tool.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| n1ql\_active\_requests7.0.0gauge Total number of active requests.                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| n1ql\_allocated\_values7.6.0counter The total number of values allocated in the query engine.                                                                                                                                               |
| n1ql\_at\_plus7.0.0counter Total number of N1QL requests with at\_plus index consistency.                                                                                                                                                   |
| n1ql\_audit\_actions7.0.0counter The total number of audit records sent to the server. Some requests cause more than one audit record to be emitted. Records in the output queue that have not yet been sent to the server are not counted. |
| n1ql\_audit\_actions\_failed7.0.0counter The total number of audit records sent to the server that failed.                                                                                                                                  |
| n1ql\_audit\_requests\_filtered7.0.0counter The number of potentially auditable requests that cause no audit action to be taken.                                                                                                            |
| n1ql\_audit\_requests\_total7.0.0counter The total number of potentially auditable requests sent to the query engine.                                                                                                                       |
| n1ql\_bulk\_get\_errors7.2.4counter Count of errors due to bulk get operations                                                                                                                                                              |
| n1ql\_cancelled7.0.0counter Total number of cancelled requests.                                                                                                                                                                             |
| n1ql\_cas\_mismatch\_errors7.2.4counter Count of CAS mismatch errors                                                                                                                                                                        |
| n1ql\_deletes7.0.0counter Total number of DELETE operations.                                                                                                                                                                                |
| n1ql\_errors7.0.0counter The total number of N1QL errors returned so far.                                                                                                                                                                   |
| n1ql\_index\_scans7.0.0counter Total number of secondary index scans.                                                                                                                                                                       |
| n1ql\_index\_scans\_fts7.2.4counter Total number of index scans performed by FTS.                                                                                                                                                           |
| n1ql\_index\_scans\_gsi7.2.4counter Total number of index scans performed by GSI.                                                                                                                                                           |
| n1ql\_index\_scans\_seq7.6.0counter Total number of sequential scans.                                                                                                                                                                       |
| n1ql\_inserts7.0.0counter Total number of INSERT operations.                                                                                                                                                                                |
| n1ql\_invalid\_requests7.0.0counter Total number of requests for unsupported endpoints.                                                                                                                                                     |
| n1ql\_load7.0.0gauge The current utilization factor of the servicers on the query node.                                                                                                                                                     |
| n1ql\_load\_factor7.6.0gauge The total load factor of the query node.                                                                                                                                                                       |
| n1ql\_mem\_quota\_exceeded\_errors7.2.4counter Count of memory quota exceeded errors                                                                                                                                                        |
| n1ql\_mutations7.0.0counter Total number of document mutations.                                                                                                                                                                             |
| n1ql\_node\_memory7.6.0gauge / bytes The total size of in use memory in the query node.                                                                                                                                                     |
| n1ql\_prepared7.0.0counter Total number of prepared statements executed.                                                                                                                                                                    |
| n1ql\_primary\_scans7.0.0counter Total number of primary index scans.                                                                                                                                                                       |
| n1ql\_primary\_scans\_fts7.2.4counter Total number of primary scans performed by FTS.                                                                                                                                                       |
| n1ql\_primary\_scans\_gsi7.2.4counter Total number of primary scans performed by GSI.                                                                                                                                                       |
| n1ql\_primary\_scans\_seq7.6.0counter Total number of primary sequential scans.                                                                                                                                                             |
| n1ql\_queued\_requests7.0.0gauge Total number of queued requests.                                                                                                                                                                           |
| n1ql\_request\_time7.0.0counter / nanoseconds Total end-to-end time to process all queries.                                                                                                                                                 |
| n1ql\_requests7.0.0counter Total number of N1QL requests.                                                                                                                                                                                   |
| n1ql\_requests\_1000ms7.0.0counter Number of queries that take longer than 1000ms.                                                                                                                                                          |
| n1ql\_requests\_250ms7.0.0counter Number of queries that take longer than 250ms.                                                                                                                                                            |
| n1ql\_requests\_5000ms7.0.0counter Number of queries that take longer than 5000ms.                                                                                                                                                          |
| n1ql\_requests\_500ms7.0.0counter Number of queries that take longer than 500ms.                                                                                                                                                            |
| n1ql\_result\_count7.0.0counter Total number of results (documents) returned by the query engine.                                                                                                                                           |
| n1ql\_result\_size7.0.0counter / bytes Total size of data returned by the query engine.                                                                                                                                                     |
| n1ql\_scan\_plus7.0.0counter Total number of N1QL requests with request\_plus index consistency.                                                                                                                                            |
| n1ql\_selects7.0.0counter Total number of SELECT requests.                                                                                                                                                                                  |
| n1ql\_service\_time7.0.0counter / nanoseconds Time to execute all queries.                                                                                                                                                                  |
| n1ql\_temp\_space\_errors7.6.0counter Count of temp space related errors                                                                                                                                                                    |
| n1ql\_timeouts7.2.4counter Count of request timeout errors                                                                                                                                                                                  |
| n1ql\_transaction\_time7.0.0counter / nanoseconds Total elapsed time of transactions so far.                                                                                                                                                |
| n1ql\_transactions7.0.0counter Total number of transactions.                                                                                                                                                                                |
| n1ql\_unauthorized\_users7.2.4counter Count of unauthorized access errors                                                                                                                                                                   |
| n1ql\_unbounded7.0.0counter Total number of N1QL requests with not\_bounded index consistency.                                                                                                                                              |
| n1ql\_updates7.0.0counter Total number of UPDATE requests.                                                                                                                                                                                  |
| n1ql\_warnings7.0.0counter The total number of N1QL warnings returned so far.                                                                                                                                                               |