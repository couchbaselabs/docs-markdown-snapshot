---
title: set flush_param
description: The command <code class="cmd">set flush_param</code> establishes
  bucket parameters for threading and memory management.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbepctl/set-flush_param.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/cli/cbepctl/set-flush_param.html)

# set flush_param

> The command `set flush_param` establishes bucket parameters for threading and memory management. 

## [](#syntax)Syntax

The basic syntax is:

cbepctl [host]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param [parameter] [value]

The syntax to configure the access log settings is:

cbepctl [hostname]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param alog_sleep_time [value]
cbepctl [hostname]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param alog_task_time [value]

The syntax for asynchronous expiry is:

cbepctl [host]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param exp_pager_stime [value]

The syntax for ejection is:

cbepctl [host]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param [parameter] [value]

Parameters used for changing ejection thresholds:

* `mem_low_wat`
* `mem_high_wat`

The syntax to set the out-of-memory threshold is:

cbepctl [host]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param mutation_mem_threshold [value]

## [](#description)Description

Tune the dynamic shared thread pool performance by changing the thread types inside the ep-engine and memcached at run time. The command `set flush_param` adjusts the number of threads that prioritize read, write, non-i/o and auxiliary-i/o operations. These settings take effect immediately and do not require that the bucket be restarted.

> [!NOTE]
> The settings for threads number take effect only if the underlying operating system has a sufficient number of CPU cores. The minimum number of CPU cores is four (4), but three (3) additional cores are required for each additional writer thread. For example, five (5) writer threads is a valid setting if the underlying hardware has at least sixteen (16) cores.

> [!NOTE]
> Changes of thresholds are NOT persistent and must be reapplied after the bucket warmup.

alog\_sleep\_time, alog\_task\_time

Couchbase Server has an optimized [disk warmup](../../learn/buckets-memory-and-storage/memory.md#initialization-and-warmup). An _access scanner_ is periodically run, to determine which keys have been the most frequently used: typically, the scanner writes these key to an _access log_, which can be accessed by Couchbase Server at warmup, so that the corresponding documents can be loaded first. (See [Initialization and Warmup](../../learn/buckets-memory-and-storage/memory.md#initialization-and-warmup) for further information; including cases where item-residency is at very high levels, and in consequence, no access log is created or used.)

The `cbepctl flush_param` command is used to change the initial time and the interval for the access scanner. For example, the initial time and interval might be changed to accommodate a peak time when an application needs these keys to be quickly available.

By default, the access scanner runs once every 24 hours at 10:00 AM GMT. The scanner is highly CPU-intensive: therefore, to reduce the cluster-wide impact of running this task, its start time should be staggered to a different value on each node in the cluster. Note also that if the scanner runs at the same time that index updates are being made (either on the current node, or on one or more other nodes) by the Index Service, the performance of the index updates may be adversely affected. The scanner should be configured to minimize the likelihood of this problem.

> [!NOTE]
> The access scanner always scans the entire key table, so increasing the frequency of the scans will not decrease the amount of work the scanner is doing.

exp\_pager\_stime

The `cbepctl flush_param exp_pager_stime` command sets the time interval to scan for expired items and erase them from memory. Couchbase Server does lazy [expiration](../../learn/buckets-memory-and-storage/memory.md#expiry-pager), that is, expired items are flagged as deleted rather than being immediately erased. Couchbase Server has a maintenance process that periodically looks through all information and erases expired items. By default, this maintenance process runs every 10 minutes, but it can be configured to run at a different interval.

> [!NOTE]
> The compaction process will also remove expired items.

mem\_low\_wat, mem\_high\_wat

[Ejection](../../learn/buckets-memory-and-storage/memory.md#ejection) means that documents are removed from RAM but the key and metadata remain. If the amount of RAM used by items reaches the high water mark (upper threshold), both active and replica data are ejected until the memory usage (amount of RAM consumed) reaches the low water mark (lower threshold). The server determines that items are not recently used based on a not-recently-used (NRU) value.

Use the `mem_low_wat` and `mem_high_wat` settings to change the server thresholds for ejection.

> [!WARNING]
> Do not change the ejection defaults unless required by Couchbase Support.

mutation\_mem\_threshold

By default, Couchbase Server sends clients a temporary out-of-memory error message if RAM is 95% consumed and only 5% RAM remains for overhead. Use the `cbepctl set flush_param mutation_mem-threshold` command parameter to change this threshold value.

> [!NOTE]
> Do not change this default to a higher value. However, this value might be reduced if you need more RAM for system overhead such as disk queue or for server data structures.

## [](#options)Options

The following are the command options:

__Table 1\. set flush\_param options__
| Option                            | Description                                                                                                                                                                                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alog\_sleep\_time                 | Access scanner interval (minute)                                                                                                                                                                          |
| alog\_task\_time                  | Access scanner next task time (UTC)                                                                                                                                                                       |
| backfile\_mem\_threshold          | Memory threshold (%) on the current bucket quota before backfill task is made to back off.                                                                                                                |
| bg\_fetch\_delay                  | Delay before executing a bg fetch (test feature).                                                                                                                                                         |
| couch\_response\_timeout          | timeout in receiving a response from CouchDB.                                                                                                                                                             |
| exp\_pager\_stime                 | Expiry Pager interval. Time interval that Couchbase Server waits before it performs cleanup and removal of expired items from memory. Setting this value to 0 will disable the Expiry Pager from running. |
| flushall\_enabled                 | Deprecated. Enable flush operation.                                                                                                                                                                       |
| max\_size                         | Maximum memory used by the server.                                                                                                                                                                        |
| mem\_high\_wat                    | High water mark in bytes.                                                                                                                                                                                 |
| mem\_low\_wat                     | Low water mark in bytes.                                                                                                                                                                                  |
| mutation\_mem\_threshold          | Amount of RAM that can be consumed in that caching layer before clients start receiving temporary out of memory messages.                                                                                 |
| timing\_log                       | Path to log detailed timing stats.                                                                                                                                                                        |
| warmup\_min\_memory\_threshold    | Memory threshold (%) during warmup to enable traffic.                                                                                                                                                     |
| warmup\_min\_items\_threshold     | Item number threshold (%) during warmup to enable traffic.                                                                                                                                                |
| klog\_compactor\_queue\_cap       | Queue cap to throttle the log compactor.                                                                                                                                                                  |
| klog\_max\_log\_size              | Maximum size of a mutation log file allowed.                                                                                                                                                              |
| klog\_max\_entry\_ratio           | Max ratio of # of items logged to # of unique items.                                                                                                                                                      |
| pager\_unbiased\_period           | Period after last access scanner run during which item pager preserve working set.                                                                                                                        |
| queue\_age\_cap                   | Maximum queue age before flushing data.                                                                                                                                                                   |
| max\_txn\_size                    | Maximum number of items in a flusher transaction.                                                                                                                                                         |
| min\_data\_age                    | Minimum data age before flushing data.                                                                                                                                                                    |
| item\_compressor\_interval        | How often the item compressor task should be run, in milliseconds. Default value is 250.                                                                                                                  |
| item\_compressor\_chunk\_duration | Maximum time, in milliseconds, for which the item compressor task is run, before being paused, and then resumed according to the established item\_compressor\_interval. Default value is 20.             |
| min\_compression\_ratio           | Minimum allowed ratio of each item’s uncompressed form to its compressed form. If the actual ratio is less than this value, the item is stored in uncompressed form. Default value is 1.2.                |

> [!NOTE]
> **%** You must use the percentage sign in order to set the value by percentage.

## [](#examples)Examples

**Examples for setting the access scanner process**

To change the time interval when the access scanner process runs to every 2880 minutes (2 days).

cbepctl 10.5.2.117:11210 -b foo-bucket -u Administrator -p password \
set flush_param alog_sleep_time 2880

This response shows the time interval changed to 2 days.

setting param: alog_sleep_time 2880
set alog_sleep_time to 2880

To change the initial time that the access scanner process runs from the 2:00 AM UTC default to 11:00 PM UTC.

cbepctl 10.5.2.117:11210 -b foo-bucket -u Administrator -p password \
set flush_param alog_task_time 23

This response shows the initial access scanner run time changed to 11:00 PM UTC.

setting param: alog_task_time 23
set alog_task_time to 23

**Examples for setting the memory cleanup**

The following example sets the cleanup process to run every 600 seconds (10 minutes). This is the interval that Couchbase Server waits before it tries to remove expired items from memory.

cbepctl 10.5.2.117:11210 -b foo-bucket -u Administrator -p password \
set flush_param exp_pager_stime 600

The following example response shows the cleanup process set to 600 seconds.

setting param: exp_pager_stime 600
set exp_pager_stime to 600

**Examples for setting the out-of-memory error message**

In this example, the threshold is reduced to 65% of RAM.

cbepctl 10.5.2.117:11210 -b foo-bucket -u Administrator -p password \
set flush_param mutation_mem_threshold 65%

The following example response shows the RAM threshold set to 65%.

setting param: mutation_mem_threshold 65
set mutation_mem_threshold to 65

**Example for setting the low water mark**

The low water mark sets the lower threshold of RAM for a specific bucket on a node. The item pager stops ejecting items once the low water mark is reached.

The following example sets the low water mark percentage to 70% of RAM.

cbepctl 10.5.2.117:11210 -b foo-bucket -u Administrator -p password \
set flush_param mem_low_wat 70%

The following example response shows the low water mark set to 70%.

setting param: mem_low_wat 70
set mem_low_wat to 70

**Example for setting the high water mark**

The high water mark sets the amount of RAM consumed by items that must be breached before infrequently used active and replica items are ejected.

The following example sets the high water mark percentage to 80% of RAM for a specific bucket on a node. This means that items in RAM on this node can consume up to 80% of RAM before the item pager begins ejecting items.

cbepctl 10.5.2.117:11210 -b foo-bucket -u Administrator -p password \
set flush_param mem_high_wat 80%

The following example response shows the high water mark of ejected items being set to 80%.

setting param: mem_high_wat 80
set mem_high_wat to 80