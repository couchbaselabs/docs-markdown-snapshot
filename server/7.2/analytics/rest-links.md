[View original HTML](/server/7.2/analytics/rest-links.html)

## [](#%5Foverview)Overview

The Analytics Links REST API is provided by the Analytics service. This API enables you to manage the links to remote Couchbase clusters and external data sources.

The API schemes and host URLs are as follows:

* <http://node:8095/>
* <https://node:18095/> (for secure access)

where `node` is the host name or IP address of a node running the Analytics service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#tags)Tags

* Single Links : Operations for single links.
* Multiple Links : Operations for multiple links.
* Legacy Methods : Operations provided for backward compatibility.

### [](#consumes)Consumes

* `application/x-www-form-urlencoded`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

* [Single Links](#%5Fsingle%5Flinks%5Fresource)
* [Multiple Links](#%5Fmultiple%5Flinks%5Fresource)
* [Legacy Methods](#%5Flegacy%5Fmethods%5Fresource)

### [](#%5Fsingle%5Flinks%5Fresource)Single Links

Operations for single links.

* [Create Link](#%5Fpost%5Flink)
* [Query Link](#%5Fget%5Flink)
* [Edit Link](#%5Fput%5Flink)
* [Delete Link](#%5Fdelete%5Flink)

#### [](#%5Fpost%5Flink)Create Link

POST /analytics/link/{scope}/{name}

##### [](#description)Description

Creates a link in the specified Analytics scope.

When creating or altering a remote link using an alternate address, note the following:

* At least one node in the remote cluster must expose the `mgmt` port (`rest_port`, default 8091) or the `mgmtSSL` port (`ssl_rest_port`, default 18091).
* Furthermore, **all** data nodes in the remote cluster must expose the `kv` port (`memcached_port`, default 11210) or the `kvSSL` port (`memcached_ssl_port`, default 11207).

Failure to do so will result in a 400 (Bad Request) error.

|  | The SSL ports are required when the **encryption** mode is set to full; the non-SSL ports are required otherwise. |
|  | ----------------------------------------------------------------------------------------------------------------- |

|  | When creating an external link, be sure to follow best practices for security. Root account credentials should never be used. It is recommended to grant the minimum possible permissions to perform the required operations, and only to allow access to the required data and resources. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

##### [](#parameters)Parameters

| Type         | Name                                         | Description                                                                                                                                                                                                                                                                                                                                                           | Schema                               |
| ------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Path**     | **scope** _required_                         | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters.                                                                                                                                                               | string                               |
| **Path**     | **name** _required_                          | The name of the link.                                                                                                                                                                                                                                                                                                                                                 | string                               |
| **FormData** | **type** _required_                          | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Azure Blob Storage. gcs: A link to Google Cloud Storage.                                                                                                                                                                             | enum (couchbase, s3, azureblob, gcs) |
| **FormData** | **hostname** _required_                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | string                               |
| **FormData** | **encryption** _required_                    | For Couchbase links only. The type of encryption used by the link. none: Neither passwords nor data are encrypted. half: Passwords are encrypted using SCRAM-SHA, but data is not. full: All data and passwords are encrypted and TLS is used.                                                                                                                        | enum (none, half, full)              |
| **FormData** | **username** _optional_                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **password** _optional_                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **certificate** _optional_                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | string                               |
| **FormData** | **clientCertificate** _optional_             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | string                               |
| **FormData** | **clientKey** _optional_                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | string                               |
| **FormData** | **accessKeyId** _required_                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | string                               |
| **FormData** | **secretAccessKey** _required_               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | string                               |
| **FormData** | **sessionToken** _optional_                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | string                               |
| **FormData** | **region** _required_                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | string                               |
| **FormData** | **serviceEndpoint** _optional_               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | string                               |
| **FormData** | **accountName** _optional_                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | string                               |
| **FormData** | **accountKey** _optional_                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | string                               |
| **FormData** | **sharedAccessSignature** _optional_         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | string                               |
| **FormData** | **managedIdentityId** _optional_             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | string                               |
| **FormData** | **clientId** _optional_                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | string                               |
| **FormData** | **tenantId** _optional_                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | string                               |
| **FormData** | **clientSecret** _optional_                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | string                               |
| **FormData** | **clientCertificatePassword** _optional_     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | string                               |
| **FormData** | **endpoint** _optional_                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | string                               |
| **FormData** | **applicationDefaultCredentials** _optional_ | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. This parameter may only have the value "true".                                                                                                                                                                     | enum (true)                          |
| **FormData** | **jsonCredentials** _optional_               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | string                               |

##### [](#responses)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | No Content           |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors) |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

##### [](#security)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

##### [](#example-http-request)Example HTTP request

The example below creates a Couchbase link named `myCbLink` in the `Default` scope, with no encryption.

Curl request

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

|  | The username and password parameters are URL-encoded to escape any special characters. |
|  | -------------------------------------------------------------------------------------- |

The example below creates a Microsoft Azure Blob link named `myBlobLink` in the `Default` scope, with anonymous authentication.

Curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/Default/myBlobLink" \
     -d type=azureblob \
     -d endpoint=my.endpoint.uri
```

The example below creates a Google Cloud Storage link named `myGcsLink` in the `Default` scope, with anonymous authentication.

Curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/Default/myGcsLink" \
     -d type=gcs
```

The example below creates an Amazon S3 link named `myAwsLink` in the `travel-sample.inventory` scope.

Curl request

```sh
curl -v -u Administrator:password \
     -X POST \
     "http://localhost:8095/analytics/link/travel-sample%2Finventory/myAwsLink" \
     -d type=s3 \
     -d region=us-east-1 \
     -d accessKeyId=myAccessKey \
     --data-urlencode secretAccessKey=mySecretKey
```

|  | The dot separator within the scope name is converted to a slash (/), which is then URL-encoded as %2F. The secretAccessKey parameter is URL-encoded to escape any special characters. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The example below creates an Amazon S3 link named `myTempLink` with temporary credentials in the `travel-sample.inventory` scope.

Curl request

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

|  | The dot separator within the scope name is converted to a slash (/), which is then URL-encoded as %2F. The secretAccessKey parameter is URL-encoded to escape any special characters. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#%5Fget%5Flink)Query Link

GET /analytics/link/{scope}/{name}

##### [](#description-2)Description

Returns information about a link in the specified Analytics scope.

##### [](#parameters-2)Parameters

| Type      | Name                 | Description                                                                                                                                                                                             | Schema                               |
| --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Path**  | **scope** _required_ | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | string                               |
| **Path**  | **name** _required_  | The name of the link.                                                                                                                                                                                   | string                               |
| **Query** | **type** _optional_  | The type of the link. If this parameter is specified, the value must match the type that was set when the link was created.                                                                             | enum (couchbase, S3, azureblob, gcs) |

##### [](#responses-2)Responses

| HTTP Code | Description                                                                                                                    | Schema                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **200**   | Success. Returns an array of objects, each of which contains information about a link.                                         | < [Links](#%5Flinks) \> array |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors)          |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors)          |

##### [](#security-2)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

##### [](#example-http-request-2)Example HTTP request

The example below queries the `myAwsLink` link in the `travel-sample.inventory` scope.

Curl request

```sh
curl -v -u Administrator:password \
     "http://localhost:8095/analytics/link/travel-sample%2Finventory/myAwsLink"
```

|  | The dot separator within the scope name is converted to a slash (/), which is then URL-encoded as %2F. |
|  | ------------------------------------------------------------------------------------------------------ |

##### [](#example-http-response)Example HTTP response

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

#### [](#%5Fput%5Flink)Edit Link

PUT /analytics/link/{scope}/{name}

##### [](#description-3)Description

Edits an existing link in the specified Analytics scope. The link name, type, and scope name cannot be modified.

##### [](#parameters-3)Parameters

| Type         | Name                                         | Description                                                                                                                                                                                                                                                                                                                                                           | Schema                               |
| ------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Path**     | **scope** _required_                         | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters.                                                                                                                                                               | string                               |
| **Path**     | **name** _required_                          | The name of the link.                                                                                                                                                                                                                                                                                                                                                 | string                               |
| **FormData** | **type** _optional_                          | The type of the link. If this parameter is specified, the value must match the type that was set when the link was created.                                                                                                                                                                                                                                           | enum (couchbase, s3, azureblob, gcs) |
| **FormData** | **hostname** _required_                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | string                               |
| **FormData** | **encryption** _required_                    | For Couchbase links only. The type of encryption used by the link. none: Neither passwords nor data are encrypted. half: Passwords are encrypted using SCRAM-SHA, but data is not. full: All data and passwords are encrypted and TLS is used.                                                                                                                        | enum (none, half, full)              |
| **FormData** | **username** _optional_                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **password** _optional_                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **certificate** _optional_                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | string                               |
| **FormData** | **clientCertificate** _optional_             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | string                               |
| **FormData** | **clientKey** _optional_                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | string                               |
| **FormData** | **accessKeyId** _required_                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | string                               |
| **FormData** | **secretAccessKey** _required_               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | string                               |
| **FormData** | **sessionToken** _optional_                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | string                               |
| **FormData** | **region** _required_                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | string                               |
| **FormData** | **serviceEndpoint** _optional_               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | string                               |
| **FormData** | **accountName** _optional_                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | string                               |
| **FormData** | **accountKey** _optional_                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | string                               |
| **FormData** | **sharedAccessSignature** _optional_         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | string                               |
| **FormData** | **managedIdentityId** _optional_             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | string                               |
| **FormData** | **clientId** _optional_                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | string                               |
| **FormData** | **tenantId** _optional_                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | string                               |
| **FormData** | **clientSecret** _optional_                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | string                               |
| **FormData** | **clientCertificatePassword** _optional_     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | string                               |
| **FormData** | **endpoint** _optional_                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | string                               |
| **FormData** | **applicationDefaultCredentials** _optional_ | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. This parameter may only have the value "true".                                                                                                                                                                     | enum (true)                          |
| **FormData** | **jsonCredentials** _optional_               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | string                               |

##### [](#responses-3)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | No Content           |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors) |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

##### [](#security-3)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

##### [](#example-http-request-3)Example HTTP request

The example below edits the link named `myCbLink` in the `Default` scope to use full encryption with a client certificate and client key.

Curl request

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

|  | The certificate, clientCertificate, and clientKey parameters use command substitution with the cat command to return the _content_ of the referenced files. The content of these files is then URL-encoded to escape any special characters. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The example below edits the Google Cloud Storage link named `myGcsLink` in the `Default` scope to use Google Application Default Credentials for authentication.

Curl request

```sh
curl -v -u Administrator:password \
     -X PUT \
     "http://localhost:8095/analytics/link/Default/myGcsLink" \
     -d type=gcs \
     -d applicationDefaultCredentials=true
```

#### [](#%5Fdelete%5Flink)Delete Link

DELETE /analytics/link/{scope}/{name}

##### [](#description-4)Description

Deletes a link in the specified Analytics scope. The link cannot be deleted if any other entities are using it, such as an Analytics collection. The entities using the link need to be disconnected from the link, otherwise, the delete operation fails.

##### [](#parameters-4)Parameters

| Type     | Name                 | Description                                                                                                                                                                                             | Schema |
| -------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **scope** _required_ | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | string |
| **Path** | **name** _required_  | The name of the link.                                                                                                                                                                                   | string |

##### [](#responses-4)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | No Content           |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors) |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

##### [](#security-4)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

##### [](#example-http-request-4)Example HTTP request

The example below deletes the link named `myCbLink` from the `Default` scope.

Curl request

```sh
curl -v -u Administrator:password \
     -X DELETE \
     "http://localhost:8095/analytics/link/Default/myCbLink"
```

The example below deletes the link named `myAwsLink` from the `travel-sample.inventory` scope.

Curl request

```sh
curl -v -u Administrator:password \
     -X DELETE \
     "http://localhost:8095/analytics/link/travel-sample%2Finventory/myAwsLink"
```

|  | The dot separator within the scope name is converted to a slash (/), which is then URL-encoded as %2F. |
|  | ------------------------------------------------------------------------------------------------------ |

### [](#%5Fmultiple%5Flinks%5Fresource)Multiple Links

Operations for multiple links.

* [Query All Links](#%5Fget%5Fall)
* [Query Scope Links](#%5Fget%5Fscope)

#### [](#%5Fget%5Fall)Query All Links

GET /analytics/link

##### [](#description-5)Description

Returns information about all links in all Analytics scopes.

##### [](#parameters-5)Parameters

| Type      | Name                     | Description                                                                                                                                                                                                                                                                                                                                     | Schema                               |
| --------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Query** | **dataverse** _optional_ | The name of an Analytics scope. When this parameter is included, the request only returns information about links in the specified scope. With this parameter, the scope name may only contain a single identifier. This parameter is provided for backward compatibility. Note that it is deprecated, and will be removed in a future release. | string                               |
| **Query** | **name** _optional_      | The name of a link. When this parameter is included, the request only returns information about the specified link. If specified, the dataverse parameter must be specified also. This parameter is provided for backward compatibility. Note that it is deprecated, and will be removed in a future release.                                   | string                               |
| **Query** | **type** _optional_      | The type of the link. If this parameter is omitted, all link types are retrieved, excluding the Local link.                                                                                                                                                                                                                                     | enum (couchbase, s3, azureblob, gcs) |

##### [](#responses-5)Responses

| HTTP Code | Description                                                                                                                    | Schema                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **200**   | Success. Returns an array of objects, each of which contains information about a link.                                         | < [Links](#%5Flinks) \> array |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors)          |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors)          |

##### [](#security-5)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

##### [](#example-http-request-5)Example HTTP request

The example below queries all links of type `S3` in all Analytics scopes.

Curl request

```sh
curl -v -u Administrator:password \
     "http://localhost:8095/analytics/link?type=S3"
```

##### [](#example-http-response-2)Example HTTP response

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

#### [](#%5Fget%5Fscope)Query Scope Links

GET /analytics/link/{scope}

##### [](#description-6)Description

Returns information about all links in the specified Analytics scope.

##### [](#parameters-6)Parameters

| Type      | Name                 | Description                                                                                                                                                                                             | Schema                               |
| --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Path**  | **scope** _required_ | The name of the Analytics scope. With this parameter, the scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | string                               |
| **Query** | **type** _optional_  | The type of the link. If this parameter is omitted, all link types are retrieved, excluding the Local link.                                                                                             | enum (couchbase, s3, azureblob, gcs) |

##### [](#responses-6)Responses

| HTTP Code | Description                                                                                                                    | Schema                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **200**   | Success. Returns an array of objects, each of which contains information about a link.                                         | < [Links](#%5Flinks) \> array |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors)          |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors)          |

##### [](#security-6)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

##### [](#example-http-request-6)Example HTTP request

The example below queries all links in the `Default` scope.

Curl request

```sh
curl -v -u Administrator:password \
     "http://localhost:8095/analytics/link/Default"
```

##### [](#example-http-response-3)Example HTTP response

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

### [](#%5Flegacy%5Fmethods%5Fresource)Legacy Methods

Operations provided for backward compatibility.

* [Create Link (Alternative)](#%5Fpost%5Falt)
* [Edit Link (Alternative)](#%5Fput%5Falt)
* [Delete Link (Alternative)](#%5Fdelete%5Falt)

#### [](#%5Fpost%5Falt)Create Link (Alternative)

POST /analytics/link

|  | operation.deprecated |
|  | -------------------- |

##### [](#description-7)Description

An alternative endpoint for [creating a link](#%5Fpost%5Flink), provided for backward compatibility.

##### [](#parameters-7)Parameters

| Type         | Name                                         | Description                                                                                                                                                                                                                                                                                                                                                           | Schema                               |
| ------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **FormData** | **dataverse** _required_                     | The name of the Analytics scope containing the link. With this parameter, the scope name may only contain a single identifier.                                                                                                                                                                                                                                        | string                               |
| **FormData** | **name** _required_                          | The name of the link.                                                                                                                                                                                                                                                                                                                                                 | string                               |
| **FormData** | **type** _required_                          | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Azure Blob Storage. gcs: A link to Google Cloud Storage.                                                                                                                                                                             | enum (couchbase, s3, azureblob, gcs) |
| **FormData** | **hostname** _required_                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | string                               |
| **FormData** | **encryption** _required_                    | For Couchbase links only. The type of encryption used by the link. none: Neither passwords nor data are encrypted. half: Passwords are encrypted using SCRAM-SHA, but data is not. full: All data and passwords are encrypted and TLS is used.                                                                                                                        | enum (none, half, full)              |
| **FormData** | **username** _optional_                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **password** _optional_                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **certificate** _optional_                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | string                               |
| **FormData** | **clientCertificate** _optional_             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | string                               |
| **FormData** | **clientKey** _optional_                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | string                               |
| **FormData** | **accessKeyId** _required_                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | string                               |
| **FormData** | **secretAccessKey** _required_               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | string                               |
| **FormData** | **sessionToken** _optional_                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | string                               |
| **FormData** | **region** _required_                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | string                               |
| **FormData** | **serviceEndpoint** _optional_               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | string                               |
| **FormData** | **accountName** _optional_                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | string                               |
| **FormData** | **accountKey** _optional_                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | string                               |
| **FormData** | **sharedAccessSignature** _optional_         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | string                               |
| **FormData** | **managedIdentityId** _optional_             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | string                               |
| **FormData** | **clientId** _optional_                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | string                               |
| **FormData** | **tenantId** _optional_                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | string                               |
| **FormData** | **clientSecret** _optional_                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | string                               |
| **FormData** | **clientCertificatePassword** _optional_     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | string                               |
| **FormData** | **endpoint** _optional_                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | string                               |
| **FormData** | **applicationDefaultCredentials** _optional_ | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. This parameter may only have the value "true".                                                                                                                                                                     | enum (true)                          |
| **FormData** | **jsonCredentials** _optional_               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | string                               |

##### [](#responses-7)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | No Content           |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors) |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

##### [](#security-7)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#%5Fput%5Falt)Edit Link (Alternative)

PUT /analytics/link

|  | operation.deprecated |
|  | -------------------- |

##### [](#description-8)Description

An alternative endpoint for [editing a link](#%5Fput%5Flink), provided for backward compatibility. The link name, type, and scope name cannot be modified.

##### [](#parameters-8)Parameters

| Type         | Name                                         | Description                                                                                                                                                                                                                                                                                                                                                           | Schema                               |
| ------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **FormData** | **dataverse** _required_                     | The name of the Analytics scope containing the link. With this parameter, the scope name may only contain a single identifier.                                                                                                                                                                                                                                        | string                               |
| **FormData** | **name** _required_                          | The name of the link.                                                                                                                                                                                                                                                                                                                                                 | string                               |
| **FormData** | **type** _optional_                          | The type of the link. If this parameter is specified, the value must match the type that was set when the link was created.                                                                                                                                                                                                                                           | enum (couchbase, s3, azureblob, gcs) |
| **FormData** | **hostname** _required_                      | For Couchbase links only. The remote hostname.                                                                                                                                                                                                                                                                                                                        | string                               |
| **FormData** | **encryption** _required_                    | For Couchbase links only. The type of encryption used by the link. none: Neither passwords nor data are encrypted. half: Passwords are encrypted using SCRAM-SHA, but data is not. full: All data and passwords are encrypted and TLS is used.                                                                                                                        | enum (none, half, full)              |
| **FormData** | **username** _optional_                      | For Couchbase links only. The remote username. Required for links with no encryption or half encryption. Required for links with full encryption if using a password. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **password** _optional_                      | For Couchbase links only. The remote password. Required for links with no encryption or half encryption. Required for links with full encryption if using a username. You should URL-encode this parameter to escape any special characters.                                                                                                                          | string                               |
| **FormData** | **certificate** _optional_                   | For Couchbase links only. The content of the target cluster root certificate. Required for links with full encryption. You should URL-encode this parameter to escape any special characters. If required, this parameter may contain multiple certificates, separated by new lines.                                                                                  | string                               |
| **FormData** | **clientCertificate** _optional_             | For Couchbase links, this is the content of the client certificate. Required for links with full encryption if using a client key. For Azure Blob links, this is the client certificate for the registered application. Used for Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.     | string                               |
| **FormData** | **clientKey** _optional_                     | For Couchbase links only. The content of the client key. Required for links with full encryption if using a client certificate. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                | string                               |
| **FormData** | **accessKeyId** _required_                   | For S3 links only. The Amazon S3 access key ID.                                                                                                                                                                                                                                                                                                                       | string                               |
| **FormData** | **secretAccessKey** _required_               | For S3 links only. The Amazon S3 secret access key. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                                            | string                               |
| **FormData** | **sessionToken** _optional_                  | For S3 links only. The Amazon S3 session token. Use this parameter if you want the link to have temporary access. Passing this parameter indicates that the accessKeyId and secretAccessKey are temporary credentials. The Amazon S3 service validates the session token with each request to check whether the provided credentials have expired or are still valid. | string                               |
| **FormData** | **region** _required_                        | For S3 links only. The Amazon S3 region.                                                                                                                                                                                                                                                                                                                              | string                               |
| **FormData** | **serviceEndpoint** _optional_               | For S3 links only. The Amazon S3 service endpoint.                                                                                                                                                                                                                                                                                                                    | string                               |
| **FormData** | **accountName** _optional_                   | For Azure Blob links only. The account name. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                               | string                               |
| **FormData** | **accountKey** _optional_                    | For Azure Blob links only. The account key. Used for shared key authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                                                                | string                               |
| **FormData** | **sharedAccessSignature** _optional_         | For Azure Blob links only. A token that can be used for authentication. Used for shared access signature authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                                       | string                               |
| **FormData** | **managedIdentityId** _optional_             | For Azure Blob links only. The managed identity ID. Used for managed identity authentication. Only available if the application is running on an Azure instance, e.g. an Azure virtual machine. You should URL-encode this parameter to escape any special characters.                                                                                                | string                               |
| **FormData** | **clientId** _optional_                      | For Azure Blob links only. The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                                            | string                               |
| **FormData** | **tenantId** _optional_                      | For Azure Blob links only. The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. You should URL-encode this parameter to escape any special characters.                                                                               | string                               |
| **FormData** | **clientSecret** _optional_                  | For Azure Blob links only. The client secret for the registered application. Used for Azure Active Directory client secret authentication. You should URL-encode this parameter to escape any special characters.                                                                                                                                                     | string                               |
| **FormData** | **clientCertificatePassword** _optional_     | For Azure Blob links only. The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. You should URL-encode this parameter to escape any special characters.                                                                                 | string                               |
| **FormData** | **endpoint** _optional_                      | For Azure Blob links and Google Cloud Storage links. The endpoint URI. Required for Azure Blob links; optional for Google Cloud Storage links.                                                                                                                                                                                                                        | string                               |
| **FormData** | **applicationDefaultCredentials** _optional_ | For Google Cloud Storage links only. If present, indicates that the link should use the Google Application Default Credentials for authenticating. This parameter may only have the value "true".                                                                                                                                                                     | enum (true)                          |
| **FormData** | **jsonCredentials** _optional_               | For Google Cloud Storage links only. The JSON credentials of the link. This parameter is not allowed if applicationDefaultCredentials is provided.                                                                                                                                                                                                                    | string                               |

##### [](#responses-8)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | No Content           |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors) |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

##### [](#security-8)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#%5Fdelete%5Falt)Delete Link (Alternative)

DELETE /analytics/link

|  | operation.deprecated |
|  | -------------------- |

##### [](#description-9)Description

An alternative endpoint for [deleting a link](#%5Fdelete%5Flink), provided for backward compatibility. The link cannot be deleted if any other entities are using it, such as an Analytics collection. The entities using the link need to be disconnected from the link, otherwise, the delete operation fails.

##### [](#parameters-9)Parameters

| Type         | Name                     | Description                                                                                                                    | Schema |
| ------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **FormData** | **dataverse** _required_ | The name of the Analytics scope containing the link. With this parameter, the scope name may only contain a single identifier. | string |
| **FormData** | **name** _required_      | The name of the link.                                                                                                          | string |

##### [](#responses-9)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | No Content           |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors) |
| **500**   | Internal Server Error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

##### [](#security-9)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

## [](#%5Fdefinitions)Definitions

This section describes the properties returned by this REST API.

* [Links](#%5Flinks)
* [Errors](#%5Ferrors)

### [](#%5Flinks)Links

These properties are common to all links.

| Name                 | Description                                                                                                                                                                                                                                                                                                                                                            | Schema                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **scope** _required_ | The name of the Analytics scope containing the link. The scope name may contain one or two identifiers, separated by a slash (/). **Example** : "travel-sample/inventory"                                                                                                                                                                                              | string                               |
| **name** _required_  | The name of the link. **Example** : "myLink"                                                                                                                                                                                                                                                                                                                           | string                               |
| **type** _required_  | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Microsoft Azure Blob Storage. gcs: A link to Google Cloud Storage. Different properties are returned, depending on the link type: refer to [Couchbase](#%5Fcouchbase), [S3](#%5Fs3), [Azure Blob](#%5Fazure-blob), or [GCS](#%5Fgcs). | enum (couchbase, s3, azureblob, gcs) |

### [](#%5Fcouchbase)Couchbase

These properties are returned for remote Couchbase links.

_Polymorphism_ : Inheritance  
_Discriminator_ : type

| Name                                     | Description                                                                                                                                                                                                                                                                                                                                                            | Schema                               |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **scope** _required_                     | The name of the Analytics scope containing the link. The scope name may contain one or two identifiers, separated by a slash (/). **Example** : "travel-sample/inventory"                                                                                                                                                                                              | string                               |
| **name** _required_                      | The name of the link. **Example** : "myLink"                                                                                                                                                                                                                                                                                                                           | string                               |
| **type** _required_                      | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Microsoft Azure Blob Storage. gcs: A link to Google Cloud Storage. Different properties are returned, depending on the link type: refer to [Couchbase](#%5Fcouchbase), [S3](#%5Fs3), [Azure Blob](#%5Fazure-blob), or [GCS](#%5Fgcs). | enum (couchbase, s3, azureblob, gcs) |
| **activeHostname** _required_            | The remote hostname. **Example** : "remoteHostName:8091"                                                                                                                                                                                                                                                                                                               | string                               |
| **bootstrapAlternateAddress** _required_ | Specifies whether the provided (bootstrap) hostname is an alternative address. **Example** : false                                                                                                                                                                                                                                                                     | boolean                              |
| **bootstrapHostname** _required_         | The provided (bootstrap) hostname. **Example** : "remoteHostName:8091"                                                                                                                                                                                                                                                                                                 | string                               |
| **certificate** _required_               | The content of the target cluster root certificate. Only set for links with full encryption. If not set, this property returns null.                                                                                                                                                                                                                                   | string                               |
| **clientCertificate** _required_         | The content of the client certificate. Only set for links with full encryption using client certificate and client key. If not set, this property returns null.                                                                                                                                                                                                        | string                               |
| **clientKey** _required_                 | The content of the client key. Only set for links with full encryption using client certificate and client key. If not set, this property returns null.                                                                                                                                                                                                                | string                               |
| **clusterCompatibility** _required_      | For internal use only. **Example** : 393221                                                                                                                                                                                                                                                                                                                            | integer                              |
| **encryption** _required_                | The type of encryption used by the link. none: Neither passwords nor data are encrypted. half: Passwords are encrypted using SCRAM-SHA, but data is not. full: All data and passwords are encrypted and TLS is used.                                                                                                                                                   | enum (none, half, full)              |
| **nodes** _required_                     | An array of objects, each of which contains information about a node in the target cluster.                                                                                                                                                                                                                                                                            | < [Nodes](#%5Fnodes) \> array        |
| **password** _required_                  | The password used to connect to the link. This is redacted for the sake of security. Not set for links with full encryption using client certificate and client key. If not set, this property returns null. **Example** : "<redacted sensitive entry>"                                                                                                                | string                               |
| **username** _required_                  | The remote username. Not set for links with full encryption using client certificate and client key. If not set, this property returns null. **Example** : "remote.user"                                                                                                                                                                                               | string                               |
| **uuid** _required_                      | A UUID uniquely identifying the link. **Example** : "6331e2a390125b662f7bcfd63ecb3a73"                                                                                                                                                                                                                                                                                 | string (UUID)                        |

**Nodes**

| Name                              | Description                                                                                    | Schema                   |
| --------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------ |
| **alternateAddresses** _optional_ | The alternate address defined on the node, if any. If not defined, this property returns null. | string                   |
| **hostname** _optional_           | The hostname of the node. If not defined, this property returns null.                          | string                   |
| **services** _optional_           | An object giving information about the services and ports configured on this node.             | [Services](#%5Fservices) |

**Services**

| Name                   | Description                                                                                     | Schema  |
| ---------------------- | ----------------------------------------------------------------------------------------------- | ------- |
| **cbas** _optional_    | The port number for a connection to the Analytics service. **Example** : 8095                   | integer |
| **cbasSSL** _optional_ | The port number for an encrypted connection to the Analytics service. **Example** : 18095       | integer |
| **kv** _optional_      | The port number for a connection to the Data service. **Example** : 11210                       | integer |
| **kvSSL** _optional_   | The port number for an encrypted connection to the Data service. **Example** : 11207            | integer |
| **mgmt** _optional_    | The port number for a connection to the Cluster Manager service. **Example** : 8091             | integer |
| **mgmtSSL** _optional_ | The port number for an encrypted connection to the Cluster Manager service. **Example** : 18091 | integer |

### [](#%5Fs3)S3

These properties are returned for S3 links.

_Polymorphism_ : Inheritance  
_Discriminator_ : type

| Name                           | Description                                                                                                                                                                                                                                                                                                                                                            | Schema                               |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **scope** _required_           | The name of the Analytics scope containing the link. The scope name may contain one or two identifiers, separated by a slash (/). **Example** : "travel-sample/inventory"                                                                                                                                                                                              | string                               |
| **name** _required_            | The name of the link. **Example** : "myLink"                                                                                                                                                                                                                                                                                                                           | string                               |
| **type** _required_            | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Microsoft Azure Blob Storage. gcs: A link to Google Cloud Storage. Different properties are returned, depending on the link type: refer to [Couchbase](#%5Fcouchbase), [S3](#%5Fs3), [Azure Blob](#%5Fazure-blob), or [GCS](#%5Fgcs). | enum (couchbase, s3, azureblob, gcs) |
| **accessKeyId** _required_     | The Amazon S3 access key ID. **Example** : "myAccessKey"                                                                                                                                                                                                                                                                                                               | string                               |
| **region** _required_          | The Amazon S3 region. **Example** : "us-east-1"                                                                                                                                                                                                                                                                                                                        | string                               |
| **secretAccessKey** _required_ | The Amazon S3 secret access key. This is redacted for the sake of security. **Example** : "<redacted sensitive entry>"                                                                                                                                                                                                                                                 | string                               |
| **sessionToken** _optional_    | For S3 links only. The Amazon S3 session token. Indicates that the link has temporary access, and that the accessKeyId and secretAccessKey are temporary credentials. This is redacted for the sake of security. **Example** : "<redacted sensitive entry>"                                                                                                            | string                               |
| **serviceEndpoint** _required_ | Amazon S3 service endpoint. If not set, this property returns null. **Example** : "my.endpoint.uri"                                                                                                                                                                                                                                                                    | string                               |

### [](#%5Fazure%5Fblob)Azure Blob

These properties are returned for Azure Blob links.

_Polymorphism_ : Inheritance  
_Discriminator_ : type

| Name                                     | Description                                                                                                                                                                                                                                                                                                                                                            | Schema                               |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **scope** _required_                     | The name of the Analytics scope containing the link. The scope name may contain one or two identifiers, separated by a slash (/). **Example** : "travel-sample/inventory"                                                                                                                                                                                              | string                               |
| **name** _required_                      | The name of the link. **Example** : "myLink"                                                                                                                                                                                                                                                                                                                           | string                               |
| **type** _required_                      | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Microsoft Azure Blob Storage. gcs: A link to Google Cloud Storage. Different properties are returned, depending on the link type: refer to [Couchbase](#%5Fcouchbase), [S3](#%5Fs3), [Azure Blob](#%5Fazure-blob), or [GCS](#%5Fgcs). | enum (couchbase, s3, azureblob, gcs) |
| **accountKey** _optional_                | The account key. Used for shared key authentication. This is redacted for the sake of security. If not set, this property returns null. **Example** : "<redacted sensitive entry>"                                                                                                                                                                                     | string                               |
| **accountName** _optional_               | The account name. Used for shared key authentication. If not set, this property returns null. **Example** : "myAccountName"                                                                                                                                                                                                                                            | string                               |
| **clientCertificate** _optional_         | The client certificate for the registered application. Used for Azure Active Directory client certificate authentication. This is redacted for the sake of security. If not set, this property returns null. **Example** : "<redacted sensitive entry>"                                                                                                                | string                               |
| **clientCertificatePassword** _optional_ | The client certificate password for the registered application. Used for Azure Active Directory client certificate authentication, if the client certificate is password-protected. This is redacted for the sake of security. If not set, this property returns null. **Example** : "<redacted sensitive entry>"                                                      | string                               |
| **clientId** _optional_                  | The client ID for the registered application. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. If not set, this property returns null. **Example** : "myClientID"                                                                                                                            | string                               |
| **clientSecret** _optional_              | The client secret for the registered application. Used for Azure Active Directory client secret authentication. This is redacted for the sake of security. If not set, this property returns null. **Example** : "<redacted sensitive entry>"                                                                                                                          | string                               |
| **endpoint** _required_                  | The endpoint URI. **Example** : "my.endpoint.uri"                                                                                                                                                                                                                                                                                                                      | string                               |
| **managedIdentityId** _optional_         | The managed identity ID. Used for managed identity authentication. If not set, this property returns null. **Example** : "myManagedIdentityID"                                                                                                                                                                                                                         | string                               |
| **sharedAccessSignature** _optional_     | A token that can be used for authentication. Used for shared access signature authentication. This is redacted for the sake of security. If not set, this property returns null. **Example** : "<redacted sensitive entry>"                                                                                                                                            | string                               |
| **tenantId** _optional_                  | The tenant ID where the registered application is created. Used for Azure Active Directory client secret authentication, or Azure Active Directory client certificate authentication. If not set, this property returns null. **Example** : "myTenantID"                                                                                                               | string                               |

### [](#%5Fgcs)GCS

These properties are returned for Google Cloud Storage links.

_Polymorphism_ : Inheritance  
_Discriminator_ : type

| Name                                         | Description                                                                                                                                                                                                                                                                                                                                                            | Schema                               |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **scope** _required_                         | The name of the Analytics scope containing the link. The scope name may contain one or two identifiers, separated by a slash (/). **Example** : "travel-sample/inventory"                                                                                                                                                                                              | string                               |
| **name** _required_                          | The name of the link. **Example** : "myLink"                                                                                                                                                                                                                                                                                                                           | string                               |
| **type** _required_                          | The type of the link. couchbase: A link to a remote Couchbase cluster. s3: A link to the Amazon S3 service. azureblob: A link to Microsoft Azure Blob Storage. gcs: A link to Google Cloud Storage. Different properties are returned, depending on the link type: refer to [Couchbase](#%5Fcouchbase), [S3](#%5Fs3), [Azure Blob](#%5Fazure-blob), or [GCS](#%5Fgcs). | enum (couchbase, s3, azureblob, gcs) |
| **applicationDefaultCredentials** _required_ | If present, indicates that the link should use the Google Application Default Credentials for authenticating. If not set, this property returns null. **Example** : "true"                                                                                                                                                                                             | enum (true)                          |
| **endpoint** _required_                      | The endpoint URI. If not set, this property returns null. **Example** : "https://storage.googleapis.com"                                                                                                                                                                                                                                                               | string                               |
| **jsonCredentials** _required_               | The JSON credentials of the link. If not set, this property returns null. **Example** : "<redacted sensitive entry>"                                                                                                                                                                                                                                                   | string                               |

### [](#%5Ferrors)Errors

| Name                 | Description       | Schema |
| -------------------- | ----------------- | ------ |
| **error** _required_ | An error message. | string |

## [](#%5Fsecurityscheme)Security

### [](#%5Fanalytics%5Fmanage)Analytics Manage

The Analytics Links REST API supports HTTP basic authentication. Credentials can be passed via HTTP headers.

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

Refer to [Roles](../learn/security/roles.html) for more details.

_Type_ : basic