---
title: Release Notes for Couchbase Autonomous Operator 2.6
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/release-notes.adoc
  xref: xref:2.6@operator::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/release-notes.html)

# Release Notes for Couchbase Autonomous Operator 2.6

Autonomous Operator 2.6 release is primarily focused on platform updates, feature parity with Couchbase Server, improvements to Pod Management and Security, as well as a number of minor fixes.

Take a look at the [What's New](whats-new.md) page for a list of new features and improvements that are available in this release.

## [](#installation)Installation

For installation instructions, refer to:

* [Install the Operator on Kubernetes](install-kubernetes.md)
* [Install the Operator on OpenShift](install-openshift.md)

## [](#upgrading-to-autonomous-operator-2-6)Upgrading to Autonomous Operator 2.6

The necessary steps needed to upgrade to this release depend on which version of the Autonomous Operator you are upgrading from.

### [](#upgrading-from-1-x-2-0-or-2-1)Upgrading from 1.x, 2.0, or 2.1

There is no direct upgrade path from versions prior to 2.2.0\. To upgrade from a 1.x, 2.0.x, or 2.1.x release, you must first upgrade to 2.4.x, paying particular attention to supported Kubernetes platforms and Couchbase Server versions. Refer to the [Operator 2.4 upgrade steps](#2.4@operator::howto-operator-upgrade.adoc) if upgrading from a pre-2.2 release.

### [](#upgrading-from-2-2-2-3-2-4-or-2-5)Upgrading from 2.2, 2.3, 2.4, or 2.5

There are no additional upgrade steps when upgrading from these versions, and you may follow the [standard upgrade process](howto-operator-upgrade.md). However, due to [K8S-3097](https://issues.couchbase.com/browse/K8S-3097), all users will encounter a mandatory upgrade cycle when upgrading from a release older than 2.5.0, to versions 2.5.0, 2.5.1, or 2.6.0 through 2.6.3, to expose the missing Indexer HTTPS Port (see [Detailed Port Description](../../server/current/install/install-ports.md#detailed-port-description) for network port requirements). This behavior has changed in version 2.5.2 and 2.6.4, and there is no mandatory upgrade cycle - the missing port is added the next time there is a regular maintenance activity that involves Pod creation.

> [!IMPORTANT]
> An upgrade cycle is a relatively heavyweight operation that requires all pods in the cluster to be replaced, and data transferred between the old and new pods. The time taken to perform this operation is dependent on network bandwidth, disk IO and the amount of data resident in the database. For large, production databases, ensure an adequate maintenance window is scheduled as to minimize any disruption to clients and other business critical functions.
> 
> For further information read the [Couchbase Upgrade](concept-upgrade.md) concepts page.

## [](#release-v264-addendum)Addendum to Release 2.6.4

Since Couchbase Autonomous Operator 2.6.4 was released, the following issues have been identified.

| Issue                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [K8S-3967](https://issues.couchbase.com/browse/K8S-3967) | **Summary:** There is a scenario where a Pod deletion takes too long to shut down, allowing Operator to see it as still active within the Couchbase Cluster, but not existing in the Kubernetes Resource database (etcd). This results in Operator classifying the Pod as an "Unknown" Pod, and summarily ejecting it from the Couchbase Cluster, which can result in a loss of Couchbase logs present on the Persistent Volumes of the Pod. |

## [](#release-v264)Release 2.6.4

Couchbase Autonomous Operator 2.6.4 was released in June 2024.

### [](#changes-in-behavior-v264)New Features and Behavioral Changes

#### [](#pod-lifecycle)Pod Lifecycle

The default value for the per-Pod `terminationGracePeriodSeconds` is 30 seconds (see [Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination)). From Operator 2.6.4, any new Pods will be created with `terminationGracePeriodSeconds` set to 1200 seconds (20 minutes), to allow time for Couchbase Server to quiesce all connections and cleanly shut down.

### [](#fixed-issues-v264)Fixed Issues

| Issue                                                    | Description                                                                                                                                               |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [K8S-3452](https://issues.couchbase.com/browse/K8S-3452) | **Summary:** Previously the Operator was triggering a mandatory upgrade cycle when upgrading from 2.4.x or earlier.                                       |
| Various                                                  | **Summary:** A number of further stability/reliability improvements around in-place upgrades (using Graceful Failover / Delta Recovery where applicable). |

## [](#release-v263)Release 2.6.3

Couchbase Autonomous Operator 2.6.3 was released in April 2024.

### [](#fixed-issues-v263)Fixed Issues

| Issue                                                    | Description                                                                                                        |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [K8S-3430](https://issues.couchbase.com/browse/K8S-3430) | **Summary:** Previously the Operator was not setting the correct recovery type for nodes without the Data Service. |

## [](#release-v262)Release 2.6.2

Couchbase Autonomous Operator 2.6.2 was released in March 2024.

### [](#fixed-issues-v262)Fixed Issues

| Issue                                                    | Description                                                                                                                    |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [K8S-3391](https://issues.couchbase.com/browse/K8S-3391) | **Summary:** Previously the Operator was not correctly deleting un-managed XDCR Remote Cluster References.                     |
| [K8S-3392](https://issues.couchbase.com/browse/K8S-3392) | **Summary:** Previously the Operator was not using the correct failover mechanism for nodes without the Data or Index Service. |

## [](#release-v261)Release 2.6.1

Couchbase Autonomous Operator 2.6.1 was released in February 2024.

### [](#changes-in-behavior-v261)New Features and Behavioral Changes

#### [](#cloud-native-gateway)Cloud Native Gateway

The Couchbase _Cloud Native Gateway_ (CNG), a new component that allows applications to access Couchbase through a set of RPC network endpoints based on [gRPC](https://grpc.io/), is now Generally Available.

See [Cloud Native Gateway](concept-cloud-native-gateway.md) for details.

#### [](#miscellaneous-improvements)Miscellaneous Improvements

* Diffs in the Operator's "Resource Updated" logs are now human readable ([K8S-3268](https://issues.couchbase.com/browse/K8S-3268)).
* Added missing Magma-related Bucket settings ([K8S-3290](https://issues.couchbase.com/browse/K8S-3290)).
* When performing a Rolling Upgrade, upgrade the Couchbase Server Orchestrator node last to reduce time spent waiting on orchestrator elections ([K8S-3305](https://issues.couchbase.com/browse/K8S-3305)).
* Improved error reporting during Alternate Address setup ([K8S-3317](https://issues.couchbase.com/browse/K8S-3317)).

### [](#fixed-issues-v261)Fixed Issues

| Issue                                                    | Description                                                                                                                                                                                         |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [K8S-3264](https://issues.couchbase.com/browse/K8S-3264) | **Summary:** Previously the Operator was not correctly honouring the useVirtualPath setting in the CouchbaseBackup resource.                                                                        |
| [K8S-3282](https://issues.couchbase.com/browse/K8S-3282) | **Summary:** Previously the Operator was emitting an extraneous "unknown field" message to the logs.                                                                                                |
| [K8S-3302](https://issues.couchbase.com/browse/K8S-3302) | **Summary:** Previously the Operator would raise a nil reference exception when a Cluster was defined with logging enabled, but a Server Group is added without a default or logging mount defined. |
| [K8S-3331](https://issues.couchbase.com/browse/K8S-3331) | **Summary:** Previously the Operator was not performing a Graceful Failover during a Delta Recovery-based Rolling Upgrade.                                                                          |
| [K8S-3332](https://issues.couchbase.com/browse/K8S-3332) | **Summary:** Previously the Operator was failing to rotate Encrypted Private Keys with Couchbase Server 7.2.4 and later.                                                                            |
| [K8S-3358](https://issues.couchbase.com/browse/K8S-3358) | **Summary:** Previously there was a conflict between the Readiness Probe configurations of the Exporter and Cloud Native Gateway sidecars.                                                          |
| [K8S-3365](https://issues.couchbase.com/browse/K8S-3365) | **Summary:** Previously the Delta Recovery upgrade test was using invalid parameters.                                                                                                               |
| [K8S-3374](https://issues.couchbase.com/browse/K8S-3374) | **Summary:** Previously the Operator was failing to pass the correct credentials to the Cloud Native Gateway sidecar.                                                                               |

## [](#release-v260)Release 2.6.0

Couchbase Autonomous Operator 2.6.0 was released in December 2023.

### [](#changes-in-behavior-v260)New Features and Behavioral Changes

#### [](#immediate-backups)Immediate Backups

The CouchbaseBackup resource now has the backup strategies of immediate\_full and immediate\_incremental to run a backup immediately.

#### [](#pod-management)Pod Management

The operator now takes into consideration index placement, data placement, and server version to identify pods to remove on scaling events. The operator now will perform in place upgrades using Delta Recovery rebalances on Couchbase Server version upgrades.

#### [](#pod-and-container-changes)Pod and Container Changes

The operator now adds the prometheus.io/scheme annotation to pods. The operator now adds platform specific zone labels for EKS, GKE and AKS to Couchbase Server persistent volume claims.

#### [](#crd-changes)CRD Changes

The field `couchbasebackuprestore.spec.backup` is no longer mandatory when using ephemeral volumes. The field `couchbasecluster.spec.onlineExpansionTimeout` has been added as an int that specifies the number of minutes between 0-30 that the operator should wait before failing over to swap rebalance for volume expansions. The field `couchbasecluster.spec.upgradeProcess` has been added as an enum of "DeltaRecovery" or "SwapRebalance". Default is "SwapRebalance".

#### [](#cli-changes)CLI Changes

Logs can now be uploaded directly to the Couchbase support portal via the `--upload-host`, `--customer`, `--upload-proxy` and `--ticket` parameters Pod Readiness Delay and Pod Readiness period can be set via the `cao create operator` command. These settings will be applied to all pods created by the operator.

### [](#fixed-issues-v260)Fixed Issues

| Issue                                                    | Description                                                                                                                            |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [K8S-3216](https://issues.couchbase.com/browse/K8S-3216) | **Summary:** Previously the operator would loop on buckets with specific settings, continuously updating and spamming logs.            |
| [K8S-3189](https://issues.couchbase.com/browse/K8S-3189) | **Summary:** Previously the operator identified the eventing\_admin role as a bucket role and not a cluster role                       |
| [K8S-3179](https://issues.couchbase.com/browse/K8S-3179) | **Summary:** Previously the operator would log a large json structure to the logs when it failed to create a pod.                      |
| [K8S-3095](https://issues.couchbase.com/browse/K8S-3095) | **Summary:** Previously the Operator would not allow you remove the setting for readerThreads                                          |
| [K8S-3283](https://issues.couchbase.com/browse/K8S-3283) | **Summary:** Previously the Operator would not use the new couchbasecluster.spec.security.podSecurityContext when creating backup jobs |
| [K8S-3167](https://issues.couchbase.com/browse/K8S-3167) | **Summary:** Previously the operator would continually update Magma Bucket settings if History Retention Annotations were missing      |

## [](#feedback)Feedback

You can have a big impact on future versions of the Operator (and its documentation) by providing Couchbase with your direct feedback and observations. Please feel free to post your questions and comments to the [Couchbase Forums](https://forums.couchbase.com/c/couchbase-server/Kubernetes).

## [](#licenses-for-third-party-components)Licenses for Third-Party Components

The complete list of licenses for Couchbase products is available on the [Legal Agreements](https://www.couchbase.com/legal/agreements) page. Couchbase is thankful to all of the individuals that have created these third-party components.

## [](#more-information)More Information

* [Couchbase Server Release Notes](../../server/current/release-notes/relnotes.md)