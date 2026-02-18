---
title: Monitor Clock Drift
description: The progressive desynchronization of nodes can be monitored.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/monitor/xdcr-monitor-timestamp-conflict-resolution.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/manage/monitor/xdcr-monitor-timestamp-conflict-resolution.html)

# Monitor Clock Drift

The progressive desynchronization of nodes can be monitored.

## [](#understanding-clock-drift)Understanding Clock Drift

In a production environment, the clock of each individual node within a Couchbase-Server cluster should be synchronized with a reference clock, provided by an NTP server. This is described in [Clock Sync with NTP](../../install/synchronize-clocks-using-ntp.md). Over time, progressive _desynchronization_ may occur: this is referred to as [Clock Drift](https://en.wikipedia.org/wiki/Clock%5Fdrift), or more simply, _drift_.

During [Intra-Cluster Replication](../../learn/clusters-and-availability/replication-architecture.md), each replica vBucket calculates drift; when it receives updates from the corresponding active vBucket, located on a separate node.

During [XDCR](../../learn/clusters-and-availability/xdcr-overview.md), each active vBucket on the target cluster calculates drift; when it receives updates from its corresponding active vBucket, located on the source cluster. If drift is greater than 5 seconds (5000 milliseconds), an alert is raised on the destination cluster; with the following message: "`[<DATE>] - Remote or replica mutation received for bucket "<BUCKET>" on node "<IP>" with timestamp more than 5000 milliseconds ahead of local clock. Please ensure that NTP is set up correctly on all nodes across the replication topology and clocks are synchronized.`"

Drift can be monitored by means of the [cbstats](#cli:cbstats/cbstats-intro.adoc) tool, using the `vbucket-details` and `all` commands; as described below.

### [](#cbstats-vbucket-details)[cbstats vbucket-details](../../cli/cbstats/cbstats-vbucket-details.md)

The following drift-related statistics are provided:

* `max_cas`. The vBucket’s current maximum hybrid logical clock timestamp. In general, this statistic shows the value issued to the last mutation or in certain cases the largest timestamp the vBucket has received (when the received timestamp is ahead of the local clock).
* `max_cas_str`. This is `max_cas`, displayed as a human-readable ISO-8601 timestamp (UTC).
* `total_abs_drift`. "Total Absolute Drift" is the accumulated drift observed by the vBucket. Drift is always accumulated as an absolute value.
* `total_abs_drift_count` . The number of updates applied to `total_abs_drift`, for the purpose of average or rate calculations.
* `drift_ahead_threshold`. The threshold at which positive drift triggers an update to `drift_ahead_exceeded`. The value is displayed in nanoseconds.
* `drift_behind_threshold`. The threshold at which positive drift triggers an update to `drift_behind_exceeded`. The value is displayed in nanoseconds as a positive value, but is converted to a negative value for actual exception checks.
* `drift_ahead_threshold_exceeded`. How many mutations have been observed with a drift above the `drift_ahead_threshold`.
* `drift_behind_threshold_exceeded`. How many mutations have been observed with a drift below the `drift_behind_threshold`.
* `logical_clock_ticks`. How many times the hybrid logical clock has had to increment the logical clock.

### [](#cbstats-all)[cbstats all](../../cli/cbstats/cbstats-all.md)

The following drift-related statistics are provided:

* `ep_active_hlc_drift`. The sum of `total_abs_drift` for the node’s active vBuckets.
* `ep_active_hlc_drift_count`. The sum of `total_abs_drift_count` for the node’s active vBuckets.
* `ep_replica_hlc_drift`. The sum of `total_abs_drift` for the node’s active vBuckets.
* `ep_replica_hlc_drift_count`. The sum of `total_abs_drift_count` for the node’s active vBuckets.
* `ep_active_ahead_exceptions`. The sum of `drift_ahead_exceeded` for the node’s active vBuckets.
* `ep_active_behind_exceptions`. The sum of `drift_behind_exceeded` for the node’s active vBuckets.
* `ep_replica_ahead_exceptions`. The sum of `drift_ahead_exceeded` for the node’s replica vBuckets.
* `ep_replica_behind_exceptions`. The sum of `drift_behind_exceeded` for the node’s replica vBuckets.