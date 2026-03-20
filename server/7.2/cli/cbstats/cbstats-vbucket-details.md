---
title: vbucket-details
description: Provides details for vBuckets.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbstats/cbstats-vbucket-details.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:cli:cbstats/cbstats-vbucket-details.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbstats/cbstats-vbucket-details.html)

# vbucket-details

> Provides details for vBuckets. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] vbucket-details [vbid]

## [](#description)Description

This command provides details for the specified vBucket, or for each vBucket if none is specified.

The identifier for each vBucket statistic begins with the string `vb_` followed by the vBucket ID and a colon. For example, for vBucket 1023, the identifier for the `uuid` statistic is `vb_1023:uuid`.

__Table 1\. vBucket statistics__
| Name                               | Description                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| num\_items                         | Number of items in this vBucket.                                                                                                                                                                                                                                                                                                 |
| num\_tmp\_items                    | Number of temporary items in memory.                                                                                                                                                                                                                                                                                             |
| num\_non\_resident                 | Total number of items which are not resident in memory for this vBucket.                                                                                                                                                                                                                                                         |
| 'num\_prepared\_sync\_writes'      | Number of durable writes currently in progress (and therefore not yet either committed or aborted) for this vBucket.                                                                                                                                                                                                             |
| vb\_pending\_perc\_mem\_resident   | % memory resident.                                                                                                                                                                                                                                                                                                               |
| vb\_pending\_eject                 | Number of times item values got ejected.                                                                                                                                                                                                                                                                                         |
| vb\_pending\_expired               | Number of times an item was expired.                                                                                                                                                                                                                                                                                             |
| ht\_memory                         | Memory overhead of the hashtable.                                                                                                                                                                                                                                                                                                |
| ht\_item\_memory                   | Total item memory.                                                                                                                                                                                                                                                                                                               |
| ht\_cache\_size                    | Total size of cache — includes non-resident items.                                                                                                                                                                                                                                                                               |
| num\_ejects                        | Number of times an item was ejected from memory.                                                                                                                                                                                                                                                                                 |
| ops\_create                        | Number of create operations.                                                                                                                                                                                                                                                                                                     |
| ops\_update                        | Number of update operations.                                                                                                                                                                                                                                                                                                     |
| ops\_delete                        | Number of delete operations.                                                                                                                                                                                                                                                                                                     |
| ops\_reject                        | Number of rejected operations.                                                                                                                                                                                                                                                                                                   |
| queue\_size                        | Pending items in disk queue.                                                                                                                                                                                                                                                                                                     |
| backfill\_queue\_size              | Items in backfill queue.                                                                                                                                                                                                                                                                                                         |
| queue\_memory                      | Memory used for disk queue.                                                                                                                                                                                                                                                                                                      |
| queue\_age                         | Sum of disk queue item age in milliseconds.                                                                                                                                                                                                                                                                                      |
| queue\_fill                        | Total enqueued items.                                                                                                                                                                                                                                                                                                            |
| queue\_drain                       | Total drained items.                                                                                                                                                                                                                                                                                                             |
| pending writes                     | Total bytes of pending writes.                                                                                                                                                                                                                                                                                                   |
| db\_data\_size                     | Total size of useful data in the database file on disk, measured in bytes.                                                                                                                                                                                                                                                       |
| db\_file\_size                     | Total size of the database file on disk (including uncompacted stale data), measured in bytes.                                                                                                                                                                                                                                   |
| high\_seqno                        | The last seqno assigned by this vBucket.                                                                                                                                                                                                                                                                                         |
| purge\_seqno                       | The last seqno purged by the compactor.                                                                                                                                                                                                                                                                                          |
| bloom\_filter                      | Status of the vBucket’s bloom filter.                                                                                                                                                                                                                                                                                            |
| bloom\_filter\_size                | Size of the bloom filter bit array.                                                                                                                                                                                                                                                                                              |
| bloom\_filter\_key\_count          | Number of keys inserted into the bloom filter. Considers overlapped items as one, so this may not be accurate at times.                                                                                                                                                                                                          |
| uuid                               | The current vBucket uuid.                                                                                                                                                                                                                                                                                                        |
| rollback\_item\_count              | Number of items rolled back.                                                                                                                                                                                                                                                                                                     |
| hp\_vb\_req\_size                  | Number of asynchronous high priority requests.                                                                                                                                                                                                                                                                                   |
| max\_cas                           | Maximum CAS of all items in the vBucket. This is a hybrid logical clock value in nanoseconds.                                                                                                                                                                                                                                    |
| max\_cas\_str                      | The vBucket’s current maximum hybrid logical clock (HLC) timestamp. In general, this statistic shows the value issued to the last mutation, or in certain cases the largest timestamp the vBucket has received, when the received timestamp is ahead of the local clock. Displayed as a human readable ISO-8601 timestamp (UTC). |
| total\_abs\_drift                  | The accumulated absolute drift for this vBucket’s hybrid logical clock in microseconds. Drift is always accumulated as an absolute value.                                                                                                                                                                                        |
| total\_abs\_drift\_count           | The number of updates applied to total\_abs\_drift, for the purpose of average or rate calculations.                                                                                                                                                                                                                             |
| drift\_ahead\_threshold\_exceeded  | How many mutations have been observed with a drift above the drift\_ahead\_threshold.                                                                                                                                                                                                                                            |
| drift\_ahead\_threshold            | Threshold at which positive drift will trigger an update to drift\_ahead\_exceeded, measured in nanoseconds.                                                                                                                                                                                                                     |
| drift\_behind\_threshold\_exceeded | How many mutations have been observed with a drift below the drift\_behind\_threshold.                                                                                                                                                                                                                                           |
| drift\_behind\_threshold           | The threshold at which positive drift will trigger an update to drift\_behind\_exceeded. The value is displayed in nanoseconds as a positive value, but is converted to a negative value for actual exception checks.                                                                                                            |
| logical\_clock\_ticks              | How many times the hybrid logical clock (HLC) has had to increment the logical clock.                                                                                                                                                                                                                                            |
| might\_contain\_xattrs             | True if the vBucket might contain xattrs. True means that xattrs were stored to the vBucket. Note that the flag does not clear itself if all xattrs were removed.                                                                                                                                                                |
| sync\_write\_accepted\_count       | Number of synchronous-write requests in this vbucket’s sequence list.                                                                                                                                                                                                                                                            |
| sync\_write\_committed\_count      | Number of synchronous-write commits in this vbucket’s sequence list.                                                                                                                                                                                                                                                             |
| sync\_write\_aborted\_count        | Number of synchronous-write aborts in this vbucket’s sequence list.                                                                                                                                                                                                                                                              |

Note also that the `cbstats` [all](cbstats-all.md) option provides summary statistics, which sum the totals across all active and replica buckets for `sync_write_accepted_count`, `sync_write_committed_count`, and `sync_write_aborted_count`. The names of these summary statistics are `vb_active_sync_write_aborted_count`, `vb_relica_sync_write_aborted_count`, and so forth.

__Table 2\. Additional vBucket statistics for ephemeral buckets__
| Name                             | Description                                                                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| seqlist\_count                   | Number of documents in this vBucket’s sequence list.                                                                                          |
| seqlist\_deleted\_count          | Count of deleted documents in this vBucket’s sequence list.                                                                                   |
| seqlist\_high\_seqno             | High sequence number in sequence list for this vBucket.                                                                                       |
| seqlist\_highest\_deduped\_seqno | Highest de-duplicated sequence number in sequence list for this vBucket.                                                                      |
| seqlist\_read\_range\_begin      | Starting sequence number for this vBucket’s sequence list read range. Marks the lower bound of possible stale documents in the sequence list. |
| seqlist\_read\_range\_end        | Ending sequence number for this vBucket’s sequence list read range. Marks the upper bound of possible stale documents in the sequence list.   |
| seqlist\_read\_range\_count      | Count of elements for this vBucket’s sequence list read range, i.e. end - begin.                                                              |
| seqlist\_stale\_count            | Count of stale documents in this vBucket’s sequence list.                                                                                     |
| seqlist\_stale\_value\_bytes     | Number of bytes of stale values in this vBucket’s sequence list.                                                                              |
| seqlist\_stale\_metadata\_bytes  | Number of bytes of stale metadata (key + fixed metadata) in this vBucket’s sequence list.                                                     |

## [](#options)Options

__Table 3\. vbucket-details options__
| Option | Description                                                                                                                                        |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| vbid   | vBucket ID. In a standard system this will be between 0 and 1023\. If not provided as part of the command then details for all vBuckets are shown. |

For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

/opt/couchbase/bin/cbstats localhost:11210 -u Administrator -p password \
-b travel-sample vbucket-details 1023

**Response**

vb_1023:                                 active
vb_1023:bloom_filter:                    DOESN'T EXIST
vb_1023:bloom_filter_key_count:          0
vb_1023:bloom_filter_size:               0
vb_1023:db_data_size:                    12978
vb_1023:db_file_size:                    53339
vb_1023:drift_ahead_threshold:           5000000000
vb_1023:drift_ahead_threshold_exceeded:  0
vb_1023:drift_behind_threshold:          5000000000
vb_1023:drift_behind_threshold_exceeded: 0
vb_1023:high_completed_seqno:            0
vb_1023:high_prepared_seqno:             0
vb_1023:high_seqno:                      20
vb_1023:hp_vb_req_size:                  0
vb_1023:ht_cache_size:                   12459
vb_1023:ht_item_memory:                  12459
vb_1023:ht_item_memory_uncompressed:     23221
vb_1023:ht_memory:                       2584
vb_1023:ht_size:                         47
vb_1023:logical_clock_ticks:             0
vb_1023:max_cas:                         1572448621032374272
vb_1023:max_cas_str:                     2019-10-30T15:17:01.32374272
vb_1023:max_deleted_revid:               0
vb_1023:might_contain_xattrs:            false
vb_1023:num_ejects:                      0
vb_1023:num_items:                       20
vb_1023:num_non_resident:                0
vb_1023:num_prepared_sync_writes:        0
vb_1023:num_temp_items:                  0
vb_1023:ops_create:                      0
vb_1023:ops_delete:                      0
vb_1023:ops_get:                         0
vb_1023:ops_reject:                      0
vb_1023:ops_update:                      0
vb_1023:pending_writes:                  0
vb_1023:purge_seqno:                     0
vb_1023:queue_age:                       0
vb_1023:queue_drain:                     1
vb_1023:queue_fill:                      1
vb_1023:queue_memory:                    0
vb_1023:queue_size:                      0
vb_1023:rollback_item_count:             0
vb_1023:sync_write_aborted_count:        0
vb_1023:sync_write_accepted_count:       0
vb_1023:sync_write_committed_count:      0
vb_1023:topology:                        [["ns_1@127.0.0.1",null]]
vb_1023:total_abs_drift:                 0
vb_1023:total_abs_drift_count:           0
vb_1023:uuid:                            6840736809150