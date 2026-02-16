[View original HTML](/server/7.6/cli/cbstats/cbstats-timing.html)

> Provides timing statistics. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] timings

## [](#description)Description

The timing stats provide histogram data from high-resolution timers over various operations within the system. This only measures the time spent in the front-end thread for each operation, meaning that the timings may not be representative if items have to be fetched from disk as part of the operation.

To retrieve more accurate timing statistics, use [mctimings](../mctimings.md) instead of `timings`.

The following are the possible return values, which depend on what occurred on the data bucket:

__Table 1\. Return values__
| Values                                                  | Description                                                                                                                                                                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bg\_load                                                | Background fetches waiting for disk.                                                                                                                                                                        |
| bg\_wait                                                | Background fetches waiting in the dispatcher queue.                                                                                                                                                         |
| set\_with\_meta                                         | set\_with\_meta latencies.                                                                                                                                                                                  |
| access\_scanner                                         | Access scanner run times.                                                                                                                                                                                   |
| checkpoint\_remover                                     | Checkpoint remover run times.                                                                                                                                                                               |
| item\_pager                                             | Item pager run times.                                                                                                                                                                                       |
| expiry\_pager                                           | Expiry pager run times.                                                                                                                                                                                     |
| pending\_ops                                            | Client connections blocked for operations in pending vBuckets.                                                                                                                                              |
| data\_age                                               | Age of data written to disk.                                                                                                                                                                                |
| disk\_commit                                            | Time waiting for a commit after a batch of updates.                                                                                                                                                         |
| disk\_del                                               | Wait for disk to delete an item.                                                                                                                                                                            |
| disk\_vb\_del                                           | Waiting for disk to delete a vBucket.                                                                                                                                                                       |
| disk\_insert                                            | Wait for disk to store a new item.                                                                                                                                                                          |
| disk\_update                                            | Wait time for disk to modify an existing item.                                                                                                                                                              |
| get\_cmd                                                | Servicing get requests.                                                                                                                                                                                     |
| store\_cmd                                              | Servicing store requests.                                                                                                                                                                                   |
| arith\_cmd                                              | Servicing incr/decr requests.                                                                                                                                                                               |
| get\_stats\_cmd                                         | Servicing get\_stats requests.                                                                                                                                                                              |
| get\_vb\_cmd                                            | Servicing vBucket status requests.                                                                                                                                                                          |
| set\_vb\_cmd                                            | Servicing vBucket set state commands.                                                                                                                                                                       |
| del\_vb\_cmd                                            | Servicing vBucket deletion commands.                                                                                                                                                                        |
| chk\_persistence\_cmd                                   | Waiting for checkpoint persistence.                                                                                                                                                                         |
| item\_alloc\_sizes                                      | Item allocation size counters (in bytes).                                                                                                                                                                   |
| notify\_io                                              | Time for waking blocked connections.                                                                                                                                                                        |
| paged\_out\_time                                        | Time (in seconds) objects are non-resident.                                                                                                                                                                 |
| storage\_age                                            | Time since most recently persisted item was initially queued for storage.                                                                                                                                   |
| bg\_batch\_size                                         | Batch size for background fetches.                                                                                                                                                                          |
| persistence\_cursor\_get\_all\_items                    | Time spent in fetching all items by persistence cursor from checkpoint queues.                                                                                                                              |
| dcp\_cursors\_get\_all\_items                           | Time spent in fetching all items by all dcp cursors from checkpoint queues.                                                                                                                                 |
| sync\_write\_commit\_majority                           | Time spent in replicating mutations to memory on a majority of the Data Service nodes that hold the data.                                                                                                   |
| sync\_write\_commit\_majority\_and\_persist\_on\_master | Time spent in replicating mutations to memory on a majority of the Data Service nodes that hold the data, plus time spent in writing mutations to disk on the node hosting the active vBucket for the data. |
| sync\_write\_commit\_persist\_to\_majority              | Time spent in replicating mutations to disk on a majority of the Data Service nodes that hold the data.                                                                                                     |

|  | The most useful stats for understanding get and set timings are get\_cmd and store\_cmd. |
|  | ---------------------------------------------------------------------------------------- |

## [](#options)Options

There are no options for this command. For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

cbstats localhost:11210 -u Administrator -p password -b beer-sample timings

**Response**

 checkpoint_remover (101 total)
    2ms - 4ms        : ( 12.87%) 13 █████▌
    4ms - 8ms        : ( 94.06%) 82 ██████████████████████████████████▉
    8ms - 16ms       : ( 98.02%)  4 █▋
    16ms - 32ms      : (100.00%)  2 ▊
    Avg              : (    4ms)
 dcp_cursors_get_all_items (2 total)
    1us - 2us        : ( 50.00%) 1 ██████████████████████
    2us - 4us        : ( 50.00%) 0
    4us - 8us        : (100.00%) 1 ██████████████████████
    Avg              : (    2us)
 disk_commit (1 total)
    2ms - 4ms        : (100.00%) 1 ████████████████████████████████████████████
    Avg              : (    2ms)
 disk_update (1 total)
    4us - 8us        : (100.00%) 1 ████████████████████████████████████████████
    Avg              : (    4us)
 get_cmd (3 total)
    4m:28s - 8m:56s  : (100.00%) 3 ████████████████████████████████████████████
    Avg              : ( 4m:28s)
 get_stats_cmd (2220 total)
    16s - 33s        : (  0.50%)   11 ▏
    33s - 1m:07s     : (  4.50%)   89 █▋
    1m:07s - 2m:14s  : ( 14.05%)  212 ███▉
    2m:14s - 4m:28s  : ( 42.12%)  623 ███████████▌
    4m:28s - 8m:56s  : (100.00%) 1285 ███████████████████████▋
    Avg              : ( 3m:20s)
 item_alloc_sizes (1 total)
    512 - 1KB     : (100.00%) 1 ███████████████████████████████████████████████
    Avg           : (    512)
 notify_io (4839 total)
    0 - 1us          : ( 17.42%)  843 ███████▏
    1us - 2us        : ( 26.04%)  417 ███▌
    2us - 4us        : ( 42.10%)  777 ██████▌
    4us - 8us        : ( 70.04%) 1352 ███████████▍
    8us - 16us       : ( 78.43%)  406 ███▍
    16us - 32us      : ( 90.80%)  599 █████
    32us - 64us      : ( 95.60%)  232 █▉
    64us - 128us     : ( 96.42%)   40 ▎
    128us - 256us    : ( 97.56%)   55 ▍
    256us - 512us    : ( 98.74%)   57 ▍
    512us - 1ms      : ( 99.03%)   14
    1ms - 2ms        : ( 99.24%)   10
    2ms - 4ms        : ( 99.48%)   12
    4ms - 8ms        : ( 99.90%)   20 ▏
    8ms - 16ms       : ( 99.98%)    4
    16ms - 32ms      : (100.00%)    1
    Avg              : (   46us)
 persistence_cursor_get_all_items (60416 total)
    0 - 1us          : ( 96.83%) 58501 ██████████████████████████████████████▋
    1us - 2us        : ( 99.33%)  1511 █
    2us - 4us        : ( 99.79%)   276 ▏
    4us - 8us        : ( 99.82%)    18
    8us - 16us       : ( 99.83%)     8
    16us - 32us      : ( 99.85%)    11
    32us - 64us      : ( 99.90%)    32
    64us - 128us     : ( 99.94%)    24
    128us - 256us    : ( 99.95%)     5
    256us - 512us    : ( 99.96%)     4
    512us - 1ms      : ( 99.96%)     1
    1ms - 2ms        : ( 99.97%)     4
    2ms - 4ms        : ( 99.98%)     7
    4ms - 8ms        : ( 99.99%)     7
    8ms - 16ms       : (100.00%)     6
    16ms - 32ms      : (100.00%)     1
    Avg              : (    1us)
 storage_age (1 total)
    0 - 1us          : (100.00%) 1 ████████████████████████████████████████████
    Avg              : (      0)
 store_cmd (1 total)
    4m:28s - 8m:56s  : (100.00%) 1 ████████████████████████████████████████████
    Avg              : ( 4m:28s)