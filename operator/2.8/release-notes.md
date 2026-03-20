---
title: Release Notes for Couchbase Kubernetes Operator 2.8
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.8@operator::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.8/release-notes.html)

# Release Notes for Couchbase Kubernetes Operator 2.8

Autonomous Operator 2.8 introduces our new Cluster Migration functionality well as a number of other improvements and minor fixes.

Take a look at the [What’s New](whats-new.md) page for a list of new features and improvements that are available in this release.

## [](#installation)Installation

For installation instructions, refer to:

* [Install the Operator on Kubernetes](install-kubernetes.md)
* [Install the Operator on OpenShift](install-openshift.md)

## [](#upgrading-to-kubernetes-operator-2-8)Upgrading to Kubernetes Operator 2.8

The necessary steps needed to upgrade to this release depend on which version of the Kubernetes Operator you are upgrading from.

### [](#upgrading-from-1-x-2-0-or-2-1)Upgrading from 1.x, 2.0, or 2.1

There is no direct upgrade path from versions prior to 2.2.0\. To upgrade from a 1.x, 2.0.x, or 2.1.x release, you must first upgrade to 2.4.x, paying particular attention to supported Kubernetes platforms and Couchbase Server versions. Refer to the [Operator 2.4 upgrade steps](#2.4@operator::howto-operator-upgrade.adoc) if upgrading from a pre-2.2 release.

### [](#upgrading-from-2-2-2-3-2-4-2-5-2-6-or-2-7)Upgrading from 2.2, 2.3, 2.4, 2.5, 2.6, or 2.7

There are no additional upgrade steps when upgrading from these versions, and you may follow the [standard upgrade process](howto-operator-upgrade.md).

For further information read the [Couchbase Upgrade](concept-upgrade.md) concepts page.

## [](#release-281)Release 2.8.1 (June 2025)

Couchbase Operator 2.8.1 was released in June 2025\. This maintenance release contains fixes to issues.

## [](#fixed-issues-v281)Fixed Issues

**[K8S-3793](https://jira.issues.couchbase.com/browse/K8S-3793/)**

Fixed a bug in Local Persistent Volume comparison logic that previously triggered unnecessary pod rebalancing when comparing existing and desired states, despite no actual differences being detected.

**[K8S-3840](https://jira.issues.couchbase.com/browse/K8S-3840/)**

Due to ephemeral volumes removing the staging directory, backups will fail if the defaultRecoveryMethod is set to resume. The admission controller will now invalidate backups using ephemeral volumes unless the defaultRecoveryMethod is set to either purge or none.

**[K8S-3889](https://jira.issues.couchbase.com/browse/K8S-3889/)**

Inplace upgrades are not supported prior to Couchbase Server Versions 7.2.x due to a required change in the startup files required by Couchbase Server.

## [](#release-v280)Release 2.8.0

Couchbase Kubernetes Operator 2.8.0 was released in March 2025.

### [](#changes-in-behavior-v280)Changes in Behaviour

#### [](#admission-controller-changes)Admission Controller Changes

The Dynamic Admission Controller (DAC) will now warn if any cluster settings don’t match our [Best Practices for Production Deployments](best-practices.md#production-deployments).

The DAC will now prevent changes to the `CouchbaseCluster` spec while a hibernation is taking place. If hibernation is enabled while a cluster is migrating, upgrading, scaling, or rebalancing, that process will conclude before the cluster enters hibernation. The DAC will warn when this is the case, and it will be visible in the operator logs.

To prevent any invalid resources failing to reconcile (i.e. if the DAC is not deployed in the current environment), the DAC Validation is now run at the beginning of the reconciliation loop. Any invalid resources will be skipped for reconciliation, marked as `NotValid`, and logged.

#### [](#bucket-and-index-service-settings)Bucket and Index Service Settings

In a previous version of the Operator, `enablePageBloomFilter` was unfortunately missed from the Index Service settings. This has been addressed in CAO 2.8.0, and it is now available as [couchbaseclusters.spec.cluster.indexer.enablePageBloomFilter](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-indexer-enablepagebloomfilter).

Until CAO 2.8.0, Bucket Compaction settings were only available to be set in the [CouchbaseCluster](resource/couchbasecluster.md) resource, at [couchbaseclusters.spec.cluster.autoCompaction](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-autocompaction). These settings have now been added to the [CouchbaseBucket](resource/couchbasebucket.md) resource at [couchbasebuckets.spec.autoCompaction](resource/couchbasebucket.md#couchbasebuckets-spec-autocompaction).

> [!IMPORTANT]
> Prior to Operator 2.8.0, the above settings could still be set directly on the cluster.
> 
> To avoid these being reset to default values during the CAO upgrade, any of the above settings that have been changed must be added to the appropriate resource during the upgrade.
> 
> Specifically, this needs to be done _after_ updating the CRDs, and _before_ installing the new Operator
> 
> For further information see [Update Existing Resources](howto-operator-upgrade.md#update-existing-resources).

#### [](#metrics-changes)Metrics Changes

A number of new metrics have been added, see [Prometheus Metrics Reference](reference-prometheus-metrics.md) for details.

It is now possible to include the Couchbase Cluster UUID, or Cluster UUID and Cluster Name, as labels with any Operator metric that is related to a specific Couchbase Cluster. This can be enabled by setting `optional-metric-labels` to either `uuid-only` or `uuid-and-name`, when using [cao create operator](tools/cao.md#cao-create-operator-flags) or [cao generate operator](tools/cao.md#cao-generate-operator-flags).

While adding the Couchbase Cluster UUID and Cluster Name labels, it was discovered that there were inconsistencies regarding the Kubernetes Namespace and Cluster Resource Name labels in some of the existing metrics. Some had separate labels for `namespace` and `name`, and some had a combined `namespace/name` label. In order to provide consistency, all metrics by default now have separate `name` and `namespace` labels. The previous behavior, where a small number of metrics had the combined form of the label, can be achieved by setting `separate-cluster-namespace-and-name` to `false`, when using [cao create operator](tools/cao.md#cao-create-operator-flags) or [cao generate operator](tools/cao.md#cao-generate-operator-flags).

#### [](#annotation-changes)Annotation Changes

##### [](#storage-backend-migration)Storage Backend Migration

As an enhancement to the Couchstore/Magma migration functionality added in Operator 2.7, CAO 2.8.0 adds two new annotations:

* Bucket Migrations are now disabled by default, to prevent unexpected node rebalances. These can be enabled with [cao.couchbase.com/buckets.enableBucketMigrationRoutines](reference-annotations.md#cao-couchbase-combuckets-enablebucketmigrationroutines).
* Similar to a maintenance upgrade, it is now possible to specify how many Pods can be migrated at a time with [cao.couchbase.com/buckets.maxConcurrentPodSwaps](reference-annotations.md#cao-couchbase-combuckets-maxconcurrentpodswaps).

##### [](#history-retention)History Retention

The annotations related to History Retention, that were added in Operator 2.4.1, have now been added to the [CouchbaseBucket](resource/couchbasebucket.md), and [CouchbaseCollection](resource/couchbasecollection.md) resources, at [couchbasebuckets.spec.historyRetention](resource/couchbasebucket.md#couchbasebuckets-spec-historyretention), and [couchbasecollections.spec.history](resource/couchbasecollection.md#couchbasecollections-spec-history), respectively.

The History Retention annotations should be considered deprecated, and it should be noted that if used, they will take precedence over the equivalent values in the resources. Care should be taken to make sure that the annotations are removed as soon as the resources have been updated with the new attributes.

### [](#fixed-issues-v280)Fixed Issues

**[K8S-3558](https://jira.issues.couchbase.com/browse/K8S-3558)**

Couchbase Autonomous Operator commences an In-place Upgrade when the cluster is under-resourced.

**[K8S-3579](https://jira.issues.couchbase.com/browse/K8S-3579)**

Couchbase Autonomous Operator tries to change invalid bucket configurations in a loop.

**[K8S-3591](https://jira.issues.couchbase.com/browse/K8S-3591)**

Couchbase Autonomous Operator crashes if Incremental Backup is missing schedule.

**[K8S-3596](https://jira.issues.couchbase.com/browse/K8S-3596)**

Crash in Operator due to invalid memory access.

**[K8S-3605](https://jira.issues.couchbase.com/browse/K8S-3605)**

Upgrade Swap Rebalance is retried with different parameters on Operator Pod deletion.

**[K8S-3609](https://jira.issues.couchbase.com/browse/K8S-3609)**

Hibernation fails to bring back any Pod with error extracting image version.

**[K8S-3621](https://jira.issues.couchbase.com/browse/K8S-3621)**

Shadowed Secret did not get updated.

**[K8S-3632](https://jira.issues.couchbase.com/browse/K8S-3632)**

Unable to set -1 for Collection-level `maxTTL`.

**[K8S-3639](https://jira.issues.couchbase.com/browse/K8S-3639)**

Operator loses track of pending Pods when an Eviction of the Operator Pod occurs.

**[K8S-3641](https://jira.issues.couchbase.com/browse/K8S-3641)**

Crash in `handleVolumeExpansion` if `enableOnlineVolumeExpansion` is True but no Volume Mounts configured.

**[K8S-3655](https://jira.issues.couchbase.com/browse/K8S-3655)**

Clear Upgrade condition if the Operator is not performing an upgrade.

**[K8S-3659](https://jira.issues.couchbase.com/browse/K8S-3659)**

When scaling down, Cluster does not maintain balance across Server Groups.

**[K8S-3696](https://jira.issues.couchbase.com/browse/K8S-3696)**

DAC prevents configuration of multiple XDCR Replications of same Buckets to different remote Clusters.

**[K8S-3772](https://jira.issues.couchbase.com/browse/K8S-3772)**

Self-Certification: Artifacts PVC should use `--storage-class` parameter when creating the Certification Pod.

**[K8S-3788](https://jira.issues.couchbase.com/browse/K8S-3788)**

Operator container crashes when there is a managed Scope/Collection Group added for the Ephemeral Bucket.

### [](#known-issues-v280)Known Issues

**[K8S-3617](https://jira.issues.couchbase.com/browse/K8S-3617)**

It’s not possible to set [couchbaseclusters.spec.cluster.indexer.redistributeIndexes](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-indexer-redistributeindexes) from True to False during a reconciliation.

**[K8S-3908](https://jira.issues.couchbase.com/browse/K8S-3908)**

Metric `couchbase_operator_memory_under_management_bytes` is incorrectly showing 0.

**[K8S-3909](https://jira.issues.couchbase.com/browse/K8S-3909)**

Metric `couchbase_operator_cpu_under_management` is incorrectly showing 0.

**[K8S-3910](https://jira.issues.couchbase.com/browse/K8S-3910)**

Operator tries to migrate storage backend of buckets even before Couchbase cluster is in 7.6.0+.

## [](#feedback)Feedback

You can have a big impact on future versions of the Operator (and its documentation) by providing Couchbase with your direct feedback and observations. Please feel free to post your questions and comments to the [Couchbase Forums](https://forums.couchbase.com/c/couchbase-server/Kubernetes).

## [](#licenses-for-third-party-components)Licenses for Third-Party Components

The complete list of licenses for Couchbase products is available on the [Legal Agreements](https://www.couchbase.com/legal/agreements) page. Couchbase is thankful to all of the individuals that have created these third-party components.

## [](#more-information)More Information

* [Couchbase Server Release Notes](../../server/current/release-notes/relnotes.md)