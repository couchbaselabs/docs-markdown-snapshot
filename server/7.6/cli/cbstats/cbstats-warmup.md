---
title: warmup
description: Shows statistics related to the node warmup.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-warmup.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-warmup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-warmup.html)

# warmup

> Shows statistics related to the node warmup. 

## [](#syntax)Syntax

The basic syntax is:

cbstats [host]:[dataport] -b [bucket_name] -p [bucket_password] warmup

## [](#description)Description

If a Couchbase Server node is starting up for the first time, it creates any database files that are necessary and begins serving data immediately. However, if there is already data on the disk, usually because the node rebooted or the service restarted, the node needs to read all of this data of the disk before it can begin serving data. This process is called _warmup_ and it can take some time depending on the size of the data.

The information about server warmup includes the status of warmup and whether warmup is enabled. The bucket must be specified for the bucket statistics; it does not need to be specified if the default bucket statistics is requested.

The following statistics are of particular interest when monitoring the warmup:

ep\_warmup\_thread

The overall indication of whether or not warmup is still running. Look for values: running and complete.

ep\_warmup\_state

This describes which phase of warmup is currently running. Look for values: loading keys, loading access log, and done.

* When `ep_warmup_state` is loading keys, compare `ep_warmup_key_count` (current number) with `ep_warmup_estimated_key_count` (target number).
* When `ep_warmup_state` is loading access log, compare `ep_warmup_value_count` (current number) with `ep_warmup_estimated_value_count` (target number).

__Table 1\. cbstats warmup stats__
| Statistic                           | Description                                                                                               | Value Type                         |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| ep\_warmup                          | Shows if warmup is enabled /disabled.                                                                     | String values: enabled or disabled |
| ep\_warmup\_dups                    | Number of failures due to duplicate keys.                                                                 | Integer                            |
| ep\_warmup\_estimated\_key\_count   | The estimated number of keys in database.                                                                 | Integer. Default: unknown          |
| ep\_warmup\_estimate\_time          | The time taken, measured in milliseconds, to discover the estimated number of keys that may be warmed up. | Integer.                           |
| ep\_warmup\_estimated\_value\_count | The estimated number of key data to read based on the access log.                                         | Integer. Default: unknown          |
| ep\_warmup\_key\_count              | Number of keys warmed up.                                                                                 | Integer                            |
| ep\_warmup\_keys\_time              | Total time (in microseconds) spent by loading persisted keys.                                             | Integer                            |
| ep\_warmup\_min\_items\_threshold   | Enable data traffic after loading this percentage of key data.                                            | Integer                            |
| ep\_warmup\_min\_memory\_threshold  | Enable data traffic after filling this % of memory.                                                       | Integer (%)                        |
| ep\_warmup\_oom                     | Number of out of memory failures during warmup.                                                           | Integer                            |
| ep\_warmup\_state                   | The current state of the warmup thread.                                                                   | String                             |
| ep\_warmup\_thread                  | Warmup thread status.                                                                                     | String values: running or complete |
| ep\_warmup\_time                    | Total time spent by loading data (warmup).                                                                | Integer (microseconds)             |
| ep\_warmup\_value\_count            | Number of values warmed up.                                                                               | Integer                            |

## [](#options)Options

The following are the command options:

__Table 2\. warmup options__
| Option           | Description                  |
| ---------------- | ---------------------------- |
| bucket\_password | The password for the bucket. |
| bucket\_name     | Name of the bucket.          |

## [](#example)Example

**Request**

cbstats localhost:11210 warmup \
-u Administrator \
-p password \
-b travel-sample

**Response**

Example response:

ep_warmup:                      enabled
ep_warmup_dups:                 0
ep_warmup_estimate_time:        36013
ep_warmup_estimated_key_count:  63310
ep_warmup_estimated_value_count: 63310
ep_warmup_key_count:            63310
ep_warmup_keys_time:            523406
ep_warmup_min_item_threshold:   100
ep_warmup_min_memory_threshold: 100
ep_warmup_oom:                  0
ep_warmup_state:                done
ep_warmup_thread:               complete
ep_warmup_time:                 584419
ep_warmup_value_count:          63310