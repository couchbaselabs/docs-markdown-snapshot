---
title: JSON Metrics
description: This content covers the statistics and metrics collected and made
  available by Sync Gateway
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/manage/pages/stats-monitoring-json.adoc
  xref: xref:3.3@sync-gateway:manage:stats-monitoring-json.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/manage/stats-monitoring-json.html)

# JSON Metrics

> This content covers the statistics and metrics collected and made available by Sync Gateway  
> Sync Gateway's statistics and metrics provide under-the-hood data on the performance, resource utilization and health of it nodes. This is increasingly important as deployments scale to support a large numbers of connected mobile and edge components.

Related _inter-syncgateway_ topics: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) | [Metrics REST API](../rest-api/rest-api-metrics.md) | [Prometheus Integration](../deploy/stats-prometheus.md)

## [](#json-format)JSON format

Use the `_expvar` endpoint to request these metrics:

Example 1\. Metrics in JSON format

```console
curl -X GET "http://localhost:4986/_expvar" -H "accept: application/json"
```

The response is a JSON object with a nested schema.

> [!NOTE]
> The statistics detailed in this schema are reset at each node restart — they are not persisted. All totals, counts, and averages are the values accrued since the last node restart unless otherwise specified.

> [!TIP]
> Use the click-through links to find out more about each item.

```json
"syncgateway": {
  "global": {
    "resource_utilization": {
      "admin_net_bytes_recv": 0,
      "admin_net_bytes_sent": 0,
      "error_count": 0,
      "go_memstats_heapalloc": 0,
      "go_memstats_heapidle": 0,
      "go_memstats_heapinuse": 0,
      "go_memstats_heapreleased": 0,
      "go_memstats_pausetotalns": 0,
      "go_memstats_stackinuse": 0,
      "go_memstats_stacksys": 0,
      "go_memstats_sys": 0,
      "goroutines_high_watermark": 0,
      "num_goroutines": 0,
      "process_memory_resident": 0,
      "pub_net_bytes_recv": 0,
      "pub_net_bytes_sent": 0,
      "system_memory_total": 0,
      "warn_count": 0,
      "process_cpu_percent_utilization": 0,
      "uptime": 0
    }
  },
  "per_db":  {
    [
      "$dbname": {
        "cache": {
          "abandoned_seqs":0,
          "chan_cache_active_revs": 0,
          "chan_cache_bypass_count": 0,
          "chan_cache_channels_added": 0,
          "chan_cache_channels_evicted_inactive": 0,
          "chan_cache_channels_evicted_nru": 0,
          "chan_cache_compact_count": 0,
          "chan_cache_compact_time": 0,
          "chan_cache_hits": 0,
          "chan_cache_max_entries": 0,
          "chan_cache_misses": 0,
          "chan_cache_num_channels": 0,
          "chan_cache_pending_queries":0,
          "chan_cache_removal_revs": 0,
          "chan_cache_tombstone_revs": 0,
          "high_seq_cached": 0,
          "high_seq_stable": 0,
          "num_active_channels": 0,
          "pending_seq_len": 0,
          "num_skipped_seqs": 0,
          "rev_cache_bypass": 0,
          "rev_cache_hits": 0,
          "rev_cache_misses": 0,
          "skipped_seq_len": 0,
          "view_queries": 0
        },
        "cbl_replication_pull": {
          "attachment_pull_bytes": 0,
          "attachment_pull_count": 0,
          "max_pending": 0,
          "num_pull_repl_active_continuous": 0,
          "num_pull_repl_active_one_shot": 0,
          "num_pull_repl_caught_up": 0,
          "num_pull_repl_since_zero": 0,
          "num_pull_repl_total_continuous": 0,
          "num_pull_repl_total_one_shot": 0,
          "request_changes_count": 0,
          "request_changes_time": 0,
          "rev_processing_time": 0,
          "rev_send_count": 0,
          "rev_send_latency": 0
        },
        "cbl_replication_push": {
          "attachment_push_bytes": 0,
          "attachment_push_count": 0,
          "conflict_write_count": 0,
          "doc_push_count": 0,
          "propose_change_count": 0,
          "propose_change_time": 0,
          "sync_function_count": 0,
          "sync_function_time": 0,
          "write_processing_time": 0
        },
        "database": {
          "compaction_attachment_start_time": 0,
          "compaction_tombstone_start_time": 0,
          "crc32c_match_count": 0,
          "dcp_caching_count": 0,
          "dcp_caching_time": 0,
          "dcp_received_count": 0,
          "dcp_received_time": 0,
          "doc_reads_bytes_blip": 0,
          "doc_writes_bytes": 0,
          "doc_writes_xattr_bytes":0,
          "high_seq_feed":0,
          "num_attachments_compacted": 0,
          "doc_writes_bytes_blip": 0,
          "num_doc_reads_blip": 0,
          "num_doc_reads_rest": 0,
          "num_doc_writes": 0,
          "num_replications_active": 0,
          "num_replications_total": 0,
          "sequence_assigned_count": 0,
          "sequence_get_count": 0,
          "sequence_incr_count":0,
          "sequence_released_count": 0,
          "sequence_reserved_count": 0,
          "warn_channel_name_size_count": 0,
          "warn_channels_per_doc_count": 0,
          "warn_grants_per_doc_count": 0,
          "warn_xattr_size_count": 0,
          "sync_function_count": 0,
          "sync_function_time": 0,
          "import_feed": 0
        },
        "delta_sync": {
          "delta_cache_hit": 0,
          "delta_cache_miss": 0,
          "delta_pull_replication_count": 0,
          "delta_push_docs_count": 0,
          "deltas_requested": 0,
          "deltas_sent": 0
        },
        "gsi_views": {
          "GSIs": 0,
            "{query name}_count": 0,
            "{query name}_error_count": 0,
            "{query name}_time": 0,
          "Views (Design doc or view)": 0,
            "{design doc name}.{view name}_count": 0,
            "{design doc name}.{view name}_error_count": 0,
            "{design doc name}.{view name}_time": 0,
        },
        "security": {
          "auth_failed_count": 0,
          "auth_success_count": 0,
          "num_access_errors": 0,
          "num_docs_rejected": 0,
          "total_auth_time": 0
        },
        "shared_bucket_import": {
          "import_cancel_cas": 0,
          "import_count": 0,
          "import_error_count": 0,
          "import_high_seq": 0,
          "import_partitions": 0,
          "import_processing_time": 0
        },
        "per_replication": {
          [
            "$replname": {
              "sgr_num_docs_pushed": 0,
              "sgr_num_docs_failed_to_push": 0,
              "sgr_docs_checked_sent": 0,
              "sgr_num_attachments_pushed": 0,
              "sgr_num_attachment_bytes_pushed": 0,
              "sgr_num_attachments_pulled": 0,
              "sgr_num_attachment_bytes_pulled": 0,
              "sgr_num_docs_pulled": 0,
              "sgr_num_docs_purged": 0,
              "sgr_num_docs_failed_to_pull": 0,
              "sgr_push_conflict_count": 0,
              "sgr_push_rejected_count": 0,
              "sgr_docs_checked_recv": 0,
              "sgr_deltas_recv": 0,
              "sgr_deltas_requested": 0,
              "sgr_deltas_sent": 0,
              "sgr_conflict_resolved_local_count": 0,
              "sgr_conflict_resolved_remote_count": 0,
              "sgr_conflict_resolved_merge_count": 0
              }
          ]
        }
    ]
  },
  "per_replication": {
    "$replname": {
      "sgr_active": true,
      "sgr_num_attachments_transferred": 0,
      "sgr_num_attachment_bytes_transferred": 0,
      "sgr_num_docs_pushed": 0,
      "sgr_num_docs_failed_to_push": 0,
      "sgr_docs_checked_sent": 0
    }
  }
}
```

## [](#global-stats)Global stats

### [](#syncgateway)syncgateway

Monitoring stats for Sync Gateway.

### [](#global)global

Global Sync Gateway stats.

### [](#resource%5Futilization)resource\_utilization

Resource utilization stats,

See: <https://golang.org/pkg/runtime/#MemStats> for more on memory allocator statistics.

#### [](#admin%5Fnet%5Fbytes%5Frecv)admin\_net\_bytes\_recv

Description

The total number of bytes received (since node start-up) on the network interface to which the Sync Gateway [api.admin\_interface](../configuration/configuration-schema-bootstrap.md#api-admin%5Finterface)is bound.

By default, that is the number of bytes received on `127.0.0.1:4985` since node start-up.

Use Case

This metric can be used to determine throughput on the admin interface:

`throughput` \= `admin_net_bytes_recv` / `admin_net_bytes_sent`

#### [](#admin%5Fnet%5Fbytes%5Fsent)admin\_net\_bytes\_sent

Description

The total number of bytes sent (since node start-up) on the network interface to which the Sync Gateway [api.admin\_interface](../configuration/configuration-schema-bootstrap.md#api-admin%5Finterface)is bound.

By default, that is the number of bytes sent on `127.0.0.1:4985` since node start-up.

Use Case

This metric can be useful in calculating the throughput on Sync Gateway's admin interface:

`throughput` \= `[admin_net_bytes_recv](#admin%5Fnet%5Fbytes%5Frecv)` / `[admin_net_bytes_sent](#admin%5Fnet%5Fbytes%5Fsent)`

#### [](#error%5Fcount)error\_count

The total number of errors logged.

#### [](#memory-allocator-statistics)memory allocator statistics

See: <https://golang.org/pkg/runtime/#MemStats> for more on memory allocator statistics.

##### [](#go%5Fmemstats%5Fheapalloc)go\_memstats\_heapalloc

Go memstats.HeapAlloc — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

##### [](#go%5Fmemstats%5Fheapidle)go\_memstats\_heapidle

Go memstats.HeapIdle — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

##### [](#go%5Fmemstats%5Fheapinuse)go\_memstats\_heapinuse

Go memstats.HeapInuse — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

##### [](#go%5Fmemstats%5Fheapreleased)go\_memstats\_heapreleased

Go memstats.HeapReleased — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

##### [](#go%5Fmemstats%5Fpausetotalns)go\_memstats\_pausetotalns

Go memstats.PauseTotalNs — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

##### [](#go%5Fmemstats%5Fstackinuse)go\_memstats\_stackinuse

Go memstats.StackInuse — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

##### [](#go%5Fmemstats%5Fstacksys)go\_memstats\_stacksys

Go memstats.StackSys — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

##### [](#go%5Fmemstats%5Fsys)go\_memstats\_sys

Go memstats.Sys — [Go memstats](https://golang.org/pkg/runtime/#MemStats)

#### [](#goroutines%5Fhigh%5Fwatermark)goroutines\_high\_watermark

Peak number of go routines since process start.

#### [](#num%5Fgoroutines)num\_goroutines

The total number of _goroutines_.

#### [](#process%5Fcpu%5Fpercent%5Futilization)process\_cpu\_percent\_utilization

Description

The CPU's utilization as percentage value.

Derivation

The CPU usage calculation is performed based on _user_ and _system_ CPU time, but it doesn't include components such as `iowait`.

Constraints

The derivation means that the values of `[process_cpu_percent_utilization](#process%5Fcpu%5Fpercent%5Futilization)` and `%Cpu`, returned when running the `top` command, will **differ**.

#### [](#process%5Fmemory%5Fresident)process\_memory\_resident

The memory utilization (_Resident Set Size_) for the process, in bytes.

#### [](#pub%5Fnet%5Fbytes%5Frecv)pub\_net\_bytes\_recv

Description

The total number of bytes received (since node start-up) on the network interface to which the Sync Gateway [api.public\_interface](../configuration/configuration-schema-bootstrap.md#api-public%5Finterface)is bound.

By default, that is the number of bytes received on `127.0.0.1:4984` since node start-up.

Use Case

The metric can be used to calculate throughput on the public interface:

`throughput` \= `[pub_net_bytes_recv](#pub%5Fnet%5Fbytes%5Frecv)` / `[pub_net_bytes_sent](#pub%5Fnet%5Fbytes%5Fsent)`

#### [](#pub%5Fnet%5Fbytes%5Fsent)pub\_net\_bytes\_sent

Description

The total number of bytes sent (since node start-up) on the network interface to which Sync Gateway [api.public\_interface](../configuration/configuration-schema-bootstrap.md#api-public%5Finterface)is bound.

By default, that is the number of bytes sent on `127.0.0.1:4984` since node start-up.

Use Case

This metric can be used to calculate throughput on the public interface:

`throughput` \= `[pub_net_bytes_recv](#pub%5Fnet%5Fbytes%5Frecv)` / `[pub_net_bytes_sent](#pub%5Fnet%5Fbytes%5Fsent)`

#### [](#system%5Fmemory%5Ftotal)system\_memory\_total

Description

The total memory available on the system in bytes.

#### [](#warn%5Fcount)warn\_count

Description

The total number of warnings logged.

#### [](#uptime)uptime

Description

The total uptime.

## [](#metrics-by-database)Metrics by Database

Quick Links

[cache](#cache) | [cbl\_replication\_pull](#cbl%5Freplication%5Fpull) | [cbl\_replication\_push](#cbl%5Freplication%5Fpush) | [database](#database) | [delta\_sync](#delta%5Fsync) | [gsi\_views](#gsi%5Fviews) | [security](#security) | [shared\_bucket\_import](#shared%5Fbucket%5Fimport) 

### [](#per%5Fdb)per\_db

The metrics for each [database](#database) declared in the config file.

### [](#dbname)$dbname

The metrics relating to a [database](#database) declared in the config file.

### [](#cache)cache

These metrics relate to caching.

#### [](#abandoned%5Fseqs)abandoned\_seqs

Description

The total number of skipped sequences that were not found after 60 minutes and were abandoned.

#### [](#chan%5Fcache%5Factive%5Frevs)chan\_cache\_active\_revs

Description

The total number of active revisions in the channel cache.

#### [](#chan%5Fcache%5Fbypass%5Fcount)chan\_cache\_bypass\_count

Description

The total number of transient bypass channel caches created to serve requests when the channel cache was at capacity.

#### [](#chan%5Fcache%5Fchannels%5Fadded)chan\_cache\_channels\_added

Description

The total number of channel caches added.

Constraints

The metric doesn't decrease when a channel is removed. That is, it is similar to [chan\_cache\_num\_channels](#chan%5Fcache%5Fnum%5Fchannels) but doesn't track removals.

#### [](#chan%5Fcache%5Fchannels%5Fevicted%5Finactive)chan\_cache\_channels\_evicted\_inactive

Description

The total number of channel cache channels evicted due to inactivity.

#### [](#chan%5Fcache%5Fchannels%5Fevicted%5Fnru)chan\_cache\_channels\_evicted\_nru

Description

The total number of active channel cache channels evicted, based on 'not recently used' criteria.

#### [](#chan%5Fcache%5Fcompact%5Fcount)chan\_cache\_compact\_count

Description

The total number of channel cache compaction runs.

#### [](#chan%5Fcache%5Fcompact%5Ftime)chan\_cache\_compact\_time

Description

The total amount of time taken by channel cache compaction across all compaction runs.

#### [](#chan%5Fcache%5Fhits)chan\_cache\_hits

Description

The total number of channel cache requests fully served by the cache.

Use Case

This metric is useful in calculating the channel cache hit ratio:

`channel cache hit ratio` \= `[chan_cache_hits](#chan%5Fcache%5Fhits)` / (`[chan_cache_hits](#chan%5Fcache%5Fhits)` \+ `[chan_cache_misses](#chan%5Fcache%5Fmisses)`)

#### [](#chan%5Fcache%5Fmax%5Fentries)chan\_cache\_max\_entries

Description

The total size of the largest channel cache.

Use Case

This metric helps with channel cache tuning, and provides a hint on cache size variation (when compared to average cache size).

#### [](#chan%5Fcache%5Fmisses)chan\_cache\_misses

Description

The total number of channel cache requests not fully served by the cache.

Use Case

This metric is useful when calculating the channel cache hit ratio:

`channel cache hit ratio` \= `[chan_cache_hits](#chan%5Fcache%5Fhits)` / (`[chan_cache_hits](#chan%5Fcache%5Fhits)` \+ `[chan_cache_misses](#chan%5Fcache%5Fmisses)`)

#### [](#chan%5Fcache%5Fnum%5Fchannels-2)chan\_cache\_num\_channels

Description

The total number of channels being cached.

Use Case

The total number of channels being cached provides insight into potential max cache size requirements and also node usage (for example, `[chan_cache_num_channels](#chan%5Fcache%5Fnum%5Fchannels)` \* `max_cache_size`).

#### [](#chan%5Fcache%5Fpending%5Fqueries)chan\_cache\_pending\_queries

Description

The total number of channel cache pending queries.

#### [](#chan%5Fcache%5Fremoval%5Frevs)chan\_cache\_removal\_revs

Description

The total number of removal revisions in the channel cache.

Use Case

This metric acts as a reminder that removals must be considered when tuning the channel cache size and also helps users understand whether they should be tuning tombstone retention policy (metadata purge interval) and running compact.

#### [](#chan%5Fcache%5Ftombstone%5Frevs)chan\_cache\_tombstone\_revs

Description

The total number of tombstone revisions in the channel cache.

Use Case

This metric acts as a reminder that tombstones and removals must be considered when tuning the channel cache size and also helps users understand whether they should be tuning tombstone retention policy (metadata purge interval), and running compact.

#### [](#high%5Fseq%5Fcached)high\_seq\_cached

Description

The highest sequence number cached.

Constraints

There may be skipped sequences lower than high\_seq\_cached.

#### [](#high%5Fseq%5Fstable)high\_seq\_stable

Description

The highest contiguous sequence number that has been cached.

#### [](#num%5Factive%5Fchannels)num\_active\_channels

Description

The total number of active channels.

#### [](#num%5Fskipped%5Fseqs)num\_skipped\_seqs

Description

The total number of skipped sequences.

Use Case

This metric helps with channel cache tuning, and provides a hint on cache size variation (when compared to average cache size).

#### [](#pending%5Fseq%5Flen)pending\_seq\_len

Description

The total number of pending sequences. These are out-of-sequence entries waiting to be cached.

#### [](#rev%5Fcache%5Fbypass)rev\_cache\_bypass

Description

The total number of revision cache bypass operations performed.

#### [](#rev%5Fcache%5Fhits)rev\_cache\_hits

Description

The total number of revision cache hits.

Use Case

This metric can be used to calculate the ratio of revision cache hits:

`Rev Cache Hit Ratio` \= `[rev_cache_hits](#rev%5Fcache%5Fhits)` / (`[rev_cache_hits](#rev%5Fcache%5Fhits)` \+ `[rev_cache_misses](#rev%5Fcache%5Fmisses)`)

#### [](#rev%5Fcache%5Fmisses)rev\_cache\_misses

Description

The total number of revision cache misses.

Use Case

This metric can be used to calculate the ratio of revision cache misses:

`Rev Cache Miss Ratio` \= `[rev_cache_misses](#rev%5Fcache%5Fmisses)` / (`[rev_cache_hits](#rev%5Fcache%5Fhits)` \+ `[rev_cache_misses](#rev%5Fcache%5Fmisses)`)

#### [](#skipped%5Fseq%5Flen)skipped\_seq\_len

Description

The current length of the pending skipped sequence queue.

#### [](#view%5Fqueries)view\_queries

Description

The total view\_queries.

### [](#cbl%5Freplication%5Fpull)cbl\_replication\_pull

#### [](#attachment%5Fpull%5Fbytes)attachment\_pull\_bytes

Description

The total size of attachments pulled. This is the **pre-compressed** size.

#### [](#attachment%5Fpull%5Fcount)attachment\_pull\_count

Description

The total number of attachments pulled.

#### [](#max%5Fpending)max\_pending

Description

The high watermark for the number of documents buffered during feed processing, waiting on a missing earlier sequence.

#### [](#num%5Fpull%5Frepl%5Factive%5Fcontinuous)num\_pull\_repl\_active\_continuous

Description

The total number of continuous pull replications in the active state.

#### [](#num%5Fpull%5Frepl%5Factive%5Fone%5Fshot)num\_pull\_repl\_active\_one\_shot

Description

The total number of one-shot pull replications in the active state.

#### [](#num%5Fpull%5Frepl%5Fcaught%5Fup)num\_pull\_repl\_caught\_up

Description

The total number of replications which have caught up to the latest changes.

#### [](#num%5Fpull%5Frepl%5Fsince%5Fzero)num\_pull\_repl\_since\_zero

Description

The total number of new replications started (`/_changes?since`\=0).

#### [](#num%5Fpull%5Frepl%5Ftotal%5Fcontinuous)num\_pull\_repl\_total\_continuous

Description

The total number of continuous pull replications.

#### [](#num%5Fpull%5Frepl%5Ftotal%5Fone%5Fshot)num\_pull\_repl\_total\_one\_shot

Description

The total number of one-shot pull replications.

#### [](#request%5Fchanges%5Fcount)request\_changes\_count

Description

The total number of changes requested.

Use Case

This metric can be used to calculate the latency of requested changes:

`changes request latency` \= `[request_changes_time](#request%5Fchanges%5Ftime)` / `[request_changes_count](#request%5Fchanges%5Fcount)`

#### [](#request%5Fchanges%5Ftime)request\_changes\_time

Description

Use Case

This metric can be used to calculate the latency of requested changes:

`changes request latency` \= `[request_changes_time](#request%5Fchanges%5Ftime)` / `[request_changes_count](#request%5Fchanges%5Fcount)`

#### [](#rev%5Fprocessing%5Ftime)rev\_processing\_time

Description

The total amount of time processing rev messages (revisions) during pull revision.

Use Case

This metric can be used with [rev\_send\_count](#rev%5Fsend%5Fcount) to calculate the average processing time per revision:

`average processing time per revision` \= `[rev_processing_time](#rev%5Fprocessing%5Ftime)` / `[rev_send_count](#rev%5Fsend%5Fcount)`

#### [](#rev%5Fsend%5Fcount)rev\_send\_count

Description

The total number of rev messages processed during replication.

Use Case

This metric can be used with [rev\_processing\_time](#rev%5Fprocessing%5Ftime) to calculate the average processing time per revision:

_average processing time per revision_ \= `[rev_processing_time](#rev%5Fprocessing%5Ftime)` / `[rev_send_count](#rev%5Fsend%5Fcount)`.

#### [](#rev%5Fsend%5Flatency)rev\_send\_latency

Description

The total amount of time between Sync Gateway receiving a request for a revision and that revision being sent.

In a pull replication, Sync Gateway sends a `/_changes` request to the client and the client responds with the list of revisions it wants to receive.

So, `[rev_send_latency](#rev%5Fsend%5Flatency)` measures the time between the client asking for those revisions and Sync Gateway sending them to the client.

Use Case

This metric gives the time taken to respond to a `/ changes` request.

Constraints

The derived value includes latency associated with processing other revisions in the same batch.

Measuring time from the `/_changes` response means that this stat will vary significantly depending on the changes batch size A larger batch size will result in a spike of this stat, even if the processing time per revision is unchanged.

A more useful stat might be the average processing time per revision:

`average processing time per revision` \= `[rev_processing_time](#rev%5Fprocessing%5Ftime)`\] / `[rev_send_count](#rev%5Fsend%5Fcount)`

### [](#cbl%5Freplication%5Fpush)cbl\_replication\_push

#### [](#attachment%5Fpush%5Fbytes)attachment\_push\_bytes

Description

The total number of attachment bytes pushed.

#### [](#compaction%5Fattachment%5Fstart%5Ftime)compaction\_attachment\_start\_time

Description

The compaction\_attachment\_start\_time.

#### [](#compaction%5Ftombstone%5Fstart%5Ftime)compaction\_tombstone\_start\_time

Description

The compaction\_tombstone\_start\_time.

#### [](#attachment%5Fpush%5Fcount)attachment\_push\_count

Description

The total number of attachments pushed.

#### [](#conflict%5Fwrite%5Fcount)conflict\_write\_count

Description

The total number of writes that left the document in a conflicted state. Includes new conflicts, and mutations that don't resolve existing conflicts.

#### [](#doc%5Fpush%5Fcount)doc\_push\_count

Description

The total number of documents pushed.

#### [](#propose%5Fchange%5Fcount)propose\_change\_count

Description

The total number of changes and-or proposeChanges messages processed since node start-up.

Use Case

The [propose\_change\_count](#propose%5Fchange%5Fcount) stat can be useful when:

* Assessing the number of redundant requested changes being pushed by the client.  
Do this by comparing the [propose\_change\_count](#propose%5Fchange%5Fcount) value with the number of actual writes [num\_doc\_writes](#num%5Fdoc%5Fwrites), which could indicate that clients are pushing changes already known to Sync Gateway.
* Identifying situations where push replications are unexpectedly being restarted from zero.  
> [!NOTE]  
> P2P synchronizations will typically show a higher incidences of rejected proposed changes.

#### [](#propose%5Fchange%5Ftime)propose\_change\_time

Description

The total time spent processing changes and/or proposeChanges messages.

Use Case

The [propose\_change\_time](#propose%5Fchange%5Ftime) stat can be useful in diagnosing push replication issues arising from potential bottlenecks changes and-or proposeChanges processing.

Contraints

The [propose\_change\_time](#propose%5Fchange%5Ftime) is not included in the [write\_processing\_time](#write%5Fprocessing%5Ftime).

#### [](#sync%5Ffunction%5Fcount)sync\_function\_count

Description

The total number of times that the sync\_function is evaluated.

Use Case

The {sync\_function\_count\_ stat is useful in assessing the usage of the sync\_function, when used in conjunction with the [sync\_function\_time](#sync%5Ffunction%5Ftime).

#### [](#sync%5Ffunction%5Ftime)sync\_function\_time

Description

The total time spent evaluating the sync\_function.

Use Case

The [sync\_function\_time](#sync%5Ffunction%5Ftime) stat can be useful when:

* Troubleshooting excessively long push times, where it can help identify potential sync\_function bottlenecks (for example, those arising from complex, or inefficient, sync\_function design
* Assessing the overall contribution of the sync\_function processing to overall push replication write times.

#### [](#write%5Fprocessing%5Ftime)write\_processing\_time

Description

Total time spent processing writes. Measures complete request-to-response time for a write.

Use Case

The [write\_processing\_time](#write%5Fprocessing%5Ftime) stat can be useful when:

* Determining the average time per write:  
`average time per write` \= [write\_processing\_time](#write%5Fprocessing%5Ftime) / [num\_doc\_writes](#num%5Fdoc%5Fwrites)stat value
* Assessing the benefit of adding additional Sync Gateway nodes, as it can point to Sync Gateway being a bottleneck
* Troubleshooting slow push replication, in which case it ought to be considered in conjunction with [sync\_function\_time](#sync%5Ffunction%5Ftime).

### [](#database)database

Stats relative to the database

#### [](#abandoned%5Fseqs-2)abandoned\_seqs

Description

The total number of skipped sequences abandoned, based on `cache.channel_cache.max_wait_skipped`.

#### [](#cache%5Ffeed)cache\_feed

Description

Contains low level dcp stats:

* `dcp_backfill_expected` \- the expected number of sequences in backfill
* `dcp_backfill_completed` \- the number of backfill items processed
* `dcp_rollback_count` \- the number of DCP rollbacks.

#### [](#crc32c%5Fmatch%5Fcount)crc32c\_match\_count

Description

The total number of instances during import when the document cas had changed, but the document was not imported because the document body had not changed.

#### [](#dcp%5Fcaching%5Fcount)dcp\_caching\_count

Description

The total number of DCP mutations added to Sync Gateway's channel cache.

Use Case

Can be used with `[dcp_caching_time](#dcp%5Fcaching%5Ftime)` to monitor cache processing latency. That is, the time between seeing a change on the DCP feed and when it's available in the channel cache:

`DCP cache latency` \= `[dcp_caching_time](#dcp%5Fcaching%5Ftime)` / `[dcp_caching_count](#dcp%5Fcaching%5Fcount)`

#### [](#dcp%5Fcaching%5Ftime)dcp\_caching\_time

Description

The total time between a DCP mutation arriving at Sync Gateway and being added to channel cache.

Use Case

This metric can be used with `[dcp_caching_count](#dcp%5Fcaching%5Fcount)` to monitor cache processing latency. That is, the time between seeing a change on the DCP feed and when it's available in the channel cache:

`dcp_cache_latency` \= `[dcp_caching_time](#dcp%5Fcaching%5Ftime)` / `[dcp_caching_count](#dcp%5Fcaching%5Fcount)`

#### [](#dcp%5Freceived%5Fcount)dcp\_received\_count

Description

The total number of document mutations received by Sync Gateway over DCP.

#### [](#dcp%5Freceived%5Ftime)dcp\_received\_time

Description

The time between a document write and that document being received by Sync Gateway over DCP. If the document was written prior to Sync Gateway starting the feed, it is recorded as the time since the feed was started.

Use Case

This metric can be used to monitor DCP feed processing latency.

#### [](#doc%5Freads%5Fbytes%5Fblip)doc\_reads\_bytes\_blip

Description

The total number of bytes read via Couchbase Lite 2.x replication since Sync Gateway node startup.

#### [](#doc%5Fwrites%5Fbytes)doc\_writes\_bytes

Description

The total number of bytes written as part of document writes since Sync Gateway node startup.

#### [](#doc%5Fwrites%5Fbytes%5Fblip)doc\_writes\_bytes\_blip

Description

The total number of bytes written as part of Couchbase Lite document writes since Sync Gateway node startup.

#### [](#doc%5Fwrites%5Fxattr%5Fbytes)doc\_writes\_xattr\_bytes

Description

The total size of xattrs written (in bytes).

#### [](#high%5Fseq%5Ffeed)high\_seq\_feed

Description

Highest sequence number seen on the caching DCP feed.

#### [](#num%5Fattachments%5Fcompacted)num\_attachments\_compacted

Description

The number of attachments compacted

#### [](#import%5Ffeed)import\_feed

Description

This metric contains low level dcp stats:

* `dcp_backfill_expected` \- the total expected number of sequences in backfill
* `dcp_backfill_completed` \- the total number of backfill items processed
* `dcp_rollback_count` \- the total number of rollbacks that occur.

#### [](#num%5Fdoc%5Freads%5Fblip)num\_doc\_reads\_blip

Description

The total number of documents read via Couchbase Lite 2.x replication since Sync Gateway node startup.

#### [](#num%5Fdoc%5Freads%5Frest)num\_doc\_reads\_rest

Description

The total number of documents read via the REST API since Sync Gateway node startup. Includes Couchbase Lite 1.x replication.

#### [](#num%5Fdoc%5Fwrites)num\_doc\_writes

Description

The total number of documents written by any means (replication, rest API interaction or imports) since Sync Gateway node startup.

#### [](#num%5Freplications%5Factive)num\_replications\_active

Description

The total number of active replications.

Constraints

This metric only counts continuous pull replications.

#### [](#num%5Freplications%5Ftotal)num\_replications\_total

Description

The total number of replications created since Sync Gateway node startup.

#### [](#sequence%5Fassigned%5Fcount)sequence\_assigned\_count

Description

The total number of sequence numbers assigned.

#### [](#sequence%5Fget%5Fcount)sequence\_get\_count

Description

The total number of high sequence lookups.

#### [](#sequence%5Fincr%5Fcount)sequence\_incr\_count

Description

The total number of times the sequence counter document has been incremented.

#### [](#sequence%5Freleased%5Fcount)sequence\_released\_count

Description

The total number of unused, reserved sequences released by Sync Gateway.

#### [](#sequence%5Freserved%5Fcount)sequence\_reserved\_count

Description

The total number of sequences reserved by Sync Gateway.

#### [](#warn%5Fchannel%5Fname%5Fsize%5Fcount)warn\_channel\_name\_size\_count

Description

The total number of warnings relating to the channel name size.

#### [](#warn%5Fchannels%5Fper%5Fdoc%5Fcount)warn\_channels\_per\_doc\_count

Description

The total number of warnings relating to the channel count exceeding the channel count threshold.

Corresponding warning message

```console
Doc id: {document id} channel count: {channel count} exceeds {channel count} for channels per doc warning threshold
```

#### [](#warn%5Fgrants%5Fper%5Fdoc%5Fcount)warn\_grants\_per\_doc\_count

Description

The total number of warnings relating to the grant count exceeding the grant count threshold.

Corresponding warning message

```console
Doc id: {document id} access and role grants count: {grant count} exceeds {grant count} for grants per doc warning threshold
```

#### [](#warn%5Fxattr%5Fsize%5Fcount)warn\_xattr\_size\_count

Description

The total number of warnings relating to the xattr sync data being larger than a configured threshold.

Corresponding warning message

```console
Doc id: {document id} sync metadata size: {xattr bytes} bytes exceeds {xattr bytes} bytes for sync metadata warning threshold
```

### [](#delta%5Fsync)delta\_sync

#### [](#delta%5Fcache%5Fhit)delta\_cache\_hit

Description

The total number of requested deltas that were available in the revision cache.

#### [](#delta%5Fcache%5Fmiss)delta\_cache\_miss

Description

The total number of requested deltas that were not available in the revision cache.

#### [](#delta%5Fpull%5Freplication%5Fcount)delta\_pull\_replication\_count

Description

The number of delta replications that have been run.

#### [](#delta%5Fpush%5Fdoc%5Fcount)delta\_push\_doc\_count

Description

The total number of documents pushed as a delta from a previous revision.

#### [](#deltas%5Frequested)deltas\_requested

Description

The total number of times a revision is sent as delta from a previous revision.

#### [](#deltas%5Fsent)deltas\_sent

Description

The total number of revisions sent to clients as deltas.

### [](#gsi%5Fviews)gsi\_views

#### [](#gsis)GSIs

The GSI metrics are defined in this section, where {query name} is a placeholder representing a Valid Query Name from this list:

Valid Query Names

* access
* roleAccess
* channels
* channelsStar
* sequences
* principals
* sessions
* tombstones
* resync
* allDocs

#### [](#query-name%5Fcount){query name}\_count

Description

The total number of queries performed.

##### [](#query-name%5Ferror%5Fcount){query name}\_error\_count

Description

The total number of errors that occurred when performing the query.

##### [](#query-name%5Ftime){query name}\_time

Description

The total time taken to perform queries.

#### [](#views)Views

The View metrics are defined in this section, where {design doc name} and {view name} are placeholders representing a Valid Design Doc Name and a Valid View Name, as defined in these lists:

Valid Design Doc Names

* sync\_gateway
* sync\_housekeeping

Valid View Names

* principals
* channels
* access
* access\_vbseq
* role\_access
* role\_access\_vbseq
* all\_docs
* import
* sessions
* tombstones

##### [](#design-doc-name-view-name%5Fcount){design doc name}.{view name}\_count

Description

The total number of view queries performed.

##### [](#design-doc-name-view-name%5Ferror%5Fcount){design doc name}.{view name}\_error\_count

Description

The total number of errors that occurred when performing the query.

##### [](#design-doc-name-view-name%5Ftime){design doc name}.{view name}\_time

Description

The total time taken to perform the view query.

### [](#security)Security

These metrics relate to security.

#### [](#auth%5Ffailed%5Fcount)auth\_failed\_count

Description

The total number of unsuccessful authentications.

Use Case

This metric is useful in monitoring the number of authentication errors.

#### [](#auth%5Fsuccess%5Fcount)auth\_success\_count

Description

The total number of successful authentications.

Use Case

This metric is useful in monitoring the number of authenticated requests.

#### [](#num%5Faccess%5Ferrors)num\_access\_errors

Description

The total number of documents rejected by write access functions (requireAccess, requireRole, requireUser).

#### [](#num%5Fdocs%5Frejected)num\_docs\_rejected

Description

The total number of documents rejected by the sync\_function.

Use Case

This metric is useful in debugging sync\_function issues and identify unexpected incoming documents.

#### [](#total%5Fauth%5Ftime)total\_auth\_time

Description

The total time spent in authenticating all requests.

Use Cases

This metric can be compared with `[auth_success_count](#auth%5Fsuccess%5Fcount)` and `[auth_failed_count](#auth%5Ffailed%5Fcount)` to derive an average success and-or fail rate.

### [](#shared%5Fbucket%5Fimport)shared\_bucket\_import

#### [](#import%5Fcancel%5Fcas)import\_cancel\_cas

Description

The total number of imports cancelled due to cas failure.

#### [](#import%5Fcount)import\_count

Description

The total number of docs imported.

#### [](#import%5Ferror%5Fcount)import\_error\_count

Description

The total number of errors arising as a result of a document import.

Corresponding Error Message

```console
Error importing doc {document id}: {error}
```

#### [](#import%5Fhigh%5Fseq)import\_high\_seq

Description

The highest sequence number value imported.

#### [](#import%5Fpartitions)import\_partitions

Description

The total number of import partitions.

#### [](#import%5Fprocessing%5Ftime)import\_processing\_time

Description

The total time taken to process a document import.

### [](#metrics-by-replication)Metrics by replication

The metrics collated and reported here relate **only** to replications run using the inter-Sync Gateway replication.

> [!NOTE]
> These metrics refer to Sync Gateway replications only; Couchbase Lite replications are not included.

#### [](#per%5Freplication)Per\_replication

(Inter-Sync Gateway)

This [per\_replication](#per%5Freplication) group header encompasses all the stats for each inter-Sync Gateway replication involving its owning database.

It comprises an array of one or more [$replname](#replname) objects, each of which represents the statistics collected and recorded against the specified $replname (`replication_id`).

#### [](#replname)$replname

This object comprises the stats collected and recorded for the inter-Sync Gateway replication named $replname (which equates to a `replication_id`). The same structure is used to return statistics from Inter-Sync Gateway and SG Replicate replications, but not all items are populated by each version.

##### [](#sgr%5Fdocs%5Fchecked%5Fsent)sgr\_docs\_checked\_sent

Description

The total number of documents checked for changes since replication started. This represents the number of potential change notifications pushed by Sync Gateway.

Constraints

* This is not necessarily the number of documents pushed, as a given target might already have the change.
* Used by Inter-Sync Gateway and SG Replicate

Values

* Continuous replication:  
The value is true for the duration of the replication, and also once it has caught up (i.e is in the idle state). The value is false if the replication is explicitly cancelled.
* One-shot replication  
The value is true for the duration of the replication, and then false when it has completed or if it is cancelled.

Use Case

This metric can be useful when analyzing replication history, and to filter by active replications.

##### [](#sgr%5Fnum%5Fdocs%5Ffailed%5Fto%5Fpush)sgr\_num\_docs\_failed\_to\_push

Description

The total number of documents that failed to be pushed since replication started.

Used by Inter-Sync Gateway and SG Replicate

##### [](#sgr%5Fnum%5Fdocs%5Fpushed)sgr\_num\_docs\_pushed

Description

The total number of documents that were pushed since replication started.

Used by Inter-Sync Gateway and SG Replicate

##### [](#sgr%5Fnum%5Fattachments%5Fpushed)sgr\_num\_attachments\_pushed

Description

The total number of attachments that were pushed since replication started.

##### [](#sgr%5Fnum%5Fattachment%5Fbytes%5Fpushed)sgr\_num\_attachment\_bytes\_pushed

Description

The total number of bytes in all the attachments that were pushed since replication started.

##### [](#sgr%5Fnum%5Fattachments%5Fpulled)sgr\_num\_attachments\_pulled

Description

The total number of attachments that were pulled since replication started.

##### [](#sgr%5Fnum%5Fattachment%5Fbytes%5Fpulled)sgr\_num\_attachment\_bytes\_pulled

Description

The total number of bytes in all the attachments that were pulled since replication started.

##### [](#sgr%5Fnum%5Fdocs%5Fpulled)sgr\_num\_docs\_pulled

Description

The total number of documents that were pulled since replication started.

##### [](#sgr%5Fnum%5Fdocs%5Fpurged)sgr\_num\_docs\_purged

Description

The total number of documents that were purged since replication started.

##### [](#sgr%5Fnum%5Fdocs%5Ffailed%5Fto%5Fpull)sgr\_num\_docs\_failed\_to\_pull

Description

The total number of document pulls that failed since replication started.

##### [](#sgr%5Fpush%5Fconflict%5Fcount)sgr\_push\_conflict\_count

Description

The total number of pushed documents that conflicted since replication started.

##### [](#sgr%5Fpush%5Frejected%5Fcount)sgr\_push\_rejected\_count

Description

The total number of pushed documents that were rejected since replication started.

##### [](#sgr%5Fdocs%5Fchecked%5Frecv)sgr\_docs\_checked\_recv

Description

The total number of documents that were purged since replication started.

##### [](#sgr%5Fdeltas%5Frecv)sgr\_deltas\_recv

Description

The total number of documents that were purged since replication started.

##### [](#sgr%5Fdeltas%5Frequested)sgr\_deltas\_requested

Description

The total number of deltas requested

##### [](#sgr%5Fdeltas%5Fsent)sgr\_deltas\_sent

Description

The total number of deltas sent

##### [](#sgr%5Fconflict%5Fresolved%5Flocal%5Fcount)sgr\_conflict\_resolved\_local\_count

Description

The total number of conflicting documents that were resolved successfully locally (by the active replicator)

##### [](#sgr%5Fconflict%5Fresolved%5Fremote%5Fcount)sgr\_conflict\_resolved\_remote\_count

Description

The total number of conflicting documents that were resolved successfully remotely (by the active replicator)

##### [](#sgr%5Fconflict%5Fresolved%5Fmerge%5Fcount)sgr\_conflict\_resolved\_merge\_count

Description

The total number of conflicting documents that were resolved successfully by a merge action (by the active replicator)

##### [](#sgw%5Fconflict%5Fskipped%5Ferror)sgw\_conflict\_skipped\_error

Description

The total number of documents that were skipped during sync because of an error in conflict resolution

## [](#metrics-by-replication-deprecated)Metrics by replication ( **\*deprecated** )

This structure and its associated metrics is deprecated at version 2.8\. The metrics collated and reported here relate **only** to replications run using the SG Replicate. For metrics relating to replications run using inter-Sync Gateway replication see: [Per\_replication](#per%5Freplication).

### [](#per%5Freplication-sg-replicate)Per\_replication (SG Replicate)

This [per\_replication](#per%5Freplication) group header encompasses all the stats for each inter-Sync Gateway replication involving its owning database.

It comprises an array of one or more [$replname](#replname) objects, each of which represents the statistics collected and recorded against the specified $replname (`replication_id`).

> [!NOTE]
> These metrics refer to Sync Gateway replications only; Couchbase Lite replications are not included.

### [](#replname-2)$replname

This object comprises the stats collected and recorded for the inter-Sync Gateway replication named $replname (which equates to a `replication_id`). The same structure is used to return statistics from Inter-Sync Gateway and SG Replicate replications, although not all items are populated by each version.

#### [](#sgr%5Factive)sgr\_active

Description

Whether the replication is active at this time. **Deprecated @ 2.8**: used only by SG Replicate.

#### [](#sgr%5Fdocs%5Fchecked%5Fsent-sgr1)sgr\_docs\_checked\_sent (sgr1)

See: [sgr\_docs\_checked\_sent](#sgr%5Fdocs%5Fchecked%5Fsent)

### [](#sgr%5Fnum%5Fattachments%5Ftransferred)sgr\_num\_attachments\_transferred

Description

The total number of attachments transferred since replication started. **Deprecated @ 2.8**: used only by SG Replicate.

### [](#sgr%5Fnum%5Fattachment%5Fbytes%5Ftransferred)sgr\_num\_attachment\_bytes\_transferred

Description

The total number of attachment bytes transferred since replication started. **Deprecated @ 2.8**: used only by SG Replicate.

### [](#sgr%5Fnum%5Fdocs%5Ffailed%5Fto%5Fpush-sgr1)sgr\_num\_docs\_failed\_to\_push (sgr1)

See: [sgr\_num\_docs\_failed\_to\_push](#sgr%5Fnum%5Fdocs%5Ffailed%5Fto%5Fpush)

### [](#sgr%5Fnum%5Fdocs%5Fpushed-sgr1)sgr\_num\_docs\_pushed (sgr1)

See: [sgr\_num\_docs\_pushed](#sgr%5Fnum%5Fdocs%5Fpushed)

## [](#alphabetic-index)Alphabetic Index

Quick Links

[$](#symbol) **|** [A - C](#a-c) **|** [D - G](#d-g) **|** [H - N](#h-n) **|** [P - Z](#p-z) 

### [](#symbol)$

* [$dbname](#dbname)
* [$replname](#replname)

### [](#a-c)A - C

* [abandoned\_seqs](#abandoned%5Fseqs)
* [abandoned\_seqs](#abandoned%5Fseqs)
* [admin\_net\_bytes\_recv](#admin%5Fnet%5Fbytes%5Frecv)
* [admin\_net\_bytes\_sent](#admin%5Fnet%5Fbytes%5Fsent)
* [attachment\_pull\_bytes](#attachment%5Fpull%5Fbytes)
* [attachment\_pull\_count](#attachment%5Fpull%5Fcount)
* [attachment\_push\_bytes](#attachment%5Fpush%5Fbytes)
* [attachment\_push\_count](#attachment%5Fpush%5Fcount)
* [auth\_failed\_count](#auth%5Ffailed%5Fcount)
* [auth\_success\_count](#auth%5Fsuccess%5Fcount)
* [chan\_cache\_compact\_count](#chan%5Fcache%5Fcompact%5Fcount)
* [cache\_feed](#cache%5Ffeed)
* [cache](#cache)
* [cbl\_replication\_pull](#cbl%5Freplication%5Fpull)
* [cbl\_replication\_push](#cbl%5Freplication%5Fpush)
* [chan\_cache\_active\_revs](#chan%5Fcache%5Factive%5Frevs)
* [chan\_cache\_bypass\_count](#chan%5Fcache%5Fbypass%5Fcount)
* [chan\_cache\_channels\_added](#chan%5Fcache%5Fchannels%5Fadded)
* [chan\_cache\_channels\_evicted\_inactive](#chan%5Fcache%5Fchannels%5Fevicted%5Finactive)
* [chan\_cache\_channels\_evicted\_nru](#chan%5Fcache%5Fchannels%5Fevicted%5Fnru)
* [chan\_cache\_hits](#chan%5Fcache%5Fhits)
* [chan\_cache\_max\_entries](#chan%5Fcache%5Fmax%5Fentries)
* [chan\_cache\_misses](#chan%5Fcache%5Fmisses)
* [chan\_cache\_num\_channels](#chan%5Fcache%5Fnum%5Fchannels)
* [chan\_cache\_pending\_queries](#chan%5Fcache%5Fpending%5Fqueries)
* [chan\_cache\_removal\_revs](#chan%5Fcache%5Fremoval%5Frevs)
* [chan\_cache\_tombstone\_revs](#chan%5Fcache%5Ftombstone%5Frevs)
* [compaction\_attachment\_start\_time](#compaction%5Fattachment%5Fstart%5Ftime)
* [compaction\_tombstone\_start\_time](#compaction%5Ftombstone%5Fstart%5Ftime)
* [conflict\_write\_count](#conflict%5Fwrite%5Fcount)
* [crc32c\_match\_count](#crc32c%5Fmatch%5Fcount)

[Back to Index Start](#alphabetic-index)

### [](#d-g)D - G

* [database](#database)
* [dcp\_caching\_count](#dcp%5Fcaching%5Fcount)
* [dcp\_caching\_time](#dcp%5Fcaching%5Ftime)
* [dcp\_received\_count](#dcp%5Freceived%5Fcount)
* [dcp\_received\_time](#dcp%5Freceived%5Ftime)
* [delta\_cache\_hit](#delta%5Fcache%5Fhit)
* [delta\_cache\_miss](#delta%5Fcache%5Fmiss)
* [delta\_pull\_replication\_count](#delta%5Fpull%5Freplication%5Fcount)
* [delta\_push\_docs\_count](#delta%5Fpush%5Fdocs%5Fcount)
* [delta\_sync](#delta%5Fsync)
* [deltas\_requested](#deltas%5Frequested)
* [deltas\_sent](#deltas%5Fsent)
* [doc\_push\_count](#doc%5Fpush%5Fcount)
* [doc\_reads\_bytes\_blip](#doc%5Freads%5Fbytes%5Fblip)
* [doc\_writes\_bytes\_blip](#doc%5Fwrites%5Fbytes%5Fblip)
* [doc\_writes\_bytes](#doc%5Fwrites%5Fbytes)
* [doc\_writes\_xattr\_bytes](#doc%5Fwrites%5Fxattr%5Fbytes)
* [error\_count](#error%5Fcount)
* [global](#global)
* [go\_memstats\_heapalloc](#go%5Fmemstats%5Fheapalloc)
* [go\_memstats\_heapidle](#go%5Fmemstats%5Fheapidle)
* [go\_memstats\_heapinuse](#go%5Fmemstats%5Fheapinuse)
* [go\_memstats\_heapreleased](#go%5Fmemstats%5Fheapreleased)
* [go\_memstats\_pausetotalns](#go%5Fmemstats%5Fpausetotalns)
* [go\_memstats\_stackinuse](#go%5Fmemstats%5Fstackinuse)
* [go\_memstats\_stacksys](#go%5Fmemstats%5Fstacksys)
* [go\_memstats\_sys](#go%5Fmemstats%5Fsys)
* [goroutines\_high\_watermark](#goroutines%5Fhigh%5Fwatermark)
* [gsi\_views](#gsi%5Fviews)
* [GSIs](#gsi)

[Back to Index Start](#alphabetic-index)

### [](#h-n)H - N

* [high\_seq\_cached](#high%5Fseq%5Fcached)
* [high\_seq\_feed](#high%5Fseq%5Ffeed)
* [high\_seq\_stable](#high%5Fseq%5Fstable)
* [import\_cancel\_cas](#import%5Fcancel%5Fcas)
* [import\_count](#import%5Fcount)
* [import\_error\_count](#import%5Ferror%5Fcount)
* [import\_feed](#import%5Ffeed)
* [import\_high\_seq](#import%5Fhigh%5Fseq)
* [import\_partitions](#import%5Fpartitions)
* [import\_processing\_time](#import%5Fprocessing%5Ftime)
* [max\_pending](#max%5Fpending)
* [num\_access\_errors](#num%5Faccess%5Ferrors)
* [num\_access\_errors](#num%5Faccess%5Ferrors)
* [num\_active\_channels](#num%5Factive%5Fchannels)
* [num\_attachments\_compacted](#num%5Fattachments%5Fcompacted)
* [num\_doc\_reads\_blip](#num%5Fdoc%5Freads%5Fblip)
* [num\_doc\_reads\_rest](#num%5Fdoc%5Freads%5Frest)
* [num\_doc\_writes](#num%5Fdoc%5Fwrites)
* [num\_docs\_rejected](#num%5Fdocs%5Frejected)
* [num\_docs\_rejected](#num%5Fdocs%5Frejected)
* [num\_goroutines](#num%5Fgoroutines)
* [num\_pull\_repl\_active\_continuous](#num%5Fpull%5Frepl%5Factive%5Fcontinuous)
* [num\_pull\_repl\_active\_one\_shot](#num%5Fpull%5Frepl%5Factive%5Fone%5Fshot)
* [num\_pull\_repl\_caught\_up](#num%5Fpull%5Frepl%5Fcaught%5Fup)
* [num\_pull\_repl\_since\_zero](#num%5Fpull%5Frepl%5Fsince%5Fzero)
* [num\_pull\_repl\_total\_continuous](#num%5Fpull%5Frepl%5Ftotal%5Fcontinuous)
* [num\_pull\_repl\_total\_one\_shot](#num%5Fpull%5Frepl%5Ftotal%5Fone%5Fshot)
* [num\_replications\_active](#num%5Freplications%5Factive)
* [num\_replications\_total](#num%5Freplications%5Ftotal)
* [num\_skipped\_seqs](#num%5Fskipped%5Fseqs)

[Back to Index Start](#alphabetic-index)

### [](#p-z)P - Z

* [pending\_seq\_len](#pending%5Fseq%5Flen)
* [per\_db](#per%5Fdb)
* [per\_replication](#per%5Freplication)
* [process\_cpu\_percent\_utilization](#process%5Fcpu%5Fpercent%5Futilization)
* [process\_memory\_resident](#process%5Fmemory%5Fresident)
* [propose\_change\_count](#propose%5Fchange%5Fcount)
* [propose\_change\_time](#propose%5Fchange%5Ftime)
* [pub\_net\_bytes\_recv](#pub%5Fnet%5Fbytes%5Frecv)
* [pub\_net\_bytes\_sent](#pub%5Fnet%5Fbytes%5Fsent)
* [request\_changes\_count](#request%5Fchanges%5Fcount)
* [request\_changes\_time](#request%5Fchanges%5Ftime)
* [resource\_utilization](#resource%5Futilization)
* [rev\_cache\_bypass](#rev%5Fcache%5Fbypass)
* [rev\_cache\_hits](#rev%5Fcache%5Fhits)
* [rev\_cache\_misses](#rev%5Fcache%5Fmisses)
* [rev\_processing\_time](#rev%5Fprocessing%5Ftime)
* [rev\_send\_count](#rev%5Fsend%5Fcount)
* [rev\_send\_latency](#rev%5Fsend%5Flatency)
* [security](#security)
* [sequence\_assigned\_count](#sequence%5Fassigned%5Fcount)
* [sequence\_get\_count](#sequence%5Fget%5Fcount)
* [sequence\_incr\_count](#sequence%5Fincr%5Fcount)
* [sequence\_released\_count](#sequence%5Freleased%5Fcount)
* [sequence\_reserved\_count](#sequence%5Freserved%5Fcount)
* [sgr\_active](#sgr%5Factive)
* [sgr\_docs\_checked\_sent](#sgr%5Fdocs%5Fchecked%5Fsent)
* [sgr\_num\_attachment\_bytes\_transferred](#sgr%5Fnum%5Fattachment%5Fbytes%5Ftransferred)
* [sgr\_num\_attachments\_transferred](#sgr%5Fnum%5Fattachments%5Ftransferred)
* [sgr\_num\_docs\_failed\_to\_push](#sgr%5Fnum%5Fdocs%5Ffailed%5Fto%5Fpush)
* [sgr\_num\_docs\_pushed](#sgr%5Fnum%5Fdocs%5Fpushed)
* [sgr\_active](#sgr%5Factive)
* [sgr\_conflict\_resolved\_local\_count](#sgr%5Fconflict%5Fresolved%5Flocal%5Fcount)
* [sgr\_conflict\_resolved\_merge\_count](#sgr%5Fconflict%5Fresolved%5Fmerge%5Fcount)
* [sgr\_conflict\_resolved\_remote\_count](#sgr%5Fconflict%5Fresolved%5Fremote%5Fcount)
* [sgr\_deltas\_recv](#sgr%5Fdeltas%5Frecv)
* [sgr\_deltas\_requested](#sgr%5Fdeltas%5Frequested)
* [sgr\_deltas\_sent](#sgr%5Fdeltas%5Fsent)
* [sgr\_docs\_checked\_recv](#sgr%5Fdocs%5Fchecked%5Frecv)
* [sgr\_docs\_checked\_sent](#sgr%5Fdocs%5Fchecked%5Fsent)
* [sgr\_num\_attachment\_bytes\_pulled](#sgr%5Fnum%5Fattachment%5Fbytes%5Fpulled)
* [sgr\_num\_attachment\_bytes\_pushed](#sgr%5Fnum%5Fattachment%5Fbytes%5Fpushed)
* [sgr\_num\_attachment\_bytes\_transferred](#sgr%5Fnum%5Fattachment%5Fbytes%5Ftransferred)
* [sgr\_num\_attachments\_pulled](#sgr%5Fnum%5Fattachments%5Fpulled)
* [sgr\_num\_attachments\_pushed](#sgr%5Fnum%5Fattachments%5Fpushed)
* [sgr\_num\_attachments\_transferred](#sgr%5Fnum%5Fattachments%5Ftransferred)
* [sgr\_num\_docs\_failed\_to\_pull](#sgr%5Fnum%5Fdocs%5Ffailed%5Fto%5Fpull)
* [sgr\_num\_docs\_failed\_to\_push](#sgr%5Fnum%5Fdocs%5Ffailed%5Fto%5Fpush)
* [sgr\_num\_docs\_pulled](#sgr%5Fnum%5Fdocs%5Fpulled)
* [sgr\_num\_docs\_purged](#sgr%5Fnum%5Fdocs%5Fpurged)
* [sgr\_num\_docs\_pushed](#sgr%5Fnum%5Fdocs%5Fpushed)
* [sgr\_push\_conflict\_count](#sgr%5Fpush%5Fconflict%5Fcount)
* [sgr\_push\_rejected\_count](#sgr%5Fpush%5Frejected%5Fcount)
* [shared\_bucket\_import](#shared%5Fbucket%5Fimport)
* [skipped\_seq\_len](#skipped%5Fseq%5Flen)
* [sync\_function\_count](#sync%5Ffunction%5Fcount)
* [sync\_function\_time](#sync%5Ffunction%5Ftime)
* [syncgateway](##syncgateway)
* [system\_memory\_total](#system%5Fmemory%5Ftotal)
* [total\_auth\_time](#total%5Fauth%5Ftime)
* [total\_auth\_time](#total%5Fauth%5Ftime)
* [uptime](#uptime)
* [view\_queries](#view%5Fqueries)
* [Views (Design doc or view)](#views)
* [warn\_channel\_name\_size\_count](#warn%5Fchannel%5Fname%5Fsize%5Fcount)
* [warn\_channels\_per\_doc\_count](#warn%5Fchannels%5Fper%5Fdoc%5Fcount)
* [warn\_count](#warn%5Fcount)
* [warn\_grants\_per\_doc\_count](#warn%5Fgrants%5Fper%5Fdoc%5Fcount)
* [warn\_xattr\_size\_count](#warn%5Fxattr%5Fsize%5Fcount)
* [write\_processing\_time](#write%5Fprocessing%5Ftime)

[Back to Index Start](#alphabetic-index)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)