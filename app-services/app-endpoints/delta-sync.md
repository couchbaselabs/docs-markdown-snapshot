---
title: Delta Sync
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/delta-sync.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:app-services::app-endpoints/delta-sync.adoc[]
---

[View original HTML](/app-services/app-endpoints/delta-sync.html)

# Delta Sync

![Delta Sync](../_images/app-endpoint/delta-sync.png) 

## [](#concepts)Concepts

Delta Sync provides the ability to replicate only those parts of a Couchbase document that have changed, syncing the document data across devices. Syncing only changed data can result in significant savings in bandwidth consumption as well as throughput improvements, especially useful where network bandwidth is constrained.

## [](#using-delta-sync)Using Delta Sync

You can enable Delta Sync per App Endpoint. To access Delta Sync, proceed through the following steps:

1. Select your desired App Endpoint.
2. Navigate to the **Settings** tab within App Endpoint settings.
3. Select the 'Delta Sync' configuration option.
4. Click the `Enable Delta Sync` checkbox.
5. Click the **Save** button to confirm your choice.

> [!NOTE]
> The App Endpoint will be offline when turning Delta Sync on or off.

## [](#storage-requirements)Storage Requirements

Storage of backed-up revision bodies means additional Couchbase Server storage space is required. This can lead to large storage requirements if you require multiple updates per day of large documents. For more information, see [Delta Sync on Sync Gateway](../../sync-gateway/current/sync/delta-sync.md).

## [](#see-also)See Also

* [Import Filters](import-filters.md)
* [Extended Attributes (XATTRs)](xattrs-for-app-services.md)
* [Cross-Origin Resource Sharing (CORS) Configuration](cors-configuration-for-app-services.md)
* [Configure App Endpoints](advanced-settings.md)
* [Create App Endpoints](creating-an-app-endpoint.md)