---
title: Release Notes for Couchbase Autonomous Operator 2.7
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.7@operator::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.7/release-notes.html)

# Release Notes for Couchbase Autonomous Operator 2.7

Autonomous Operator 2.7 release provides full support for Couchbase Server 7.6, and several improvements to Pod Scheduling and Networking, as well as a number of minor fixes.

Take a look at the [What's New](whats-new.md) page for a list of new features and improvements that are available in this release.

## [](#installation)Installation

For installation instructions, refer to:

* [Install the Operator on Kubernetes](install-kubernetes.md)
* [Install the Operator on OpenShift](install-openshift.md)

## [](#upgrading-to-autonomous-operator-2-7)Upgrading to Autonomous Operator 2.7

The necessary steps needed to upgrade to this release depend on which version of the Autonomous Operator you are upgrading from.

### [](#upgrading-from-1-x-2-0-or-2-1)Upgrading from 1.x, 2.0, or 2.1

There is no direct upgrade path from versions prior to 2.2.0\. To upgrade from a 1.x, 2.0.x, or 2.1.x release, you must first upgrade to 2.4.x, paying particular attention to supported Kubernetes platforms and Couchbase Server versions. Refer to the [Operator 2.4 upgrade steps](#2.4@operator::howto-operator-upgrade.adoc) if upgrading from a pre-2.2 release.

### [](#upgrading-from-2-2-2-3-2-4-2-5-or-2-6)Upgrading from 2.2, 2.3, 2.4, 2.5, or 2.6

There are no additional upgrade steps when upgrading from these versions, and you may follow the [standard upgrade process](howto-operator-upgrade.md). However, due to [K8S-3097](https://issues.couchbase.com/browse/K8S-3097), all users will encounter a mandatory upgrade cycle when upgrading from a release older than 2.5.0, to versions 2.5.0, 2.5.1, or 2.6.0 through 2.6.3, to expose the missing Indexer HTTPS Port (see [Detailed Port Description](../../server/current/install/install-ports.md#detailed-port-description) for network port requirements). This behavior has changed in versions 2.5.2, 2.6.4, and 2.7.0, and there is no mandatory upgrade cycle — the missing port is added the next time there is a regular maintenance activity that involves Pod creation.

> [!IMPORTANT]
> An upgrade cycle is a relatively heavyweight operation that requires all pods in the cluster to be replaced, and data transferred between the old and new pods. The time taken to perform this operation is dependent on network bandwidth, disk IO and the amount of data resident in the database. For large, production databases, ensure an adequate maintenance window is scheduled as to minimize any disruption to clients and other business critical functions.
> 
> For further information read the [Couchbase Upgrade](concept-upgrade.md) concepts page.

## [](#release-271)Release 2.7.1

Couchbase Operator 2.7.1 was released in August 2025\. This maintenance release contains fixes to issues.

### [](#fixed-issues-v271)Fixed Issues

| Issue                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [K8S-3968](https://jira.issues.couchbase.com/browse/K8S-3968/) | **Summary:** There is a scenario where a Pod deletion takes too long to shut down, allowing Operator to see it as still active within the Couchbase Cluster, but not existing in the Kubernetes Resource database (etcd). This results in Operator classifying the Pod as an "Unknown" Pod, and summarily ejecting it from the Couchbase Cluster, which can result in a loss of Couchbase logs present on the Persistent Volumes of the Pod. |
| [K8S-4038](https://jira.issues.couchbase.com/browse/K8S-4038/) | **Summary:** In prior versions of Couchbase Operator, it was possible to set invalid values for the Indexer's Replica Count.                                                                                                                                                                                                                                                                                                                 |
| [K8S-4043](https://jira.issues.couchbase.com/browse/K8S-4043/) | **Summary:** Fixed a bug in the comparison of the existing and desired state of Local Persistent Volumes that can cause swap rebalances of pods with no reported diff.                                                                                                                                                                                                                                                                       |
| [K8S-4045](https://jira.issues.couchbase.com/browse/K8S-4045/) | **Summary:** In prior versions of Couchbase Operator, it was possible for pods to be scheduled unevenly across server groups.                                                                                                                                                                                                                                                                                                                |
| [K8S-4047](https://jira.issues.couchbase.com/browse/K8S-4047/) | **Summary:** In previous versions of Couchbase Operator, a user was unable to configure multiple replications per bucket. This limitation has been removed.                                                                                                                                                                                                                                                                                  |
| [K8S-4144](https://jira.issues.couchbase.com/browse/K8S-4144/) | **Summary:** In prior versions of Couchbase Operator, the metrics port annotation (prometheus.io/port) was set to 8091, even if TLS was enabled. It will not correctly set to 18091.                                                                                                                                                                                                                                                         |

## [](#release-v270)Release 2.7.0

Couchbase Autonomous Operator 2.7.0 was released in August 2024.

### [](#changes-in-behavior-v270)Changes in Behaviour

#### [](#delta-recovery-in-place-upgrades)Delta Recovery / In-Place Upgrades

The `DeltaRecovery` upgrade strategy added in Operator 2.6 has been replaced by `InPlaceUpgrade`, to better reflect the actual behaviour (not every Service can be Delta Recovered), and `DeltaRecovery` is now deprecated.

#### [](#storage-backend-migration)Storage Backend Migration

In Server 7.6 it is now possible to migrate between the Couchstore and Magma storage backends, as described in [Migrate a Bucket's Storage Backend](#7.6@server:manage/manage-buckets/migrate-bucket.adoc). Operator will automatically start the required Rebalances if it detects an unresolved Storage backend change. Storage Backend can also be configured using annotations, see [Bucket Backend Configuration](reference-annotations.md#bucket-backend-configuration) for more details.

#### [](#query-service-settings)Query Service Settings

Over time, a significant gap had appeared between the Query Service settings available in Couchbase Server, and the ones exposed via the `CouchbaseCluster` CRD in Autonomous Operator. This has been addressed in CAO 2.7.0, and the following cluster-wide settings are now available:

* Server 6.5+: `queryPipelineBatch`, `queryPipelineCap`, `queryScanCap`, `queryTimeout`, `queryPreparedLimit`, `queryCompletedLimit`, `queryCompletedThreshold`, `queryLogLevel`, `queryMaxParallelism`.
* Server 7.0+: `queryTxTimeout`, `queryMemoryQuota`, `queryUseCBO`, `queryCleanupClientAttempts`, `queryCleanupLostAttempts`, `queryCleanupWindow`, `queryNumAtrs`.
* Server 7.6+: `queryNodeQuota`, `queryUseReplica`, `queryNodeQuotaValPercent`, `queryNumCpus`, `queryCompletedMaxPlanSize`.

Note that `queryNodeQuota` is being exposed via the existing [spec.cluster.queryServiceMemoryQuota](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-queryservicememoryquota). For Server versions prior to 7.6, this value is used to determine Pod resource requirements, and from version 7.6 onwards will also be used to set `queryNodeQuota` on the Couchbase Server cluster (see [K8S-3436](https://issues.couchbase.com/browse/K8S-3436)).

Note that `queryNumCpus` requires a restart of the Query Service to take effect. In practice in a Kubernetes environment, this means that this will only affect Pods started after the setting has been updated.

> [!IMPORTANT]
> Prior to Operator 2.7.0, the above Query Service settings could still be set directly on the cluster.
> 
> To avoid these being reset to default values during the CAO upgrade, any of the above settings that have been changed must be added to the `CouchbaseCluster` resource during the upgrade.
> 
> Specifically, this needs to be done _after_ updating the CRDs, and _before_ installing the new Operator
> 
> For further information see [Update Existing Resources](howto-operator-upgrade.md#update-existing-resources).

#### [](#audit-log-pruning)Audit Log Pruning

With the addition of native pruning of rotated Audit Logs in Server 7.6, the [garbageCollection](resource/couchbasecluster.md#couchbaseclusters-spec-logging-audit-garbagecollection) sidecar is now deprecated.

#### [](#miscellaneous-changes)Miscellaneous Changes

* `cao collect logs` now has improved handling of larger clusters ([K8S-3322](https://issues.couchbase.com/browse/K8S-3322)).
* [couchbaseclusters.spec.networking.exposedFeatures](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposedfeatures) now includes `backup` as an option, allowing external access for the `cbbackupmgr` tool ([K8S-3508](https://issues.couchbase.com/browse/K8S-3508)).
* Any options specified at [couchbaseclusters.spec.security.securityContext](resource/couchbasecluster.md#couchbaseclusters-spec-security-securitycontext) are now also applied to the Operator Backup container ([K8S-3417](https://issues.couchbase.com/browse/K8S-3417)).
* It is possible to set a longer Termination Grace Period on the Cloud Native Gateway container with [terminationGracePeriodSeconds](resource/couchbasecluster.md#couchbaseclusters-spec-networking-cloudnativegateway-terminationgraceperiodseconds) ([K8S-3257](https://issues.couchbase.com/browse/K8S-3257)).
* A number of new metrics have been added, see [Prometheus Metrics Reference](reference-prometheus-metrics.md) for details.

### [](#fixed-issues-v270)Fixed Issues

| Issue                                                    | Description                                                                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [K8S-3377](https://issues.couchbase.com/browse/K8S-3377) | **Summary:** Previously the TestTLSRotateCAKillPodAndKillOperator test was failing with Server 7.6.                 |
| [K8S-3391](https://issues.couchbase.com/browse/K8S-3391) | **Summary:** Previously the Operator was not correctly deleting un-managed XDCR Remote Cluster References.          |
| [K8S-3452](https://issues.couchbase.com/browse/K8S-3452) | **Summary:** Previously the Operator was triggering a mandatory upgrade cycle when upgrading from 2.4.x or earlier. |
| [K8S-3587](https://issues.couchbase.com/browse/K8S-3587) | **Summary:** Previously the eventing\_manage\_functions RBAC role was missing from the list of cluster roles.       |

### [](#known-issues-v270)Known Issues

| Issue                                                         | Description                                                                                                                                                                                      |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [K8S-3632](https://issues.couchbase.com/browse/K8S-3632)      | **Summary:** It is not currently possible to set [couchbasecollections.spec.maxTTL](resource/couchbasecollection.md#couchbasecollections-spec-maxttl) to \-1 to disable expiry.                  |
| [K8S-3663](https://jira.issues.couchbase.com/browse/K8S-3663) | Three tests: TestPersistentVolumeAutoRecovery, TestUpgradeSupportableKillStatefulPodOnCreate, and TestAutoscaleUpMandatoryMutualTLS may fail when running self-certification on Kubernetes 1.31. |

## [](#feedback)Feedback

You can have a big impact on future versions of the Operator (and its documentation) by providing Couchbase with your direct feedback and observations. Please feel free to post your questions and comments to the [Couchbase Forums](https://forums.couchbase.com/c/couchbase-server/Kubernetes).

## [](#licenses-for-third-party-components)Licenses for Third-Party Components

The complete list of licenses for Couchbase products is available on the [Legal Agreements](https://www.couchbase.com/legal/agreements) page. Couchbase is thankful to all of the individuals that have created these third-party components.

## [](#more-information)More Information

* [Couchbase Server Release Notes](../../server/current/release-notes/relnotes.md)