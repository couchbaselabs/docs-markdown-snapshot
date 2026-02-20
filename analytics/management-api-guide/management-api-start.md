---
title: Get Started with the Capella Analytics Management API
description: To get started with the Capella Analytics Management API, you must
  create an API key. An API key authenticates and authorizes you to access the
  Capella Analytics Management API.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/management-api-guide/pages/management-api-start.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:management-api-guide:management-api-start.adoc[]
---

[View original HTML](/analytics/management-api-guide/management-api-start.html)

# Get Started with the Capella Analytics Management API

> To get started with the Capella Analytics Management API, you must create an API key. An API key authenticates and authorizes you to access the Capella Analytics Management API. 

This page is for Capella Analytics. For Capella operational, see [Get Started with the Management API](../../cloud/management-api-guide/management-api-start.md).

This page describes how to create and manage API keys for the Management API only.

To create an initial bootstrap API key to access the Management API, you must use the Capella UI. Once you have created an initial bootstrap API key, you can use the Management API itself to create further API keys.

## [](#understand-management-api-keys)Understand Management API Keys

Each API key for the Management API has the following characteristics:

* API keys are associated with Couchbase Capella roles and permissions.
* Every API key has an expiration date.
* Every API key is associated with an allowed IP Address list.

### [](#organization-roles-and-project-access)Organization Roles and Project Access

Each API key is associated with one or more organization roles, which determine the privileges that the API key has within the organization. For more information about organization roles, see [Organization Roles](../../cloud/organizations/organization-user-roles.md).

Each API key may have access to one or more projects, depending on the organization role. For each project, each API key is associated with one or more project roles, which determine the privileges that the API key has within each project. For more information about project roles, see [Project Roles](../../cloud/projects/project-roles.md).

You can create an API key at the level of an organization or a project.

* When you create an API key at the organization level, you may specify the organization roles for the API key, which projects the API key is associated with, and the project roles for the API key within each project.
* When you create an API key at the project level, the API key has the Organization Member role for the organization containing the project, and has access to the project where you created it. You may specify project roles for the API key within that project.

An API key must have the appropriate Capella roles to access an endpoint. The Management API reference guide lists the roles that are needed for each endpoint.

### [](#expiration)Expiration

By default, each API key expires 180 days after creation. You can specify a different expiration, or specify that the API key does not expire. For security, it’s recommended that you should let API keys expire and create new API keys regularly.

### [](#ip-access)IP Access

By default, when you first create an API key, you can use that API key to access the Management API from any IP address. For security, it’s recommended that each API key should only be able to access the Management API from specific IP addresses.

For each API key, you can grant access from:

* Individual IP addresses.
* Blocks of IP addresses using [CIDR notation](https://en.wikipedia.org/wiki/Classless%5FInter-Domain%5FRouting#CIDR%5Fnotation).

## [](#display-management-api-keys)Display Management API Keys

You can display Management API keys [within an organization](#display-keys-org) or [within a project](#display-keys-proj).

### [](#display-keys-org)Within an Organization

To display Management API keys within an organization:

1. In the navigation breadcrumbs in the Capella UI, click your organization name.
2. Go to **Settings** **API Keys**.

### [](#display-keys-proj)Within a Project

To display Management API keys within a project:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Projects**. Select the project where you want to see API keys.
  2. Click your current project name or search for the project where you want to see API keys.
2. Go to **Settings** **API Keys**.

The API keys for the Management API are displayed. If you have generated any API keys, they’re listed here. By default, there are no API keys for the Management API.

## [](#generate-management-api-keys)Generate Management API Keys

You can generate Management API keys [within an organization](#gen-keys-org) or [within a project](#gen-keys-proj).

### [](#gen-keys-org)Within an Organization

To generate a Management API key at the organization level:

1. Display the list of Management API keys [within the organization](#display-keys-org).
2. Click **Generate Key**.
3. In the **Key Name** field, enter a name for the API key.
4. (Optional) In the **Description** field, enter a description of the API key.
5. In the **Organization Roles** section, select one or more organization roles for the API key.
6. If the API key has the Organization Member role, configure the projects that the API key can access:

  1. Click **Configure Project Access**.
  2. Use the toggle controls to select each project which you want the API key to access, or click **Select all**.
  3. For each project which the API key can access, select one or more project roles for the API key.
  4. Click **Save**.

Now [specify other details](#gen-keys-cont) and download the Management API key.

### [](#gen-keys-proj)Within a Project

To generate a Management API key at the project level:

1. Display the list of Management API keys [within the project](#display-keys-proj).
2. Click **Generate Key**.
3. In the **Key Name** field, enter a name for the API key.
4. (Optional) In the **Description** field, enter a description of the API key.
5. Select one or more project roles for the API key.

Now [specify other details](#gen-keys-cont) and download the Management API key.

### [](#gen-keys-cont)Specify Details and Download the API Key

To specify other details and download the API key:

1. In the **Key Expiration** section, accept the default expiration, change the expiration, or specify that the key should not expire.
2. Specify IP access for the API key:

  1. Click **Add Allowed IP Address**.
  2. To allow a specific IP address or block, in the **Add IP / CIDR Block** field, enter the IP address or CIDR notation.
  3. To add your current IP address block, click **Add Current IP Address**.
  4. Click **Add**.
3. When you’re ready, click **Generate Key**.  
The Capella UI shows the new API key ID and the new API key secret. The API key secret is hidden to prevent others reading it.  
> [!WARNING]  
> You must copy or download the API key secret now. When you leave this page, you’ll not be able to copy or download the API key secret again.
4. To download the API key secret, click **Download Key**. The key is saved by your browser in a file called `<name>-api-key-token.txt`, where `<name>` is the name of the API key.
5. To copy either the API key ID or the API key secret to the clipboard, click the copy icon () next to the field.
6. When you have copied or downloaded the API key secret, click **Back to API Keys list**.

The API key is now listed with the Management API Keys.

## [](#view-management-api-keys)View Management API Keys

To view details of a Management API key:

1. Display the list of Management API keys [within an organization](#display-keys-org) or [within a project](#display-keys-proj).
2. Click the name of the API key.  
The details of the API key are displayed: the name, description, organization roles, expiration, allowed IP addresses, and project access.
3. When ready, click **Back to the API Keys list**.

## [](#delete-management-api-keys)Delete Management API Keys

To delete a Management API key:

1. Display the list of Management API keys [within an organization](#display-keys-org) or [within a project](#display-keys-proj).
2. Next to the API key you want to delete, click the trash can icon ().
3. In the confirmation dialog box, click in the provided text field and type `delete`.
4. Click **Delete**.

The API key is deleted.

## [](#next-steps)Next Steps

* To make an API call, see [Make an API Call with the Capella Analytics Management API](management-api-use.md).
* For a full reference guide, see [Capella Columnar Management API Reference](../management-api-reference/index.md).
* For an error reference, see [Capella Analytics Management API Errors](management-api-errors.md).