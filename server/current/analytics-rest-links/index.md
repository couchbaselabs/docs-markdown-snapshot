---
title: Analytics Links REST API
description: A description of the Links REST API for Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/8.0/docs/modules/analytics-rest-links/pages/index.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:server:analytics-rest-links:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/analytics-rest-links/index.html)

# Analytics Links REST API

## [](#overview)Overview

The Analytics Links REST API is provided by the Analytics Service. This API enables you to manage the links to remote Couchbase clusters and external data sources.

### Version information

**Version:** 8.0

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                        |
| **host**   | The host name or IP address of a node running the Analytics Service. **Example:** localhost |
| **port**   | The Analytics Service REST port. Use 18095 for secure access. **Values:** 8095, 18095       |

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Legacy Methods](#tag-LegacyMethods)  
[Multiple Links](#tag-MultipleLinks)  
[Single Links](#tag-SingleLinks)

### [](#tag-LegacyMethods)Legacy Methods

**Table of Contents**

[Delete Link (Alternative)](#delete%5Falt)  
[Create Link (Alternative)](#post%5Falt)  
[Edit Link (Alternative)](#put%5Falt)

#### [](#delete%5Falt)Delete Link (Alternative)

DELETE /analytics/link

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#delete%5Falt-description)Description

An alternative endpoint for [deleting a link](#delete%5Flink), provided for backward compatibility. The link cannot be deleted if any other entities are using it, such as an Analytics collection. The entities using the link need to be disconnected from the link, otherwise, the delete operation fails.

Consumes

* application/x-www-form-urlencoded

Produces

* application/json

##### [](#delete%5Falt-parameters)Parameters

Form Parameters

| Name                  | Description                                                                                                                    | Schema |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **dataverse**required | The name of the Analytics scope containing the link. With this parameter, the scope name may only contain a single identifier. | String |
| **name**required      | The name of the link.                                                                                                          | String |

##### [](#delete%5Falt-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 200       | The operation was successful.                                                                                                  |                  |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong) |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong) |

##### [](#delete%5Falt-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#post%5Falt)Create Link (Alternative)

POST /analytics/link

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#post%5Falt-description)Description

An alternative endpoint for [creating a link](#post%5Flink), provided for backward compatibility.

Consumes

* application/x-www-form-urlencoded

Produces

* application/json

##### [](#post%5Falt-parameters)Parameters

Form Parameters

| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                           | Schema |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **dataverse**required                     | The name of the Analytics scope containing the link. With this parameter, the scope name may only contain a single identifier.                                                                                                                                                                                                                                        | String |
| **name**required                          | The name of the link.                                                                                                                                                                                                                                                                                                                                                 | String |
| **type**required                          | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Azure Blob Storage. gcs: A link to Google Cloud Storage. **Values:** "couchbase", "s3", "azureblob", "gcs"                                                                                                                           | String |
| **hostname**required                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | String |
| **username**optional                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **password**optional                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **encryption**required                    | For Couchbase links only. The type of encryption used by the link. For details, see [encryption](#encryption). **Values:** "none", "half", "full"                                                                                                                                                                                                                     | String |
| **certificate**optional                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | String |
| **clientCertificate**optional             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | String |
| **clientKey**optional                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | String |
| **accessKeyId**required                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | String |
| **secretAccessKey**required               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | String |
| **sessionToken**optional                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | String |
| **region**required                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | String |
| **serviceEndpoint**optional               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | String |
| **endpoint**optional                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | String |
| **accountName**optional                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | String |
| **accountKey**optional                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | String |
| **sharedAccessSignature**optional         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | String |
| **managedIdentityId**optional             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | String |
| **clientId**optional                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | String |
| **tenantId**optional                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | String |
| **clientSecret**optional                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | String |
| **clientCertificatePassword**optional     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | String |
| **jsonCredentials**optional               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | String |
| **applicationDefaultCredentials**optional | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. **Values:** "true"                                                                                                                                                                                                 | String |

##### [](#post%5Falt-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 200       | The operation was successful.                                                                                                  |                  |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong) |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong) |

##### [](#post%5Falt-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#put%5Falt)Edit Link (Alternative)

PUT /analytics/link

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#put%5Falt-description)Description

An alternative endpoint for [editing a link](#put%5Flink), provided for backward compatibility. The link name, type, and scope name cannot be modified.

Consumes

* application/x-www-form-urlencoded

Produces

* application/json

##### [](#put%5Falt-parameters)Parameters

Form Parameters

| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                           | Schema |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **dataverse**required                     | The name of the Analytics scope containing the link. With this parameter, the scope name may only contain a single identifier.                                                                                                                                                                                                                                        | String |
| **name**required                          | The name of the link.                                                                                                                                                                                                                                                                                                                                                 | String |
| **type**optional                          | The type of the link. If this parameter is specified, the value must match the type that was set when the link was created. **Values:** "couchbase", "s3", "azureblob", "gcs"                                                                                                                                                                                         | String |
| **hostname**required                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | String |
| **username**optional                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **password**optional                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **encryption**required                    | For Couchbase links only. The type of encryption used by the link. For details, see [encryption](#encryption). **Values:** "none", "half", "full"                                                                                                                                                                                                                     | String |
| **certificate**optional                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | String |
| **clientCertificate**optional             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | String |
| **clientKey**optional                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | String |
| **accessKeyId**required                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | String |
| **secretAccessKey**required               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | String |
| **sessionToken**optional                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | String |
| **region**required                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | String |
| **serviceEndpoint**optional               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | String |
| **endpoint**optional                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | String |
| **accountName**optional                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | String |
| **accountKey**optional                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | String |
| **sharedAccessSignature**optional         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | String |
| **managedIdentityId**optional             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | String |
| **clientId**optional                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | String |
| **tenantId**optional                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | String |
| **clientSecret**optional                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | String |
| **clientCertificatePassword**optional     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | String |
| **jsonCredentials**optional               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | String |
| **applicationDefaultCredentials**optional | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. **Values:** "true"                                                                                                                                                                                                 | String |

##### [](#put%5Falt-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 200       | The operation was successful.                                                                                                  |                  |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong) |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong) |

##### [](#put%5Falt-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

### [](#tag-MultipleLinks)Multiple Links

**Table of Contents**

[Query All Links](#get%5Fall)  
[Query Scope Links](#get%5Fscope)

#### [](#get%5Fall)Query All Links

GET /analytics/link

##### [](#get%5Fall-description)Description

Returns information about all links in all Analytics scopes.

Produces

* application/json

##### [](#get%5Fall-parameters)Parameters

Query Parameters

| Name                  | Description                                                                                                                                                                                                                                                                                                                          | Schema |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **dataverse**optional | The name of an Analytics scope. When this parameter is included, the request only returns information about links in the specified scope. With this parameter, the scope name may only contain a single identifier. This parameter is deprecated, and will be removed in a future release. It's provided for backward compatibility. | String |
| **name**optional      | The name of a link. When this parameter is included, the request only returns information about the specified link. If specified, the dataverse parameter must be specified also. This parameter is deprecated, and will be removed in a future release. It's provided for backward compatibility.                                   | String |
| **type**optional      | The type of the link. If this parameter is omitted, all link types are retrieved, excluding the Local link. **Values:** "couchbase", "s3", "azureblob", "gcs"                                                                                                                                                                        | String |

##### [](#get%5Fall-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| 200       | Success. Returns an array of objects, each of which contains information about a link.                                         | [Links](#ResponseAll) array |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong)            |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong)            |

##### [](#get%5Fall-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

##### [](#example-http-request)Example HTTP Request

The example below queries all links of type `S3` in all Analytics scopes.

curl request

```sh
curl -v -u Administrator:password \
     "http://localhost:8095/analytics/link?type=S3"
```

##### [](#example-http-response)Example HTTP Response

Response 200

```json
[ {
  "accessKeyId" : "myAccessKey",
  "name" : "myAwsLink",
  "region" : "us-east-1",
  "scope" : "travel-sample/inventory",
  "secretAccessKey" : "<redacted sensitive entry>",
  "serviceEndpoint" : null,
  "type" : "s3"
}, {
  "accessKeyId" : "myTempAccessKey",
  "name" : "myTempLink",
  "region" : "eu-west-1",
  "scope" : "travel-sample/inventory",
  "secretAccessKey" : "<redacted sensitive entry>",
  "serviceEndpoint" : null,
  "sessionToken" : "<redacted sensitive entry>",
  "type" : "s3"
} ]
```

#### [](#get%5Fscope)Query Scope Links

GET /analytics/link/{scope}

##### [](#get%5Fscope-description)Description

Returns information about all links in the specified Analytics scope.

Produces

* application/json

##### [](#get%5Fscope-parameters)Parameters

Path Parameters

| Name              | Description                                                                                                                                                                                             | Schema |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope**required | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | String |

Query Parameters

| Name             | Description                                                                                                                                                   | Schema |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **type**optional | The type of the link. If this parameter is omitted, all link types are retrieved, excluding the Local link. **Values:** "couchbase", "s3", "azureblob", "gcs" | String |

##### [](#get%5Fscope-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| 200       | Success. Returns an array of objects, each of which contains information about a link.                                         | [Links](#ResponseAll) array |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong)            |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong)            |

##### [](#get%5Fscope-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

##### [](#example-http-request-2)Example HTTP Request

The example below queries all links in the `Default` scope.

curl request

```sh
curl -v -u Administrator:password \
     "http://localhost:8095/analytics/link/Default"
```

##### [](#example-http-response-2)Example HTTP Response

Response 200

```json
[
  {
    "accountKey": null,
    "accountName": null,
    "clientCertificate": null,
    "clientCertificatePassword": null,
    "clientId": null,
    "clientSecret": null,
    "endpoint": "my.endpoint.uri",
    "managedIdentityId": null,
    "name": "myBlobLink",
    "scope": "Default",
    "sharedAccessSignature": null,
    "tenantId": null,
    "type": "azureblob"
  },
  {
    "activeHostname": "remoteHostName:8091",
    "bootstrapAlternateAddress": false,
    "bootstrapHostname": "remoteHostName:8091",
    "certificate": null,
    "clientCertificate": null,
    "clientKey": null,
    "clusterCompatibility": 393221,
    "encryption": "none",
    "name": "myCbLink",
    "nodes": [
      {
        "alternateAddresses": null,
        "hostname": null,
        "services": {
          "cbas": 8095,
          "cbasSSL": 18095,
          "kv": 11210,
          "kvSSL": 11207,
          "mgmt": 8091,
          "mgmtSSL": 18091
        }
      }
    ],
    "password": "<redacted sensitive entry>",
    "scope": "Default",
    "type": "couchbase",
    "username": "remote.user",
    "uuid": "6331e2a390125b662f7bcfd63ecb3a73"
  }
]
```

### [](#tag-SingleLinks)Single Links

**Table of Contents**

[Delete Link](#delete%5Flink)  
[Query Link](#get%5Flink)  
[Create Link](#post%5Flink)  
[Edit Link](#put%5Flink)

#### [](#delete%5Flink)Delete Link

DELETE /analytics/link/{scope}/{name}

##### [](#delete%5Flink-description)Description

Deletes a link in the specified Analytics scope. The link cannot be deleted if any other entities are using it, such as an Analytics collection. The entities using the link need to be disconnected from the link, otherwise, the delete operation fails.

Produces

* application/json

##### [](#delete%5Flink-parameters)Parameters

Path Parameters

| Name              | Description                                                                                                                                                                                             | Schema |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope**required | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | String |
| **name**required  | The name of the link.                                                                                                                                                                                   | String |

##### [](#delete%5Flink-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 200       | The operation was successful.                                                                                                  |                  |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong) |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong) |

##### [](#delete%5Flink-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

##### [](#example-http-requests)Example HTTP Requests

The example below deletes the link named `myCbLink` from the `Default` scope.

curl request

```sh
curl -v -u Administrator:password \
     -X DELETE \
     "http://localhost:8095/analytics/link/Default/myCbLink"
```

The example below deletes the link named `myAwsLink` from the `travel-sample.inventory` scope.

curl request

```sh
curl -v -u Administrator:password \
     -X DELETE \
     "http://localhost:8095/analytics/link/travel-sample%2Finventory/myAwsLink"
```

> [!NOTE]
> The dot separator within the scope name is converted to a slash (`/`), which is then URL-encoded as `%2F`.

#### [](#get%5Flink)Query Link

GET /analytics/link/{scope}/{name}

##### [](#get%5Flink-description)Description

Returns information about a link in the specified Analytics scope.

Produces

* application/json

##### [](#get%5Flink-parameters)Parameters

Path Parameters

| Name              | Description                                                                                                                                                                                             | Schema |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope**required | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | String |
| **name**required  | The name of the link.                                                                                                                                                                                   | String |

Query Parameters

| Name             | Description                                                                                                                                                                   | Schema |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **type**optional | The type of the link. If this parameter is specified, the value must match the type that was set when the link was created. **Values:** "couchbase", "s3", "azureblob", "gcs" | String |

##### [](#get%5Flink-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| 200       | Success. Returns an array of objects, each of which contains information about a link.                                         | [Links](#ResponseAll) array |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong)            |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong)            |

##### [](#get%5Flink-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

##### [](#example-http-request-3)Example HTTP Request

The example below queries the `myAwsLink` link in the `travel-sample.inventory` scope.

curl request

```sh
curl -v -u Administrator:password \
     "http://localhost:8095/analytics/link/travel-sample%2Finventory/myAwsLink"
```

> [!NOTE]
> The dot separator within the scope name is converted to a slash (`/`), which is then URL-encoded as `%2F`.

##### [](#example-http-response-3)Example HTTP Response

Response 200

```json
[ {
  "accessKeyId" : "myAccessKey",
  "name" : "myAwsLink",
  "region" : "us-east-1",
  "scope" : "travel-sample/inventory",
  "secretAccessKey" : "<redacted sensitive entry>",
  "serviceEndpoint" : null,
  "type" : "s3"
} ]
```

#### [](#post%5Flink)Create Link

POST /analytics/link/{scope}/{name}

##### [](#post%5Flink-description)Description

Creates a link in the specified Analytics scope.

Consumes

* application/x-www-form-urlencoded

Produces

* application/json

When creating or altering a remote link using an alternate address, note the following:

* At least one node in the remote cluster must expose the `mgmt` port (`rest_port`, default 8091) or the `mgmtSSL` port (`ssl_rest_port`, default 18091).
* Furthermore, **all** data nodes in the remote cluster must expose the `kv` port (`memcached_port`, default 11210) or the `kvSSL` port (`memcached_ssl_port`, default 11207).

Failure to do so will result in a 400 (Bad Request) error.

> [!NOTE]
> The SSL ports are required when the **encryption** mode is set to `full`; the non-SSL ports are required otherwise.

> [!CAUTION]
> When creating an external link, be sure to follow best practices for security. Root account credentials should never be used. Grant the minimum possible permissions to perform the required operations, and only allow access to the required data and resources.

##### [](#post%5Flink-parameters)Parameters

Path Parameters

| Name              | Description                                                                                                                                                                                             | Schema |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope**required | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | String |
| **name**required  | The name of the link.                                                                                                                                                                                   | String |

Form Parameters

| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                           | Schema |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **type**required                          | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Azure Blob Storage. gcs: A link to Google Cloud Storage. **Values:** "couchbase", "s3", "azureblob", "gcs"                                                                                                                           | String |
| **hostname**required                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | String |
| **username**optional                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **password**optional                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **encryption**required                    | For Couchbase links only. The type of encryption used by the link. For details, see [encryption](#encryption). **Values:** "none", "half", "full"                                                                                                                                                                                                                     | String |
| **certificate**optional                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | String |
| **clientCertificate**optional             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | String |
| **clientKey**optional                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | String |
| **accessKeyId**required                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | String |
| **secretAccessKey**required               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | String |
| **sessionToken**optional                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | String |
| **region**required                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | String |
| **serviceEndpoint**optional               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | String |
| **endpoint**optional                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | String |
| **accountName**optional                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | String |
| **accountKey**optional                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | String |
| **sharedAccessSignature**optional         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | String |
| **managedIdentityId**optional             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | String |
| **clientId**optional                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | String |
| **tenantId**optional                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | String |
| **clientSecret**optional                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | String |
| **clientCertificatePassword**optional     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | String |
| **jsonCredentials**optional               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | String |
| **applicationDefaultCredentials**optional | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. **Values:** "true"                                                                                                                                                                                                 | String |

##### [](#post%5Flink-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 200       | The operation was successful.                                                                                                  |                  |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong) |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong) |

##### [](#post%5Flink-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

##### [](#example-http-requests-2)Example HTTP Requests

The example below creates a Couchbase link named `myCbLink` in the `Default` scope, with no encryption.

curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/Default/myCbLink" \
     -d type=couchbase \
     -d hostname=remoteHostName:8091 \
     -d encryption=none \
     --data-urlencode username=remote.user \
     --data-urlencode password=remote.p4ssw0rd
```

> [!NOTE]
> The `username` and `password` parameters are URL-encoded to escape any special characters.

The example below creates a Microsoft Azure Blob link named `myBlobLink` in the `Default` scope, with anonymous authentication.

curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/Default/myBlobLink" \
     -d type=azureblob \
     -d endpoint=my.endpoint.uri
```

The example below creates a Google Cloud Storage link named `myGcsLink` in the `Default` scope, with anonymous authentication.

curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/Default/myGcsLink" \
     -d type=gcs
```

The example below creates an Amazon S3 link named `myAwsLink` in the `travel-sample.inventory` scope.

curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/travel-sample%2Finventory/myAwsLink" \
     -d type=s3 \
     -d region=us-east-1 \
     -d accessKeyId=myAccessKey \
     --data-urlencode secretAccessKey=mySecretKey
```

> [!NOTE]
> The dot separator within the scope name is converted to a slash (`/`), which is then URL-encoded as `%2F`. The `secretAccessKey` parameter is URL-encoded to escape any special characters.

The example below creates an Amazon S3 link named `myTempLink` with temporary credentials in the `travel-sample.inventory` scope.

curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/travel-sample%2Finventory/myTempLink" \
     -d type=s3 \
     -d region=eu-west-1 \
     -d accessKeyId=myTempAccessKey \
     -d sessionToken=mySessionToken \
     --data-urlencode secretAccessKey=myTempSecretKey
```

> [!NOTE]
> The dot separator within the scope name is converted to a slash (`/`), which is then URL-encoded as `%2F`. The `secretAccessKey` parameter is URL-encoded to escape any special characters.

#### [](#put%5Flink)Edit Link

PUT /analytics/link/{scope}/{name}

##### [](#put%5Flink-description)Description

Edits an existing link in the specified Analytics scope. The link name, type, and scope name cannot be modified.

Consumes

* application/x-www-form-urlencoded

Produces

* application/json

##### [](#put%5Flink-parameters)Parameters

Path Parameters

| Name              | Description                                                                                                                                                                                             | Schema |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope**required | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | String |
| **name**required  | The name of the link.                                                                                                                                                                                   | String |

Form Parameters

| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                           | Schema |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **type**optional                          | The type of the link. If this parameter is specified, the value must match the type that was set when the link was created. **Values:** "couchbase", "s3", "azureblob", "gcs"                                                                                                                                                                                         | String |
| **hostname**required                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | String |
| **username**optional                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **password**optional                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | String |
| **encryption**required                    | For Couchbase links only. The type of encryption used by the link. For details, see [encryption](#encryption). **Values:** "none", "half", "full"                                                                                                                                                                                                                     | String |
| **certificate**optional                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | String |
| **clientCertificate**optional             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | String |
| **clientKey**optional                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | String |
| **accessKeyId**required                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | String |
| **secretAccessKey**required               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | String |
| **sessionToken**optional                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | String |
| **region**required                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | String |
| **serviceEndpoint**optional               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | String |
| **endpoint**optional                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | String |
| **accountName**optional                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | String |
| **accountKey**optional                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | String |
| **sharedAccessSignature**optional         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | String |
| **managedIdentityId**optional             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | String |
| **clientId**optional                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | String |
| **tenantId**optional                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | String |
| **clientSecret**optional                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | String |
| **clientCertificatePassword**optional     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | String |
| **jsonCredentials**optional               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | String |
| **applicationDefaultCredentials**optional | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. **Values:** "true"                                                                                                                                                                                                 | String |

##### [](#put%5Flink-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| 200       | The operation was successful.                                                                                                  |                  |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Wrong) |
| 500       | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Wrong) |

##### [](#put%5Flink-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

##### [](#example-http-requests-3)Example HTTP Requests

The example below edits the link named `myCbLink` in the `Default` scope to use full encryption with a client certificate and client key.

curl request

```sh
curl -v -u Administrator:password \
     -X PUT \
     "http://localhost:8095/analytics/link/Default/myCbLink" \
     -d type=couchbase \
     -d hostname=remoteHostName:8091 \
     -d encryption=full \
     --data-urlencode "certificate=$(cat ./cert/targetClusterRootCert.pem)" \
     --data-urlencode "clientCertificate=$(cat ./cert/clientCert.pem)" \
     --data-urlencode "clientKey=$(cat ./cert/client.key)"
```

> [!NOTE]
> The `certificate`, `clientCertificate`, and `clientKey` parameters use command substitution with the `cat` command to return the content of the referenced files. The content of these files is then URL-encoded to escape any special characters.

The example below edits the Google Cloud Storage link named `myGcsLink` in the `Default` scope to use Google Application Default Credentials for authentication.

curl request

```sh
curl -v -u Administrator:password \
     -X PUT \
     "http://localhost:8095/analytics/link/Default/myGcsLink" \
     -d type=gcs \
     -d applicationDefaultCredentials=true
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Links](#ResponseAll)  
[Azure Blob Response](#ResponseAzureBlob)  
[Azure Blob Specific Response](#ResponseAzureBlobSpecific)  
[Couchbase Response](#ResponseCouchbase)  
[Couchbase Specific Response](#ResponseCouchbaseSpecific)  
[Nodes](#ResponseCouchbaseSpecificNode)  
[Services](#ResponseCouchbaseSpecificNodeServices)  
[GCS Response](#ResponseGCS)  
[GCS Specific Response](#ResponseGCSSpecific)  
[S3 Response](#ResponseS3)  
[S3 Specific Response](#ResponseS3Specific)  
[Errors](#Wrong)

### [](#ResponseAll)Links

 Object

| Property          |                                                                                                                                                                                                                                                       | Schema |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope**required | The name of the Analytics scope containing the link. The scope name may contain one or two identifiers, separated by a slash (/). **Example:** "travel-sample/inventory"                                                                              | String |
| **name**required  | The name of the link. **Example:** "myLink"                                                                                                                                                                                                           | String |
| **type**required  | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Microsoft Azure Blob Storage. gcs: A link to Google Cloud Storage. **Values:** "couchbase", "s3", "azureblob", "gcs" | String |

This schema has alternative properties, depending on the value of **type**:

| Value     |                                                               | Schema                                    |
| --------- | ------------------------------------------------------------- | ----------------------------------------- |
| azureblob | These properties are returned for Azure Blob links.           | [Azure Blob Response](#ResponseAzureBlob) |
| couchbase | These properties are returned for remote Couchbase links.     | [Couchbase Response](#ResponseCouchbase)  |
| gcs       | These properties are returned for Google Cloud Storage links. | [GCS Response](#ResponseGCS)              |
| s3        | These properties are returned for S3 links.                   | [S3 Response](#ResponseS3)                |

#### Azure Blob Response

 Composite Schema

| All of …​ |                                          | Schema                                                     |
| --------- | ---------------------------------------- | ---------------------------------------------------------- |
|           | Properties common to all links.          | [Links](#ResponseAll)                                      |
| and       | Properties specific to Azure Blob links. | [Azure Blob Specific Response](#ResponseAzureBlobSpecific) |

#### Azure Blob Specific Response

 Object

Property

Schema

**accountKey**  
optional

The account key. Used for shared key authentication. This is redacted for the sake of security. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** ""  

String

**accountName**  
optional

The account name. Used for shared key authentication. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** `"myAccountName"`  

String

**clientCertificate**  
optional

The client certificate for the registered application. Used for Azure Active Directory client certificate authentication. This is redacted for the sake of security. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** ""  

String

**clientCertificatePassword**  
optional

The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. This is redacted for the sake of security. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** ""  

String

**clientId**  
optional

The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. If not set, this property returns `null`.

**Example:** `"myClientID"`  

String

**clientSecret**  
optional

The client secret for the registered application. Used for Azure Active Directory client secret authentication. This is redacted for the sake of security. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** ""  

String

**endpoint**  
required

The endpoint URI.

**Example:** `"my.endpoint.uri"`  

String

**managedIdentityId**  
optional

The managed identity ID. Used for managed identity authentication. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** `"myManagedIdentityID"`  

String

**sharedAccessSignature**  
optional

A token that can be used for authentication. Used for shared access signature authentication. This is redacted for the sake of security. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** ""  

String

**tenantId**  
optional

The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** `"myTenantID"`  

String

#### Couchbase Response

 Composite Schema

| All of …​ |                                                | Schema                                                    |
| --------- | ---------------------------------------------- | --------------------------------------------------------- |
|           | Properties common to all links.                | [Links](#ResponseAll)                                     |
| and       | Properties specific to remote Couchbase links. | [Couchbase Specific Response](#ResponseCouchbaseSpecific) |

#### Couchbase Specific Response

 Object

Property

Schema

**activeHostname**  
required

The remote hostname.

**Example:** `"remoteHostName:8091"`  

String

**bootstrapAlternateAddress**  
required

Specifies whether the provided (bootstrap) hostname is an alternative address.

**Example:** `false`  

Boolean

**bootstrapHostname**  
required

The provided (bootstrap) hostname.

**Example:** `"remoteHostName:8091"`  

String

**certificate**  
required

The content of the target cluster root certificate. Only set for links with full encryption. If not set, this property returns `null`.

**Nullable:** yes  

String

**clientCertificate**  
required

The content of the client certificate. Only set for links with full encryption using client certificate and client key. If not set, this property returns `null`.

**Nullable:** yes  

String

**clientKey**  
required

The content of the client key. Only set for links with full encryption using client certificate and client key. If not set, this property returns `null`.

**Nullable:** yes  

String

**clusterCompatibility**  
required

For internal use only.

**Example:** `393221`  

Integer

**encryption**  
required

The type of encryption used by the link.

* `none`: Neither passwords nor data are encrypted.
* `half`: Passwords are encrypted using SCRAM-SHA, but data is not.
* `full`: All data and passwords are encrypted and TLS is used.

**Values:** `"none"`, `"half"`, `"full"`  

String

**nodes**  
required

An array of objects, each of which contains information about a node in the target cluster.

[Nodes](#ResponseCouchbaseSpecificNode) array

**password**  
required

The password used to connect to the link. This is redacted for the sake of security. Not set for links with full encryption using client certificate and client key. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** ""  

String

**username**  
required

The remote username. Not set for links with full encryption using client certificate and client key. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** `"remote.user"`  

String

**uuid**  
required

A UUID uniquely identifying the link.

**Example:** `"6331e2a390125b662f7bcfd63ecb3a73"`  

UUID (UUID)

#### Nodes

 Object

| Property                       |                                                                                                                  | Schema                                             |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **alternateAddresses**optional | The alternate address defined on the node, if any. If not defined, this property returns null. **Nullable:** yes | String                                             |
| **hostname**optional           | The hostname of the node. If not defined, this property returns null. **Nullable:** yes                          | String                                             |
| **services**optional           | An object giving information about the services and ports configured on this node.                               | [Services](#ResponseCouchbaseSpecificNodeServices) |

#### Services

 Object

| Property            |                                                                                                | Schema  |
| ------------------- | ---------------------------------------------------------------------------------------------- | ------- |
| **cbas**optional    | The port number for a connection to the Analytics Service. **Example:** 8095                   | Integer |
| **cbasSSL**optional | The port number for an encrypted connection to the Analytics Service. **Example:** 18095       | Integer |
| **kv**optional      | The port number for a connection to the Data service. **Example:** 11210                       | Integer |
| **kvSSL**optional   | The port number for an encrypted connection to the Data service. **Example:** 11207            | Integer |
| **mgmt**optional    | The port number for a connection to the Cluster Manager service. **Example:** 8091             | Integer |
| **mgmtSSL**optional | The port number for an encrypted connection to the Cluster Manager service. **Example:** 18091 | Integer |

#### GCS Response

 Composite Schema

| All of …​ |                                                    | Schema                                        |
| --------- | -------------------------------------------------- | --------------------------------------------- |
|           | Properties common to all links.                    | [Links](#ResponseAll)                         |
| and       | Properties specific to Google Cloud Storage links. | [GCS Specific Response](#ResponseGCSSpecific) |

#### GCS Specific Response

 Object

Property

Schema

**applicationDefaultCredentials**  
required

If present, indicates that the link should use the Google Application Default Credentials for authenticating. If not set, this property returns `null`.

**Values:** `"true"`  
**Nullable:** yes  
**Example:** `"true"`  

String

**endpoint**  
required

The endpoint URI. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** `"https://storage.googleapis.com"`  

String

**jsonCredentials**  
required

The JSON credentials of the link. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** ""  

String

#### S3 Response

 Composite Schema

| All of …​ |                                  | Schema                                      |
| --------- | -------------------------------- | ------------------------------------------- |
|           | Properties common to all links.  | [Links](#ResponseAll)                       |
| and       | Properties specific to S3 links. | [S3 Specific Response](#ResponseS3Specific) |

#### S3 Specific Response

 Object

Property

Schema

**accessKeyId**  
required

The Amazon S3 access key ID.

**Example:** `"myAccessKey"`  

String

**region**  
required

The Amazon S3 region.

**Example:** `"us-east-1"`  

String

**secretAccessKey**  
required

The Amazon S3 secret access key. This is redacted for the sake of security.

**Example:** ""  

String

**sessionToken**  
optional

The Amazon S3 session token. Indicates that the link has temporary access, and that the `accessKeyId` and `secretAccessKey` are temporary credentials. This is redacted for the sake of security.

**Example:** ""  

String

**serviceEndpoint**  
required

Amazon S3 service endpoint. If not set, this property returns `null`.

**Nullable:** yes  
**Example:** `"my.endpoint.uri"`  

String

### [](#Wrong)Errors

 Object

| Property          |                   | Schema |
| ----------------- | ----------------- | ------ |
| **error**required | An error message. | String |

## [](#security)Security

The Analytics Links REST API supports HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-AnalyticsManage)Analytics Manage

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

**Type:** http

For more information, see [Roles](../learn/security/roles.md).