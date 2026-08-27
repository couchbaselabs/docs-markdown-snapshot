---
title: Prepare for XDCR
description: Before setting up a replication, make sure you have the appropriate
  administrative roles.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-xdcr/prepare-for-xdcr.adoc
  xref: xref:server:manage:manage-xdcr/prepare-for-xdcr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-xdcr/prepare-for-xdcr.html)

# Prepare for XDCR

> Before setting up a replication, make sure you have the appropriate administrative roles. Then, make sure your cluster is appropriately configured and provisioned. 

## [](#establish-roles-for-xdcr)Establish Roles for XDCR

Couchbase Server enforces _Role-Based Access Control_. This means that to access specific system-resources, corresponding _privileges_ are required. Privileges have a fixed association with _roles_, which are assigned to _users_.

Full information on Role-Based Access Control is provided in [Authorization](../../learn/security/authorization-overview.md). If you possess the role of _Full_, _Cluster_, or _XDCR Administrator_, you can create, edit, and delete cluster references and replications.

## [](#prepare-your-cluster-for-XDCR)Prepare Your Cluster for XDCR

Before beginning XDCR management:

* Configure all nodes within the source cluster so that they can individually communicate over the network to all nodes within the target cluster.
* Ensure that all Couchbase Server platforms match. For instance, if you want to replicate from a Linux-based cluster, you need to do so with another Linux-based cluster.
* Confirm that your cluster is properly sized, and is able to handle new XDCR streams. For example, XDCR needs 1-2 additional CPU cores per stream; and in some cases, will require additional RAM and network resources as well. If a cluster is not sized to handle _both_ the existing workload _and_ the new XDCR streams, the performance of both XDCR and the cluster overall may be negatively impacted.
* Couchbase Server uses TCP/IP port `8091` to exchange cluster configuration information. If you are communicating with a destination cluster over a dedicated connection, or over the Internet, ensure that all nodes in the destination and source clusters can communicate with each other over port `8091`.

> [!NOTE]
> Versions of Couchbase Server before 8.0 do not support XDCR replication between buckets with different numbers of vBuckets. They also do not support Magma buckets with 128 vBuckets. Due to both these limitations, you cannot replicate from a pre-8.0 cluster to a Magma bucket with 128 vBuckets. You can replicate in the opposite direction (from a Magma bucket with 128 vBuckets to a pre-8.0 cluster) because Magma buckets on Couchbase Server 8.0 and later can replicate to buckets with a different number of vBuckets. However, you should avoid doing so because bidirectional replication is impossible in this configuration.

## [](#next-xdcr-steps-after-preparation)Next Steps

Once your source and target clusters have been prepared, to start XDCR management, [Create a Reference](create-xdcr-reference.md).