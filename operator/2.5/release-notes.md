---
title: Release Notes for Couchbase Autonomous Operator 2.5
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/release-notes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.5@operator::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/release-notes.html)

# Release Notes for Couchbase Autonomous Operator 2.5

Autonomous Operator 2.5 release is primarily focused on platform updates, feature parity with Couchbase Server, improvements to Pod Management and Security, as well as a number of minor fixes.

Take a look at the [What’s New](whats-new.md) page for a list of new features and improvements that are available in this release.

## [](#installation)Installation

For installation instructions, refer to:

* [Install the Operator on Kubernetes](install-kubernetes.md)
* [Install the Operator on OpenShift](install-openshift.md)

## [](#upgrading-to-autonomous-operator-2-5)Upgrading to Autonomous Operator 2.5

The necessary steps needed to upgrade to this release depend on which version of the Autonomous Operator you are upgrading from.

### [](#upgrading-from-1-x-2-0-2-1)Upgrading from 1.x, 2.0, 2.1

There is no direct upgrade path from versions prior to 2.2.0\. To upgrade from a 1.x, 2.0.x, or 2.1.x release, you must first upgrade to 2.4.x, paying particular attention to supported Kubernetes platforms and Couchbase Server versions. Refer to the [Operator 2.4 upgrade steps](#2.4@operator::howto-operator-upgrade.adoc) if upgrading from a pre-2.2 release.

### [](#upgrading-from-2-2-2-3-and-2-4)Upgrading from 2.2, 2.3, and 2.4

There are no additional upgrade steps when upgrading from these versions, and you may follow the [standard upgrade process](howto-operator-upgrade.md). However, due to [K8S-3097](https://issues.couchbase.com/browse/K8S-3097), all users will encounter a mandatory upgrade cycle when upgrading from a release older than 2.5.0, to versions 2.5.0 or 2.5.1, to expose the missing Indexer HTTPS Port (see [Detailed Port Description](../../server/current/install/install-ports.md#detailed-port-description) for network port requirements). This behavior has changed in version 2.5.2 and there is no mandatory upgrade cycle - the missing port is added the next time there is a regular maintenance activity that involves Pod creation.

> [!IMPORTANT]
> An upgrade cycle is a relatively heavyweight operation that requires all pods in the cluster to be replaced, and data transferred between the old and new pods. The time taken to perform this operation is dependent on network bandwidth, disk IO and the amount of data resident in the database. For large, production databases, ensure an adequate maintenance window is scheduled as to minimize any disruption to clients and other business critical functions.
> 
> For further information read the [Couchbase Upgrade](concept-upgrade.md) concepts page.

## [](#release-v252)Release 2.5.2

Couchbase Autonomous Operator 2.5.2 was released in May 2024.

### [](#fixed-issues-v252)Fixed Issues

| Issue                                                    | Description                                                                                                              |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [K8S-3412](https://issues.couchbase.com/browse/K8S-3412) | **Summary:** Previously the Operator was not correctly deleting un-managed XDCR Remote Cluster References.               |
| [K8S-3452](https://issues.couchbase.com/browse/K8S-3452) | **Summary:** Previously the Operator was triggering a mandatory upgrade cycle when upgrading from 2.4.x or earlier.      |
| [K8S-3456](https://issues.couchbase.com/browse/K8S-3456) | **Summary:** Previously the Operator was failing to rotate Encrypted Private Keys with Couchbase Server 7.2.4 and later. |

## [](#release-v251)Release 2.5.1

Couchbase Autonomous Operator 2.5.1 was released in December 2023.

### [](#fixed-issues-v251)Fixed Issues

| Issue                                                    | Description                                                                                                                        |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [K8S-3234](https://issues.couchbase.com/browse/K8S-3234) | **Summary:** Previously the Operator would log a large JSON structure to the logs when it failed to create a Pod.                  |
| [K8S-3235](https://issues.couchbase.com/browse/K8S-3235) | **Summary:** Previously the Operator identified the eventing\_admin role as a Bucket role and not a Cluster role.                  |
| [K8S-3236](https://issues.couchbase.com/browse/K8S-3236) | **Summary:** Previously the operator would continually update Magma Bucket settings if History Retention Annotations were missing. |
| [K8S-3239](https://issues.couchbase.com/browse/K8S-3239) | **Summary:** Previously the Operator would not allow you to remove the setting for readerThreads.                                  |

## [](#release-v250)Release 2.5.0

Couchbase Autonomous Operator 2.5.0 was released in August 2023.

### [](#changes-in-behavior-v250)New Features and Behavioral Changes

#### [](#feature-parity-with-couchbase-server)Feature Parity with Couchbase Server

The Operator now allows Data Service (`memcached`) AuxIO and NonIO Threads to be configured.

The CouchbaseBackup resource now has a Default Recovery Method which specifies how `cbbackupmgr` should recover from broken Backup/Restore attempts.

#### [](#pod-management)Pod Management

The Operator now parallelizes pod creation, for example during cluster creation and when performing upgrades, saving overall wall-clock time.

The Operator now adds specific labels to the PodDisruptionBudget for Cluster Member Pods, to make sure that only Cluster Members are included in the count used during a disruption. Similarly, the internal pod cache behaviour has been improved to only cache Cluster Member pods.

#### [](#pod-and-container-security-contexts)Pod and Container Security Contexts

From Operator 2.5, [couchbaseclusters.spec.securityContext](resource/couchbasecluster.md#couchbaseclusters-spec-securitycontext) has been deprecated in favour of [couchbaseclusters.spec.security.podSecurityContext](resource/couchbasecluster.md#couchbaseclusters-spec-security-podsecuritycontext) and [couchbaseclusters.spec.security.securityContext](resource/couchbasecluster.md#couchbaseclusters-spec-security-securitycontext), to define privilege and access control settings for Pods or Containers.

### [](#fixed-issues-v250)Fixed Issues

| Issue                                                    | Description                                                                                                                                                               |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [K8S-3001](https://issues.couchbase.com/browse/K8S-3001) | **Summary:** Previously the Operator was not correctly ignoring/discarding existing XDCR Replications when Managed XDCR was enabled on already-managed Couchbase Cluster. |
| [K8S-3010](https://issues.couchbase.com/browse/K8S-3010) | **Summary:** Previously the Operator would crash if a Backup resource was added with missing schedules.                                                                   |
| [K8S-3033](https://issues.couchbase.com/browse/K8S-3033) | **Summary:** Couchbase Server allows autoFailoverMaxCount of more than 3 from 7.1.0 onwards. The Operator now honours this, and sets the correct default.                 |
| [K8S-3041](https://issues.couchbase.com/browse/K8S-3041) | **Summary:** Previously the Operator was logging excessive node-related 'Reconcile completed' messages at info rather than debug.                                         |
| [K8S-3076](https://issues.couchbase.com/browse/K8S-3076) | **Summary:** Previously the Operator was logging excessive RBAC-related 'Reconcile completed' messages at info rather than debug.                                         |
| [K8S-3097](https://issues.couchbase.com/browse/K8S-3097) | **Summary:** Previously the Indexer HTTPS Port (19102) was not being exposed by either the Couchbase Server Pod or the service.                                           |

## [](#feedback)Feedback

You can have a big impact on future versions of the Operator (and its documentation) by providing Couchbase with your direct feedback and observations. Please feel free to post your questions and comments to the [Couchbase Forums](https://forums.couchbase.com/c/couchbase-server/Kubernetes).

## [](#licenses-for-third-party-components)Licenses for Third-Party Components

The complete list of licenses for Couchbase products is available on the [Legal Agreements](https://www.couchbase.com/legal/agreements) page. Couchbase is thankful to all of the individuals that have created these third-party components.

## [](#more-information)More Information

* [Couchbase Server Release Notes](../../server/current/release-notes/relnotes.md)