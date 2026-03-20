---
title: What&#8217;s New?
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/whats-new.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.7@operator::whats-new.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.7/whats-new.html)

# What&#8217;s New?

Autonomous Operator 2.7 release provides full support for Couchbase Server 7.6, and several improvements to Pod Scheduling and Networking, as well as a number of minor fixes.

## [](#couchbase-server-7-6)Couchbase Server 7.6

See [What’s New in Version 7.6](../../server/7.6/introduction/whats-new.md) for full details, but the following new functionality is available in Operator 2.7, for clusters running Server 7.6:

* Data Service - Minimum Replica Count: Set with [couchbaseclusters.spec.cluster.data.minReplicasCount](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-data-minreplicascount).
* Data Service - Bucket Rank: Set with [couchbasebuckets.spec.rank](resource/couchbasebucket.md#couchbasebuckets-spec-rank).
* Index Service - File-based Rebalance: Enabled with [couchbaseclusters.spec.cluster.indexer.enableShardAffinity](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-indexer-enableshardaffinity).
* Auditing - Prune Rotated Logs: Set with [couchbaseclusters.spec.logging.audit.rotation.pruneAge](resource/couchbasecluster.md#couchbaseclusters-spec-logging-audit-rotation-pruneage).
* Cluster Arbiter (Serviceless) Nodes: Created by leaving [couchbaseclusters.spec.servers.services](resource/couchbasecluster.md#couchbaseclusters-spec-servers-services) empty.
* Backup - Backup and Restore Users and Groups: Set with [couchbasebackups.spec.services.users](resource/couchbasebackup.md#couchbasebackups-spec-services-users) and [couchbasebackuprestores.spec.services.users](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-services-users).
* Cross Data Center Replication (XDCR) - Connection Precheck: Called automatically when adding a Remote Cluster Reference.
* Data Service - Storage backend migration: Operator will automatically start the required Rebalances if it detects an unresolved Storage backend change. Storage Backend can also be configured using annotations, see [Bucket Backend Configuration](reference-annotations.md#bucket-backend-configuration) for more details.
* Authentication - LDAP Middlebox Compatibility Mode: Can now be disabled if needed via [couchbaseclusters.spec.security.ldap.middleboxCompMode](resource/couchbasecluster.md#couchbaseclusters-spec-security-ldap-middleboxcompmode).
* Data Service - Collections: [couchbasecollections.spec.maxTTL](resource/couchbasecollection.md#couchbasecollections-spec-maxttl) is now mutable. However, due to [K8S-3632](https://issues.couchbase.com/browse/K8S-3632), it is not possible to set `maxTTL` to `-1` to disable expiry for that Collection.

## [](#delta-recovery-in-place-upgrades)Delta Recovery / In-Place Upgrades

The `DeltaRecovery` upgrade process added in Operator 2.6 has been replaced by `InPlaceUpgrade`, to better reflect the actual behavior (not every Service can be Delta Recovered), and `DeltaRecovery` is now deprecated.

See [couchbaseclusters.spec.upgradeProcess](resource/couchbasecluster.md#couchbaseclusters-spec-upgradeprocess) for more details.

## [](#server-group-improvements)Server Group Improvements

In public cloud providers, it is common for the Server Groups in use to match the Availability Zones, and for there to be a small number of them. In private data centres they are more likely to be used to represent a larger number of zones, based on racks, rows of racks, or even rooms, as well as PDUs and switches.

To allow a more even spread of Pods over a larger range of Server Groups, we have added the `shuffleServerGroups` annotation.

To take advantage of there being more Server Groups available during Pod rescheduling, we have added the `rescheduleDifferentServerGroup` annotation .

See [Cluster Scheduling](reference-annotations.md#cluster-scheduling) for more details.

## [](#pod-rescheduling)Pod Rescheduling

By applying the `reschedule` annotation to a Couchbase Pod, the operator will detect it and reschedule the Pod based on the currently selected upgrade process. This allows Pods to be moved before any planned maintenance is performed on the Kubernetes Worker Nodes.

See [Pod Rescheduling](reference-annotations.md#pod-rescheduling) for more details.

## [](#improved-host-network-support)Improved Host Network Support

When the new `networking.improvedHostNetwork` annotation is enabled on a cluster, the Operator will skip SAN validation and will add the underlying Kubernetes hostname a Pod is running on to the alternate addresses list.

See [Host Network](reference-annotations.md#host-network) for more details.

## [](#more-granular-couchbase-server-upgrades)More Granular Couchbase Server Upgrades

Previously it was only possible to set a single Couchbase Server image for the entire `CouchbaseCluster` at [couchbaseclusters.spec.image](resource/couchbasecluster.md#couchbaseclusters-spec-image), triggering a cluster-wide upgrade. It is now possible to (optionally) set this at the Server Group/Server Class level, using [couchbaseclusters.spec.servers.image](resource/couchbasecluster.md#couchbaseclusters-spec-servers-image). This overrides the Cluster-level setting, allowing per-Group/per-Class upgrades.