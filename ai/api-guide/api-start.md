---
title: Get Started with AI Services APIs
description: To get started with the Couchbase Capella APIs for AI Services, you
  must create an API key. An API key authenticates and authorizes you to access
  the APIs.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/api-guide/pages/api-start.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:api-guide:api-start.adoc[]
---

[View original HTML](/ai/api-guide/api-start.html)

# Get Started with AI Services APIs

> To get started with the Couchbase Capella APIs for AI Services, you must create an API key. An API key authenticates and authorizes you to access the APIs. 

This page is for Capella AI Services. It covers the AI Services features in the Management API, and the Model Service API. For more information about the Management API for Capella Operational features, see [Get Started with the Management API](../../cloud/management-api-guide/management-api-start.md).

This page describes how to generate and manage:

* [API keys for the Management API](#management-api-keys).
* [Model Service API keys for the Model Service API](#model-service-keys).

Use the Management API to configure and manage AI Services. Use the Model Service API to send inference requests to your AI models and view their outputs.

## [](#management-api-keys)Management API Keys

To create an initial bootstrap API key to access the Management API, you must use the [Capella UI](#gen-keys-org). Once you have created an initial bootstrap API key, you can use the [Management API](../../cloud/management-api-reference/index.md#tag/Api-Keys) itself to create further API keys.

### [](#understand-management-api-keys)Understand Management API Keys

Each API key for the Management API has the following characteristics:

* API keys are associated with Couchbase Capella roles and permissions.
* Every API key has an expiration date.
* Every API key is associated with an allowed IP address list.

#### [](#organization-roles-and-project-access)Organization Roles and Project Access

Each API key is associated with 1 or more organization roles, which determine the privileges that the API key has within the organization. For more information about organization roles, see [Organization Roles](../../cloud/organizations/organization-user-roles.md).

Each API key may have access to 1 or more projects, depending on the organization role. For each project, each API key is associated with 1 or more project roles, which determine the privileges that the API key has within each project. For more information about project roles, see [Project Roles](../../cloud/projects/project-roles.md).

You can create an API key at the organization or a project level:

* When you create an API key at the organization level, you may specify the organization roles for the API key, which projects the API key is associated with, and the project roles for the API key within each project.
* When you create an API key at the project level, the API key has the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role for the organization containing the project, and has access to the project where you created it. You may specify project roles for the API key within that project.

An API key must have the appropriate Capella roles to access an endpoint. The [Management API reference guide](../../cloud/management-api-reference/index.md) lists the roles that are needed for each endpoint.

#### [](#expiration)Expiration

By default, each API key expires 180 days after creation. You can specify a different expiration, or specify that the API key does not expire. For security, you should let API keys expire and create new API keys regularly.

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

### [](#gen-keys-org)Generate Management API Keys

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
  3. For each project which the API key can access, select 1 or more [project roles](../../cloud/projects/project-roles.md) for the API key.
  4. Click **Save**.
7. In **Key Expiration**, accept the default expiration, change the expiration, or specify that the key should not expire.
8. In **Allowed IP Addresses**, click **Added Allowed IP Address** to specify IP access for the API key.
9. Select 1 of the following options:

  1. To allow a specific IP address or block, in the **Add IP / CIDR Block** field, enter the IP address or CIDR notation.
  2. To add your current IP address block, click **Add Current IP Address**.
10. Click **Add**.
11. When you’re ready, click **Generate Key**.  
The Capella UI shows the new API key ID and the new API key token. The API key token is hidden to prevent others reading it.  
> [!WARNING]  
> You must copy or download the API key token now. When you leave this page, you will not be able to copy or download the API key token again.
12. To download the API key token, click **Download Key**. The key is saved by your browser in a file called `<name>-api-key-token.txt`, where `<name>` is the name of the API key.
13. To copy either the API key ID or the API key token to the clipboard, click the copy icon () next to the field.

To generate a Management API key at the project level:

1. Display the list of Management API keys [within the project](#display-keys-proj).
2. Click **Generate Key**.
3. In the **Key Name** field, enter a name for the API key.
4. (Optional) In the **Description** field, enter a description of the API key.
5. In **Roles**, select 1 or more [project roles](../../cloud/projects/project-roles.md) for the API key.
6. In the **Key Expiration**, accept the default expiration, change the expiration, or specify that the key should not expire.
7. In **Allowed IP Addresses**, click **Added Allowed IP Address** to specify IP access for the API key.
8. Select 1 of the following options:

  1. To allow a specific IP address or block, in the **Add IP / CIDR Block** field, enter the IP address or CIDR notation.
  2. To add your current IP address, click **Add Current IP Address**.
9. Click **Add**.
10. When you’re ready, click **Generate Key**.  
The Capella UI shows the new API key ID and the new API key token. The API key token is hidden to prevent others reading it.  
> [!WARNING]  
> You must copy or download the API key token now. When you leave this page, you will not be able to copy or download the API key token again.
11. To download the API key token, click **Download Key**. The key is saved by your browser in a file called `<name>-api-key-token.txt`, where `<name>` is the name of the API key.
12. To copy either the API key ID or the API key token to the clipboard, click the copy icon () next to the field.

### [](#view-management-keys)View Management API Keys

To view details of a Management API key:

1. Display the list of Management API keys [within an organization or within a project](#display-keys).
2. Click the name of the API key.  
The details of the API key are displayed: the name, description, organization roles, expiration, allowed IP addresses, and project access.

### [](#delete-management-keys)Delete Management API Keys

To delete a Management API key:

1. Display the list of Management API keys [within an organization or within a project](#display-keys).
2. Next to the API key you want to delete, click the trash can icon ().
3. In the confirmation dialogue, confirm that you want to delete the API key.
4. Click **Delete**.

## [](#model-service-keys)Model Service API Keys

To create an initial bootstrap API key to access the Model Service API, you can use [the Capella AI Services UI](#generate-model-keys) or the [Management API](../../cloud/management-api-reference/index.md#tag/Model-Services-API-Keys-%28AI-Services%29).

### [](#understand-model-service-api-keys)Understand Model Service API Keys

Each API key for the Model Service API has the following characteristics:

* API keys are associated with an AWS region. When creating a Model Service API key, you must select the same AWS region as the model you want to connect to.
* Every API key has an expiration date.
* Every API key is associated with an allowed IP address list.

#### [](#organization-roles)Organization Roles

To create and configure Model Service API keys, you must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role.

Each Model Service API key has access to Capella models deployed in the same AWS region. For more information about Capella models, see [Deploy an Embedding Model](../build/model-service/deploy-embed-model.md) or [Deploy a Large Language Model (LLM)](../build/model-service/deploy-llm-model.md).

#### [](#aws-regions)AWS Regions

When you create an API key, you must associate it with 1 of the AWS regions used by your models.

If all your models are deployed in the same region, you can use a single API key to access all of them. If your models are deployed across different regions, you’ll need to create a separate API key for each region.

#### [](#value-adds)Value Adds and Security Features

When you create an API key, it’s configured based on the **Value Adds** and **Security Features** that you enabled during model deployment. If you later change these or enable additional ones, any existing API keys associated with that model will no longer work. To restore access, you need to [create a new Model Service API key](#generate-model-keys).

Only the following **Value Adds** and **Security Features** affect API key compatibility:

* [Caching](../build/model-service/configure-value-adds.md#caching)
* Async processing for [LLMs](../build/model-service/configure-value-adds.md#async-processing) or [embedding models](../build/model-service/configure-embed-performance.md#async-processing)
* [Guardrails](../build/model-service/configure-guardrails-security.md#guardrails)
* [Jailbreak](../build/model-service/configure-guardrails-security.md#jailbreak)

#### [](#expiration-2)Expiration

By default, each API key expires 180 days after creation. You can specify a different expiration, or specify that the API key does not expire. For security, you should let API keys expire and create new API keys regularly.

#### [](#ip-access-2)IP Access

For security, each API key should only be able to access the Model Service API from specific IP addresses.

For each API key, you can grant access from:

* Individual IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format.
* Blocks of IP addresses in [IPv4](https://en.wikipedia.org/wiki/IPv4) format using [CIDR notation](https://en.wikipedia.org/wiki/Classless%5FInter-Domain%5FRouting#CIDR%5Fnotation).

### [](#view-model-keys)View Model Service API Keys

To display your region’s API keys:

1. In the Capella UI, go to **AI Services** **Access Control**.

By default, there are no API keys for your AI Services AWS region.

### [](#generate-model-keys)Generate Model Service API Keys

To generate a Model Service API key:

1. In the Capella UI, go to **AI Services** **Access Control**.
2. Click **Generate API Key**.
3. In the **API Key Name** field, enter a name for the API key.
4. In the **Expiration (Days)** field, accept the default expiration, change the expiration, or specify that the key should not expire.
5. In the **Region** field, select the AWS region for this API key.  
> [!IMPORTANT]  
> Select a region with deployed models where you want to use this API key. For more information, see [AWS Regions](#aws-regions).
6. (Optional) In the **Description** field, enter a description of the API key.
7. Specify IP access for the API key by choosing one of the following options:

  1. Click **Add IP Address Manually** to allow a specific IP address or CIDR block.
  2. Click **Add Current IP Address** to add your current IP address.
  3. Click **Allow Access from Anywhere** to allow any IP address to access models with this API key.
8. Click **Add Allowed IP Address**.
9. When you’re ready, click **Generate API Key**.  
The Capella UI shows the new API key ID and the new API key token. The API key token is hidden to prevent others reading it.  
> [!WARNING]  
> You must copy or download the API key token now. When you leave this page, you’ll not be able to copy or download the API key token again.
10. To download the API key token, click **Download Key**. The key is saved by your browser in a file called `<name>-api-key-token.txt`, where `<name>` is the name of the API key.
11. To copy either the API key ID or the API key token to the clipboard, click the copy icon () next to the field.

### [](#delete-model-keys)Delete Model Service API Keys

To delete a Model Service API key:

1. In the Capella UI, go to **AI Services** **Access Control**.
2. Next to the API key you want to delete, click the trash can icon ().
3. In the confirmation dialogue, confirm that you want to delete the API key.
4. Click **Delete API Key**.

## [](#next-steps)Next Steps

* To make an API call, see [Make an API Call with AI Services APIs](api-use.md).
* For a full reference guide for the Management API, see [Management API Reference](../../cloud/management-api-reference/index.md).
* For a full reference guide for the Model Service API, see [Inference API Reference](../model-service-api-reference/rest-api.md).
* For a reference of the Management API errors, see [Management API Error Messages ](api-errors.md#management-api-errors).
* For a reference of the AI Services Model Service API errors, see [Model Service API Error Messages ](api-errors.md#model-api-errors).