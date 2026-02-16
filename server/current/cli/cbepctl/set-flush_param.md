[View original HTML](/server/current/cli/cbepctl/set-flush_param.html)

> The command `set flush_param` establishes bucket parameters for threading and memory management. 

## [](#syntax)Syntax

The basic syntax is:

cbepctl [host]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param [parameter] [value]

The syntax to configure the access log settings is:

cbepctl [hostname]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param alog_sleep_time [value]
cbepctl [hostname]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param alog_task_time [value]

The syntax for ejection is:

cbepctl [host]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param [parameter] [value]

The syntax to set the out-of-memory threshold is:

cbepctl [host]:11210 -b [bucket-name] -u [administrator-name] -p [administrator-password] set flush_param mutation_mem_threshold [value]

## [](#description)Description

Tune the dynamic shared thread pool performance by changing the thread types inside the ep-engine and memcached at run time. The command `set flush_param` adjusts the number of threads that prioritize read, write, non-i/o and auxiliary-i/o operations. These settings take effect immediately and do not require that the bucket be restarted.

|  | The settings for threads number take effect only if the underlying operating system has a sufficient number of CPU cores. The minimum number of CPU cores is four (4), but three (3) additional cores are required for each additional writer thread. For example, five (5) writer threads is a valid setting if the underlying hardware has at least sixteen (16) cores. Changes of thresholds are NOT persistent and must be reapplied after the bucket warmup. The settings warmup\_min\_items\_threshold, warmup\_min\_memory\_threshold, exp\_pager\_stime, mem\_high\_wat, and mem\_low\_wat are removed, and no longer supported through cbepctl. These settings are replaced by new settings expiryPagerSleepTime, warmupBehavior, memoryLowWatermark, and memoryHighWatermark, which can be configured using REST APIs. See [Creating and Editing Buckets](../../rest-api/rest-bucket-create.md). |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

alog\_sleep\_time, alog\_task\_time

Couchbase Server has an optimized [disk warmup](../../learn/buckets-memory-and-storage/memory.md#initialization-and-warmup). An _access scanner_ is periodically run, to determine which keys have been the most frequently used: typically, the scanner writes these key to an _access log_, which can be accessed by Couchbase Server at warmup, so that the corresponding documents can be loaded first. (See [Initialization and Warmup](../../learn/buckets-memory-and-storage/memory.md#initialization-and-warmup) for further information; including cases where item-residency is at very high levels, and in consequence, no access log is created or used.)

The `cbepctl flush_param` command is used to change the initial time and the interval for the access scanner. For example, the initial time and interval might be changed to accommodate a peak time when an application needs these keys to be quickly available.

By default, the access scanner runs once every 24 hours at 10:00 AM GMT. The scanner is highly CPU-intensive: therefore, to reduce the cluster-wide impact of running this task, its start time should be staggered to a different value on each node in the cluster. Note also that if the scanner runs at the same time that index updates are being made (either on the current node, or on one or more other nodes) by the Index Service, the performance of the index updates may be adversely affected. The scanner should be configured to minimize the likelihood of this problem.

|  | The access scanner always scans the entire key table, so increasing the frequency of the scans will not decrease the amount of work the scanner is doing. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------- |

mutation\_mem\_threshold

By default, Couchbase Server sends clients a temporary out-of-memory error message if RAM is 95% consumed and only 5% RAM remains for overhead. Use the `cbepctl set flush_param mutation_mem-threshold` command parameter to change this threshold value.

|  | Do not change this default to a higher value. However, this value might be reduced if you need more RAM for system overhead such as disk queue or for server data structures. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#options)Options

The following are the command options:

__Table 1\. set flush\_param options__
| Option                            | Description                                                                                                                                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alog\_sleep\_time                 | Access scanner interval (minute)                                                                                                                                                              |
| alog\_task\_time                  | Access scanner next task time (UTC)                                                                                                                                                           |
| backfile\_mem\_threshold          | Memory threshold (%) on the current bucket quota before backfill task is made to back off.                                                                                                    |
| bg\_fetch\_delay                  | Delay before executing a bg fetch (test feature).                                                                                                                                             |
| couch\_response\_timeout          | timeout in receiving a response from CouchDB.                                                                                                                                                 |
| flushall\_enabled                 | Deprecated. Enable flush operation.                                                                                                                                                           |
| max\_size                         | Maximum memory used by the server.                                                                                                                                                            |
| mutation\_mem\_threshold          | Amount of RAM that can be consumed in that caching layer before clients start receiving temporary out of memory messages.                                                                     |
| timing\_log                       | Path to log detailed timing stats.                                                                                                                                                            |
| klog\_compactor\_queue\_cap       | Queue cap to throttle the log compactor.                                                                                                                                                      |
| klog\_max\_log\_size              | Maximum size of a mutation log file allowed.                                                                                                                                                  |
| klog\_max\_entry\_ratio           | Max ratio of # of items logged to # of unique items.                                                                                                                                          |
| pager\_unbiased\_period           | Period after last access scanner run during which item pager preserve working set.                                                                                                            |
| queue\_age\_cap                   | Maximum queue age before flushing data.                                                                                                                                                       |
| max\_txn\_size                    | Maximum number of items in a flusher transaction.                                                                                                                                             |
| min\_data\_age                    | Minimum data age before flushing data.                                                                                                                                                        |
| item\_compressor\_interval        | How often the item compressor task should be run, in milliseconds. Default value is 250.                                                                                                      |
| item\_compressor\_chunk\_duration | Maximum time, in milliseconds, for which the item compressor task is run, before being paused, and then resumed according to the established item\_compressor\_interval. Default value is 20. |
| min\_compression\_ratio           | Minimum allowed ratio of each item’s uncompressed form to its compressed form. If the actual ratio is less than this value, the item is stored in uncompressed form. Default value is 1.2.    |

|  | **%** You must use the percentage sign in order to set the value by percentage. |
|  | ------------------------------------------------------------------------------- |

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

**Examples for setting the out-of-memory error message**

In this example, the threshold is reduced to 65% of RAM.

cbepctl 10.5.2.117:11210 -b foo-bucket -u Administrator -p password \
set flush_param mutation_mem_threshold 65%

The following example response shows the RAM threshold set to 65%.

setting param: mutation_mem_threshold 65
set mutation_mem_threshold to 65