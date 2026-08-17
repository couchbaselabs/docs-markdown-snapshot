---
title: About App Endpoints
description: Learn about App Endpoints, how they work, and how to configure them
  in Couchbase Capella.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/about-app-endpoints.adoc
  xref: xref:app-services::app-endpoints/about-app-endpoints.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/about-app-endpoints.html)

# About App Endpoints

> Learn about App Endpoints, how they work, and how to configure them in Couchbase Capella. 

An App Endpoint represents an instance of your application on App Services.

## [](#key-concepts)Key Concepts

* An App Service can have multiple App Endpoints.
* Each App Endpoint links to 1 `Memory and Disk` bucket, 1 scope, and at least 1 collection.
* App Endpoints synchronize data between Capella and mobile or IoT devices.
* App Endpoints can share scopes but cannot link to the same collections.
* Each App Endpoint handles data synchronization, security, and RBAC for your application.

## [](#linking-collections)Linking Collections

When you link collections to an App Endpoint, you make them mobile-aware. This allows you to sync collection data from cloud to edge for use in your mobile and IoT applications. You can only use data from collections linked to your App Endpoint within your mobile and IoT applications.

App Endpoints can share scopes but cannot link to the same collections. You can link a maximum of 250 collections from a scope to an App Endpoint in a single linking operation.

For more information about use cases of scopes and collections, see the [Scopes and Collections Support in Couchbase Mobile blog post](https://www.couchbase.com/blog/scopes-collections-couchbase-mobile/).

## [](#collection-level-configuration)Collection-Level Configuration

From App Services version 3.1.8, you can configure the following settings at the collection level:

* [Access Control and Data Validation](access-control-data-validation.md) \- Customize RBAC rules per collection
* [Resync](resync.md) \- Resync documents per collection or batch of collections
* [Import Filters](import-filters.md) \- Configure import filters per collection

> [!IMPORTANT]
> You can find advanced settings, such as [Delta Sync](delta-sync.md) or [Import Filters](import-filters.md), in the [advanced settings menu](advanced-settings.md) in the Capella UI.

For more information about scopes and collections, see [Buckets, Scopes and Collections](../../cloud/clusters/data-service/about-buckets-scopes-collections.md) in the Capella operational documentation.

## [](#eventing-compatibility)Eventing Compatibility

The [Eventing Service](../../cloud/eventing/eventing-overview.md) can run 1 or more Eventing Functions in your operational cluster to handle data changes according to a real-time Event-Condition-Action model. You can create Eventing Functions that can read and write data from a keyspace (bucket, scope, or collection) that's linked to an App Endpoint.

App Services 3.2.2 or later is fully compatible with Eventing on operational clusters using Couchbase Server 7.6.5 or later.

When [creating Eventing Functions](../../cloud/eventing/add-eventing-functions.md) to use with App Services, you must select **Enable App Services Compatibility**.

## [](#app-endpoint-states)App Endpoint States

App Endpoints can be in 1 of the following states:

**Initializing**

App Services is linking 1 or more collections. You can update configuration, link collections, unlink collections, or change the authentication provider. You cannot create app users, app roles, or perform data synchronization.

**Offline**

Collections have finished linking, but the endpoint is not accepting client connections. You can continue configuration or resume the endpoint to an **Online** state.

**Online**

The App Endpoint is available for clients to connect and synchronize data.

**Resyncing**

The sync function reprocesses all documents linked to the App Endpoint. This occurs when you trigger a resync operation to reapply access control rules or update channel assignments.

### [](#state-transitions)State Transitions

* When you create an App Endpoint, it enters **Initializing** while linking collections.
* After linking completes, it moves to **Offline**.
* You must manually resume the endpoint to move it to **Online**.
* If you link or unlink collections on an existing endpoint, it returns to its previous state after the operation completes.

## [](#see-also)See Also

* [Create App Endpoints](#creating-an-app-endpoint.adoc)
* [Advanced Settings](advanced-settings.md)
* [Access Control and Data Validation](access-control-data-validation.md)
* [Couchbase Server - Scopes and Collections](../../server/current/learn/data/scopes-and-collections.md)