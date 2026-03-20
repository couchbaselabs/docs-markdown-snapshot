---
title: Release Notes for Couchbase Kubernetes Operator 2.9
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:operator::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/release-notes.html)

# Release Notes for Couchbase Kubernetes Operator 2.9

This page summarizes the fixes and known issues in Couchbase Kubernetes Operator 2.9, and links to the associated issues.

## [](#new-features)New Features

For information about new features and major improvements made in Couchbase Kubernetes Operator 2.9, see [What’s New](whats-new.md).

## [](#release-290)Release 2.9 (December 2025)

Couchbase Kubernetes Operator 2.9 was released in December 2025\. This release contains fixes to issues and known issues.

### [](#fixed-issues-v290)Fixed Issues in 2.9

For Couchbase Kubernetes Operator 2.9 released in December 2025, these are the fixed issues.

**[K8S-1537](https://jira.issues.couchbase.com/browse/K8S-1537/)**

The cluster UUID is no longer required when creating remote cluster connections.

**[K8S-2829](https://jira.issues.couchbase.com/browse/K8S-2829/)**

You can now specify the `cao.couchbase.com/additionalArgs` annotation on CouchbaseBackup and CouchbaseRestore resources to pass additional `cbbackupmgr` arguments to the container.

**[K8S-3016](https://jira.issues.couchbase.com/browse/K8S-3016/)**

You can now specify the Couchbase Server password policy using the CouchbaseCluster resource.

**[K8S-3121](https://jira.issues.couchbase.com/browse/K8S-3121/)**

You can now specify to preserve the CouchbaseBackupRestore resource after the restore completes.

**[K8S-3153](https://jira.issues.couchbase.com/browse/K8S-3153/)**

New TCP tunables (`tcpKeepAliveIdle`, `tcpKeepAliveInterval`, `tcpKeepAliveProbes`, `tcpUserTimeout`) are now available through the CouchbaseCluster resource when using Couchbase Server 8.0.

**[K8S-3258](https://jira.issues.couchbase.com/browse/K8S-3258/)**

Added the `logging.configNameReleasePrefix` boolean to the Helm chart. The default value is `false`. When set to `true`, the Operator prefixes the Fluent Bit configuration with the release name.

Couchbase recommends enabling this setting only on new clusters because enabling it on existing clusters triggers recreation of all pods.

**[K8S-3371](https://jira.issues.couchbase.com/browse/K8S-3371/)**

You can now specify environment variables for the CouchbaseBackup and CouchbaseBackupRestore pods to allow `cbbackupmgr` tuning.

**[K8S-3434](https://jira.issues.couchbase.com/browse/K8S-3434/)**

`spec.monitoring` is deprecated and no longer attaches an exporter sidecar to the Couchbase Server pod.

**[K8S-3535](https://jira.issues.couchbase.com/browse/K8S-3535/)**

If `couchbasecluster.spec.buckets.managed` is set to `false`, restoring from backup automatically creates buckets.

**[K8S-3616](https://jira.issues.couchbase.com/browse/K8S-3616/)**

New REST API bucket settings for the Data Service are now available in Couchbase Server 8.0.

**[K8S-3638](https://jira.issues.couchbase.com/browse/K8S-3638/)**

You can now specify a merge schedule on the CouchbaseBackup resource.

**[K8S-3646](https://jira.issues.couchbase.com/browse/K8S-3646/)**

You can now set the Query Service `CompletedStreamSize` using the CouchbaseCluster resource.

**[K8S-3650](https://jira.issues.couchbase.com/browse/K8S-3650/)**

When using Couchbase Server 8.0, you can no longer create Memcached buckets.

**[K8S-3715](https://jira.issues.couchbase.com/browse/K8S-3715/)**

Added RBAC roles for users to match new roles added in Couchbase Server 8.0.

**[K8S-3786](https://jira.issues.couchbase.com/browse/K8S-3786/)**

You can now specify `default` and `disk_io_optimized` for the Data Service reader threads.

**[K8S-3917](https://jira.issues.couchbase.com/browse/K8S-3917/)**

You can now set `overheadMemory` for `autoResourceAllocation` to specify a static overhead amount.

**[K8S-3951](https://jira.issues.couchbase.com/browse/K8S-3951/)**

`cao.couchbase.com/autoCompaction.magmaFragmentationPercentage` has been replaced by a field in the CouchbaseCluster CRD.

**[K8S-4013](https://jira.issues.couchbase.com/browse/K8S-4013/)**

You can now disable DNS resolution verification when creating pods before activating them in the cluster.

**[K8S-4016](https://jira.issues.couchbase.com/browse/K8S-4016/)**

Fixed a bug that caused a panic when a member pod became unresponsive.

**[K8S-4028](https://jira.issues.couchbase.com/browse/K8S-4028/)**

Added an upgrade stanza to the CouchbaseCluster resource to give users more control over upgrades.

**[K8S-4091](https://jira.issues.couchbase.com/browse/K8S-4091/)**

Updated `spec.networking.addressFamily` to accept `IPv4Only`, `IPv4Priority`, `IPv6Only`, and `IPv6Priority`. The existing `IPv4` and `IPv6` values retain the `IPv4Only` and `IPv6Only` behavior, so no change is required for existing configurations.

These values are deprecated and will be removed in a future release.

The priority or only option determines whether `addressFamilyOnly` is set to `true` or `false`.

**[K8S-4097](https://jira.issues.couchbase.com/browse/K8S-4097/)**

The MirWatchdog is an out-of-band check that provides additional alerting. It is used when the Operator cannot reconcile a cluster due to reasons outside its control and requires manual user intervention. Scenarios include, but are not limited to, TLS expiration, Couchbase authentication errors, and loss of quorum. This feature is disabled by default but can be enabled and configured by using the `mirWatchdog` field in the CouchbaseCluster CRD. If the cluster enters this condition, it will:

1. Set the `cluster_manual_intervention` gauge metric to `1`.
2. Add the `ManualInterventionRequired` condition to the cluster, where possible, with a message describing the reason for entering the MIR state.
3. Raise a `ManualInterventionRequired` Kubernetes event, with the message describing the reason for entering manual intervention.
4. Optionally, skips reconciliation until the manual intervention required state is resolved, that is, until the issue that caused the condition is fixed.

**[K8S-4101](https://jira.issues.couchbase.com/browse/K8S-4101/)**

Added support for the Encryption at Rest feature of Couchbase Server 8.0.

**[K8S-4108](https://jira.issues.couchbase.com/browse/K8S-4108/)**

The CouchbaseUser resource now includes an `enabled` flag to allow administrators to enable or disable user accounts.

**[K8S-4109](https://jira.issues.couchbase.com/browse/K8S-4109/)**

The CouchbaseUser resource now allows the administrators to enforce password change on a user’s first login using the `couchbaseuser.spec.userPassword.requireInitialChange` field.

**[K8S-4111](https://jira.issues.couchbase.com/browse/K8S-4111/)**

CouchbaseBucket resources now support `durabilityImpossibleFallback` with values `disabled` and `fallbackToActiveAck`.

**[K8S-4112](https://jira.issues.couchbase.com/browse/K8S-4112/)**

Added multiple settings to CouchbaseBucket resources to configure XDCR Conflict Logging.

**[K8S-4114](https://jira.issues.couchbase.com/browse/K8S-4114/)**

Added a CouchbaseCluster resource setting that enables auto‑failover of Ephemeral Buckets with no replicas in Couchbase Server 8.0 and later versions.

**[K8S-4117](https://jira.issues.couchbase.com/browse/K8S-4117/)**

Added `data.diskUsageLimit` to the CouchbaseCluster resource to enable Disk Usage Guardrails.

**[K8S-4118](https://jira.issues.couchbase.com/browse/K8S-4118/)**

Added support for SDK Telemetry settings in Couchbase Server 8.0 and later versions.

**[K8S-4120](https://jira.issues.couchbase.com/browse/K8S-4120/)**

For CouchbaseBuckets, now the default storage engine is `magma` and the vBucketCount is `128`.

**[K8S-4144](https://jira.issues.couchbase.com/browse/K8S-4144/)**

In the earlier versions of Couchbase Kubernetes Operator, the metrics port annotation `prometheus.io/port` was set to `8091`, even when TLS was enabled. It now correctly sets to `18091`.

**[K8S-4158](https://jira.issues.couchbase.com/browse/K8S-4158/)**

EvictionPolicy changes can now be applied to an online bucket during a swap rebalance.

**[K8S-4161](https://jira.issues.couchbase.com/browse/K8S-4161/)**

Operator 2.9.0 allows you to set `spec.cluster.analytics.numReplicas`. This feature is supported only on Couchbase Server 7.6 and later versions.

**[K8S-4203](https://jira.issues.couchbase.com/browse/K8S-4203/)**

Fixed an issue where metrics scrapes became too large when the Operator managed many clusters.

**[K8S-4209](https://jira.issues.couchbase.com/browse/K8S-4209/)**

Full backups can now be resumed.

**[K8S-4273](https://jira.issues.couchbase.com/browse/K8S-4273/)**

Fixed an issue where the Operator failed to remove pods from the cluster.

**[K8S-4279](https://jira.issues.couchbase.com/browse/K8S-4279/)**

Fixed an issue where log message tags were inconsistent.

**[K8S-4404](https://jira.issues.couchbase.com/browse/K8S-4404/)**

Fixed an issue that caused upgrades to fail when image definitions used SHA256 digests.

### [](#known-issues-29)Known Issues in 2.9

For Couchbase Kubernetes Operator 2.9 released in December 2025, these are the known issues that aren’t yet resolved.

**[K8S-3839](https://jira.issues.couchbase.com/browse/K8S-3839/)**

Removing a server group from a cluster that uses InPlaceUpgrades can cause the Operator to fail to reconcile the cluster.

**[K8S-4349](https://jira.issues.couchbase.com/browse/K8S-4349/)**

The CouchbaseCluster CRD now exceeds the size limit for client-side apply. Use the `--server-side` option with `kubectl apply` to apply the resource.

**[K8S-4433](https://jira.issues.couchbase.com/browse/K8S-4433/)**

When running in mixed mode and before the upgrade to 8.0 completes, creating a Memcached bucket can cause the Operator to fail reconciliation.

**[K8S-4436](https://jira.issues.couchbase.com/browse/K8S-4436/)**

Upgrading the Couchbase Kubernetes Operator while the cluster is not fully upgraded causes the Operator to complete the cluster upgrade immediately.

**[K8S-4445](https://jira.issues.couchbase.com/browse/K8S-4445/)**

The CouchbaseRestore resource status may fail to update from Couchbase Backup containers. This does not prevent the restore from occurring.

**[K8S-4448](https://jira.issues.couchbase.com/browse/K8S-4448/)**

Changing the server groups applied to a server class while the Operator is recovering a pod can block reconciliation.

**[K8S-4456](https://jira.issues.couchbase.com/browse/K8S-4456/)**

Operator must be paused when using `cao create pod`. Otherwise, the Operator identifies the pod as foreign and removes it.

**[K8S-4469](https://jira.issues.couchbase.com/browse/K8S-4469/)**

Editing a Couchbase bucket storage backend while enabling or disabling `BucketMigrationRoutines` on a CouchbaseCluster can trigger a race condition that leads to an unreconcilable state.

**[K8S-4471](https://jira.issues.couchbase.com/browse/K8S-4471/)**

When `spec.networking.addressFamily` is set to `IPv6Priority` or `IPv6Only`, the Operator creates the cluster Service as IPv4 SingleStack, which causes pod launch failures. Patching the Service to `PreferDualStack` (IPv4, IPv6) allows the cluster to be created.

**[K8S-4474](https://jira.issues.couchbase.com/browse/K8S-4474/)**

Attempting to change bucket settings during a storage backend migration causes the Operator to fail to reconcile the cluster.

**[K8S-4477](https://jira.issues.couchbase.com/browse/K8S-4477/)**

The admission controller allows you to set the `collectionHistoryDefault` value on Couchstore buckets. This setting has no effect on Couchstore buckets.

**[K8S-4482](https://jira.issues.couchbase.com/browse/K8S-4482/)**

Attempting to change the `evictionPolicy` setting during a storage backend migration while `OnlineEvictionPolicyChange` is `true` can lead to an unreconcilable state.

**[K8S-4485](https://jira.issues.couchbase.com/browse/K8S-4485/)**

Manually editing a bucket’s storage backend with BucketMigrationRoutines disabled can prevent the Operator from reconciling the cluster.

**[K8S-4486](https://jira.issues.couchbase.com/browse/K8S-4486/)**

You can start a Couchbase Server upgrade while a Bucket Storage Backend Migration is in progress. This can result in an unreconcilable state.

**[K8S-4487](https://jira.issues.couchbase.com/browse/K8S-4487/)**

Manual Intervention Watchdog does not clear the rebalancing condition when entering the Manual Intervention Required condition.

**[K8S-4488](https://jira.issues.couchbase.com/browse/K8S-4488/)**

Reconciliation can begin before the Manual Intervention Watchdog is fully disabled.

**[K8S-4490](https://jira.issues.couchbase.com/browse/K8S-4490/)**

During stabilization, the Operator reconciles some, but not all CouchbaseCluster settings.

**[K8S-4496](https://jira.issues.couchbase.com/browse/K8S-4496/)**

It is possible to set replicas lower than the minimum required for a CouchbaseCluster when using an Ephemeral bucket.

**[K8S-4497](https://jira.issues.couchbase.com/browse/K8S-4497/)**

The dynamic admission controller treats the default bucket storage backend as Couchstore, even on 8.0 clusters.

**[K8S-4498](https://jira.issues.couchbase.com/browse/K8S-4498/)**

The order of password policy updates and user password changes can affect whether the Operator can make these changes successfully.

**[K8S-4499](https://jira.issues.couchbase.com/browse/K8S-4499/)**

It’s possible to rotate admin credentials to a password that does not meet the cluster password policy, which can prevent the Operator from reconciling the cluster.

**[K8S-4504](https://jira.issues.couchbase.com/browse/K8S-4504/)**

Setting reader and writer threads to `balanced` during an upgrade from Couchbase Server 7.6 to 8.0 can cause memcached to crash. Removing the reader and writer thread settings from the CRD resolves the issue.

**[K8S-4507](https://jira.issues.couchbase.com/browse/K8S-4507/)**

Enabling shard affinity in mixed mode, before the cluster fully supports the setting, can cause the Operator to fail reconciliation.

**[K8S-4508](https://jira.issues.couchbase.com/browse/K8S-4508/)**

The Operator may not clear the unreconcilable condition after the resource is fixed.

**[K8S-4509](https://jira.issues.couchbase.com/browse/K8S-4509/)**

Holding a cluster in mixed mode between 7.2.x and 7.6.x can prevent the Operator from reconciling some cluster settings.

**[K8S-4510](https://jira.issues.couchbase.com/browse/K8S-4510/)**

Remaining in mixed mode on older Couchbase Server versions can cause the Operator to log errors due to incorrect version checks.

**[K8S-4511](https://jira.issues.couchbase.com/browse/K8S-4511/)**

You cannot currently specify Arbiter nodes in the services order during an upgrade.

**[K8S-4512](https://jira.issues.couchbase.com/browse/K8S-4512/)**

The Operator can update Index Storage settings twice accidentally.

**[K8S-4514](https://jira.issues.couchbase.com/browse/K8S-4514/)**

The Operator can update the Fluent Bit configuration accidentally.

**[K8S-4515](https://jira.issues.couchbase.com/browse/K8S-4515/)**

While processing a bucket migration, the Operator does not send the correct online change flag for modifications to Couchbase Server when changing the Eviction Policy.

**[K8S-4520](https://jira.issues.couchbase.com/browse/K8S-4520/)**

The admission controller allows encryption at rest to be enabled in mixed mode.

**[K8S-4521](https://jira.issues.couchbase.com/browse/K8S-4521/)**

The admission controller allows use of the Couchbase User `spec.user` field for users that reference clusters not running version 8.0.0.

## [](#feedback)Feedback

You can have a big impact on future versions of the Operator (and its documentation) by providing Couchbase with your direct feedback and observations. Please feel free to post your questions and comments to the [Couchbase Forums](https://forums.couchbase.com/c/couchbase-server/Kubernetes).

## [](#licenses-for-third-party-components)Licenses for Third-Party Components

The complete list of licenses for Couchbase products is available on the [Legal Agreements](https://www.couchbase.com/legal/agreements) page. Couchbase is thankful to all of the individuals that have created these third-party components.

## [](#more-information)More Information

* [Couchbase Server Release Notes Version 8.0](../../server/current/release-notes/relnotes.md)
* [What’s New in Couchbase Server Version 8.0](../../server/current/introduction/whats-new.md)