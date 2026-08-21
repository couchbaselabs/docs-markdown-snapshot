---
title: Resync your App Endpoint
pubDate: 2026-08-21T04:43:23.418Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/resync.adoc
  xref: xref:app-services::app-endpoints/resync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/resync.html)

# Resync your App Endpoint

## [](#concepts)Concepts

All document changes made on the Couchbase Lite client app or on the Capella server are automatically synchronized with App Services. Every change is processed by the [Access Control function](access-control-data-validation.md).

If the Read Access Policies (defined in the Access Control function via [Channel assignments](../security/channels.md)) change on the server bucket, use the Resync feature to apply those changes to existing documents.

You can manage Resync of documents per collection within a scope. For more information, see [Scopes and Collections in App Endpoints](creating-an-app-endpoint.md#app-endpoint-sc).

## [](#basics)Basics

You can access Resync from two locations:

* From the Linked Collections table:

  * Go to **Security** **Access and Validation**, select one or more collections in the **Linked Collections** table, and then click **Resync**.
* From a collection's Access Control page:

  * Click a collection name in the **Linked Collections** table to open its Access Control page, and then click **Resync**.
  * Initiates resync only on that linked collection.

> [!NOTE]
> Only one Resync can be in progress at a given time for a collection or a batch of collections.

To manually resync, select one or more linked collections and click ****Resync**.

## [](#pause-and-resync)Pause and Resync

If the App Endpoint is running, resyncing requires it to be paused first. You're prompted to confirm:

> [!NOTE]
> Pause App Endpoint and Resync
> 
> Resyncing now will pause your App Endpoint. Apps cannot connect to your App Endpoint during a resync.

Click ****Pause and Resync** to continue, or ****Cancel** to back out.

## [](#monitor-resync-progress)Monitor Resync Progress

Once you confirm, the App Endpoint status changes to **RESYNCING**, and an information panel appears above the collections list.

### [](#resync-in-progress)Resync in Progress

The panel displays:

* The number of linked collections being resynced.
* The number of documents processed and changed, against the estimated total, for example: `Processed 0 and changed 0 of ~3072 estimated documents.`

> [!NOTE]
> The estimated total is based on the number of documents in the collection at the start of the resync. This number does not update if documents are added to or removed from the collection while the resync is running.

Each linked collection being resynced shows an **App Endpoint resync in progress** status.

To cancel the operation before it finishes, click ****Stop Resync**.

> [!NOTE]
> If you stop a resync and start it again, the processed and changed document counts reset to zero.

### [](#resync-complete)Resync Complete

When the resync finishes, the panel updates to confirm completion, for example: `Document resync complete: 3072 documents processed.`

The App Endpoint remains **paused** after the resync completes. A banner reminds you that applications cannot connect to or access the endpoint until you resume it.

Click **Resume app endpoint** to bring it back online.

> [!CAUTION]
> Resuming the App Endpoint cancels any ongoing Resync operation.

Once resumed, the App Endpoint status returns to **ONLINE**, and a confirmation banner, **Successfully resumed App Endpoint**, appears.

Click the close icon (**x**) to dismiss any notification.

## [](#resync-considerations)Resync Considerations

If the Access Control Function is changed, App Services can reprocess all existing documents in the bucket to recalculate the routing and access assignments through a resync, but there are some situations when it is not necessary to do so:

* The modifications to your Access Control Function only impact write security and not routing or access.
* You only want the changes to channel or access rules to apply to documents written after the change was made.
* In the Resync state, no user's full access privileges are known until all documents have been scanned.

> [!IMPORTANT]
> During the resync process the App Endpoint will be offline. During this period no end user requests will be processed, which will impact data synchronization between your mobile and IoT applications and Server.

## [](#see-also)See Also

* [Configure Access Control and Data Validation](access-control-data-validation.md)
* [Create App Endpoints](creating-an-app-endpoint.md)
* [Advanced Settings for App Endpoints](advanced-settings.md)