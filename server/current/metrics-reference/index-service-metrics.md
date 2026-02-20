---
title: Index Service Metrics
description: A list of the metrics provided by the Index Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/index-service-metrics.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:metrics-reference:index-service-metrics.adoc[]
---

[View original HTML](/server/current/metrics-reference/index-service-metrics.html)

# Index Service Metrics

> A list of the metrics provided by the Index Service. 

The following Index-Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

See [Index Service Cross Reference](index-service-metrics-cross-reference.md) if you are looking for a metric name you know from an alternative supported or legacy tool.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| index\_avg\_disk\_bps7.2.0gauge Sum of disk bytes written per second, of all indexes, located on this node                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| index\_avg\_drain\_rate7.0.0gauge Average number of documents indexed per second, for this index                                                                                                                 |
| index\_avg\_item\_size7.0.0gauge / bytes Average size of the indexed items, for this index                                                                                                                       |
| index\_avg\_mutation\_rate7.2.0gauge Sum of mutation rates of all indexes, located on this node                                                                                                                  |
| index\_avg\_resident\_percent7.2.0gauge Average resident percent across all indexes, located on this node                                                                                                        |
| index\_avg\_scan\_latency7.0.0gauge / Nanoseconds Average latency observed by the index scans, for this index                                                                                                    |
| index\_cache\_hits7.0.0counter The number of times the required index page for both scan and mutations is found in memory, for this index                                                                        |
| index\_cache\_misses7.0.0counter The number of times the required index page for both scan and mutations is NOT found in memory, for this index                                                                  |
| index\_codebook\_mem\_usage7.7counter / bytes Amount of memory used by codebook for this index, includes memory used for coarse codebook and quantization codebook                                               |
| index\_codebook\_train\_duration7.7counter / Nanoseconds Amount of time spent in training the codebook, for this index                                                                                           |
| index\_data\_size7.0.0gauge / bytes The approximate size of the valid uncompressed index data, for this index                                                                                                    |
| index\_data\_size\_on\_disk7.0.0gauge / bytes The size of the valid compressed index data, for this index                                                                                                        |
| index\_disk\_bytes7.6.4counter / bytes Number of bytes read from and written to disk, including insert, get, and delete operations                                                                               |
| index\_disk\_size7.0.0gauge / bytes Total disk space taken up by this index, after compression. This includes index data files, checkpoints etc.                                                                 |
| index\_frag\_percent7.0.0gauge Percentage of invalid index data, for this index                                                                                                                                  |
| index\_heap\_in\_use7.0.0gauge / bytes Total heap memory in use by indexer process in the node                                                                                                                   |
| index\_items\_count7.0.0gauge The actual number of items present in the latest index snapshot, for this index                                                                                                    |
| index\_log\_space\_on\_disk7.0.0gauge / bytes The size of the index data files - including garbage, for this index                                                                                               |
| index\_memory\_quota7.0.0gauge / bytes Configured memory quota for the index service nodes                                                                                                                       |
| index\_memory\_rss7.2.0gauge / bytes Resident set size of the indexer process, running on this node                                                                                                              |
| index\_memory\_total\_storage7.2.0gauge / bytes Amount of memory used by the index memory allocator, on this node                                                                                                |
| index\_memory\_used7.0.0gauge / bytes The memory used by this index                                                                                                                                              |
| index\_memory\_used\_storage7.2.0gauge / bytes Amount of memory used by underlying index storage, on this node                                                                                                   |
| index\_memory\_used\_total7.0.0gauge / bytes Total memory used by the indexer process                                                                                                                            |
| index\_net\_avg\_scan\_rate7.0.0gauge Average index scan rate across all indexes, for this node                                                                                                                  |
| index\_num\_diverging\_replica\_indexes8.0.0gauge Number of index partitions with diverging replica item counts.                                                                                                 |
| index\_num\_docs\_indexed7.0.0counter Number of document updates (of type insert, modify, delete) observed by this index                                                                                         |
| index\_num\_docs\_pending7.0.0gauge Number of pending updates that are yet to be received by index service, for this index                                                                                       |
| index\_num\_docs\_queued7.0.0gauge Number of updates queued (but not yet processed) by index service, for this index                                                                                             |
| index\_num\_indexes7.2.0gauge Total number of indexes, located on this node                                                                                                                                      |
| index\_num\_items\_flushed7.6.4counter Number of documents written from memory to index storage                                                                                                                  |
| index\_num\_requests7.0.0counter Number of scan requests received by the index service, for this index                                                                                                           |
| index\_num\_rows\_returned7.0.0counter Number of rows/index entries returned as the scan result during index scans, for this index                                                                               |
| index\_num\_rows\_scanned7.0.0counter Number of rows/index entries read during the index scans, for this index                                                                                                   |
| index\_num\_storage\_instances7.2.0gauge Total number of storage instances, located on this node                                                                                                                 |
| index\_partn\_is\_diverging\_replica8.0.0gauge Set to '1' if the index partition has diverging replica item counts                                                                                               |
| index\_partn\_items\_count7.6.6gauge The actual number of items present in the latest index snapshot, for this partition                                                                                         |
| index\_raw\_data\_size7.0.0gauge / bytes Encoded, uncompressed size of the index data, for this index                                                                                                            |
| index\_recs\_in\_mem7.0.0gauge Number of index entries cached in memory, for this index                                                                                                                          |
| index\_recs\_on\_disk7.0.0gauge Number of index entries stored on disk, which are not cached in memory, for this index                                                                                           |
| index\_resident\_percent7.0.0gauge Ratio of records in memory to total records, for this index                                                                                                                   |
| index\_scan\_bytes\_read7.0.0counter / bytes Number of bytes read from the index storage during index scans, for this index                                                                                      |
| index\_scan\_cache\_hits8.0counter Number of times the required index page for serving scan request is found in memory, for this index                                                                           |
| index\_scan\_cache\_misses8.0counter Number of times the required index page for serving scan request is NOT found in memory, for this index                                                                     |
| index\_state7.6.6gauge The current state of this index; CREATED: 0, READY: 1, INITIAL: 2, CATCHUP: 3, ACTIVE: 4, DELETED: 5, ERROR: 6, NIL: 7, SCHEDULED: 8, RECOVERED: 9\. Index is usable only in ACTIVE state |
| index\_storage\_avg\_item\_size7.6.0gauge / bytes Ratio of total item size and total records                                                                                                                     |
| index\_storage\_bytes\_incoming7.6.0gauge / bytes Aggregated total of bytes that are added to the stores and intended to be written on disc                                                                      |
| index\_storage\_bytes\_written7.6.0gauge / bytes Aggregated total of bytes written to the disc(data and recovery)                                                                                                |
| index\_storage\_cleaner\_blk\_read\_bs7.6.0gauge / bytes Total of number bytes read for cleaner log reads (both data and recovery)                                                                               |
| index\_storage\_cleaner\_num\_reads7.6.0gauge Total of number of cleaner log reads (both data and recovery)                                                                                                      |
| index\_storage\_compression\_ratio7.6.0gauge / bytes Ratio of cumulative number of page bytes compressed and cumulative number of page bytes after compression                                                   |
| index\_storage\_current\_quota7.6.0gauge / bytes Plasma's internally active memory quota for this node. It is tuned by memtuner.                                                                                 |
| index\_storage\_heap\_limit7.6.0gauge / bytes Plasma's global heap limit for managed memory for this node                                                                                                        |
| index\_storage\_hvi\_blk\_read\_bs8.0.0gauge Total number of bytes that were read from disk into memory                                                                                                          |
| index\_storage\_hvi\_blk\_reads\_bs\_get8.0.0gauge Total number of bytes that were read from disk into memory for index scans                                                                                    |
| index\_storage\_hvi\_blk\_reads\_bs\_lookup8.0.0gauge Total number of bytes that were read from disk into memory for lookups                                                                                     |
| index\_storage\_hvi\_buf\_memused8.0.0gauge Total Memory used by various reusable buffers                                                                                                                        |
| index\_storage\_hvi\_bytes\_incoming8.0.0gauge Total number of bytes that were added to the stores and intended to be written to disk                                                                            |
| index\_storage\_hvi\_bytes\_written8.0.0gauge Total number of bytes that were written to disk                                                                                                                    |
| index\_storage\_hvi\_compacts8.0.0gauge Total count of compaction operations performed                                                                                                                           |
| index\_storage\_hvi\_compression\_ratio\_avg8.0.0gauge Ratio of data bytes to be compressed and data bytes after compression                                                                                     |
| index\_storage\_hvi\_fragmentation8.0.0gauge The fraction of garbage data present on disk                                                                                                                        |
| index\_storage\_hvi\_memory\_used8.0.0gauge Total memory used by HVI indexes                                                                                                                                     |
| index\_storage\_hvi\_num\_reads8.0.0gauge Total number of times a disk block is read into memory                                                                                                                 |
| index\_storage\_hvi\_num\_reads\_get8.0.0gauge Total number of times a disk block was read into memory due to index scans                                                                                        |
| index\_storage\_hvi\_num\_reads\_lookup8.0.0gauge Total number of times a disk block was read into memory due to lookups                                                                                         |
| index\_storage\_hvi\_resident\_ratio8.0.0gauge Ratio of cache mem used and cacheable size                                                                                                                        |
| index\_storage\_hvi\_total\_disk\_size8.0.0gauge Total disk usage in bytes                                                                                                                                       |
| index\_storage\_hvi\_total\_used\_size8.0.0gauge Total number of disk bytes used. This size is eligible for cleanups in subsequent compactions.                                                                  |
| index\_storage\_items\_count7.6.0gauge Aggregated number of items that are currently in the stores                                                                                                               |
| index\_storage\_lookup\_blk\_reads\_bs7.6.0gauge / bytes Total number of bytes that were read from disc into memory for lookups                                                                                  |
| index\_storage\_lookup\_num\_reads7.6.0gauge Total number of LSS lookups for looking up items from stores                                                                                                        |
| index\_storage\_lss\_blk\_rdr\_reads\_bs7.6.0gauge / bytes Total number of bytes that were read from disc into memory from the logs(both data and recovery) for index scans                                      |
| index\_storage\_lss\_blk\_read\_bs7.6.0gauge / bytes Total number of bytes that were read from disc into memory from the logs(both data and recovery)                                                            |
| index\_storage\_lss\_fragmentation7.6.0gauge The fraction of garbage data present in the logs                                                                                                                    |
| index\_storage\_lss\_num\_reads7.6.0gauge Total number of times an LSS(both data and recovery) block is read from disk into memory                                                                               |
| index\_storage\_lss\_used\_space7.6.0gauge / bytes Total number of bytes used by data and recovery logs                                                                                                          |
| index\_storage\_memory\_stats\_size\_page7.6.0gauge / bytes Aggregated number of bytes of memory currently in use by Plasma for page records                                                                     |
| index\_storage\_num\_burst\_visits7.6.0gauge Aggregated total of pages visited during burst eviction                                                                                                             |
| index\_storage\_num\_evictable7.6.0gauge Aggregated total of the number of pages can be compressed                                                                                                               |
| index\_storage\_num\_evicted7.6.0gauge Aggregated total of the number of pages that were evicted and persisted to disc                                                                                           |
| index\_storage\_num\_pages7.6.0gauge Aggregated number of pages that are currently in use                                                                                                                        |
| index\_storage\_num\_periodic\_visits7.6.0gauge Aggregated total of pages visited during periodic eviction                                                                                                       |
| index\_storage\_purges7.6.0gauge Aggregated number of times various pages are compacted due to the MVCCPurger being triggered                                                                                    |
| index\_storage\_reclaim\_pending\_global7.6.0gauge / bytes Aggregated number of bytes across all plasma instances which have been freed but not yet returned to OS                                               |
| index\_storage\_resident\_ratio7.6.0gauge Ratio of cached records and total records                                                                                                                              |
| index\_storage\_rlss\_num\_reads7.6.0gauge Total number of times an LSS block was read into memory due to index scans                                                                                            |
| index\_total\_data\_size7.2.0gauge / bytes Sum of data size of all indexes, located on this node                                                                                                                 |
| index\_total\_disk\_size7.2.0gauge / bytes Sum of disk size of all indexes, located on this node                                                                                                                 |
| index\_total\_drain\_rate7.2.0gauge Sum of drain rate of all indexes, located on this node                                                                                                                       |
| index\_total\_mutation\_queue\_size7.0.0gauge Total number of index updates queued in the mutation queues, on this node                                                                                          |
| index\_total\_pending\_scans7.0.0gauge Sum of number of pending scans across all indexes, located on this node                                                                                                   |
| index\_total\_raw\_data\_size7.0.0gauge / bytes Sum of encoded, uncompressed size of the index data across all indexes, located on this node                                                                     |
| index\_total\_requests7.2.0counter Sum of number of requests received by all indexes, located on this node                                                                                                       |
| index\_total\_rows\_returned7.2.0counter Sum of number of rows returned during index scan across all indexes, located on this node                                                                               |
| index\_total\_rows\_scanned7.2.0counter Sum of number of rows scanned during index scans across all indexes, located on this node                                                                                |
| index\_total\_scan\_duration7.0.0counter / Nanoseconds Total time taken by the scans requests, for this index                                                                                                    |