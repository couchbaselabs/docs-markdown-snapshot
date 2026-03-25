---
title: Public REST API (Static Page)
description: Description of the Sync Gateway Public REST API, alternative
  representation as a static page
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/rest_api_public_static.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::rest_api_public_static.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/rest_api_public_static.html)

# Public REST API (Static Page)

> Description of the Sync Gateway Public REST API, alternative representation as a static page  

Related _REST API_ topics: [Admin REST API (Static Page)](rest%5Fapi%5Fadmin%5Fstatic.md) | [Metrics REST API (Static Page)](rest%5Fapi%5Fmetrics%5Fstatic.md)

## [](#%5Fpaths)Resources

This resources section groups together the available API operations under functional categories.

* [Attachment](#%5Fattachment%5Fresource)
* [Authentication](#%5Fauthentication%5Fresource)
* [Database](#%5Fdatabase%5Fresource)
* [Document](#%5Fdocument%5Fresource)
* [Document (local)](#%5Fdocument%5Flocal%5Fresource)
* [Server](#%5Fserver%5Fresource)
* [Session](#%5Fsession%5Fresource)

### [](#%5Fattachment%5Fresource)Attachment

Work with attachments

#### [](#%5Fgetattachment)Get Specific Attachment

GET /{db}/{doc}/{attachment}

##### [](#description)Description

This request retrieves a file attachment associated with the document. The raw data of the associated attachment is returned (just as if you were accessing a static file). The Content-Type response header is the same content type set when the document attachment was added to the database.

To remove an attachment from a document, simply update the `_attachments` dictionary of the document in the PUT `/{db}/{id}` request. From then on, the attachment will not be replicated but will still reside in the Couchbase Server bucket (see open ticket [#1648](https://github.com/couchbase/sync%5Fgateway/issues/1648)).

##### [](#parameters)Parameters

| Type      | Name                      | Description                                                                                                                                                                                                                    | Schema |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **Path**  | **attachment** _required_ | Attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | string |
| **Path**  | **db** _required_         | Database name                                                                                                                                                                                                                  | string |
| **Path**  | **doc** _required_        | Document ID                                                                                                                                                                                                                    | string |
| **Query** | **rev** _optional_        | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.)                                                                                                                | string |

##### [](#responses)Responses

| HTTP Code | Description                                                                                   | Schema          |
| --------- | --------------------------------------------------------------------------------------------- | --------------- |
| **200**   | The message body contains the attachment, in the format specified in the Content-Type header. | string (binary) |
| **304**   | Not Modified, the attachment wasn’t modified if ETag equals the If-None-Match header          | No Content      |
| **404**   | Not Found, the specified database, document or attachment was not found.                      | No Content      |

#### [](#%5Fupdateattachment)Create or Update Specific Attachment

PUT /{db}/{doc}/{attachment}

##### [](#description-2)Description

This request adds or updates the supplied request content as an attachment to the specified document, the maximum content size of an attachment is 20MB. The attachment name must be a URL-encoded string (the file name). You must also supply either the rev query parameter or the If-Match HTTP header for validation, and the Content-Type headers (to set the attachment content type).

When uploading an attachment using an existing attachment name, the corresponding stored content of the database will be updated. Because you must supply the revision information to add an attachment to the document, this serves as validation to update the existing attachment.

Uploading an attachment updates the corresponding document revision. Revisions are tracked for the parent document, not individual attachments.

To remove an attachment from a document, simply update the `_attachments` dictionary of the document in the PUT `/{db}/{id}` request. From then on, the attachment will not be replicated but will still reside in the Couchbase Server bucket (see open ticket [#1648](https://github.com/couchbase/sync%5Fgateway/issues/1648)).

##### [](#parameters-2)Parameters

| Type       | Name                        | Description                                                                                                                                                                                                                    | Schema          |
| ---------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| **Header** | **Content-Type** _optional_ | Attachment Content-Type                                                                                                                                                                                                        | string          |
| **Path**   | **attachment** _required_   | Attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | string          |
| **Path**   | **db** _required_           | Database name                                                                                                                                                                                                                  | string          |
| **Path**   | **doc** _required_          | Document ID                                                                                                                                                                                                                    | string          |
| **Query**  | **rev** _optional_          | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.)                                                                                                                | string          |
| **Body**   | **body** _optional_         | The request body                                                                                                                                                                                                               | string (binary) |

##### [](#responses-2)Responses

| HTTP Code | Description                                                              | Schema                 |
| --------- | ------------------------------------------------------------------------ | ---------------------- |
| **200**   | Operation completed successfully                                         | [Success](#%5Fsuccess) |
| **409**   | Conflict, the document revision wasn’t specified or it’s not the latest. | No Content             |

### [](#%5Fauthentication%5Fresource)Authentication

Work with authentication

#### [](#%5Fauthenticationviafacebook)Get Facebook Authenticated Session

POST /{db}/_facebook

##### [](#description-3)Description

Sync Gateway allows users to authenticate using a Facebook account.

Your application is responsible for generating a Facebook token; this generally needs to be done by running the Facebook login flow inside a web-view and capturing the generated token. This endpoint can be used to check the validity of the access token. To allow Facebook Login with Sync Gateway, it must be explicitly enabled in the Sync Gateway configuration file by setting the [facebook.register](config-properties.html#facebook-register) property to `true`.

##### [](#parameters-3)Parameters

| Type     | Name                | Description   | Schema                                       |
| -------- | ------------------- | ------------- | -------------------------------------------- |
| **Path** | **db** _required_   | Database name | string                                       |
| **Body** | **body** _optional_ | Request body  | [body](#%5Fauthenticationviafacebook%5Fbody) |

**body**

| Name                         | Description                                   | Schema |
| ---------------------------- | --------------------------------------------- | ------ |
| **access\_token** _optional_ | The access token for the user to authenticate | string |

##### [](#responses-3)Responses

| HTTP Code | Description                                                                                    | Schema                 |
| --------- | ---------------------------------------------------------------------------------------------- | ---------------------- |
| **200**   | Session successfully created. The Set-Cookie response header contains the session credentials. | [Session](#%5Fsession) |
| **401**   | Facebook verification server status <Facebook status code>                                     | No Content             |
| **502**   | Invalid response from Facebook verifier                                                        | No Content             |

#### [](#%5Fauthenticationviagoogle)Get Google Authenticated Session

POST /{db}/_google

##### [](#description-4)Description

Sync Gateway allows users to authenticate using a Google account.

Your application is responsible for generating a Google token; this generally needs to be done by running the Google login flow inside a web-view and capturing the generated token. This endpoint can be used to check the validity of the access token. To allow Google Login with Sync Gateway, it must be explicitly enabled in the Sync Gateway configuration file by setting the [google.register](config-properties.html#google-register) property to `true` and setting the [google.app\_client\_id](config-properties.html#google-app%5Fclient%5Fid) property with a Google app client ID.

##### [](#parameters-4)Parameters

| Type     | Name                | Description   | Schema                                     |
| -------- | ------------------- | ------------- | ------------------------------------------ |
| **Path** | **db** _required_   | Database name | string                                     |
| **Body** | **body** _optional_ | Request body  | [body](#%5Fauthenticationviagoogle%5Fbody) |

**body**

| Name                     | Description                                   | Schema |
| ------------------------ | --------------------------------------------- | ------ |
| **id\_token** _optional_ | The access token for the user to authenticate | string |

##### [](#responses-4)Responses

| HTTP Code | Description                                                                                    | Schema                 |
| --------- | ---------------------------------------------------------------------------------------------- | ---------------------- |
| **200**   | Session successfully created. The Set-Cookie response header contains the session credentials. | [Session](#%5Fsession) |
| **401**   | Returns the Google response’s ErrorDescription                                                 | No Content             |
| **502**   | Invalid response from Google token verifier                                                    | No Content             |

#### [](#%5Fgetopenid)OpenID Connect Authentication.

GET /{db}/_oidc

##### [](#description-5)Description

Called by clients to initiate the OIDC Authorization Code flow.

##### [](#parameters-5)Parameters

| Type      | Name                    | Description                                                                                                                                                                                                               | Schema  |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Path**  | **db** _required_       | Database name                                                                                                                                                                                                             | string  |
| **Query** | **offline** _optional_  | When true, requests a refresh token from the OP. Sets access\_type=offline and prompt=consent on the redirect to the OP. Secure clients should set offline=true and persist the returned refresh token to secure storage. | boolean |
| **Query** | **provider** _optional_ | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider.                          | string  |

##### [](#responses-5)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                               | Schema     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **302**   | Redirect to the requested OpenID Connect provider for authentication. Redirect link is returned in the Location header.                                                                                                                                                                   | No Content |
| **400**   | Bad request. Reason is returned as "OpenID Connect not configured for database default". If a provider was specified in the request, that provider was not defined in the Sync Gateway config. If no provider was specified, OpenID Connect is not configured in the Sync Gateway config. | No Content |
| **500**   | Server Error. Sync Gateway is unable to connect and validate the OpenID Connect provider requested.                                                                                                                                                                                       | No Content |

#### [](#%5Fgetopenidauthcallback)Get OIDC Callback.

GET /{db}/_oidc_callback

##### [](#description-6)Description

Sync Gateway callback URL that clients are redirected to by the OpenID Connect provider.

##### [](#parameters-6)Parameters

| Type      | Name                    | Description                                                                                                                                                                                      | Schema |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **Path**  | **db** _required_       | Database name                                                                                                                                                                                    | string |
| **Query** | **code** _required_     | OpenID Connect Authorization code.                                                                                                                                                               | string |
| **Query** | **provider** _optional_ | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider. | string |

##### [](#responses-6)Responses

| HTTP Code | Description                                                  | Schema                                                     |
| --------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| **200**   | Successful OpenID Connect authentication.                    | [Response 200](#%5Fgetopenidauthcallback%5Fresponse%5F200) |
| **400**   | Bad request.                                                 | No Content                                                 |
| **401**   | Authentication failed. Reason returned in the response body. | No Content                                                 |

**Response 200**

| Name                          | Description                  | Schema |
| ----------------------------- | ---------------------------- | ------ |
| **access\_token** _optional_  | OpenID Connect access token  | string |
| **expires\_in** _optional_    | TTL for id\_token            | number |
| **id\_token** _optional_      | OpenID Connect ID token      | string |
| **name** _optional_           | Sync Gateway username        | string |
| **refresh\_token** _optional_ | OpenID Connect refresh token | string |
| **session\_id** _optional_    | Sync Gateway session token   | string |
| **token\_type** _optional_    | OpenID Connect token type    | string |

#### [](#%5Fgetopenidauth)Get OIDC Authentication.

GET /{db}/_oidc_challenge

##### [](#description-7)Description

Called by clients to initiate the OIDC Authorization Code flow.

##### [](#parameters-7)Parameters

| Type      | Name                    | Description                                                                                                                                                                                                               | Schema  |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Path**  | **db** _required_       | Database name                                                                                                                                                                                                             | string  |
| **Query** | **offline** _optional_  | When true, requests a refresh token from the OP. Sets access\_type=offline and prompt=consent on the redirect to the OP. Secure clients should set offline=true and persist the returned refresh token to secure storage. | boolean |
| **Query** | **provider** _optional_ | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider.                          | string  |

##### [](#responses-7)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                               | Schema     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **302**   | Redirect to the requested OpenID Connect provider for authentication. Redirect link is returned in the Location header.                                                                                                                                                                   | No Content |
| **400**   | Bad request. Reason is returned as "OpenID Connect not configured for database default". If a provider was specified in the request, that provider was not defined in the Sync Gateway config. If no provider was specified, OpenID Connect is not configured in the Sync Gateway config. | No Content |
| **500**   | Server Error. Sync Gateway is unable to connect and validate the OpenID Connect provider requested.                                                                                                                                                                                       | No Content |

#### [](#%5Fgetopenidrefreshtoken)Get OIDC Refresh.

GET /{db}/_oidc_refresh

##### [](#description-8)Description

Used to obtain a new OpenID Connect ID token based on the provided refresh token.

##### [](#parameters-8)Parameters

| Type      | Name                          | Description                                                                                                                                                                                      | Schema |
| --------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **Path**  | **db** _required_             | Database name                                                                                                                                                                                    | string |
| **Query** | **provider** _optional_       | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider. | string |
| **Query** | **refresh\_token** _required_ | OpenID Connect refresh token.                                                                                                                                                                    | string |

##### [](#responses-8)Responses

| HTTP Code | Description                                     | Schema                                                     |
| --------- | ----------------------------------------------- | ---------------------------------------------------------- |
| **200**   | Successful OpenID Connect authentication.       | [Response 200](#%5Fgetopenidrefreshtoken%5Fresponse%5F200) |
| **400**   | Bad request.                                    | No Content                                                 |
| **401**   | Authentication failed. Unable to refresh token. | No Content                                                 |

**Response 200**

| Name                         | Description                 | Schema |
| ---------------------------- | --------------------------- | ------ |
| **access\_token** _optional_ | OpenID Connect access token | string |
| **expires\_in** _optional_   | TTL for id\_token           | number |
| **id\_token** _optional_     | OpenID Connect ID token     | string |
| **name** _optional_          | Sync Gateway username       | string |
| **session\_id** _optional_   | Sync Gateway session token  | string |
| **token\_type** _optional_   | OpenID Connect token type   | string |

### [](#%5Fdatabase%5Fresource)Database

Work with databases

#### [](#%5Fgetdatabaseinfo)Get Database Data

GET /{db}/

##### [](#description-9)Description

This request retrieves information about the database.

##### [](#parameters-9)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-9)Responses

| HTTP Code | Description                              | Schema                   |
| --------- | ---------------------------------------- | ------------------------ |
| **200**   | Request completed successfully.          | [Database](#%5Fdatabase) |
| **401**   | Unauthorized. Login required.            | No Content               |
| **404**   | Not Found. Requested database not found. | No Content               |

#### [](#%5Fgetalldocswithparametersinbody)Get All Specified Documents

POST /{db}/_all_docs

##### [](#description-10)Description

This request retrieves specified documents from the database.

##### [](#parameters-10)Parameters

| Type      | Name                         | Description                                                                                                                                                                                                                                                       | Schema                 | Default |
| --------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------- |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                                                                                                     | string                 |         |
| **Query** | **access** _optional_        | Indicates whether to include in the response a list of what access this document grants (i.e. which users it allows to access which channels.) This option may only be used from the admin port.                                                                  | boolean                | "false" |
| **Query** | **channels** _optional_      | Indicates whether to include in the response a channels property containing an array of channels this document is assigned to. (Channels not accessible by the user making the request will not be listed.)                                                       | boolean                | "false" |
| **Query** | **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned.                                                                                                           | boolean                | "false" |
| **Query** | **revs** _optional_          | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter. | boolean                | "false" |
| **Query** | **update\_seq** _optional_   | Default is false. Indicates whether to include the update\_seq (document sequence ID) property in the response.                                                                                                                                                   | boolean                | "false" |
| **Body**  | **body** _optional_          | Request body                                                                                                                                                                                                                                                      | [AllDocs](#%5Falldocs) |         |

##### [](#responses-10)Responses

| HTTP Code | Description   | Schema                         |
| --------- | ------------- | ------------------------------ |
| **200**   | Query results | [QueryResult](#%5Fqueryresult) |

#### [](#%5Fgetalldocs)Get All Docs

GET /{db}/_all_docs

##### [](#description-11)Description

This request returns a built-in view of all the documents in the database.

##### [](#parameters-11)Parameters

| Type      | Name                         | Description                                                                                                                                                                                                                                                       | Schema           | Default |
| --------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------- |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                                                                                                     | string           |         |
| **Query** | **access** _optional_        | Indicates whether to include in the response a list of what access this document grants (i.e. which users it allows to access which channels.) This option may only be used from the admin port.                                                                  | boolean          | "false" |
| **Query** | **channels** _optional_      | Indicates whether to include in the response a channels property containing an array of channels this document is assigned to. (Channels not accessible by the user making the request will not be listed.)                                                       | boolean          | "false" |
| **Query** | **endkey** _optional_        | If this parameter is provided, stop returning records when the specified key is reached.                                                                                                                                                                          | string           |         |
| **Query** | **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned.                                                                                                           | boolean          | "false" |
| **Query** | **keys** _optional_          | Specify a list of document IDs.                                                                                                                                                                                                                                   | < string > array |         |
| **Query** | **limit** _optional_         | Limits the number of result rows to the specified value. Using a value of 0 has the same effect as the value 1.                                                                                                                                                   | integer          |         |
| **Query** | **revs** _optional_          | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter. | boolean          | "false" |
| **Query** | **startkey** _optional_      | Returns records starting with the specified key.                                                                                                                                                                                                                  | string           |         |
| **Query** | **update\_seq** _optional_   | Default is false. Indicates whether to include the update\_seq (document sequence ID) property in the response.                                                                                                                                                   | boolean          | "false" |

##### [](#responses-11)Responses

| HTTP Code | Description   | Schema                         |
| --------- | ------------- | ------------------------------ |
| **200**   | Query results | [QueryResult](#%5Fqueryresult) |

#### [](#%5Fupdatedocsinbulk)Create, Update or Delete Bulk docs

POST /{db}/_bulk_docs

##### [](#description-12)Description

This request enables you to add, update, or delete multiple documents to a database in a single request. To add new documents, you can either specify the ID (`_id`) or let the software create an ID. To update existing documents, you must provide the document ID, revision identifier (`_rev`), and new document values. To delete existing documents you must provide the document ID, revision identifier, and the deletion flag (`_deleted`).

The JSON returned by the `_bulk_docs` operation consists of an array of JSON structures, one for each document in the original submission. The returned JSON structure should be examined to ensure that all of the documents submitted in the original request were successfully added to the database.

##### [](#parameters-12)Parameters

| Type     | Name                        | Description      | Schema                                              |
| -------- | --------------------------- | ---------------- | --------------------------------------------------- |
| **Path** | **db** _required_           | Database name    | string                                              |
| **Body** | **BulkDocsBody** _optional_ | The request body | [BulkDocsBody](#%5Fupdatedocsinbulk%5Fbulkdocsbody) |

**BulkDocsBody**

| Name                      | Description                                                                                                                                                               | Schema                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **docs** _optional_       | List containing new or updated documents. Each object in the array can contain the following properties \_id, \_rev, \_deleted, and values for new and updated documents. | < [Document](#%5Fdocument) \> array |
| **new\_edits** _optional_ | Indicates whether to assign new revision identifiers to new edits. **Default** : true                                                                                     | boolean                             |

##### [](#responses-12)Responses

| HTTP Code | Description                                                                                                                                       | Schema                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **201**   | Documents have been created or updated. The response object is an array with the status for each document submitted in the original request.      | < [Response 201](#%5Fupdatedocsinbulk%5Fresponse%5F201) \> array |
| **409**   | The operation failed with a forbidden error. Probably because the document already exists in the database but a revision number wasn’t specified. | [Forbidden](#%5Fforbidden)                                       |

**Response 201**

| Name               | Description                | Schema |
| ------------------ | -------------------------- | ------ |
| **id** _optional_  | Design document identifier | string |
| **rev** _optional_ | Revision identifier        | string |

#### [](#%5Fgetdocsinbulk)Get Bulk Documents

POST /{db}/_bulk_get

##### [](#description-13)Description

This request returns any number of documents, as individual bodies in a MIME multipart response.

Each enclosed body contains one requested document. The bodies appear in the same order as in the request, but can also be identified by their X-Doc-ID and X-Rev-ID headers. A body for a document with no attachments will have content type application/json and contain the document itself. A body for a document that has attachments will be written as a nested multipart/related body. Its first part will be the document’s JSON, and the subsequent parts will be the attachments (each identified by a Content-Disposition header giving its attachment name.)

##### [](#parameters-13)Parameters

| Type      | Name                       | Description                                                                                                                                                                                                                                                                                            | Schema                                         | Default |
| --------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ------- |
| **Path**  | **db** _required_          | Database name                                                                                                                                                                                                                                                                                          | string                                         |         |
| **Query** | **attachments** _optional_ | Default is false. Include attachment bodies in response.                                                                                                                                                                                                                                               | boolean                                        | "false" |
| **Query** | **revs** _optional_        | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter.                                      | boolean                                        | "false" |
| **Query** | **revs\_limit** _optional_ | The number of revisions to include in the response from the document history. This parameter is only honoured if the revs=true querystring parameter is also sent in the request. If revs=true is specified and revs\_limit isn’t, the full revision history is returned.                              | integer                                        |         |
| **Body**  | **BulkGetBody** _optional_ | List of documents being requested. Each array element is an object that must contain an id property giving the document ID. It may contain a rev property if a specific revision is desired. It may contain an atts\_since property (as in a single-document GET) to limit which attachments are sent. | [BulkGetBody](#%5Fgetdocsinbulk%5Fbulkgetbody) |         |

**BulkGetBody**

| Name                | Schema                                               |
| ------------------- | ---------------------------------------------------- |
| **docs** _optional_ | < [docs](#%5Fdb%5Fbulk%5Fget%5Fpost%5Fdocs) \> array |

**docs**

| Name              | Description  | Schema |
| ----------------- | ------------ | ------ |
| **id** _optional_ | Document ID. | string |

##### [](#responses-13)Responses

| HTTP Code | Description                                                                                                                                                                                | Schema                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| **200**   | Request completed successfully                                                                                                                                                             | No Content                                         |
| **301**   | Request failed with a forbidden error. This usually happens because the user requesting that document doesn’t have access to it. Access to documents is granted to users through channels. | [Response 301](#%5Fgetdocsinbulk%5Fresponse%5F301) |

**Response 301**

| Name                     | Description                            | Schema  |
| ------------------------ | -------------------------------------- | ------- |
| **\_id** _optional_      | The document ID that was requested     | string  |
| **\_removed** _optional_ | **Default** : true                     | boolean |
| **\_rev** _optional_     | The revision number that was requested | string  |

##### [](#produces)Produces

* `multipart/mixed`

##### [](#example-http-response)Example HTTP response

###### [](#response-200)Response 200

```json
{
  "multipart/mixed (document found)" : "--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\nContent-Type: application/json\n\n{\"_id\":\"doc123\",\"_rev\":\"1-c543d6514c609f65180f94af247aaffe\",\"hello\":\"world!\"}\n--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\n",
  "multipart/mixed (document not found)" : "--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\nContent-Type: application/json; error=\"true\"\n\n{\"error\":\"not_found\",\"id\":\"doc1234\",\"reason\":\"missing\",\"status\":404}\n--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\n"
}
```

#### [](#%5Fgetchangeswithparametersinbody)Get Changes Feed (body parameters)

POST /{db}/_changes

##### [](#description-14)Description

Same as the GET /\_changes request except the parameters are in the JSON body.

##### [](#parameters-14)Parameters

| Type     | Name                       | Description      | Schema                                                          |
| -------- | -------------------------- | ---------------- | --------------------------------------------------------------- |
| **Path** | **db** _required_          | Database name    | string                                                          |
| **Body** | **ChangesBody** _optional_ | The request body | [ChangesBody](#%5Fgetchangeswithparametersinbody%5Fchangesbody) |

**ChangesBody**

| Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Schema           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **active\_only** _optional_  | Default is false. When true, the changes response doesn’t include either deleted documents, or notification for documents that the user no longer has access to. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                 | boolean          |
| **channels** _optional_      | A comma-separated list of channel names. The response will be filtered to only documents in these channels. (This parameter must be used with the sync\_gateway/bychannel filter parameter; see below.)                                                                                                                                                                                                                                                                                                                                                              | string           |
| **doc\_ids** _optional_      | A list of document IDs as a valid JSON array. The response will be filtered to only documents with these IDs. (This parameter must be used with the \_doc\_ids filter parameter; see below.)                                                                                                                                                                                                                                                                                                                                                                         | < string > array |
| **feed** _optional_          | Default is 'normal'. Specifies type of change feed. Valid values are normal, continuous, longpoll, websocket. **Default** : "normal"                                                                                                                                                                                                                                                                                                                                                                                                                                 | string           |
| **filter** _optional_        | Indicates that the returned documents should be filtered. The valid values are sync\_gateway/bychannel and \_doc\_ids.                                                                                                                                                                                                                                                                                                                                                                                                                                               | string           |
| **heartbeat** _optional_     | The heartbeat defines the interval (in milliseconds) at which an empty line (CRLF) is written to the response. It helps prevent Sync Gateway from deciding the socket is idle and closing it. The heartbeat value overrides any timeout value, to keep the feed alive indefinitely. Setting heartbeat=0 results in no heartbeat. **Default:** 0, which is no heartbeat **Constraints:** \* Applies ONLY where feed=longpoll or feed=continuous \* Minimum: 25000 (25 seconds) \* Maximum: None – unless you define one in your configuration file using MaxHeartbeat | integer          |
| **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                          | boolean          |
| **limit** _optional_         | Limits the number of result rows to the specified value. Using a value of 0 has the same effect as the value 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | integer          |
| **since** _optional_         | Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                                                                                                                                                                                                                                                     | object           |
| **style** _optional_         | Default is 'main\_only'. Number of revisions to return in the changes array. The only possible value is all\_docs and it returns all leaf revisions including conflicts and deleted former conflicts. **Default** : "main\_only"                                                                                                                                                                                                                                                                                                                                     | string           |
| **timeout** _optional_       | The timeout value defines the maximum period (in milliseconds) to wait for a change, before sending a response. This wait applies even when there are no results. Setting timeout=0 results in no timeout. **Default:** 300000 (5 minutes/300 seconds) **Constraints:** \* Applies ONLY where feed=longpoll or feed=continuous \* Minimum: 0, no timeout \* Maximum: 1500000 (15 minutes)                                                                                                                                                                            | integer          |

##### [](#responses-14)Responses

| HTTP Code | Description                    | Schema                 |
| --------- | ------------------------------ | ---------------------- |
| **200**   | Request completed successfully | [Changes](#%5Fchanges) |

#### [](#%5Fgetchanges)Get Changes Feed (query parameters)

GET /{db}/_changes

##### [](#description-15)Description

This request retrieves a sorted list of changes made to documents in the database, in time order of application.

Each document appears at most once, ordered by its most recent change, regardless of how many times it’s been changed. This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

##### [](#parameters-15)Parameters

| Type      | Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Schema           | Default      |
| --------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------ |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | string           |              |
| **Query** | **active\_only** _optional_  | Default is false. When true, the changes response doesn’t include either deleted documents, or notification for documents that the user no longer has access to.                                                                                                                                                                                                                                                                                                                                                                                                      | boolean          | "false"      |
| **Query** | **channels** _optional_      | A comma-separated list of channel names. The response will be filtered to only documents in these channels. (This parameter must be used with the sync\_gateway/bychannel filter parameter; see below.)                                                                                                                                                                                                                                                                                                                                                               | string           |              |
| **Query** | **doc\_ids** _optional_      | A list of document IDs as a valid JSON array. The response will be filtered to only documents with these IDs. This parameter must be used with the filter=\_doc\_ids and feed=normal parameters.                                                                                                                                                                                                                                                                                                                                                                      | < string > array |              |
| **Query** | **feed** _optional_          | Default is 'normal'. Specifies type of change feed. Valid values are normal, continuous, longpoll, websocket.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | string           | "normal"     |
| **Query** | **filter** _optional_        | Indicates that the reported documents should be filtered. The valid values are sync\_gateway/bychannel and \_doc\_ids.                                                                                                                                                                                                                                                                                                                                                                                                                                                | string           |              |
| **Query** | **heartbeat** _optional_     | The heartbeat defines the interval (in milliseconds) at which an empty line (CRLF) is written to the response. It helps prevent Sync Gateway from deciding the socket is idle and closing it. The heartbeat value overrides any timeout value, to keep the feed alive indefinitely. Setting heartbeat=0 results in no heartbeat. **Default:** 0, which is no heartbeat **Constraints:** \* Applies ONLY where feed=longpoll or feed=continuous. \* Minimum: 25000 (25 seconds) \* Maximum: None – unless you define one in your configuration file using MaxHeartbeat | integer          | 0            |
| **Query** | **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned.                                                                                                                                                                                                                                                                                                                                                                                                               | boolean          | "false"      |
| **Query** | **limit** _optional_         | Limits the number of result rows to the specified value. Using a value of 0 has the same effect as the value 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | integer          |              |
| **Query** | **since** _optional_         | Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                                                                                                                                                                                                                                                      | string           |              |
| **Query** | **style** _optional_         | Default is 'main\_only'. Number of revisions to return in the changes array. main\_only returns the current winning revision, all\_docs returns all leaf revisions including conflicts and deleted former conflicts.                                                                                                                                                                                                                                                                                                                                                  | string           | "main\_only" |
| **Query** | **timeout** _optional_       | The timeout value defines the maximum period (in milliseconds) to wait for a change, before sending a response. This wait applies even when there are no results. Setting timeout=0 results in no timeout. **Default:** 300000 (5 minutes/300 seconds) **Constraints:** \* Applies ONLY where feed=longpoll or feed=continuous. \* Minimum: 0, no timeout \* Maximum: 1500000 (15 minutes)                                                                                                                                                                            | integer          | 300000       |

##### [](#responses-15)Responses

| HTTP Code | Description                    | Schema                 |
| --------- | ------------------------------ | ---------------------- |
| **200**   | Request completed successfully | [Changes](#%5Fchanges) |

#### [](#%5Fgetrevisionids)Get Revision ID Diff

POST /{db}/_revs_diff

##### [](#description-16)Description

Given a set of document/revision IDs, returns the subset of those that do not correspond to revisions stored in the database.

##### [](#parameters-16)Parameters

| Type     | Name                | Description   | Schema                           |
| -------- | ------------------- | ------------- | -------------------------------- |
| **Path** | **db** _required_   | Database name | string                           |
| **Body** | **body** _optional_ | Request body  | < string, < string > array > map |

##### [](#responses-16)Responses

| HTTP Code | Description                | Schema                                                               |
| --------- | -------------------------- | -------------------------------------------------------------------- |
| **200**   | The request was successful | < string, [Response 200](#%5Fgetrevisionids%5Fresponse%5F200) \> map |

**Response 200**

| Name                   | Description                                                                              | Schema           |
| ---------------------- | ---------------------------------------------------------------------------------------- | ---------------- |
| **missing** _optional_ | A list of revision IDs for that document (the ones that are not stored in the database). | < string > array |

### [](#%5Fdocument%5Fresource)Document

Work with documents

#### [](#%5Fadddocument)Create New Document

POST /{db}/

##### [](#description-17)Description

This request creates a new document in the specified database.

You can either specify the document ID by including the \_id in the request message body (the value must be a string), or let the software generate an ID.

The maximum size allowed for a document is 20MB.

##### [](#parameters-17)Parameters

| Type     | Name                | Description       | Schema |
| -------- | ------------------- | ----------------- | ------ |
| **Path** | **db** _required_   | Database name     | string |
| **Body** | **body** _optional_ | The document body | object |

##### [](#responses-17)Responses

| HTTP Code | Description                           | Schema                 |
| --------- | ------------------------------------- | ---------------------- |
| **201**   | The document was written successfully | [Success](#%5Fsuccess) |

#### [](#%5Fgetdocument)Get Specific Document

GET /{db}/{doc}

##### [](#description-18)Description

This request retrieves a document from a database.

##### [](#parameters-18)Parameters

| Type      | Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                              | Schema           | Default |
| --------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------- |
| **Path**  | **db** _required_          | Database name                                                                                                                                                                                                                                                                                                                                                                                                                            | string           |         |
| **Path**  | **doc** _required_         | Document ID                                                                                                                                                                                                                                                                                                                                                                                                                              | string           |         |
| **Query** | **attachments** _optional_ | Default is false. Include attachment bodies in response.                                                                                                                                                                                                                                                                                                                                                                                 | boolean          | "false" |
| **Query** | **atts\_since** _optional_ | Include attachments only since specified revisions. Does not include attachments for specified revisions.                                                                                                                                                                                                                                                                                                                                | < string > array |         |
| **Query** | **open\_revs** _optional_  | Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only [leaf revision](glossary.html) bodies that haven’t been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. | < string > array |         |
| **Query** | **rev** _optional_         | Revision identifier of the revision to get. By default, Sync Gateway returns the current revision. This parameter is generally only needed for conflict resolution. For example where the app might need to retrieve a conflicting leaf revision that isn’t the current revision.                                                                                                                                                        | string           |         |
| **Query** | **revs** _optional_        | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter.                                                                                                                                                                        | boolean          | "false" |
| **Query** | **show\_exp** _optional_   | Whether to show the \_exp property in the response.                                                                                                                                                                                                                                                                                                                                                                                      | boolean          | "false" |

##### [](#responses-18)Responses

| HTTP Code | Description                                                         | Schema |
| --------- | ------------------------------------------------------------------- | ------ |
| **200**   | The message body contains the following objects in a JSON document. | object |

#### [](#%5Faddorupdatedocument)Create or Update Specific Document

PUT /{db}/{doc}

##### [](#description-19)Description

This request creates a new document or creates a new revision of an existing document. It enables you to specify the identifier for a new document rather than letting the software create an identifier.

If you want to create a new document and let the software create an identifier, use the POST /db request.

If the document specified by doc does not exist, a new document is created and assigned the identifier specified in doc. If the document already exists, the document is updated with the JSON document in the message body and given a new revision. The maximum size allowed for a document is 20MB.

Since Sync Gateway 1.3, an expiry property (`_exp`) can also be specified to purge the document after a given time. If **convergence** is enabled (introduced in Sync Gateway 1.5), the behavior of the expiry feature changes in the following way: when the expiry value is reached, instead of getting purged, the **active** revision of the document is tombstoned. If there is another non-tombstoned revision for this document (i.e a conflict) it will become the active revision. The tombstoned revision will be purged when the server’s metadata purge interval is reached.

##### [](#parameters-19)Parameters

| Type      | Name                      | Description                                                                                                                                                                                                                                                                                                                                             | Schema                   | Default |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------- |
| **Path**  | **db** _required_         | Database name                                                                                                                                                                                                                                                                                                                                           | string                   |         |
| **Path**  | **doc** _required_        | Document ID                                                                                                                                                                                                                                                                                                                                             | string                   |         |
| **Query** | **new\_edits** _optional_ | Default is true. Setting this to false indicates that the request body is an already-existing revision that should be directly inserted into the database, instead of a modification to apply to the current document. (This mode is used by the replicato.) This option must be used in conjunction with the \_revisions property in the request body. | boolean                  | "true"  |
| **Query** | **rev** _required_        | Revision identifier of the revision to update. It must be the last revision in the history.                                                                                                                                                                                                                                                             | string                   |         |
| **Body**  | **Document** _optional_   | Request body                                                                                                                                                                                                                                                                                                                                            | [Document](#%5Fdocument) |         |

##### [](#responses-19)Responses

| HTTP Code | Description                                                         | Schema                 |
| --------- | ------------------------------------------------------------------- | ---------------------- |
| **200**   | The response is a JSON document that contains the following objects | [Success](#%5Fsuccess) |

#### [](#%5Fdeletedocument)Delete Specific Document

DELETE /{db}/{doc}

##### [](#description-20)Description

This request deletes a document from the database.

When a document is deleted, the revision number is updated so the database can track the deletion in synchronized copies.

##### [](#parameters-20)Parameters

| Type      | Name               | Description                                                                                                     | Schema |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------- | ------ |
| **Path**  | **db** _required_  | Database name                                                                                                   | string |
| **Path**  | **doc** _required_ | Document ID                                                                                                     | string |
| **Query** | **rev** _required_ | Revision identifier of the revision to delete. It must be the identifier of the latest revision in the history. | string |

##### [](#responses-20)Responses

| HTTP Code | Description                   | Schema                 |
| --------- | ----------------------------- | ---------------------- |
| **200**   | Document successfully removed | [Success](#%5Fsuccess) |

### [](#%5Fdocument%5Flocal%5Fresource)Document (local)

Work with local documents

#### [](#%5Fgetlocaldoc)Get Specific Local Document

GET /{db}/_local/{local_doc}

##### [](#description-21)Description

This request retrieves a local document.

Local document IDs begin with \_local/. Local documents are not replicated or indexed, don’t support attachments, and don’t save revision histories.

In practice local documents mostly used by Couchbase Lite’s replicator, as a place to store replication checkpoint data.

##### [](#parameters-21)Parameters

| Type     | Name                      | Description                             | Schema |
| -------- | ------------------------- | --------------------------------------- | ------ |
| **Path** | **db** _required_         | Database name                           | string |
| **Path** | **local\_doc** _required_ | Local document IDs begin with \_local/. | string |

##### [](#responses-21)Responses

| HTTP Code | Description                                                         | Schema                 |
| --------- | ------------------------------------------------------------------- | ---------------------- |
| **200**   | The message body contains the following objects in a JSON document. | [Success](#%5Fsuccess) |

#### [](#%5Faddorupdatelocaldoc)Create or Update a Local Document

PUT /{db}/_local/{local_doc}

##### [](#description-22)Description

This request creates or updates a local document.

Local document IDs begin with \_local/. Local documents are not replicated or indexed, don’t support attachments, and don’t save revision histories.

In practice they are almost only used by the client’s replicator, as a place to store replication checkpoint data.

##### [](#parameters-22)Parameters

| Type     | Name                      | Description                             | Schema |
| -------- | ------------------------- | --------------------------------------- | ------ |
| **Path** | **db** _required_         | Database name                           | string |
| **Path** | **local\_doc** _required_ | Local document IDs begin with \_local/. | string |

##### [](#responses-22)Responses

| HTTP Code | Description | Schema                 |
| --------- | ----------- | ---------------------- |
| **201**   | Created     | [Success](#%5Fsuccess) |

#### [](#%5Fdeletelocaldoc)Delete Specific Local Document

DELETE /{db}/_local/{local_doc}

##### [](#description-23)Description

This request deletes a local document.

Local document IDs begin with \_local/. Local documents are not replicated or indexed, don’t support attachments, and don’t save revision histories. In practice they are almost only used by Couchbase Lite’s replicator, as a place to store replication checkpoint data.

##### [](#parameters-23)Parameters

| Type      | Name                      | Description                                                                                                     | Schema |
| --------- | ------------------------- | --------------------------------------------------------------------------------------------------------------- | ------ |
| **Path**  | **db** _required_         | Database name                                                                                                   | string |
| **Path**  | **local\_doc** _required_ | Local document IDs begin with \_local/.                                                                         | string |
| **Query** | **batch** _optional_      | Stores the document in batch mode. To use, set the value to ok.                                                 | string |
| **Query** | **rev** _optional_        | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.) | string |

##### [](#responses-23)Responses

| HTTP Code | Description                   | Schema                 |
| --------- | ----------------------------- | ---------------------- |
| **200**   | Document successfully removed | [Success](#%5Fsuccess) |

### [](#%5Fserver%5Fresource)Server

Work with the server

#### [](#%5Fgetserverinfo)Get Server Data

GET /

##### [](#description-24)Description

Returns meta-information about the server.

##### [](#responses-24)Responses

| HTTP Code | Description                        | Schema                                      |
| --------- | ---------------------------------- | ------------------------------------------- |
| **200**   | Meta-information about the server. | [ServerData\_model](#%5Fserverdata%5Fmodel) |

### [](#%5Fsession%5Fresource)Session

Work with sessions

#### [](#%5Faddusersession)Create User Session

POST /{db}/_session

##### [](#description-25)Description

If the credentials provided in the request body are valid, the session is created with an idle session timeout of 24 hours.

An idle session timeout in the context of Sync Gateway is defined as the following: if 10% or more of the current expiration time has elapsed when a subsequent request with that session id is processed, the session’s expiry time is automatically updated to 24 hours from that time.

##### [](#parameters-24)Parameters

| Type     | Name                       | Description                                                              | Schema                                          |
| -------- | -------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------- |
| **Path** | **db** _required_          | Database name                                                            | string                                          |
| **Body** | **SessionBody** _optional_ | The message body is a JSON document that contains the following objects. | [SessionBody](#%5Faddusersession%5Fsessionbody) |

**SessionBody**

| Name                    | Description                                             | Schema |
| ----------------------- | ------------------------------------------------------- | ------ |
| **name** _optional_     | Username of the user the session will be associated to. | string |
| **password** _optional_ | User password.                                          | string |

##### [](#responses-25)Responses

| HTTP Code | Description                                                                                    | Schema                 |
| --------- | ---------------------------------------------------------------------------------------------- | ---------------------- |
| **200**   | Session successfully created. The Set-Cookie response header contains the session credentials. | [Session](#%5Fsession) |

#### [](#%5Fdeleteusersession)Delete User Session

DELETE /{db}/_session

##### [](#description-26)Description

This request deletes the session that currently authenticates the requests.

##### [](#parameters-25)Parameters

| Type       | Name                  | Description                          | Schema |
| ---------- | --------------------- | ------------------------------------ | ------ |
| **Header** | **cookie** _optional_ | The cookie of the logged-in session. | string |
| **Path**   | **db** _required_     | Database name                        | string |

##### [](#responses-26)Responses

| HTTP Code | Description                           | Schema     |
| --------- | ------------------------------------- | ---------- |
| **200**   | The session was successfully removed. | No Content |

## [](#%5Fdefinitions)Definitions

### [](#%5Fdocumentresponse)DocumentResponse

| Name                 | Description         | Schema |
| -------------------- | ------------------- | ------ |
| **\_id** _optional_  | Document identifier | string |
| **\_rev** _optional_ | Revision identifier | string |

### [](#%5Ferror)Error

| Name                   | Schema          |
| ---------------------- | --------------- |
| **code** _optional_    | integer (int32) |
| **fields** _optional_  | string          |
| **message** _optional_ | string          |

### [](#%5Fexpvars)ExpVars

| Name                                    | Description                                                                     | Schema                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **cb** _optional_                       | Variables reported by the Couchbase SDK (go\_couchbase package)                 | object                                                              |
| **cmdline** _optional_                  | Built-in variables from the Go runtime, lists the command-line arguments        | object                                                              |
| **mc** _optional_                       | Variables reported by the low-level memcached API (gomemcached package)         | object                                                              |
| **memstats** _optional_                 | Dumps a large amount of information about the memory heap and garbage collector | object                                                              |
| **syncGateway\_changeCache** _optional_ |                                                                                 | [syncGateway\_changeCache](#%5Fexpvars%5Fsyncgateway%5Fchangecache) |
| **syncGateway\_db** _optional_          |                                                                                 | [syncGateway\_db](#%5Fexpvars%5Fsyncgateway%5Fdb)                   |

**syncGateway\_changeCache**

| Name                            | Description                                                          | Schema |
| ------------------------------- | -------------------------------------------------------------------- | ------ |
| **lag-queue-0000ms** _optional_ | Histogram of delay from Tap feed till doc is posted to changes feed  | object |
| **lag-tap-0000ms** _optional_   | Histogram of delay from doc save till it shows up in Tap feed        | object |
| **lag-total-0000ms** _optional_ | Histogram of total delay from doc save till posted to changes feed   | object |
| **maxPending** _optional_       | Max number of sequences waiting on a missing earlier sequence number | object |
| **outOfOrder** _optional_       | Number of out-of-order sequences posted                              | object |
| **view\_queries** _optional_    | Number of queries to channels view                                   | object |

**syncGateway\_db**

| Name                                       | Description                                                                                           | Schema |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------ |
| **channelChangesFeeds** _optional_         | Number of calls to db.changesFeed, i.e. generating a changes feed for a single channel.               | object |
| **channelLogAdds** _optional_              | Number of entries added to channel logs                                                               | object |
| **channelLogAppends** _optional_           | Number of times entries were written to channel logs using an APPEND operation                        | object |
| **channelLogCacheHits** _optional_         | Number of requests for channel-logs that were fulfilled from the in-memory cache                      | object |
| **channelLogRewriteCollisions** _optional_ | Number of collisions while attempting to rewrite channel logs using SET                               | object |
| **channelLogRewrites** _optional_          | Number of times entries were written to channel logs using a SET operation (rewriting the entire log) | object |
| **document\_gets** _optional_              | Number of times a document was read from the database                                                 | object |
| **revisionCache\_adds** _optional_         | Number of revisions added to the revision cache                                                       | object |
| **revisionCache\_hits** _optional_         | Number of times a revision-cache lookup succeeded                                                     | object |
| **revisionCache\_misses** _optional_       | Number of times a revision-cache lookup failed                                                        | object |
| **revs\_added** _optional_                 | Number of revisions added to the database (including deletions)                                       | object |
| **sequence\_gets** _optional_              | Number of times the database’s lastSequence was read                                                  | object |
| **sequence\_reserves** _optional_          | Number of times the database’s lastSequence was incremented                                           | object |

### [](#%5Fforbidden)Forbidden

| Name                  | Description              | Schema  |
| --------------------- | ------------------------ | ------- |
| **error** _optional_  | **Default** : "conflict" | string  |
| **id** _optional_     |                          | string  |
| **reason** _optional_ |                          | string  |
| **status** _optional_ |                          | integer |

### [](#%5Flogtags)LogTags

| Name                   | Description                                                                                                                                                                                                                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Access** _optional_  | access() calls made by the sync function                                                                                                                                                                                                                      | boolean |
| **Attach** _optional_  | Attachment processing                                                                                                                                                                                                                                         | boolean |
| **Auth** _optional_    | Authentication                                                                                                                                                                                                                                                | boolean |
| **Bucket** _optional_  | Sync Gateway interactions with the bucket (verbose logging).                                                                                                                                                                                                  | boolean |
| **CRUD** _optional_    | Updates made by Sync Gateway to documents (CRUD+ for verbose logging)                                                                                                                                                                                         | boolean |
| **Cache** _optional_   | Interactions with Sync Gateway’s in-memory channel cache (Cache+ for verbose logging)                                                                                                                                                                         | boolean |
| **Changes** _optional_ | Processing of \_changes requests (Changes+ for verbose logging)                                                                                                                                                                                               | boolean |
| **DCP** _optional_     | DCP-feed processing (verbose logging)                                                                                                                                                                                                                         | boolean |
| **Events** _optional_  | Event processing (webhooks) (Events+ for verbose logging)                                                                                                                                                                                                     | boolean |
| **Feed** _optional_    | Server-feed processing (Feed+ for verbose logging)                                                                                                                                                                                                            | boolean |
| **HTTP** _optional_    | All requests made to the Sync Gateway REST APIs (Sync and Admin). Note that the log keyword HTTP is always enabled, which means that HTTP requests and error responses are always logged (in a non-verbose manner). HTTP+ provides more verbose HTTP logging. | boolean |

### [](#%5Fpurgebody)PurgeBody

Document ID

| Name                      | Description                                                                                 | Schema              |
| ------------------------- | ------------------------------------------------------------------------------------------- | ------------------- |
| **a\_doc\_id** _optional_ | Only possible value is \["\*"\]. It permanently removes all revisions for that document ID. | < enum (\*) > array |

### [](#%5Fsuccess)Success

| Name               | Description                                    | Schema  |
| ------------------ | ---------------------------------------------- | ------- |
| **id** _optional_  | Design document identifier                     | string  |
| **ok** _optional_  | Indicates whether the operation was successful | boolean |
| **rev** _optional_ | Revision identifier                            | string  |

### [](#%5Fuser)User

| Name                           | Description                                                                                                                                                                                     | Schema           |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **admin\_channels** _optional_ | Array of channel names to give the user access to                                                                                                                                               | < string > array |
| **admin\_roles** _optional_    | Array of role names to assign to this user                                                                                                                                                      | < string > array |
| **all\_channels** _optional_   | Array of channel names the user is given access to                                                                                                                                              | < string > array |
| **disabled** _optional_        | Boolean property to disable this user. The user will not be able to login if this property is set to true.                                                                                      | boolean          |
| **email** _optional_           | Email of the user that will be created.                                                                                                                                                         | string           |
| **name** _optional_            | Name of the user that will be created                                                                                                                                                           | string           |
| **password** _optional_        | Password of the user that will be created. Required, unless the allow\_empty\_password Sync Gateway per-database configuration value is set to true, in which case the password can be omitted. | string           |
| **roles** _optional_           | Array of role names the user is given access to                                                                                                                                                 | < string > array |

### [](#%5Fchangesfeedrow)ChangesFeedRow

| Name                   | Description                                                             | Schema                                             |
| ---------------------- | ----------------------------------------------------------------------- | -------------------------------------------------- |
| **changes** _optional_ | List of the document’s leafs. Each leaf object contains one field, rev. | < [changes](#%5Fchangesfeedrow%5Fchanges) \> array |
| **deleted** _optional_ | Indicate whether the row is deleted **Default** : false                 | boolean                                            |
| **doc** _optional_     |                                                                         | object                                             |
| **id** _optional_      | Document identifier                                                     | string                                             |
| **seq** _optional_     | Update sequence number                                                  | integer                                            |

**changes**

| Name               | Description                                       | Schema |
| ------------------ | ------------------------------------------------- | ------ |
| **rev** _optional_ | Identifier of the document revision that changed. | string |

### [](#%5Fview)View

| Name                 | Description                                                                                                     | Schema                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **\_rev** _optional_ | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.) | string                    |
| **views** _optional_ | List of views to save on this design document.                                                                  | [views](#%5Fview%5Fviews) |

**views**

| Name                          | Description                      | Schema                                        |
| ----------------------------- | -------------------------------- | --------------------------------------------- |
| **my\_view\_name** _optional_ | The view’s map/reduce functions. | [my\_view\_name](#%5Fview%5Fmy%5Fview%5Fname) |

**my\_view\_name**

| Name                  | Description                                          | Schema |
| --------------------- | ---------------------------------------------------- | ------ |
| **map** _optional_    | Inline JavaScript definition for the map function    | string |
| **reduce** _optional_ | Inline JavaScript definition for the reduce function | string |

### [](#%5Fqueryrow)QueryRow

| Name                 | Description                                                                             | Schema |
| -------------------- | --------------------------------------------------------------------------------------- | ------ |
| **doc** _optional_   | The document body. This is only returned if include\_docs=true is specified in the URL. | object |
| **id** _optional_    | The ID of the document.                                                                 | string |
| **key** _optional_   | The key in the output row.                                                              | object |
| **value** _optional_ | The value in the output row.                                                            | object |

### [](#%5Fdesign)Design

| Name                  | Description                            | Schema          |
| --------------------- | -------------------------------------- | --------------- |
| **count** _optional_  | Total number of items available.       | integer (int32) |
| **limit** _optional_  | Number of items to retrieve (100 max). | integer (int32) |
| **offset** _optional_ | Position in pagination.                | integer (int32) |

### [](#%5Falldocs)AllDocs

| Name                | Description                                      | Schema           |
| ------------------- | ------------------------------------------------ | ---------------- |
| **keys** _optional_ | List of identifiers of the documents to retrieve | < string > array |

### [](#%5Fchanges)Changes

| Name                     | Description                                                                                   | Schema                                          |
| ------------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **last\_seq** _optional_ | Last change sequence number                                                                   | object                                          |
| **results** _optional_   | List of changes to the database. See the following table for a list of fields in this object. | < [ChangesFeedRow](#%5Fchangesfeedrow) \> array |

### [](#%5Fdatabase)Database

| Name                                 | Description                                                                                                                                                                                                            | Schema  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **db\_name** _optional_              | Name of the database                                                                                                                                                                                                   | string  |
| **db\_uuid** _optional_              | Database identifier                                                                                                                                                                                                    | integer |
| **disk\_format\_version** _optional_ | Database schema version                                                                                                                                                                                                | integer |
| **disk\_size** _optional_            | Total amount of data stored on the disk (in bytes)                                                                                                                                                                     | integer |
| **instance\_start\_time** _optional_ | Date and time the database was opened (in microseconds since 1 January 1970)                                                                                                                                           | string  |
| **state** _optional_                 | The state of the specified database. Possible values are 'Online' and 'Offline'. A database can be taken offline and brought back online using the /{db}/\_offline and /{db}/\_online endpoints on the Admin REST API. | string  |
| **update\_seq** _optional_           | Number of updates to the database                                                                                                                                                                                      | string  |

### [](#%5Fdocument)Document

| Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema                                      |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **\_attachments** _optional_ |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [\_attachments](#%5Fdocument%5Fattachments) |
| **\_exp** _optional_         | Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document (TTL is not supported for databases in walrus mode). The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2016 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiries are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc} when show\_exp=true is included in the querystring. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. | string                                      |
| **\_id** _optional_          | The document ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | string                                      |
| **\_rev** _optional_         | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | string                                      |
| **\_revisions** _optional_   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [\_revisions](#%5Fdocument%5Frevisions)     |

**\_attachments**

| Name                            | Schema                                               |
| ------------------------------- | ---------------------------------------------------- |
| **attachment\_name** _optional_ | [attachment\_name](#%5Fdocument%5Fattachment%5Fname) |

**attachment\_name**

| Name                         | Description                         | Schema |
| ---------------------------- | ----------------------------------- | ------ |
| **content\_type** _optional_ | The content type of the attachment. | string |

**\_revisions**

| Name                 | Description                                                   | Schema           |
| -------------------- | ------------------------------------------------------------- | ---------------- |
| **ids** _optional_   | Array of valid revision IDs, in reverse order (latest first). | < string > array |
| **start** _optional_ | Prefix number for the latest revision.                        | integer          |

### [](#%5Fqueryresult)QueryResult

| Name                       | Description                                                                          | Schema                              |
| -------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------- |
| **offset** _optional_      | Starting index of the returned rows.                                                 | string                              |
| **rows** _optional_        |                                                                                      | < [QueryRow](#%5Fqueryrow) \> array |
| **total\_rows** _optional_ | Number of documents in the database. This number is not the number of rows returned. | integer                             |

### [](#%5Freplication)Replication

| Name                       | Description                                                | Schema  |
| -------------------------- | ---------------------------------------------------------- | ------- |
| **ok** _optional_          | Indicates whether the replication operation was successful | boolean |
| **session\_id** _optional_ | Session identifier                                         | string  |

### [](#%5Fserverdata%5Fmodel)ServerData\_model

| Name                          | Description                                                                     | Schema |
| ----------------------------- | ------------------------------------------------------------------------------- | ------ |
| **couchdb** _optional_        | Contains the string 'Welcome' (this is required for compatibility with CouchDB) | string |
| **vendor/name** _optional_    | The server type ('Couchbase Sync Gateway)                                       | string |
| **vendor/version** _optional_ | The server version                                                              | string |
| **version** _optional_        | Sync Gateway version number                                                     | string |

### [](#%5Fsession)Session

| Name                                    | Description                                  | Schema                         |
| --------------------------------------- | -------------------------------------------- | ------------------------------ |
| **authentication\_handlers** _optional_ | List of authentication methods.              | < string > array               |
| **ok** _optional_                       | Always true if the operation was successful. | boolean                        |
| **userCtx** _optional_                  |                                              | [UserContext](#%5Fusercontext) |

### [](#%5Fusercontext)UserContext

Context for this user.

| Name                    | Description                                                                                                                                                                           | Schema |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **channels** _optional_ | Key-value pairs with a channel name as the key and the sequence number that granted the user access to the channel as value. ! is the public channel and every user has access to it. | object |
| **name** _optional_     | The user’s name.                                                                                                                                                                      | string |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)