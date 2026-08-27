---
title: Required Permissions for Azure Blob Storage
description: This page outlines the required permissions when reading data from
  or writing data to Azure Blob Storage.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/required-permissions-azure.adoc
  xref: xref:analytics:sources:required-permissions-azure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/required-permissions-azure.html)

# Required Permissions for Azure Blob Storage

> This page outlines the required permissions when reading data from or writing data to Azure Blob Storage. 

Capella Analytics supports the following authentication methods for Azure Blob Storage:

* Anonymous — Access public containers without credentials. The endpoint URL is sufficient.
* Shared Key — The account key grants full read and write permissions by default. No additional permission configuration is required.
* Shared Access Signature (SAS) — Generate a SAS token with the permissions described in the [SAS Token Permissions](#sas-permissions) section.
* Service Principal (Entra ID) — Register a Microsoft Entra ID application and assign it the required role on your storage account. Follow the steps in the [Service Principal (Entra ID) Permissions](#service-principal-permissions) section.

## [](#sas-permissions)SAS Token Permissions

To use Shared Access Signature authentication, generate a SAS token. The token must include the correct permissions for Capella Analytics to read from or write to your Azure Blob Storage container.

To generate a SAS token with the required permissions:

1. Log in to the [Azure portal](https://portal.azure.com).
2. Select the storage account you want to use.
3. Under **Security + networking**, select **Shared access signature**.
4. Under **Allowed services**, select **Blob**.  
Capella Analytics uses this service to read and write data.
5. Under **Allowed resource types**, select both of the following:

  * **Container** — Required to list objects in the storage account.
  * **Object** — Required to read and write objects in the storage account.
6. Under **Allowed permissions**, select the following:

| Permission | Required for             |
| ---------- | ------------------------ |
| Read       | Reading and writing data |
| List       | Reading and writing data |
| Write      | Writing data             |
| Add        | Writing data             |
| Create     | Writing data             |
| Delete     | Writing data             |
7. Specify the **Start** and **Expiry** date and time for the SAS token.
8. Under **Allowed protocols**, select **HTTPS only** or **HTTPS and HTTP**.
9. Click **Generate SAS and connection string**.
10. Copy the generated SAS token.  
> [!NOTE]  
> Include the `?` at the start of the token when entering it in Capella Analytics.

## [](#service-principal-permissions)Service Principal (Entra ID) Permissions

To use Service Principal authentication, register an application in Microsoft Entra ID, create a client secret, and assign it the required role on your Azure Blob Storage account.

### [](#part-1-register-an-application-in-microsoft-entra-id)Part 1: Register an Application in Microsoft Entra ID

1. Log in to the [Azure portal](https://portal.azure.com).
2. Go to the **Microsoft Entra ID** service.
3. Under **Manage**, click **App registrations**, then click **\+ New registration**.  
For more information, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Azure documentation.
4. In the **Name** field, enter a name for the application (for example, `capella-analytics-application`).
5. Leave **Supported account types** as the default (single tenant).
6. Click **Register**.
7. On the **Overview** page, copy and save the following values:

  * **Application (client) ID** — this is your `clientId`
  * **Directory (tenant) ID** — this is your `tenantId`

### [](#part-2-create-a-client-secret)Part 2: Create a Client Secret

1. In the application registration, click **Certificates & secrets**.
2. Click **\+ New client secret**.  
For more information, see [Create a new client secret](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret) in the Azure documentation.
3. Add a description and click **Add**.
4. Copy and save the **Value** of the new secret before navigating away — it's only visible once.  
> [!WARNING]  
> This is your `clientSecret`. If you navigate away without copying it, you must create a new secret.
5. Set an appropriate expiry for the secret.

### [](#part-3-assign-a-blob-storage-role-to-the-service-principal)Part 3: Assign a Blob Storage Role to the Service Principal

1. In the Azure portal, go to **Storage accounts** and select the storage account you want to use.
2. Click **Access Control (IAM)**.  
For more information, see [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) in the Azure documentation.
3. Click **Add** **Add role assignment**.
4. Select one of the following roles based on your use case:

  * `Storage Blob Data Reader` — read-only access, sufficient for querying data with external collections
  * `Storage Blob Data Contributor` — read and write access, required when using the `COPY TO` statement
5. Under **Assign access to**, select **User, group, or service principal**.
6. Click **\+ Select members**, search for your application name (for example, `capella-analytics-application`), and select it.
7. Click **Review + assign**.  
> [!NOTE]  
> Role assignment propagation can take up to 15 minutes.

### [](#capella-analytics-field-reference)Capella Analytics Field Reference

Use the following table to locate the values required when configuring a Service Principal link in Capella Analytics:

| Capella Analytics field | Where to find it                                                   |
| ----------------------- | ------------------------------------------------------------------ |
| Client ID               | **App registrations** → **Overview** → **Application (client) ID** |
| Client Secret           | **App registrations** → **Certificates & secrets** → secret value  |
| Tenant ID               | **App registrations** → **Overview** → **Directory (tenant) ID**   |

## [](#see-also)See Also

* [Azure Blob Storage](external-azure.md)
* [Set Up Azure Blob Storage External Source](setup-azure-blob-external-source.md)
* [Query and Explore with the Workbench](../query/workbench.md)