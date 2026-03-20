---
title: Prerequisites and System Requirements
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/prerequisite-and-setup.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:operator::prerequisite-and-setup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/prerequisite-and-setup.html)

# Prerequisites and System Requirements

> The Kubernetes Operator supports several popular Kubernetes environments and cloud-native utilities. 

To install the Couchbase Kubernetes Operator, all you need is a Kubernetes or OpenShift cluster running one of the [compatible versions listed below](#kubernetes-platform-compatibility).

> [!NOTE]
> For all supported software versions listed on this page, maintenance/patch releases (x.x**.X**) inherit the same support level, unless noted otherwise.

## [](#couchbase-compatibility)Couchbase Compatibility

Couchbase compatibility falls under these 3 categories:

* **Unsupported**: This combination is not tested and is not within the scope of technical support if you have purchased a support agreement.
* **Compatible**: This combination has been tested previously and should be compatible. Our technical support organization does not recommend this combination. You may run the [Operator Self-Certification Lifecycle](concept-platform-certification.md) tooling to verify the Operator will work on a compatible platform. We therefore highly encourage the use of a supported platform version.
* **Supported**: This combination is subject to ongoing quality assurance and is fully supported by our technical support organization.

This release supports the deployment of the following Couchbase software:

| Software                            | Version     |
| ----------------------------------- | ----------- |
| Couchbase Server Enterprise Edition | 7.2 - 8.0\* |

\*: Couchbase Server 8.0 is supported with Operator 2.8.1; however, new features in 8.0 are only supported on Operator 2.9.x

The following diagram depicts Couchbase Server compatibility with the Operator for this, and previous releases, and can be used to calculate upgrade paths:

Couchbase Server Compatibility

![compatibility server](_images/compatibility-server.png)

### [](#couchbase-backup-and-restore-compatibility)Couchbase Backup and Restore Compatibility

This release supports the following container images for [managed backup and restore](concept-backup.md) of Couchbase clusters:

| Container Image                                                             | Backup Utility                                                                                                             | Backup From and Restore To |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [operator-backup:1.5.0](https://hub.docker.com/r/couchbase/operator-backup) | [cbbackupmgr 7.6.8](https://docs.couchbase.com/server/7.6/manage/manage-backup-and-restore/manage-backup-and-restore.html) | Couchbase Server 7.2+      |

The following diagram depicts Operator Backup image compatibility with all supported Couchbase Server versions, you should consider this when upgrading Couchbase Server:

Operator Backup Compatibility

![compatibility backup](_images/compatibility-backup.png)

### [](#couchbase-fluent-bit-compatibility)Couchbase Fluent Bit Compatibility

This release supports the following versions of the Couchbase Fluent Bit image for log forwarding:

| Couchbase Operator Version | Supported Couchbase Fluent Bit Versions |
| -------------------------- | --------------------------------------- |
| 2.6.0                      | 1.2.0 - 1.2.7                           |
| 2.7.0                      | 1.2.0 - 1.2.9                           |
| 2.8.0                      | 1.2.0 - 1.3.0                           |
| 2.9.0                      | 1.2.0 - 1.3.0                           |

Operator Fluent Bit Compatibility

![compatibility fluentbit](_images/compatibility-fluentbit.png)

## [](#kubernetes-platform-compatibility)Kubernetes Compatibility

This release supports the following Kubernetes platforms:

| Platform                             | Version     |
| ------------------------------------ | ----------- |
| Open Source Kubernetes               | 1.31 - 1.35 |
| Red Hat OpenShift Container Platform | 4.18 - 4.20 |

The following diagrams depict Couchbase Operator compatibility with Kubernetes and OpenShift platforms, and can be used to calculate upgrade paths:

Kubernetes and Red Hat OpenShift Compatibility

![compatibility kubernetes](_images/compatibility-kubernetes.png)

> [!IMPORTANT]
> Where an Operator release is marked as _supported_, this means it has been fully tested for functionality on that platform version. Couchbase Support will actively recreate and diagnose issues. Where relevant, fixes will be made to the affected product and patch releases made.
> 
> Where an Operator release is marked as _compatible,_ however, this means it has been assessed by the development team to be technically feasible, and may have had rudimentary compatibility testing. You may run the [Operator Self-Certification Lifecycle](concept-platform-certification.md) tooling to verify the Operator will work on a compatible platform. Support will be provided on a best-effort basis, and any issues may not result in fixes and patch releases. We therefore highly encourage the use of a supported platform version.

### [](#managed-kubernetes-compatibility)Managed Kubernetes Compatibility

This release supports the following managed Kubernetes services and utilities:

* Amazon EKS
* Google GKE
* Microsoft AKS
* K3s
* Bottlerocket OS

## [](#compatibility-pv)Persistent Volume Compatibility

Persistent volumes are mandatory for production deployments. The Couchbase Operator is designed to work with any CSI-compliant storage driver and compatibility with different CSI implementations can be validated using the [Operator Self-Certification Lifecycle](concept-platform-certification.md) tooling. Review the Kubernetes Operator [best practices](best-practices.md#persistent-volumes-best-practices) for more information about cluster supportability requirements.

## [](#hardware-requirements)Hardware Requirements

It is highly recommended that your Couchbase clusters are deployed with some form of compute and memory resource request in order to ensure fair scheduling of workloads and to ensure resources are available to meet basic service levels.

### [](#cpu-and-memory-requirements)CPU and Memory Requirements

You can set all resource allocations yourself explicitly. However, for new users to the platform, we recommend using [auto resource allocation](resource/couchbasecluster.md#couchbaseclusters-spec-autoresourceallocation). Auto resource allocation will require:

* 2 CPUs per Couchbase pod by default.
* 512MiB of memory per pod for each of the Data, Index, Search, and Eventing Services that are enabled. 1GiB of memory per pod if the Analytics Service is enabled. An additional 25% memory overhead on top of the memory requirements for each service. For a typical development cluster where all services are enabled, this would equal 3.75GiB.

You can read more about pod scheduling in the [best practices](best-practices.md#pod-scheduling) documentation.

### [](#architecture-requirements)Architecture requirements

The Kubernetes Operator supports both ARM and AMD64 Kubernetes clusters. The architecture of each node must be uniform across the cluster as the use of mixed architecture nodes is not supported.

> [!NOTE]
> The official Couchbase docker repository contains multi-arch images which do not require explicit references to architecture tags when being pulled and deployed. However, when pulling from a private repository, or performing intermediate processing on a machine with a different architecture than the deployed cluster, the use of explicit tags may be required to ensure the correct images are deployed.

> [!IMPORTANT]
> For optimal performance with Couchbase Server 8.0 and later versions, in particular for vector search (FTS and GSI) workloads, use nodes that support AVX2 CPU instructions (x86-64-v3 Microarchitecture). For guidance on detecting AVX2 support and scheduling pods on AVX2-capable nodes, see [AVX2-Aware Scheduling for Couchbase Server](tutorial-avx2-scheduling.md).

## [](#rbac-and-networking-requirements)RBAC and Networking Requirements

Preparing the Kubernetes cluster to run the Operator may require setting up proper RBAC and network settings in your Kubernetes cluster. Before moving forward, review the following documentation:

* [Operator RBAC Settings](reference-operator-rbac.md)
* [Kubernetes Networking](concept-kubernetes-networking.md)
* [Couchbase Networking](concept-couchbase-networking.md)

## [](#next-steps)Next Steps

As you’re setting up your Kubernetes environment, make sure that you’re following the recommended [best practices](best-practices.md).

Once your Kubernetes environment is set up, you can move on to installing the admission controller and the Operator.

* [Install the Operator on Kubernetes](install-kubernetes.md)
* [Install the Operator on OpenShift](install-openshift.md)