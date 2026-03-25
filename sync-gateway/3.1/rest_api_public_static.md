---
title: Public REST API (Static Page)
description: Description of the Sync Gateway Public REST API, alternative
  representation as a static page
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/rest_api_public_static.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@sync-gateway::rest_api_public_static.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/rest_api_public_static.html)

# Public REST API (Static Page)

> Description of the Sync Gateway Public REST API, alternative representation as a static page  

Related _REST API_ topics: [Admin REST API (Static Page)](rest%5Fapi%5Fadmin%5Fstatic.md) | [Metrics REST API (Static Page)](rest%5Fapi%5Fmetrics%5Fstatic.md)

## [](#overview)Overview

### Version information

_Version_ : 3.1

### Host information

{protocol}://{hostname}:4984

Public API

| Component    | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| **protocol** | The protocol to use (HTTP or HTTPS) **Values:** http, https **Example:** http |
| **hostname** | The hostname to use **Example:** localhost                                    |

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Authentication](#tag-Authentication)  
[Database Management](#tag-DatabaseManagement)  
[Document](#tag-Document)  
[Document Attachment](#tag-DocumentAttachment)  
[Replication](#tag-Replication)  
[Server](#tag-Server)  
[Session](#tag-Session)  
[Unsupported](#tag-Unsupported)

### [](#tag-Authentication)Authentication

Manage OpenID Connect Authentication

[OpenID Connect authentication initiation via Location header redirect](#get%5Fdb-%5Foidc)  
[OpenID Connect authentication callback](#get%5Fdb-%5Foidc%5Fcallback)  
[OpenID Connect authentication initiation via WWW-Authenticate header](#get%5Fdb-%5Foidc%5Fchallenge)  
[OpenID Connect token refresh](#get%5Fdb-%5Foidc%5Frefresh)  
[OpenID Connect mock provider](#get%5Fdb-%5Foidc%5Ftesting-.well-known-openid-configuration)  
[OpenID Connect mock login page handler](#get%5Fdb-%5Foidc%5Ftesting-authenticate)  
[OpenID Connect mock login page](#get%5Fdb-%5Foidc%5Ftesting-authorize)  
[OpenID Connect public certificates for signing keys](#get%5Fdb-%5Foidc%5Ftesting-certs)  
[Create a new Facebook-based session](#post%5Fdb-%5Ffacebook)  
[Create a new Google-based session](#post%5Fdb-%5Fgoogle)  
[OpenID Connect mock login page handler](#post%5Fdb-%5Foidc%5Ftesting-authenticate)  
[OpenID Connect mock login page](#post%5Fdb-%5Foidc%5Ftesting-authorize)  
[OpenID Connect mock token](#post%5Fdb-%5Foidc%5Ftesting-token)

#### [](#get%5Fdb-%5Foidc)OpenID Connect authentication initiation via Location header redirect

GET /{db}/_oidc

##### [](#get%5Fdb-%5Foidc-description)Description

Called by clients to initiate the OpenID Connect Authorization Code Flow. Redirects to the OpenID Connect provider if successful.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                    | Description                                                                                                                                                                                                          | Schema |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **provider** _optional_ | The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                               | String |
| **offline** _optional_  | If true, the OpenID Connect provider is requested to confirm with the user the permissions requested and refresh the OIDC token. To do this, access\_type=offline and prompt=consent is set on the redirection link. | String |

##### [](#get%5Fdb-%5Foidc-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| 302       | Successfully connected with the OpenID Connect provider so now redirecting to the requested OIDC provider for authentication.        |                            |
| 400       | The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. |                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError) |
| 500       | Unable to connect and validate with the OpenID Connect provider requested                                                            |                            |

#### [](#get%5Fdb-%5Foidc%5Fcallback)OpenID Connect authentication callback

GET /{db}/_oidc_callback

##### [](#get%5Fdb-%5Foidc%5Fcallback-description)Description

The callback URL that the client is redirected to after authenticating with the OpenID Connect provider.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc%5Fcallback-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                    | Description                                                                                                                                                                                                              | Schema |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **error** _optional_    | The OpenID Connect error, if any occurred.                                                                                                                                                                               | String |
| **code** _required_     | The OpenID Connect authentication code.                                                                                                                                                                                  | String |
| **provider** _optional_ | The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                                   | String |
| **state** _optional_    | The OpenID Connect state to verify against the state cookie. This is used to prevent cross-site request forgery (CSRF). This is not required if disable\_callback\_state=true for the provider config (NOT recommended). | String |

##### [](#get%5Fdb-%5Foidc%5Fcallback-responses)Responses

| HTTP Code | Description                                                                                              | Schema                                                                       |
| --------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 200       | Successfully authenticated with OpenID Connect.                                                          | [OpenIDConnectCallbackProperties](#OpenID%5FConnect%5Fcallback%5Fproperties) |
| 400       | A problem occurred when reading the callback request body                                                |                                                                              |
| 401       | An error was received from the OpenID Connect provider. This means the error query parameter was filled. |                                                                              |
| 404       | Resource could not be found                                                                              | [HTTPError](#HTTP%5FError)                                                   |
| 500       | A problem occurred in regards to the token                                                               | [PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse)       |

#### [](#get%5Fdb-%5Foidc%5Fchallenge)OpenID Connect authentication initiation via WWW-Authenticate header

GET /{db}/_oidc_challenge

##### [](#get%5Fdb-%5Foidc%5Fchallenge-description)Description

Called by clients to initiate the OpenID Connect Authorization Code Flow. This will establish a connection with the provider, then put the redirect URL in the `WWW-Authenticate` header.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc%5Fchallenge-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                    | Description                                                                                                                                                                                                          | Schema |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **provider** _optional_ | The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                               | String |
| **offline** _optional_  | If true, the OpenID Connect provider is requested to confirm with the user the permissions requested and refresh the OIDC token. To do this, access\_type=offline and prompt=consent is set on the redirection link. | String |

##### [](#get%5Fdb-%5Foidc%5Fchallenge-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| 400       | The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. |                            |
| 401       | Successfully connected with the OpenID Connect provider so now the client can login.                                                 |                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError) |
| 500       | Unable to connect and validate with the OpenID Connect provider requested                                                            |                            |

#### [](#get%5Fdb-%5Foidc%5Frefresh)OpenID Connect token refresh

GET /{db}/_oidc_refresh

##### [](#get%5Fdb-%5Foidc%5Frefresh-description)Description

Refresh the OpenID Connect token based on the provided refresh token.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc%5Frefresh-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                          | Description                                                                                                                                                            | Schema |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **refresh\_token** _required_ | The OpenID Connect refresh token.                                                                                                                                      | String |
| **provider** _optional_       | The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used. | String |

##### [](#get%5Fdb-%5Foidc%5Frefresh-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| 200       | Successfully authenticated with OpenID Connect.                                                                                      | [OpenIDConnectCallbackProperties](#OpenID%5FConnect%5Fcallback%5Fproperties) |
| 400       | The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. |                                                                              |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError)                                                   |
| 500       | Unable to connect and validate with the OpenID Connect provider requested                                                            |                                                                              |

#### [](#get%5Fdb-%5Foidc%5Ftesting-.well-known-openid-configuration)OpenID Connect mock provider

GET /{db}/_oidc_testing/.well-known/openid-configuration

##### [](#get%5Fdb-%5Foidc%5Ftesting-.well-known-openid-configuration-description)Description

Mock an OpenID Connect provider response for testing purposes. This returns a response that is the same structure as what Sync Gateway expects from an OIDC provider after initiating OIDC authentication.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc%5Ftesting-.well-known-openid-configuration-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#get%5Fdb-%5Foidc%5Ftesting-.well-known-openid-configuration-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                                                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200       | Successfully generated OpenID Connect provider mock response.                                                                        | [GetDbOidcTestingWellKnownOpenidConfiguration200Response](#get%5Fdb%5F%5Foidc%5Ftesting%5F%5Fwell%5Fknown%5Fopenid%5Fconfiguration%5F200%5Fresponse) |
| 403       | The OpenID Connect unsupported config option oidc\_test\_provider is not enabled. To use this endpoint, this option must be enabled. |                                                                                                                                                      |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError)                                                                                                                           |

#### [](#get%5Fdb-%5Foidc%5Ftesting-authenticate)OpenID Connect mock login page handler

GET /{db}/_oidc_testing/authenticate

##### [](#get%5Fdb-%5Foidc%5Ftesting-authenticate-description)Description

Used to handle the login page displayed for the `GET /{db}/_oidc_testing/authorize` endpoint.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc%5Ftesting-authenticate-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                                  | Description                                   | Schema  |
| ------------------------------------- | --------------------------------------------- | ------- |
| **redirect\_uri** _optional_          | The Sync Gateway OpenID Connect callback URL. | String  |
| **scope** _required_                  | The OpenID Connect authentication scope.      | String  |
| **username** _required_               |                                               | String  |
| **tokenttl** _required_               |                                               | Integer |
| **identity-token-formats** _required_ |                                               | String  |
| **authenticated** _required_          |                                               | String  |

##### [](#get%5Fdb-%5Foidc%5Ftesting-authenticate-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| 302       | Redirecting to Sync Gateway OpenID Connect callback URL                                                                              |                            |
| 403       | The OpenID Connect unsupported config option oidc\_test\_provider is not enabled. To use this endpoint, this option must be enabled. |                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Foidc%5Ftesting-authorize)OpenID Connect mock login page

GET /{db}/_oidc_testing/authorize

##### [](#get%5Fdb-%5Foidc%5Ftesting-authorize-description)Description

Show a mock OpenID Connect login page for the client to log in to.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc%5Ftesting-authorize-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                 | Description                              | Schema |
| -------------------- | ---------------------------------------- | ------ |
| **scope** _required_ | The OpenID Connect authentication scope. | String |

##### [](#get%5Fdb-%5Foidc%5Ftesting-authorize-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| 200       | OK                                                                                                                                   |                            |
| 400       | A validation error occurred with the scope.                                                                                          | [HTTPError](#HTTP%5FError) |
| 403       | The OpenID Connect unsupported config option oidc\_test\_provider is not enabled. To use this endpoint, this option must be enabled. |                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError) |
| 500       | An error occurred.                                                                                                                   | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Foidc%5Ftesting-certs)OpenID Connect public certificates for signing keys

GET /{db}/_oidc_testing/certs

##### [](#get%5Fdb-%5Foidc%5Ftesting-certs-description)Description

Return a mock OpenID Connect public key to be used as signing keys.

Produces

* application/json

##### [](#get%5Fdb-%5Foidc%5Ftesting-certs-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#get%5Fdb-%5Foidc%5Ftesting-certs-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| 200       | Returned public key successfully                                                                                                     | [GetDbOidcTestingCerts200Response](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse) |
| 403       | The OpenID Connect unsupported config option oidc\_test\_provider is not enabled. To use this endpoint, this option must be enabled. |                                                                                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError)                                                                 |
| 500       | An error occurred while getting the private RSA key                                                                                  | [PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse)                     |

#### [](#post%5Fdb-%5Ffacebook)Create a new Facebook-based session

POST /{db}/_facebook

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#post%5Fdb-%5Ffacebook-description)Description

Creates a new session based on a Facebook user. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Ffacebook-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description | Schema                                          |
| ------------------- | ----------- | ----------------------------------------------- |
| **Body** _optional_ |             | [PostDbFacebookRequest](#PostDbFacebookRequest) |

##### [](#post%5Fdb-%5Ffacebook-responses)Responses

| HTTP Code | Description                                           | Schema                                                                 |
| --------- | ----------------------------------------------------- | ---------------------------------------------------------------------- |
| 200       | Session created successfully                          |                                                                        |
| 400       | Origin is not in the approved list of allowed origins | [HTTPError](#HTTP%5FError)                                             |
| 401       | Received error from Facebook verifier                 | [PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse) |
| 404       | Resource could not be found                           | [HTTPError](#HTTP%5FError)                                             |
| 502       | Received invalid response from the Facebook verifier  | [PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse) |
| 504       | Unable to send request to Facebook API                | [PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse) |

#### [](#post%5Fdb-%5Fgoogle)Create a new Google-based session

POST /{db}/_google

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#post%5Fdb-%5Fgoogle-description)Description

Creates a new session based on a Google user. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Fgoogle-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description | Schema                                      |
| ------------------- | ----------- | ------------------------------------------- |
| **Body** _optional_ |             | [PostDbGoogleRequest](#PostDbGoogleRequest) |

##### [](#post%5Fdb-%5Fgoogle-responses)Responses

| HTTP Code | Description                                                                       | Schema                                                                 |
| --------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200       | Session created successfully                                                      |                                                                        |
| 400       | Origin is not in the approved list of allowed origins                             | [HTTPError](#HTTP%5FError)                                             |
| 401       | Received error from Google token verifier or invalid application ID in the config | [PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse) |
| 404       | Resource could not be found                                                       | [HTTPError](#HTTP%5FError)                                             |
| 502       | Received invalid response from the Google token verifier                          | [PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse) |
| 504       | Unable to send request to the Google token verifier                               |                                                                        |

#### [](#post%5Fdb-%5Foidc%5Ftesting-authenticate)OpenID Connect mock login page handler

POST /{db}/_oidc_testing/authenticate

##### [](#post%5Fdb-%5Foidc%5Ftesting-authenticate-description)Description

Used to handle the login page displayed for the `GET /{db}/_oidc_testing/authorize` endpoint.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Foidc%5Ftesting-authenticate-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                         | Description                                   | Schema |
| ---------------------------- | --------------------------------------------- | ------ |
| **redirect\_uri** _optional_ | The Sync Gateway OpenID Connect callback URL. | String |
| **scope** _required_         | The OpenID Connect authentication scope.      | String |

Body Parameter

| Name                | Description                                                              | Schema                                                                        |
| ------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **Body** _optional_ | Properties passed from the OpenID Connect mock login page to the handler | [PostDbOidcTestingAuthenticateRequest](#PostDbOidcTestingAuthenticateRequest) |

##### [](#post%5Fdb-%5Foidc%5Ftesting-authenticate-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| 302       | Redirecting to Sync Gateway OpenID Connect callback URL                                                                              |                            |
| 403       | The OpenID Connect unsupported config option oidc\_test\_provider is not enabled. To use this endpoint, this option must be enabled. |                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Foidc%5Ftesting-authorize)OpenID Connect mock login page

POST /{db}/_oidc_testing/authorize

##### [](#post%5Fdb-%5Foidc%5Ftesting-authorize-description)Description

Show a mock OpenID Connect login page for the client to log in to.

Produces

* application/json

##### [](#post%5Fdb-%5Foidc%5Ftesting-authorize-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                 | Description                              | Schema |
| -------------------- | ---------------------------------------- | ------ |
| **scope** _required_ | The OpenID Connect authentication scope. | String |

##### [](#post%5Fdb-%5Foidc%5Ftesting-authorize-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| 200       | OK                                                                                                                                   |                            |
| 400       | A validation error occurred with the scope.                                                                                          | [HTTPError](#HTTP%5FError) |
| 403       | The OpenID Connect unsupported config option oidc\_test\_provider is not enabled. To use this endpoint, this option must be enabled. |                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError) |
| 500       | An error occurred.                                                                                                                   | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Foidc%5Ftesting-token)OpenID Connect mock token

POST /{db}/_oidc_testing/token

##### [](#post%5Fdb-%5Foidc%5Ftesting-token-description)Description

Return a mock OpenID Connect token for the OIDC authentication flow.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Foidc%5Ftesting-token-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description | Schema                                                          |
| ------------------- | ----------- | --------------------------------------------------------------- |
| **Body** _optional_ |             | [PostDbOidcTestingTokenRequest](#PostDbOidcTestingTokenRequest) |

##### [](#post%5Fdb-%5Foidc%5Ftesting-token-responses)Responses

| HTTP Code | Description                                                                                                                          | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| 200       | Properties expected back from an OpenID Connect provider after successful authentication                                             | [OIDCToken](#OIDC%5Ftoken) |
| 400       | Invalid token provided                                                                                                               |                            |
| 403       | The OpenID Connect unsupported config option oidc\_test\_provider is not enabled. To use this endpoint, this option must be enabled. |                            |
| 404       | Resource could not be found                                                                                                          | [HTTPError](#HTTP%5FError) |

### [](#tag-DatabaseManagement)Database Management

**Table of Contents**

[Get database information](#get%5Fdb-)  
[Get changes list](#get%5Fkeyspace-%5Fchanges)  
[Check if database exists](#head%5Fdb-)  
[/{db}/\_changes](#head%5Fkeyspace-%5Fchanges)  
[/{db}/\_ensure\_full\_commit](#post%5Fdb-%5Fensure%5Ffull%5Fcommit)  
[Get changes list](#post%5Fkeyspace-%5Fchanges)  
[Compare revisions to what is in the database](#post%5Fkeyspace-%5Frevs%5Fdiff)  
[Create DB public API stub](#put%5Ftargetdb-)

#### [](#get%5Fdb-)Get database information

GET /{db}/

##### [](#get%5Fdb--description)Description

Retrieve information about the database.

Produces

* application/json

##### [](#get%5Fdb--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#get%5Fdb--responses)Responses

| HTTP Code | Description                                | Schema                                            |
| --------- | ------------------------------------------ | ------------------------------------------------- |
| 200       | Successfully returned database information | [GetDb200Response](#get%5Fdb%5F%5F200%5Fresponse) |
| 404       | Resource could not be found                | [HTTPError](#HTTP%5FError)                        |

#### [](#get%5Fkeyspace-%5Fchanges)Get changes list

GET /{keyspace}/_changes

##### [](#get%5Fkeyspace-%5Fchanges-description)Description

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

Produces

* application/json

##### [](#get%5Fkeyspace-%5Fchanges-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   | Schema       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **limit** _optional_         | Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                                          | Integer      |
| **since** _optional_         | Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                                                                                                                              | String       |
| **style** _optional_         | Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs). **Values:** "main\_only", "all\_docs"                                                                                                                                                                                                                                             | String       |
| **active\_only** _optional_  | Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                                                 | Boolean      |
| **include\_docs** _optional_ | Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                                               | Boolean      |
| **revocations** _optional_   | If true, revocation messages will be sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                                                | Boolean      |
| **filter** _optional_        | Set a filter to either filter by channels or document IDs. **Values:** "sync\_gateway/bychannel", "\_doc\_ids"                                                                                                                                                                                                                                                                                                                                | String       |
| **channels** _optional_      | A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                                           | String       |
| **doc\_ids** _optional_      | A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal. Also accepts a comma separated list of document IDs instead.                                                                                                                                                         | String array |
| **heartbeat** _optional_     | The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This will override any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the server replication configuration. **Minimum:** 25000 | Integer      |
| **timeout** _optional_       | This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout. **Minimum:** 0 **Maximum:** 900000                                                                                                                                                               | Integer      |
| **feed** _optional_          | The type of changes feed to use. **Values:** "normal", "longpoll", "continuous", "websocket"                                                                                                                                                                                                                                                                                                                                                  | String       |

##### [](#get%5Fkeyspace-%5Fchanges-responses)Responses

| HTTP Code | Description                            | Schema                                                                         |
| --------- | -------------------------------------- | ------------------------------------------------------------------------------ |
| 200       | Successfully returned the changes feed | [GetKeyspaceChanges200Response](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse) |
| 400       | There was a problem with your request  | [HTTPError](#HTTP%5FError)                                                     |
| 404       | Resource could not be found            | [HTTPError](#HTTP%5FError)                                                     |

#### [](#head%5Fdb-)Check if database exists

HEAD /{db}/

##### [](#head%5Fdb--description)Description

Check if a database exists by using the response status code.

Produces

* application/json

##### [](#head%5Fdb--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#head%5Fdb--responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | Database exists             |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fkeyspace-%5Fchanges)/{db}/\_changes

HEAD /{keyspace}/_changes

##### [](#head%5Fkeyspace-%5Fchanges-description)Description

##### [](#head%5Fkeyspace-%5Fchanges-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

##### [](#head%5Fkeyspace-%5Fchanges-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          |        |
| 400       | Bad Request |        |
| 404       | Not Found   |        |

#### [](#post%5Fdb-%5Fensure%5Ffull%5Fcommit)/{db}/\_ensure\_full\_commit

POST /{db}/_ensure_full_commit

##### [](#post%5Fdb-%5Fensure%5Ffull%5Fcommit-description)Description

This endpoint is non-functional but is present for CouchDB compatibility.

Produces

* application/json

##### [](#post%5Fdb-%5Fensure%5Ffull%5Fcommit-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#post%5Fdb-%5Fensure%5Ffull%5Fcommit-responses)Responses

| HTTP Code | Description | Schema                                                                                       |
| --------- | ----------- | -------------------------------------------------------------------------------------------- |
| 201       | OK          | [PostDbEnsureFullCommit201Response](#post%5Fdb%5F%5Fensure%5Ffull%5Fcommit%5F201%5Fresponse) |

#### [](#post%5Fkeyspace-%5Fchanges)Get changes list

POST /{keyspace}/_changes

##### [](#post%5Fkeyspace-%5Fchanges-description)Description

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fkeyspace-%5Fchanges-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Body Parameter

| Name                | Description | Schema                                                    |
| ------------------- | ----------- | --------------------------------------------------------- |
| **Body** _optional_ |             | [PostKeyspaceChangesRequest](#PostKeyspaceChangesRequest) |

##### [](#post%5Fkeyspace-%5Fchanges-responses)Responses

| HTTP Code | Description                            | Schema                                                                         |
| --------- | -------------------------------------- | ------------------------------------------------------------------------------ |
| 200       | Successfully returned the changes feed | [GetKeyspaceChanges200Response](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse) |
| 400       | There was a problem with your request  | [HTTPError](#HTTP%5FError)                                                     |
| 404       | Resource could not be found            | [HTTPError](#HTTP%5FError)                                                     |

#### [](#post%5Fkeyspace-%5Frevs%5Fdiff)Compare revisions to what is in the database

POST /{keyspace}/_revs_diff

##### [](#post%5Fkeyspace-%5Frevs%5Fdiff-description)Description

Takes a set of document IDs, each with a set of revision IDs. For each document, an array of unknown revisions are returned with an array of known revisions that may be recent ancestors.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fkeyspace-%5Frevs%5Fdiff-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Body Parameter

| Name                | Description | Schema                                                      |
| ------------------- | ----------- | ----------------------------------------------------------- |
| **Body** _optional_ |             | [PostKeyspaceRevsDiffRequest](#PostKeyspaceRevsDiffRequest) |

##### [](#post%5Fkeyspace-%5Frevs%5Fdiff-responses)Responses

| HTTP Code | Description                 | Schema                                                                                |
| --------- | --------------------------- | ------------------------------------------------------------------------------------- |
| 200       | Comparisons successful      | [PostKeyspaceRevsDiff200Response](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse) |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError)                                                            |

#### [](#put%5Ftargetdb-)Create DB public API stub

PUT /{targetdb}/

##### [](#put%5Ftargetdb--description)Description

A stub that always returns an error on the Public API, for createTarget/CouchDB compatibility.

##### [](#put%5Ftargetdb--parameters)Parameters

Path Parameters

| Name                    | Description                  | Schema |
| ----------------------- | ---------------------------- | ------ |
| **targetdb** _required_ | The database name to target. | String |

##### [](#put%5Ftargetdb--responses)Responses

| HTTP Code | Description                                                       | Schema |
| --------- | ----------------------------------------------------------------- | ------ |
| 403       | Database does not exist and cannot be created over the public API |        |
| 412       | Database exists                                                   |        |

### [](#tag-Document)Document

Create and manage documents

[Delete a document](#delete%5Fkeyspace-docid)  
[Delete a local document](#delete%5Fkeyspace-%5Flocal-docid)  
[Gets all the documents in the database with the given parameters](#get%5Fkeyspace-%5Fall%5Fdocs)  
[Get a document](#get%5Fkeyspace-docid)  
[Get local document](#get%5Fkeyspace-%5Flocal-docid)  
[/{db}/\_all\_docs](#head%5Fkeyspace-%5Fall%5Fdocs)  
[Check if a document exists](#head%5Fkeyspace-docid)  
[Check if local document exists](#head%5Fkeyspace-%5Flocal-docid)  
[Create a new document](#post%5Fkeyspace-)  
[Get all the documents in the database using a built-in view](#post%5Fkeyspace-%5Fall%5Fdocs)  
[Bulk document operations](#post%5Fkeyspace-%5Fbulk%5Fdocs)  
[Get multiple documents in a MIME multipart response](#post%5Fkeyspace-%5Fbulk%5Fget)  
[Upsert a document](#put%5Fkeyspace-docid)  
[Upsert a local document](#put%5Fkeyspace-%5Flocal-docid)

#### [](#delete%5Fkeyspace-docid)Delete a document

DELETE /{keyspace}/{docid}

##### [](#delete%5Fkeyspace-docid-description)Description

Delete a document from the database. A new revision is created so the database can track the deletion in synchronized copies.

A revision ID either in the header or on the query parameters is required.

Produces

* application/json

##### [](#delete%5Fkeyspace-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                               | String |

Query Parameters

| Name               | Description                      | Schema |
| ------------------ | -------------------------------- | ------ |
| **rev** _optional_ | The document revision to target. | String |

Header Parameters

| Name                    | Description                | Schema |
| ----------------------- | -------------------------- | ------ |
| **If-Match** _optional_ | The revision ID to target. | String |

##### [](#delete%5Fkeyspace-docid-responses)Responses

| HTTP Code | Description                           | Schema                         |
| --------- | ------------------------------------- | ------------------------------ |
| 200       | New revision created successfully     | [NewRevision](#New%5Frevision) |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError)     |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError)     |

#### [](#delete%5Fkeyspace-%5Flocal-docid)Delete a local document

DELETE /{keyspace}/_local/{docid}

##### [](#delete%5Fkeyspace-%5Flocal-docid-description)Description

This request deletes a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Produces

* application/json

##### [](#delete%5Fkeyspace-%5Flocal-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The name of the local document ID excluding the \_local/ prefix.                                                                                            | String |

Query Parameters

| Name               | Description                                | Schema |
| ------------------ | ------------------------------------------ | ------ |
| **rev** _required_ | The revision ID of the revision to delete. | String |

##### [](#delete%5Fkeyspace-%5Flocal-docid-responses)Responses

| HTTP Code | Description                                                               | Schema                     |
| --------- | ------------------------------------------------------------------------- | -------------------------- |
| 200       | Successfully removed the local document.                                  |                            |
| 400       | There was a problem with your request                                     | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                                               | [HTTPError](#HTTP%5FError) |
| 409       | A revision ID conflict would result from deleting this document revision. |                            |

#### [](#get%5Fkeyspace-%5Fall%5Fdocs)Gets all the documents in the database with the given parameters

GET /{keyspace}/_all_docs

##### [](#get%5Fkeyspace-%5Fall%5Fdocs-description)Description

Returns all documents in the database based on the specified parameters.

Produces

* application/json

##### [](#get%5Fkeyspace-%5Fall%5Fdocs-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                         | Description                                                                                            | Schema       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| **include\_docs** _optional_ | Include the body associated with each document.                                                        | Boolean      |
| **channels** _optional_      | Include the channels each document is part of that the calling user also has access too.               | Boolean      |
| **access** _optional_        | Include what user/roles that each document grants access too.                                          | Boolean      |
| **revs** _optional_          | Include all the revisions for each document under the \_revisions property.                            | Boolean      |
| **update\_seq** _optional_   | Include the document sequence number update\_seq property for each document.                           | Boolean      |
| **keys** _optional_          | An array of document ID strings to filter by.                                                          | String array |
| **startkey** _optional_      | Return records starting with the specified key.                                                        | String       |
| **endkey** _optional_        | Stop returning records when this key is reached.                                                       | String       |
| **limit** _optional_         | This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. | Big Decimal  |

##### [](#get%5Fkeyspace-%5Fall%5Fdocs-responses)Responses

| HTTP Code | Description                           | Schema                                                                            |
| --------- | ------------------------------------- | --------------------------------------------------------------------------------- |
| 200       | Operation ran successfully            | [GetKeyspaceAllDocs200Response](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse) |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError)                                                        |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError)                                                        |

#### [](#get%5Fkeyspace-docid)Get a document

GET /{keyspace}/{docid}

##### [](#get%5Fkeyspace-docid-description)Description

Retrieve a document from the database by its doc ID.

Produces

* application/json

##### [](#get%5Fkeyspace-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                               | String |

Query Parameters

| Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                             | Schema       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **rev** _optional_         | The document revision to target.                                                                                                                                                                                                                                                                                                                                                                                        | String       |
| **open\_revs** _optional_  | Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only leaf revision bodies that haven't been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. | String array |
| **show\_exp** _optional_   | Whether to show the expiry property (\_exp) in the response.                                                                                                                                                                                                                                                                                                                                                            | Boolean      |
| **revs\_from** _optional_  | Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit.                                                                                                                                                                                                                                                                   | String array |
| **atts\_since** _optional_ | Include attachments only since specified revisions. Excludes the attachments for the specified revisions. Only gets used if attachments=true.                                                                                                                                                                                                                                                                           | String array |
| **revs\_limit** _optional_ | Maximum amount of revisions to return for each document.                                                                                                                                                                                                                                                                                                                                                                | Integer      |
| **attachments** _optional_ | Include attachment bodies in response.                                                                                                                                                                                                                                                                                                                                                                                  | Boolean      |
| **replicator2** _optional_ | Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                          | Boolean      |

##### [](#get%5Fkeyspace-docid-responses)Responses

| HTTP Code | Description                                                                                                                                             | Schema                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 200       | Document found and returned successfully                                                                                                                | [GetKeyspaceDocid200Response](#get%5Fkeyspace%5Fdocid%5F200%5Fresponse) |
| 400       | Document ID is not in an allowed format therefore is invalid. This could be because it is over 250 characters or is prefixed with an underscore ("\_"). | [HTTPError](#HTTP%5FError)                                              |
| 404       | Resource could not be found                                                                                                                             | [HTTPError](#HTTP%5FError)                                              |
| 501       | Not Implemented. It is likely this error was caused due to trying to use an enterprise-only feature on the community edition.                           | [HTTPError](#HTTP%5FError)                                              |

#### [](#get%5Fkeyspace-%5Flocal-docid)Get local document

GET /{keyspace}/_local/{docid}

##### [](#get%5Fkeyspace-%5Flocal-docid-description)Description

This request retrieves a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Produces

* application/json

##### [](#get%5Fkeyspace-%5Flocal-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The name of the local document ID excluding the \_local/ prefix.                                                                                            | String |

##### [](#get%5Fkeyspace-%5Flocal-docid-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Successfully found local document     |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fkeyspace-%5Fall%5Fdocs)/{db}/\_all\_docs

HEAD /{keyspace}/_all_docs

##### [](#head%5Fkeyspace-%5Fall%5Fdocs-description)Description

Produces

* application/json

##### [](#head%5Fkeyspace-%5Fall%5Fdocs-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                         | Description                                                                                            | Schema       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ | ------------ |
| **include\_docs** _optional_ | Include the body associated with each document.                                                        | Boolean      |
| **channels** _optional_      | Include the channels each document is part of that the calling user also has access too.               | Boolean      |
| **access** _optional_        | Include what user/roles that each document grants access too.                                          | Boolean      |
| **revs** _optional_          | Include all the revisions for each document under the \_revisions property.                            | Boolean      |
| **update\_seq** _optional_   | Include the document sequence number update\_seq property for each document.                           | Boolean      |
| **keys** _optional_          | An array of document ID strings to filter by.                                                          | String array |
| **startkey** _optional_      | Return records starting with the specified key.                                                        | String       |
| **endkey** _optional_        | Stop returning records when this key is reached.                                                       | String       |
| **limit** _optional_         | This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. | Big Decimal  |

##### [](#head%5Fkeyspace-%5Fall%5Fdocs-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | OK                                    |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fkeyspace-docid)Check if a document exists

HEAD /{keyspace}/{docid}

##### [](#head%5Fkeyspace-docid-description)Description

Return a status code based on if the document exists or not.

Produces

* application/json

##### [](#head%5Fkeyspace-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                               | String |

Query Parameters

| Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                             | Schema       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **rev** _optional_         | The document revision to target.                                                                                                                                                                                                                                                                                                                                                                                        | String       |
| **open\_revs** _optional_  | Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only leaf revision bodies that haven't been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. | String array |
| **show\_exp** _optional_   | Whether to show the expiry property (\_exp) in the response.                                                                                                                                                                                                                                                                                                                                                            | Boolean      |
| **revs\_from** _optional_  | Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit.                                                                                                                                                                                                                                                                   | String array |
| **atts\_since** _optional_ | Include attachments only since specified revisions. Excludes the attachments for the specified revisions. Only gets used if attachments=true.                                                                                                                                                                                                                                                                           | String array |
| **revs\_limit** _optional_ | Maximum amount of revisions to return for each document.                                                                                                                                                                                                                                                                                                                                                                | Integer      |
| **attachments** _optional_ | Include attachment bodies in response.                                                                                                                                                                                                                                                                                                                                                                                  | Boolean      |
| **replicator2** _optional_ | Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                          | Boolean      |

##### [](#head%5Fkeyspace-docid-responses)Responses

| HTTP Code | Description                                                                                                                                             | Schema                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Document exists                                                                                                                                         |                            |
| 400       | Document ID is not in an allowed format therefore is invalid. This could be because it is over 250 characters or is prefixed with an underscore ("\_"). | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                                                                                                                             | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fkeyspace-%5Flocal-docid)Check if local document exists

HEAD /{keyspace}/_local/{docid}

##### [](#head%5Fkeyspace-%5Flocal-docid-description)Description

This request checks if a local document exists.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Produces

* application/json

##### [](#head%5Fkeyspace-%5Flocal-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The name of the local document ID excluding the \_local/ prefix.                                                                                            | String |

##### [](#head%5Fkeyspace-%5Flocal-docid-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Document exists                       |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fkeyspace-)Create a new document

POST /{keyspace}/

##### [](#post%5Fkeyspace--description)Description

Create a new document in the keyspace.

This will generate a random document ID unless specified in the body.

A document can have a maximum size of 20MB.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fkeyspace--parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                     | Description                                            | Schema  |
| ------------------------ | ------------------------------------------------------ | ------- |
| **roundtrip** _optional_ | Block until document has been received by change cache | Boolean |

Body Parameter

| Name                | Description | Schema                                      |
| ------------------- | ----------- | ------------------------------------------- |
| **Body** _optional_ |             | [PostKeyspaceRequest](#PostKeyspaceRequest) |

##### [](#post%5Fkeyspace--responses)Responses

| HTTP Code | Description                                 | Schema                         |
| --------- | ------------------------------------------- | ------------------------------ |
| 200       | New document revision created successfully. | [NewRevision](#New%5Frevision) |
| 400       | There was a problem with your request       | [HTTPError](#HTTP%5FError)     |
| 404       | Resource could not be found                 | [HTTPError](#HTTP%5FError)     |
| 409       | Resource already exists under that name     | [HTTPError](#HTTP%5FError)     |
| 415       | Invalid content type                        | [HTTPError](#HTTP%5FError)     |

#### [](#post%5Fkeyspace-%5Fall%5Fdocs)Get all the documents in the database using a built-in view

POST /{keyspace}/_all_docs

##### [](#post%5Fkeyspace-%5Fall%5Fdocs-description)Description

Returns all documents in the database based on the specified parameters.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fkeyspace-%5Fall%5Fdocs-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                         | Description                                                                                            | Schema      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| **include\_docs** _optional_ | Include the body associated with each document.                                                        | Boolean     |
| **channels** _optional_      | Include the channels each document is part of that the calling user also has access too.               | Boolean     |
| **access** _optional_        | Include what user/roles that each document grants access too.                                          | Boolean     |
| **revs** _optional_          | Include all the revisions for each document under the \_revisions property.                            | Boolean     |
| **update\_seq** _optional_   | Include the document sequence number update\_seq property for each document.                           | Boolean     |
| **startkey** _optional_      | Return records starting with the specified key.                                                        | String      |
| **endkey** _optional_        | Stop returning records when this key is reached.                                                       | String      |
| **limit** _optional_         | This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. | Big Decimal |

Body Parameter

| Name                | Description | Schema                                                    |
| ------------------- | ----------- | --------------------------------------------------------- |
| **Body** _optional_ |             | [PostKeyspaceAllDocsRequest](#PostKeyspaceAllDocsRequest) |

##### [](#post%5Fkeyspace-%5Fall%5Fdocs-responses)Responses

| HTTP Code | Description                           | Schema                                                                            |
| --------- | ------------------------------------- | --------------------------------------------------------------------------------- |
| 200       | Operation ran successfully            | [GetKeyspaceAllDocs200Response](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse) |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError)                                                        |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError)                                                        |

#### [](#post%5Fkeyspace-%5Fbulk%5Fdocs)Bulk document operations

POST /{keyspace}/_bulk_docs

##### [](#post%5Fkeyspace-%5Fbulk%5Fdocs-description)Description

This will allow multiple documented to be created, updated or deleted in bulk.

To create a new document, simply add the body in an object under `docs`. A doc ID will be generated by Sync Gateway unless `_id` is specified.

To update an existing document, provide the document ID (`_id`) and revision ID (`_rev`) as well as the new body values.

To delete an existing document, provide the document ID (`_id`), revision ID (`_rev`), and set the deletion flag (`_deleted`) to true.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fkeyspace-%5Fbulk%5Fdocs-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Body Parameter

| Name                | Description | Schema                                                      |
| ------------------- | ----------- | ----------------------------------------------------------- |
| **Body** _optional_ |             | [PostKeyspaceBulkDocsRequest](#PostKeyspaceBulkDocsRequest) |

##### [](#post%5Fkeyspace-%5Fbulk%5Fdocs-responses)Responses

| HTTP Code | Description                                                                                                                                                               | Schema                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 201       | Executed all operations. Each object in the returned array represents a document. Each document should be checked to make sure it was successfully added to the database. | [PostKeyspaceBulkDocs201ResponseInner](#post%5Fkeyspace%5F%5Fbulk%5Fdocs%5F201%5Fresponse%5Finner)array |
| 400       | There was a problem with your request                                                                                                                                     | [HTTPError](#HTTP%5FError)                                                                              |
| 404       | Resource could not be found                                                                                                                                               | [HTTPError](#HTTP%5FError)                                                                              |

#### [](#post%5Fkeyspace-%5Fbulk%5Fget)Get multiple documents in a MIME multipart response

POST /{keyspace}/_bulk_get

##### [](#post%5Fkeyspace-%5Fbulk%5Fget-description)Description

This request returns any number of documents, as individual bodies in a MIME multipart response.

Each enclosed body contains one requested document. The bodies appear in the same order as in the request, but can also be identified by their `X-Doc-ID` and `X-Rev-ID` headers (if the `attachments` query is `true`).

A body for a document with no attachments will have content type `application/json` and contain the document itself.

A body for a document that has attachments will be written as a nested `multipart/related` body.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fkeyspace-%5Fbulk%5Fget-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                       | Description                                                                                                                                                                                                                                | Schema  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| **attachments** _optional_ | This is for whether to include attachments in each of the documents returned or not.                                                                                                                                                       | Boolean |
| **revs** _optional_        | Include all the revisions for each document under the \_revisions property.                                                                                                                                                                | Boolean |
| **revs\_limit** _optional_ | The number of revisions to include in the response from the document history. This parameter only makes a different if the revs query parameter is set to true. The full revision history will be returned if revs is set but this is not. | Integer |

Header Parameters

| Name                                  | Description                                                                                                                                                                                                                                                                              | Schema |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **X-Accept-Part-Encoding** _optional_ | If this header includes gzip then the part HTTP compression encoding will be done.                                                                                                                                                                                                       | String |
| **Accept-Encoding** _optional_        | If this header includes gzip then the the HTTP response will be compressed. This takes priority over X-Accept-Part-Encoding. Only part compression will be done if X-Accept-Part-Encoding=gzip and the User-Agent is below 1.2 due to clients not being able to handle full compression. | String |

Body Parameter

| Name                | Description | Schema                                                    |
| ------------------- | ----------- | --------------------------------------------------------- |
| **Body** _optional_ |             | [PostKeyspaceBulkGetRequest](#PostKeyspaceBulkGetRequest) |

##### [](#post%5Fkeyspace-%5Fbulk%5Fget-responses)Responses

| HTTP Code | Description                                                  | Schema                     |
| --------- | ------------------------------------------------------------ | -------------------------- |
| 200       | Returned the requested docs as multipart/mixed response type |                            |
| 400       | Bad Request                                                  |                            |
| 404       | Resource could not be found                                  | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fkeyspace-docid)Upsert a document

PUT /{keyspace}/{docid}

##### [](#put%5Fkeyspace-docid-description)Description

This will upsert a document meaning if it does not exist, then it will be created. Otherwise a new revision will be made for the existing document. A revision ID must be provided if targetting an existing document.

A document ID must be specified for this endpoint. To let Sync Gateway generate the ID, use the `POST /{db}/` endpoint.

If a document does exist, then replace the document content with the request body. This means unspecified fields will be removed in the new revision.

The maximum size for a document is 20MB.

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fkeyspace-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                               | String |

Query Parameters

| Name                       | Description                                                                                                                                                                                                                                                                                                                         | Schema  |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **roundtrip** _optional_   | Block until document has been received by change cache                                                                                                                                                                                                                                                                              | Boolean |
| **replicator2** _optional_ | Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                      | Boolean |
| **new\_edits** _optional_  | Setting this to false indicates that the request body is an already-existing revision that should be directly inserted into the database, instead of a modification to apply to the current document. This mode is used for replication. This option must be used in conjunction with the \_revisions property in the request body. | Boolean |
| **rev** _optional_         | The document revision to target.                                                                                                                                                                                                                                                                                                    | String  |

Header Parameters

| Name                    | Description                | Schema |
| ----------------------- | -------------------------- | ------ |
| **If-Match** _optional_ | The revision ID to target. | String |

Body Parameter

| Name                | Description | Schema                                      |
| ------------------- | ----------- | ------------------------------------------- |
| **Body** _optional_ |             | [PostKeyspaceRequest](#PostKeyspaceRequest) |

##### [](#put%5Fkeyspace-docid-responses)Responses

| HTTP Code | Description                             | Schema                         |
| --------- | --------------------------------------- | ------------------------------ |
| 201       | Created                                 | [NewRevision](#New%5Frevision) |
| 400       | There was a problem with your request   | [HTTPError](#HTTP%5FError)     |
| 404       | Resource could not be found             | [HTTPError](#HTTP%5FError)     |
| 409       | Resource already exists under that name | [HTTPError](#HTTP%5FError)     |
| 415       | Invalid content type                    | [HTTPError](#HTTP%5FError)     |

#### [](#put%5Fkeyspace-%5Flocal-docid)Upsert a local document

PUT /{keyspace}/_local/{docid}

##### [](#put%5Fkeyspace-%5Flocal-docid-description)Description

This request creates or updates a local document. Updating a local document requires that the revision ID be put in the body under `_rev`.

Local document IDs are given a `_local/` prefix. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by the client's replicator, as a place to store replication checkpoint data.

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fkeyspace-%5Flocal-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The name of the local document ID excluding the \_local/ prefix.                                                                                            | String |

Body Parameter

| Name                | Description              | Schema                                                        |
| ------------------- | ------------------------ | ------------------------------------------------------------- |
| **Body** _optional_ | The body of the document | [PutKeyspaceLocalDocidRequest](#PutKeyspaceLocalDocidRequest) |

##### [](#put%5Fkeyspace-%5Flocal-docid-responses)Responses

| HTTP Code | Description                                                                    | Schema                         |
| --------- | ------------------------------------------------------------------------------ | ------------------------------ |
| 201       | Document successfully written. The document ID will be prefixed with \_local/. | [NewRevision](#New%5Frevision) |
| 400       | There was a problem with your request                                          | [HTTPError](#HTTP%5FError)     |
| 404       | Resource could not be found                                                    | [HTTPError](#HTTP%5FError)     |
| 409       | A revision ID conflict would result from updating this document revision.      |                                |

### [](#tag-DocumentAttachment)Document Attachment

**Table of Contents**

[Delete an attachment on a document](#delete%5Fkeyspace-docid-attach)  
[Get an attachment from a document](#get%5Fkeyspace-docid-attach)  
[Check if attachment exists](#head%5Fkeyspace-docid-attach)  
[Create or update an attachment on a document](#put%5Fkeyspace-docid-attach)

#### [](#delete%5Fkeyspace-docid-attach)Delete an attachment on a document

DELETE /{keyspace}/{docid}/{attach}

##### [](#delete%5Fkeyspace-docid-attach-description)Description

This request deletes an attachment associated with the document.

If the attachment exists, the attachment will be removed from the document.

Produces

* application/json

##### [](#delete%5Fkeyspace-docid-attach-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                        | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection.                                                                        | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                                                                                                      | String |
| **attach** _required_   | The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | String |

Query Parameters

| Name               | Description                                  | Schema |
| ------------------ | -------------------------------------------- | ------ |
| **rev** _optional_ | The existing document revision ID to modify. | String |

Header Parameters

| Name                    | Description                                                | Schema |
| ----------------------- | ---------------------------------------------------------- | ------ |
| **If-Match** _optional_ | An alternative way of specifying the document revision ID. | String |

##### [](#delete%5Fkeyspace-docid-attach-responses)Responses

| HTTP Code | Description                                       | Schema                         |
| --------- | ------------------------------------------------- | ------------------------------ |
| 200       | Attachment removed from the document successfully | [NewRevision](#New%5Frevision) |
| 404       | Resource could not be found                       | [HTTPError](#HTTP%5FError)     |
| 409       | Resource already exists under that name           | [HTTPError](#HTTP%5FError)     |

#### [](#get%5Fkeyspace-docid-attach)Get an attachment from a document

GET /{keyspace}/{docid}/{attach}

##### [](#get%5Fkeyspace-docid-attach-description)Description

This request retrieves a file attachment associated with the document.

The raw data of the associated attachment is returned (just as if you were accessing a static file). The `Content-Type` response header is the same content type set when the document attachment was added to the database. The `Content-Disposition` response header will be set if the content type is considered unsafe to display in a browser (unless overridden by by database config option `serve_insecure_attachment_types`) which will force the attachment to be downloaded.

If the `meta` query parameter is set then the response will be in JSON with the additional metadata tags.

Produces

* application/json

##### [](#get%5Fkeyspace-docid-attach-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                        | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection.                                                                        | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                                                                                                      | String |
| **attach** _required_   | The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | String |

Query Parameters

| Name                             | Description                                                      | Schema  |
| -------------------------------- | ---------------------------------------------------------------- | ------- |
| **rev** _optional_               | The document revision to target.                                 | String  |
| **content\_encoding** _optional_ | Set to false to disable the Content-Encoding response header.    | Boolean |
| **meta** _optional_              | Return only the metadata of the attachment in the response body. | Boolean |

Header Parameters

| Name                 | Description                  | Schema |
| -------------------- | ---------------------------- | ------ |
| **Range** _optional_ | RFC-2616 bytes range header. | String |

##### [](#get%5Fkeyspace-docid-attach-responses)Responses

| HTTP Code | Description                            | Schema                     |
| --------- | -------------------------------------- | -------------------------- |
| 200       | Found attachment successfully.         |                            |
| 206       | Partial attachment content returned    |                            |
| 404       | Resource could not be found            | [HTTPError](#HTTP%5FError) |
| 416       | Requested range exceeds content length |                            |

#### [](#head%5Fkeyspace-docid-attach)Check if attachment exists

HEAD /{keyspace}/{docid}/{attach}

##### [](#head%5Fkeyspace-docid-attach-description)Description

This request check if the attachment exists on the specified document.

Produces

* application/json

##### [](#head%5Fkeyspace-docid-attach-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                        | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection.                                                                        | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                                                                                                      | String |
| **attach** _required_   | The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | String |

Query Parameters

| Name               | Description                      | Schema |
| ------------------ | -------------------------------- | ------ |
| **rev** _optional_ | The document revision to target. | String |

##### [](#head%5Fkeyspace-docid-attach-responses)Responses

| HTTP Code | Description                                                    | Schema                     |
| --------- | -------------------------------------------------------------- | -------------------------- |
| 200       | The document exists and the attachment exists on the document. |                            |
| 404       | Resource could not be found                                    | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fkeyspace-docid-attach)Create or update an attachment on a document

PUT /{keyspace}/{docid}/{attach}

##### [](#put%5Fkeyspace-docid-attach-description)Description

This request adds or updates an attachment associated with the document. If the document does not exist, it will be created and the attachment will be added to it.

If the attachment already exists, the data of the existing attachment will be replaced in the new revision.

The maximum content size of an attachment is 20MB. The `Content-Type` header of the request specifies the content type of the attachment.

Consumes

* Attachment content type

Produces

* application/json

##### [](#put%5Fkeyspace-docid-attach-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                        | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection.                                                                        | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                                                                                                      | String |
| **attach** _required_   | The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | String |

Query Parameters

| Name               | Description                                                                                     | Schema |
| ------------------ | ----------------------------------------------------------------------------------------------- | ------ |
| **rev** _optional_ | The existing document revision ID to modify. Required only when modifying an existing document. | String |

Header Parameters

| Name                        | Description                                                | Schema |
| --------------------------- | ---------------------------------------------------------- | ------ |
| **Content-Type** _optional_ | The content type of the attachment.                        | String |
| **If-Match** _optional_     | An alternative way of specifying the document revision ID. | String |

Body Parameter

| Name                | Description         | Schema |
| ------------------- | ------------------- | ------ |
| **Body** _optional_ | The attachment data | String |

##### [](#put%5Fkeyspace-docid-attach-responses)Responses

| HTTP Code | Description                                               | Schema                         |
| --------- | --------------------------------------------------------- | ------------------------------ |
| 201       | Attachment added to new or existing document successfully | [NewRevision](#New%5Frevision) |
| 404       | Resource could not be found                               | [HTTPError](#HTTP%5FError)     |
| 409       | Resource already exists under that name                   | [HTTPError](#HTTP%5FError)     |

### [](#tag-Replication)Replication

Create and manage inter-Sync Gateway replications

[Handle incoming BLIP Sync web socket request](#get%5Fdb-%5Fblipsync)

#### [](#get%5Fdb-%5Fblipsync)Handle incoming BLIP Sync web socket request

GET /{db}/_blipsync

##### [](#get%5Fdb-%5Fblipsync-description)Description

This handles incoming BLIP Sync requests from either Couchbase Lite or another Sync Gateway node. The connection has to be upgradable to a websocket connection or else the request will fail.

Produces

* application/json

##### [](#get%5Fdb-%5Fblipsync-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                  | Description                                                                                                                                          | Schema |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **client** _optional_ | This is the client type that is making the BLIP Sync request. Used to control client-type specific replication behaviour. **Values:** "cbl2", "sgr2" | String |

##### [](#get%5Fdb-%5Fblipsync-responses)Responses

| HTTP Code | Description                                          | Schema                     |
| --------- | ---------------------------------------------------- | -------------------------- |
| 101       | Upgraded to a web socket connection                  |                            |
| 404       | Resource could not be found                          | [HTTPError](#HTTP%5FError) |
| 426       | Cannot upgrade connection to a web socket connection | [HTTPError](#HTTP%5FError) |

### [](#tag-Server)Server

Manage server activities

[Get server information](#get%5F-)  
[Check if API is available](#get%5F%5Fping)  
[Check if server online](#head%5F-)  
[Check if API is available](#head%5F%5Fping)

#### [](#get%5F-)Get server information

GET /

##### [](#get%5F--description)Description

Returns information about the Sync Gateway node.

Produces

* application/json

##### [](#get%5F--responses)Responses

| HTTP Code | Description                 | Schema                                        |
| --------- | --------------------------- | --------------------------------------------- |
| 200       | Returned server information | [Get200Response](#get%5F%5F%5F200%5Fresponse) |

#### [](#get%5F%5Fping)Check if API is available

GET /_ping

##### [](#get%5F%5Fping-description)Description

Returns OK status if API is available.

Produces

* text/plain

##### [](#get%5F%5Fping-responses)Responses

| HTTP Code | Description     | Schema |
| --------- | --------------- | ------ |
| 200       | Returned status | String |

#### [](#head%5F-)Check if server online

HEAD /

##### [](#head%5F--description)Description

Check if the server is online by checking the status code of response.

##### [](#head%5F--responses)Responses

| HTTP Code | Description      | Schema |
| --------- | ---------------- | ------ |
| 200       | Server is online |        |

#### [](#head%5F%5Fping)Check if API is available

HEAD /_ping

##### [](#head%5F%5Fping-description)Description

Returns OK status if API is available.

##### [](#head%5F%5Fping-responses)Responses

| HTTP Code | Description         | Schema |
| --------- | ------------------- | ------ |
| 200       | Server is available |        |

### [](#tag-Session)Session

Manage user sessions

[Log out](#delete%5Fdb-%5Fsession)  
[Get information about the current user](#get%5Fdb-%5Fsession)  
[/{db}/\_session](#head%5Fdb-%5Fsession)  
[Create a new user session](#post%5Fdb-%5Fsession)

#### [](#delete%5Fdb-%5Fsession)Log out

DELETE /{db}/_session

##### [](#delete%5Fdb-%5Fsession-description)Description

Invalidates the session for the currently authenticated user and removes their session cookie.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

Produces

* application/json

##### [](#delete%5Fdb-%5Fsession-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#delete%5Fdb-%5Fsession-responses)Responses

| HTTP Code | Description                               | Schema                     |
| --------- | ----------------------------------------- | -------------------------- |
| 200       | Successfully removed session (logged out) |                            |
| 400       | Bad Request                               |                            |
| 404       | Resource could not be found               | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Fsession)Get information about the current user

GET /{db}/_session

##### [](#get%5Fdb-%5Fsession-description)Description

This will get the information about the current user.

Produces

* application/json

##### [](#get%5Fdb-%5Fsession-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#get%5Fdb-%5Fsession-responses)Responses

| HTTP Code | Description                               | Schema                                                  |
| --------- | ----------------------------------------- | ------------------------------------------------------- |
| 200       | Properties associated with a user session | [UserSessionInformation](#User%5FSession%5FInformation) |
| 404       | Resource could not be found               | [HTTPError](#HTTP%5FError)                              |

#### [](#head%5Fdb-%5Fsession)/{db}/\_session

HEAD /{db}/_session

##### [](#head%5Fdb-%5Fsession-description)Description

Produces

* application/json

##### [](#head%5Fdb-%5Fsession-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#head%5Fdb-%5Fsession-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | OK                          |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Fsession)Create a new user session

POST /{db}/_session

##### [](#post%5Fdb-%5Fsession-description)Description

Generates a login session for the user based on the credentials provided in the request body or if that fails (due to invalid credentials or none provided at all), generates the new session for the currently authenticated user instead. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Fsession-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description                                               | Schema                                        |
| ------------------- | --------------------------------------------------------- | --------------------------------------------- |
| **Body** _optional_ | The body can depend on if using the Public or Admin APIs. | [PostDbSessionRequest](#PostDbSessionRequest) |

##### [](#post%5Fdb-%5Fsession-responses)Responses

| HTTP Code | Description                                                                               | Schema                                                               |
| --------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 200       | Session created successfully. Returned body is dependant on if using Public or Admin APIs | [PostDbSession200Response](#post%5Fdb%5F%5Fsession%5F200%5Fresponse) |
| 400       | Origin is not in the approved list of allowed origins                                     | [HTTPError](#HTTP%5FError)                                           |
| 404       | Resource could not be found                                                               | [HTTPError](#HTTP%5FError)                                           |

### [](#tag-Unsupported)Unsupported

Endpoints that are not supported by Sync Gateway

[Delete a design document | Unsupported](#delete%5Fdb-%5Fdesign-ddoc)  
[Get views of a design document | Unsupported](#get%5Fdb-%5Fdesign-ddoc)  
[Query a view on a design document | Unsupported](#get%5Fdb-%5Fdesign-ddoc-%5Fview-view)  
[Check if view of design document exists | Unsupported](#head%5Fdb-%5Fdesign-ddoc)  
[Update views of a design document | Unsupported](#put%5Fdb-%5Fdesign-ddoc)

#### [](#delete%5Fdb-%5Fdesign-ddoc)Delete a design document | Unsupported

DELETE /{db}/_design/{ddoc}

##### [](#delete%5Fdb-%5Fdesign-ddoc-description)Description

**This is unsupported**

Delete a design document.

Produces

* application/json

##### [](#delete%5Fdb-%5Fdesign-ddoc-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **ddoc** _required_ | The design document name.                              | String |

##### [](#delete%5Fdb-%5Fdesign-ddoc-responses)Responses

| HTTP Code | Description                                                                                                     | Schema                     |
| --------- | --------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Design document deleted successfully                                                                            |                            |
| 403       | Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one. |                            |
| 404       | Resource could not be found                                                                                     | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Fdesign-ddoc)Get views of a design document | Unsupported

GET /{db}/_design/{ddoc}

##### [](#get%5Fdb-%5Fdesign-ddoc-description)Description

**This is unsupported**

Query a design document.

Produces

* application/json

##### [](#get%5Fdb-%5Fdesign-ddoc-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **ddoc** _required_ | The design document name.                              | String |

##### [](#get%5Fdb-%5Fdesign-ddoc-responses)Responses

| HTTP Code | Description                                                                                                     | Schema                                                                      |
| --------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 200       | Successfully returned design document.                                                                          | [GetDbDesignDdoc200Response](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse) |
| 403       | Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one. |                                                                             |
| 404       | Resource could not be found                                                                                     | [HTTPError](#HTTP%5FError)                                                  |

#### [](#get%5Fdb-%5Fdesign-ddoc-%5Fview-view)Query a view on a design document | Unsupported

GET /{db}/_design/{ddoc}/_view/{view}

##### [](#get%5Fdb-%5Fdesign-ddoc-%5Fview-view-description)Description

**This is unsupported**

Query a view on a design document.

Produces

* application/json

##### [](#get%5Fdb-%5Fdesign-ddoc-%5Fview-view-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **ddoc** _required_ | The design document name.                              | String |
| **view** _required_ | The view to target.                                    | String |

Query Parameters

| Name                           | Description                                                                                                                                                          | Schema       |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **inclusive\_end** _optional_  | Indicates whether the specified end key should be included in the result.                                                                                            | Boolean      |
| **descending** _optional_      | Return documents in descending order.                                                                                                                                | Boolean      |
| **include\_docs** _optional_   | Only works when using Couchbase Server 3.0 and earlier. Indicates whether to include the full content of the documents in the response.                              | Boolean      |
| **reduce** _optional_          | Whether to execute a reduce function on the response or not.                                                                                                         | Boolean      |
| **group** _optional_           | Group the results using the reduce function to a group or single row.                                                                                                | Boolean      |
| **skip** _optional_            | Skip the specified number of documents before starting to return results.                                                                                            | Integer      |
| **limit** _optional_           | Return only the specified number of documents                                                                                                                        | Integer      |
| **group\_level** _optional_    | Specify the group level to be used.                                                                                                                                  | Integer      |
| **startkey\_docid** _optional_ | Return documents starting with the specified document identifier.                                                                                                    | String       |
| **endkey\_docid** _optional_   | Stop returning records when the specified document identifier is reached.                                                                                            | String       |
| **stale** _optional_           | Allow the results from a stale view to be used, without triggering a rebuild of all views within the encompassing design document. **Values:** "ok", "update\_after" | String       |
| **startkey** _optional_        | Return records starting with the specified key.                                                                                                                      | String       |
| **endkey** _optional_          | Stop returning records when this key is reached.                                                                                                                     | String       |
| **key** _optional_             | Return only the document that matches the specified key.                                                                                                             | String       |
| **keys** _optional_            | An array of document ID strings to filter by.                                                                                                                        | String array |

##### [](#get%5Fdb-%5Fdesign-ddoc-%5Fview-view-responses)Responses

| HTTP Code | Description                 | Schema                                                                                               |
| --------- | --------------------------- | ---------------------------------------------------------------------------------------------------- |
| 200       | Returned view successfully  | [GetDbDesignDdocViewView200Response](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse) |
| 403       | Forbidden                   |                                                                                                      |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError)                                                                           |

#### [](#head%5Fdb-%5Fdesign-ddoc)Check if view of design document exists | Unsupported

HEAD /{db}/_design/{ddoc}

##### [](#head%5Fdb-%5Fdesign-ddoc-description)Description

**This is unsupported**

Check if a design document can be queried.

Produces

* application/json

##### [](#head%5Fdb-%5Fdesign-ddoc-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **ddoc** _required_ | The design document name.                              | String |

##### [](#head%5Fdb-%5Fdesign-ddoc-responses)Responses

| HTTP Code | Description                                                                                                     | Schema                     |
| --------- | --------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Design document exists                                                                                          |                            |
| 403       | Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one. |                            |
| 404       | Resource could not be found                                                                                     | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fdb-%5Fdesign-ddoc)Update views of a design document | Unsupported

PUT /{db}/_design/{ddoc}

##### [](#put%5Fdb-%5Fdesign-ddoc-description)Description

**This is unsupported**

Update the views of a design document.

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fdb-%5Fdesign-ddoc-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **ddoc** _required_ | The design document name.                              | String |

Body Parameter

| Name                | Description | Schema                                                    |
| ------------------- | ----------- | --------------------------------------------------------- |
| **Body** _optional_ |             | [GetDbDesignDdoc200Response](#GetDbDesignDdoc200Response) |

##### [](#put%5Fdb-%5Fdesign-ddoc-responses)Responses

| HTTP Code | Description                                                                                                     | Schema                     |
| --------- | --------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Design document changes successfully                                                                            |                            |
| 403       | Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one. |                            |
| 404       | Resource could not be found                                                                                     | [HTTPError](#HTTP%5FError) |

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[ChangesFeed](#Changes-feed)  
[DesignDoc](#Design-doc)  
[Document](#Document)  
[Get200Response](#get%5F%5F%5F200%5Fresponse)  
[Get200ResponseVendor](#get%5F%5F%5F200%5Fresponse%5Fvendor)  
[GetDb200Response](#get%5Fdb%5F%5F200%5Fresponse)  
[GetDbDesignDdoc200Response](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse)  
[GetDbDesignDdoc200ResponseOptions](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Foptions)  
[GetDbDesignDdoc200ResponseViewsValue](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Fviews%5Fvalue)  
[GetDbDesignDdocViewView200Response](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse)  
[GetDbDesignDdocViewView200ResponseErrorsInner](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse%5Ferrors%5Finner)  
[GetDbDesignDdocViewView200ResponseRowsInner](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse%5Frows%5Finner)  
[GetDbOidcTestingCerts200Response](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse)  
[GetDbOidcTestingCerts200ResponseKeysInner](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse%5Fkeys%5Finner)  
[GetDbOidcTestingWellKnownOpenidConfiguration200Response](#get%5Fdb%5F%5Foidc%5Ftesting%5F%5Fwell%5Fknown%5Fopenid%5Fconfiguration%5F200%5Fresponse)  
[GetKeyspaceAllDocs200Response](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse)  
[GetKeyspaceAllDocs200ResponseRowsInner](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner)  
[GetKeyspaceAllDocs200ResponseRowsInnerValue](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner%5Fvalue)  
[GetKeyspaceChanges200Response](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse)  
[GetKeyspaceChanges200ResponseResultsInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner)  
[GetKeyspaceChanges200ResponseResultsInnerChangesInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner%5Fchanges%5Finner)  
[GetKeyspaceDocid200Response](#get%5Fkeyspace%5Fdocid%5F200%5Fresponse)  
[HTTP-Error](#HTTP%5FError)  
[New-revision](#New%5Frevision)  
[NodeInfo](#NodeInfo)  
[OpenID Connect callback properties](#OIDC-callback)  
[OIDCLoginPageHandler](#OIDC-login-page-handler)  
[OIDC-token](#OIDC%5Ftoken)  
[OpenID Connect callback properties](#OpenID%5FConnect%5Fcallback%5Fproperties)  
[PostDbEnsureFullCommit201Response](#post%5Fdb%5F%5Fensure%5Ffull%5Fcommit%5F201%5Fresponse)  
[PostDbFacebook401Response](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse)  
[PostDbFacebookRequest](#post%5Fdb%5F%5Ffacebook%5Frequest)  
[PostDbGoogleRequest](#post%5Fdb%5F%5Fgoogle%5Frequest)  
[PostDbOidcTestingAuthenticateRequest](#post%5Fdb%5F%5Foidc%5Ftesting%5Fauthenticate%5Frequest)  
[PostDbOidcTestingTokenRequest](#post%5Fdb%5F%5Foidc%5Ftesting%5Ftoken%5Frequest)  
[PostDbSession200Response](#post%5Fdb%5F%5Fsession%5F200%5Fresponse)  
[PostDbSession200ResponseUserCtx](#post%5Fdb%5F%5Fsession%5F200%5Fresponse%5FuserCtx)  
[PostDbSession200ResponseUserCtxChannelsValue](#post%5Fdb%5F%5Fsession%5F200%5Fresponse%5FuserCtx%5Fchannels%5Fvalue)  
[PostDbSessionRequest](#post%5Fdb%5F%5Fsession%5Frequest)  
[PostKeyspaceAllDocsRequest](#post%5Fkeyspace%5F%5Fall%5Fdocs%5Frequest)  
[PostKeyspaceBulkDocs201ResponseInner](#post%5Fkeyspace%5F%5Fbulk%5Fdocs%5F201%5Fresponse%5Finner)  
[PostKeyspaceBulkDocsRequest](#post%5Fkeyspace%5F%5Fbulk%5Fdocs%5Frequest)  
[PostKeyspaceBulkGetRequest](#post%5Fkeyspace%5F%5Fbulk%5Fget%5Frequest)  
[PostKeyspaceBulkGetRequestDocsInner](#post%5Fkeyspace%5F%5Fbulk%5Fget%5Frequest%5Fdocs%5Finner)  
[PostKeyspaceChangesRequest](#post%5Fkeyspace%5F%5Fchanges%5Frequest)  
[PostKeyspaceRequest](#post%5Fkeyspace%5F%5Frequest)  
[PostKeyspaceRequestAttachmentsValue](#post%5Fkeyspace%5F%5Frequest%5F%5Fattachments%5Fvalue)  
[PostKeyspaceRequestRevisions](#post%5Fkeyspace%5F%5Frequest%5F%5Frevisions)  
[PostKeyspaceRevsDiff200Response](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse)  
[PostKeyspaceRevsDiff200ResponseDocid](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse%5Fdocid)  
[PostKeyspaceRevsDiffRequest](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5Frequest)  
[PutKeyspaceLocalDocidRequest](#put%5Fkeyspace%5F%5Flocal%5Fdocid%5Frequest)  
[User Session Information](#User%5FSession%5FInformation)  
[UserSessionInformationUserCtx](#User%5FSession%5FInformation%5FuserCtx)

### [](#Changes-feed)ChangesFeed

 Object

| Property                 |                                  | Schema                                                                                                            |
| ------------------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **results** _optional_   | **Unique items:** true           | [GetKeyspaceChanges200ResponseResultsInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner)array |
| **last\_seq** _optional_ | The last change sequence number. | String                                                                                                            |

### [](#Design-doc)DesignDoc

 Object

| Property                |  | Schema                                                                                       |
| ----------------------- |  | -------------------------------------------------------------------------------------------- |
| **language** _optional_ |  | String                                                                                       |
| **views** _optional_    |  | [Map](#Map)                                                                                  |
| **options** _optional_  |  | [GetDbDesignDdoc200ResponseOptions](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Foptions) |

### [](#Document)Document

 Object

| Property                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Schema                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **\_id** _optional_          | The ID of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String                                                                       |
| **\_rev** _optional_         | The revision of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | String                                                                       |
| **\_exp** _optional_         | Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document. The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2022 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiry values are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc}  when show\_exp=true is included in the query. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. | String                                                                       |
| **\_deleted** _optional_     | Whether the document is a tombstone or not. If true, it is a tombstone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Boolean                                                                      |
| **\_revisions** _optional_   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [PostKeyspaceRequestRevisions](#post%5Fkeyspace%5F%5Frequest%5F%5Frevisions) |
| **\_attachments** _optional_ |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Map](#Map)                                                                  |
| _additionalproperty_         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Any Type                                                                     |

### [](#get%5F%5F%5F200%5Fresponse)Get200Response

 Object

| Property                          |                                                                                                                                                                     | Schema                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **ADMIN** _optional_              | true if the request is from the Admin API - otherwise omitted.                                                                                                      | Boolean                                                      |
| **couchdb** _required_            | CouchDB welcome                                                                                                                                                     | String                                                       |
| **vendor** _required_             | Product vendor                                                                                                                                                      | [Get200ResponseVendor](#get%5F%5F%5F200%5Fresponse%5Fvendor) |
| **version** _optional_            | Product version, including the build number and edition (i.e. EE or CE) Omitted if api.hide\_product\_version=true                                                  | String                                                       |
| **persistent\_config** _optional_ | Indication for whether sync gateway is running in persistent config mode or legacy config mode. true if the sync gateway node is running in persistent config mode. | Boolean                                                      |

### [](#get%5F%5F%5F200%5Fresponse%5Fvendor)Get200ResponseVendor

 Object

| Property               |                                                         | Schema |
| ---------------------- | ------------------------------------------------------- | ------ |
| **name** _required_    | Product name                                            | String |
| **version** _optional_ | API version. Omitted if api.hide\_product\_version=true | String |

### [](#get%5Fdb%5F%5F200%5Fresponse)GetDb200Response

 Object

| Property                              |                                                                                                                    | Schema      |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| **db\_name** _optional_               | Database name                                                                                                      | String      |
| **update\_seq** _optional_            | The last sequence number that was committed to the database. Will return 0 if the database is offline.             | Integer     |
| **committed\_update\_seq** _optional_ | The last sequence number that was committed to the database. Will return 0 if the database is offline.             | Integer     |
| **instance\_start\_time** _optional_  | Timestamp of when the database opened, in microseconds since the Unix epoch.                                       | Integer     |
| **compact\_running** _optional_       | Indicates whether database compaction is currently taking place or not.                                            | Boolean     |
| **purge\_seq** _optional_             | Unused field.                                                                                                      | Big Decimal |
| **disk\_format\_version** _optional_  | Unused field.                                                                                                      | Big Decimal |
| **state** _optional_                  | The database state. Change using the /{db}/\_offline and /{db}/\_online endpoints. **Values:** "Online", "Offline" | String      |
| **server\_uuid** _optional_           | Unique server identifier.                                                                                          | String      |

### [](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse)GetDbDesignDdoc200Response

 Object

| Property                |  | Schema                                                                                       |
| ----------------------- |  | -------------------------------------------------------------------------------------------- |
| **language** _optional_ |  | String                                                                                       |
| **views** _optional_    |  | [Map](#Map)                                                                                  |
| **options** _optional_  |  | [GetDbDesignDdoc200ResponseOptions](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Foptions) |

### [](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Foptions)GetDbDesignDdoc200ResponseOptions

 Object

| Property                                       |  | Schema |
| ---------------------------------------------- |  | ------ |
| **local\_seq** _optional_                      |  | String |
| **include\_design** _optional_                 |  | String |
| **raw** _optional_                             |  | String |
| **index\_xattr\_on\_deleted\_docs** _optional_ |  | String |

### [](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Fviews%5Fvalue)GetDbDesignDdoc200ResponseViewsValue

 Object

| Property              |  | Schema |
| --------------------- |  | ------ |
| **map** _optional_    |  | String |
| **reduce** _optional_ |  | String |

### [](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse)GetDbDesignDdocViewView200Response

 Object

| Property                   |  | Schema                                                                                                                                |
| -------------------------- |  | ------------------------------------------------------------------------------------------------------------------------------------- |
| **total\_rows** _required_ |  | Integer                                                                                                                               |
| **rows** _required_        |  | [GetDbDesignDdocViewView200ResponseRowsInner](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse%5Frows%5Finner)array     |
| **errors** _optional_      |  | [GetDbDesignDdocViewView200ResponseErrorsInner](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse%5Ferrors%5Finner)array |

### [](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse%5Ferrors%5Finner)GetDbDesignDdocViewView200ResponseErrorsInner

 Object

| Property              |  | Schema |
| --------------------- |  | ------ |
| **From** _optional_   |  | String |
| **Reason** _optional_ |  | String |

### [](#get%5Fdb%5F%5Fdesign%5Fddoc%5F%5Fview%5Fview%5F200%5Fresponse%5Frows%5Finner)GetDbDesignDdocViewView200ResponseRowsInner

 Object

| Property             |  | Schema |
| -------------------- |  | ------ |
| **id** _optional_    |  | String |
| **key** _optional_   |  | Object |
| **value** _optional_ |  | Object |
| **doc** _optional_   |  | Object |

### [](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse)GetDbOidcTestingCerts200Response

 Object

| Property            |  | Schema                                                                                                                  |
| ------------------- |  | ----------------------------------------------------------------------------------------------------------------------- |
| **keys** _required_ |  | [GetDbOidcTestingCerts200ResponseKeysInner](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse%5Fkeys%5Finner)array |

### [](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse%5Fkeys%5Finner)GetDbOidcTestingCerts200ResponseKeysInner

 Object

| Property                    |  | Schema       |
| --------------------------- |  | ------------ |
| **Key** _required_          |  | Object       |
| **KeyID** _required_        |  | String       |
| **Use** _required_          |  | String       |
| **Certificates** _optional_ |  | Object array |
| **Algorithm** _optional_    |  | String       |

### [](#get%5Fdb%5F%5Foidc%5Ftesting%5F%5Fwell%5Fknown%5Fopenid%5Fconfiguration%5F200%5Fresponse)GetDbOidcTestingWellKnownOpenidConfiguration200Response

 Object

| Property                                                  |  | Schema |
| --------------------------------------------------------- |  | ------ |
| **issuer** _optional_                                     |  | String |
| **authorization\_endpoint** _optional_                    |  | String |
| **token\_endpoint** _optional_                            |  | String |
| **jwks\_uri** _optional_                                  |  | String |
| **userinfo\_endpoint** _optional_                         |  | String |
| **id\_token\_signing\_alg\_values\_supported** _optional_ |  | String |
| **response\_types\_supported** _optional_                 |  | String |
| **subject\_types\_supported** _optional_                  |  | String |
| **scopes\_supported** _optional_                          |  | String |
| **claims\_supported** _optional_                          |  | String |
| **token\_endpoint\_auth\_methods\_supported** _optional_  |  | String |

### [](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse)GetKeyspaceAllDocs200Response

 Object

| Property                   |                        | Schema                                                                                                         |
| -------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| **rows** _required_        | **Unique items:** true | [GetKeyspaceAllDocs200ResponseRowsInner](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner)array |
| **total\_rows** _required_ |                        | Big Decimal                                                                                                    |
| **update\_seq** _required_ |                        | Big Decimal                                                                                                    |

### [](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner)GetKeyspaceAllDocs200ResponseRowsInner

 Object

| Property             |  | Schema                                                                                                                 |
| -------------------- |  | ---------------------------------------------------------------------------------------------------------------------- |
| **key** _optional_   |  | String                                                                                                                 |
| **id** _optional_    |  | String                                                                                                                 |
| **value** _optional_ |  | [GetKeyspaceAllDocs200ResponseRowsInnerValue](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner%5Fvalue) |

### [](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner%5Fvalue)GetKeyspaceAllDocs200ResponseRowsInnerValue

 Object

| Property           |  | Schema |
| ------------------ |  | ------ |
| **rev** _optional_ |  | String |

### [](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse)GetKeyspaceChanges200Response

 Object

| Property                 |                                  | Schema                                                                                                            |
| ------------------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **results** _optional_   | **Unique items:** true           | [GetKeyspaceChanges200ResponseResultsInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner)array |
| **last\_seq** _optional_ | The last change sequence number. | String                                                                                                            |

### [](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner)GetKeyspaceChanges200ResponseResultsInner

 Object

| Property               |                                                                                           | Schema                                                                                                                                          |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **seq** _optional_     | The change sequence number.                                                               | Big Decimal                                                                                                                                     |
| **id** _optional_      | The document ID the change happened on.                                                   | String                                                                                                                                          |
| **changes** _optional_ | List of document leafs with each leaf containing only a rev field. **Unique items:** true | [GetKeyspaceChanges200ResponseResultsInnerChangesInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner%5Fchanges%5Finner)array |

### [](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner%5Fchanges%5Finner)GetKeyspaceChanges200ResponseResultsInnerChangesInner

 Object

| Property           |                                                  | Schema |
| ------------------ | ------------------------------------------------ | ------ |
| **rev** _optional_ | The new revision that was caused by that change. | String |

### [](#get%5Fkeyspace%5Fdocid%5F200%5Fresponse)GetKeyspaceDocid200Response

 Object

| Property             |                                  | Schema   |
| -------------------- | -------------------------------- | -------- |
| **\_id** _optional_  | The ID of the document.          | String   |
| **\_rev** _optional_ | The revision ID of the document. | String   |
| _additionalproperty_ |                                  | Any Type |

### [](#HTTP%5FError)HTTP-Error

 Object

| Property              |                        | Schema |
| --------------------- | ---------------------- | ------ |
| **error** _required_  | The error name.        | String |
| **reason** _required_ | The error description. | String |

### [](#New%5Frevision)New-revision

 Object

| Property           |                                             | Schema  |
| ------------------ | ------------------------------------------- | ------- |
| **id** _required_  | The ID of the document.                     | String  |
| **ok** _required_  | Whether the request completed successfully. | Boolean |
| **rev** _required_ | The revision of the document.               | String  |

### [](#NodeInfo)NodeInfo

 Object

| Property                          |                                                                                                                                                                     | Schema                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **ADMIN** _optional_              | true if the request is from the Admin API - otherwise omitted.                                                                                                      | Boolean                                                      |
| **couchdb** _required_            | CouchDB welcome                                                                                                                                                     | String                                                       |
| **vendor** _required_             | Product vendor                                                                                                                                                      | [Get200ResponseVendor](#get%5F%5F%5F200%5Fresponse%5Fvendor) |
| **version** _optional_            | Product version, including the build number and edition (i.e. EE or CE) Omitted if api.hide\_product\_version=true                                                  | String                                                       |
| **persistent\_config** _optional_ | Indication for whether sync gateway is running in persistent config mode or legacy config mode. true if the sync gateway node is running in persistent config mode. | Boolean                                                      |

### [](#OIDC-callback)OpenID Connect callback properties

 Object

| Property                      |                                             | Schema      |
| ----------------------------- | ------------------------------------------- | ----------- |
| **id\_token** _optional_      | The OpenID Connect ID token                 | String      |
| **refresh\_token** _optional_ | The OpenID Connect ID refresh token         | String      |
| **session\_id** _optional_    | The Sync Gateway session token              | String      |
| **name** _optional_           | The Sync Gateway user                       | String      |
| **access\_token** _optional_  | The OpenID Connect access token             | String      |
| **token\_type** _optional_    | The OpenID Connect ID token type            | String      |
| **expires\_in** _optional_    | The time until the id\_token expires (TTL). | Big Decimal |

### [](#OIDC-login-page-handler)OIDCLoginPageHandler

 Object

| Property                              |  | Schema |
| ------------------------------------- |  | ------ |
| **username** _required_               |  | String |
| **tokenttl** _required_               |  | String |
| **identity-token-formats** _required_ |  | String |
| **authenticated** _required_          |  | String |

### [](#OIDC%5Ftoken)OIDC-token

 Object

| Property                      |  | Schema |
| ----------------------------- |  | ------ |
| **access\_token** _optional_  |  | String |
| **token\_type** _optional_    |  | String |
| **refresh\_token** _optional_ |  | String |
| **expires\_in** _optional_    |  | String |
| **id\_token** _optional_      |  | String |

### [](#OpenID%5FConnect%5Fcallback%5Fproperties)OpenID Connect callback properties

 Object

| Property                      |                                             | Schema      |
| ----------------------------- | ------------------------------------------- | ----------- |
| **id\_token** _optional_      | The OpenID Connect ID token                 | String      |
| **refresh\_token** _optional_ | The OpenID Connect ID refresh token         | String      |
| **session\_id** _optional_    | The Sync Gateway session token              | String      |
| **name** _optional_           | The Sync Gateway user                       | String      |
| **access\_token** _optional_  | The OpenID Connect access token             | String      |
| **token\_type** _optional_    | The OpenID Connect ID token type            | String      |
| **expires\_in** _optional_    | The time until the id\_token expires (TTL). | Big Decimal |

### [](#post%5Fdb%5F%5Fensure%5Ffull%5Fcommit%5F201%5Fresponse)PostDbEnsureFullCommit201Response

 Object

| Property                             |                                                                              | Schema  |
| ------------------------------------ | ---------------------------------------------------------------------------- | ------- |
| **instance\_start\_time** _optional_ | Timestamp of when the database opened, in microseconds since the Unix epoch. | Integer |
| **ok** _optional_                    |                                                                              | Boolean |

### [](#post%5Fdb%5F%5Ffacebook%5F401%5Fresponse)PostDbFacebook401Response

 Object

| Property              |  | Schema |
| --------------------- |  | ------ |
| **error** _optional_  |  | String |
| **reason** _optional_ |  | String |

### [](#post%5Fdb%5F%5Ffacebook%5Frequest)PostDbFacebookRequest

 Object

| Property                     |                                                   | Schema |
| ---------------------------- | ------------------------------------------------- | ------ |
| **access\_token** _required_ | Facebook access token to base the new session on. | String |

### [](#post%5Fdb%5F%5Fgoogle%5Frequest)PostDbGoogleRequest

 Object

| Property                 |                                             | Schema |
| ------------------------ | ------------------------------------------- | ------ |
| **id\_token** _required_ | Google ID token to base the new session on. | String |

### [](#post%5Fdb%5F%5Foidc%5Ftesting%5Fauthenticate%5Frequest)PostDbOidcTestingAuthenticateRequest

 Object

| Property                              |  | Schema |
| ------------------------------------- |  | ------ |
| **username** _required_               |  | String |
| **tokenttl** _required_               |  | String |
| **identity-token-formats** _required_ |  | String |
| **authenticated** _required_          |  | String |

### [](#post%5Fdb%5F%5Foidc%5Ftesting%5Ftoken%5Frequest)PostDbOidcTestingTokenRequest

 Object

| Property                      |                                                                                                 | Schema |
| ----------------------------- | ----------------------------------------------------------------------------------------------- | ------ |
| **grant\_type** _required_    | The grant type of the token to request. Can either be an authorization\_code or refresh\_token. | String |
| **code** _optional_           | **grant\_type=authorization\_code only**: The OpenID Connect authentication token.              | String |
| **refresh\_token** _optional_ | **grant\_type=refresh\_token only**: The OpenID Connect refresh token.                          | String |

### [](#post%5Fdb%5F%5Fsession%5F200%5Fresponse)PostDbSession200Response

 Object

| Property                                |                                                                                                     | Schema                                                                                |
| --------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **authentication\_handlers** _required_ | Used for CouchDB compatability. Always contains "default" and "cookie". **Values:** default, cookie | String array                                                                          |
| **ok** _required_                       | Used for CouchDB compatability. Always true.                                                        | Boolean                                                                               |
| **userCtx** _required_                  |                                                                                                     | [PostDbSession200ResponseUserCtx](#post%5Fdb%5F%5Fsession%5F200%5Fresponse%5FuserCtx) |

### [](#post%5Fdb%5F%5Fsession%5F200%5Fresponse%5FuserCtx)PostDbSession200ResponseUserCtx

 Object

| Property                |                                                                                                  | Schema      |
| ----------------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| **channels** _required_ | A map of the channels the user is in along with the sequence number the user was granted access. | [Map](#Map) |
| **name** _required_     | The name of the user. **Minimum length:** 1                                                      | String      |

### [](#post%5Fdb%5F%5Fsession%5F200%5Fresponse%5FuserCtx%5Fchannels%5Fvalue)PostDbSession200ResponseUserCtxChannelsValue

 Composite Schema

One of the following:

* Big Decimal
* String

### [](#post%5Fdb%5F%5Fsession%5Frequest)PostDbSessionRequest

 Object

| Property                |                                                   | Schema |
| ----------------------- | ------------------------------------------------- | ------ |
| **name** _optional_     | User name to generate the session for.            | String |
| **password** _optional_ | Password of the user to generate the session for. | String |

### [](#post%5Fkeyspace%5F%5Fall%5Fdocs%5Frequest)PostKeyspaceAllDocsRequest

 Object

| Property            |                                    | Schema       |
| ------------------- | ---------------------------------- | ------------ |
| **keys** _required_ | List of the documents to retrieve. | String array |

### [](#post%5Fkeyspace%5F%5Fbulk%5Fdocs%5F201%5Fresponse%5Finner)PostKeyspaceBulkDocs201ResponseInner

 Object

| Property              |                                                                  | Schema  |
| --------------------- | ---------------------------------------------------------------- | ------- |
| **id** _required_     | The ID of the document that the operation was performed on.      | String  |
| **rev** _optional_    | The new revision of the document if the operation was a success. | String  |
| **error** _optional_  | The error type if the operation of the document failed.          | String  |
| **reason** _optional_ | The reason the operation failed.                                 | String  |
| **status** _optional_ | The HTTP status code for why the operation failed.               | Integer |

### [](#post%5Fkeyspace%5F%5Fbulk%5Fdocs%5Frequest)PostKeyspaceBulkDocsRequest

 Object

| Property                  |                                                                                                                | Schema                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **new\_edits** _optional_ | This controls whether to assign new revision identifiers to new edits (true) or use the existing ones (false). | Boolean                                                   |
| **docs** _required_       |                                                                                                                | [PostKeyspaceRequest](#post%5Fkeyspace%5F%5Frequest)array |

### [](#post%5Fkeyspace%5F%5Fbulk%5Fget%5Frequest)PostKeyspaceBulkGetRequest

 Object

| Property            |  | Schema                                                                                                |
| ------------------- |  | ----------------------------------------------------------------------------------------------------- |
| **docs** _required_ |  | [PostKeyspaceBulkGetRequestDocsInner](#post%5Fkeyspace%5F%5Fbulk%5Fget%5Frequest%5Fdocs%5Finner)array |

### [](#post%5Fkeyspace%5F%5Fbulk%5Fget%5Frequest%5Fdocs%5Finner)PostKeyspaceBulkGetRequestDocsInner

 Object

| Property          |                                 | Schema |
| ----------------- | ------------------------------- | ------ |
| **id** _required_ | ID of the document to retrieve. | String |

### [](#post%5Fkeyspace%5F%5Fchanges%5Frequest)PostKeyspaceChangesRequest

 Object

| Property                     |                                                                                                                                                                                                                                                                                                                                                                                                                            | Schema  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **limit** _optional_         | Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                       | String  |
| **style** _optional_         | Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                                                                | String  |
| **active\_only** _optional_  | Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                              | String  |
| **include\_docs** _optional_ | Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                            | Boolean |
| **revocations** _optional_   | If true, revocation messages will be sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                             | String  |
| **filter** _optional_        | Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                                                                 | String  |
| **channels** _optional_      | A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                        | String  |
| **doc\_ids** _optional_      | A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal.                                                                                                                                                                                                   | String  |
| **heartbeat** _optional_     | The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This will override any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the server replication configuration. | String  |
| **timeout** _optional_       | This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                                               | String  |
| **feed** _optional_          | The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                                                           | String  |

### [](#post%5Fkeyspace%5F%5Frequest)PostKeyspaceRequest

 Object

| Property                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Schema                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **\_id** _optional_          | The ID of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String                                                                       |
| **\_rev** _optional_         | The revision of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | String                                                                       |
| **\_exp** _optional_         | Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document. The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2022 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiry values are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc}  when show\_exp=true is included in the query. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. | String                                                                       |
| **\_deleted** _optional_     | Whether the document is a tombstone or not. If true, it is a tombstone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Boolean                                                                      |
| **\_revisions** _optional_   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [PostKeyspaceRequestRevisions](#post%5Fkeyspace%5F%5Frequest%5F%5Frevisions) |
| **\_attachments** _optional_ |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Map](#Map)                                                                  |
| _additionalproperty_         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Any Type                                                                     |

### [](#post%5Fkeyspace%5F%5Frequest%5F%5Fattachments%5Fvalue)PostKeyspaceRequestAttachmentsValue

 Object

| Property                     |                                       | Schema |
| ---------------------------- | ------------------------------------- | ------ |
| **content\_type** _optional_ | Content type of the attachment.       | String |
| **data** _optional_          | The data in the attachment in base64. | String |

### [](#post%5Fkeyspace%5F%5Frequest%5F%5Frevisions)PostKeyspaceRequestRevisions

 Object

| Property             |                                                               | Schema       |
| -------------------- | ------------------------------------------------------------- | ------------ |
| **start** _optional_ | Prefix number for the latest revision.                        | Big Decimal  |
| **ids** _optional_   | Array of valid revision IDs, in reverse order (latest first). | String array |

### [](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse)PostKeyspaceRevsDiff200Response

 Object

| Property             |                  | Schema                                                                                             |
| -------------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| **docid** _optional_ | The document ID. | [PostKeyspaceRevsDiff200ResponseDocid](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse%5Fdocid) |

### [](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse%5Fdocid)PostKeyspaceRevsDiff200ResponseDocid

 Object

| Property                           |                                                                     | Schema       |
| ---------------------------------- | ------------------------------------------------------------------- | ------------ |
| **missing** _optional_             | The revisions that are not in the database (and therefore missing). | String array |
| **possible\_ancestors** _optional_ | An array of known revisions that might be the recent ancestors.     | String array |

### [](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5Frequest)PostKeyspaceRevsDiffRequest

 Object

| Property             |                                                                       | Schema       |
| -------------------- | --------------------------------------------------------------------- | ------------ |
| **docid** _optional_ | The document ID with an array of revisions to use for the comparison. | String array |

### [](#put%5Fkeyspace%5F%5Flocal%5Fdocid%5Frequest)PutKeyspaceLocalDocidRequest

 Object

| Property             |                                                                    | Schema |
| -------------------- | ------------------------------------------------------------------ | ------ |
| **\_rev** _optional_ | Revision to replace. Required if updating existing local document. | String |

### [](#User%5FSession%5FInformation)User Session Information

 Object

| Property                                |                                                                         | Schema                                                                   |
| --------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **authentication\_handlers** _optional_ | The ways authentication can be established to authenticate as the user. | String array                                                             |
| **ok** _optional_                       |                                                                         | Boolean                                                                  |
| **userCtx** _optional_                  |                                                                         | [UserSessionInformationUserCtx](#User%5FSession%5FInformation%5FuserCtx) |

### [](#User%5FSession%5FInformation%5FuserCtx)UserSessionInformationUserCtx

 Object

| Property                |                                                                                                                                                                     | Schema |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **channels** _optional_ | A map of the channels the user has access to and the sequence number each channel was created at. The key is the channel name and the value is the sequence number. | Object |
| **name** _optional_     | The name of the user.                                                                                                                                               | String |

---

###### 

### [](#related-content)Related Content

[](#-2) 

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

[](#-3) 

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

[](#-4) 

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)