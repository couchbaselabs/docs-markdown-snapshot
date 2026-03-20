---
title: Sample Buckets
description: Sample buckets contain scopes, collections, and documents that are
  ready to be experimented with.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-settings/install-sample-buckets.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:manage:manage-settings/install-sample-buckets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/manage/manage-settings/install-sample-buckets.html)

# Sample Buckets

> Sample buckets contain scopes, collections, and documents that are ready to be experimented with. 

## [](#configuring-sample-buckets)Sample Buckets

Sample buckets contain data for experimental use. Sample buckets are referred to in code and command-line examples throughout Couchbase-Server documentation.

Full and Cluster administrators can install sample buckets with [Couchbase Web Console](#install-sample-buckets-with-the-ui) and the [REST API](#install-sample-buckets-with-the-rest-api).

### [](#scopes-collection-and-sample-buckets)Scopes, Collections, and Sample Buckets

Couchbase Server Version 7.0 introduces [Scopes and Collections](../../learn/data/scopes-and-collections.md), which allow data within a bucket to be organized according to type. Buckets created and used on previous versions of the server, after upgrade to 7.x, initially have all their data within the _default_ collection, which is itself within the _default_ scope. From this point, data can be selectively migrated from the default collection into other, administrator-defined collections.

Each sample bucket provided with 7.x contains its data _either_:

* Entirely within the default scope and collection. These buckets are `beer-sample` and `gamesim-sample`.
* Within multiple scopes and collections that have been pre-defined to exist in addition to the default scope and collection; _and_ within the default scope and collection also. This is the configuration provided for the `travel-sample` bucket. In total, _seven_ scopes exist within this bucket:

  * `_default`. This contains the `_default` collection; within which all documents reside. The `_default` collection therefore itself contains all documents that existed in pre-7.0 versions of the `travel-sample` bucket.
  * `inventory`. This also contains all documents that existed in pre-7.0 versions of the `travel-sample` buckets, but in a different configuration: here, the documents are distributed, according to type, across five collections; which are named `airline`, `airport`, `landmark`, `hotel`, and `route`.
  * `tenant_agent_00` to `tenant_agent_04`. Each of these five scopes contains two collections; which are named `users` and `bookings`.

Since all three sample buckets contain, in their default collection, all data they held in pre-7.0 versions of Couchbase Server, programs written to access this data in its original locations will be able to continue doing so with minimal adjustment. All three buckets can also be used for experiments with _migration_, whereby the data is selectively redistributed into administrator-created collections. See [Migrate Data to a Collection with the UI](../manage-xdcr/replicate-using-scopes-and-collections.md#migrate-data-to-a-collection-with-the-ui).

The `travel-sample` bucket contains travel-related data already in migrated form, within the collections in the scope `inventory`. The bucket can thus be used for immediate experimentation with application-access to scopes and collections.

The `travel-sample` bucket also contains data within the `tenant_agent` scopes, which is appropriate for experimentation with _multi-tenancy-based_ application access.

## [](#install-sample-buckets-with-the-ui)Install Sample Buckets with the UI

From the **Settings** screen, select the **Sample Buckets** tab. The **Sample Buckets** screen now appears, as follows:

![settings samples](../_images/manage-settings/settings-samples.png) 

Note that if one or more sample buckets have already been loaded, they are listed under the **Installed Samples** section of the page.

For information on assigning roles to users, so as to enable them to access sample buckets following installation, see [Manage Users and Roles](../manage-security/manage-users-and-roles.md).

To install, select one or more sample buckets from the displayed list, using the checkboxes provided. For example, select the `travel-sample` bucket:

![select travel sample bucket](../_images/manage-settings/select-travel-sample-bucket.png) 

If there is insufficient memory available for the specified installation, a notification appears at the lower left of Couchbase Web Console:

![insufficientRamWarning](../_images/manage-settings/insufficientRamWarning.png) 

For information on configuring memory quotas, see the information on [General](general-settings.md) settings. For information on managing (including deleting) buckets, see [Manage Buckets](../manage-buckets/bucket-management-overview.md).

If and when you have sufficient memory, click **Load Sample Data**.

![loadSampleDataButton](../_images/manage-settings/loadSampleDataButton.png) 

When installed, the sample bucket is listed under the **Installed Samples** section of the page. It also appears in the **Buckets** screen, where its definition can be edited. See [Manage Buckets](../manage-buckets/bucket-management-overview.md), for information.

## [](#install-sample-buckets-with-the-rest-api)Install Sample Buckets with the REST API

To install sample buckets with the REST API, use the `POST /sampleBuckets/install` HTTP method and URI, as follows:

curl -X POST -u Administrator:password \
http://10.143.194.101:8091/sampleBuckets/install \
-d '["travel-sample", "beer-sample"]'

If successful, the call returns an empty list.

For further information on using the REST API, including details of how to retrieve a list of currently available sample buckets, see [Managing Sample Buckets](../../rest-api/rest-sample-buckets.md). For information on _deleting_ buckets (including sample buckets), see [Deleting Buckets](../../rest-api/rest-bucket-delete.md).