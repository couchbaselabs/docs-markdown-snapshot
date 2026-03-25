---
title: Couchbase Cluster Hibernation
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/concept-hibernation.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.5@operator::concept-hibernation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/concept-hibernation.html)

# Couchbase Cluster Hibernation

> The Operator allows a Couchbase cluster to be hibernated. This documents what hibernation means and the hibernation life-cycle. 

## [](#hibernation)Hibernation

Hibernation is the process of deactivating a Couchbase cluster.

When a cluster is put into hibernation with the [couchbaseclusters.spec.hibernate](resource/couchbasecluster.md#couchbaseclusters-spec-hibernate) attribute, all the pods associated with the cluster are terminated. How the pods are terminated, and under what conditions can be specified by the user with the [couchbaseclusters.spec.hibernationStrategy](resource/couchbasecluster.md#couchbaseclusters-spec-hibernationstrategy) attribute.

By hibernating a Couchbase cluster:

* Compute resources required by the cluster are released

  * This leads to cost savings when the cluster is not being used.
  * This leads to Kubernetes resources becoming available to be reused by other workloads.

When a cluster is hibernated, any persistent volumes associated with the cluster are retained. This allows the cluster to be recovered at the point of hibernation with existing data still intact.

### [](#hibernation-strategies)Hibernation Strategies

At present there is only one hibernation strategy:

Immediate hibernation

This immediately terminates any pods associated with the cluster. Any writes to the database that reside in a store queue, but not persisted to disk, will be lost. Any writes that must be persisted to disk should use durable writes that guarantee to the client the data has been persisted and potentially replicated.

## [](#waking-from-hibernation)Waking from Hibernation

A cluster that is hibernating can be awoken by setting [couchbaseclusters.spec.hibernate](resource/couchbasecluster.md#couchbaseclusters-spec-hibernate) to false, or removing that attribute. The cluster will be recovered in exactly the same way as it would from a total loss of all pods.

Ephemeral clusters—​with no persistent volumes—​will be recreated. Be aware that for ephemeral clusters, the cluster UUID will change, and will require XDCR clients to be reconfigured.

Persistent volume backed clusters will be recovered. The persistent metadata on the volumes will ensure the cluster is restored exactly as it was before hibernation.

Supportable clusters, with both volume backed and ephemeral server classes, will be first recovered from persistent volumes, then the ephemeral pods will be failed over and reprovisioned. When using this cluster topology, it is possible that Couchbase server will refuse to fail over ephemeral nodes. Automatic recovery can be enabled, in this situation, by setting the [couchbaseclusters.spec.recoveryPolicy](resource/couchbasecluster.md#couchbaseclusters-spec-recoverypolicy) attribute to `PrioritizeUptime`. This will allow the Operator to force failover of the affected pods, and then recover.

## [](#monitoring-hibernation)Monitoring Hibernation

The Operator updates the cluster conditions during the life cycle of a hibernation. This allows 3rd party observers to know when a cluster has hibernated fully. When completely hibernated all I/O to persistent volumes will have terminated and be in a stable state.