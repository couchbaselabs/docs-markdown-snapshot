---
title: Manage App Endpoints Lifecycle
description: Pause, resume, and delete App Endpoints for maintenance or to lower
  costs when the service is not required.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/configuring-app-endpoints.adoc
  xref: xref:app-services::app-endpoints/configuring-app-endpoints.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/configuring-app-endpoints.html)

# Manage App Endpoints Lifecycle

> Pause, resume, and delete App Endpoints for maintenance or to lower costs when the service is not required. 

For information about creating App Endpoints, see [Create an App Endpoint](#creating-an-app-endpoint.adoc).

## [](#resume-endpoint)Resume an App Endpoint

After creating an App Endpoint, it remains in an **Offline** state. You must resume the App Endpoint to make it available for client connections.

Before resuming your App Endpoint, configure the following:

* [Authentication provider](../security/set-up-authentication-provider.md)
* [Access control and data validation](access-control-data-validation.md) per collection
* [App users](../security/create-user.md) and [App roles](../security/create-app-role.md)
* [Advanced settings](advanced-settings.md) such as Delta Sync or Import Filters

To resume your App Endpoint:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name or expand and select the organization where you want to work with App Services.
  2. Click your current project name or search for the project where you want to work with App Services.
2. Go to **App Services**.
3. Select your App Service from the list.
4. Go to **App Endpoint**.
5. Click **Create App Endpoint**.
6. Select the App Service that contains your App Endpoint.
7. Go to **App Endpoints**.
8. Select your App Endpoint from the list.
9. Go to **Settings**.
10. Click **Resume App Endpoint**.

Your App Endpoint changes to an **Online** state and is now available for synchronization.

## [](#pause-endpoint)Pause an App Endpoint

You can pause an App Endpoint for maintenance or to lower costs when the service is not required.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name or expand and select the organization where you want to work with App Services.
  2. Click your current project name or search for the project where you want to work with App Services.
2. Go to **App Services**.
3. Select your App Service from the list.
4. Go to **App Endpoint**.
5. Click **Create App Endpoint**.
6. Select the App Service that contains your App Endpoint.
7. Go to **App Endpoints**.
8. Select your App Endpoint from the list.
9. Go to **Settings**.
10. Click **Pause App Endpoint**.

Your App Endpoint moves to an **Offline** state and stops accepting client connections.

To resume the App Endpoint, see [Resume an App Endpoint](#resume-endpoint).

## [](#delete-endpoint)Delete an App Endpoint

You can delete an App Endpoint entirely. Deleting an App Endpoint pauses it, then removes it permanently.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name or expand and select the organization where you want to work with App Services.
  2. Click your current project name or search for the project where you want to work with App Services.
2. Go to **App Services**.
3. Select your App Service from the list.
4. Go to **App Endpoint**.
5. Click **Create App Endpoint**.
6. Select the App Service that contains your App Endpoint.
7. Go to **App Endpoints**.
8. Select your App Endpoint from the list.
9. Go to **Settings**.
10. Click **Delete App Endpoint**.
11. Confirm that you want to delete the App Endpoint.

> [!IMPORTANT]
> Capella prevents you from deleting a bucket that is linked to an App Endpoint. To delete the associated bucket, you must delete the App Endpoint first.

## [](#see-also)See Also

* [Create an App Endpoint](#creating-an-app-endpoint.adoc)
* [About App Endpoints](about-app-endpoints.md)
* [Access Control and Data Validation](access-control-data-validation.md)
* [Advanced Settings](advanced-settings.md)