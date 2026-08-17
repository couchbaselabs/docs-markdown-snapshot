---
title: Kubernetes Automated Upgrade
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/concept-kubernetes-upgrade.adoc
  xref: xref:2.7@operator::concept-kubernetes-upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.7/concept-kubernetes-upgrade.html)

# Kubernetes Automated Upgrade

During your normal course of operations, you'll no doubt need to upgrade the Kubernetes cluster on which your Couchbase deployment resides. This page details the requirements and considerations that you'll need to take into account when performing an online upgrade of a Kubernetes cluster that's hosting a stateful application like Couchbase Server.

## [](#overview)Overview

The general procedure for upgrading a Kubernetes cluster starts with upgrading the Kubernetes master components (e.g. API, controllers, and database). This part of the upgrade should not affect the operation of existing Operator deployments or Couchbase cluster resources.

Once the upgrades to the master components are complete, the next step is to manually drain the Kubernetes nodes, one at a time, of their containers. After a node is completely drained, you can upgrade the `kubelet` component and make any other necessary hypervisor upgrades (e.g. security patching and kernel updates). Once the node has completed all of its upgrades, it can then be untainted and used again by Kubernetes to schedule and run pods on.

When upgrading Kubernetes nodes that are running Couchbase pods, there are certain requirements that you need to adhere to before and after each node has been drained. These requirements, detailed in the following sections, must be met for each node before you can move on to another node.

> [!IMPORTANT]
> The exact upgrade process is dependent on your Kubernetes installation method or cloud provider. Consult the relevant third-party documentation for full instructions.

## [](#operator-and-couchbase-cluster-considerations)Operator and Couchbase Cluster Considerations

Kubernetes provides some resources that help with upgrades to minimize disruption due to pods being evicted from Kubernetes nodes. Pod [disruption budgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/), for example, may limit the number of pods matching a rule that are allowed to be down at the same time. Pods cannot be evicted from a Kubernetes node if this limit is passed. Only once the number of _ready_ pods are within the specified tolerance, can evictions start again.

For a stateful application, like Couchbase Server, a pod being _ready_ (responding to API requests on the admin port) after it has been evicted and recreated by the Operator, does not mean that the environment is safe to evict another pod. Instead, you must ensure that all data is safely rebalanced and replicated across the Couchbase cluster before you can evict another. Failure to do so may result in data loss.

> [!NOTE]
> It is possible that multiple Couchbase Server pods may be resident on the same node that is being evicted. This depends on your specific deployment configuration. If the pods belong to the same cluster, they may need to be manually failed over via the [Couchbase Web Console](howto-ui.md) in order for the Operator to recover and rebalance.

The Operator itself is a stateless application typically managed by a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). When an Operator pod is evicted, the Deployment controller will automatically recreate a replacement pod that will begin managing `CouchbaseCluster` resources in its name space.

## [](#preparation-for-upgrade)Preparation for Upgrade

Before beginning an upgrade to your Kubernetes cluster, review the following considerations and prerequisites:

* Because an eviction deletes a pod, ensure that the Couchbase cluster is scaled correctly so that it can handle the increased load of having a pod down while a new pod is balanced into the cluster.
* To minimize disruption, ensure that a short failover period is configured with the [couchbaseclusters.spec.cluster.autoFailoverTimeout](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-autofailovertimeout) parameter to reduce down time before another node takes over the load.
* Ensure that there is [capacity](concept-sizing.md) in your Kubernetes cluster to handle the scheduling of replacement Couchbase pods. For example, if a Couchbase cluster were running on Kubernetes nodes marked exclusively for use by Couchbase, and anti-affinity were enabled as per the deployment [best practices](best-practices.md), the Kubernetes cluster would require at least one other node capable of scheduling and running your Couchbase workload. For clusters deployed with server group support, this would require another node per availability zone.

## [](#performing-the-upgrade)Performing the Upgrade

There are two supported methods for upgrading a Kubernetes cluster: Automatic and manual.

### [](#automatic-upgrade)Automatic Upgrade

To prevent downtime or a data loss scenario, the Operator provides controls for how automated Kubernetes upgrades proceed.

A `PodDisruptionBudget` is created for each `CouchbaseCluster` resource created. The `PodDisruptionBudget` specifies that at least the cluster size minus one node (N-1) be ready at any time. This constraint allows, at most, one node to be evicted at a time. As a result, it's recommended that to support an automatic Kubernetes upgrade, the cluster be deployed with anti-affinity enabled to guarantee only a single eviction at a time.

To ensure Couchbase Server nodes report that they are ready once they are added to the cluster and balanced in, the Kubernetes Pods are created with a [readiness gate](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate). The readiness gate is only set once all of the Couchbase Server nodes are balanced into the cluster and the cluster is in a stable condition that can tolerate the loss of a Pod without losing data.

### [](#manual-upgrade)Manual Upgrade

When you drain a Kubernetes node containing a Couchbase pod, the following sequence of events will occur:

* The Operator will detect that a cluster member is down. You should monitor this via the [Operator logs](howto-manage-operator-logging.md) or [Couchbase Web Console](howto-ui.md).
* The Couchbase pod will be failed over and the Operator will create a replacement pod in order to restore server class sizing.
* The Operator will initiate a rebalance to redistribute data across the cluster and restore redundancy constraints.

Only when the rebalance is successfully complete can you safely drain and upgrade another Kubernetes node containing a Couchbase pod belonging to the same Couchbase cluster.