---
title: Search Service Metrics
description: A list of the metrics provided by the Search Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/metrics-reference/pages/search-service-metrics.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:metrics-reference:search-service-metrics.adoc[]
---

[View original HTML](/server/7.6/metrics-reference/search-service-metrics.html)

# Search Service Metrics

> A list of the metrics provided by the Search Service. 

The following Search Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| fts\_avg\_grpc\_queries\_latency7.0.0gauge / milliseconds Average latency per query, using gRPC for streaming, for an index                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fts\_avg\_internal\_queries\_latency7.0.0gauge / milliseconds Average latency of inter-node queries per unit time for an index                                                                                                    |
| fts\_avg\_queries\_latency7.0.0gauge / milliseconds Average latency of queries per unit time for an index                                                                                                                         |
| fts\_batch\_bytes\_added7.0.0counter / bytes Total number of bytes from batches yet to be indexed.                                                                                                                                |
| fts\_batch\_bytes\_removed7.0.0counter / bytes Total number of bytes from batches which have been indexed.                                                                                                                        |
| fts\_curr\_batches\_blocked\_by\_herder7.0.0gauge The difference between the number of batches that have been indexed and the number of batches yet to be indexed                                                                 |
| fts\_doc\_count7.0.0counter Number of documents in the index                                                                                                                                                                      |
| fts\_num\_batches\_introduced7.0.0counter Total number of batches introduced as part of indexing.                                                                                                                                 |
| fts\_num\_bytes\_ram\_quota7.6.0gauge / bytes The number of bytes allocated by the cluster manager as maximum usable memory for fts service                                                                                       |
| fts\_num\_bytes\_used\_disk7.0.0gauge / bytes The number of bytes used on disk by the index                                                                                                                                       |
| fts\_num\_bytes\_used\_disk\_by\_root7.0.0gauge / bytes The number of bytes used on disk by the root segment                                                                                                                      |
| fts\_num\_bytes\_used\_ram7.0.0gauge / bytes The number of bytes used in memory                                                                                                                                                   |
| fts\_num\_files\_on\_disk7.0.0gauge The number of files on disk for an index                                                                                                                                                      |
| fts\_num\_knn\_search\_requests7.6.0counter Total number of search requests with KNN                                                                                                                                              |
| fts\_num\_mutations\_to\_index7.0.0gauge DCP sequence numbers yet to be indexed for an index                                                                                                                                      |
| fts\_num\_pindexes\_actual7.0.0gauge Total number of pindexes currently                                                                                                                                                           |
| fts\_num\_pindexes\_target7.0.0gauge Planned/expected number of pindexes                                                                                                                                                          |
| fts\_num\_recs\_to\_persist7.0.0gauge The number of entries (terms, records, dictionary rows, etc) by Bleve not yet persisted to storage                                                                                          |
| fts\_num\_root\_filesegments7.0.0gauge The number of file segments in the root segment                                                                                                                                            |
| fts\_num\_root\_memorysegments7.0.0gauge The number of memory segments in the root segment                                                                                                                                        |
| fts\_pct\_cpu\_gc7.0.0gauge / percent The percentage of CPU time spent by an index in garbage collection                                                                                                                          |
| fts\_pct\_used\_ram7.6.0gauge / percent The percentage of RAM quota used by the fts service                                                                                                                                       |
| fts\_tot\_batches\_flushed\_on\_maxops7.0.0counter Total number of batches executed due to the batch size being greater than the maximum number of operations per batch                                                           |
| fts\_tot\_batches\_flushed\_on\_timer7.0.0counter Total number of batches executed at regular intervals                                                                                                                           |
| fts\_tot\_bleve\_dest\_closed7.0.0counter Total number of times Bleve destinations closed                                                                                                                                         |
| fts\_tot\_bleve\_dest\_opened7.0.0counter The number of times Bleve destinations opened                                                                                                                                           |
| fts\_tot\_grpc\_listeners\_closed7.0.0counter Total number of gRPC listeners closed                                                                                                                                               |
| fts\_tot\_grpc\_listeners\_opened7.0.0counter Total number of gRPC listeners opened                                                                                                                                               |
| fts\_tot\_grpc\_queryreject\_on\_memquota7.0.0counter Total number of gRPC queries rejected due to the memory quota being lesser than the estimated memory required for merging search results from all partitions from the query |
| fts\_tot\_grpcs\_listeners\_closed7.0.0counter Total number of gRPC SSL listeners closed                                                                                                                                          |
| fts\_tot\_grpcs\_listeners\_opened7.0.0counter Total number of gRPC SSL listeners opened                                                                                                                                          |
| fts\_tot\_http\_limitlisteners\_closed7.0.0counter Total number of HTTP limit listeners closed                                                                                                                                    |
| fts\_tot\_http\_limitlisteners\_opened7.0.0counter Total number of HTTP limit listeners opened                                                                                                                                    |
| fts\_tot\_https\_limitlisteners\_closed7.0.0counter Total number of HTTPS limit listeners closed                                                                                                                                  |
| fts\_tot\_https\_limitlisteners\_opened7.0.0counter Total number of HTTPS limit listeners opened                                                                                                                                  |
| fts\_tot\_queryreject\_on\_memquota7.0.0counter Total number of queries rejected due to the memory quota being lesser than the estimated memory required for merging search results from all partitions from the query            |
| fts\_tot\_remote\_grpc7.0.0counter Total number of remote(i.e. different node) gRPC requests                                                                                                                                      |
| fts\_tot\_remote\_grpc\_ssl7.6.0counter Total number of remote(i.e. different node) gRPC SSL requests when adding clients.                                                                                                        |
| fts\_tot\_remote\_grpc\_tls7.0.0counter Total number of remote(i.e. different node) gRPC SSL requests when adding clients.                                                                                                        |
| fts\_tot\_remote\_http7.0.0counter Total number of remote(i.e. different node) HTTP requests                                                                                                                                      |
| fts\_tot\_remote\_http27.0.0counter Total number of remote(i.e. different node) HTTP SSL requests                                                                                                                                 |
| fts\_tot\_remote\_http\_ssl7.6.0counter Total number of remote(i.e. different node) HTTP SSL requests                                                                                                                             |
| fts\_total\_bytes\_indexed7.0.0gauge Rate of bytes indexed for an index                                                                                                                                                           |
| fts\_total\_bytes\_query\_results7.0.0counter / bytes Size of results coming back from full text queries for search results, including the entire size of the JSON sent                                                           |
| fts\_total\_compaction\_written\_bytes7.0.0counter / bytes Number of bytes written to disk as a result of compaction                                                                                                              |
| fts\_total\_gc7.0.0counter The number of garbage collection events triggered                                                                                                                                                      |
| fts\_total\_grpc\_internal\_queries7.0.0counter The number of internal gRPC requests from the co-ordinating node for the query to other nodes, for an index                                                                       |
| fts\_total\_grpc\_queries7.0.0counter The total number of queries, using gRPC for streaming, for an index                                                                                                                         |
| fts\_total\_grpc\_queries\_error7.0.0counter The number of queries that resulted in an error, using gRPC for streaming, for an index                                                                                              |
| fts\_total\_grpc\_queries\_slow7.0.0counter The number of queries in the slow query log, using gRPC for streaming, for an index                                                                                                   |
| fts\_total\_grpc\_queries\_timeout7.0.0counter The number of queries that exceeded the timeout, using gRPC for streaming, for an index                                                                                            |
| fts\_total\_internal\_queries7.0.0counter The number of internal queries from the co-ordinating node to other nodes, per unit time for an index                                                                                   |
| fts\_total\_knn\_searches7.6.0counter Total bleve knn search operations                                                                                                                                                           |
| fts\_total\_queries7.0.0counter The number of full text queries per second for an index                                                                                                                                           |
| fts\_total\_queries\_bad\_request\_error7.6.0counter The number of FTS queries that resulted in an error due to a bad request                                                                                                     |
| fts\_total\_queries\_consistency\_error7.6.0counter The number of FTS queries that resulted in an error due to a failure to meet consistency requirements                                                                         |
| fts\_total\_queries\_error7.0.0counter The number of FTS queries for an index that resulted in an error                                                                                                                           |
| fts\_total\_queries\_max\_result\_window\_exceeded\_error7.6.0counter The number of FTS queries that resulted in an error due to exceeding the maximum result window                                                              |
| fts\_total\_queries\_partial\_results\_error7.6.0counter The number of FTS queries that resulted in an error due to only partial results being returned                                                                           |
| fts\_total\_queries\_rejected\_by\_herder7.0.0counter The number of queries rejected by the app herder when the memory used exceeds the application's query quota                                                                 |
| fts\_total\_queries\_search\_in\_context\_error7.6.0counter The number of FTS queries that resulted in an error while searching in context                                                                                        |
| fts\_total\_queries\_slow7.0.0counter The number of FTS queries in the slow query log                                                                                                                                             |
| fts\_total\_queries\_timeout7.0.0counter The number of FTS queries for an index that exceeded the timeout                                                                                                                         |
| fts\_total\_request\_time7.0.0counter / nanoseconds Total time spent processing query requests for an index                                                                                                                       |
| fts\_total\_term\_searchers7.0.0counter Number of bleve term searchers                                                                                                                                                            |
| fts\_total\_term\_searchers\_finished7.0.0counter Total term searchers that have finished serving a query                                                                                                                         |
| fts\_total\_vectors7.6.1gauge The total number of vectors indexed                                                                                                                                                                 |