---
title: Release Notes for Couchbase Server 8.0
description: Couchbase Server 8.0.0 introduces many fixes, as well as some
  deprecations and removals.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/release-notes/pages/relnotes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/release-notes/relnotes.html)

# Release Notes for Couchbase Server 8.0

## [](#new-features)New Features

These release notes are focused on bug fixes and breaking changes.

For information about new features and major improvements made in Couchbase Server 8.0, see [What’s New](../introduction/whats-new.md).

## [](#release-80)Release 8.0 (October 2025)

Couchbase Server 8.0 was released in October 2025\. This release contains fixes to issues.

## [](#dlist-fixed-issues-80)Fixed Issues

### [](#dlist-fixed-issues-80-cluster-manager)Cluster Manager

**[MB-30260](https://jira.issues.couchbase.com/browse/MB-30260/)**

Couchbase Server now supports locking/unlocking users.

This puts the user in a state where they are unable to authenticate against Couchbase, while being able to unlock them at a later time, allowing them to authenticate again.

**[MB-31823](https://jira.issues.couchbase.com/browse/MB-31823/)**

Couchbase Server now supports giving users a temporary password.

Giving the user a temporary password puts the user in a state where they must first change their password in the UI before they can perform any actions. This can be used to hand out user credentials, while ensuring that those credentials do not continue to be used, for security assurance.

**[MB-50939](https://jira.issues.couchbase.com/browse/MB-50939/)**

We have enhanced the security of node-to-node (N2N) communication. Previously, N2N traffic was authenticated using **basic authentication**. With this release, when **N2N encryption is enabled**, communication between nodes now uses **mutual TLS (mTLS)** instead of basic authentication.

**[MB-60349](https://jira.issues.couchbase.com/browse/MB-60349/)**

Now you can add or remove non-Data Services dynamically on existing nodes in a cluster, without adding or removing nodes. Rebalancing is automatically triggered to distribute service workloads and complete the modification. These are the services that can be modified:

* `index` (Index Service)
* `n1ql` (Query Service)
* `fts` (Search Service)
* `cbas` (Analytics Service)
* `eventing` (Eventing Service)
* `backup` (Backup Service) You can modify these services using the Couchbase UI, REST API and CLI.

**[MB-61457](https://jira.issues.couchbase.com/browse/MB-61457/)**

The following data service settings are now supported in the /pools/default/buckets REST api

* accessScannerEnabled (true | false)
* expiryPagerSleepTime (0 - maxInt, default 600)
* memoryLowWatermark (50-89, default 75)
* memoryHighWatermark (51-90, default 85)
* warmupBehavior (backround | blocking | none)

**[MB-63755](https://jira.issues.couchbase.com/browse/MB-63755/)**

The Cluster Manager now supports tracking a latest time of use for users.

Once enabled for certain users, this can be used to identify if they become inactive from the perspective of the Cluster Manager, i.e. seeing when they last used the UI. Please note that this does not cover other activity by users, so this should not be used to monitor activity of applications users.

**[MB-65779](https://jira.issues.couchbase.com/browse/MB-65779/)**

Cluster Manager

A new REST API has been introduced to facilitate the deletion of specific global memcached settings, enabling users to reset these settings to their memcached defaults. This change only impacts "extra" settings, which are not always passed to memcached.

Data Service

The Data-Service `external_auth_request_timeout` is now configurable, allowing users to set a value between 0 and the maximum 32-bit unsigned integer value. The default is set to 60 seconds, and the value can be passed in seconds.

**[MB-66615](https://jira.issues.couchbase.com/browse/MB-66615/)**

The bucket statistics REST API `GET /pools/default/buckets/[bucket-name]/stats` is deprecated and replaced with `GET /pools/default/stats/range/[metric_name]/[function-expression]`. Similarly, to retrieve statistics for multiple metrics, Couchbase supports the REST API `POST /pools/default/stats/range`. For retrieving the XDCR statistics details, instead of the REST API `GET /pools/default/buckets/[source_bucket]/stats/[destination_endpoint]`, Couchbase now supports the REST API `GET /pools/default/stats/range/[statistics_name]`.

**[MB-67106](https://jira.issues.couchbase.com/browse/MB-67106/)**

**Metric Rename – Cache Miss Ratio → Get Miss Ratio**The _Cache Miss Ratio_ metric name suggested it measured memory or disk caching performance. In reality, as of version 7.6.2, it was redefined to measure the proportion of read (`get`) operations that fail because the requested key is not present in the bucket at all. To eliminate this confusion, the metric has been renamed to **Get Miss Ratio**.

### [](#dlist-fixed-issues-80-data-service)Data Service

**[MB-9418](https://jira.issues.couchbase.com/browse/MB-9418/)**

Configurable Warmup Behavior (Background Warmup):

The new Warmup behaviour setting, configured using `warmupBehavior` in the REST API, controls when a persistent bucket becomes fully available for read and write operations after a bucket restart. This setting replaces multiple warmup threshold parameters with a single configuration point:

* **background** (default): The bucket becomes fully available as soon as required metadata is loaded from storage. The bucket’s cache is then filled in the background until memory usage reaches the low watermark (`memoryLowWatermark`).
* **blocking**: This is the original behaviour. The bucket becomes read-available as soon as required metadata is loaded from storage, then continues filling the cache until memory usage reaches the low watermark (`memoryLowWatermark`). The bucket becomes fully available only after this point.
* **none**: Disables warmup. The bucket becomes fully available as soon as required metadata is loaded from storage. The cache remains empty.

_API Changes:_ the REST API now includes the per-bucket setting `warmupBehavior`. The previous advanced tuning settings `warmup_min_items_threshold` and `warmup_min_memory_threshold` have been removed from the `cbepctl` interface.

**[MB-60542](https://jira.issues.couchbase.com/browse/MB-60542/)**

The metric `kv_vb_ht_memory_bytes` is deprecated as it measured the overhead per-hashtable vs the total memory used by the hashtable. The metric is replaced with `kv_vb_ht_memory_overhead`, which reflects what is being measured.

In this release, both the metrics will exist, but `kv_vb_ht_memory_bytes` will eventually be removed.

Any system using `kv_vb_ht_memory_bytes` should migrate to using `kv_vb_ht_memory_overhead`.

**[MB-61385](https://jira.issues.couchbase.com/browse/MB-61385/)**

SET and DELETE with Meta operations could distort the vbucket max\_cas if a faulty CAS value is provided in the operation, setting the vbuckets max\_cas to an unusually high or inconsistent value. Inadvertently affecting the Hybrid Logical Clock (HLC) and Last Write Wins (LLW) conflict resolution via XDCR. In certain cases, this resulted in legitimate mutations being skipped or ignored during replication. For this reason, the system now fails front-end operations with a CAS value that exceeds the `hlc_max_future_threshold`, default value of 65 minutes, to prevent a vbucket’s max\_cas from getting distorted.

**[MB-62295](https://jira.issues.couchbase.com/browse/MB-62295/)**

Previously audit would log to a _file_ named audit.log and as part of rotation the file was _renamed_ to a different name. In this release, this is replaced by `audit.log` being a symbolic link to the file currently being written to.

**[MB-62647](https://jira.issues.couchbase.com/browse/MB-62647/)**

`kv_ep_mem_low_wat_percent_ratio` and `kv_ep_mem_high_wat_percent_ratio` used to report values 0 - 0.01, instead of 0 - 1.

The values are correctly remapped to be in the 0–1 range.

**[MB-62678](https://jira.issues.couchbase.com/browse/MB-62678/)**

Resolved an issue where TTL-driven deletions via `VBucket::deleteItem` could generate invalid tombstones containing a document body. This issue occurred when TTL was triggered during the second phase of a 2-phase delete operation. The fix ensures that when TTL triggers at CMD\_DEL, the document body is correctly removed and a valid tombstone is generated.

**[MB-62969](https://jira.issues.couchbase.com/browse/MB-62969/)**

The support for the following Data Service settings are removed from `cbepctl`:

* `access_scanner_enabled`
* `exp_pager_stime`
* `warmup_min_items_threshold`
* `warmup_min_memory_threshold`
* `secondary_warmup_min_items_threshold`
* `secondary_warmup_min_memory_threshold`The settings are now supported via the ns\_server REST API `` /pools/default/buckets`as `accessScannerEnabled ``, `expiryPagerSleepTime`, `warmupBehavior`, `memoryLowWatermark`, and `memoryHighWatermark`.

**[MB-63827](https://jira.issues.couchbase.com/browse/MB-63827/)**

| Version      | Description                                                                                                                                                                                         | Resolution                                                                |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 7.2.7        | DCP connection metrics for connection names not conforming to server format are not exposed to Prometheus.                                                                                          | The metrics are aggregated and exposed with connection\_type="\_unknown". |
| 7.6.6, 8.0.0 | DCP connection metrics for connection names not conforming to server format are not aggregated by connection type when exposing to Prometheus, potentially producing a large number of time series. | The metrics are aggregated and exposed with connection\_type="\_unknown". |

**[MB-63938](https://jira.issues.couchbase.com/browse/MB-63938/)**

It is no longer possible to run commands such as `mcstat [options] statgroup1 statgroup2` to fetch multiple stat groups. In 8.0 this no longer supported to make it easier to pass arguments to the various stat groups.

Pre 8.0 a user would need to add quotes (or escape the whitespace) between the stat group like:

`$ mcstat [options] "vbucket-details 1"`

In 8.0 this may be written as

`mcstat [options] vbucket-details 1`

**[MB-65779](https://jira.issues.couchbase.com/browse/MB-65779/)**

Cluster Manager

A new REST API has been introduced to facilitate the deletion of specific global memcached settings, enabling users to reset these settings to their memcached defaults. This change only impacts "extra" settings, which are not always passed to memcached.

Data Service

The Data-Service `external_auth_request_timeout` is now configurable, allowing users to set a value between 0 and the maximum 32-bit unsigned integer value. The default is set to 60 seconds, and the value can be passed in seconds.

**[MB-67106](https://jira.issues.couchbase.com/browse/MB-67106/)**

**Metric Rename – Cache Miss Ratio → Get Miss Ratio**The _Cache Miss Ratio_ metric name suggested it measured memory or disk caching performance. In reality, as of version 7.6.2, it was redefined to measure the proportion of read (`get`) operations that fail because the requested key is not present in the bucket at all. To eliminate this confusion, the metric has been renamed to **Get Miss Ratio**.

### [](#dlist-fixed-issues-80-views)Views

**[MB-30260](https://jira.issues.couchbase.com/browse/MB-30260/)**

Couchbase Server now supports locking/unlocking users.

This puts the user in a state where they are unable to authenticate against Couchbase, while being able to unlock them at a later time, allowing them to authenticate again.

**[MB-31823](https://jira.issues.couchbase.com/browse/MB-31823/)**

Couchbase Server now supports giving users a temporary password.

Giving the user a temporary password puts the user in a state where they must first change their password in the UI before they can perform any actions. This can be used to hand out user credentials, while ensuring that those credentials do not continue to be used, for security assurance.

**[MB-62639](https://jira.issues.couchbase.com/browse/MB-62639/)**

Couchbase Server now allows users to specify the network type when adding a self-managed target.

**[MB-67213](https://jira.issues.couchbase.com/browse/MB-67213/)**

**Metric Rename – Cache Miss Ratio → Get Miss Ratio**The _Cache Miss Ratio_ metric name suggested it measured memory or disk caching performance. In reality, as of version 7.6.2, it was redefined to measure the proportion of read (`get`) operations that fail because the requested key is not present in the bucket at all. To eliminate this confusion, the metric has been renamed to **Get Miss Ratio**.

**[MB-67280](https://jira.issues.couchbase.com/browse/MB-67280/)**

**Change to Bucket Priority Settings**

As part of improving background task scheduling, we have replaced the legacy implementation with a standardized, more advanced scheduler. As a result, setting a bucket’s priority to high or low no longer affects system behavior. Consequently, the option to set bucket priority has been removed from the UI.

Previously, task scheduling relied on a basic two-priority queue (high and low), which had limitations—such as busy polling. The new scheduling mechanism (introduced in MB-36956) eliminates these issues.

> [!NOTE]
> Bucket priority settings are still available via the REST API and CLI to maintain compatibility with existing customer scripts and tooling.

### [](#dlist-fixed-issues-80-xdcr)XDCR

**[MB-11575](https://jira.issues.couchbase.com/browse/MB-11575/)**

XDCR now supports the identification of Incoming Replications on a cluster. The Incoming Replications can be viewed on the XDCR tab of the UI or retrieved by using the REST API

**[MB-58989](https://jira.issues.couchbase.com/browse/MB-58989/)**

In this release, XDCR introduces the new Conflict Logging feature. It detects and logs concurrent conflicts that occur in different clusters but on the same document version due to independent modifications by locally connected applications during Active-Active replication.

**[MB-62507](https://jira.issues.couchbase.com/browse/MB-62507/)**

Before this fix, various loggers all share the same logging level. Setting the logger to Debug, for example, would cause all components to print debug messages that clogs the log files. This fix now introduces the ability to set more granular levels of logging for each component as needed.

**[MB-62564](https://jira.issues.couchbase.com/browse/MB-62564/)**

This release introduces bundling with `xdcrDiffer`, which is a diagnostic utility. This utility verifies data consistency between XDCR clusters. It identifies missing or mismatched documents by comparing metadata and content hashes across source and target clusters.

**[MB-66140](https://jira.issues.couchbase.com/browse/MB-66140/)**

In some scenarios, due to race conditions, changing the filter expression or explicit/migration mapping may cause the replication to fail streaming from the beginning. As a consequence, some Source bucket documents may get missed from being replicated to the Target bucket. This has been fixed in 8.0\. It is advised to avoid changing these three replication settings:

* filterExpression
* collectionsExplicitMapping
* collectionsMigrationMode

until all nodes in the cluster have been upgraded.

### [](#dlist-fixed-issues-80-query-service)Query Service

**[MB-62793](https://jira.issues.couchbase.com/browse/MB-62793/)**

The original limit of one XATTR per KV op was relaxed to a maximum of 16 in KV server version 7.6; this ticket explores extending that relaxation to queries.

With this change, users can:

1. Use up to 15 XATTR fields in their query.
2. CREATE INDEX no longer imposes a limit on the number of XATTR fields that can be indexed.

**[MB-63459](https://jira.issues.couchbase.com/browse/MB-63459/)**

New to this release is the ability to manipulate document extended attributes (xattrs) via common SQL++ statements.

INSERT and UPSERT statement OPTIONS may now include an “xattrs” object element detailing additions and changes to the xattrs (omissions do not delete xattrs). The UPDATE statement now supports SET and UNSET of meta().xattrs.{attribute} elements.

**[MB-66703](https://jira.issues.couchbase.com/browse/MB-66703/)**

Added a plan version to prepared statements and logic to trigger reprepare when outdated plans are detected. This avoids duplicate OFFSET execution in mixedmode clusters due to changes in ORDER BY and LIMIT/OFFSET handling.

**[MB-67849](https://jira.issues.couchbase.com/browse/MB-67849/)**

The recent builds of Couchbase Server versions 7.2.7 through 8.1.0 and Enterprise Analytics 2.1.0 include updates from the go\_json library to address int64 overflow issues reported under MB-67849\. The updates involve implementing proper checks for int64 overflow to properly represent large numbers (greater than 263 or less than -263).

### [](#dlist-fixed-issues-80-index-service)Index Service

**[MB-64982](https://jira.issues.couchbase.com/browse/MB-64982/)**

When shard affinity is enabled, the indexer internally maps all replicas of an index to an alternateID. If such an alternateID exists on a node outside the list of nodes, instead of preventing replica creation, the system creates a new replica with the same alternateID on different nodes. This leads to rebalance failures on the affected nodes.

### [](#dlist-fixed-issues-80-search-service)Search Service

**[MB-64766](https://jira.issues.couchbase.com/browse/MB-64766/)**

Introduced a new `decoded_sort` field in query responses. This provides human-readable sort values by decoding geo distances (in meters) and numeric fields, while returning strings as-is. This is only done when the `type` field is specified in the sort definition of the query.

### [](#dlist-fixed-issues-80-tools)Tools

**[MB-44863](https://jira.issues.couchbase.com/browse/MB-44863/)**

When using the Backup Service, you can now configure a retention period for a repository, automating the deletion of old backups if desired. You can choose a default retention period for a repository, and you can choose to override this default for particular individual backups if desired.

**[MB-60337](https://jira.issues.couchbase.com/browse/MB-60337/)**

Previously, it was possible to remove backups which would cause dependent incremental backups to become invalid if they depended on those deleted backups. With this release, such deletes are prevented by default, but can be overridden with the new `--disable-safe-remove-check` flag.

**[MB-62564](https://jira.issues.couchbase.com/browse/MB-62564/)**

This release introduces bundling with `xdcrDiffer`, which is a diagnostic utility. This utility verifies data consistency between XDCR clusters. It identifies missing or mismatched documents by comparing metadata and content hashes across source and target clusters.

**[MB-62655](https://jira.issues.couchbase.com/browse/MB-62655/)**

The new Query AWR (Automatic Workload Repository) Report Generator tool allows customers to generate reports on query performance statistics. This tool requires AWR to be enabled on the cluster.

**[MB-63389](https://jira.issues.couchbase.com/browse/MB-63389/)**

**Memcached bucket removal** – Memcached buckets, deprecated in 6.5.1, have been fully removed in 8.0.0\. Cluster upgrades from earlier versions will fail if Memcached buckets are present. Remove all Memcached buckets before upgrading.

**[MB-66173](https://jira.issues.couchbase.com/browse/MB-66173/)**

Automated the process of resolving name conflicts between collections or scopes in the backup and those in the target cluster, during a restore. For this purpose, we have added a new flag, `--auto-resolve-conflicts` to the `cbbackupmgr restore` parameter.

## [](#breaking-changes-80)Breaking changes 8.0 (October 2025)

Couchbase Server 8.0 was released in October 2025\. This release contains the following breaking changes:

### [](#cluster-manager)Cluster Manager

**[MB-47905](https://jira.issues.couchbase.com/browse/MB-47905/)**

We have introduced the ability to support both client certificate authentication and n2n encryption at the same time.

However, the client certificate will not work with the old OOTB CA certificates due to the extended attribute.

Therefore, you will need to regenerate your OOTB CA certificates (if the CA certificate is the one from before `7.6` or if they have the attribute above) before this feature is enabled.

**[MB-62777](https://jira.issues.couchbase.com/browse/MB-62777/)**

**Magma with 128 vBuckets Now Default Storage Engine**

Starting with Couchbase Server Enterprise `8.0`, new buckets default to the Magma storage engine configured with 128 vBuckets, replacing Couchstore as the default.

This change reduces the minimum memory quota from 1 GiB (required by Magma with 1024 vBuckets) to 100 MiB per node—matching Couchstore, while retaining Magma’s performance and efficiency benefits.

For more details, see the [What’s New](../introduction/whats-new.md#whats-new-magma-vbuckets) page.

### [](#data-service)Data Service

**[MB-9418](https://jira.issues.couchbase.com/browse/MB-9418/)**

Configurable Warmup Behavior (Background Warmup): The new `warmup_behavior` setting, configured using `warmupBehavior` in the REST API, controls when a persistent bucket becomes fully available for read and write operations after a bucket restart. This setting replaces multiple warmup threshold parameters with a single configuration point:

* **background** (default): The bucket becomes fully available as soon as required metadata is loaded from storage. The bucket’s cache is then filled in the background until memory usage reaches the low watermark (`memoryLowWatermark`).
* **blocking**: This is the original behaviour. The bucket becomes read-available as soon as required metadata is loaded from storage, then continues filling the cache until memory usage reaches the low watermark (`memoryLowWatermark`). The bucket becomes fully available only after this point.
* **none**: Disables warmup. The bucket becomes fully available as soon as required metadata is loaded from storage. The cache remains empty.

API Changes: The REST API now includes the per-bucket setting `warmupBehavior`. The previous advanced tuning settings `warmup_min_items_threshold` and `warmup_min_memory_threshold` have been removed from the `cbepctl` interface.

**[MB-63938](https://jira.issues.couchbase.com/browse/MB-63938/)**

It is no longer possible to run commands such as `mcstat [options] statgroup1 statgroup2` to fetch multiple stat groups. In 8.0 this no longer supported to make it easier to pass arguments to the various stat groups.

Pre 8.0 a user would need to add quotes (or escape the whitespace) between the stat group like:

`$ mcstat [options] "vbucket-details 1"`

In 8.0 this may be written as

`mcstat [options] vbucket-details 1`

**[MB-63946](https://jira.issues.couchbase.com/browse/MB-63946/)**

When using `mcstat` it is no longer possible to use `--json=pretty`.

The request to pretty-print the JSON is ignored

Users can use a pipe in conjunction with an external formatting tool such as jq to obtain formatted output:

`mcstat [options] --json [statgroup] | jq .`

### [](#views)Views

**[MB-63212](https://jira.issues.couchbase.com/browse/MB-63212/)**

Couchbase Server 8.0 has removed support for Memcached buckets. They were deprecated in version 6.5.1.

Before upgrading to Couchbase Server 8.0, you must remove any Memcached buckets from your cluster. You can replace them with ephemeral buckets which are similar to Memcached buckets but support features such as rebalance, backup, query, and eventing. See [Bucket capabilities](https://docs-archive.couchbase.com/server/6.6/learn/buckets-memory-and-storage/buckets.html#bucket-capabilities) for a summary of the differences between Memcached and ephemeral buckets.

If you do not remove your Memcached buckets, the upgrade process reports an error message telling you to remove the Memcached buckets before proceeding.

**[MB-67280](https://jira.issues.couchbase.com/browse/MB-67280/)**

**Change to Bucket Priority Settings**

As part of improving background task scheduling, we have replaced the legacy implementation with a standardized, more advanced scheduler. As a result, setting a bucket’s priority to high or low no longer affects system behavior. Consequently, the option to set bucket priority has been removed from the UI.

Previously, task scheduling relied on a basic two-priority queue (high and low), which had limitations—such as busy polling. The new scheduling mechanism (introduced in MB-36956) eliminates these issues.

> [!NOTE]
> Bucket priority settings are still available via the REST API and CLI to maintain compatibility with existing customer scripts and tooling.

### [](#index-service)Index Service

**[MB-63192](https://jira.issues.couchbase.com/browse/MB-63192/)**

The latest updates introduce a new shard assignment algorithm, impacting both vector and non-vector indexes by offering more aggressive sharing of plasma shards in version 8.0 compared to 7.6\. This adjustment might affect performance when comparing upgrades from earlier versions like 7.2 to 8.0 or 7.6 to 8.0\. Shard assignment logic should be functionally tested in these scenarios. The algorithm is behind a feature flag and can be toggled off to revert to older behaviors if needed. For Capella upgrades, it’s possible all shards might already exist, potentially requiring additional shards for vector indexes depending on resource availability. On-prem clusters keep file-based rebalance off by default. Performance testing, as noted in ongoing evaluations, indicates a 7% regression during initial index builds at CPU saturation, but no impact on incremental builds. The benefits include improved memory control, suggesting the changes are acceptable at this stage.

### [](#tools)Tools

**[MB-60337](https://jira.issues.couchbase.com/browse/MB-60337/)**

Previously, it was possible to remove backups which would cause dependent incremental backups to become invalid if they depended on those deleted backups. With this release, such deletes are prevented by default, but can be overridden with the new `--disable-safe-remove-check` flag.

**[MB-63389](https://jira.issues.couchbase.com/browse/MB-63389/)**

**Memcached bucket removal** – Memcached buckets, deprecated in 6.5.1, have been fully removed in 8.0.0\. Cluster upgrades from earlier versions will fail if Memcached buckets are present. Remove all Memcached buckets before upgrading.

## [](#known-issues-800)Known Issues 8.0.0 (October 2025)

For Couchbase Server 8.0.0 was released in October 2025, these are the known issues that aren’t yet resolved.

### [](#dlist-known-issues-800-index-service)Index Service

**[MB-68626](https://jira.issues.couchbase.com/browse/MB-68626/)**

**Vector Index Batch Build Memory Consumption**

When building multiple vector indexes in a batch, the system fetches random sample vectors from KV for all indexes simultaneously, even though only one index is trained at a time. If the indexer is not properly sized for build batch size, this can cause excessive memory consumption, leading to Out of Memory (OOM) kills.

**Root Cause:** Indexer fetches and evaluates vectors for all indexes in the batch concurrently without throttling, creating significant memory overhead.

**Symptoms:**

* OOM kills during vector index build operations
* High memory usage (HeapInUse approaching memory quota)
* Fatal error: `runtime: out of memory`
* Memory allocation failures during vector sampling

**Workaround:** Properly size the indexer for random sample vectors and configure the index build batch size to limit the number of indexes built together by taking into account the available memory quota and vector sizes

## [](#documentation-for-earlier-versions)Documentation for Earlier Versions

Documentation for earlier versions of Couchbase software can be found in the [Documentation Archive](https://docs-archive.couchbase.com/home/index.html).