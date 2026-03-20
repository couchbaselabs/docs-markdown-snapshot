---
title: Resync your App Endpoint
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/resync.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:app-services::app-endpoints/resync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/resync.html)

# Resync your App Endpoint

All document changes made on the Couchbase Lite client app or on the Capella server are automatically synchronized with App Services. Every change is processed by the [Access Control function](access-control-data-validation.md).

If the Read Access Policies (defined in the Access Control function via [Channel assignments](../security/channels.md)) change on the server bucket, use the Resync feature to apply those changes to existing documents.

You can manage Resync of documents per collection within a scope. For more information, see [Scopes and Collections in App Endpoints](creating-an-app-endpoint.md#app-endpoint-sc).

## [](#basics)Basics

You can access the Access Control function from two locations:

* The ****Resync** button is on the Security tab in your App Endpoint settings, located in the Linked Collections table.

  * The ****Resync** button lets you resync one or multiple collections

> [!NOTE]
> Only one Resync can be in progress at a given time for a collection or a batch of collections.

* The ****Resync** button directly within the Access Control function of a given linked collection.

  * This button initiates the resync only on the selected linked collection.

To manually resync an App Endpoint, click on the ****Resync** button. If the App Endpoint is running, you will be prompted to ****Pause Endpoint** first. The resync will then proceed automatically. Once the resync is complete, you can ****Resume App Endpoint** from the same page.

> [!CAUTION]
> Resuming the App Endpoint cancels any ongoing Resync operation.

## [](#resync-considerations)Resync Considerations

If the Access Control Function is changed, App Services can reprocess all existing documents in the bucket to recalculate the routing and access assignments through a resync, but there are some situations when it is not necessary to do so:

* The modifications to your Access Control Function only impact write security and not routing or access.
* You only want the changes to channel or access rules to apply to documents written after the change was made.
* In the Resync state, no user’s full access privileges are known until all documents have been scanned.

> [!IMPORTANT]
> During the resync process the App Endpoint will be offline, during this period no end user requests will be processed, which will impact data synchronization between your mobile and IoT applications and Server.

## [](#see-also)See Also

* [Configure Access Control and Data Validation](access-control-data-validation.md)
* [Create App Endpoints](creating-an-app-endpoint.md)
* [Advanced Settings for App Endpoints](advanced-settings.md)