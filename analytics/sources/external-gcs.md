---
title: Google Cloud Storage (GCS)
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/external-gcs.adoc
  xref: xref:analytics:sources:external-gcs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/external-gcs.html)

# Google Cloud Storage (GCS)

> To provide query access to OLAP data in GCS, you create an external link and associate it with an external collection. 

Google Cloud Storage (GCS) external sources allow you to connect to and query data stored in GCS buckets directly from your database. Before setting up a GCS external source, make sure you have the necessary GCP permissions and configured credentials.

You also need the following information about the GCS bucket containing the data you want to query:

* [Credentials](#credentials)
* [The Location Path](#prefix)

### [](#credentials)Credentials

To create an external link for private data in a GCS bucket, you must supply the JSON credentials of the service account that has access to the GCS bucket.

Use the service account key to sign a JSON Web Token (JWT) and exchange it for an access token. Because service account keys are a security risk if not managed correctly, you should choose a more secure alternative to service account keys whenever possible.

These credentials must have permission to list and read data from GCS bucket. For more information, see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview) in the Google Cloud documentation.

You do not need credentials for publicly available data in a GCS bucket.

> [!TIP]
> When you create an external link, be sure to follow best practices for security. Couchbase recommends that you grant the minimum possible permissions to perform the required operations, and allow access only to the required data and resources. You should never use root account credentials.

### [](#prefix)The Location Path

When you create an external collection based on a GCS bucket, you can supply a path to the files Capella Analytics queries. A path consists of one or more prefixes that define a hierarchical organization, using a format such as `topLevel/nextLevel/lowestLevel`. The path does not include filenames.

> [!TIP]
> If you use the GCS bucket console, prefixes are also referred to as folders.

To make querying the external data source as efficient as possible, you should supply a path that's as specific and precise as possible. You can use static prefixes, dynamic prefixes, or a mixture of both to define a path. For information about static and dynamic prefixes, see [Design a Location Path](dynamic-prefixes.md).

> [!IMPORTANT]
> Because you cannot index the data located in an external store, Couchbase encourages thoughtful design of the paths used in external collections.

For information about using prefixes for data on a GCS bucket, see [List the objects in a bucket using a prefix filter](https://cloud.google.com/storage/docs/samples/storage-list-files-with-prefix) in the Google Cloud documentation.

You can select a subset of the files in a location by using fields that include and exclude filenames.

For detailed instructions on setting up and configuring Google Cloud Storage external sources, see the following:

* [Set Up Google Cloud Storage (GCS) External Source](setup-gcs-external-source.md)
* [Cloud Read/Write Permissions for GCS](required-permissions-gcs.md)

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Access Data](../intro/examples.md)