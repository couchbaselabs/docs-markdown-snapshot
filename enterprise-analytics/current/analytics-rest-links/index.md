---
title: Analytics Links REST API
description: A description of the Links REST API for Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/analytics-rest-links/pages/index.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:analytics-rest-links:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/analytics-rest-links/index.html)

# Analytics Links REST API

* Single Links
  * postCreate Link
  * getQuery Link
  * putEdit Link
  * delDelete Link
* Multiple Links
  * getQuery All Links

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Links REST API (2.2)

Download OpenAPI specification:

This API enables you to manage the links to remote Couchbase clusters and external data sources.

## [](#tag/Single-Links)Single Links

Operations for single links.

## [](#tag/Single-Links/operation/post%5Flink)Create Link 

Creates a link

##### Authorizations:

_AnalyticsManage_ _CreateLink_

##### path Parameters

| namerequired | string The name of the link. |
| ------------ | ---------------------------- |

##### Request Body schema: application/x-www-form-urlencoded

| typerequired                  | string (Create Request Type) Enum: "couchbase" "s3" "azureblob" "gcs" "http" The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to the Azure Blob Storage service. gcs: A link to the Google Cloud Storage service. http: A link to an HTTP service.                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hostnamerequired              | string For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                                                      |
| username                      | string For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                                                        |
| password                      | string For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                                                        |
| encryptionrequired            | string Enum: "none" "half" "full" For Couchbase links only. The type of encryption used by the link. none: Neither passwords nor data are encrypted. half: Passwords are encrypted using SCRAM-SHA, but data is not. full: All data and passwords are encrypted and TLS is used.                                                                                                                           |
| certificate                   | string For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                                                |
| clientCertificate             | string For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                           |
| clientKey                     | string For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                              |
| certificates                  | string For Couchbase links only. The content of the target cluster root certificate(s), as an alternative to certificate. May contain multiple certificates, separated by new lines, to support certificate rotation. You should URL-encode this parameter to escape any special characters.                                                                                                               |
| clientKeyPassphrase           | string For Couchbase links only. A JSON object describing how to obtain the passphrase used to decrypt an encrypted client key.                                                                                                                                                                                                                                                                            |
| httpsOpts                     | string For Couchbase links only. A JSON object configuring TLS verification (verifyPeer, verifyHostname) for links with full encryption.                                                                                                                                                                                                                                                                   |
| preventRedirects              | boolean For Couchbase links only. If set to true, the link is prevented from following redirects to the target cluster's active nodes.                                                                                                                                                                                                                                                                     |
| regionrequired                | string For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                                                            |
| accessKeyId                   | string For S3 links only. The Amazon S3 access key ID. Required when using access key authentication. Must be provided together with secretAccessKey.                                                                                                                                                                                                                                                      |
| secretAccessKey               | string For S3 links only. The Amazon S3 secret access key. Required when using access key authentication. Must be provided together with accessKeyId. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                               |
| sessionToken                  | string For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Requires accessKeyId and secretAccessKey to also be provided. Passing this parameter indicates that the credentials are temporary. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. |
| instanceProfile               | string Value: "true" For S3 links only. If set to true, the link uses the EC2 instance profile for authentication. Cannot be combined with accessKeyId, secretAccessKey, or sessionToken.                                                                                                                                                                                                                  |
| roleArn                       | string For S3 links only. The Amazon Resource Name (ARN) of the role to assume for cross-account authentication. Requires either instanceProfile or accessKeyId and secretAccessKey (non-temporary) to provide the credentials used to assume the role.                                                                                                                                                    |
| externalId                    | string For S3 links only. An external ID for cross-account role assumption. Used together with roleArn. If roleArn is provided and externalId is not, one is automatically generated and returned in the response.                                                                                                                                                                                         |
| crossRegion                   | boolean For S3 links only. If set to true, allows the link to access S3 buckets in regions other than the one specified by region. Warning: Accessing buckets in a different region incurs cross-region data transfer charges.                                                                                                                                                                             |
| serviceEndpoint               | string For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                                                  |
| pathStyleAddressing           | boolean For S3 links only. If set to true, uses path-style addressing for S3 requests instead of virtual-hosted-style. Defaults to true if serviceEndpoint is set.                                                                                                                                                                                                                                         |
| disableSslVerify              | boolean For S3 links only. If set to true, SSL verification is disabled.                                                                                                                                                                                                                                                                                                                                   |
| checksumBehavior              | string Enum: "when\_required" "when\_supported" For S3 links only. Controls when the client sends additional integrity checksums on requests, primarily for S3-compatible storage. when\_required only sends a checksum when the service requires one; when\_supported sends one whenever the service supports it.                                                                                         |
| inputStreamType               | string Enum: "classic" "analytics" For S3 links only. The S3 input-stream implementation to use when reading objects.                                                                                                                                                                                                                                                                                      |
| changeDetectionMode           | string Enum: "server" "client" "none" For S3 links only. The change-detection mode used when reading objects (none disables change detection).                                                                                                                                                                                                                                                             |
| endpointrequired              | string The endpoint URI. Required for Azure Blob links; optional for S3 links (e.g. when using S3-compatible storage).                                                                                                                                                                                                                                                                                     |
| accountName                   | string For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                             |
| accountKey                    | string For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                              |
| sharedAccessSignature         | string For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                     |
| jsonCredentials               | string For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                                                  |
| applicationDefaultCredentials | boolean For Google Cloud Storage links only. If true, the link uses Google Application Default Credentials for authentication. Cannot be combined with jsonCredentials.                                                                                                                                                                                                                                    |
| bearerToken                   | string The bearer token for bearer token authentication. Cannot be combined with username, password, or OAuth2 parameters. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                          |
| oauthTokenUri                 | string The OAuth2 token URI. Required for OAuth2 authentication. Must be provided together with oauthClientId and oauthClientSecret. Cannot be combined with bearerToken, username, or password.                                                                                                                                                                                                           |
| oauthClientId                 | string The OAuth2 client ID. Required for OAuth2 authentication. Must be provided together with oauthTokenUri and oauthClientSecret.                                                                                                                                                                                                                                                                       |
| oauthClientSecret             | string The OAuth2 client secret. Required for OAuth2 authentication. Must be provided together with oauthTokenUri and oauthClientId. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                |
| oauthAllowedScopes            | string The allowed OAuth2 scopes. Optional when using OAuth2 authentication.                                                                                                                                                                                                                                                                                                                               |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**500** 

Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments.

post/api/v1/link/{name}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/link/{name}

### Response samples 

* 400
* 500

Content type

application/json

Copy

`{
* "error": "string"
}`

## [](#tag/Single-Links/operation/get%5Flink)Query Link 

Returns information about a link.

##### Authorizations:

_AnalyticsManage_ _DescribeLink_

##### path Parameters

| namerequired | string The name of the link. |
| ------------ | ---------------------------- |

##### query Parameters

| type | string (Edit Request Type) Enum: "couchbase" "s3" "azureblob" "gcs" "http" The type of the link. If this parameter is specified, the value must match the type that was set when the link was created. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Responses

**200** 

Success. Returns an array of objects, each of which contains information about a link.

**400** 

Bad request. A parameter has an incorrect value.

**500** 

Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments.

get/api/v1/link/{name}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/link/{name}

### Response samples 

* 200
* 400
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "name": "myLink",
  * "type": "couchbase"  
}
]`

## [](#tag/Single-Links/operation/put%5Flink)Edit Link 

Edits an existing link. The link name and type cannot be modified.

##### Authorizations:

_AnalyticsManage_ _AlterLink_

##### path Parameters

| namerequired | string The name of the link. |
| ------------ | ---------------------------- |

##### Request Body schema: application/x-www-form-urlencoded

| type                          | string (Edit Request Type) Enum: "couchbase" "s3" "azureblob" "gcs" "http" The type of the link. If this parameter is specified, the value must match the type that was set when the link was created.                                                                                                                                                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hostnamerequired              | string For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                                                      |
| username                      | string For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                                                        |
| password                      | string For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                                                        |
| encryptionrequired            | string Enum: "none" "half" "full" For Couchbase links only. The type of encryption used by the link. none: Neither passwords nor data are encrypted. half: Passwords are encrypted using SCRAM-SHA, but data is not. full: All data and passwords are encrypted and TLS is used.                                                                                                                           |
| certificate                   | string For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                                                |
| clientCertificate             | string For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                           |
| clientKey                     | string For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                              |
| certificates                  | string For Couchbase links only. The content of the target cluster root certificate(s), as an alternative to certificate. May contain multiple certificates, separated by new lines, to support certificate rotation. You should URL-encode this parameter to escape any special characters.                                                                                                               |
| clientKeyPassphrase           | string For Couchbase links only. A JSON object describing how to obtain the passphrase used to decrypt an encrypted client key.                                                                                                                                                                                                                                                                            |
| httpsOpts                     | string For Couchbase links only. A JSON object configuring TLS verification (verifyPeer, verifyHostname) for links with full encryption.                                                                                                                                                                                                                                                                   |
| preventRedirects              | boolean For Couchbase links only. If set to true, the link is prevented from following redirects to the target cluster's active nodes.                                                                                                                                                                                                                                                                     |
| regionrequired                | string For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                                                            |
| accessKeyId                   | string For S3 links only. The Amazon S3 access key ID. Required when using access key authentication. Must be provided together with secretAccessKey.                                                                                                                                                                                                                                                      |
| secretAccessKey               | string For S3 links only. The Amazon S3 secret access key. Required when using access key authentication. Must be provided together with accessKeyId. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                               |
| sessionToken                  | string For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Requires accessKeyId and secretAccessKey to also be provided. Passing this parameter indicates that the credentials are temporary. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. |
| instanceProfile               | string Value: "true" For S3 links only. If set to true, the link uses the EC2 instance profile for authentication. Cannot be combined with accessKeyId, secretAccessKey, or sessionToken.                                                                                                                                                                                                                  |
| roleArn                       | string For S3 links only. The Amazon Resource Name (ARN) of the role to assume for cross-account authentication. Requires either instanceProfile or accessKeyId and secretAccessKey (non-temporary) to provide the credentials used to assume the role.                                                                                                                                                    |
| externalId                    | string For S3 links only. An external ID for cross-account role assumption. Used together with roleArn. If roleArn is provided and externalId is not, one is automatically generated and returned in the response.                                                                                                                                                                                         |
| crossRegion                   | boolean For S3 links only. If set to true, allows the link to access S3 buckets in regions other than the one specified by region. Warning: Accessing buckets in a different region incurs cross-region data transfer charges.                                                                                                                                                                             |
| serviceEndpoint               | string For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                                                  |
| pathStyleAddressing           | boolean For S3 links only. If set to true, uses path-style addressing for S3 requests instead of virtual-hosted-style. Defaults to true if serviceEndpoint is set.                                                                                                                                                                                                                                         |
| disableSslVerify              | boolean For S3 links only. If set to true, SSL verification is disabled.                                                                                                                                                                                                                                                                                                                                   |
| checksumBehavior              | string Enum: "when\_required" "when\_supported" For S3 links only. Controls when the client sends additional integrity checksums on requests, primarily for S3-compatible storage. when\_required only sends a checksum when the service requires one; when\_supported sends one whenever the service supports it.                                                                                         |
| inputStreamType               | string Enum: "classic" "analytics" For S3 links only. The S3 input-stream implementation to use when reading objects.                                                                                                                                                                                                                                                                                      |
| changeDetectionMode           | string Enum: "server" "client" "none" For S3 links only. The change-detection mode used when reading objects (none disables change detection).                                                                                                                                                                                                                                                             |
| endpointrequired              | string The endpoint URI. Required for Azure Blob links; optional for S3 links (e.g. when using S3-compatible storage).                                                                                                                                                                                                                                                                                     |
| accountName                   | string For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                             |
| accountKey                    | string For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                              |
| sharedAccessSignature         | string For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                     |
| jsonCredentials               | string For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                                                  |
| applicationDefaultCredentials | boolean For Google Cloud Storage links only. If true, the link uses Google Application Default Credentials for authentication. Cannot be combined with jsonCredentials.                                                                                                                                                                                                                                    |
| bearerToken                   | string The bearer token for bearer token authentication. Cannot be combined with username, password, or OAuth2 parameters. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                          |
| oauthTokenUri                 | string The OAuth2 token URI. Required for OAuth2 authentication. Must be provided together with oauthClientId and oauthClientSecret. Cannot be combined with bearerToken, username, or password.                                                                                                                                                                                                           |
| oauthClientId                 | string The OAuth2 client ID. Required for OAuth2 authentication. Must be provided together with oauthTokenUri and oauthClientSecret.                                                                                                                                                                                                                                                                       |
| oauthClientSecret             | string The OAuth2 client secret. Required for OAuth2 authentication. Must be provided together with oauthTokenUri and oauthClientId. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                |
| oauthAllowedScopes            | string The allowed OAuth2 scopes. Optional when using OAuth2 authentication.                                                                                                                                                                                                                                                                                                                               |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**500** 

Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments.

put/api/v1/link/{name}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/link/{name}

### Response samples 

* 400
* 500

Content type

application/json

Copy

`{
* "error": "string"
}`

## [](#tag/Single-Links/operation/delete%5Flink)Delete Link 

Deletes a link. The link cannot be deleted if any other entities are using it, such as a collection. The entities using the link need to be disconnected from the link, otherwise, the delete operation fails.

##### Authorizations:

_AnalyticsManage_ _DropLink_

##### path Parameters

| namerequired | string The name of the link. |
| ------------ | ---------------------------- |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**500** 

Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments.

delete/api/v1/link/{name}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/link/{name}

### Response samples 

* 400
* 500

Content type

application/json

Copy

`{
* "error": "string"
}`

## [](#tag/Multiple-Links)Multiple Links

Operations for multiple links.

## [](#tag/Multiple-Links/operation/get%5Fall)Query All Links 

Returns information about all links

##### Authorizations:

_AnalyticsManage_ _DescribeLink_

##### query Parameters

| type | string Enum: "couchbase" "s3" "azureblob" "gcs" "http" The type of the link. If this parameter is omitted, all link types are retrieved, excluding the Local link. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Responses

**200** 

Success. Returns an array of objects, each of which contains information about a link.

**400** 

Bad request. A parameter has an incorrect value.

**500** 

Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments.

get/api/v1/link

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/link

### Response samples 

* 200
* 400
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "name": "myLink",
  * "type": "couchbase"  
}
]`