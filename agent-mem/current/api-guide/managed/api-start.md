---
title: Get Started with the Agent Memory APIs
description: To get started with the Couchbase Capella APIs for Agent Memory,
  you must create an API key. An API key authenticates and authorizes you to
  access the APIs.
pubDate: 2026-10-31T04:25:29.610Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/api-guide/pages/managed/api-start.adoc
  xref: xref:agent-mem:api-guide:managed/api-start.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/api-guide/managed/api-start.html)

# Get Started with the Agent Memory APIs

> To get started with the Couchbase Capella APIs for Agent Memory, you must create an API key. An API key authenticates and authorizes you to access the APIs. 

This page covers all changes for the Agent Memory API and the Couchbase Capella Management API. The Management API includes features for [Capella Operational](../../../../cloud/management-api-guide/management-api-intro.md), [Capella App Services](../../../../app-services/management-api-guide/management-api-intro.md), [Operational Insights Capella](../../../../operational-insights-cloud/management-api-guide/management-api-intro.md), and [AI Data Plane](../../../../ai/api-guide/api-intro.md).

This page describes how to manage:

* [API keys for the Management API](#management-api-keys).
* [Agent Memory API keys for the Agent Memory API](#agent-memory-keys).
* [Agent Memory server endpoints](#agent-memory-endpoint).
* [Allowed IP addresses for your Agent Memory servers](#agent-memory-allowed-ips).

Use the Management API to deploy and manage Agent Memory servers and Agent Memory API keys. Use the Agent Memory API to store and retrieve memory on your Agent Memory server.

## [](#management-api-keys)Management API Keys

To create an initial bootstrap API key to access the Management API, you must use the [Capella UI](#generate-keys). Once you have created an initial bootstrap API key, you can use the [Management API](../../../../cloud/management-api-reference/index.md#tag/Api-Keys) itself to create further API keys.

### [](#understand-management-api-keys)Understand Management API Keys

Each API key for the Management API has the following characteristics:

* API keys are associated with Couchbase Capella roles and permissions.
* Every API key has an expiration date.
* Every API key is associated with an allowed IP address list.

#### [](#organization-roles-and-project-access)Organization Roles and Project Access

Each API key is associated with 1 or more organization roles, which determine the privileges that the API key has within the organization. For more information about organization roles, see [Organization Roles](../../../../cloud/organizations/organization-user-roles.md).

Each API key may have access to 1 or more projects, depending on the organization role. For each project, each API key is associated with 1 or more project roles, which determine the privileges that the API key has within each project. For more information about project roles, see [Project Roles](../../../../cloud/projects/project-roles.md).

You can create an API key at the organization or a project level:

* When you create an API key at the organization level, you may specify the organization roles for the API key, which projects the API key is associated with, and the project roles for the API key within each project.
* When you create an API key at the project level, the API key has the [Organization Member](../../../../cloud/organizations/organization-user-roles.md#organization-role-member) role for the organization containing the project, and has access to the project where you created it. You may specify project roles for the API key within that project.

An API key must have the appropriate Capella roles to access an endpoint. The [Management API reference guide](../../../../cloud/management-api-reference/index.md) lists the roles that are needed for each endpoint.

#### [](#expiration)Expiration

By default, each API key expires 180 days after creation. You can specify a different expiration, or specify that the API key does not expire. For security, create new API keys regularly and let old API keys expire after transitioning to the new keys.

#### [](#ip-access)IP Access

By default, when you first create an API key, you can use that API key to access the Management API from any IP address. For security, each API key should only be able to access the Management API from specific IP addresses.

For each API key, you can grant access from:

* Individual IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format.
* Blocks of IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format using [CIDR notation](https://en.wikipedia.org/wiki/Classless%5FInter-Domain%5FRouting#CIDR%5Fnotation).

### [](#display-keys)Display Management API Keys

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

### [](#generate-keys)Generate Management API Keys

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
  3. For each project which the API key can access, select 1 or more [project roles](../../../../cloud/projects/project-roles.md) for the API key.
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
5. In **Roles**, select 1 or more [project roles](../../../../cloud/projects/project-roles.md) for the API key.
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

### [](#view-management-api-keys)View Management API Keys

To view details of a Management API key:

1. Display the list of Management API keys [within an organization or within a project](#display-keys).
2. Click the name of the API key.  
The details of the API key are displayed: the name, description, organization roles, expiration, allowed IP addresses, and project access.

### [](#delete-management-api-keys)Delete Management API Keys

To delete a Management API key:

1. Display the list of Management API keys [within an organization or within a project](#display-keys).
2. Next to the API key you want to delete, click the trash can icon ().
3. In the confirmation dialogue, confirm that you want to delete the API key.
4. Click **Delete**.

## [](#agent-memory-keys)Agent Memory API Keys

To create an initial bootstrap API key to access the Agent Memory API, you can use [the Capella UI](#generate-agent-memory-keys) or the [Management API](../../../../cloud/management-api-reference/index.md#tag/AI-Agent-Memory-API-Keys/operation/createAgentMemoryApiKey).

### [](#prerequisites)Prerequisites

To view, create, and delete Agent Memory API keys, you must have 1 of the following roles:

* [Organization Owner](../../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
* [Project Owner](../../../../cloud/projects/project-roles.md#project-owner-role)

To view Agent Memory API keys, you can also have the [Cluster Manager](../../../../cloud/projects/project-roles.md#project-cluster-manager-role) or [Cluster Viewer](../../../../cloud/projects/project-roles.md#project-cluster-viewer-role) project role. These roles cannot create or delete API keys.

### [](#view-agent-memory-keys)View Agent Memory API Keys

To display your Agent Memory API keys:

1. In the Capella UI, go to **AI Data Plane** **Access Control**.
2. Select the **Agent Memory** tab.

By default, there are no Agent Memory API keys.

### [](#generate-agent-memory-keys)Generate Agent Memory API Keys

> [!NOTE]
> You can only generate an API key for an Agent Memory server that has finished deploying.

To generate an Agent Memory API key:

1. In the Capella UI, choose 1 of the following options:

  * Go to **AI Data Plane** **Access Control**.
  * Go to **AI Data Plane** **Agent Memory**.

  * Access Control
  * Agent Memory

  1. Select the **Agent Memory** tab.
  2. Click **Generate API Key**.
  3. In the **Agent Memory** list, select the Agent Memory server for this API key.

  1. Next to your Agent Memory server, click **More Options (⋮)** **Generate API Key**.
2. In the **API Key Name** field, enter a name for the API key.
3. In the **Expiry** list, accept the default expiration, change the expiration, or specify that the key should not expire.
4. (Optional) In the **Description** field, enter a description of the API key.
5. Under **Access**, select the access level for the API key. For more information, see [Access Levels](api-intro.md#access-level).
6. Click **Generate API Key**.  
The Capella UI shows the new API key ID and the new API key token.  
> [!WARNING]  
> You must copy or download the API key token now. When you leave this page, you cannot copy or download the API key token again.
7. To download the API key token, click **Download Key**.
8. To copy either the API key ID or the API key token to the clipboard, click  next to the field.

### [](#delete-agent-memory-keys)Delete Agent Memory API Keys

To delete an Agent Memory API key:

1. In the Capella UI, go to **AI Data Plane** **Access Control**.
2. Select the **Agent Memory** tab.
3. Next to the API key you want to delete, click .
4. Confirm that you want to delete the API key and click **Delete API Key**.

## [](#agent-memory-endpoint)Agent Memory Server Endpoint

The Agent Memory API uses your Agent Memory server's endpoint as its base URL. The endpoint is unique to every Agent Memory server you deploy.

To copy your Agent Memory server endpoint, you can use the [Capella UI](#copy-agent-memory-endpoint) or the [Management API](../../../../cloud/management-api-reference/index.md#tag/AI-Agent-Memory-Servers/operation/getAgentMemoryServer).

### [](#prerequisites-2)Prerequisites

To copy the endpoint, you must have a [project role](../../../../cloud/projects/project-roles.md) on the project that contains the operational cluster your Agent Memory server connects to.

### [](#copy-agent-memory-endpoint)Copy Your Agent Memory Server Endpoint

To copy your Agent Memory server endpoint:

1. Go to **AI Data Plane** **Agent Memory**.
2. Click the name of your Agent Memory server.
3. Under **Connect**, copy the **Endpoint**.

## [](#agent-memory-allowed-ips)Allowed IP Addresses for Agent Memory

For security, your Agent Memory server only accepts requests from IP addresses in its allowed IP address list. A new Agent Memory server has no allowed IP addresses, so it blocks all requests until you add at least 1\. Allowed IP addresses apply to an Agent Memory server, not to an individual API key.

To add an allowed IP address, you can use [the Capella UI](#add-agent-memory-ips) or the [Management API](../../../../cloud/management-api-reference/index.md#tag/AI-Agent-Memory-Allowed-CIDRs/operation/createAgentMemoryServerAllowedCidr).

For each Agent Memory server, you can grant access from:

* Individual IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format.
* Blocks of IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format using [CIDR notation](https://en.wikipedia.org/wiki/Classless%5FInter-Domain%5FRouting#CIDR%5Fnotation).

You can add up to 50 allowed IP addresses to each Agent Memory server.

### [](#allowed-ip-prerequisites)Prerequisites

To view, add, and delete allowed IP addresses for an Agent Memory server, you must have 1 of the following roles:

* [Organization Owner](../../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
* [Project Owner](../../../../cloud/projects/project-roles.md#project-owner-role)
* [Cluster Manager](../../../../cloud/projects/project-roles.md#project-cluster-manager-role)

To view allowed IP addresses, you can also have the [Cluster Viewer](../../../../cloud/projects/project-roles.md#project-cluster-viewer-role) project role.

### [](#view-agent-memory-ips)View Allowed IP Addresses

To display the allowed IP addresses for your Agent Memory servers:

1. In the Capella UI, go to **AI Data Plane** **Allowed IP Addresses**.
2. Select the **Agent Memory** tab.

By default, there are no allowed IP addresses.

### [](#add-agent-memory-ips)Add Allowed IP Addresses

To add an allowed IP address:

1. In the Capella UI, choose 1 of the following options:

  * Go to **AI Data Plane** **Allowed IP Addresses**.
  * Go to **AI Data Plane** **Agent Memory**.

  * Allowed IP Addresses
  * Agent Memory

  1. Select the **Agent Memory** tab.
  2. Click **Add Allowed IP Address**.
  3. In the **Agent Memory** list, select the Agent Memory server.  
  You can only add allowed IP addresses to an Agent Memory server with a **Healthy** status.

  1. Next to your Agent Memory server, click **More Options (⋮)** **Add Allowed IP**.
2. In the **Select Allowed IP** list, select 1 of the following options:  
Add IP Address Manually  
Allow a specific IP address or CIDR block. Enter the IP address or CIDR block in the **Allowed IP / CIDR Block** field.  
Add Current IP Address  
Allow your current IP address.  
Allow Access from Anywhere  
Allow any IP address to access your Agent Memory server. In the confirmation dialog, enter `Yes` and click **Allow Access from Anywhere**.
3. Click **Add Allowed IP Address**.

### [](#delete-agent-memory-ips)Delete Allowed IP Addresses

To delete an allowed IP address:

1. In the Capella UI, go to **AI Data Plane** **Allowed IP Addresses**.
2. Select the **Agent Memory** tab.
3. Next to the allowed IP address you want to delete, click .
4. Confirm that you want to delete the allowed IP address and click **Delete Allowed IP**.

## [](#next-steps)Next Steps

* To make an API call, see [Make an API Call with the Agent Memory APIs](api-use.md).
* For a full reference guide for the Management API, see [Couchbase Capella Management API Reference](../../../../cloud/management-api-reference/index.md).
* For a full reference guide for the Agent Memory API, see [Agent Memory API Reference](../../agent-memory-api-reference/rest-api.md).
* For a reference of the Management API and Agent Memory API errors, see [The Agent Memory API Errors](api-errors.md).