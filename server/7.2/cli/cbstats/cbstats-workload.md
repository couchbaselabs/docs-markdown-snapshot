---
title: workload
description: Provides the workload status of threads for buckets.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbstats/cbstats-workload.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:cli:cbstats/cbstats-workload.adoc[]
---

[View original HTML](/server/7.2/cli/cbstats/cbstats-workload.html)

# workload

> Provides the workload status of threads for buckets. 

## [](#syntax)Syntax

Basic syntax:

cbstats [hostname]:[port] -b [bucket_name] workload

## [](#description)Description

This command is used to check how many threads of various types are currently running.

## [](#options)Options

The following are the command options:

__Table 1\. workload options__
| Option | Description | bucket\_name |
| ------ | ----------- | ------------ |

## [](#example)Example

**Request:**

cbstats 10.5.2.54:11210 workload

**Response:**

This example shows four reader threads and four writer threads on the default bucket in the cluster at `10.5.2.54:11210`. The vBucket map for the bucket is grouped into multiple vBuckets, where one read worker accesses one of the vBuckets. In this example, there is one reader for each of the four vBuckets.

 ep_workload:LowPrioQ_AuxIO:InQsize:   5
 ep_workload:LowPrioQ_AuxIO:OutQsize:  0
 ep_workload:LowPrioQ_NonIO:InQsize:   55
 ep_workload:LowPrioQ_NonIO:OutQsize:  0
 ep_workload:LowPrioQ_Reader:InQsize:  20
 ep_workload:LowPrioQ_Reader:OutQsize: 0
 ep_workload:LowPrioQ_Writer:InQsize:  30
 ep_workload:LowPrioQ_Writer:OutQsize: 0
 ep_workload:num_auxio:                1
 ep_workload:num_nonio:                1
 ep_workload:num_readers:              4
 ep_workload:num_shards:               4
 ep_workload:num_sleepers:             10
 ep_workload:num_writers:              4
 ep_workload:ready_tasks:              0