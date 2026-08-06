---
title: Analytics Settings REST API
description: A description of the Settings REST API for Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/analytics-rest-settings/pages/index.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:analytics-rest-settings:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/analytics-rest-settings/index.html)

# Analytics Settings REST API

* getView Enterprise Analytics Settings
* postModify Enterprise Analytics Settings

[API docs by Redocly](https://redocly.com/redoc/)

# Cluster Settings REST API (2.2)

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

 Expand all  Collapse all 

`{
* "blobStorageScheme": "s3",
* "blobStorageBucket": "enterprise-analytics-bucket",
* "blobStorageRegion": "us-west-2",
* "blobStoragePrefix": "analytics-data/",
* "blobStorageAnonymousAuth": false,
* "blobStorageForcePathStyle": false,
* "blobStoragePathStyleAddressing": false,
* "blobStorageEndpoint": "<https://my-object-storage:18082>",
* "blobStorageDisableSslVerify": false,
* "blobStorageCertificates": [
  * "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"  
],
* "blobStorageAccessKeyId": "AKIAIOSFODNN7EXAMPLE",
* "blobStorageSecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
* "blobStorageChecksumBehavior": "when_required",
* "blobStorageAzureClientId": "00000000-0000-0000-0000-000000000000",
* "numStoragePartitions": 128,
* "skipValidation": false,
* "warnings": [
  * {
    * "code": 21999,
    * "msg": "Disabling SSL verification in a production environment is highly insecure and exposes the system to serious risks, including Man-in-the-Middle (MITM) attacks",
    * "retriable": true  
  }  
]
}`

## [](#operation/post%5Fsettings)Modify Enterprise Analytics Settings 

Sets cluster-level Analytics settings.

##### Authorizations:

_ClusterWrite_

##### Request Body schema: application/x-www-form-urlencoded

| blobStorageScheme              | string Enum: "s3" "azblob" "gs" The storage scheme (provider) to use. Supported values: s3 — AWS S3 or an S3-compatible storage service. azblob — Azure Blob Storage. gs — Google Cloud Storage.                                                                                                                                                                                                                                                                                                                       |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| blobStorageBucket              | string The name of the blob storage bucket (S3) or container (Azure Blob Storage) where Enterprise Analytics will store its data.                                                                                                                                                                                                                                                                                                                                                                                      |
| blobStorageRegion              | string The region of the blob storage bucket. Applies only when blobStorageScheme is s3.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| blobStoragePrefix              | string Optional. The path prefix within the bucket (S3) or container (Azure Blob Storage) where Enterprise Analytics will store its data. If not specified, the data is stored in the root of the bucket /                                                                                                                                                                                                                                                                                                             |
| blobStorageAnonymousAuth       | boolean Applies when blobStorageScheme is s3 or gs. Not supported when blobStorageScheme is azblob. If true, the storage bucket will be accessed without any credentials (anonymous access). See also blobStorageAccessKeyId and blobStorageSecretAccessKey for static credentials, or omit all credential fields to use the Standard Credential Chain.                                                                                                                                                                |
| blobStorageForcePathStyle      | boolean Deprecated (Deprecated) Use blobStoragePathStyleAddressing instead.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| blobStoragePathStyleAddressing | boolean Applies only when blobStorageScheme is s3 and a custom blobStorageEndpoint is configured (S3-compatible storage). If true, path-style URLs are used (e.g., https://s3.example.com/bucket-name/key). If false, virtual-hosted-style URLs are used (e.g., https://bucket-name.s3.example.com/key). Some S3-compatible storage services require path-style addressing. Replaces the deprecated blobStorageForcePathStyle.                                                                                         |
| blobStorageEndpoint            | string The endpoint URL for the blob storage service. Required when using S3-compatible storage or Azure Blob Storage. For s3 (S3-compatible): the URL of your S3-compatible storage service (e.g., https://my-object-storage:18082). For azblob: the Blob service endpoint for your Azure storage account (e.g., https://mycompany.blob.core.windows.net/).                                                                                                                                                           |
| blobStorageDisableSslVerify    | boolean If true, disables certificate verification for SSL/TLS connections to the blob storage endpoint. Useful for testing or when using self-signed certificates, but **not recommended for production**. Warning: Disabling SSL verification in a production environment is highly insecure and exposes the system to serious risks, including Man-in-the-Middle (MITM) attacks.                                                                                                                                    |
| blobStorageCertificates        | Array of strings Applies only when blobStorageScheme is s3. One or more PEM-encoded certificates to trust when connecting to the blob storage endpoint. Only required if the endpoint is signed by a certificate authority (CA) other than a well-known public CA (e.g., for self-signed or private/internal CA certificates). Multiple certificates can be provided to support certificate rotation. **Available from Enterprise Analytics 2.1.1.**                                                                   |
| blobStorageAccessKeyId         | string Optional. Applies only when blobStorageScheme is s3. The Access Key ID for static credential authentication. If provided, must be supplied together with blobStorageSecretAccessKey. If omitted, the Standard Credential Chain is used (instance profile, environment variables, etc.) to obtain credentials automatically. See also blobStorageAnonymousAuth for anonymous access. **Available from Enterprise Analytics 2.1.1.**                                                                              |
| blobStorageSecretAccessKey     | string Optional. Applies only when blobStorageScheme is s3. The Secret Access Key for static credential authentication. If provided, must be supplied together with blobStorageAccessKeyId. If omitted, the Standard Credential Chain is used (instance profile, environment variables, etc.) to obtain credentials automatically. On input, supply the actual secret value. In logs and in responses from the API this value is masked as \*\*\* for security reasons. **Available from Enterprise Analytics 2.1.1.** |
| blobStorageChecksumBehavior    | string Enum: "when\_required" "when\_supported" Applies only when blobStorageScheme is s3. Controls when the client sends additional integrity checksums on object uploads. Supported values: when\_required — only send a checksum when the storage service requires one. when\_supported — send a checksum whenever the storage service supports it. Useful for S3-compatible storage services that do not fully support the default checksum behavior.                                                              |
| blobStorageAzureClientId       | string Applies only when blobStorageScheme is azblob. The client ID of the user-assigned managed identity to use when authenticating to Azure Blob Storage. If omitted, the default Azure credential chain is used.                                                                                                                                                                                                                                                                                                    |
| numStoragePartitions           | integer \[ 1 .. 1024 \] Specifies the number of partitions that will be used when storing the data in the blob storage bucket.                                                                                                                                                                                                                                                                                                                                                                                         |
| skipValidation                 | boolean If true, skips validation of the supplied settings, including the connectivity test against the configured blob storage. Intended for advanced or automated provisioning scenarios; in normal use the settings are validated before being applied.                                                                                                                                                                                                                                                             |

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

 Expand all  Collapse all 

`{
* "blobStorageScheme": "s3",
* "blobStorageBucket": "enterprise-analytics-bucket",
* "blobStorageRegion": "us-west-2",
* "blobStoragePrefix": "analytics-data/",
* "blobStorageAnonymousAuth": false,
* "blobStorageForcePathStyle": false,
* "blobStoragePathStyleAddressing": false,
* "blobStorageEndpoint": "<https://my-object-storage:18082>",
* "blobStorageDisableSslVerify": false,
* "blobStorageCertificates": [
  * "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"  
],
* "blobStorageAccessKeyId": "AKIAIOSFODNN7EXAMPLE",
* "blobStorageSecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
* "blobStorageChecksumBehavior": "when_required",
* "blobStorageAzureClientId": "00000000-0000-0000-0000-000000000000",
* "numStoragePartitions": 128,
* "skipValidation": false,
* "warnings": [
  * {
    * "code": 21999,
    * "msg": "Disabling SSL verification in a production environment is highly insecure and exposes the system to serious risks, including Man-in-the-Middle (MITM) attacks",
    * "retriable": true  
  }  
]
}`