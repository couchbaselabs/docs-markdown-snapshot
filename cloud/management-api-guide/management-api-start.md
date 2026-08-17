---
title: Get Started with the Capella Operational Management API
description: To get started with the Couchbase Capella Operational Management
  API, you must create an API key. An API key authenticates and authorizes you
  to access the Management API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/management-api-guide/pages/management-api-start.adoc
  xref: xref:cloud:management-api-guide:management-api-start.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/management-api-guide/management-api-start.html)

# Get Started with the Capella Operational Management API

> To get started with the Couchbase Capella Operational Management API, you must create an API key. An API key authenticates and authorizes you to access the Management API. 

This page is for Capella operational. For the Couchbase AI Data Plane, see [Get Started with the Couchbase AI Data Plane APIs](../../ai/api-guide/api-start.md). For Capella Analytics, see [Get Started with the Capella Analytics Management API](../../analytics/management-api-guide/management-api-start.md).

This page describes how to create and manage API keys for the Management API only.

To create an initial bootstrap API key to access the Management API, you must use the Capella UI. Once you have created an initial bootstrap API key, you can use the Management API itself to create further API keys.

## [](#understand-management-api-keys)Understand Management API Keys

Each API key for the Management API has the following characteristics:

* API keys are associated with Couchbase Capella roles and permissions.
* Every API key has an expiration date.
* Every API key is associated with an allowed IP address list.

### [](#organization-roles-and-project-access)Organization Roles and Project Access

Each API key is associated with 1 or more organization roles, which determine the privileges that the API key has within the organization. For more information about organization roles, see [Organization Roles](../organizations/organization-user-roles.md).

Each API key may have access to 1 or more projects, depending on the organization role. For each project, each API key is associated with 1 or more project roles, which determine the privileges that the API key has within each project. For more information about project roles, see [Project Roles](../projects/project-roles.md).

You can create an API key at the organization or a project level:

* When you create an API key at the organization level, you may specify the organization roles for the API key, which projects the API key is associated with, and the project roles for the API key within each project.
* When you create an API key at the project level, the API key has the [Organization Member](../organizations/organization-user-roles.md#organization-role-member) role for the organization containing the project, and has access to the project where you created it. You may specify project roles for the API key within that project.

An API key must have the appropriate Capella roles to access an endpoint. The [Management API reference guide](../management-api-reference/index.md) lists the roles that are needed for each endpoint.

### [](#expiration)Expiration

By default, each API key expires 180 days after creation. You can specify a different expiration, or specify that the API key does not expire. For security, create new API keys regularly and let old API keys expire after transitioning to the new keys.

### [](#ip-access)IP Access

By default, when you first create an API key, you can use that API key to access the Management API from any IP address. For security, each API key should only be able to access the Management API from specific IP addresses.

For each API key, you can grant access from:

* Individual IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format.
* Blocks of IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format using [CIDR notation](https://en.wikipedia.org/wiki/Classless%5FInter-Domain%5FRouting#CIDR%5Fnotation).

## [](#display-keys)Display Management API Keys

You can display Management API keys within an organization or within a project. By default, there are no API keys for the Management API.

* Organization Level
* Project Level

To display Management API keys within an organization:

1. In the Capella UI, click your initials.
2. Click **Organizations**.
3. Select the organization you want to create API keys for.
4. Go to **Settings** **API Keys**.

To display Management API keys within a project:

1. In your organization, go to **Projects**.
2. Select the project you want to create API keys for.
3. Go to **Settings** **API Keys**.

## [](#generate-keys)Generate Management API Keys

You can generate Management API keys within an organization or within a project.

* Organization Level
* Project Level

To generate a Management API key at the organization level:

1. Display the list of Management API keys [within the organization](#display-keys).
2. Click **Generate Key**.
3. In the **Key Name** field, enter a name for the API key.
4. (Optional) In the **Description** field, enter a description of the API key.
5. In **Organization Roles**, select 1 or more organization roles for the API key.
6. If the API key has the `Organization Member` role, configure the projects that the API key can access:

  1. Click **Configure Project Access**.
  2. Enable the projects you want the API key to access, or click **Select all**.
  3. For each project which the API key can access, select 1 or more [project roles](../projects/project-roles.md) for the API key.
  4. Click **Save**.
7. In **Key Expiration**, accept the default expiration, change the expiration, or specify that the key should not expire.
8. In **Allowed IP Addresses**, click **Added Allowed IP Address** to specify IP access for the API key.
9. Select 1 of the following options:

  1. To allow a specific IP address or block, in the **Add IP / CIDR Block** field, enter the IP address or CIDR notation.
  2. To add your current IP address block, click **Add Current IP Address**.
10. Click **Add**.
11. When you're ready, click **Generate Key**.  
The Capella UI shows the new API key ID and the new API key token. The API key token is hidden to prevent others reading it.  
> [!WARNING]  
> You must copy or download the API key token now. When you leave this page, you will not be able to copy or download the API key token again.
12. To download the API key token, click **Download Key**. The key is saved by your browser in a file called `<name>-api-key-token.txt`, where `<name>` is the name of the API key.
13. To copy either the API key ID or the API key token to the clipboard, click the copy icon () next to the field.

To generate a Management API key at the project level:

1. Display the list of Management API keys [within the project](#display-keys).
2. Click **Generate Key**.
3. In the **Key Name** field, enter a name for the API key.
4. (Optional) In the **Description** field, enter a description of the API key.
5. In **Roles**, select 1 or more [project roles](../projects/project-roles.md) for the API key.
6. In the **Key Expiration**, accept the default expiration, change the expiration, or specify that the key should not expire.
7. In **Allowed IP Addresses**, click **Added Allowed IP Address** to specify IP access for the API key.
8. Select 1 of the following options:

  1. To allow a specific IP address or block, in the **Add IP / CIDR Block** field, enter the IP address or CIDR notation.
  2. To add your current IP address, click **Add Current IP Address**.
9. Click **Add**.
10. When you're ready, click **Generate Key**.  
The Capella UI shows the new API key ID and the new API key token. The API key token is hidden to prevent others reading it.  
> [!WARNING]  
> You must copy or download the API key token now. After leaving this page, you cannot copy or download the API key token.
11. To download the API key token, click **Download Key**. The key is saved by your browser in a file called `<name>-api-key-token.txt`, where `<name>` is the name of the API key.
12. To copy either the API key ID or the API key token to the clipboard, click the copy icon () next to the field.

## [](#view-management-keys)View Management API Keys

To view details of a Management API key:

1. Display the list of Management API keys [within an organization or within a project](#display-keys).
2. Click the name of the API key.  
The details of the API key are displayed: the name, description, organization roles, expiration, allowed IP addresses, and project access.

## [](#delete-management-keys)Delete Management API Keys

To delete a Management API key:

1. Display the list of Management API keys [within an organization or within a project](#display-keys).
2. Next to the API key you want to delete, click the trash can icon ().
3. In the confirmation dialogue, confirm that you want to delete the API key.
4. Click **Delete**.

## [](#next-steps)Next Steps

* To make an API call, see [Make an API Call with the Capella Operational Management API](management-api-use.md).
* For a full reference guide, see [Capella Operational Management API Reference](../management-api-reference/index.md).
* For an error reference, see [Capella Operational Management API Errors](management-api-errors.md).