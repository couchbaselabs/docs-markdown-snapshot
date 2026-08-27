---
title: Azure Blob Storage
description: To provide query access to OLAP data in Azure Blob Storage, you
  create an external link and associate it with an external collection.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/external-azure.adoc
  xref: xref:analytics:sources:external-azure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/external-azure.html)

# Azure Blob Storage

> To provide query access to OLAP data in Azure Blob Storage, you create an external link and associate it with an external collection. 

Azure Blob Storage external sources allow you to connect to and query data stored in Azure Blob Storage containers directly from your database. Before setting up an Azure Blob Storage external source, make sure you have the necessary Azure permissions and authentication credentials.

You also need the following information about the Azure Blob Storage container:

* [Credentials](#credentials)
* [The Location Path](#prefix)

### [](#credentials)Credentials

Capella Analytics supports the following authentication methods for Azure Blob Storage links. Choose the method that aligns with your organization's security requirements.

Anonymous

Access public containers without credentials. The Azure Storage Service Endpoint URL is sufficient. No additional fields are required.

Shared Key

Authenticate using your Azure Storage Account Name and its associated Account Key. For more information, see [Manage storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage) in the Azure documentation.

Shared Access Signature (SAS)

Grant time-limited, granular access to specific resources using a SAS token. For more information, see [Grant limited access to Azure Storage resources using shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) in the Azure documentation.

Service Principal (Entra ID)

Authenticate using a Microsoft Entra ID application with a Client ID, Client Secret, and Tenant ID for programmatic access control. For more information, see [Application and service principal objects in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals) in the Azure documentation.

> [!TIP]
> When you create an external link, follow best practices for security. Couchbase recommends that you grant the minimum possible permissions to perform the required operations, and allow access only to the required data and resources.

### [](#prefix)The Location Path

When you create an external collection based on an Azure Blob Storage container, you can supply a path to the files that Capella Analytics queries. A path consists of one or more prefixes that define a hierarchical organization, using a format such as `topLevel/nextLevel/lowestLevel`. The path does not include filenames.

> [!TIP]
> In the Azure portal, prefixes within a container are also referred to as virtual directories or folders.

To make querying the external data source as efficient as possible, supply a path that's as specific and precise as possible. You can use static prefixes, dynamic prefixes, or a mixture of both to define a path. For information about static and dynamic prefixes, see [Design a Location Path](dynamic-prefixes.md).

> [!IMPORTANT]
> Because you cannot index data located in an external store, Couchbase encourages thoughtful design of the paths used in external collections.

You can select a subset of the files in a location by using fields that include and exclude filenames.

For detailed instructions on setting up and configuring Azure Blob Storage external sources, see:

* [Set Up Azure Blob Storage External Source](setup-azure-blob-external-source.md)
* [Required Permissions for Azure Blob Storage](required-permissions-azure.md)

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Access Data](../intro/examples.md)