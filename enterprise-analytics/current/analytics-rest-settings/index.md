---
title: Analytics Settings REST API
description: A description of the Settings REST API for Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/analytics-rest-settings/pages/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/analytics-rest-settings/index.html)

# Analytics Settings REST API

* getView Enterprise Analytics Settings
* postModify Enterprise Analytics Settings

[API docs by Redocly](https://redocly.com/redoc/)

# Cluster Settings REST API (2.0)

Download OpenAPI specification:

This API enables you to view or set cluster-level Enterprise Analytics settings.

## [](#operation/get%5Fsettings)View Enterprise Analytics Settings 

Retrieves cluster-level Analytics settings.

##### Authorizations:

_ClusterRead_

### Responses

**200** 

The operation was successful.

**401** 

Unauthorized. The user name or password may be incorrect.

get/settings/analytics

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/settings/analytics

### Response samples 

* 200
* 401

Content type

application/json

Copy

`{
* "blobStorageScheme": "s3",
* "blobStorageBucket": "enteprise-analytics-bucket",
* "blobStorageRegion": "us-west-2",
* "blobStoragePrefix": "analytics-data/",
* "blobStorageAnonymousAuth": false,
* "blobStorageForcePathStyle": false,
* "numStoragePartitions": 128
}`

## [](#operation/post%5Fsettings)Modify Enterprise Analytics Settings 

Sets cluster-level Analytics settings.

##### Authorizations:

_ClusterWrite_

##### Request Body schema: application/x-www-form-urlencoded

| blobStorageScheme         | string Specifies the blob storage scheme.                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| blobStorageBucket         | string Specifies the blob storage bucket name.                                                                              |
| blobStorageRegion         | string Specifies the blob storage bucket region.                                                                            |
| blobStoragePrefix         | string Specifies the blob storage bucket prefix where enteprise analytics will store its data.                              |
| blobStorageAnonymousAuth  | boolean Specifies if anonymous authentication should be used when accessing the blob storage bucket.                        |
| blobStorageForcePathStyle | boolean Specifies if path style should be should be used when accessing the blob storage bucket.                            |
| numStoragePartitions      | integer \[ 1 .. 1024 \] Specifies the number partitions that will be used when storing the data in the blob storage bucket. |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

post/settings/analytics

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/settings/analytics

### Response samples 

* 200
* 400
* 401

Content type

application/json

Copy

`{
* "blobStorageScheme": "s3",
* "blobStorageBucket": "enteprise-analytics-bucket",
* "blobStorageRegion": "us-west-2",
* "blobStoragePrefix": "analytics-data/",
* "blobStorageAnonymousAuth": false,
* "blobStorageForcePathStyle": false,
* "numStoragePartitions": 128
}`