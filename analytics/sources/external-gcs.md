[View original HTML](/analytics/sources/external-gcs.html)

> To provide query access to OLAP data in GCS, you create an external link and associate it with an external collection. 

## [](#prerequisites)Prerequisites

Your Capella Analytics account must have either the [Project Owner](../admin/auth/auth-ui.md#project-owner-role) or [Project Manager](../admin/auth/auth-ui.md#project-cluster-manager-role) role to be able to create a link for the external data.

You need several pieces of information about the GCS bucket containing the data you want to query.

### [](#credentials)Credentials

To create an external link for a private data in GCS bucket, you must supply json credentials of the service account having access to GCS bucket.

Using a service account key to sign a JSON Web Token (JWT) and exchanging it for an access token. Because service account keys are a security risk if not managed correctly, you should choose a more secure alternative to service account keys whenever possible.

These credentials must have permission to list and read data from GCS bucket. For more information, see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview) in the Google Cloud documentation.

You do not need credentials for publicly available data in GCS bucket.

|  | When you create an external link, be sure to follow best practices for security. Couchbase recommends that you grant the minimum possible permissions to perform the required operations, and allow access only to the required data and resources. You should never use root account credentials. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#prefix)The Location Path

When you create an external collection based on GCS bucket, you can supply a path to the files Capella Analytics queries. A path consists of one or more prefixes that define a hierarchical organization, using a format such as `topLevel/nextLevel/lowestLevel`. The path does not include filenames.

|  | If you use the GCS bucket console, prefixes are also referred to as folders. |
|  | ---------------------------------------------------------------------------- |

To make querying the external data source as efficient as possible, you should supply a path that’s as specific and precise as possible. You can use static prefixes, dynamic prefixes, or a mixture of both to define a path. For information about static and dynamic prefixes, see [Design a Location Path](dynamic-prefixes.md).

|  | Because you cannot index the data located in an external store, Couchbase encourages thoughtful design of the paths used in external collections. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------- |

For information about using prefixes for data on GCS bucket, see [List the objects in a bucket using a prefix filter](https://cloud.google.com/storage/docs/samples/storage-list-files-with-prefix) in the Google Cloud documentation.

You can select a subset of the files in a location by using fields that include and exclude filenames.

## [](#create)Create a Link for GCS

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to explore the existing databases, scopes, and collections. You can add a database and scope if necessary: see [Create a Database](database-objects.md#database).
4. Select **Create** **Data Link**. The **Create Link for <cluster name> Cluster** dialog opens.
5. Select **Google Cloud Storage** then click **Continue**
6. In the **Link Name** field, enter a name for the link.
7. If the GCS bucket is private, add your json credentials to the **Authentication** field.
8. Click **Save & Continue** to proceed. Capella Analytics creates the link to the GCS data source.

## [](#create-a-collection-for-gcs-data)Create a Collection for GCS Data

You must create a collection for the data before you can query it in Capella Analytics. After you create the link to GCS, Capella Analytics prompts you to create a collection for your data. You can create the collection immediately by clicking **Create Linked Collection**. If you want to create the collection later, click **Complete Later**. When you’re ready to create the collection, hover over the link name’s under **Links** and select **More Options (⋮)** **Create Linked Collection**.

To complete creating the collection:

1. On the **Create Collection Linked to <GCSLinkName>** dialog, select the database and scope and enter a name for the collection.
2. In the **GCS Bucket** field, enter the name of a GCS bucket. Supply only the name of the bucket, not a URL.
3. In the **GCS Path** field, enter one or more prefixes separated by slashes `/` to identify the location of the files you want to query. Do not include filenames in the path. To query files located at the top-most, or bucket, level, leave the path blank. See [Design a Location Path](dynamic-prefixes.md).
4. Choose the **File Format** of the files at that destination. Depending on the format you select, you may see additional fields:

  * CSV and TSV
  * Parquet

  * Define the data types for the fields in the files as a comma-separated list of `<field-name> <datatype>` values. The `<datatype>` is one of the [primitive data types](../sqlpp/10%5Fdata%5Ftype.md). If the field’s value does not match the data type, Capella Analytics ignores the record. You can also specify `NOT UNKNOWN` flag after the data type to have Capella Analytics ignore the record if the value is `missing` or `null`. For example:  
  id BIGINT NOT UNKNOWN, firstname STRING, lastname STRING
  * Clear **File includes header row** if the first line of your CSV file is not a list of the columns in the file.
  * If your data uses a value other than an empty string (`""`) to indicate a null value, select **Use custom string as Null** and enter the value.  
Choose whether Capella Analytics should parse embedded JSON data and convert decimal values to doubles.
5. Optionally, use either the **Include** or **Exclude** field to specify files to include in, or exclude from, queries. You can use the following wildcards:

  * `*` matches any character or characters
  * `?` matches any single character
  * `[ sequence ]` matches any characters in the supplied sequence
  * `[! sequence ]` matches any characters not in the supplied sequence  
  For example, if the bucket stores both JSON and Parquet files, you can enter `*.JSON` in the **Include** field to query only the files that are in JSON format.
6. Click **Create Collection**. Your link and collection appear under the scope in the explorer.

The link is now available to provide your credentials whenever you query data in the external data source.

|  | Because the data in an external collection is not ingested into Capella Analytics and remains on the external host, Capella Analytics cannot index it. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Access Data](../intro/examples.md)