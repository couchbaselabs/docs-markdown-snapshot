---
title: Query Service Metrics
description: A list of the metrics provided by the Query Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/metrics-reference/pages/query-service-metrics.adoc
pubDate: 2026-04-18T05:14:52.159Z
link: xref:7.6@server:metrics-reference:query-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
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
| n1ql\_boot\_timestamp\_seconds7.6.0gauge / seconds The time the service booted in fractional seconds since Unix epoch.                                                                                                                      |
| n1ql\_bucket\_reads7.6.0gauge The total number of reads on the bucket.                                                                                                                                                                      |
| n1ql\_bucket\_retries7.6.0gauge The total number of retries on the bucket.                                                                                                                                                                  |
| n1ql\_bucket\_writes7.6.0gauge The total number of writes on the bucket.                                                                                                                                                                    |
| n1ql\_bulk\_get\_errors7.2.4counter Count of errors due to bulk get operations                                                                                                                                                              |
| n1ql\_cancelled7.0.0counter Total number of cancelled requests.                                                                                                                                                                             |
| n1ql\_cas\_mismatch\_errors7.2.4counter Count of CAS mismatch errors                                                                                                                                                                        |
| n1ql\_counter\_cu\_total7.6.0counter / seconds The number of distinct operations recording Compute Units (CUs) with Regulator.                                                                                                              |
| n1ql\_credit\_cu\_total7.6.0counter / seconds The number of Compute Units (CUs) refunded.                                                                                                                                                   |
| n1ql\_credit\_ru\_total7.6.0counter / seconds The number of Read Units (RUs) refunded.                                                                                                                                                      |
| n1ql\_credit\_wu\_total7.6.0counter / seconds The number of Write Units (WUs) refunded.                                                                                                                                                     |
| n1ql\_curl\_call\_errors7.6.2counter The number of CURL() calls made by statements that failed (returned an error).                                                                                                                         |
| n1ql\_curl\_calls7.6.2counter The number of CURL() calls made by statements.                                                                                                                                                                |
| n1ql\_deletes7.0.0counter Total number of DELETE operations.                                                                                                                                                                                |
| n1ql\_errors7.0.0counter The total number of N1QL errors returned so far.                                                                                                                                                                   |
| n1ql\_ffdc\_manual7.6.6counter The total number of ffdc captures triggered due to manual invocation of ffdc admin api                                                                                                                       |
| n1ql\_ffdc\_memory\_rate7.6.6counter The total number of ffdc captures triggered due to memory usage rate increasing by 20% of the average memory usage over the past 2 hours                                                               |
| n1ql\_ffdc\_memory\_threshold7.6.6counter The total number of ffdc captures triggered due to memory usage exceeding the 80% threshold                                                                                                       |
| n1ql\_ffdc\_plus\_queue\_full7.6.6counter The total number of ffdc captures triggered due to the plus-request queue being full                                                                                                              |
| n1ql\_ffdc\_request\_queue\_full7.6.6counter The total number of ffdc captures triggered due to the unbounded-request queue being full                                                                                                      |
| n1ql\_ffdc\_shutdown7.6.6counter The total number of ffdc captures triggered due to shutdown processing exceeding 30 minutes                                                                                                                |
| n1ql\_ffdc\_sigterm7.6.6counter The total number of ffdc captures triggered by a SIGTERM signal                                                                                                                                             |
| n1ql\_ffdc\_stalled\_queue7.6.6counter The total number of ffdc captures triggered due to no requests being processed when the queued requests exceed three times the number of servicers within the last 30 seconds                        |
| n1ql\_ffdc\_total7.6.6counter The total number of ffdc occurrences                                                                                                                                                                          |
| n1ql\_index\_hint\_not\_followed7.6.11counter The total number of index hints not followed                                                                                                                                                  |
| n1ql\_index\_scans7.0.0counter Total number of secondary index scans.                                                                                                                                                                       |
| n1ql\_index\_scans\_fts7.2.4counter Total number of index scans performed by FTS.                                                                                                                                                           |
| n1ql\_index\_scans\_gsi7.2.4counter Total number of index scans performed by GSI.                                                                                                                                                           |
| n1ql\_index\_scans\_seq7.6.0counter Total number of sequential scans.                                                                                                                                                                       |
| n1ql\_inserts7.0.0counter Total number of INSERT operations.                                                                                                                                                                                |
| n1ql\_invalid\_requests7.0.0counter Total number of requests for unsupported endpoints.                                                                                                                                                     |
| n1ql\_load7.0.0gauge The current utilization factor of the servicers on the query node.                                                                                                                                                     |
| n1ql\_load\_factor7.6.0gauge The total load factor of the query node.                                                                                                                                                                       |
| n1ql\_mem\_quota\_exceeded\_errors7.2.4counter Count of memory quota exceeded errrors                                                                                                                                                       |
| n1ql\_meter\_cu\_total7.6.0counter / seconds The number of Compute Units (CUs) recorded.                                                                                                                                                    |
| n1ql\_mutations7.0.0counter Total number of document mutations.                                                                                                                                                                             |
| n1ql\_node\_memory7.6.0gauge / bytes The total size of in use memory in the query node.                                                                                                                                                     |
| n1ql\_node\_rss7.6.1gauge / bytes The resident set size (RSS) of the query node process.                                                                                                                                                    |
| n1ql\_op\_count\_total7.6.0counter / seconds The number of distinct operations recorded with Regulator.                                                                                                                                     |
| n1ql\_prepared7.0.0counter Total number of prepared statements executed.                                                                                                                                                                    |
| n1ql\_primary\_scans7.0.0counter Total number of primary index scans.                                                                                                                                                                       |
| n1ql\_primary\_scans\_fts7.2.4counter Total number of primary scans performed by FTS.                                                                                                                                                       |
| n1ql\_primary\_scans\_gsi7.2.4counter Total number of primary scans performed by GSI.                                                                                                                                                       |
| n1ql\_primary\_scans\_seq7.6.0counter Total number of primary sequential scans.                                                                                                                                                             |
| n1ql\_queued\_requests7.0.0gauge Total number of queued requests.                                                                                                                                                                           |
| n1ql\_reject\_count\_total7.6.0counter / seconds The number of times Regulator instructed an operation to be rejected.                                                                                                                      |
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
| n1ql\_tenant\_kv\_throttle\_count7.6.0gauge The total number of times KV has been throttled for queries on this tenant.                                                                                                                     |
| n1ql\_tenant\_kv\_throttle\_seconds\_total7.6.0gauge / seconds The total amount of time KV has been throttled for queries on this tenant.                                                                                                   |
| n1ql\_tenant\_memory7.6.0gauge / bytes The total size of in use tenant memory.                                                                                                                                                              |
| n1ql\_tenant\_reads7.6.0gauge The total number of reads on the tenant.                                                                                                                                                                      |
| n1ql\_tenant\_retries7.6.0gauge The total number of retries on the tenant.                                                                                                                                                                  |
| n1ql\_tenant\_writes7.6.0gauge The total number of writes on the tenant.                                                                                                                                                                    |
| n1ql\_throttle\_count\_total7.6.0counter / seconds The number of times Regulator instructed an operation to throttle.                                                                                                                       |
| n1ql\_throttle\_seconds\_total7.6.0counter / seconds The total time spent throttling (in seconds).                                                                                                                                          |
| n1ql\_timeouts7.2.4counter Count of request timeout errors                                                                                                                                                                                  |
| n1ql\_transaction\_time7.0.0counter / nanoseconds Total elapsed time of transactions so far.                                                                                                                                                |
| n1ql\_transactions7.0.0counter Total number of transactions.                                                                                                                                                                                |
| n1ql\_unauthorized\_users7.2.4counter Count of unauthorized access errors                                                                                                                                                                   |
| n1ql\_unbounded7.0.0counter Total number of N1QL requests with not\_bounded index consistency.                                                                                                                                              |
| n1ql\_updates7.0.0counter Total number of UPDATE requests.                                                                                                                                                                                  |
| n1ql\_warnings7.0.0counter The total number of N1QL warnings returned so far.                                                                                                                                                               |