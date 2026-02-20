---
title: Index Service Metrics
description: A list of the metrics provided by the Index Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/metrics-reference/pages/index-service-metrics.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:metrics-reference:index-service-metrics.adoc[]
---

[View original HTML](/server/7.2/metrics-reference/index-service-metrics.html)

# Index Service Metrics

> A list of the metrics provided by the Index Service. 

The following Index-Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| index\_avg\_disk\_bps7.2.0 gauge Sum of disk bytes written per second, of all indexes, located on this node                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- |
| index\_avg\_drain\_rate7.0.0 gauge Average number of documents indexed per second, for this index                                                 |
| index\_avg\_item\_size7.0.0 gauge / bytes Average size of the indexed items, for this index                                                       |
| index\_avg\_mutation\_rate7.2.0 gauge Sum of mutation rates of all indexes, located on this node                                                  |
| index\_avg\_resident\_percent7.2.0 gauge Average resident percent across all indexes, located on this node                                        |
| index\_avg\_scan\_latency7.0.0 gauge / Nanoseconds Average latency observed by the index scans, for this index                                    |
| index\_cache\_hits7.0.0 counter Number of times the required index page is found in memory, for this index                                        |
| index\_cache\_misses7.0.0 counter Number of times the required index page is NOT found in memory, for this index                                  |
| index\_data\_size7.0.0 gauge / bytes The approximate size of the valid uncompressed index data, for this index                                    |
| index\_data\_size\_on\_disk7.0.0 gauge / bytes The size of the valid compressed index data, for this index                                        |
| index\_disk\_size7.0.0 gauge / bytes Total disk space taken up by this index, after compression. This includes index data files, checkpoints etc. |
| index\_frag\_percent7.0.0 gauge Percentage of invalid index data, for this index                                                                  |
| index\_items\_count7.0.0 gauge The actual number of items present in the latest index snapshot, for this index                                    |
| index\_log\_space\_on\_disk7.0.0 gauge / bytes The size of the index data files - including garbage, for this index                               |
| index\_memory\_quota7.0.0 gauge / bytes Configured memory quota for the index service nodes                                                       |
| index\_memory\_rss7.2.0 gauge / bytes Resident set size of the indexer process, running on this node                                              |
| index\_memory\_total\_storage7.2.0 gauge / bytes Amount of memory used by the index memory allocator, on this node                                |
| index\_memory\_used7.0.0 gauge / bytes The memory used by this index                                                                              |
| index\_memory\_used\_storage7.2.0 gauge / bytes Amount of memory used by underlying index storage, on this node                                   |
| index\_memory\_used\_total7.0.0 gauge / bytes Total memory used by the indexer process                                                            |
| index\_num\_docs\_indexed7.0.0 counter Number of document updates (of type insert, modify, delete) observed by this index                         |
| index\_num\_docs\_pending7.0.0 gauge Number of pending updates that are yet to be received by index service, for this index                       |
| index\_num\_docs\_queued7.0.0 gauge Number of updates queued (but not yet processed) by index service, for this index                             |
| index\_num\_indexes7.2.0 gauge Total number of indexes, located on this node                                                                      |
| index\_num\_requests7.0.0 counter Number of scan requests received by the index service, for this index                                           |
| index\_num\_rows\_returned7.0.0 counter Number of rows/index entries returned as the scan result during index scans, for this index               |
| index\_num\_rows\_scanned7.0.0 counter Number of rows/index entries read during the index scans, for this index                                   |
| index\_num\_storage\_instances7.2.0 gauge Total number of storage instances, located on this node                                                 |
| index\_raw\_data\_size7.0.0 gauge / bytes Encoded, uncompressed size of the index data, for this index                                            |
| index\_recs\_in\_mem7.0.0 gauge Number of index entries cached in memory, for this index                                                          |
| index\_recs\_on\_disk7.0.0 gauge Number of index entries stored on disk, which are not cached in memory, for this index                           |
| index\_resident\_percent7.0.0 gauge Ratio of records in memory to total records, for this index                                                   |
| index\_scan\_bytes\_read7.0.0 counter / bytes Number of bytes read from the index storage during index scans, for this index                      |
| index\_total\_data\_size7.2.0 gauge / bytes Sum of data size of all indexes, located on this node                                                 |
| index\_total\_disk\_size7.2.0 gauge / bytes Sum of disk size of all indexes, located on this node                                                 |
| index\_total\_drain\_rate7.2.0 gauge Sum of drain rate of all indexes, located on this node                                                       |
| index\_total\_requests7.2.0 counter Sum of number of requests received by all indexes, located on this node                                       |
| index\_total\_rows\_returned7.2.0 counter Sum of number of rows returned during index scan across all indexes, located on this node               |
| index\_total\_rows\_scanned7.2.0 counter Sum of number of rows scanned during index scans across all indexes, located on this node                |
| index\_total\_scan\_duration7.0.0 counter / Nanoseconds Total time taken by the scans requests, for this index                                    |