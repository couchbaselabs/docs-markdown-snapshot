---
title: Amazon S3
description: To provide query access to OLAP data in an AWS S3 bucket, you
  create an external link and associate it with an external collection.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/external-s3.adoc
  xref: xref:analytics:sources:external-s3.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/external-s3.html)

# Amazon S3

> To provide query access to OLAP data in an AWS S3 bucket, you create an external link and associate it with an external collection. 

Amazon S3 external sources allow you to connect to and query data stored in S3 buckets directly from your database. Before setting an S3 external source, make sure you have the necessary AWS permissions and configured credentials.

You also need the following information about the S3 bucket containing the data you want to query:

* [Credentials](#credentials)
* [The Location Path](#prefix)

### [](#credentials)Credentials

To create an external link for private data in an Amazon S3 bucket, you must supply an access key ID and secret access key. These credentials must have permission to list and read data from the bucket. For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Faccess-keys.html) in the AWS documentation.

You can specify a session token to indicate that the credentials are temporary. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Fcredentials%5Ftemp.html) in the AWS documentation.

You do not need credentials for publicly available data in S3.

> [!TIP]
> When you create an external link, be sure to follow best practices for security. Couchbase recommends that you grant the minimum possible permissions to perform the required operations, and allow access only to the required data and resources. You should never use root account credentials.

### [](#prefix)The Location Path

When you create an external collection based on an S3 bucket, you can supply a path to the files Capella Analytics queries. A path consists of one or more prefixes that define a hierarchical organization, using a format such as `topLevel/nextLevel/lowestLevel`. The path does not include filenames.

> [!TIP]
> If you use the Amazon S3 console, prefixes are also referred to as folders.

To make querying the external data source as efficient as possible, you should supply a path that's as specific and precise as possible. You can use static prefixes, dynamic prefixes, or a mixture of both to define a path. For information about static and dynamic prefixes, see [Design a Location Path](dynamic-prefixes.md).

> [!IMPORTANT]
> Because you cannot index the data located in an external store, Couchbase encourages thoughtful design of the paths used in external collections.

For information about using prefixes for data on S3, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the AWS documentation.

You can select a subset of the files in a location by using fields that include and exclude filenames.

For detailed instructions on setting and configuring Amazon S3 external sources, see the following:

* [Set Up Amazon S3 External Source](setup-aws-s3-external-source.md)
* [Cloud Read/Write Permissions for AWS](required-permissions-aws.md)

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Access Data](../intro/examples.md)