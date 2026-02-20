---
title: Query Data in External Data Sources
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sources/pages/external-s3.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:sources:external-s3.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/sources/external-s3.html)

# Query Data in External Data Sources

> To provide query access to OLAP data in an Amazon S3 and S3-compatible storage, you create an external link and associate it with an external collection. 

## [](#prerequisites)Prerequisites

To use the Enterprise Analytics UI to query data, you need the `**Enterprise Analytics Access**` role along with specific privileges.

You need several pieces of information about the in Amazon S3 and S3-compatible storage containing the data you want to query.

### [](#credentials)Credentials

To create an external link for a private data in an Amazon S3 and S3-compatible storage, you must supply an access key ID and secret access key. These credentials must have permission to list and read data from the storage. For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Faccess-keys.html) in the AWS documentation.

You can specify a session token to indicate that the credentials are temporary. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Ftemp.html) in the AWS documentation.

You do not need credentials for publicly available data in Amazon S3 and S3-compatible storage.

> [!TIP]
> When you create an external link, be sure to follow best practices for security. Couchbase recommends that you grant the minimum possible permissions to perform the required operations, and allow access only to the required data and resources. You should never use root account credentials.

### [](#prefix)The Location Path

When you create an external collection based on an Amazon S3 or S3-compatible storage, you can supply a path to the files Enterprise Analytics queries. A path consists of a prefix that defines a hierarchical organization, using a format such as `topLevel/nextLevel/lowestLevel`. The path does not include filenames.

> [!TIP]
> If you use the Amazon S3 console, prefixes are also referred to as folders.

To make querying the external data source as efficient as possible, you should supply a path that’s as specific and precise as possible. You can use static prefixes, dynamic prefixes, or a mixture of both to define a path. For information about static and dynamic prefixes, see [Design a Location Path](dynamic-prefixes.md).

> [!IMPORTANT]
> Because you cannot index the data located in an external store, Couchbase encourages thoughtful design of the paths used in external collections.

For information about using prefixes for data on S3, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the AWS documentation.

You can select a subset of the files in a location by using fields that include and exclude filenames.

### [](#alternate-storage-provider-information)Alternate Storage Provider Information

If you’re accessing data from an S3-compatible storage provider, you need your provider’s endpoint address. You do not need to provide an endpoint for Amazon S3 storage.

## [](#create)Create a Link for Amazon S3 and S3-compatible Storage

1. In the UI, select the **Workbench** tab.
2. Select **\+ new link**.
3. In the **Link Name** field, enter a name for the link.
4. In the **Link Type** field, select **S3**.
5. In the **Access Key ID** and the **Secret Access Key ID** fields, add your credentials. If you have temporary access to the storage, in the **Session Token** field enter an Amazon S3 session token.
6. In the **Region** field, select the Amazon S3 region.
7. If accessing an S3 or S3-compatible object store provider, in the **Endpoint** field enter the URL for that provider.
8. Click **Save**, **Discard Changes**, or **Drop Link** to proceed.

## [](#create-a-collection-foramazon-s3and-s3-compatible-data)Create a Collection for Amazon S3 and S3-Compatible Data

* In the UI, select the **Workbench** tab.
* Select btn\[+ collection\].
* In the **Collection Name** field, enter a name for the collection.
* In the **Bucket Name** field, enter the name of an S3 bucket. NOTE: You must supply only the name of the bucket and not an URL.
* In the **Path** field, enter 1 or more prefixes separated by slashes (`/`) to identify the location of the files you want to query. Do not include filenames in the path. To query files located at the top-most, or bucket, level, leave the path blank. See [Design a Location Path](dynamic-prefixes.md).
* In the **File Format** field, select the required format of the files at that destination. Depending on the format you select, you may see additional fields:

* CSV and TSV
* Parquet
* JSON
* Avro

* Define the data types for the fields in the files as a comma-separated list of `<field-name> <datatype>` values. The `<datatype>` is 1 of the [primitive data types](../../../server/current/analytics/10%5Fdata%5Ftype.md). If the field’s value does not match the data type, Enterprise Analytics ignores the record. You can also specify `NOT UNKNOWN` flag after the data type to have Enterprise Analytics ignore the record if the value is `missing` or `null`. For example:  
id BIGINT NOT UNKNOWN, firstname STRING, lastname STRING
* Select **Header** if the first line of your CSV file is not a list of the columns in the file.
* If your data uses a value other than an empty string (`""`) to indicate a null value, select **Use custom string as Null** and enter the value.  
Choose whether Enterprise Analytics should parse embedded JSON data and convert decimal values to doubles, and select the relevant timezone in the **Timezone** field.  
Choose whether Enterprise Analytics should parse embedded JSON data and convert decimal values to doubles.  
Choose whether Enterprise Analytics should parse embedded JSON data and convert decimal values to doubles.

In the **Include** or **Exclude** field, specify files to include in or exclude from queries. You can use the following wildcards:

* `*`: matches any character or characters
* `?`: matches any single character
* `[ {sequence} ]` matches any characters in the supplied sequence
* `[! {sequence} ]` matches any characters not in the supplied sequence

For example, if the bucket stores both JSON and Parquet files, you can enter **.JSON in the \*Include** field to query only the files that are in JSON format. 
* Click **Save**. Your collection appears under the scope in the explorer.

> [!NOTE]
> You cannot create Secondary indexes on collections that are created on external storage.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Enterprise Analytics](database-objects.md)
* [Connecting to Data Sources](../intro/connecting-to-data-sources.md)