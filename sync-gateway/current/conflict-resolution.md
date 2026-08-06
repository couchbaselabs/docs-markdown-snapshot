---
title: Conflict Resolution
description: How Sync Gateway resolves document conflicts during synchronization
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/ROOT/pages/conflict-resolution.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway::conflict-resolution.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/conflict-resolution.html)

# Conflict Resolution

> How Sync Gateway resolves document conflicts during synchronization  

Related _Sync_ topics: [Conflict Resolution](conflict-resolution.md) | [Bootstrap Configuration](configuration/configuration-schema-bootstrap.md)

## [](#overview)Overview

Starting with Sync Gateway 4.0+, the default conflict resolution strategy has changed from **Most Write Wins** (MWW) to **Last Write Wins** (LWW):

* **Most Write Wins**: The source (device/cluster) with more changes to a document wins in conflicts
* **Last Write Wins**: Timestamp-based resolution where the document with the latest timestamp wins

This fundamental change aligns with the shift from revision trees to version vectors and enables better consistency across distributed deployments.

Conflicts are automatically resolved \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] using deterministic algorithms that verify consistency across all participating nodes.

## [](#conflict-resolution-strategies)Conflict Resolution Strategies

### [](#last-write-wins-default-in-4-0)Last Write Wins (Default in 4.0+)

Last Write Wins uses hybrid logical clock timestamp comparison to resolve conflicts deterministically. The document with the latest timestamp wins the conflict, with timestamps generated using version vectors and Hybrid Logical Vectors (HLV) for accurate ordering.

This strategy provides:

* Deterministic conflict resolution across all clusters
* Consistency with XDCR [timestamp-based conflict resolution](../../server/current/learn/clusters-and-availability/xdcr-conflict-resolution.md#timestamp-based-conflict-resolution)
* Better support for active-active deployments
* Alignment with modern distributed systems practices

Timestamp accuracy depends on clock synchronization. XDCR deployments expect server clocks to remain synchronized (see [Time Synchronization](../../server/current/learn/clusters-and-availability/xdcr-conflict-resolution.md#time-synchronization)). Mobile devices may have unsynchronized clocks, but each Couchbase Lite instance maintains its own Hybrid Logical Clock that captures relative time, providing sufficient accuracy for conflict resolution.

### [](#most-write-wins-versions-4-0)Most Write Wins (Versions < 4.0+)

Sync Gateway uses Most Write Wins conflict resolution in the following scenarios:

* Sync Gateway 4.0+ replicating with Couchbase Lite < 4.0+ clients
* Sync Gateway 4.0+ replicating with Sync Gateway < 4.0+ instances via Inter-Sync Gateway Replication
* Cross-version compatibility scenarios

In these cases, the document with the most revisions wins the conflict, maintaining backward compatibility.

> [!NOTE]
> For Sync Gateway versions less than 4.0+, Most Write Wins is the default behavior. See [Upgrading Sync Gateway](upgrading.md) for upgrade instructions.

## [](#xdcr-integration)XDCR Integration

For active-active deployments using XDCR with Sync Gateway 4.0+, configure your Couchbase Server buckets to use **Timestamp-based** conflict resolution to match Sync Gateway's Last Write Wins behavior.

> [!IMPORTANT]
> This configuration has significant constraints:

* The conflict resolution strategy must be chosen when the bucket is created and cannot be changed later
* Both sides of an XDCR replication must have matching conflict resolution strategies
* This is only feasible for new deployments, not existing ones

For detailed information about configuring XDCR conflict resolution, see [Choosing a Conflict Resolution Policy](../../server/current/learn/clusters-and-availability/xdcr-conflict-resolution.md#choosing%5Fa%5Fconflict%5Fresolution%5Fpolicy).

When properly configured, this ensures consistent conflict resolution across: \* Sync Gateway ↔ Couchbase Lite replication \* XDCR bucket-to-bucket replication \* Mixed mobile and server-side application scenarios

See [BI-directional XDCR with Mobile Clusters](server-compatibility/server-compatibility-xdcr-mobile.md) for detailed configuration guidance.

## [](#platform-specific-documentation)Platform-Specific Documentation

The Couchbase Lite SDK guides describe how automatic conflict resolution works on each platform:

[Swift](../../couchbase-lite/current/swift/conflict.md) | [Java](../../couchbase-lite/current/java/conflict.md) | [Java (Android)](../../couchbase-lite/current/android/conflict.md) | [C#](../../couchbase-lite/current/csharp/conflict.md) | [Objective-C](../../couchbase-lite/current/objc/conflict.md)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](access-control/sync-function/sync-function.md)
* [Import filter](sync/import-processing.md)
* [Access Control](configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api/rest-api.md)
* [Admin REST API](rest-api/rest-api-admin.md)
* [Metrics REST API](rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)

---

[1](#%5Ffootnoteref%5F1). Since Couchbase Lite 2.0