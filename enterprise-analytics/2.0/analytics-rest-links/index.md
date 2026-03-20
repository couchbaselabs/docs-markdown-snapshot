---
title: Analytics Links REST API
description: A description of the Links REST API for Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/analytics-rest-links/pages/index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:analytics-rest-links:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/analytics-rest-links/index.html)

# Analytics Links REST API

* Single Links
  * postCreate Link
  * getQuery Link
  * putEdit Link
  * delDelete Link
* Multiple Links
  * getQuery All Links

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Links REST API (2.0)

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

| typerequired            | string (Create Request Type) Enum: "couchbase" "s3" The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. #\* azureblob: A link to Azure Blob Storage. #\* gcs: A link to Google Cloud Storage.                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hostnamerequired        | string For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        |
| username                | string For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          |
| password                | string For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          |
| encryptionrequired      | string Enum: "none" "half" "full" For Couchbase links only. The type of encryption used by the link. For details, see [encryption](#encryption).                                                                                                                                                                                                                             |
| certificate             | string For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  |
| clientCertificate       | string For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. #For Azure Blob links, this is the client certificate for the registered application. #Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.   |
| clientKey               | string For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                |
| accessKeyIdrequired     | string For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       |
| secretAccessKeyrequired | string For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            |
| sessionToken            | string For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. |
| regionrequired          | string For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              |
| serviceEndpoint         | string For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    |

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

| type | string (Edit Request Type) Enum: "couchbase" "s3" The type of the link. If this parameter is specified, the value must match the type that was set when the link was created. |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

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

| type                    | string (Edit Request Type) Enum: "couchbase" "s3" The type of the link. If this parameter is specified, the value must match the type that was set when the link was created.                                                                                                                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hostnamerequired        | string For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        |
| username                | string For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          |
| password                | string For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          |
| encryptionrequired      | string Enum: "none" "half" "full" For Couchbase links only. The type of encryption used by the link. For details, see [encryption](#encryption).                                                                                                                                                                                                                             |
| certificate             | string For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  |
| clientCertificate       | string For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. #For Azure Blob links, this is the client certificate for the registered application. #Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.   |
| clientKey               | string For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                |
| accessKeyIdrequired     | string For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       |
| secretAccessKeyrequired | string For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            |
| sessionToken            | string For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. |
| regionrequired          | string For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              |
| serviceEndpoint         | string For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    |

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