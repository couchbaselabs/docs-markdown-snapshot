---
title: Set Up Azure Blob Storage External Source
description: To provide query access to OLAP data in Azure Blob Storage, you
  create an external link and associate it with an external collection.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/setup-azure-blob-external-source.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:analytics:sources:setup-azure-blob-external-source.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/setup-azure-blob-external-source.html)

# Set Up Azure Blob Storage External Source

> To provide query access to OLAP data in Azure Blob Storage, you create an external link and associate it with an external collection. 

## [](#prerequisites)Prerequisites

Your Capella Analytics account must have either the [Project Owner](../admin/auth/auth-ui.md#project-owner-role) or [Project Manager](../admin/auth/auth-ui.md#project-cluster-manager-role) role to be able to create a link for the external data.

* If you want to access private data from an Azure Blob Storage container, you need credentials that can list and read data from that container. For more information, see [Credentials](external-azure.md#credentials).
* You have the path to the data you want to access from your Azure Blob Storage container. For more information, see [Location Path](external-azure.md#prefix).

## [](#create)Create a Link for Azure Blob Storage

To create an external link to Azure Blob Storage:

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name.
3. Use the explorer to explore the existing databases, scopes, and collections. You can add a database and scope if necessary: see [Create a Database](database-objects.md#database).
4. Select **Create** **Data Link**.
5. Select **Azure** then click **Continue**.
6. In the **Link Name** field, enter a name for the link.
7. In the **Endpoint** field, enter the Azure Storage Service URL for your storage account.  
The endpoint URL has the following format: `<https://<storageaccountname>.blob.core.windows.net>`
8. From **Authentication Method**, select one of the following options:

  * Anonymous
  * Shared Key
  * Shared Access Signature (SAS)
  * Service Principal (Entra ID)  
Select this option to access a public Azure Blob Storage container that does not require credentials. The endpoint URL you supplied is sufficient.

  * In the **Account Name** field, enter your Azure Storage Account name.
  * In the **Account Key** field, enter the associated storage account access key.  
> [!NOTE]  
> The Account Key is a sensitive credential and is masked in logs.

  * In the **Shared Access Signature** field, enter a SAS token that grants time-limited access to the required resources.  
> [!NOTE]  
> The SAS token is a sensitive credential and is masked in logs.  
For more information about generating a SAS token, see [Shared access signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) in the Azure documentation.

  * In the **Client ID** field, enter the Application (client) ID from your Microsoft Entra ID app registration.
  * In the **Client Secret** field, enter the associated client secret.
  * In the **Tenant ID** field, enter the Directory (tenant) ID.  
> [!NOTE]  
> The Client Secret is a sensitive credential and is masked in logs.  
For more information about setting up a Service Principal, see [Service Principal (Entra ID) Permissions](required-permissions-azure.md#service-principal-permissions).
9. (Optional) Select **Disable SSL Verification** to turn off SSL/TLS certificate verification.  
> [!CAUTION]  
> Enable this option only for local development or testing environments. Disabling SSL verification in production exposes data in transit to security risks.
10. Click **Save & Continue**.

Capella Analytics creates the link to the Azure Blob Storage data source. The new link appears in the Workbench, identified with an **Azure** tag.

The link is now available to provide your credentials whenever you query data in the external data source.

> [!NOTE]
> Because the data in an external collection is not ingested into Capella Analytics and remains on the external host, Capella Analytics cannot index it.

## [](#create-a-collection-for-azure-blob-storage-data)Create a Collection for Azure Blob Storage Data

You must create a collection for the data before you can query it in Capella Analytics. After you create the link to Azure Blob Storage, Capella Analytics prompts you to create a collection for your data. You can create the collection by clicking **Create Linked Collection**. If you want to create the collection later, click **Complete Later**. When you're ready to create the collection, hover over the link name under **Links** and select **More Options (⋮)** **Create Linked Collection**.

To complete creating the collection:

1. On the **Create Collection Linked to <Azure link name>** dialog, select the database and scope and enter a name for the collection.
2. In the **Azure Container Name** field, enter the name of the Azure Blob Storage container. Enter only the name of the container, not a URL.
3. In the **Path** field, enter one or more prefixes separated by slashes `/` to identify the location of the files you want to query. Do not include filenames in the path. To query files located at the top-most or container level, leave the path blank. See [Design a Location Path](dynamic-prefixes.md).
4. Choose the **File Format** of the files at that destination. Depending on the format you select, you may see additional fields:

  * JSON
  * CSV and TSV
  * Parquet
  * Avro  
JSON format requires no additional fields.

  * Define the data types for the fields in the files as a comma-separated list of `<field-name> <datatype>` values. The `<datatype>` is one of the [primitive data types](../sqlpp/10%5Fdata%5Ftype.md). If the field's value does not match the data type, Capella Analytics ignores the record. You can also specify the `NOT UNKNOWN` flag after the data type to have Capella Analytics ignore the record if the value is `missing` or `null`. For example:  
  id BIGINT NOT UNKNOWN, firstname STRING, lastname STRING
  * Clear **File includes header row** if the first line of your CSV file is not a list of the columns in the file.
  * If your data uses a value other than an empty string (`""`) to indicate a null value, select **Use custom string as Null** and enter the value.  
Choose whether Capella Analytics should parse embedded JSON data and convert decimal values to doubles.  
Avro format requires no additional fields.

1. (Optional) Use either the **Include** or **Exclude** field to specify files to include in, or exclude from, queries. You can use the following wildcards:

  * `*` matches any character or characters.
  * `?` matches any single character.
  * `[ sequence ]` matches any characters in the supplied sequence.
  * `[! sequence ]` matches any characters not in the supplied sequence.  
  For example, a container may store both JSON and Parquet files. Enter `*.JSON` in the **Include** field to query only the JSON files.
2. Click **Create Collection**. Your link and collection appear under the scope in the explorer.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Access Data](../intro/examples.md)