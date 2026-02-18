---
title: XDCR Active-Active and Eventing
description: Understand how to safely use Couchbase Eventing functions in
  bi-directional XDCR environments, including Sync Gateway 4.0 compatibility.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/server-compatibility/pages/xdcr-active-active-eventing.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/server-compatibility/xdcr-active-active-eventing.html)

# XDCR Active-Active and Eventing

> Understand how to safely use Couchbase Eventing functions in bi-directional XDCR environments, including Sync Gateway 4.0 compatibility.  
> Learn how to design Couchbase Eventing functions to avoid replication loops and conflicts in active-active XDCR environments with Sync Gateway 4.0.

_Related topics_: [Buckets](server-compatibility-buckets.md) | [Collections](server-compatibility-collections.md) | [Eventing](server-compatibility-eventing.md) | [Transactions](server-compatibility-transactions.md) | [XDCR](server-compatibility-xdcr.md) | [Backup and restore](server-compatibility-backups.md)

_Other Topics_: [Compatibility Matrix](../product-notes/compatibility.md)

## [](#introduction)Introduction

With sync gateway 4.0, you can use [Couchbase Server Cross Data Center Replication](../../../server/current/learn/clusters-and-availability/xdcr-overview.md) (XDCR) alongside Eventing functions to process or enrich documents.

However, in active-active XDCR environments, improper function design can create "replication" loops and data "conflicts" that compromise cluster stability.

## [](#overview)Overview

Active-active XDCR replicates documents bidirectionally between clusters. Eventing functions deployed on both ends of this replication topology must avoid reprocessing updated documents in a way that causes XDCR to ping-pong and never stop replicating.

The following issues can arise:

* You must design Eventing functions that properly modify documents in replicated buckets.
* Without protection logic, these functions can create infinite replication loops.
* This typically occurs when you deploy the same Eventing function that updates the source documents on both of the clusters in an active-active replication topology.

## [](#understanding-the-replication-loop-issue)Understanding the Replication Loop Issue

### [](#lbl-eventing-loop-example)Example: Enriching IP Address Documents

Consider this example function, based on `case_2_enrich_ips` from the [Couchbase Eventing documentation](../../../server/current/eventing/eventing-example-data-enrichment.md):

The `case_2_enrich_ips` function, on mutation of a document, enriches the mutated document in the same collection with additional fields, `ip_num_start` and `ip_num_end`.

```javascript
function OnUpdate(doc, meta) {
    log('document seen', doc);

    doc["ip_num_start"] = get_numip_first_3_octets(doc["ip_start"]);
    doc["ip_num_end"] = get_numip_first_3_octets(doc["ip_end"]);
    log('document updated to', doc);
    src[meta.id] = doc;
}

function get_numip_first_3_octets(ip) {
    var return_val = 0;
    if (ip) {
        var parts = ip.split('.');
        return_val = (parts[0] * (256 * 256 * 256)) + (parts[1] * (256 * 256)) + (parts[2] * 256) + parseInt(parts[3]);
        return return_val;
    }
}
```

When deployed on both clusters, this function continuously reprocesses the same document:

Cluster Logs – Cluster 1

```console
... "document seen" {"ip_start":"5.62.60.1", ...}
... "document updated to" {"ip_num_start":87964673, ...}
... "document seen" {"ip_num_start":87964673, ...}
```

Cluster Logs – Cluster 2

```console
... "document seen" {"ip_start":"5.62.60.1", ...}
... "document updated to" {"ip_num_start":87964673, ...}
```

This behavior repeats indefinitely due to the mutual triggering of updates.

## [](#preventing-redundant-updates)Preventing Redundant Updates

### [](#lbl-prevent-redundant)Basic Protection: Field Presence Check

One way to avoid loops is to check whether the document has already been enriched. The OnUpdate Eventing function below includes a check at the top to return if the additional fields already exist in the document.

```javascript
function OnUpdate(doc, meta) {
    log('document seen', doc);

    if ('ip_num_start' in doc || !('ip_start' in doc)) return;

    doc["ip_num_start"] = get_numip_first_3_octets(doc["ip_start"]);
    doc["ip_num_end"] = get_numip_first_3_octets(doc["ip_end"]);
    log('document updated to', doc);
    src[meta.id] = doc;
}
```

This eliminates infinite replication, but may still lead to race conditions and conflicts due to update timing.

## [](#preventing-conflicts-with-location-based-logic)Preventing Conflicts with Location-Based Logic

### [](#lbl-location-check)Advanced Protection: Cluster Identifier Check

A better solution introduces a per-cluster ID (e.g., `DC1`, `DC2`) to conditionally apply transformations.

```javascript
function OnUpdate(doc, meta) {
    log('document seen', doc);
    var local = "DC1";

    if ('ip_num_start' in doc || !('ip_start' in doc)) return;

    if (doc["update_location"] == local) {
        doc["ip_num_start"] = get_numip_first_3_octets(doc["ip_start"]);
        doc["ip_num_end"] = get_numip_first_3_octets(doc["ip_end"]);
        log('document updated to', doc);
        src[meta.id] = doc;
    }
}
```

This approach ensures that only the originating cluster updates the document, eliminating conflicts and loops.

When designing Eventing functions for active-active XDCR environments, consider these approaches:

* State Checks: Avoid updates if fields already exist.
* Use consistent, location-based rules to guide execution.
* Validate field presence and document structure.
* Single-Cluster Deployment: Run Eventing only on one cluster and let XDCR replicate the processed documents to other clusters.
* Dedicated Buckets: Use isolated buckets for processing that are not part of the XDCR replication configuration.
* External Transformations: Offload complex transformations to external services.

### [](#testing-and-monitoring)Testing and Monitoring

* **Simulate in Dev**: Mirror active-active setups in a development environment.
* **Monitor Logs**: Review logs after deployment to verify expected behavior.
* **Gradual Deployment**: Introduce changes incrementally, testing at each step.
* **Document Dependencies**: Inform app teams about required fields like `update_location`.

> [!IMPORTANT]
> Without proper logic, Eventing functions in active-active XDCR environments may create infinite loops that consume excessive resources and destabilize the system.
> 
> These issues apply to all Couchbase versions with Eventing and XDCR support, and are now relevant with Sync Gateway 4.0 support for Bidirectional XDCR.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](../access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)