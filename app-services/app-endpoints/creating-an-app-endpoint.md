---
title: Create App Endpoints
description: Create an App Endpoint to synchronize data between Couchbase
  Capella and mobile or IoT applications.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/creating-an-app-endpoint.adoc
  xref: xref:app-services::app-endpoints/creating-an-app-endpoint.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/creating-an-app-endpoint.html)

# Create App Endpoints

> Create an App Endpoint to synchronize data between Couchbase Capella and mobile or IoT applications. 

## [](#prerequisites)Prerequisites

Before creating an App Endpoint, verify that you have:

* Created an [App Service](../app-services/creating-an-app-service.md).
* A [Memory and Disk](../../cloud/clusters/data-service/manage-buckets.md#%5Fbucket%5Ftypes) bucket available in the operational cluster linked to your App Service.
* Verified that your bucket has [maxTTL](../../cloud/clusters/data-service/manage-buckets.md#time-to-live) set to `0` (no bucket-level Time To Live configured).
* Verified that collections you plan to link have [maxTTL](../../cloud/clusters/data-service/scopes-collections.md#create-collection) set to `0` (no collection-level Time To Live configured).

> [!IMPORTANT]
> App Services does not support Time To Live (TTL) on buckets or collections linked to App Endpoints. Collection-level TTL can cause App Services' system documents (including those with `_sync` prefixes) to expire, which prevents synchronization from functioning correctly. If you need expiry behavior, set [expiration on individual documents](#cloud:clusters:data-service/document-expiration.adoc) or use per-collection sync functions.

## [](#create-an-app-endpoint)Create an App Endpoint

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name or expand and select the organization where you want to work with App Services.
  2. Click your current project name or search for the project where you want to work with App Services.
2. Go to **App Services**.
3. Select your App Service from the list.
4. Go to **App Endpoint**.
5. Click **Create App Endpoint**.
6. In the Create App Endpoint dialog, enter a name for your App Endpoint.
7. Select a `Memory and Disk` bucket and a scope.  
> [!NOTE]  
> The bucket must have **maxTTL** set to `0`. See [more about TTL restrictions](#ttl-restrictions).
8. Select 1 or more collections to link to your App Endpoint.  
> [!NOTE]  
> Collections must have **maxTTL** set to `0`. You can link a maximum of 250 collections from a scope to an App Endpoint in a single linking operation.App Endpoints can share scopes but cannot link to the same collections.  
> [!IMPORTANT]  
> Linking large numbers of collections can result in long linking times. During linking, you cannot connect to your App Endpoint and sync data.
9. Click **Create App Endpoint**.

Your App Endpoint enters an **Initializing** state while App Services links the collections. Once linking completes, the App Endpoint moves to an **Offline** state.

The default authentication provider is Basic Authentication. You can [configure a different authentication provider](../security/set-up-authentication-provider.md) after creation.

## [](#next-steps)Next Steps

After creating your App Endpoint:

1. Configure an [authentication provider](../security/set-up-authentication-provider.md) as the default is basic authentication.
2. Set up [access control and data validation](access-control-data-validation.md) per collection.
3. Create [app users](../security/create-user.md) and [app roles](../security/create-app-role.md).
4. Configure [advanced settings](advanced-settings.md) such as Delta Sync or Import Filters.
5. [Resume your App Endpoint](#configuring-app-endpoints.adoc#resume-endpoint) to an **Online** state to allow client connections.

For more information about App Endpoints, see [About App Endpoints](about-app-endpoints.md).