---
title: Query Data in Azure Blob Storage
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sources/pages/external-azureblob.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sources:external-azureblob.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sources/external-azureblob.html)

# Query Data in Azure Blob Storage

> To query data in Azure Blob Storage, you create an external link and associate it with an external collection. 

## [](#prerequisites)Prerequisites

To use the Enterprise Analytics UI to query data, you need the `**Enterprise Analytics Access**` role along with specific privileges.

You need several pieces of information about the Azure Blob Storage container with the data you want to query.

### [](#credentials)Credentials

To create an external link for private data in an Azure Blob Storage container, you must supply credentials for the storage account. These credentials must have permission to list and read data from the container. For more information, see [Manage storage account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage) in the Microsoft Azure documentation.

You do not need credentials for publicly available data in Azure Blob Storage.

> [!TIP]
> When you create an external link, be sure to follow best practices for security. Couchbase recommends that you grant the minimum possible permissions to perform the required operations, and allow access only to the required data and resources. You should never use root account credentials.

### [](#prefix)The Location Path

When you create an external collection based on an Azure Blob Storage container, you can supply a path to the files Enterprise Analytics queries. A path consists of one or more prefixes that define a hierarchical organization, using a format such as `topLevel/nextLevel/lowestLevel`. The path does not include filenames.

> [!TIP]
> If you use the Azure portal, prefixes are also referred to as folders.

To make querying the external data source as efficient as possible, you should supply a path that's as specific and precise as possible. You can use static prefixes, dynamic prefixes, or a mixture of both to define a path. For information about static and dynamic prefixes, see [Design a Location Path](dynamic-prefixes.md).

> [!IMPORTANT]
> Because you cannot index the data located in an external store, Couchbase encourages thoughtful design of the paths used in external collections.

For information about using prefixes for data in Azure Blob Storage, see [List blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-list) in the Microsoft Azure documentation.

You can select a subset of the files in a location by using fields that include and exclude filenames.

## [](#create)Create a Link for Azure Blob Storage

1. In the UI, select the **Workbench** tab.
2. Select **\+ new link**.
3. In the **Link Name** field, enter a name for the link.
4. In the **Link Type** field, select **Azure Blob Storage**.
5. In the **Authentication** field, add the credentials for your Azure storage account.
6. Click **Save & Continue** to proceed. Enterprise Analytics creates the link to the Azure Blob Storage data source.

## [](#create-a-collection-for-azure-blob-storage-data)Create a Collection for Azure Blob Storage Data

1. In the UI, select the **Workbench** tab.
2. On the created Azure Blob Storage link, select **\+ collection**.
3. In the **Collection Name** field, enter a name for the collection.
4. In the **Database** field, select the database.
5. In the **Scope** field, select the scope.
6. In the **Container Name** field, enter the name of the Azure Blob Storage container. Supply only the name of the container, not a URL.
7. In the **Path** field, enter one or more prefixes separated by slashes `/` to identify the location of the files you want to query. Do not include filenames in the path. To query files located at the top-most, or container, level, leave the path blank. See [Design a Location Path](dynamic-prefixes.md).
8. In the **File Format** field, select the format of the files at that destination. Depending on the format you select, you may see additional fields:

  * CSV and TSV
  * Parquet
  * JSON
  * Avro

  * Define the data types for the fields in the files as a comma-separated list of `<field-name> <datatype>` values. The `<datatype>` is one of the [primitive data types](../sqlpp/10%5Fdata%5Ftype.md). If the field's value does not match the data type, Enterprise Analytics ignores the record. You can also specify the `NOT UNKNOWN` flag after the data type to have Enterprise Analytics ignore the record if the value is `missing` or `null`. For example:  
  id BIGINT NOT UNKNOWN, firstname STRING, lastname STRING
  * Clear **File includes header row** if the first line of your CSV file is not a list of the columns in the file.
  * If your data uses a value other than an empty string (`""`) to indicate a null value, select **Use custom string as Null** and enter the value.  
Choose whether Enterprise Analytics should parse embedded JSON data and convert decimal values to doubles.  
Choose whether Enterprise Analytics should parse embedded JSON data and convert decimal values to doubles.  
Choose whether Enterprise Analytics should parse embedded JSON data and convert decimal values to doubles.
9. Optionally, use either the **Include** or **Exclude** field to specify files to include in, or exclude from, queries. You can use the following wildcards:

  * `*` matches any character or characters
  * `?` matches any single character
  * `[ sequence ]` matches any characters in the supplied sequence
  * `[! sequence ]` matches any characters not in the supplied sequence  
  For example, if the container stores both JSON and Parquet files, you can enter `*.JSON` in the **Include** field to query only the files that are in JSON format.
10. Click **Save**. Your collection appears under the scope in the explorer.

> [!NOTE]
> Because the data in an external collection is not ingested into Enterprise Analytics and remains on the external host, Enterprise Analytics cannot index it.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Enterprise Analytics](database-objects.md)
* [Connecting to Data Sources](../intro/connecting-to-data-sources.md)