---
title: Backup and Restore Considerations
description: How Cloud Native Gateway relates to Couchbase backup and restore
  operations, and what to consider for disaster recovery.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/availability-and-failover/pages/backup-restore-considerations.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:availability-and-failover:backup-restore-considerations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/availability-and-failover/backup-restore-considerations.html)

# Backup and Restore Considerations

> How Cloud Native Gateway relates to Couchbase backup and restore operations, and what to consider for disaster recovery. 

## [](#cloud-native-gateway-and-backup-operations)Cloud Native Gateway and Backup Operations

Cloud Native Gateway is a stateless translation layer. It does not store data, and it does not participate in backup or restore operations.

### [](#what-cloud-native-gateway-does-not-back-up)What Cloud Native Gateway Does Not Back Up

* **Cloud Native Gateway has no persistent state** \- Cloud Native Gateway does not maintain any data on disk. All cluster configuration, vBucket maps, and routing information are fetched dynamically from the Couchbase cluster at startup and updated in real time.
* **Connection state is ephemeral** \- Active client connections, in-flight requests, and rate limiter counters exist only in memory and are lost on restart. This is by design and does not affect data integrity.
* **Transaction state is transient** \- In-progress transaction state within Cloud Native Gateway is not persisted. If Cloud Native Gateway restarts, uncommitted transactions are cleaned up by Couchbase Server's background transaction cleanup process.

### [](#what-needs-to-be-backed-up)What Needs to Be Backed Up

The following items related to Cloud Native Gateway should be part of your backup strategy, but are managed outside of Cloud Native Gateway itself:

* **Couchbase Server data** — Use `cbbackupmgr`, the Couchbase Backup Service, or Couchbase Capella's backup functionality to back up bucket data. This is independent of Cloud Native Gateway.
* **Cloud Native Gateway configuration** — In Kubernetes, the `CouchbaseCluster` custom resource definition, Kubernetes Secrets (TLS certificates, credentials), and any associated NetworkPolicies or Service definitions should be managed through Infrastructure-as-Code (Helm charts, Kustomize, GitOps) and version-controlled.
* **TLS certificates** — Ensure your TLS certificates and private keys are stored in a secure, backed-up location (secrets manager, certificate management system).

## [](#restore-operations)Restore Operations

This section covers restoring Couchbase clusters and Cloud Native Gateway configurations after a backup.

### [](#restoring-the-couchbase-cluster)Restoring the Couchbase Cluster

When restoring a Couchbase cluster from backup:

1. Restore the Couchbase Server data using `cbbackupmgr` or the Backup Service.
2. Cloud Native Gateway instances automatically connect to the restored cluster (if the connection string and credentials remain valid).
3. Cloud Native Gateway discover the restored cluster's configuration, including buckets, scopes, collections, and topology.
4. Client applications can reconnect to Cloud Native Gateway and resume operations once the restore is complete.

No special Cloud Native Gateway steps are required during a restore operation.

### [](#restoring-to-a-new-cluster)Restoring to a New Cluster

If restoring to a new Couchbase cluster (different hostname or IP):

1. Deploy the new cluster and restore data.
2. Update Cloud Native Gateway's configuration to point to the new cluster:

  * In Kubernetes: update the `CouchbaseCluster` resource or Cloud Native Gateway's connection string.
  * In standalone mode: restart Cloud Native Gateway with the new `--cb-host` value.
3. Update client connection strings if the Cloud Native Gateway endpoint address has changed.

## [](#disaster-recovery)Disaster Recovery

Disaster recovery (DR) ensures business continuity by maintaining service availability during failures or disasters. This section describes how to implement disaster recovery strategies with Couchbase Server and Cloud Native Gateway.

### [](#active-passive-dr)Active-Passive DR

In an active-passive disaster recovery configuration:

1. The primary site runs Couchbase Server with Cloud Native Gateway.
2. The secondary site has a standby Couchbase cluster with XDCR replicating data from the primary.
3. Cloud Native Gateway instances on the secondary site are pre-deployed but may be idle (connected to the standby cluster).
4. During failover to the secondary site, update DNS or load balancer configuration to direct client traffic to the secondary Cloud Native Gateway endpoints.

Cloud Native Gateway does not require any special configuration for DR. The key consideration is ensuring that Cloud Native Gateway configuration (credentials, TLS certificates) on the secondary site matches the standby cluster.

### [](#cross-region-considerations)Cross-Region Considerations

For cross-region disaster recovery with Couchbase Capella or multi-site deployments:

* Each region has its own Cloud Native Gateway instances connected to the local Couchbase cluster.
* XDCR handles data replication between regions.
* Global DNS (Route53, Cloud DNS, Traffic Manager) or a global load balancer directs traffic to the appropriate region.
* Cloud Native Gateway instances in the failed region become unavailable; Cloud Native Gateway instances in the surviving region continue serving traffic against their local cluster.