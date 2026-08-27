---
title: Admin REST API (Static Page)
description: Description of the Sync Gateway Admin REST API, alternative
  representation as a static page
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/rest_api_admin_static.adoc
  xref: xref:3.1@sync-gateway::rest_api_admin_static.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/rest_api_admin_static.html)

# Admin REST API (Static Page)

> Description of the Sync Gateway Admin REST API, alternative representation as a static page  

Related _REST API_ topics: [Public REST API (Static Page)](rest%5Fapi%5Fpublic%5Fstatic.md) | [Metrics REST API (Static Page)](rest%5Fapi%5Fmetrics%5Fstatic.md)

## [](#overview)Overview

### Version information

_Version_ : 3.1

### Host information

{protocol}://{hostname}:4985

Admin API

| Component    | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| **protocol** | The protocol to use (HTTP or HTTPS) **Values:** http, https **Example:** http |
| **hostname** | The hostname to use **Example:** localhost                                    |

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Authentication](#tag-Authentication)  
[Database Configuration](#tag-DatabaseConfiguration)  
[Database Management](#tag-DatabaseManagement)  
[Database Security](#tag-DatabaseSecurity)  
[Document](#tag-Document)  
[Metrics](#tag-Metrics)  
[Profiling](#tag-Profiling)  
[Replication](#tag-Replication)  
[Server](#tag-Server)  
[Session](#tag-Session)  
[Unsupported](#tag-Unsupported)

### [](#tag-Authentication)Authentication

Manage authentication

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

### [](#tag-DatabaseConfiguration)Database Configuration

**Table of Contents**

[Delete import filter](#delete%5Fkeyspace-%5Fconfig-import%5Ffilter)  
[Remove custom sync function](#delete%5Fkeyspace-%5Fconfig-sync)  
[Get database configuration](#get%5Fdb-%5Fconfig)  
[Get database import filter](#get%5Fkeyspace-%5Fconfig-import%5Ffilter)  
[Get database sync function](#get%5Fkeyspace-%5Fconfig-sync)  
[Update database configuration](#post%5Fdb-%5Fconfig)  
[Replace database configuration](#put%5Fdb-%5Fconfig)  
[Set database import filter](#put%5Fkeyspace-%5Fconfig-import%5Ffilter)  
[Set database sync function](#put%5Fkeyspace-%5Fconfig-sync)

#### [](#delete%5Fkeyspace-%5Fconfig-import%5Ffilter)Delete import filter

DELETE /{keyspace}/_config/import_filter

##### [](#delete%5Fkeyspace-%5Fconfig-import%5Ffilter-description)Description

This will remove the custom import filter function from the database configuration so that Sync Gateway will not filter any documents during import.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#delete%5Fkeyspace-%5Fconfig-import%5Ffilter-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Header Parameters

| Name                    | Description                                                                                                                                                      | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **If-Match** _optional_ | If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. | String |

##### [](#delete%5Fkeyspace-%5Fconfig-import%5Ffilter-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Successfully deleted the import filter                                                                                                                                                                                                   |                            |
| 404       | Resource could not be found                                                                                                                                                                                                              | [HTTPError](#HTTP%5FError) |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [HTTPError](#HTTP%5FError) |

#### [](#delete%5Fkeyspace-%5Fconfig-sync)Remove custom sync function

DELETE /{keyspace}/_config/sync

##### [](#delete%5Fkeyspace-%5Fconfig-sync-description)Description

This will remove the custom sync function from the database configuration.

The default sync function is equivalent to:

```javascript
function (doc) {
  channel(doc.channels);
}

```

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#delete%5Fkeyspace-%5Fconfig-sync-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Header Parameters

| Name                    | Description                | Schema |
| ----------------------- | -------------------------- | ------ |
| **If-Match** _optional_ | The revision ID to target. | String |

##### [](#delete%5Fkeyspace-%5Fconfig-sync-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Successfully reset the sync function                                                                                                                                                                                                     |                            |
| 404       | Resource could not be found                                                                                                                                                                                                              | [HTTPError](#HTTP%5FError) |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Fconfig)Get database configuration

GET /{db}/_config

##### [](#get%5Fdb-%5Fconfig-description)Description

Retrieve the full configuration for the database specified.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#get%5Fdb-%5Fconfig-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                               | Description                                                                                                               | Schema  |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------- |
| **redact** _optional_              | No longer supported field.                                                                                                | Boolean |
| **include\_javascript** _optional_ | Include the fields that have Javascript functions in the response. E.g. sync function, import filter, and event handlers. | Boolean |
| **include\_runtime** _optional_    | Whether to include the values set at runtime, and default values.                                                         | Boolean |
| **refresh\_config** _optional_     | Forces the configuration to be reloaded on the Sync Gateway node.                                                         | Boolean |

##### [](#get%5Fdb-%5Fconfig-responses)Responses

| HTTP Code | Description                                   | Schema                               |
| --------- | --------------------------------------------- | ------------------------------------ |
| 200       | Successfully retrieved database configuration | [DatabaseConfig](#Database%5Fconfig) |
| 404       | Resource could not be found                   | [HTTPError](#HTTP%5FError)           |

#### [](#get%5Fkeyspace-%5Fconfig-import%5Ffilter)Get database import filter

GET /{keyspace}/_config/import_filter

##### [](#get%5Fkeyspace-%5Fconfig-import%5Ffilter-description)Description

This returns the database's import filter that documents are ran through when importing.

Response will be blank if there has been no import filter set.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/javascript
* application/json

##### [](#get%5Fkeyspace-%5Fconfig-import%5Ffilter-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

##### [](#get%5Fkeyspace-%5Fconfig-import%5Ffilter-responses)Responses

| HTTP Code | Description                              | Schema                     |
| --------- | ---------------------------------------- | -------------------------- |
| 200       | Successfully retrieved the import filter | String                     |
| 404       | Resource could not be found              | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fkeyspace-%5Fconfig-sync)Get database sync function

GET /{keyspace}/_config/sync

##### [](#get%5Fkeyspace-%5Fconfig-sync-description)Description

This returns the database's sync function.

Response will be blank if there has been no sync function set.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/javascript
* application/json

##### [](#get%5Fkeyspace-%5Fconfig-sync-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

##### [](#get%5Fkeyspace-%5Fconfig-sync-responses)Responses

| HTTP Code | Description                              | Schema                     |
| --------- | ---------------------------------------- | -------------------------- |
| 200       | Successfully retrieved the sync function | String                     |
| 404       | Resource could not be found              | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Fconfig)Update database configuration

POST /{db}/_config

##### [](#post%5Fdb-%5Fconfig-description)Description

This is used to update the database configuration fields specified. Only the fields specified in the request will have their values replaced.

The bucket and database name cannot be changed. If these need to be changed, the database will need to be deleted then recreated with the new settings.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Fconfig-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Header Parameters

| Name                    | Description                                                                                                                                                      | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **If-Match** _optional_ | If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. | String |

Body Parameter

| Name                | Description                                 | Schema                            |
| ------------------- | ------------------------------------------- | --------------------------------- |
| **Body** _optional_ | The database configuration fields to update | [DatabaseConfig](#DatabaseConfig) |

##### [](#post%5Fdb-%5Fconfig-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 201       | Database configuration successfully updated                                                                                                                                                                                              |                            |
| 400       | There was a problem with your request                                                                                                                                                                                                    | [HTTPError](#HTTP%5FError) |
| 404       | Not Found                                                                                                                                                                                                                                |                            |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fdb-%5Fconfig)Replace database configuration

PUT /{db}/_config

##### [](#put%5Fdb-%5Fconfig-description)Description

Replaces the database configuration with the one sent in the request.

The bucket and database name cannot be changed. If these need to be changed, the database will need to be deleted then recreated with the new settings.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fdb-%5Fconfig-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                                     | Description                                                                                 | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| **disable\_oidc\_validation** _optional_ | If set, will not attempt to validate the configured OpenID Connect providers are reachable. | Boolean |

Header Parameters

| Name                    | Description                                                                                                                                                      | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **If-Match** _optional_ | If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. | String |

Body Parameter

| Name                | Description                           | Schema                            |
| ------------------- | ------------------------------------- | --------------------------------- |
| **Body** _optional_ | The new database configuration to use | [DatabaseConfig](#DatabaseConfig) |

##### [](#put%5Fdb-%5Fconfig-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 201       | Database configuration successfully updated                                                                                                                                                                                              |                            |
| 400       | There was a problem with your request                                                                                                                                                                                                    | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                                                                                                                                                                                                              | [HTTPError](#HTTP%5FError) |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter)Set database import filter

PUT /{keyspace}/_config/import_filter

##### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-description)Description

This will allow you to update the database's import filter.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Consumes

* application/javascript

Produces

* application/json

##### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                                     | Description                                                                                 | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| **disable\_oidc\_validation** _optional_ | If set, will not attempt to validate the configured OpenID Connect providers are reachable. | Boolean |

Header Parameters

| Name                    | Description                                                                                                                                                      | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **If-Match** _optional_ | If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. | String |

Body Parameter

| Name                | Description              | Schema |
| ------------------- | ------------------------ | ------ |
| **Body** _optional_ | The import filter to use | String |

##### [](#put%5Fkeyspace-%5Fconfig-import%5Ffilter-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Updated import filter successfully                                                                                                                                                                                                       |                            |
| 400       | There was a problem with your request                                                                                                                                                                                                    | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                                                                                                                                                                                                              | [HTTPError](#HTTP%5FError) |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fkeyspace-%5Fconfig-sync)Set database sync function

PUT /{keyspace}/_config/sync

##### [](#put%5Fkeyspace-%5Fconfig-sync-description)Description

This will allow you to update the sync function.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Consumes

* application/javascript

Produces

* application/json

##### [](#put%5Fkeyspace-%5Fconfig-sync-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Query Parameters

| Name                                     | Description                                                                                 | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| **disable\_oidc\_validation** _optional_ | If set, will not attempt to validate the configured OpenID Connect providers are reachable. | Boolean |

Header Parameters

| Name                    | Description                                                                                                                                                      | Schema |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **If-Match** _optional_ | If set to a configuration's Etag value, enables optimistic concurrency control for the request. Returns HTTP 412 if another update happened underneath this one. | String |

Body Parameter

| Name                | Description                  | Schema |
| ------------------- | ---------------------------- | ------ |
| **Body** _optional_ | The new sync function to use | String |

##### [](#put%5Fkeyspace-%5Fconfig-sync-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                              | Schema                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Updated sync function successfully                                                                                                                                                                                                       |                            |
| 400       | There was a problem with your request                                                                                                                                                                                                    | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                                                                                                                                                                                                              | [HTTPError](#HTTP%5FError) |
| 412       | Precondition Failed The supplied If-Match header did not match the current version of the configuration. Returned when optimistic concurrency control is used, and there has been an update to the configuration in between this update. | [HTTPError](#HTTP%5FError) |

### [](#tag-DatabaseManagement)Database Management

**Table of Contents**

[Remove a database](#delete%5Fdb-)  
[Get a list of all the databases](#get%5F%5Fall%5Fdbs)  
[Get database information](#get%5Fdb-)  
[Get the status of the most recent compact operation](#get%5Fdb-%5Fcompact)  
[Get resync status](#get%5Fdb-%5Fresync)  
[Get changes list](#get%5Fkeyspace-%5Fchanges)  
[Check if database exists](#head%5Fdb-)  
[/{db}/\_changes](#head%5Fkeyspace-%5Fchanges)  
[Manage a compact operation](#post%5Fdb-%5Fcompact)  
[/{db}/\_ensure\_full\_commit](#post%5Fdb-%5Fensure%5Ffull%5Fcommit)  
[Take the database offline](#post%5Fdb-%5Foffline)  
[Bring the database online](#post%5Fdb-%5Fonline)  
[Start or stop Resync](#post%5Fdb-%5Fresync)  
[Get changes list](#post%5Fkeyspace-%5Fchanges)  
[Compare revisions to what is in the database](#post%5Fkeyspace-%5Frevs%5Fdiff)  
[Create a new Sync Gateway database](#put%5Fdb-)

#### [](#delete%5Fdb-)Remove a database

DELETE /{db}/

##### [](#delete%5Fdb--description)Description

Removes a database from the Sync Gateway cluster

**Note:** If running in legacy mode, this will only delete the database from the current node.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#delete%5Fdb--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#delete%5Fdb--responses)Responses

| HTTP Code | Description                        | Schema                     |
| --------- | ---------------------------------- | -------------------------- |
| 200       | Successfully removed the database  | Object                     |
| 404       | Resource could not be found        | [HTTPError](#HTTP%5FError) |
| 500       | Cannot remove database from bucket | [HTTPError](#HTTP%5FError) |

#### [](#get%5F%5Fall%5Fdbs)Get a list of all the databases

GET /_all_dbs

##### [](#get%5F%5Fall%5Fdbs-description)Description

This retrieves all the databases that are in the current Sync Gateway node. If verbose, returns bucket and state information for each database, otherwise returns names only.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#get%5F%5Fall%5Fdbs-parameters)Parameters

Query Parameters

| Name                   | Description | Schema  |
| ---------------------- | ----------- | ------- |
| **verbose** _optional_ |             | Boolean |

##### [](#get%5F%5Fall%5Fdbs-responses)Responses

| HTTP Code | Description                               | Schema                                                       |
| --------- | ----------------------------------------- | ------------------------------------------------------------ |
| 200       | Successfully retrieved all database names | [GetAllDbs200Response](#get%5F%5Fall%5Fdbs%5F200%5Fresponse) |

#### [](#get%5Fdb-)Get database information

GET /{db}/

##### [](#get%5Fdb--description)Description

Retrieve information about the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

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

#### [](#get%5Fdb-%5Fcompact)Get the status of the most recent compact operation

GET /{db}/_compact

##### [](#get%5Fdb-%5Fcompact-description)Description

This will retrieve the current status of the most recent compact operation.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#get%5Fdb-%5Fcompact-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                | Description                                                                                                                                                                                                                 | Schema |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **type** _optional_ | This is the type of compaction to use. The type must be either: attachment for cleaning up legacy (pre-3.0) attachments tombstone for purging the JSON bodies of non-leaf revisions.' **Values:** "attachment", "tombstone" | String |

##### [](#get%5Fdb-%5Fcompact-responses)Responses

| HTTP Code | Description                              | Schema                             |
| --------- | ---------------------------------------- | ---------------------------------- |
| 200       | Compaction status retrieved successfully | [CompactStatus](#Compact%5Fstatus) |
| 400       | There was a problem with your request    | [HTTPError](#HTTP%5FError)         |
| 404       | Resource could not be found              | [HTTPError](#HTTP%5FError)         |

#### [](#get%5Fdb-%5Fresync)Get resync status

GET /{db}/_resync

##### [](#get%5Fdb-%5Fresync-description)Description

This will retrieve the status of last resync operation (whether it is running or not) in the Sync Gateway cluster.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#get%5Fdb-%5Fresync-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#get%5Fdb-%5Fresync-responses)Responses

| HTTP Code | Description                                                    | Schema                           |
| --------- | -------------------------------------------------------------- | -------------------------------- |
| 200       | successfully retrieved the most recent resync operation status | [ResyncStatus](#Resync%5Fstatus) |
| 404       | Resource could not be found                                    | [HTTPError](#HTTP%5FError)       |

#### [](#get%5Fkeyspace-%5Fchanges)Get changes list

GET /{keyspace}/_changes

##### [](#get%5Fkeyspace-%5Fchanges-description)Description

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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
| **request\_plus** _optional_ | When true, ensures all valid documents written prior to the request being issued are included in the response. This is only applicable for non-continuous feeds.                                                                                                                                                                                                                                                                              | Boolean      |

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

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#post%5Fdb-%5Fcompact)Manage a compact operation

POST /{db}/_compact

##### [](#post%5Fdb-%5Fcompact-description)Description

This allows a new compact operation to be done on the database, or to stop an existing running compact operation.

The type of compaction that is done depends on what the `type` query parameter is set to. The 2 options will:

* `tombstone` \- purge the JSON bodies of non-leaf revisions. This is known as database compaction. Database compaction is done periodically automatically by the system. JSON bodies of leaf nodes (conflicting branches) are not removed therefore it is important to resolve conflicts in order to re-claim disk space.
* `attachment` \- purge all unlinked/unused legacy (pre 3.0) attachments. If the previous attachment compact operation failed, this will attempt to restart the `compact_id` at the appropriate phase (if possible).

Both types can each have a maximum of 1 compact operation running at any one point. This means that an attachment compaction can be running at the same time as a tombstone compaction but not 2 tombstone compactions.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#post%5Fdb-%5Fcompact-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                    | Description                                                                                                                                                                                                                 | Schema  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **type** _optional_     | This is the type of compaction to use. The type must be either: attachment for cleaning up legacy (pre-3.0) attachments tombstone for purging the JSON bodies of non-leaf revisions.' **Values:** "attachment", "tombstone" | String  |
| **action** _optional_   | Defines whether the a compact operation is being started or stopped. **Values:** "start", "stop"                                                                                                                            | String  |
| **reset** _optional_    | **Attachment compaction only** This forces a fresh compact start instead of trying to resume the previous failed compact operation.                                                                                         | Boolean |
| **dry\_run** _optional_ | **Attachment compaction only** This will run through all 3 stages of attachment compact but will not purge any attachments. This can be used to check how many attachments will be purged.'                                 | Boolean |

##### [](#post%5Fdb-%5Fcompact-responses)Responses

| HTTP Code | Description                                                                | Schema                     |
| --------- | -------------------------------------------------------------------------- | -------------------------- |
| 200       | Started or stopped compact operation successfully                          |                            |
| 400       | There was a problem with your request                                      | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                                                | [HTTPError](#HTTP%5FError) |
| 503       | Cannot start compaction due to another compaction operation still running. | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Fensure%5Ffull%5Fcommit)/{db}/\_ensure\_full\_commit

POST /{db}/_ensure_full_commit

##### [](#post%5Fdb-%5Fensure%5Ffull%5Fcommit-description)Description

This endpoint is non-functional but is present for CouchDB compatibility.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#post%5Fdb-%5Foffline)Take the database offline

POST /{db}/_offline

##### [](#post%5Fdb-%5Foffline-description)Description

This will take the database offline meaning actions can be taken without disrupting current operations ungracefully or having the restart the Sync Gateway instance.

This will not take the backing Couchbase Server bucket offline.

Taking a database offline that is in the progress of coming online will take the database offline after it comes online.

Taking the database offline will:

* Close all active `_changes` feeds for the database.
* Reject all access to the database via the Public REST API (returning a 503 Service Unavailable code).
* Reject most Admin API requests (by returning a 503 Service Unavailable code). The only endpoints to be available are: the resync endpoints, the configuration endpoints, `DELETE, GET, HEAD /{db}/`, `POST /{db}/_offline`, and `POST /{db}/_online`.
* Stops webhook event handlers.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Produces

* application/json

##### [](#post%5Fdb-%5Foffline-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#post%5Fdb-%5Foffline-responses)Responses

| HTTP Code | Description                                                 | Schema                     |
| --------- | ----------------------------------------------------------- | -------------------------- |
| 200       | Database has been taken offline successfully                |                            |
| 404       | Resource could not be found                                 | [HTTPError](#HTTP%5FError) |
| 503       | An error occurred while trying to take the database offline | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Fonline)Bring the database online

POST /{db}/_online

##### [](#post%5Fdb-%5Fonline-description)Description

This will bring the database online so the Public and full Admin REST API requests can be served.

Bringing a database online will:

* Close the database connection to the backing Couchbase Server bucket.
* Reload the database configuration, and connect to the backing Couchbase Server bucket.
* Re-establish access to the database from the Public REST API and accept all Admin API requests.

A specific delay before bringing the database online may be wanted to:

* Make the database available for Couchbase Lite clients at a specific time.
* Make the databases on several Sync Gateway instances available at the same time.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Fonline-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description                                                       | Schema                                      |
| ------------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| **Body** _optional_ | Add an optional delay to wait before bringing the database online | [PostDbOnlineRequest](#PostDbOnlineRequest) |

##### [](#post%5Fdb-%5Fonline-responses)Responses

| HTTP Code | Description                                                             | Schema                     |
| --------- | ----------------------------------------------------------------------- | -------------------------- |
| 200       | Database will be brought online immediately or with the specified delay |                            |
| 404       | Resource could not be found                                             | [HTTPError](#HTTP%5FError) |
| 503       | An error occurred                                                       | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Fresync)Start or stop Resync

POST /{db}/_resync

##### [](#post%5Fdb-%5Fresync-description)Description

This can be used to start or stop a resync operation. A resync operation will cause all documents in the keyspace to be reprocessed through the sync function.

Generally, a resync operation might be wanted when the sync function has been modified in such a way that the channel or access mappings for any existing documents would change as a result.

A resync operation cannot be run if the database is online. The database can be taken offline by calling the `POST /{db}/_offline` endpoint.

In a multi-node cluster, the resync operation _must_ be run on only a single node. Therefore, users should bring other nodes offline before initiating this action. Undefined system behaviour will happen if running resync on more than 1 node.

The `requireUser()` and `requireRole()` calls in the sync function will always return `true`.

* **action=start** \- This is an asynchronous operation, and will start resync in the background.
* **action=stop** \- This will stop the currently running resync operation.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Fresync-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                                 | Description                                                                                                                                                                                                                                                      | Schema  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **action** _optional_                | This is whether to start a new resync job or stop an existing one. **Values:** "start", "stop"                                                                                                                                                                   | String  |
| **regenerate\_sequences** _optional_ | **Use this only when requested to do so by the Couchbase support team** This request will regenerate the sequence numbers for each document processed. If scopes parameter is specified, the principal sequence documents will not have their sequences updated. | Boolean |
| **reset** _optional_                 | This forces a fresh resync run instead of trying to resume the previous resync operation                                                                                                                                                                         | Boolean |

Body Parameter

| Name                | Description | Schema                                      |
| ------------------- | ----------- | ------------------------------------------- |
| **Body** _optional_ |             | [PostDbResyncRequest](#PostDbResyncRequest) |

##### [](#post%5Fdb-%5Fresync-responses)Responses

| HTTP Code | Description                                             | Schema                           |
| --------- | ------------------------------------------------------- | -------------------------------- |
| 200       | successfully changed the status of the resync operation | [ResyncStatus](#Resync%5Fstatus) |
| 503       | Service Unavailable                                     | [HTTPError](#HTTP%5FError)       |

#### [](#post%5Fkeyspace-%5Fchanges)Get changes list

POST /{keyspace}/_changes

##### [](#post%5Fkeyspace-%5Fchanges-description)Description

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

#### [](#put%5Fdb-)Create a new Sync Gateway database

PUT /{db}/

##### [](#put%5Fdb--description)Description

This is to create a new database for Sync Gateway.

The new database name will be the name specified in the URL, not what is specified in the request body database configuration.

If the bucket is not provided in the database configuration, Sync Gateway will attempt to find and use the database name as the bucket.

By default, the new database will be brought online immediately. This can be avoided by including `"offline": true` in the configuration in the request body.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fdb--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                                     | Description                                                                                 | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ------- |
| **disable\_oidc\_validation** _optional_ | If set, will not attempt to validate the configured OpenID Connect providers are reachable. | Boolean |

Body Parameter

| Name                | Description                                   | Schema                            |
| ------------------- | --------------------------------------------- | --------------------------------- |
| **Body** _optional_ | The configuration to use for the new database | [DatabaseConfig](#DatabaseConfig) |

##### [](#put%5Fdb--responses)Responses

| HTTP Code | Description                               | Schema                     |
| --------- | ----------------------------------------- | -------------------------- |
| 201       | Database created successfully             |                            |
| 400       | There was a problem with your request     | [HTTPError](#HTTP%5FError) |
| 403       | An authentication failure occurred        | [HTTPError](#HTTP%5FError) |
| 409       | A database already exists for this bucket | [HTTPError](#HTTP%5FError) |
| 412       | A database under that name already exists | [HTTPError](#HTTP%5FError) |
| 500       | A server error occurred                   | [HTTPError](#HTTP%5FError) |

### [](#tag-DatabaseSecurity)Database Security

**Table of Contents**

[Delete a role](#delete%5Fdb-%5Frole-name)  
[Delete a user](#delete%5Fdb-%5Fuser-name)  
[Get all names of the roles](#get%5Fdb-%5Frole-)  
[Get a role](#get%5Fdb-%5Frole-name)  
[Get all the names of the users](#get%5Fdb-%5Fuser-)  
[Get a user](#get%5Fdb-%5Fuser-name)  
[/{db}/\_role/](#head%5Fdb-%5Frole-)  
[Check if role exists](#head%5Fdb-%5Frole-name)  
[/{db}/\_user/](#head%5Fdb-%5Fuser-)  
[Check if user exists](#head%5Fdb-%5Fuser-name)  
[Create a new role](#post%5Fdb-%5Frole-)  
[Create a new user](#post%5Fdb-%5Fuser-)  
[Upsert a role](#put%5Fdb-%5Frole-name)  
[Upsert a user](#put%5Fdb-%5Fuser-name)

#### [](#delete%5Fdb-%5Frole-name)Delete a role

DELETE /{db}/_role/{name}

##### [](#delete%5Fdb-%5Frole-name-description)Description

Delete a role from the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Produces

* application/json

##### [](#delete%5Fdb-%5Frole-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the role.                                  | String |

##### [](#delete%5Fdb-%5Frole-name-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | OK                          |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#delete%5Fdb-%5Fuser-name)Delete a user

DELETE /{db}/_user/{name}

##### [](#delete%5Fdb-%5Fuser-name-description)Description

Delete a user from the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Produces

* application/json

##### [](#delete%5Fdb-%5Fuser-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the user.                                  | String |

##### [](#delete%5Fdb-%5Fuser-name-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | User deleted successfully   |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Frole-)Get all names of the roles

GET /{db}/_role/

##### [](#get%5Fdb-%5Frole--description)Description

Retrieves all the roles that are in the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#get%5Fdb-%5Frole--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                   | Description                                                              | Schema  |
| ---------------------- | ------------------------------------------------------------------------ | ------- |
| **deleted** _optional_ | Indicates that roles marked as deleted should be included in the result. | Boolean |

##### [](#get%5Fdb-%5Frole--responses)Responses

| HTTP Code | Description                  | Schema                     |
| --------- | ---------------------------- | -------------------------- |
| 200       | Roles retrieved successfully | String array               |
| 404       | Resource could not be found  | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Frole-name)Get a role

GET /{db}/_role/{name}

##### [](#get%5Fdb-%5Frole-name-description)Description

Retrieve a single roles properties.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#get%5Fdb-%5Frole-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the role.                                  | String |

##### [](#get%5Fdb-%5Frole-name-responses)Responses

| HTTP Code | Description                       | Schema                     |
| --------- | --------------------------------- | -------------------------- |
| 200       | Properties associated with a role | [Role1](#Role%5F1)         |
| 404       | Resource could not be found       | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Fuser-)Get all the names of the users

GET /{db}/_user/

##### [](#get%5Fdb-%5Fuser--description)Description

Retrieves all the names of the users that are in the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#get%5Fdb-%5Fuser--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                      | Description                                                                    | Schema  |
| ------------------------- | ------------------------------------------------------------------------------ | ------- |
| **name\_only** _optional_ | Whether to return user names only, or more detailed information for each user. | Boolean |
| **limit** _optional_      | How many results to return. Using a value of 0 results in no limit.            | Integer |

##### [](#get%5Fdb-%5Fuser--responses)Responses

| HTTP Code | Description                  | Schema                     |
| --------- | ---------------------------- | -------------------------- |
| 200       | Users retrieved successfully | String array               |
| 404       | Resource could not be found  | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Fuser-name)Get a user

GET /{db}/_user/{name}

##### [](#get%5Fdb-%5Fuser-name-description)Description

Retrieve a single users information.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#get%5Fdb-%5Fuser-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the user.                                  | String |

##### [](#get%5Fdb-%5Fuser-name-responses)Responses

| HTTP Code | Description                       | Schema                     |
| --------- | --------------------------------- | -------------------------- |
| 200       | Properties associated with a user | [User1](#User%5F1)         |
| 404       | Resource could not be found       | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fdb-%5Frole-)/{db}/\_role/

HEAD /{db}/_role/

##### [](#head%5Fdb-%5Frole--description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#head%5Fdb-%5Frole--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#head%5Fdb-%5Frole--responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | OK                          |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fdb-%5Frole-name)Check if role exists

HEAD /{db}/_role/{name}

##### [](#head%5Fdb-%5Frole-name-description)Description

Check if the role exists by checking the status code.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#head%5Fdb-%5Frole-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the role.                                  | String |

##### [](#head%5Fdb-%5Frole-name-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | Role exists                 |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fdb-%5Fuser-)/{db}/\_user/

HEAD /{db}/_user/

##### [](#head%5Fdb-%5Fuser--description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#head%5Fdb-%5Fuser--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#head%5Fdb-%5Fuser--responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | OK                          |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fdb-%5Fuser-name)Check if user exists

HEAD /{db}/_user/{name}

##### [](#head%5Fdb-%5Fuser-name-description)Description

Check if the user exists by checking the status code.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#head%5Fdb-%5Fuser-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the user.                                  | String |

##### [](#head%5Fdb-%5Fuser-name-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | User exists |        |
| 404       | Not Found   |        |

#### [](#post%5Fdb-%5Frole-)Create a new role

POST /{db}/_role/

##### [](#post%5Fdb-%5Frole--description)Description

Create a new role using the request body to specify the properties on the role.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Frole--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description                       | Schema          |
| ------------------- | --------------------------------- | --------------- |
| **Body** _optional_ | Properties associated with a role | [Role1](#Role1) |

##### [](#post%5Fdb-%5Frole--responses)Responses

| HTTP Code | Description                             | Schema                     |
| --------- | --------------------------------------- | -------------------------- |
| 201       | New role created successfully           |                            |
| 404       | Resource could not be found             | [HTTPError](#HTTP%5FError) |
| 409       | Resource already exists under that name | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Fuser-)Create a new user

POST /{db}/_user/

##### [](#post%5Fdb-%5Fuser--description)Description

Create a new user using the request body to specify the properties on the user.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Fuser--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description                       | Schema          |
| ------------------- | --------------------------------- | --------------- |
| **Body** _optional_ | Properties associated with a user | [User1](#User1) |

##### [](#post%5Fdb-%5Fuser--responses)Responses

| HTTP Code | Description                             | Schema                     |
| --------- | --------------------------------------- | -------------------------- |
| 201       | New user created successfully           |                            |
| 404       | Resource could not be found             | [HTTPError](#HTTP%5FError) |
| 409       | Resource already exists under that name | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fdb-%5Frole-name)Upsert a role

PUT /{db}/_role/{name}

##### [](#put%5Fdb-%5Frole-name-description)Description

If the role does not exist, create a new role otherwise update the existing role.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fdb-%5Frole-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the role.                                  | String |

Body Parameter

| Name                | Description                       | Schema          |
| ------------------- | --------------------------------- | --------------- |
| **Body** _optional_ | Properties associated with a role | [Role1](#Role1) |

##### [](#put%5Fdb-%5Frole-name-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | OK                          |                            |
| 201       | Created                     |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fdb-%5Fuser-name)Upsert a user

PUT /{db}/_user/{name}

##### [](#put%5Fdb-%5Fuser-name-description)Description

If the user does not exist, create a new user otherwise update the existing user.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fdb-%5Fuser-name-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the user.                                  | String |

Body Parameter

| Name                | Description                       | Schema          |
| ------------------- | --------------------------------- | --------------- |
| **Body** _optional_ | Properties associated with a user | [User1](#User1) |

##### [](#put%5Fdb-%5Fuser-name-responses)Responses

| HTTP Code | Description                         | Schema                     |
| --------- | ----------------------------------- | -------------------------- |
| 200       | Existing user modified successfully |                            |
| 201       | New user created                    |                            |
| 404       | Resource could not be found         | [HTTPError](#HTTP%5FError) |

### [](#tag-Document)Document

Create and manage documents and attachments

[Delete a document](#delete%5Fkeyspace-docid)  
[Delete an attachment on a document](#delete%5Fkeyspace-docid-attach)  
[Delete a local document](#delete%5Fkeyspace-%5Flocal-docid)  
[Gets all the documents in the database with the given parameters](#get%5Fkeyspace-%5Fall%5Fdocs)  
[Get a document](#get%5Fkeyspace-docid)  
[Get an attachment from a document](#get%5Fkeyspace-docid-attach)  
[Get local document](#get%5Fkeyspace-%5Flocal-docid)  
[Get a document with the corresponding metadata](#get%5Fkeyspace-%5Fraw-docid)  
[/{db}/\_all\_docs](#head%5Fkeyspace-%5Fall%5Fdocs)  
[Check if a document exists](#head%5Fkeyspace-docid)  
[Check if attachment exists](#head%5Fkeyspace-docid-attach)  
[Check if local document exists](#head%5Fkeyspace-%5Flocal-docid)  
[/{keyspace}/\_raw/{docid}](#head%5Fkeyspace-%5Fraw-docid)  
[Create a new document](#post%5Fkeyspace-)  
[Get all the documents in the database using a built-in view](#post%5Fkeyspace-%5Fall%5Fdocs)  
[Bulk document operations](#post%5Fkeyspace-%5Fbulk%5Fdocs)  
[Get multiple documents in a MIME multipart response](#post%5Fkeyspace-%5Fbulk%5Fget)  
[Purge a document](#post%5Fkeyspace-%5Fpurge)  
[Upsert a document](#put%5Fkeyspace-docid)  
[Create or update an attachment on a document](#put%5Fkeyspace-docid-attach)  
[Upsert a local document](#put%5Fkeyspace-%5Flocal-docid)

#### [](#delete%5Fkeyspace-docid)Delete a document

DELETE /{keyspace}/{docid}

##### [](#delete%5Fkeyspace-docid-description)Description

Delete a document from the database. A new revision is created so the database can track the deletion in synchronized copies.

A revision ID either in the header or on the query parameters is required.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

#### [](#delete%5Fkeyspace-%5Flocal-docid)Delete a local document

DELETE /{keyspace}/_local/{docid}

##### [](#delete%5Fkeyspace-%5Flocal-docid-description)Description

This request deletes a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#get%5Fkeyspace-docid-attach)Get an attachment from a document

GET /{keyspace}/{docid}/{attach}

##### [](#get%5Fkeyspace-docid-attach-description)Description

This request retrieves a file attachment associated with the document.

The raw data of the associated attachment is returned (just as if you were accessing a static file). The `Content-Type` response header is the same content type set when the document attachment was added to the database. The `Content-Disposition` response header will be set if the content type is considered unsafe to display in a browser (unless overridden by by database config option `serve_insecure_attachment_types`) which will force the attachment to be downloaded.

If the `meta` query parameter is set then the response will be in JSON with the additional metadata tags.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#get%5Fkeyspace-%5Flocal-docid)Get local document

GET /{keyspace}/_local/{docid}

##### [](#get%5Fkeyspace-%5Flocal-docid-description)Description

This request retrieves a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#get%5Fkeyspace-%5Fraw-docid)Get a document with the corresponding metadata

GET /{keyspace}/_raw/{docid}

##### [](#get%5Fkeyspace-%5Fraw-docid-description)Description

Returns the a documents latest revision with its metadata.

Note: The direct use of this endpoint is unsupported. The sync metadata is maintained internally by Sync Gateway and its structure can change. It should not be used to drive business logic of applications since the response to the `/{db}/_raw/{id}` endpoint can change at any time.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#get%5Fkeyspace-%5Fraw-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                               | String |

Query Parameters

| Name                        | Description                                                                          | Schema  |
| --------------------------- | ------------------------------------------------------------------------------------ | ------- |
| **include\_doc** _optional_ | Include the body associated with the document.                                       | String  |
| **redact** _optional_       | This redacts sensitive parts of the response. Cannot be used when include\_docs=true | Boolean |

##### [](#get%5Fkeyspace-%5Fraw-docid-responses)Responses

| HTTP Code | Description                           | Schema                                                                              |
| --------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| 200       | Document found successfully           | [GetKeyspaceRawDocid200Response](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse) |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError)                                                          |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError)                                                          |

#### [](#head%5Fkeyspace-%5Fall%5Fdocs)/{db}/\_all\_docs

HEAD /{keyspace}/_all_docs

##### [](#head%5Fkeyspace-%5Fall%5Fdocs-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#head%5Fkeyspace-docid-attach)Check if attachment exists

HEAD /{keyspace}/{docid}/{attach}

##### [](#head%5Fkeyspace-docid-attach-description)Description

This request check if the attachment exists on the specified document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#head%5Fkeyspace-%5Flocal-docid)Check if local document exists

HEAD /{keyspace}/_local/{docid}

##### [](#head%5Fkeyspace-%5Flocal-docid-description)Description

This request checks if a local document exists.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#head%5Fkeyspace-%5Fraw-docid)/{keyspace}/\_raw/{docid}

HEAD /{keyspace}/_raw/{docid}

##### [](#head%5Fkeyspace-%5Fraw-docid-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#head%5Fkeyspace-%5Fraw-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                               | String |

##### [](#head%5Fkeyspace-%5Fraw-docid-responses)Responses

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#post%5Fkeyspace-%5Fpurge)Purge a document

POST /{keyspace}/_purge

##### [](#post%5Fkeyspace-%5Fpurge-description)Description

The purge command provides a way to remove a document from the database. The operation removes _all_ revisions (active and tombstones) for the specified document(s). A common usage of this endpoint is to remove tombstone documents that are no longer needed, thus recovering storage space and reducing data replicated to clients. Other clients are not notified when a revision has been purged; so in order to purge a revision from the system it must be done from all databases (on Couchbase Lite and Sync Gateway).

When `enable_shared_bucket_access` is enabled, this endpoint removes the document and its associated extended attributes.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fkeyspace-%5Fpurge-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |

Body Parameter

| Name                | Description        | Schema                                                |
| ------------------- | ------------------ | ----------------------------------------------------- |
| **Body** _optional_ | Purge request body | [PostKeyspacePurgeRequest](#PostKeyspacePurgeRequest) |

##### [](#post%5Fkeyspace-%5Fpurge-responses)Responses

| HTTP Code | Description                                                                                                                                                                           | Schema                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 200       | Attempted documents purge. Check output to verify the documents that were purged. The document IDs will not be listed if they have not been purged (for example, due to no existing). | [PostKeyspacePurge200Response](#post%5Fkeyspace%5F%5Fpurge%5F200%5Fresponse) |
| 400       | Bad request. This could be due to the documents listed in the request body not having the \[\\"\*\\"\] value for each document ID.                                                    | [HTTPError](#HTTP%5FError)                                                   |
| 404       | Resource could not be found                                                                                                                                                           | [HTTPError](#HTTP%5FError)                                                   |

#### [](#put%5Fkeyspace-docid)Upsert a document

PUT /{keyspace}/{docid}

##### [](#put%5Fkeyspace-docid-description)Description

This will upsert a document meaning if it does not exist, then it will be created. Otherwise a new revision will be made for the existing document. A revision ID must be provided if targetting an existing document.

A document ID must be specified for this endpoint. To let Sync Gateway generate the ID, use the `POST /{db}/` endpoint.

If a document does exist, then replace the document content with the request body. This means unspecified fields will be removed in the new revision.

The maximum size for a document is 20MB.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

#### [](#put%5Fkeyspace-docid-attach)Create or update an attachment on a document

PUT /{keyspace}/{docid}/{attach}

##### [](#put%5Fkeyspace-docid-attach-description)Description

This request adds or updates an attachment associated with the document. If the document does not exist, it will be created and the attachment will be added to it.

If the attachment already exists, the data of the existing attachment will be replaced in the new revision.

The maximum content size of an attachment is 20MB. The `Content-Type` header of the request specifies the content type of the attachment.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

#### [](#put%5Fkeyspace-%5Flocal-docid)Upsert a local document

PUT /{keyspace}/_local/{docid}

##### [](#put%5Fkeyspace-%5Flocal-docid-description)Description

This request creates or updates a local document. Updating a local document requires that the revision ID be put in the body under `_rev`.

Local document IDs are given a `_local/` prefix. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by the client's replicator, as a place to store replication checkpoint data.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

### [](#tag-Metrics)Metrics

Get Sync Gateway statistics

[Get all Sync Gateway statistics](#get%5F%5Fexpvar)  
[Get memory statistics](#get%5F%5Fstats)

#### [](#get%5F%5Fexpvar)Get all Sync Gateway statistics

GET /_expvar

##### [](#get%5F%5Fexpvar-description)Description

This returns a snapshot of all metrics in Sync Gateway for debugging and monitoring purposes.

This includes per database stats, replication stats, and server stats.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

Produces

* application/javascript

##### [](#get%5F%5Fexpvar-responses)Responses

| HTTP Code | Description         | Schema                                                    |
| --------- | ------------------- | --------------------------------------------------------- |
| 200       | Returned statistics | [GetExpvar200Response](#get%5F%5Fexpvar%5F200%5Fresponse) |

#### [](#get%5F%5Fstats)Get memory statistics

GET /_stats

##### [](#get%5F%5Fstats-description)Description

This will return the current Sync Gateway nodes memory statistics such as current memory usage.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

Produces

* application/json

##### [](#get%5F%5Fstats-responses)Responses

| HTTP Code | Description                      | Schema                                                  |
| --------- | -------------------------------- | ------------------------------------------------------- |
| 200       | Returned memory usage statistics | [GetStats200Response](#get%5F%5Fstats%5F200%5Fresponse) |

### [](#tag-Profiling)Profiling

Generate information to help debug and fine-tune Sync Gateway

[Get fgprof profile](#get%5F%5Fdebug-fgprof)  
[Get block profile](#get%5F%5Fdebug-pprof-block)  
[Get passed in command line parameters](#get%5F%5Fdebug-pprof-cmdline)  
[Get goroutine profile](#get%5F%5Fdebug-pprof-goroutine)  
[Get the heap pprof debug file](#get%5F%5Fdebug-pprof-heap)  
[Get mutex profile](#get%5F%5Fdebug-pprof-mutex)  
[Get the profile pprof debug file](#get%5F%5Fdebug-pprof-profile)  
[Get symbol pprof debug information](#get%5F%5Fdebug-pprof-symbol)  
[Get the threadcreate pprof debug file](#get%5F%5Fdebug-pprof-threadcreate)  
[Get trace profile](#get%5F%5Fdebug-pprof-trace)  
[Get fgprof profile](#post%5F%5Fdebug-fgprof)  
[Get block profile](#post%5F%5Fdebug-pprof-block)  
[Get passed in command line parameters](#post%5F%5Fdebug-pprof-cmdline)  
[Get goroutine profile](#post%5F%5Fdebug-pprof-goroutine)  
[Get the heap pprof debug file](#post%5F%5Fdebug-pprof-heap)  
[Get mutex profile](#post%5F%5Fdebug-pprof-mutex)  
[Get the profile pprof debug file](#post%5F%5Fdebug-pprof-profile)  
[Get symbol pprof debug information](#post%5F%5Fdebug-pprof-symbol)  
[Get the threadcreate pprof debug file](#post%5F%5Fdebug-pprof-threadcreate)  
[Get trace profile](#post%5F%5Fdebug-pprof-trace)  
[Dump heap profile](#post%5F%5Fheap)  
[Start or Stop continuous CPU profiling](#post%5F%5Fprofile)  
[Create point-in-time profile](#post%5F%5Fprofile-profilename)

#### [](#get%5F%5Fdebug-fgprof)Get fgprof profile

GET /_debug/fgprof

##### [](#get%5F%5Fdebug-fgprof-description)Description

A sampling Go profiler that allows you to analyze On-CPU as well as [Off-CPU](https://www.brendangregg.com/offcpuanalysis.html) (e.g. I/O) time together.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/x-gzip

##### [](#get%5F%5Fdebug-fgprof-parameters)Parameters

Query Parameters

| Name                   | Description                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------- | ------- |
| **seconds** _optional_ | The amount of seconds to run the profiler for. **Minimum:** 0 | Integer |

##### [](#get%5F%5Fdebug-fgprof-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#get%5F%5Fdebug-pprof-block)Get block profile

GET /_debug/pprof/block

##### [](#get%5F%5Fdebug-pprof-block-description)Description

Returns stack traces that led to blocking on synchronization primitives.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream
* application/json

##### [](#get%5F%5Fdebug-pprof-block-parameters)Parameters

Query Parameters

| Name                   | Description                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------- | ------- |
| **seconds** _optional_ | The amount of seconds to run the profiler for. **Minimum:** 0 | Integer |

##### [](#get%5F%5Fdebug-pprof-block-responses)Responses

| HTTP Code | Description | Schema                     |
| --------- | ----------- | -------------------------- |
| 200       | OK          | String                     |
| 403       | Forbidden   | [HTTPError](#HTTP%5FError) |

#### [](#get%5F%5Fdebug-pprof-cmdline)Get passed in command line parameters

GET /_debug/pprof/cmdline

##### [](#get%5F%5Fdebug-pprof-cmdline-description)Description

Gets the command line parameters that was passed in to Sync Gateway which will include the binary, flags (if any) and startup configuration.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* text/plain

##### [](#get%5F%5Fdebug-pprof-cmdline-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#get%5F%5Fdebug-pprof-goroutine)Get goroutine profile

GET /_debug/pprof/goroutine

##### [](#get%5F%5Fdebug-pprof-goroutine-description)Description

Stack traces of all current goroutines.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#get%5F%5Fdebug-pprof-goroutine-parameters)Parameters

Query Parameters

| Name                   | Description                                                                    | Schema  |
| ---------------------- | ------------------------------------------------------------------------------ | ------- |
| **seconds** _optional_ | If set, collect a delta profile for the given duration, instead of a snapshot. | Integer |

##### [](#get%5F%5Fdebug-pprof-goroutine-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#get%5F%5Fdebug-pprof-heap)Get the heap pprof debug file

GET /_debug/pprof/heap

##### [](#get%5F%5Fdebug-pprof-heap-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#get%5F%5Fdebug-pprof-heap-parameters)Parameters

Query Parameters

| Name                   | Description                                                                    | Schema  |
| ---------------------- | ------------------------------------------------------------------------------ | ------- |
| **seconds** _optional_ | If set, collect a delta profile for the given duration, instead of a snapshot. | Integer |

##### [](#get%5F%5Fdebug-pprof-heap-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#get%5F%5Fdebug-pprof-mutex)Get mutex profile

GET /_debug/pprof/mutex

##### [](#get%5F%5Fdebug-pprof-mutex-description)Description

Returns stack traces of holders of contended mutexes.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream
* application/json

##### [](#get%5F%5Fdebug-pprof-mutex-parameters)Parameters

Query Parameters

| Name                   | Description                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------- | ------- |
| **seconds** _optional_ | The amount of seconds to run the profiler for. **Minimum:** 0 | Integer |

##### [](#get%5F%5Fdebug-pprof-mutex-responses)Responses

| HTTP Code | Description | Schema                     |
| --------- | ----------- | -------------------------- |
| 200       | OK          | String                     |
| 403       | Forbidden   | [HTTPError](#HTTP%5FError) |

#### [](#get%5F%5Fdebug-pprof-profile)Get the profile pprof debug file

GET /_debug/pprof/profile

##### [](#get%5F%5Fdebug-pprof-profile-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#get%5F%5Fdebug-pprof-profile-parameters)Parameters

Query Parameters

| Name                   | Description                                                                    | Schema  |
| ---------------------- | ------------------------------------------------------------------------------ | ------- |
| **seconds** _optional_ | If set, collect a delta profile for the given duration, instead of a snapshot. | Integer |

##### [](#get%5F%5Fdebug-pprof-profile-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#get%5F%5Fdebug-pprof-symbol)Get symbol pprof debug information

GET /_debug/pprof/symbol

##### [](#get%5F%5Fdebug-pprof-symbol-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* text/plain

##### [](#get%5F%5Fdebug-pprof-symbol-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#get%5F%5Fdebug-pprof-threadcreate)Get the threadcreate pprof debug file

GET /_debug/pprof/threadcreate

##### [](#get%5F%5Fdebug-pprof-threadcreate-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#get%5F%5Fdebug-pprof-threadcreate-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#get%5F%5Fdebug-pprof-trace)Get trace profile

GET /_debug/pprof/trace

##### [](#get%5F%5Fdebug-pprof-trace-description)Description

Responds with the execution trace in binary form.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#get%5F%5Fdebug-pprof-trace-parameters)Parameters

Query Parameters

| Name                   | Description | Schema  |
| ---------------------- | ----------- | ------- |
| **seconds** _optional_ |             | Integer |

##### [](#get%5F%5Fdebug-pprof-trace-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-fgprof)Get fgprof profile

POST /_debug/fgprof

##### [](#post%5F%5Fdebug-fgprof-description)Description

A sampling Go profiler that allows you to analyze On-CPU as well as [Off-CPU](https://www.brendangregg.com/offcpuanalysis.html) (e.g. I/O) time together.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/x-gzip

##### [](#post%5F%5Fdebug-fgprof-parameters)Parameters

Query Parameters

| Name                   | Description                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------- | ------- |
| **seconds** _optional_ | The amount of seconds to run the profiler for. **Minimum:** 0 | Integer |

##### [](#post%5F%5Fdebug-fgprof-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-pprof-block)Get block profile

POST /_debug/pprof/block

##### [](#post%5F%5Fdebug-pprof-block-description)Description

Returns stack traces that led to blocking on synchronization primitives.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream
* application/json

##### [](#post%5F%5Fdebug-pprof-block-parameters)Parameters

Query Parameters

| Name                   | Description                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------- | ------- |
| **seconds** _optional_ | The amount of seconds to run the profiler for. **Minimum:** 0 | Integer |

##### [](#post%5F%5Fdebug-pprof-block-responses)Responses

| HTTP Code | Description | Schema                     |
| --------- | ----------- | -------------------------- |
| 200       | OK          | String                     |
| 403       | Forbidden   | [HTTPError](#HTTP%5FError) |

#### [](#post%5F%5Fdebug-pprof-cmdline)Get passed in command line parameters

POST /_debug/pprof/cmdline

##### [](#post%5F%5Fdebug-pprof-cmdline-description)Description

Gets the command line parameters that was passed in to Sync Gateway which will include the binary, flags (if any) and startup configuration.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* text/plain

##### [](#post%5F%5Fdebug-pprof-cmdline-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-pprof-goroutine)Get goroutine profile

POST /_debug/pprof/goroutine

##### [](#post%5F%5Fdebug-pprof-goroutine-description)Description

Stack traces of all current goroutines.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#post%5F%5Fdebug-pprof-goroutine-parameters)Parameters

Query Parameters

| Name                   | Description                                                                    | Schema  |
| ---------------------- | ------------------------------------------------------------------------------ | ------- |
| **seconds** _optional_ | If set, collect a delta profile for the given duration, instead of a snapshot. | Integer |

##### [](#post%5F%5Fdebug-pprof-goroutine-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-pprof-heap)Get the heap pprof debug file

POST /_debug/pprof/heap

##### [](#post%5F%5Fdebug-pprof-heap-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#post%5F%5Fdebug-pprof-heap-parameters)Parameters

Query Parameters

| Name                   | Description                                                                    | Schema  |
| ---------------------- | ------------------------------------------------------------------------------ | ------- |
| **seconds** _optional_ | If set, collect a delta profile for the given duration, instead of a snapshot. | Integer |

##### [](#post%5F%5Fdebug-pprof-heap-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-pprof-mutex)Get mutex profile

POST /_debug/pprof/mutex

##### [](#post%5F%5Fdebug-pprof-mutex-description)Description

Returns stack traces of holders of contended mutexes.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream
* application/json

##### [](#post%5F%5Fdebug-pprof-mutex-parameters)Parameters

Query Parameters

| Name                   | Description                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------- | ------- |
| **seconds** _optional_ | The amount of seconds to run the profiler for. **Minimum:** 0 | Integer |

##### [](#post%5F%5Fdebug-pprof-mutex-responses)Responses

| HTTP Code | Description | Schema                     |
| --------- | ----------- | -------------------------- |
| 200       | OK          | String                     |
| 403       | Forbidden   | [HTTPError](#HTTP%5FError) |

#### [](#post%5F%5Fdebug-pprof-profile)Get the profile pprof debug file

POST /_debug/pprof/profile

##### [](#post%5F%5Fdebug-pprof-profile-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#post%5F%5Fdebug-pprof-profile-parameters)Parameters

Query Parameters

| Name                   | Description                                                                    | Schema  |
| ---------------------- | ------------------------------------------------------------------------------ | ------- |
| **seconds** _optional_ | If set, collect a delta profile for the given duration, instead of a snapshot. | Integer |

##### [](#post%5F%5Fdebug-pprof-profile-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-pprof-symbol)Get symbol pprof debug information

POST /_debug/pprof/symbol

##### [](#post%5F%5Fdebug-pprof-symbol-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* text/plain

##### [](#post%5F%5Fdebug-pprof-symbol-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-pprof-threadcreate)Get the threadcreate pprof debug file

POST /_debug/pprof/threadcreate

##### [](#post%5F%5Fdebug-pprof-threadcreate-description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#post%5F%5Fdebug-pprof-threadcreate-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fdebug-pprof-trace)Get trace profile

POST /_debug/pprof/trace

##### [](#post%5F%5Fdebug-pprof-trace-description)Description

Responds with the execution trace in binary form.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/octet-stream

##### [](#post%5F%5Fdebug-pprof-trace-parameters)Parameters

Query Parameters

| Name                   | Description | Schema  |
| ---------------------- | ----------- | ------- |
| **seconds** _optional_ |             | Integer |

##### [](#post%5F%5Fdebug-pprof-trace-responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          | String |

#### [](#post%5F%5Fheap)Dump heap profile

POST /_heap

##### [](#post%5F%5Fheap-description)Description

This endpoint will dump a pprof heap profile.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Consumes

* application/json

Produces

* application/json

##### [](#post%5F%5Fheap-parameters)Parameters

Body Parameter

| Name                | Description | Schema                                                          |
| ------------------- | ----------- | --------------------------------------------------------------- |
| **Body** _optional_ |             | [PostProfileProfilenameRequest](#PostProfileProfilenameRequest) |

##### [](#post%5F%5Fheap-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Successfully dumped heap profile      |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |

#### [](#post%5F%5Fprofile)Start or Stop continuous CPU profiling

POST /_profile

##### [](#post%5F%5Fprofile-description)Description

This endpoint allows you to start and stop continuous CPU profiling.

To start profiling the CPU, call this endpoint and supply a file to output the pprof file to.

To stop profiling, call this endpoint but don't supply the `file` in the body.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Consumes

* application/json

Produces

* application/json

##### [](#post%5F%5Fprofile-parameters)Parameters

Body Parameter

| Name                | Description | Schema                                                          |
| ------------------- | ----------- | --------------------------------------------------------------- |
| **Body** _optional_ |             | [PostProfileProfilenameRequest](#PostProfileProfilenameRequest) |

##### [](#post%5F%5Fprofile-responses)Responses

| HTTP Code | Description                                   | Schema                     |
| --------- | --------------------------------------------- | -------------------------- |
| 200       | Successfully started or stopped CPU profiling |                            |
| 400       | There was a problem with your request         | [HTTPError](#HTTP%5FError) |

#### [](#post%5F%5Fprofile-profilename)Create point-in-time profile

POST /_profile/{profilename}

##### [](#post%5F%5Fprofile-profilename-description)Description

This endpoint allows you to create a pprof snapshot of the given type.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Consumes

* application/json

Produces

* application/json

##### [](#post%5F%5Fprofile-profilename-parameters)Parameters

Path Parameters

| Name                       | Description                                                                                         | Schema |
| -------------------------- | --------------------------------------------------------------------------------------------------- | ------ |
| **profilename** _required_ | The handler to use for profiling. **Values:** "heap", "block", "threadcreate", "mutex", "goroutine" | String |

Body Parameter

| Name                | Description | Schema                                                          |
| ------------------- | ----------- | --------------------------------------------------------------- |
| **Body** _optional_ |             | [PostProfileProfilenameRequest](#PostProfileProfilenameRequest) |

##### [](#post%5F%5Fprofile-profilename-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Successfully created profile          |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError) |

### [](#tag-Replication)Replication

Create and manage inter-Sync Gateway replications

[Stop and delete a replication](#delete%5Fdb-%5Freplication-replicationid)  
[Handle incoming BLIP Sync web socket request](#get%5Fdb-%5Fblipsync)  
[Get all replication configurations](#get%5Fdb-%5Freplication-)  
[Get a replication configuration](#get%5Fdb-%5Freplication-replicationid)  
[Get all replication statuses](#get%5Fdb-%5FreplicationStatus-)  
[Get replication status](#get%5Fdb-%5FreplicationStatus-replicationid)  
[/{db}/\_replication/](#head%5Fdb-%5Freplication-)  
[Check if a replication exists](#head%5Fdb-%5Freplication-replicationid)  
[/{db}/\_replicationStatus/](#head%5Fdb-%5FreplicationStatus-)  
[Check if replication exists](#head%5Fdb-%5FreplicationStatus-replicationid)  
[Upsert a replication](#post%5Fdb-%5Freplication-)  
[Upsert a replication](#put%5Fdb-%5Freplication-replicationid)  
[Control a replication state](#put%5Fdb-%5FreplicationStatus-replicationid)

#### [](#delete%5Fdb-%5Freplication-replicationid)Stop and delete a replication

DELETE /{db}/_replication/{replicationid}

##### [](#delete%5Fdb-%5Freplication-replicationid-description)Description

This will delete a replication causing it to stop and no longer exist.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Produces

* application/json

##### [](#delete%5Fdb-%5Freplication-replicationid-parameters)Parameters

Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

##### [](#delete%5Fdb-%5Freplication-replicationid-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Replication successfully deleted      |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Fblipsync)Handle incoming BLIP Sync web socket request

GET /{db}/_blipsync

##### [](#get%5Fdb-%5Fblipsync-description)Description

This handles incoming BLIP Sync requests from either Couchbase Lite or another Sync Gateway node. The connection has to be upgradable to a websocket connection or else the request will fail.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

#### [](#get%5Fdb-%5Freplication-)Get all replication configurations

GET /{db}/_replication/

##### [](#get%5Fdb-%5Freplication--description)Description

This will retrieve all database replication definitions.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Produces

* application/json

##### [](#get%5Fdb-%5Freplication--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#get%5Fdb-%5Freplication--responses)Responses

| HTTP Code | Description                                                                                                                                                                             | Schema                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| 200       | Retrieved replication configurations successfully. The assigned\_node fields will end with (local) or (non-local) depending on if the replication is running on this Sync Gateway node. | [AllReplications](#All%5Freplications) |
| 404       | Resource could not be found                                                                                                                                                             | [HTTPError](#HTTP%5FError)             |

#### [](#get%5Fdb-%5Freplication-replicationid)Get a replication configuration

GET /{db}/_replication/{replicationid}

##### [](#get%5Fdb-%5Freplication-replicationid-description)Description

Retrieve a replication configuration from the database.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Produces

* application/json

##### [](#get%5Fdb-%5Freplication-replicationid-parameters)Parameters

Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

##### [](#get%5Fdb-%5Freplication-replicationid-responses)Responses

| HTTP Code | Description                                          | Schema                           |
| --------- | ---------------------------------------------------- | -------------------------------- |
| 200       | Successfully retrieved the replication configuration | [Replication1](#Replication%5F1) |
| 404       | Resource could not be found                          | [HTTPError](#HTTP%5FError)       |

#### [](#get%5Fdb-%5FreplicationStatus-)Get all replication statuses

GET /{db}/_replicationStatus/

##### [](#get%5Fdb-%5FreplicationStatus--description)Description

Retrieve all the replication statuses in the Sync Gateway node.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Produces

* application/json

##### [](#get%5Fdb-%5FreplicationStatus--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Query Parameters

| Name                         | Description                                                                        | Schema  |
| ---------------------------- | ---------------------------------------------------------------------------------- | ------- |
| **activeOnly** _optional_    | Only return replications that are actively running (state=running).                | Boolean |
| **localOnly** _optional_     | Only return replications that were started on the current Sync Gateway node.       | Boolean |
| **includeError** _optional_  | Include replications that have stopped due to an error (state=error).              | Boolean |
| **includeConfig** _optional_ | Include the replication configuration with each replicator status in the response. | Boolean |

##### [](#get%5Fdb-%5FreplicationStatus--responses)Responses

| HTTP Code | Description                                      | Schema                                          |
| --------- | ------------------------------------------------ | ----------------------------------------------- |
| 200       | Successfully retrieved all replication statuses. | [ReplicationStatus](#Replication%5Fstatus)array |
| 400       | There was a problem with your request            | [HTTPError](#HTTP%5FError)                      |

#### [](#get%5Fdb-%5FreplicationStatus-replicationid)Get replication status

GET /{db}/_replicationStatus/{replicationid}

##### [](#get%5Fdb-%5FreplicationStatus-replicationid-description)Description

Retrieve the status of a replication.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Produces

* application/json

##### [](#get%5Fdb-%5FreplicationStatus-replicationid-parameters)Parameters

Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

Query Parameters

| Name                         | Description                                                                        | Schema  |
| ---------------------------- | ---------------------------------------------------------------------------------- | ------- |
| **activeOnly** _optional_    | Only return replications that are actively running (state=running).                | Boolean |
| **localOnly** _optional_     | Only return replications that were started on the current Sync Gateway node.       | Boolean |
| **includeError** _optional_  | Include replications that have stopped due to an error (state=error).              | Boolean |
| **includeConfig** _optional_ | Include the replication configuration with each replicator status in the response. | Boolean |

##### [](#get%5Fdb-%5FreplicationStatus-replicationid-responses)Responses

| HTTP Code | Description                               | Schema                                     |
| --------- | ----------------------------------------- | ------------------------------------------ |
| 200       | Successfully retrieved replication status | [ReplicationStatus](#Replication%5Fstatus) |
| 400       | There was a problem with your request     | [HTTPError](#HTTP%5FError)                 |
| 404       | Could not find replication                | [HTTPError](#HTTP%5FError)                 |

#### [](#head%5Fdb-%5Freplication-)/{db}/\_replication/

HEAD /{db}/_replication/

##### [](#head%5Fdb-%5Freplication--description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### [](#head%5Fdb-%5Freplication--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#head%5Fdb-%5Freplication--responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          |        |
| 404       | Not Found   |        |

#### [](#head%5Fdb-%5Freplication-replicationid)Check if a replication exists

HEAD /{db}/_replication/{replicationid}

##### [](#head%5Fdb-%5Freplication-replicationid-description)Description

Check if a replication exists.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### [](#head%5Fdb-%5Freplication-replicationid-parameters)Parameters

Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

##### [](#head%5Fdb-%5Freplication-replicationid-responses)Responses

| HTTP Code | Description                | Schema |
| --------- | -------------------------- | ------ |
| 200       | Replication exists         |        |
| 404       | Replication does not exist |        |

#### [](#head%5Fdb-%5FreplicationStatus-)/{db}/\_replicationStatus/

HEAD /{db}/_replicationStatus/

##### [](#head%5Fdb-%5FreplicationStatus--description)Description

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

##### [](#head%5Fdb-%5FreplicationStatus--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#head%5Fdb-%5FreplicationStatus--responses)Responses

| HTTP Code | Description | Schema |
| --------- | ----------- | ------ |
| 200       | OK          |        |
| 400       | Bad Request |        |

#### [](#head%5Fdb-%5FreplicationStatus-replicationid)Check if replication exists

HEAD /{db}/_replicationStatus/{replicationid}

##### [](#head%5Fdb-%5FreplicationStatus-replicationid-description)Description

Check if a replication exists.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Produces

* application/json

##### [](#head%5Fdb-%5FreplicationStatus-replicationid-parameters)Parameters

Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

Query Parameters

| Name                         | Description                                                                        | Schema  |
| ---------------------------- | ---------------------------------------------------------------------------------- | ------- |
| **activeOnly** _optional_    | Only return replications that are actively running (state=running).                | Boolean |
| **localOnly** _optional_     | Only return replications that were started on the current Sync Gateway node.       | Boolean |
| **includeError** _optional_  | Include replications that have stopped due to an error (state=error).              | Boolean |
| **includeConfig** _optional_ | Include the replication configuration with each replicator status in the response. | Boolean |

##### [](#head%5Fdb-%5FreplicationStatus-replicationid-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Replication exists                    |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Freplication-)Upsert a replication

POST /{db}/_replication/

##### [](#post%5Fdb-%5Freplication--description)Description

Create or update a replication in the database.

If an existing replication is being updated, that replication must be stopped first.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Consumes

* application/json

Produces

* application/json

##### [](#post%5Fdb-%5Freplication--parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

Body Parameter

| Name                | Description                                                                                                                                                                                                                                   | Schema                                                                          |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Body** _optional_ | If the replication\_id matches an existing replication then the existing configuration will be updated. Only the specified fields in the request will be used to update the existing configuration. Unspecified fields will remain untouched. | [UserConfigurableReplicationProperties](#UserConfigurableReplicationProperties) |

##### [](#post%5Fdb-%5Freplication--responses)Responses

| HTTP Code | Description                                 | Schema                     |
| --------- | ------------------------------------------- | -------------------------- |
| 200       | Updated existing configuration successfully |                            |
| 201       | Created new replication successfully        |                            |
| 400       | There was a problem with your request       | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                 | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fdb-%5Freplication-replicationid)Upsert a replication

PUT /{db}/_replication/{replicationid}

##### [](#put%5Fdb-%5Freplication-replicationid-description)Description

Create or update a replication in the database.

The replication ID does **not** need to be set in the request body.

If an existing replication is being updated, that replication must be stopped first and, if the `replication_id` is specified in the request body, it must match the replication ID in the URI.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Consumes

* application/json

Produces

* application/json

##### [](#put%5Fdb-%5Freplication-replicationid-parameters)Parameters

Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

Body Parameter

| Name                | Description                                                                                                                                                                                                                                   | Schema                                                                          |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Body** _optional_ | If the replication\_id matches an existing replication then the existing configuration will be updated. Only the specified fields in the request will be used to update the existing configuration. Unspecified fields will remain untouched. | [UserConfigurableReplicationProperties](#UserConfigurableReplicationProperties) |

##### [](#put%5Fdb-%5Freplication-replicationid-responses)Responses

| HTTP Code | Description                                 | Schema                     |
| --------- | ------------------------------------------- | -------------------------- |
| 200       | Updated existing configuration successfully |                            |
| 201       | Created new replication successfully        |                            |
| 400       | There was a problem with your request       | [HTTPError](#HTTP%5FError) |
| 404       | Resource could not be found                 | [HTTPError](#HTTP%5FError) |

#### [](#put%5Fdb-%5FreplicationStatus-replicationid)Control a replication state

PUT /{db}/_replicationStatus/{replicationid}

##### [](#put%5Fdb-%5FreplicationStatus-replicationid-description)Description

Control the replication by changing its state.

This is done through the action query parameter, which has 3 valid values:

* `start` \- starts a stopped replication
* `stop` \- stops an active replication
* `reset` \- resets the replication checkpoint to 0\. For bidirectional replication, both push and pull checkpoints are reset to 0\. The replication must be stopped to use this.

Required Sync Gateway RBAC roles:

* Sync Gateway Replicator

Produces

* application/json

##### [](#put%5Fdb-%5FreplicationStatus-replicationid-parameters)Parameters

Path Parameters

| Name                         | Description                                             | Schema |
| ---------------------------- | ------------------------------------------------------- | ------ |
| **db** _required_            | The name of the database to run the operation against.  | String |
| **replicationid** _required_ | What replication to target based on its replication ID. | String |

Query Parameters

| Name                  | Description                                                                       | Schema |
| --------------------- | --------------------------------------------------------------------------------- | ------ |
| **action** _required_ | The target state to put the replicator into. **Values:** "start", "stop", "reset" | String |

##### [](#put%5Fdb-%5FreplicationStatus-replicationid-responses)Responses

| HTTP Code | Description                                     | Schema                                     |
| --------- | ----------------------------------------------- | ------------------------------------------ |
| 200       | Successfully changed target state of replicator | [ReplicationStatus](#Replication%5Fstatus) |
| 400       | There was a problem with your request           | [HTTPError](#HTTP%5FError)                 |
| 404       | Resource could not be found                     | [HTTPError](#HTTP%5FError)                 |

### [](#tag-Server)Server

Manage server activities

[Cancel the Sync Gateway Collect Info job](#delete%5F%5Fsgcollect%5Finfo)  
[Get server information](#get%5F-)  
[Get server configuration](#get%5F%5Fconfig)  
[Get console logging settings](#get%5F%5Flogging)  
[Check if API is available](#get%5F%5Fping)  
[Get the status of the Sync Gateway Collect Info](#get%5F%5Fsgcollect%5Finfo)  
[Get the server status](#get%5F%5Fstatus)  
[Check if server online](#head%5F-)  
[Check if API is available](#head%5F%5Fping)  
[Update console logging settings](#post%5F%5Flogging)  
[Run the post upgrade process on all databases](#post%5F%5Fpost%5Fupgrade)  
[Start Sync Gateway Collect Info](#post%5F%5Fsgcollect%5Finfo)  
[Set runtime configuration](#put%5F%5Fconfig)  
[Set console logging settings](#put%5F%5Flogging)

#### [](#delete%5F%5Fsgcollect%5Finfo)Cancel the Sync Gateway Collect Info job

DELETE /_sgcollect_info

##### [](#delete%5F%5Fsgcollect%5Finfo-description)Description

This endpoint is used to cancel a current Sync Gateway Collect Info (sgcollect\_info) job that is running.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#delete%5F%5Fsgcollect%5Finfo-responses)Responses

| HTTP Code | Description                           | Schema                                                                           |
| --------- | ------------------------------------- | -------------------------------------------------------------------------------- |
| 200       | Job cancelled successfully            | [DeleteSgcollectInfo200Response](#delete%5F%5Fsgcollect%5Finfo%5F200%5Fresponse) |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError)                                                       |

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

#### [](#get%5F%5Fconfig)Get server configuration

GET /_config

##### [](#get%5F%5Fconfig-description)Description

This will return the configuration that the Sync Gateway node was initially started up with, or the currently config if `include_runtime` is set.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#get%5F%5Fconfig-parameters)Parameters

Query Parameters

| Name                            | Description                                                                                              | Schema  |
| ------------------------------- | -------------------------------------------------------------------------------------------------------- | ------- |
| **redact** _optional_           | No longer supported field.                                                                               | Boolean |
| **include\_runtime** _optional_ | Whether to include the values set after starting (at runtime), default values, and all loaded databases. | Boolean |

##### [](#get%5F%5Fconfig-responses)Responses

| HTTP Code | Description                                | Schema                             |
| --------- | ------------------------------------------ | ---------------------------------- |
| 200       | Successfully returned server configuration | [StartupConfig](#Startup%5Fconfig) |
| 400       | There was a problem with your request      | [HTTPError](#HTTP%5FError)         |

#### [](#get%5F%5Flogging)Get console logging settings

GET /_logging

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#get%5F%5Flogging-description)Description

**Deprecated in favour of `GET /_config`**This will return a map of the log keys being used for the console logging.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#get%5F%5Flogging-responses)Responses

| HTTP Code | Description                      | Schema      |
| --------- | -------------------------------- | ----------- |
| 200       | Returned map of console log keys | [Map](#Map) |

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

#### [](#get%5F%5Fsgcollect%5Finfo)Get the status of the Sync Gateway Collect Info

GET /_sgcollect_info

##### [](#get%5F%5Fsgcollect%5Finfo-description)Description

This will return the status of whether Sync Gateway Collect Info (sgcollect\_info) is currently running or not.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#get%5F%5Fsgcollect%5Finfo-responses)Responses

| HTTP Code | Description                     | Schema                                                                     |
| --------- | ------------------------------- | -------------------------------------------------------------------------- |
| 200       | Returned sgcollect\_info status | [GetSgcollectInfo200Response](#get%5F%5Fsgcollect%5Finfo%5F200%5Fresponse) |

#### [](#get%5F%5Fstatus)Get the server status

GET /_status

##### [](#get%5F%5Fstatus-description)Description

This will retrieve the status of each database and the overall server status.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#get%5F%5Fstatus-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Returned the status successfully      | [Status1](#Status%5F1)     |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |

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

#### [](#post%5F%5Flogging)Update console logging settings

POST /_logging

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#post%5F%5Flogging-description)Description

**Deprecated in favour of `PUT /_config`**This is for enabling the log keys provided and optionally changing the console log level.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Consumes

* application/json

Produces

* application/json

##### [](#post%5F%5Flogging-parameters)Parameters

Query Parameters

| Name                    | Description                                                                                                                                                                                | Schema  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| **logLevel** _optional_ | The is what to set the console log level too. **Values:** "none", "error", "warn", "info", "debug", "trace"                                                                                | String  |
| **level** _optional_    | **Deprecated: use log level instead.** This sets the console log level depending on the value provide. 1 sets to info, 2 sets to warn, and 3 sets to error.' **Minimum:** 1 **Maximum:** 3 | Integer |

Body Parameter

| Name                | Description                     | Schema      |
| ------------------- | ------------------------------- | ----------- |
| **Body** _optional_ | The console log keys to upsert. | [Map](#Map) |

##### [](#post%5F%5Flogging-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Log keys successfully updated.        |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |

#### [](#post%5F%5Fpost%5Fupgrade)Run the post upgrade process on all databases

POST /_post_upgrade

##### [](#post%5F%5Fpost%5Fupgrade-description)Description

The post upgrade process involves removing obsolete design documents and indexes when they are no longer needed.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#post%5F%5Fpost%5Fupgrade-parameters)Parameters

Query Parameters

| Name                   | Description                                                     | Schema |
| ---------------------- | --------------------------------------------------------------- | ------ |
| **preview** _optional_ | If set, a dry-run will be done to return what would be removed. | String |

##### [](#post%5F%5Fpost%5Fupgrade-responses)Responses

| HTTP Code | Description      | Schema                                                                   |
| --------- | ---------------- | ------------------------------------------------------------------------ |
| 200       | Returned results | [PostPostUpgrade200Response](#post%5F%5Fpost%5Fupgrade%5F200%5Fresponse) |

#### [](#post%5F%5Fsgcollect%5Finfo)Start Sync Gateway Collect Info

POST /_sgcollect_info

##### [](#post%5F%5Fsgcollect%5Finfo-description)Description

This endpoint is used to start a Sync Gateway Collect Info (sgcollect\_info) job so that Sync Gateway diagnostic data can be outputted to a file.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Consumes

* application/json

Produces

* application/json

##### [](#post%5F%5Fsgcollect%5Finfo-parameters)Parameters

Body Parameter

| Name                | Description             | Schema                                                |
| ------------------- | ----------------------- | ----------------------------------------------------- |
| **Body** _optional_ | sgcollect\_info options | [PostSgcollectInfoRequest](#PostSgcollectInfoRequest) |

##### [](#post%5F%5Fsgcollect%5Finfo-responses)Responses

| HTTP Code | Description                                           | Schema                                                                       |
| --------- | ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| 200       | Successfully started sgcollect\_info                  | [PostSgcollectInfo200Response](#post%5F%5Fsgcollect%5Finfo%5F200%5Fresponse) |
| 400       | There was a problem with your request                 | [HTTPError](#HTTP%5FError)                                                   |
| 500       | An error occurred while trying to run sgcollect\_info | [HTTPError](#HTTP%5FError)                                                   |

#### [](#put%5F%5Fconfig)Set runtime configuration

PUT /_config

##### [](#put%5F%5Fconfig-description)Description

This endpoint is used to dynamically set runtime options, like logging without needing a restart.

These options are not persisted, and will not survive a restart of Sync Gateway.

The endpoint only accepts a limited number of options that can be changed at runtime. See request body schema for allowable options.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Consumes

* application/json

Produces

* application/json

##### [](#put%5F%5Fconfig-parameters)Parameters

Body Parameter

| Name                | Description | Schema                          |
| ------------------- | ----------- | ------------------------------- |
| **Body** _optional_ |             | [RuntimeConfig](#RuntimeConfig) |

##### [](#put%5F%5Fconfig-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Successfully set runtime options      |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |

#### [](#put%5F%5Flogging)Set console logging settings

PUT /_logging

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

##### [](#put%5F%5Flogging-description)Description

**Deprecated in favour of `PUT /_config`**Enable or disable console log keys and optionally change the console log level.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Consumes

* application/json

Produces

* application/json

##### [](#put%5F%5Flogging-parameters)Parameters

Query Parameters

| Name                    | Description                                                                                                                                                                                | Schema  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| **logLevel** _optional_ | The is what to set the console log level too. **Values:** "none", "error", "warn", "info", "debug", "trace"                                                                                | String  |
| **level** _optional_    | **Deprecated: use log level instead.** This sets the console log level depending on the value provide. 1 sets to info, 2 sets to warn, and 3 sets to error.' **Minimum:** 1 **Maximum:** 3 | Integer |

Body Parameter

| Name                | Description                                     | Schema      |
| ------------------- | ----------------------------------------------- | ----------- |
| **Body** _optional_ | The map of log keys to use for console logging. | [Map](#Map) |

##### [](#put%5F%5Flogging-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Log keys successfully replaced.       |                            |
| 400       | There was a problem with your request | [HTTPError](#HTTP%5FError) |

### [](#tag-Session)Session

Manage user sessions

[Remove session](#delete%5Fdb-%5Fsession-sessionid)  
[Remove all of a users sessions](#delete%5Fdb-%5Fuser-name-%5Fsession)  
[Remove session with user validation](#delete%5Fdb-%5Fuser-name-%5Fsession-sessionid)  
[Get information about the current user](#get%5Fdb-%5Fsession)  
[Get session information](#get%5Fdb-%5Fsession-sessionid)  
[/{db}/\_session](#head%5Fdb-%5Fsession)  
[Create a new user session](#post%5Fdb-%5Fsession)

#### [](#delete%5Fdb-%5Fsession-sessionid)Remove session

DELETE /{db}/_session/{sessionid}

##### [](#delete%5Fdb-%5Fsession-sessionid-description)Description

Invalidates the session provided so that anyone using it is logged out and is prevented from future use.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Produces

* application/json

##### [](#delete%5Fdb-%5Fsession-sessionid-parameters)Parameters

Path Parameters

| Name                     | Description                                            | Schema |
| ------------------------ | ------------------------------------------------------ | ------ |
| **db** _required_        | The name of the database to run the operation against. | String |
| **sessionid** _required_ | The ID of the session to target.                       | String |

##### [](#delete%5Fdb-%5Fsession-sessionid-responses)Responses

| HTTP Code | Description                           | Schema                     |
| --------- | ------------------------------------- | -------------------------- |
| 200       | Successfully removed the user session |                            |
| 404       | Resource could not be found           | [HTTPError](#HTTP%5FError) |

#### [](#delete%5Fdb-%5Fuser-name-%5Fsession)Remove all of a users sessions

DELETE /{db}/_user/{name}/_session

##### [](#delete%5Fdb-%5Fuser-name-%5Fsession-description)Description

Invalidates all the sessions that a user has.

Will still return a `200` status code if the user has no sessions.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Produces

* application/json

##### [](#delete%5Fdb-%5Fuser-name-%5Fsession-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **name** _required_ | The name of the user.                                  | String |

##### [](#delete%5Fdb-%5Fuser-name-%5Fsession-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | User now has no sessions    |                            |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#delete%5Fdb-%5Fuser-name-%5Fsession-sessionid)Remove session with user validation

DELETE /{db}/_user/{name}/_session/{sessionid}

##### [](#delete%5Fdb-%5Fuser-name-%5Fsession-sessionid-description)Description

Invalidates the session only if it belongs to the user.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

Produces

* application/json

##### [](#delete%5Fdb-%5Fuser-name-%5Fsession-sessionid-parameters)Parameters

Path Parameters

| Name                     | Description                                            | Schema |
| ------------------------ | ------------------------------------------------------ | ------ |
| **db** _required_        | The name of the database to run the operation against. | String |
| **name** _required_      | The name of the user.                                  | String |
| **sessionid** _required_ | The ID of the session to target.                       | String |

##### [](#delete%5Fdb-%5Fuser-name-%5Fsession-sessionid-responses)Responses

| HTTP Code | Description                                                                       | Schema                     |
| --------- | --------------------------------------------------------------------------------- | -------------------------- |
| 200       | Session has been successfully removed as the user was associated with the session |                            |
| 404       | Resource could not be found                                                       | [HTTPError](#HTTP%5FError) |

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

#### [](#get%5Fdb-%5Fsession-sessionid)Get session information

GET /{db}/_session/{sessionid}

##### [](#get%5Fdb-%5Fsession-sessionid-description)Description

Retrieve session information such as the user the session belongs too and what channels that user can access.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#get%5Fdb-%5Fsession-sessionid-parameters)Parameters

Path Parameters

| Name                     | Description                                            | Schema |
| ------------------------ | ------------------------------------------------------ | ------ |
| **db** _required_        | The name of the database to run the operation against. | String |
| **sessionid** _required_ | The ID of the session to target.                       | String |

##### [](#get%5Fdb-%5Fsession-sessionid-responses)Responses

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

Generates a login session for a user and returns the session ID and cookie name for that session. If no TTL is provided, then the default of 24 hours will be used.

A session cannot be generated for an non-existent user or the `GUEST` user.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Application

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

| HTTP Code | Description                                                                                | Schema                                                               |
| --------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| 200       | Session created successfully. Returned body is dependant on if using Public or Admin APIs. | [PostDbSession200Response](#post%5Fdb%5F%5Fsession%5F200%5Fresponse) |
| 400       | Origin is not in the approved list of allowed origins                                      | [HTTPError](#HTTP%5FError)                                           |
| 404       | Resource could not be found                                                                | [HTTPError](#HTTP%5FError)                                           |

### [](#tag-Unsupported)Unsupported

Endpoints that are not supported by Sync Gateway

[Delete a design document | Unsupported](#delete%5Fdb-%5Fdesign-ddoc)  
[Get views of a design document | Unsupported](#get%5Fdb-%5Fdesign-ddoc)  
[Query a view on a design document | Unsupported](#get%5Fdb-%5Fdesign-ddoc-%5Fview-view)  
[Dump a view | Unsupported](#get%5Fdb-%5Fdump-view)  
[Query a view on the default design document | Unsupported](#get%5Fdb-%5Fview-view)  
[Dump all the documents in a channel | Unsupported](#get%5Fkeyspace-%5Fdumpchannel-channel)  
[Revision tree structure in Graphviz Dot format | Unsupported](#get%5Fkeyspace-%5Frevtree-docid)  
[Check if view of design document exists | Unsupported](#head%5Fdb-%5Fdesign-ddoc)  
[Flush the entire database bucket | Unsupported](#post%5Fdb-%5Fflush)  
[Disabled endpoint](#post%5Fdb-%5Frepair)  
[Update views of a design document | Unsupported](#put%5Fdb-%5Fdesign-ddoc)

#### [](#delete%5Fdb-%5Fdesign-ddoc)Delete a design document | Unsupported

DELETE /{db}/_design/{ddoc}

##### [](#delete%5Fdb-%5Fdesign-ddoc-description)Description

**This is unsupported**

Delete a design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

| HTTP Code | Description                 | Schema                                                                  |
| --------- | --------------------------- | ----------------------------------------------------------------------- |
| 200       | Returned view successfully  | [GetDbViewView200Response](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse) |
| 403       | Forbidden                   |                                                                         |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError)                                              |

#### [](#get%5Fdb-%5Fdump-view)Dump a view | Unsupported

GET /{db}/_dump/{view}

##### [](#get%5Fdb-%5Fdump-view-description)Description

**This is unsupported**

This queries the view and outputs it as HTML.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* text/html
* application/json

##### [](#get%5Fdb-%5Fdump-view-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
| **view** _required_ | The view to target.                                    | String |

##### [](#get%5Fdb-%5Fdump-view-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | Retrieved view successfully | String                     |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |
| 500       | Internal Server Error       | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fdb-%5Fview-view)Query a view on the default design document | Unsupported

GET /{db}/_view/{view}

##### [](#get%5Fdb-%5Fview-view-description)Description

**This is unsupported**

Query a view on the default Sync Gateway design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* application/json

##### [](#get%5Fdb-%5Fview-view-parameters)Parameters

Path Parameters

| Name                | Description                                            | Schema |
| ------------------- | ------------------------------------------------------ | ------ |
| **db** _required_   | The name of the database to run the operation against. | String |
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

##### [](#get%5Fdb-%5Fview-view-responses)Responses

| HTTP Code | Description                 | Schema                                                                  |
| --------- | --------------------------- | ----------------------------------------------------------------------- |
| 200       | Returned view successfully  | [GetDbViewView200Response](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse) |
| 403       | Forbidden                   |                                                                         |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError)                                              |

#### [](#get%5Fkeyspace-%5Fdumpchannel-channel)Dump all the documents in a channel | Unsupported

GET /{keyspace}/_dumpchannel/{channel}

##### [](#get%5Fkeyspace-%5Fdumpchannel-channel-description)Description

**This is unsupported**

This queries a channel and displays all the document IDs and revisions that are in that channel.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

Produces

* text/html
* application/json

##### [](#get%5Fkeyspace-%5Fdumpchannel-channel-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **channel** _required_  | The channel to dump all the documents from.                                                                                                                 | String |

Query Parameters

| Name                 | Description                                                                                                                                                                      | Schema |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **since** _optional_ | Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response. | String |

##### [](#get%5Fkeyspace-%5Fdumpchannel-channel-responses)Responses

| HTTP Code | Description                                   | Schema                     |
| --------- | --------------------------------------------- | -------------------------- |
| 200       | Successfully got all documents in the channel | String                     |
| 404       | Resource could not be found                   | [HTTPError](#HTTP%5FError) |

#### [](#get%5Fkeyspace-%5Frevtree-docid)Revision tree structure in Graphviz Dot format | Unsupported

GET /{keyspace}/_revtree/{docid}

##### [](#get%5Fkeyspace-%5Frevtree-docid-description)Description

This returns the Dot syntax of the revision tree for the document so that it can be rendered in to a PNG image using the [Graphviz CLI tool](https://www.graphviz.org/).

To use:

1. Install the Graphviz tool. Using Brew, this can be done by calling `brew install graphviz`.
2. Save the response text from this endpoint to a file (for example, `revtree.dot`).
3. Render the PNG by calling `dot -Tpng revtree.dot > revtree.png`.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

**Note: This endpoint is useful for debugging purposes only. It is not officially supported.**

Produces

* application/json

##### [](#get%5Fkeyspace-%5Frevtree-docid-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                 | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **keyspace** _required_ | The keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. | String |
| **docid** _required_    | The document ID to run the operation against.                                                                                                               | String |

##### [](#get%5Fkeyspace-%5Frevtree-docid-responses)Responses

| HTTP Code | Description                 | Schema                     |
| --------- | --------------------------- | -------------------------- |
| 200       | Found document              | String                     |
| 404       | Resource could not be found | [HTTPError](#HTTP%5FError) |

#### [](#head%5Fdb-%5Fdesign-ddoc)Check if view of design document exists | Unsupported

HEAD /{db}/_design/{ddoc}

##### [](#head%5Fdb-%5Fdesign-ddoc-description)Description

**This is unsupported**

Check if a design document can be queried.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

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

#### [](#post%5Fdb-%5Fflush)Flush the entire database bucket | Unsupported

POST /{db}/_flush

##### [](#post%5Fdb-%5Fflush-description)Description

**This is unsupported**

This will purge _all_ documents.

The bucket will only be flushed if the unsupported database configuration option `enable_couchbase_bucket_flush` is set.

Required Sync Gateway RBAC roles:

* Sync Gateway Dev Ops

Produces

* application/json

##### [](#post%5Fdb-%5Fflush-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#post%5Fdb-%5Fflush-responses)Responses

| HTTP Code | Description                                 | Schema                     |
| --------- | ------------------------------------------- | -------------------------- |
| 200       | Successfully flushed the bucket             |                            |
| 404       | Resource could not be found                 | [HTTPError](#HTTP%5FError) |
| 503       | The bucket does not support flush or delete | [HTTPError](#HTTP%5FError) |

#### [](#post%5Fdb-%5Frepair)Disabled endpoint

POST /{db}/_repair

##### [](#post%5Fdb-%5Frepair-description)Description

This endpoint is disabled.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect

##### [](#post%5Fdb-%5Frepair-parameters)Parameters

Path Parameters

| Name              | Description                                            | Schema |
| ----------------- | ------------------------------------------------------ | ------ |
| **db** _required_ | The name of the database to run the operation against. | String |

##### [](#post%5Fdb-%5Frepair-responses)Responses

| HTTP Code | Description               | Schema |
| --------- | ------------------------- | ------ |
| 500       | This endpoint is disabled |        |

#### [](#put%5Fdb-%5Fdesign-ddoc)Update views of a design document | Unsupported

PUT /{db}/_design/{ddoc}

##### [](#put%5Fdb-%5Fdesign-ddoc-description)Description

**This is unsupported**

Update the views of a design document.

Required Sync Gateway RBAC roles:

* Sync Gateway Application

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

[All replications](#All%5Freplications)  
[ChangesFeed](#Changes-feed)  
[CollectionAccessConfig](#CollectionAccessConfig)  
[Collection config](#Collection%5Fconfig)  
[Compact-status](#Compact%5Fstatus)  
[Console-logging-config](#Console%5Flogging%5Fconfig)  
[Credentials config](#Credentials%5Fconfig)  
[Credentials config](#Credentials%5Fconfig%5F1)  
[Database-config](#Database)  
[Database-config](#Database%5Fconfig)  
[DatabaseConfigCache](#Database%5Fconfig%5Fcache)  
[DatabaseConfigCacheChannelCache](#Database%5Fconfig%5Fcache%5Fchannel%5Fcache)  
[DatabaseConfigCacheRevCache](#Database%5Fconfig%5Fcache%5Frev%5Fcache)  
[DatabaseConfigCors](#Database%5Fconfig%5Fcors)  
[DatabaseConfigDeltaSync](#Database%5Fconfig%5Fdelta%5Fsync)  
[DatabaseConfigEventHandlers](#Database%5Fconfig%5Fevent%5Fhandlers)  
[DatabaseConfigLocalJwtValue](#Database%5Fconfig%5Flocal%5Fjwt%5Fvalue)  
[DatabaseConfigLocalJwtValueKeysInner](#Database%5Fconfig%5Flocal%5Fjwt%5Fvalue%5Fkeys%5Finner)  
[DatabaseConfigLogging](#Database%5Fconfig%5Flogging)  
[DatabaseConfigLoggingConsole](#Database%5Fconfig%5Flogging%5Fconsole)  
[DatabaseConfigOidc](#Database%5Fconfig%5Foidc)  
[DatabaseConfigOidcProvidersValue](#Database%5Fconfig%5Foidc%5Fproviders%5Fvalue)  
[DatabaseConfigReplications](#Database%5Fconfig%5Freplications)  
[DatabaseConfigUnsupported](#Database%5Fconfig%5Funsupported)  
[DatabaseConfigUnsupportedApiEndpoints](#Database%5Fconfig%5Funsupported%5Fapi%5Fendpoints)  
[DatabaseConfigUnsupportedOidcTestProvider](#Database%5Fconfig%5Funsupported%5Foidc%5Ftest%5Fprovider)  
[DatabaseConfigUnsupportedUserViews](#Database%5Fconfig%5Funsupported%5Fuser%5Fviews)  
[DatabaseConfigUnsupportedWarningThresholds](#Database%5Fconfig%5Funsupported%5Fwarning%5Fthresholds)  
[DeleteSgcollectInfo200Response](#delete%5F%5Fsgcollect%5Finfo%5F200%5Fresponse)  
[DesignDoc](#Design-doc)  
[Document](#Document)  
[Event-config](#Event%5Fconfig)  
[ExpVars](#ExpVars)  
[Get200Response](#get%5F%5F%5F200%5Fresponse)  
[Get200ResponseVendor](#get%5F%5F%5F200%5Fresponse%5Fvendor)  
[GetAllDbs200Response](#get%5F%5Fall%5Fdbs%5F200%5Fresponse)  
[GetAllDbs200ResponseOneOfInner](#get%5F%5Fall%5Fdbs%5F200%5Fresponse%5FoneOf%5Finner)  
[GetDb200Response](#get%5Fdb%5F%5F200%5Fresponse)  
[GetDbDesignDdoc200Response](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse)  
[GetDbDesignDdoc200ResponseOptions](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Foptions)  
[GetDbDesignDdoc200ResponseViewsValue](#get%5Fdb%5F%5Fdesign%5Fddoc%5F200%5Fresponse%5Fviews%5Fvalue)  
[GetDbOidcTestingCerts200Response](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse)  
[GetDbOidcTestingCerts200ResponseKeysInner](#get%5Fdb%5F%5Foidc%5Ftesting%5Fcerts%5F200%5Fresponse%5Fkeys%5Finner)  
[GetDbOidcTestingWellKnownOpenidConfiguration200Response](#get%5Fdb%5F%5Foidc%5Ftesting%5F%5Fwell%5Fknown%5Fopenid%5Fconfiguration%5F200%5Fresponse)  
[GetDbViewView200Response](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse)  
[GetDbViewView200ResponseErrorsInner](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse%5Ferrors%5Finner)  
[GetDbViewView200ResponseRowsInner](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse%5Frows%5Finner)  
[GetExpvar200Response](#get%5F%5Fexpvar%5F200%5Fresponse)  
[GetExpvar200ResponseSyncGatewayChangeCache](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache)  
[GetExpvar200ResponseSyncGatewayDb](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)  
[GetExpvar200ResponseSyncgateway](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)  
[GetExpvar200ResponseSyncgatewayGlobal](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal)  
[GetExpvar200ResponseSyncgatewayGlobalResourceUtilization](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal%5Fresource%5Futilization)  
[GetExpvar200ResponseSyncgatewayPerDbInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Fdb%5Finner)  
[GetExpvar200ResponseSyncgatewayPerReplicationInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner)  
[GetExpvar200ResponseSyncgatewayPerReplicationInnerReplicationId](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner%5F%5Freplication%5Fid)  
[GetKeyspaceAllDocs200Response](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse)  
[GetKeyspaceAllDocs200ResponseRowsInner](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner)  
[GetKeyspaceAllDocs200ResponseRowsInnerValue](#get%5Fkeyspace%5F%5Fall%5Fdocs%5F200%5Fresponse%5Frows%5Finner%5Fvalue)  
[GetKeyspaceChanges200Response](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse)  
[GetKeyspaceChanges200ResponseResultsInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner)  
[GetKeyspaceChanges200ResponseResultsInnerChangesInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner%5Fchanges%5Finner)  
[GetKeyspaceDocid200Response](#get%5Fkeyspace%5Fdocid%5F200%5Fresponse)  
[GetKeyspaceRawDocid200Response](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse)  
[GetKeyspaceRawDocid200ResponseSync](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync)  
[GetKeyspaceRawDocid200ResponseSyncChannelSetHistoryInner](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fchannel%5Fset%5Fhistory%5Finner)  
[GetKeyspaceRawDocid200ResponseSyncChannelSetInner](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fchannel%5Fset%5Finner)  
[GetKeyspaceRawDocid200ResponseSyncHistory](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fhistory)  
[GetSgcollectInfo200Response](#get%5F%5Fsgcollect%5Finfo%5F200%5Fresponse)  
[GetStats200Response](#get%5F%5Fstats%5F200%5Fresponse)  
[HTTP-Error](#HTTP%5FError)  
[Log-rotation-config](#Log%5Frotation%5Fconfig)  
[LoggingConfig](#Logging-config)  
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
[PostDbOnlineRequest](#post%5Fdb%5F%5Fonline%5Frequest)  
[PostDbResyncRequest](#post%5Fdb%5F%5Fresync%5Frequest)  
[PostDbSession200Response](#post%5Fdb%5F%5Fsession%5F200%5Fresponse)  
[PostDbSessionRequest](#post%5Fdb%5F%5Fsession%5Frequest)  
[PostKeyspaceAllDocsRequest](#post%5Fkeyspace%5F%5Fall%5Fdocs%5Frequest)  
[PostKeyspaceBulkDocs201ResponseInner](#post%5Fkeyspace%5F%5Fbulk%5Fdocs%5F201%5Fresponse%5Finner)  
[PostKeyspaceBulkDocsRequest](#post%5Fkeyspace%5F%5Fbulk%5Fdocs%5Frequest)  
[PostKeyspaceBulkGetRequest](#post%5Fkeyspace%5F%5Fbulk%5Fget%5Frequest)  
[PostKeyspaceBulkGetRequestDocsInner](#post%5Fkeyspace%5F%5Fbulk%5Fget%5Frequest%5Fdocs%5Finner)  
[PostKeyspaceChangesRequest](#post%5Fkeyspace%5F%5Fchanges%5Frequest)  
[PostKeyspacePurge200Response](#post%5Fkeyspace%5F%5Fpurge%5F200%5Fresponse)  
[PostKeyspacePurgeRequest](#post%5Fkeyspace%5F%5Fpurge%5Frequest)  
[PostKeyspaceRequest](#post%5Fkeyspace%5F%5Frequest)  
[PostKeyspaceRequestAttachmentsValue](#post%5Fkeyspace%5F%5Frequest%5F%5Fattachments%5Fvalue)  
[PostKeyspaceRequestRevisions](#post%5Fkeyspace%5F%5Frequest%5F%5Frevisions)  
[PostKeyspaceRevsDiff200Response](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse)  
[PostKeyspaceRevsDiff200ResponseDocid](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5F200%5Fresponse%5Fdocid)  
[PostKeyspaceRevsDiffRequest](#post%5Fkeyspace%5F%5Frevs%5Fdiff%5Frequest)  
[PostPostUpgrade200Response](#post%5F%5Fpost%5Fupgrade%5F200%5Fresponse)  
[PostPostUpgrade200ResponsePostUpgradeResultsValue](#post%5F%5Fpost%5Fupgrade%5F200%5Fresponse%5Fpost%5Fupgrade%5Fresults%5Fvalue)  
[PostProfileProfilenameRequest](#post%5F%5Fprofile%5Fprofilename%5Frequest)  
[PostSgcollectInfo200Response](#post%5F%5Fsgcollect%5Finfo%5F200%5Fresponse)  
[PostSgcollectInfoRequest](#post%5F%5Fsgcollect%5Finfo%5Frequest)  
[PutKeyspaceLocalDocidRequest](#put%5Fkeyspace%5F%5Flocal%5Fdocid%5Frequest)  
[User configurable replication properties](#Replication)  
[Replication](#Replication%5F1)  
[Replication-status](#Replication%5Fstatus)  
[Resync-status](#Resync%5Fstatus)  
[Replication](#Retrieved-replication)  
[Role](#Role)  
[Role](#Role%5F1)  
[Role](#Role%5F2)  
[Runtime-config](#Runtime%5Fconfig)  
[RuntimeConfigLogging](#Runtime%5Fconfig%5Flogging)  
[Scopes](#Scopes)  
[Scopes](#Scopes%5F1)  
[Serverless](#Serverless)  
[Startup-config](#Startup%5Fconfig)  
[StartupConfigApi](#Startup%5Fconfig%5Fapi)  
[StartupConfigApiCors](#Startup%5Fconfig%5Fapi%5Fcors)  
[StartupConfigApiHttps](#Startup%5Fconfig%5Fapi%5Fhttps)  
[StartupConfigAuth](#Startup%5Fconfig%5Fauth)  
[StartupConfigBootstrap](#Startup%5Fconfig%5Fbootstrap)  
[StartupConfigLogging](#Startup%5Fconfig%5Flogging)  
[StartupConfigLoggingDebug](#Startup%5Fconfig%5Flogging%5Fdebug)  
[StartupConfigLoggingDebugRotation](#Startup%5Fconfig%5Flogging%5Fdebug%5Frotation)  
[StartupConfigLoggingError](#Startup%5Fconfig%5Flogging%5Ferror)  
[StartupConfigLoggingErrorRotation](#Startup%5Fconfig%5Flogging%5Ferror%5Frotation)  
[StartupConfigLoggingInfo](#Startup%5Fconfig%5Flogging%5Finfo)  
[StartupConfigLoggingInfoRotation](#Startup%5Fconfig%5Flogging%5Finfo%5Frotation)  
[StartupConfigLoggingStats](#Startup%5Fconfig%5Flogging%5Fstats)  
[StartupConfigLoggingTrace](#Startup%5Fconfig%5Flogging%5Ftrace)  
[StartupConfigLoggingWarn](#Startup%5Fconfig%5Flogging%5Fwarn)  
[StartupConfigLoggingWarnRotation](#Startup%5Fconfig%5Flogging%5Fwarn%5Frotation)  
[StartupConfigReplicator](#Startup%5Fconfig%5Freplicator)  
[StartupConfigUnsupported](#Startup%5Fconfig%5Funsupported)  
[StartupConfigUnsupportedHttp2](#Startup%5Fconfig%5Funsupported%5Fhttp2)  
[StartupConfigUnsupportedServerless](#Startup%5Fconfig%5Funsupported%5Fserverless)  
[Status](#Status)  
[Status](#Status%5F1)  
[Status1DatabasesValue](#Status%5F1%5Fdatabases%5Fvalue)  
[Status1DatabasesValueCluster](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster)  
[Status1DatabasesValueClusterNodes](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Fnodes)  
[Status1DatabasesValueClusterNodesNodeUuid](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Fnodes%5Fnode%5Fuuid)  
[Status1DatabasesValueClusterReplication](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Freplication)  
[User](#User)  
[User](#User%5F1)  
[User1CollectionAccessValueValue](#User%5F1%5Fcollection%5Faccess%5Fvalue%5Fvalue)  
[User](#User%5F2)  
[User configurable replication properties](#User%5Fconfigurable%5Freplication%5Fproperties)  
[User Session Information](#User%5FSession%5FInformation)  
[UserSessionInformationUserCtx](#User%5FSession%5FInformation%5FuserCtx)

### [](#All%5Freplications)All replications

 Object

| Property                       |                             | Schema                           |
| ------------------------------ | --------------------------- | -------------------------------- |
| **replication\_id** _optional_ | Properties of a replication | [Replication1](#Replication%5F1) |

### [](#Changes-feed)ChangesFeed

 Object

| Property                 |                                  | Schema                                                                                                            |
| ------------------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **results** _optional_   | **Unique items:** true           | [GetKeyspaceChanges200ResponseResultsInner](#get%5Fkeyspace%5F%5Fchanges%5F200%5Fresponse%5Fresults%5Finner)array |
| **last\_seq** _optional_ | The last change sequence number. | String                                                                                                            |

### [](#CollectionAccessConfig)CollectionAccessConfig

 Object

| Property                          |                                                                                                                                                                                           | Schema           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **admin\_channels** _optional_    | A list of channels to explicitly grant to the user.                                                                                                                                       | String array     |
| **all\_channels** _optional_      | All the channels that the user has been granted access to. Access could have been granted through the sync function, roles, or explicitly on the user under the admin\_channels property. | String array     |
| **jwt\_channels** _optional_      | The channels that the user has been granted access to through channels\_claim.                                                                                                            | String array     |
| **jwt\_last\_updated** _optional_ | The last time that the user's JWT roles/channels were updated.                                                                                                                            | Date (date-time) |

### [](#Collection%5Fconfig)Collection config

 Object

| Property                      |                                                                                                                                                                                                                                                                                                                                                                                  | Schema |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **sync** _optional_           | The Javascript function that newly created documents in this collection are ran through.                                                                                                                                                                                                                                                                                         | String |
| **import\_filter** _optional_ | This is the function that all imported documents in this collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported. import\_docs in the database config must be true to make this field applicable. | String |

### [](#Compact%5Fstatus)Compact-status

 Object

| Property                           |                                                                                                                                                                                                                                      | Schema |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **status** _required_              | The status of the current operation.                                                                                                                                                                                                 | String |
| **start\_time** _required_         | The ISO-8601 date and time the compact operation was started.                                                                                                                                                                        | String |
| **last\_error** _required_         | The last error that occurred in the compact operation (if any).                                                                                                                                                                      | String |
| **docs\_purged** _optional_        | **Applicable to tombstone compaction only** This is the amount of documents that have been purged so far.                                                                                                                            | String |
| **marked\_attachments** _optional_ | **Applicable to attachment compaction only** This is the number of references there are to legacy attachments.                                                                                                                       | String |
| **purged\_attachments** _optional_ | **Applicable to attachment compaction only** This is the amount of attachments that have been purged so far.                                                                                                                         | String |
| **compact\_id** _optional_         | **Applicable to attachment compaction only** This is the ID of the compaction.                                                                                                                                                       | String |
| **phase** _optional_               | **Applicable to attachment compaction only** This indicates the current phase of running attachment compact processes. For failed processes, this indicates the phase at which a compact\_id restart will commence (where relevant). | String |
| **dry\_run** _optional_            | **Applicable to attachment compaction only** **Values:** "mark", "sweep", "cleanup"                                                                                                                                                  | String |

### [](#Console%5Flogging%5Fconfig)Console-logging-config

 Object

| Property                               |                                                                                                        | Schema                                        |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **log\_level** _optional_              | Log Level for the console output **Values:** "none", "error", "warn", "info", "debug", "trace"         | String                                        |
| **log\_keys** _optional_               | Log Keys for the console output                                                                        | String array                                  |
| **color\_enabled** _optional_          | Log with color for the console output                                                                  | Boolean                                       |
| **file\_output** _optional_            | Override the default stderr output, and write to the file specified instead                            | String                                        |
| **enabled** _optional_                 | Toggle for this log output                                                                             | Boolean                                       |
| **rotation** _optional_                |                                                                                                        | [LogRotationConfig](#Log%5Frotation%5Fconfig) |
| **collation\_buffer\_size** _optional_ | The size of the log collation buffer. The default is 10 if the output is stderr, or 1000 if to a file. | Integer                                       |

### [](#Credentials%5Fconfig)Credentials config

 Object

| Property                        |                                                                           | Schema |
| ------------------------------- | ------------------------------------------------------------------------- | ------ |
| **username** _optional_         | Username for authenticating to the bucket                                 | String |
| **password** _optional_         | Password for authenticating to the bucket. This value is always redacted. | String |
| **x509\_cert\_path** _optional_ | Cert path (public key) for X.509 bucket auth                              | String |
| **x509\_key\_path** _optional_  | Key path (private key) for X.509 bucket auth                              | String |

### [](#Credentials%5Fconfig%5F1)Credentials config

 Object

| Property                        |                                                                           | Schema |
| ------------------------------- | ------------------------------------------------------------------------- | ------ |
| **username** _optional_         | Username for authenticating to the bucket                                 | String |
| **password** _optional_         | Password for authenticating to the bucket. This value is always redacted. | String |
| **x509\_cert\_path** _optional_ | Cert path (public key) for X.509 bucket auth                              | String |
| **x509\_key\_path** _optional_  | Key path (private key) for X.509 bucket auth                              | String |

### [](#Database)Database-config

 Object

| Property                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Schema                                                               |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **server** _optional_                                  | This is the Couchbase Server address or addresses that the database connect to.                                                                                                                                                                                                                                                                                                                                                                                                                                              | String                                                               |
| **pool** _optional_                                    | This field is unsupported and ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String                                                               |
| **bucket** _optional_                                  | The Couchbase Server backing bucket for the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String                                                               |
| **username** _optional_                                | The username for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String                                                               |
| **password** _optional_                                | The password for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String                                                               |
| **certpath** _optional_                                | The cert path (public key) for X.509 bucket auth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String                                                               |
| **keypath** _optional_                                 | The key path (private key) for X.509 bucket auth                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | String                                                               |
| **cacertpath** _optional_                              | The root CA cert path for X.509 bucket authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String                                                               |
| **kv\_tls\_port** _optional_                           | The Memcached TLS port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Integer                                                              |
| **max\_concurrent\_query\_ops** _optional_             | The maximum amount of query operations that can be running at any one point.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer                                                              |
| **scopes** _optional_                                  | An object keyed by scope name containing config for the specific collection. **Maximum items:** 1                                                                                                                                                                                                                                                                                                                                                                                                                            | [Map](#Map)                                                          |
| **name** _optional_                                    | The name of the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | String                                                               |
| **sync** _optional_                                    | The Javascript function that newly created documents are ran through for the default scope and collection. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                                                                                                                      | String                                                               |
| **users** _optional_                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Map](#Map)                                                          |
| **roles** _optional_                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Map](#Map)                                                          |
| **revs\_limit** _optional_                             | The maximum depth a document's revision tree can grow too. The minimum is 20 if conflicts are allowed and 0 if not. It is not recommended to go below 100 when conflicts are allowed. **Minimum:** 0                                                                                                                                                                                                                                                                                                                         | Big Decimal                                                          |
| **import\_docs** _optional_                            | If true, documents will be imported in to Sync Gateway from the bucket when requested. Documents will be ran through the set import\_filter if any is set. The default value depends on the edition of Sync Gateway being used. If the edition is the community-edition, then this will default to false or else in the enterprise-edition, it will default to true. This can also be set to the string continuous which maps to true.                                                                                       | Boolean                                                              |
| **import\_partitions** _optional_                      | \*\* This is an enterprise-edition feature only\*\* This is how many import partitions should be used for import sharding. Partitions are distributed among all Sync Gateway nodes participating in import processing (import\_docs=true), and each process a subset of the server's vbuckets. Each partition is processed by an independent function that runs simultaneously to others, so import\_partitions can be used to tune concurrency based on the number of Sync Gateway nodes, and the number of cores per node. | Big Decimal                                                          |
| **import\_filter** _optional_                          | This is the function that all imported documents in the default scope and collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported. import\_docs must be true to make this field applicable. If scopes parameter is set, this is ignored.                                                                                                      | String                                                               |
| **import\_backup\_old\_rev** _optional_                | This controls whether import should attempt to create a temporary backup of the previous revision body (if available) when the document is modified in the bucket.                                                                                                                                                                                                                                                                                                                                                           | Boolean                                                              |
| **event\_handlers** _optional_                         | These are the settings for webhooks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [DatabaseConfigEventHandlers](#Database%5Fconfig%5Fevent%5Fhandlers) |
| **feed\_type** _optional_                              | The type of feed to use to communicate with Couchbase Server. This will use DCP regardless of specification. **Values:** "DCP"                                                                                                                                                                                                                                                                                                                                                                                               | String                                                               |
| **allow\_empty\_password** _optional_                  | This controls whether users that are created can have an empty password or not.                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean                                                              |
| **cache** _optional_                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [DatabaseConfigCache](#Database%5Fconfig%5Fcache)                    |
| **rev\_cache\_size** _optional_                        | **Deprecated, please use the database setting cache.rev\_cache.size instead** The maximum number of revisions to store in the revision cache.                                                                                                                                                                                                                                                                                                                                                                                | Big Decimal                                                          |
| **offline** _optional_                                 | Start the database in an offline state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean                                                              |
| **unsupported** _optional_                             | These are unsupported options and therefore it is not recommended to use them.                                                                                                                                                                                                                                                                                                                                                                                                                                               | [DatabaseConfigUnsupported](#Database%5Fconfig%5Funsupported)        |
| **local\_jwt** _optional_                              | Configuration for Local JWT authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Map](#Map)                                                          |
| **oidc** _optional_                                    | Configuration for OpenID Connect authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [DatabaseConfigOidc](#Database%5Fconfig%5Foidc)                      |
| **old\_rev\_expiry\_seconds** _optional_               | The number of seconds before old revisions are removed from the Couchbase Server bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                     | Big Decimal                                                          |
| **view\_query\_timeout\_secs** _optional_              | The number of seconds before a view query should timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer                                                              |
| **local\_doc\_expiry\_secs** _optional_                | The number of seconds before a \_local document should expire.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer                                                              |
| **enable\_shared\_bucket\_access** _optional_          | Whether to use extended attributes to store Sync Gateway document (\_sync) metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean                                                              |
| **session\_cookie\_secure** _optional_                 | Override the session cookie secure flag. If set, the cookie will have the secure flag. This will default to true if startup config api.https.tls\_cert\_path is set otherwise it will default to false.                                                                                                                                                                                                                                                                                                                      | Boolean                                                              |
| **session\_cookie\_name** _optional_                   | This can be used to define a custom per-database session cookie name.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String                                                               |
| **session\_cookie\_http\_only** _optional_             | Make all session cookies for the database set the HttpOnly flag so they are inaccessible to JavaScript.                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean                                                              |
| **allow\_conflicts** _optional_                        | This controls whether to allow conflicting document revisions.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Boolean                                                              |
| **num\_index\_replicas** _optional_                    | This is the number of Global Secondary Indexes (GSI) to use for core indexes.                                                                                                                                                                                                                                                                                                                                                                                                                                                | Big Decimal                                                          |
| **use\_views** _optional_                              | Force the use of views instead of GSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean                                                              |
| **send\_www\_authenticate\_header** _optional_         | Controls whether to send a WWW-Authenticate header in 401 Unauthorized HTTP responses.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean                                                              |
| **disable\_password\_auth** _optional_                 | Whether to disable username/password authentication and only allow OIDC and guest access.                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean                                                              |
| **bucket\_op\_timeout\_ms** _optional_                 | This is the amount of milliseconds should pass before a bucket operation times out. An error will be returned if the bucket operation times out saying: operation timed out.                                                                                                                                                                                                                                                                                                                                                 | Big Decimal                                                          |
| **slow\_query\_warning\_threshold** _optional_         | The amount of milliseconds a N1QL query should run before logging a warning.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Big Decimal                                                          |
| **delta\_sync** _optional_                             | Delta sync configuration settings. **This is an enterprise-edition feature only**                                                                                                                                                                                                                                                                                                                                                                                                                                            | [DatabaseConfigDeltaSync](#Database%5Fconfig%5Fdelta%5Fsync)         |
| **compact\_interval\_days** _optional_                 | The interval between scheduled tombstone compaction runs (in days). This can be a floating point number. If set to 0, compaction will not run automatically.                                                                                                                                                                                                                                                                                                                                                                 | Big Decimal                                                          |
| **sgreplicate\_enabled** _optional_                    | Whether the node should accept assign replications (true) or not (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean                                                              |
| **sgreplicate\_websocket\_heartbeat\_secs** _optional_ | Use a custom heartbeat interval (in seconds) for websocket ping frames.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Integer                                                              |
| **replications** _optional_                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [DatabaseConfigReplications](#Database%5Fconfig%5Freplications)      |
| **serve\_insecure\_attachment\_types** _optional_      | If set, always serve attachments with the Content-Type header set to the type of the attachment. When serving an attachment, usually the Content-Type header is set to the type of the attachment but the Content-Disposition response header will be set instead if the content type is vulnerable to a phishing attack, causing the browser to download the file instead of display it. This option will override that behaviour and always set the Content-Type header.                                                   | Boolean                                                              |
| **query\_pagination\_limit** _optional_                | The query limit to be used during pagination of large queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer                                                              |
| **user\_xattr\_key** _optional_                        | The key to use for the user xattr that will be accessible from the sync function. IF empty, the feature will be disabled.                                                                                                                                                                                                                                                                                                                                                                                                    | String                                                               |
| **client\_partition\_window\_secs** _optional_         | How long (in seconds) clients can remain offline for without losing replication metadata. Defaults to 30 days (in seconds)                                                                                                                                                                                                                                                                                                                                                                                                   | Integer                                                              |
| **guest** _optional_                                   | Properties associated with a user                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [User1](#User%5F1)                                                   |
| **javascript\_timeout\_secs** _optional_               | The maximum number of seconds the sync, import filter, and custom conflict resolver JavaScript functions are allowed to run for before timing out. Set to 0 to allow the JS functions to run uncapped.                                                                                                                                                                                                                                                                                                                       | Big Decimal                                                          |
| **suspendable** _optional_                             | Set to true to allow the database to be suspended. Defaults to true when running in serverless mode otherwise defaults to false.                                                                                                                                                                                                                                                                                                                                                                                             | Boolean                                                              |
| **cors** _optional_                                    | CORS configuration for this database; if present, overrides server's config.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [DatabaseConfigCors](#Database%5Fconfig%5Fcors)                      |
| **logging** _optional_                                 | Per-database logging configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [DatabaseConfigLogging](#Database%5Fconfig%5Flogging)                |

### [](#Database%5Fconfig)Database-config

 Object

| Property                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Schema                                                               |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **server** _optional_                                  | This is the Couchbase Server address or addresses that the database connect to.                                                                                                                                                                                                                                                                                                                                                                                                                                              | String                                                               |
| **pool** _optional_                                    | This field is unsupported and ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String                                                               |
| **bucket** _optional_                                  | The Couchbase Server backing bucket for the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String                                                               |
| **username** _optional_                                | The username for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String                                                               |
| **password** _optional_                                | The password for authenticating to the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String                                                               |
| **certpath** _optional_                                | The cert path (public key) for X.509 bucket auth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String                                                               |
| **keypath** _optional_                                 | The key path (private key) for X.509 bucket auth                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | String                                                               |
| **cacertpath** _optional_                              | The root CA cert path for X.509 bucket authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String                                                               |
| **kv\_tls\_port** _optional_                           | The Memcached TLS port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Integer                                                              |
| **max\_concurrent\_query\_ops** _optional_             | The maximum amount of query operations that can be running at any one point.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer                                                              |
| **scopes** _optional_                                  | An object keyed by scope name containing config for the specific collection. **Maximum items:** 1                                                                                                                                                                                                                                                                                                                                                                                                                            | [Map](#Map)                                                          |
| **name** _optional_                                    | The name of the database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | String                                                               |
| **sync** _optional_                                    | The Javascript function that newly created documents are ran through for the default scope and collection. If scopes parameter is set, this is ignored.                                                                                                                                                                                                                                                                                                                                                                      | String                                                               |
| **users** _optional_                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Map](#Map)                                                          |
| **roles** _optional_                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [Map](#Map)                                                          |
| **revs\_limit** _optional_                             | The maximum depth a document's revision tree can grow too. The minimum is 20 if conflicts are allowed and 0 if not. It is not recommended to go below 100 when conflicts are allowed. **Minimum:** 0                                                                                                                                                                                                                                                                                                                         | Big Decimal                                                          |
| **import\_docs** _optional_                            | If true, documents will be imported in to Sync Gateway from the bucket when requested. Documents will be ran through the set import\_filter if any is set. The default value depends on the edition of Sync Gateway being used. If the edition is the community-edition, then this will default to false or else in the enterprise-edition, it will default to true. This can also be set to the string continuous which maps to true.                                                                                       | Boolean                                                              |
| **import\_partitions** _optional_                      | \*\* This is an enterprise-edition feature only\*\* This is how many import partitions should be used for import sharding. Partitions are distributed among all Sync Gateway nodes participating in import processing (import\_docs=true), and each process a subset of the server's vbuckets. Each partition is processed by an independent function that runs simultaneously to others, so import\_partitions can be used to tune concurrency based on the number of Sync Gateway nodes, and the number of cores per node. | Big Decimal                                                          |
| **import\_filter** _optional_                          | This is the function that all imported documents in the default scope and collection are ran through in order to filter out what to import and what not to import. This allows you to control what is made available to Couchbase Mobile clients. If it is not set, then no documents are filtered when imported. import\_docs must be true to make this field applicable. If scopes parameter is set, this is ignored.                                                                                                      | String                                                               |
| **import\_backup\_old\_rev** _optional_                | This controls whether import should attempt to create a temporary backup of the previous revision body (if available) when the document is modified in the bucket.                                                                                                                                                                                                                                                                                                                                                           | Boolean                                                              |
| **event\_handlers** _optional_                         | These are the settings for webhooks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [DatabaseConfigEventHandlers](#Database%5Fconfig%5Fevent%5Fhandlers) |
| **feed\_type** _optional_                              | The type of feed to use to communicate with Couchbase Server. This will use DCP regardless of specification. **Values:** "DCP"                                                                                                                                                                                                                                                                                                                                                                                               | String                                                               |
| **allow\_empty\_password** _optional_                  | This controls whether users that are created can have an empty password or not.                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean                                                              |
| **cache** _optional_                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [DatabaseConfigCache](#Database%5Fconfig%5Fcache)                    |
| **rev\_cache\_size** _optional_                        | **Deprecated, please use the database setting cache.rev\_cache.size instead** The maximum number of revisions to store in the revision cache.                                                                                                                                                                                                                                                                                                                                                                                | Big Decimal                                                          |
| **offline** _optional_                                 | Start the database in an offline state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean                                                              |
| **unsupported** _optional_                             | These are unsupported options and therefore it is not recommended to use them.                                                                                                                                                                                                                                                                                                                                                                                                                                               | [DatabaseConfigUnsupported](#Database%5Fconfig%5Funsupported)        |
| **local\_jwt** _optional_                              | Configuration for Local JWT authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Map](#Map)                                                          |
| **oidc** _optional_                                    | Configuration for OpenID Connect authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [DatabaseConfigOidc](#Database%5Fconfig%5Foidc)                      |
| **old\_rev\_expiry\_seconds** _optional_               | The number of seconds before old revisions are removed from the Couchbase Server bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                     | Big Decimal                                                          |
| **view\_query\_timeout\_secs** _optional_              | The number of seconds before a view query should timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer                                                              |
| **local\_doc\_expiry\_secs** _optional_                | The number of seconds before a \_local document should expire.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer                                                              |
| **enable\_shared\_bucket\_access** _optional_          | Whether to use extended attributes to store Sync Gateway document (\_sync) metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean                                                              |
| **session\_cookie\_secure** _optional_                 | Override the session cookie secure flag. If set, the cookie will have the secure flag. This will default to true if startup config api.https.tls\_cert\_path is set otherwise it will default to false.                                                                                                                                                                                                                                                                                                                      | Boolean                                                              |
| **session\_cookie\_name** _optional_                   | This can be used to define a custom per-database session cookie name.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String                                                               |
| **session\_cookie\_http\_only** _optional_             | Make all session cookies for the database set the HttpOnly flag so they are inaccessible to JavaScript.                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean                                                              |
| **allow\_conflicts** _optional_                        | This controls whether to allow conflicting document revisions.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Boolean                                                              |
| **num\_index\_replicas** _optional_                    | This is the number of Global Secondary Indexes (GSI) to use for core indexes.                                                                                                                                                                                                                                                                                                                                                                                                                                                | Big Decimal                                                          |
| **use\_views** _optional_                              | Force the use of views instead of GSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean                                                              |
| **send\_www\_authenticate\_header** _optional_         | Controls whether to send a WWW-Authenticate header in 401 Unauthorized HTTP responses.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean                                                              |
| **disable\_password\_auth** _optional_                 | Whether to disable username/password authentication and only allow OIDC and guest access.                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean                                                              |
| **bucket\_op\_timeout\_ms** _optional_                 | This is the amount of milliseconds should pass before a bucket operation times out. An error will be returned if the bucket operation times out saying: operation timed out.                                                                                                                                                                                                                                                                                                                                                 | Big Decimal                                                          |
| **slow\_query\_warning\_threshold** _optional_         | The amount of milliseconds a N1QL query should run before logging a warning.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Big Decimal                                                          |
| **delta\_sync** _optional_                             | Delta sync configuration settings. **This is an enterprise-edition feature only**                                                                                                                                                                                                                                                                                                                                                                                                                                            | [DatabaseConfigDeltaSync](#Database%5Fconfig%5Fdelta%5Fsync)         |
| **compact\_interval\_days** _optional_                 | The interval between scheduled tombstone compaction runs (in days). This can be a floating point number. If set to 0, compaction will not run automatically.                                                                                                                                                                                                                                                                                                                                                                 | Big Decimal                                                          |
| **sgreplicate\_enabled** _optional_                    | Whether the node should accept assign replications (true) or not (false).                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean                                                              |
| **sgreplicate\_websocket\_heartbeat\_secs** _optional_ | Use a custom heartbeat interval (in seconds) for websocket ping frames.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Integer                                                              |
| **replications** _optional_                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [DatabaseConfigReplications](#Database%5Fconfig%5Freplications)      |
| **serve\_insecure\_attachment\_types** _optional_      | If set, always serve attachments with the Content-Type header set to the type of the attachment. When serving an attachment, usually the Content-Type header is set to the type of the attachment but the Content-Disposition response header will be set instead if the content type is vulnerable to a phishing attack, causing the browser to download the file instead of display it. This option will override that behaviour and always set the Content-Type header.                                                   | Boolean                                                              |
| **query\_pagination\_limit** _optional_                | The query limit to be used during pagination of large queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer                                                              |
| **user\_xattr\_key** _optional_                        | The key to use for the user xattr that will be accessible from the sync function. IF empty, the feature will be disabled.                                                                                                                                                                                                                                                                                                                                                                                                    | String                                                               |
| **client\_partition\_window\_secs** _optional_         | How long (in seconds) clients can remain offline for without losing replication metadata. Defaults to 30 days (in seconds)                                                                                                                                                                                                                                                                                                                                                                                                   | Integer                                                              |
| **guest** _optional_                                   | Properties associated with a user                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [User1](#User%5F1)                                                   |
| **javascript\_timeout\_secs** _optional_               | The maximum number of seconds the sync, import filter, and custom conflict resolver JavaScript functions are allowed to run for before timing out. Set to 0 to allow the JS functions to run uncapped.                                                                                                                                                                                                                                                                                                                       | Big Decimal                                                          |
| **suspendable** _optional_                             | Set to true to allow the database to be suspended. Defaults to true when running in serverless mode otherwise defaults to false.                                                                                                                                                                                                                                                                                                                                                                                             | Boolean                                                              |
| **cors** _optional_                                    | CORS configuration for this database; if present, overrides server's config.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [DatabaseConfigCors](#Database%5Fconfig%5Fcors)                      |
| **logging** _optional_                                 | Per-database logging configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [DatabaseConfigLogging](#Database%5Fconfig%5Flogging)                |

### [](#Database%5Fconfig%5Fcache)DatabaseConfigCache

 Object

| Property                                   |                                                                                                                                                                                           | Schema                                                                          |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **rev\_cache** _optional_                  | The revision cache config settings.                                                                                                                                                       | [DatabaseConfigCacheRevCache](#Database%5Fconfig%5Fcache%5Frev%5Fcache)         |
| **channel\_cache** _optional_              | The channel cache config settings.                                                                                                                                                        | [DatabaseConfigCacheChannelCache](#Database%5Fconfig%5Fcache%5Fchannel%5Fcache) |
| **max\_wait\_pending** _optional_          | **Deprecated, please use the database setting cache.channel\_cache.max\_wait\_pending instead** The maximum time (in milliseconds) for waiting for a pending sequence before skipping it. | Big Decimal                                                                     |
| **max\_wait\_skipped** _optional_          | **Deprecated, please use the database setting cache.channel\_cache.max\_wait\_skipped instead** The maximum time (in milliseconds) for waiting for pending sequences before skipping.     | Big Decimal                                                                     |
| **enable\_star\_channel** _optional_       | **Deprecated, please use the database setting cache.channel\_cache.enable\_star\_channel instead** Used to control whether Sync Gateway should use the all documents (\*) channel.        | Boolean                                                                         |
| **channel\_cache\_max\_length** _optional_ | **Deprecated, please use the database setting cache.channel\_cache.max\_length instead** The maximum number of entries maintained in cache per channel.                                   | Big Decimal                                                                     |
| **channel\_cache\_min\_length** _optional_ | **Deprecated, please use the database setting cache.channel\_cache.min\_length instead** The minimum number of entries maintained in cache per channel.                                   | Integer                                                                         |
| **channel\_cache\_expiry** _optional_      | **Deprecated, please use the database setting cache.channel\_cache.expiry\_seconds instead** The time (seconds) to keep entries in cache beyond the minimum retained.                     | Integer                                                                         |
| **max\_num\_pending** _optional_           | **Deprecated, please use the database setting cache.channel\_cache.max\_num\_pending instead** The max number of pending sequences before skipping.                                       | Integer                                                                         |

### [](#Database%5Fconfig%5Fcache%5Fchannel%5Fcache)DatabaseConfigCacheChannelCache

 Object

| Property                                     |                                                                                                                                                                                                                                                                                                               | Schema      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **max\_number** _optional_                   | The maximum number of channel caches which can exist at any one point.                                                                                                                                                                                                                                        | Integer     |
| **compact\_high\_watermark\_pct** _optional_ | The trigger value for starting the channel cache eviction process. Specify this as a percentage which will be the percentage used on \`max\_number). When the cache size, determined by max\_number, reaches the high watermark, the eviction process iterates through the cache, removing inactive channels. | Integer     |
| **compact\_low\_watermark\_pct** _optional_  | The trigger value for stopping the channel cache eviction process. Specify this as a percentage which will be the percentage used on \`max\_number). When the cache size, determined by max\_number returns to a value lower than the percentage of it set here, the cache eviction process is stopped.       | Integer     |
| **max\_wait\_pending** _optional_            | The maximum time (in milliseconds) for waiting for a pending sequence before skipping it.                                                                                                                                                                                                                     | Big Decimal |
| **max\_num\_pending** _optional_             | The maximum number of pending sequences before skipping sequences.                                                                                                                                                                                                                                            | Integer     |
| **max\_wait\_skipped** _optional_            | The maximum amount of time (in milliseconds) to wait for a skipped sequence before abandoning it.                                                                                                                                                                                                             | Big Decimal |
| **enable\_star\_channel** _optional_         | Used to control whether Sync Gateway should use the all documents (\*) channel.                                                                                                                                                                                                                               | Boolean     |
| **max\_length** _optional_                   | The maximum number of entries to maintain in the cache per channel.                                                                                                                                                                                                                                           | Integer     |
| **min\_length** _optional_                   | The minimum number of entries to maintain in the cache per channel.                                                                                                                                                                                                                                           | Integer     |
| **expiry\_seconds** _optional_               | The amount of time (in seconds) to keep entries in the cache beyond the minimum retained.                                                                                                                                                                                                                     | Integer     |
| **query\_limit** _optional_                  | **Deprecated in favour of the database setting query\_pagination\_limit** The limit used for channel queries.                                                                                                                                                                                                 | Integer     |

### [](#Database%5Fconfig%5Fcache%5Frev%5Fcache)DatabaseConfigCacheRevCache

 Object

| Property                    |                                                                           | Schema |
| --------------------------- | ------------------------------------------------------------------------- | ------ |
| **size** _optional_         | The maximum number of revisions that can be stored in the revision cache. | String |
| **shard\_count** _optional_ | The number of shards the revision cache should be split into.             | String |

### [](#Database%5Fconfig%5Fcors)DatabaseConfigCors

 Object

| Property                     |                                                                       | Schema       |
| ---------------------------- | --------------------------------------------------------------------- | ------------ |
| **origin** _optional_        | List of allowed origins, use \['\*'\] to allow access from everywhere | String array |
| **login\_origin** _optional_ | List of allowed login origins                                         | String array |
| **headers** _optional_       | List of allowed headers                                               | String array |

### [](#Database%5Fconfig%5Fdelta%5Fsync)DatabaseConfigDeltaSync

 Object

| Property                              |                                                                                                           | Schema      |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------- |
| **enabled** _optional_                | Whether delta sync is enabled. **This is an enterprise-edition feature only**                             | Boolean     |
| **rev\_max\_age\_seconds** _optional_ | The number of seconds deltas for old revisions are available for. This defaults to 24 hours (in seconds). | Big Decimal |

### [](#Database%5Fconfig%5Fevent%5Fhandlers)DatabaseConfigEventHandlers

 Object

| Property                          |                                                                                                             | Schema                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **max\_processes** _optional_     | The maximum amount of concurrent event handling independent functions that can be running at the same time. | String                         |
| **wait\_for\_process** _optional_ | The maximum amount of time (in milliseconds) to wait when the even queue is full.                           | String                         |
| **document\_changed** _optional_  |                                                                                                             | [EventConfig](#Event%5Fconfig) |
| **db\_state\_changed** _optional_ |                                                                                                             | [EventConfig](#Event%5Fconfig) |

### [](#Database%5Fconfig%5Flocal%5Fjwt%5Fvalue)DatabaseConfigLocalJwtValue

 Object

| Property                        |                                                                                                                                                                                                              | Schema                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| **issuer** _required_           | The value to match against the "iss" claim of JWTs.                                                                                                                                                          | String                                                                                               |
| **register** _optional_         | If to register a new Sync Gateway user account when a user logs in with a JWT.                                                                                                                               | Boolean                                                                                              |
| **client\_id** _required_       | The value to match against the "aud" claim of JWTs. Set to an empty string to disable audience validation.                                                                                                   | String                                                                                               |
| **algorithms** _required_       | The JWT signing algorithms to accept for authentication.                                                                                                                                                     | String array                                                                                         |
| **keys** _required_             | The JSON Web Keys to use to validate JWTs.                                                                                                                                                                   | [DatabaseConfigLocalJwtValueKeysInner](#Database%5Fconfig%5Flocal%5Fjwt%5Fvalue%5Fkeys%5Finner)array |
| **disable\_session** _optional_ | Disable Sync Gateway session creation on successful JWT authentication.                                                                                                                                      | Boolean                                                                                              |
| **user\_prefix** _optional_     | This is the username prefix for all users created through this provider.                                                                                                                                     | String                                                                                               |
| **username\_claim** _optional_  | Allows a different OpenID Connect field to be specified instead of the Subject (sub). The field name to use can be specified here.                                                                           | String                                                                                               |
| **roles\_claim** _optional_     | If set, the value(s) of the given JSON Web Token claim will be added to the user's roles. The value of this claim must be either a string or an array of strings, any other type will result in an error.    | String                                                                                               |
| **channels\_claim** _optional_  | If set, the value(s) of the given JSON Web Token claim will be added to the user's channels. The value of this claim must be either a string or an array of strings, any other type will result in an error. | String                                                                                               |

### [](#Database%5Fconfig%5Flocal%5Fjwt%5Fvalue%5Fkeys%5Finner)DatabaseConfigLocalJwtValueKeysInner

 Object

| Property           |                                                                                                     | Schema |
| ------------------ | --------------------------------------------------------------------------------------------------- | ------ |
| **kty** _optional_ | The cryptographic algorithm family used with the key, such as "RSA" or "EC" **Values:** "RSA", "EC" | String |
| **use** _optional_ | The intended use of the public key. Only 'sig' is accepted. **Values:** "sig"                       | String |
| **alg** _optional_ | The algorithm intended for use with the key.                                                        | String |
| **kid** _optional_ | The Key ID, used to identify the key to use.                                                        | String |
| **crv** _optional_ | For Elliptic Curve keys, the name of the curve to use. **Values:** "P-256", "P-384", "P-521"        | String |
| **x** _optional_   | For Elliptic Curve keys, the X coordinate of the point, as a base64url string.                      | String |
| **y** _optional_   | For Elliptic Curve keys, the Y coordinate of the point, as a base64url string.                      | String |
| **n** _optional_   | For RSA keys, the modulus value of the key, as a Base64urlUInt-encoded value.                       | String |
| **e** _optional_   | For RSA keys, the exponent of the public key, as a Base64urlUInt-encoded value.                     | String |

### [](#Database%5Fconfig%5Flogging)DatabaseConfigLogging

 Object

| Property               |                                | Schema                                                                 |
| ---------------------- | ------------------------------ | ---------------------------------------------------------------------- |
| **console** _optional_ | Console logging configuration. | [DatabaseConfigLoggingConsole](#Database%5Fconfig%5Flogging%5Fconsole) |

### [](#Database%5Fconfig%5Flogging%5Fconsole)DatabaseConfigLoggingConsole

 Object

| Property                  |                                                                                                | Schema       |
| ------------------------- | ---------------------------------------------------------------------------------------------- | ------------ |
| **log\_level** _optional_ | Log Level for the console output **Values:** "none", "error", "warn", "info", "debug", "trace" | String       |
| **log\_keys** _optional_  | Log Keys for the console output                                                                | String array |

### [](#Database%5Fconfig%5Foidc)DatabaseConfigOidc

 Object

| Property                         |                                                                               | Schema      |
| -------------------------------- | ----------------------------------------------------------------------------- | ----------- |
| **providers** _optional_         | List of OpenID Connect issuers.                                               | [Map](#Map) |
| **default\_provider** _optional_ | The default provider to use when the provider is not specified in the client. | String      |

### [](#Database%5Fconfig%5Foidc%5Fproviders%5Fvalue)DatabaseConfigOidcProvidersValue

 Object

| Property                                         |                                                                                                                                                                                                                                                              | Schema       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| **issuer** _optional_                            | The URL for the OpenID Connect issuer.                                                                                                                                                                                                                       | String       |
| **register** _optional_                          | If to register a new Sync Gateway user account when a user logs in with OpenID Connect.                                                                                                                                                                      | Boolean      |
| **client\_id** _optional_                        | The OpenID Connect provider client ID.                                                                                                                                                                                                                       | String       |
| **validation\_key** _optional_                   | The OpenID Connect provider client secret.                                                                                                                                                                                                                   | String       |
| **callback\_url** _optional_                     | The URL that the OpenID Connect will redirect to after authentication. If not provided, a callback URL will be generated.                                                                                                                                    | String       |
| **disable\_session** _optional_                  | Disable Sync Gateway session creation on successful OpenID Connect authentication.                                                                                                                                                                           | Boolean      |
| **scope** _optional_                             | The scope sent for the OpenID Connect request.                                                                                                                                                                                                               | String array |
| **include\_access** _optional_                   | This is whether the \_oidc\_callback response should include the OpenID Connect access token and associated fields (such as token\_type, and expires\_in).                                                                                                   | Boolean      |
| **user\_prefix** _optional_                      | This is the username prefix for all users created through this provider.                                                                                                                                                                                     | String       |
| **discovery\_url** _optional_                    | The non-standard discovery endpoint.                                                                                                                                                                                                                         | String       |
| **disable\_cfg\_validation** _optional_          | This bypasses the configuration validation based on the OpenID Connect specifications. This may be required for some OpenID providers that don't strictly adhere to the specifications.                                                                      | Boolean      |
| **disable\_callback\_state** _optional_          | Controls whether to maintain state between the auth request and callback endpoints (/\_oidc and /\_oidc\_callback). **This is not recommended as it would cause OpenID Connect authentication to be vulnerable to Cross-Site Request Forgery (CSRF, XSRF).** | Boolean      |
| **username\_claim** _optional_                   | Allows a different OpenID Connect field to be specified instead of the Subject (sub). The field name to use can be specified here.                                                                                                                           | String       |
| **roles\_claim** _optional_                      | If set, the value(s) of the given OpenID Connect authentication token claim will be added to the user's roles. The value of this claim must be either a string or an array of strings, any other type will result in an error.                               | String       |
| **channels\_claim** _optional_                   | If set, the value(s) of the given OpenID Connect authentication token claim will be added to the user's channels. The value of this claim must be either a string or an array of strings, any other type will result in an error.                            | String       |
| **allow\_unsigned\_provider\_tokens** _optional_ | Allows users accept unsigned tokens from providers.                                                                                                                                                                                                          | Boolean      |
| **IsDefault** _optional_                         | Indicates if this is the default OpenID Connect provider.                                                                                                                                                                                                    | Boolean      |
| **Name** _optional_                              | The name of the OpenID Connect Provider.                                                                                                                                                                                                                     | String       |
| **InsecureSkipVerify** _optional_                | Determines whether the TLS certificate verification should be disabled for this provider.                                                                                                                                                                    | Boolean      |

### [](#Database%5Fconfig%5Freplications)DatabaseConfigReplications

 Object

| Property                       |                             | Schema                                                                                   |
| ------------------------------ | --------------------------- | ---------------------------------------------------------------------------------------- |
| **replication\_id** _optional_ | Properties of a replication | [UserConfigurableReplicationProperties](#User%5Fconfigurable%5Freplication%5Fproperties) |

### [](#Database%5Fconfig%5Funsupported)DatabaseConfigUnsupported

 Object

| Property                                         |                                                               | Schema                                                                                                 |
| ------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **user\_views** _optional_                       |                                                               | [DatabaseConfigUnsupportedUserViews](#Database%5Fconfig%5Funsupported%5Fuser%5Fviews)                  |
| **oidc\_test\_provider** _optional_              |                                                               | [DatabaseConfigUnsupportedOidcTestProvider](#Database%5Fconfig%5Funsupported%5Foidc%5Ftest%5Fprovider) |
| **api\_endpoints** _optional_                    |                                                               | [DatabaseConfigUnsupportedApiEndpoints](#Database%5Fconfig%5Funsupported%5Fapi%5Fendpoints)            |
| **warning\_thresholds** _optional_               |                                                               | [DatabaseConfigUnsupportedWarningThresholds](#Database%5Fconfig%5Funsupported%5Fwarning%5Fthresholds)  |
| **oidc\_tls\_skip\_verify** _optional_           | Enable self-signed certificates for OIDC testing.             | Boolean                                                                                                |
| **sgr\_tls\_skip\_verify** _optional_            | Enable self-signed certificates for SG-replicate testing.     | Boolean                                                                                                |
| **remote\_config\_tls\_skip\_verify** _optional_ | Enable self-signed certificates for external JavaScript load. | Boolean                                                                                                |
| **guest\_read\_only** _optional_                 | Restrict GUEST document access to read-only.                  | Boolean                                                                                                |
| **force\_api\_forbidden\_errors** _optional_     | Force REST API errors to return forbidden                     | Boolean                                                                                                |
| **dcp\_read\_buffer** _optional_                 | Set the dcp feed to use a different read buffer size.         | Big Decimal                                                                                            |
| **kv\_buffer** _optional_                        | Set the kv pool to use a different buffer size.               | Big Decimal                                                                                            |

### [](#Database%5Fconfig%5Funsupported%5Fapi%5Fendpoints)DatabaseConfigUnsupportedApiEndpoints

 Object

| Property                                        |                                                                                                 | Schema  |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------- |
| **enable\_couchbase\_bucket\_flush** _optional_ | **Setting for test purposes only** Whether Couchbase buckets can be flushed via Admin REST API. | Boolean |

### [](#Database%5Fconfig%5Funsupported%5Foidc%5Ftest%5Fprovider)DatabaseConfigUnsupportedOidcTestProvider

 Object

| Property               |                                                                                 | Schema  |
| ---------------------- | ------------------------------------------------------------------------------- | ------- |
| **enabled** _optional_ | Whether the oidc\_test\_provider endpoints should be exposed on the public API. | Boolean |

### [](#Database%5Fconfig%5Funsupported%5Fuser%5Fviews)DatabaseConfigUnsupportedUserViews

 Object

| Property               |                                                                  | Schema  |
| ---------------------- | ---------------------------------------------------------------- | ------- |
| **enabled** _optional_ | Whether pass-through view query is supported through public API. | Boolean |

### [](#Database%5Fconfig%5Funsupported%5Fwarning%5Fthresholds)DatabaseConfigUnsupportedWarningThresholds

 Object

| Property                                           |                                                                                                       | Schema      |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| **xattr\_size\_bytes** _optional_                  | The number of bytes to be used as a threshold for xattr size limit warnings.                          | Big Decimal |
| **channels\_per\_doc** _optional_                  | The number of channels per document to be used as a threshold for the channel count warnings.         | Big Decimal |
| **access\_and\_role\_grants\_per\_doc** _optional_ | The number of access and role grants per document to be used as a threshold for grant count warnings. | Big Decimal |
| **channels\_per\_user** _optional_                 | The number of channels per user to be used as a threshold for channel count warnings.                 | Big Decimal |
| **channel\_name\_size** _optional_                 | The number of channel name characters to be used as a threshold for channel name warnings.            | Big Decimal |

### [](#delete%5F%5Fsgcollect%5Finfo%5F200%5Fresponse)DeleteSgcollectInfo200Response

 Object

| Property              |                                    | Schema |
| --------------------- | ---------------------------------- | ------ |
| **status** _optional_ | The new status of sgcollect\_info. | String |

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

### [](#Event%5Fconfig)Event-config

 Object

| Property               |                                                                                     | Schema      |
| ---------------------- | ----------------------------------------------------------------------------------- | ----------- |
| **handler** _optional_ | The handler type. **Values:** "webhook"                                             | String      |
| **url** _optional_     | The URL of the webhook.                                                             | String      |
| **filter** _optional_  | The Javascript function to use to filter the webhook events.                        | String      |
| **timeout** _optional_ | The amount of time (in seconds) to attempt connect to the webhook before giving up. | Big Decimal |
| **options** _optional_ | The options for the event.                                                          | [Map](#Map) |

### [](#ExpVars)ExpVars

 Object

| Property                                |                                                                                 | Schema                                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **cmdline** _optional_                  | Built-in variables from the Go runtime, lists the command-line arguments        | Object                                                                                                      |
| **memstats** _optional_                 | Dumps a large amount of information about the memory heap and garbage collector | Object                                                                                                      |
| **cb** _optional_                       | Variables reported by the Couchbase SDK (go\_couchbase package)                 | Object                                                                                                      |
| **mc** _optional_                       | Variables reported by the low-level memcached API (gomemcached package)         | Object                                                                                                      |
| **syncGateway\_changeCache** _optional_ |                                                                                 | [GetExpvar200ResponseSyncGatewayChangeCache](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache) |
| **syncGateway\_db** _optional_          |                                                                                 | [GetExpvar200ResponseSyncGatewayDb](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)                   |
| **syncgateway** _optional_              | Monitoring stats                                                                | [GetExpvar200ResponseSyncgateway](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)                          |

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

### [](#get%5F%5Fall%5Fdbs%5F200%5Fresponse)GetAllDbs200Response

 Composite Schema

One of the following:

* String array
* [GetAllDbs200ResponseOneOfInner](#get%5F%5Fall%5Fdbs%5F200%5Fresponse%5FoneOf%5Finner)array

### [](#get%5F%5Fall%5Fdbs%5F200%5Fresponse%5FoneOf%5Finner)GetAllDbs200ResponseOneOfInner

 Object

| Property                          |                                                                                          | Schema  |
| --------------------------------- | ---------------------------------------------------------------------------------------- | ------- |
| **db\_name** _optional_           | The name of the database.                                                                | String  |
| **bucket** _optional_             | The Couchbase Server backing bucket for the database.                                    | String  |
| **state** _optional_              | The database state. **Values:** "Online", "Offline", "Starting", "Stopping", "Resyncing" | String  |
| **require\_resync** _optional_    | Indicates whether the database requires resync before it can be brought online.          | Boolean |
| **init\_in\_progress** _optional_ | Indicates whether database initialization is in progress.                                | Boolean |

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
| **init\_in\_progress** _optional_     | Indicates whether database initialization is in progress.                                                          | Boolean     |

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

### [](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse)GetDbViewView200Response

 Object

| Property                   |  | Schema                                                                                                   |
| -------------------------- |  | -------------------------------------------------------------------------------------------------------- |
| **total\_rows** _required_ |  | Integer                                                                                                  |
| **rows** _required_        |  | [GetDbViewView200ResponseRowsInner](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse%5Frows%5Finner)array     |
| **errors** _optional_      |  | [GetDbViewView200ResponseErrorsInner](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse%5Ferrors%5Finner)array |

### [](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse%5Ferrors%5Finner)GetDbViewView200ResponseErrorsInner

 Object

| Property              |  | Schema |
| --------------------- |  | ------ |
| **From** _optional_   |  | String |
| **Reason** _optional_ |  | String |

### [](#get%5Fdb%5F%5Fview%5Fview%5F200%5Fresponse%5Frows%5Finner)GetDbViewView200ResponseRowsInner

 Object

| Property             |  | Schema |
| -------------------- |  | ------ |
| **id** _optional_    |  | String |
| **key** _optional_   |  | Object |
| **value** _optional_ |  | Object |
| **doc** _optional_   |  | Object |

### [](#get%5F%5Fexpvar%5F200%5Fresponse)GetExpvar200Response

 Object

| Property                                |                                                                                 | Schema                                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **cmdline** _optional_                  | Built-in variables from the Go runtime, lists the command-line arguments        | Object                                                                                                      |
| **memstats** _optional_                 | Dumps a large amount of information about the memory heap and garbage collector | Object                                                                                                      |
| **cb** _optional_                       | Variables reported by the Couchbase SDK (go\_couchbase package)                 | Object                                                                                                      |
| **mc** _optional_                       | Variables reported by the low-level memcached API (gomemcached package)         | Object                                                                                                      |
| **syncGateway\_changeCache** _optional_ |                                                                                 | [GetExpvar200ResponseSyncGatewayChangeCache](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache) |
| **syncGateway\_db** _optional_          |                                                                                 | [GetExpvar200ResponseSyncGatewayDb](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)                   |
| **syncgateway** _optional_              | Monitoring stats                                                                | [GetExpvar200ResponseSyncgateway](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)                          |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache)GetExpvar200ResponseSyncGatewayChangeCache

 Object

| Property                        |                                                                      | Schema |
| ------------------------------- | -------------------------------------------------------------------- | ------ |
| **maxPending** _optional_       | Max number of sequences waiting on a missing earlier sequence number | Object |
| **lag-tap-0000ms** _optional_   | Histogram of delay from doc save till it shows up in Tap feed        | Object |
| **lag-queue-0000ms** _optional_ | Histogram of delay from Tap feed till doc is posted to changes feed  | Object |
| **lag-total-0000ms** _optional_ | Histogram of total delay from doc save till posted to changes feed   | Object |
| **outOfOrder** _optional_       | Number of out-of-order sequences posted                              | Object |
| **view\_queries** _optional_    | Number of queries to channels view                                   | Object |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)GetExpvar200ResponseSyncGatewayDb

 Object

| Property                                   |                                                                                                       | Schema |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------ |
| **channelChangesFeeds** _optional_         | Number of calls to db.changesFeed, i.e. generating a changes feed for a single channel.               | Object |
| **channelLogAdds** _optional_              | Number of entries added to channel logs                                                               | Object |
| **channelLogAppends** _optional_           | Number of times entries were written to channel logs using an APPEND operation                        | Object |
| **channelLogCacheHits** _optional_         | Number of requests for channel-logs that were fulfilled from the in-memory cache                      | Object |
| **channelLogRewrites** _optional_          | Number of times entries were written to channel logs using a SET operation (rewriting the entire log) | Object |
| **channelLogRewriteCollisions** _optional_ | Number of collisions while attempting to rewrite channel logs using SET                               | Object |
| **document\_gets** _optional_              | Number of times a document was read from the database                                                 | Object |
| **revisionCache\_adds** _optional_         | Number of revisions added to the revision cache                                                       | Object |
| **revisionCache\_hits** _optional_         | Number of times a revision-cache lookup succeeded                                                     | Object |
| **revisionCache\_misses** _optional_       | Number of times a revision-cache lookup failed                                                        | Object |
| **revs\_added** _optional_                 | Number of revisions added to the database (including deletions)                                       | Object |
| **sequence\_gets** _optional_              | Number of times the database's lastSequence was read                                                  | Object |
| **sequence\_reserves** _optional_          | Number of times the database's lastSequence was incremented                                           | Object |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)GetExpvar200ResponseSyncgateway

 Object

| Property                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema                                                                                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **global** _optional_           | Global Sync Gateway stats                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [GetExpvar200ResponseSyncgatewayGlobal](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal)                                      |
| **per\_db** _optional_          | This array contains stats for all databases declared in the config file -- see the [Sync Gateway Statistics Schema](./../stats-monitoring.html) for more details on the metrics collected and reported by Sync Gateway. The statistics for each {$db\_name} database are grouped into: cache related statistics collections statistics cbl\_replication\_push cbl\_replication\_pull database\_related\_statistics delta\_sync gsi\_views security\_related\_statistics shared\_bucket\_import per\_replication statistics for each replication\_id | [GetExpvar200ResponseSyncgatewayPerDbInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Fdb%5Finner)array                   |
| **per\_replication** _optional_ | An array of stats for each replication declared in the config file **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                                                                                                                                                                                                                                    | [GetExpvar200ResponseSyncgatewayPerReplicationInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner)array |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal)GetExpvar200ResponseSyncgatewayGlobal

 Object

| Property                             |                            | Schema                                                                                                                                        |
| ------------------------------------ | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **resource\_utilization** _optional_ | Resource utilization stats | [GetExpvar200ResponseSyncgatewayGlobalResourceUtilization](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal%5Fresource%5Futilization) |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal%5Fresource%5Futilization)GetExpvar200ResponseSyncgatewayGlobalResourceUtilization

 Object

| Property                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Schema        |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **admin\_net\_bytes\_recv** _optional_            | The total number of bytes received (since node start-up) on the network interface to which the Sync Gateway api.admin\_interface is bound.                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer       |
| **admin\_net\_bytes\_sent** _optional_            | The total number of bytes sent (since node start-up) on the network interface to which the Sync Gateway api.admin\_interface is bound.                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer       |
| **error\_count** _optional_                       | The total number of errors logged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **go\_memstats\_heapalloc** _optional_            | HeapAlloc is bytes of allocated heap objects. Allocated heap objects include all reachable objects, as well as unreachable objects that the garbage collector has not yet freed. Specifically, HeapAlloc increases as heap objects are allocated and decreases as the heap is swept and unreachable objects are freed. Sweeping occurs incrementally between GC cycles, so these two processes occur simultaneously, and as a result HeapAlloc tends to change smoothly (in contrast with the sawtooth that is typical of stop-the-world garbage collectors).                 | Integer       |
| **go\_memstats\_heapidle** _optional_             | HeapIdle is bytes in idle (unused) spans. Idle spans have no objects in them. These spans could be (and may already have been) returned to the OS, or they can be reused for heap allocations, or they can be reused as stack memory. HeapIdle minus HeapReleased estimates the amount of memory that could be returned to the OS, but is being retained by the runtime so it can grow the heap without requesting more memory from the OS. If this difference is significantly larger than the heap size, it indicates there was a recent transient spike in live heap size. | Integer       |
| **go\_memstats\_heapinuse** _optional_            | HeapInuse is bytes in in-use spans. In-use spans have at least one object in them. These spans an only be used for other objects of roughly the same size. HeapInuse minus HeapAlloc estimates the amount of memory that has been dedicated to particular size classes, but is not currently being used. This is an upper bound on fragmentation, but in general this memory can be reused efficiently.                                                                                                                                                                       | Integer       |
| **go\_memstats\_heapreleased** _optional_         | HeapReleased is bytes of physical memory returned to the OS. This counts heap memory from idle spans that was returned to the OS and has not yet been reacquired for the heap.                                                                                                                                                                                                                                                                                                                                                                                                | Integer       |
| **go\_memstats\_pausetotalns** _optional_         | PauseTotalNs is the cumulative nanoseconds in GC stop-the-world pauses since the program started. During a stop-the-world pause, all goroutines are paused and only the garbage collector can run.                                                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **go\_memstats\_stackinuse** _optional_           | StackInuse is bytes in stack spans. In-use stack spans have at least one stack in them. These spans can only be used for other stacks of the same size. There is no StackIdle because unused stack spans are returned to the heap (and hence counted toward HeapIdle).                                                                                                                                                                                                                                                                                                        | Integer       |
| **go\_memstats\_stacksys** _optional_             | StackSys is bytes of stack memory obtained from the OS. StackSys is StackInuse, plus any memory obtained directly from the OS for OS thread stacks (which should be minimal).                                                                                                                                                                                                                                                                                                                                                                                                 | Integer       |
| **go\_memstats\_sys** _optional_                  | Sys is the total bytes of memory obtained from the OS. Sys is the sum of the XSys fields below. Sys measures the virtual address space reserved by the Go runtime for the heap, stacks, and other internal data structures. It's likely that not all of the virtual address space is backed by physical memory at any given moment, though in general it all was at some point.                                                                                                                                                                                               | Integer       |
| **goroutines\_high\_watermark** _optional_        | Peak number of go routines since process start.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer       |
| **num\_goroutines** _optional_                    | The total number of goroutines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer       |
| **num\_idle\_kv\_ops** _optional_                 | The total number of idle kv operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer       |
| **process\_cpu\_percent\_utilization** _optional_ | The CPU utilization as percentage value \* 10\. The extra 10 multiplier is a mistake left for backwards compatibility. Please consider using node\_cpu\_percent\_utilization as of version 3.2\. The CPU usage calculation is performed based on user and system CPU time, but it does not include components such as iowait. The derivation means that the values of process\_cpu\_percent\_utilization and %Cpu, returned when running the top command, will differ.                                                                                                        | Float (float) |
| **node\_cpu\_percent\_utilization** _optional_    | The node CPU utilization as percentage value, since the last time this stat was called. The CPU usage calculation is performed based on user and system CPU time, but it does not include components such as iowait.                                                                                                                                                                                                                                                                                                                                                          | Float (float) |
| **process\_memory\_resident** _optional_          | The memory utilization (Resident Set Size) for the process, in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer       |
| **pub\_net\_bytes\_recv** _optional_              | The total number of bytes received (since node start-up) on the network interface to which the Sync Gateway api.public\_interface is bound. By default, that is the number of bytes received on 127.0.0.1:4984 since node start-up                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **pub\_net\_bytes\_sent** _optional_              | The total number of bytes sent (since node start-up) on the network interface to which Sync Gateway api.public\_interface is bound. By default, that is the number of bytes sent on 127.0.0.1:4984 since node start-up.                                                                                                                                                                                                                                                                                                                                                       | Integer       |
| **system\_memory\_total** _optional_              | The total memory available on the system in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **warn\_count** _optional_                        | The total number of warnings logged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer       |
| **uptime** _optional_                             | The total uptime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer       |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Fdb%5Finner)GetExpvar200ResponseSyncgatewayPerDbInner

 Object

| Property                        |  | Schema |
| ------------------------------- |  | ------ |
| **cache** _optional_            |  | Object |
| **database** _optional_         |  | Object |
| **per\_replication** _optional_ |  | Object |
| **collections** _optional_      |  | Object |
| **security** _optional_         |  | Object |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner)GetExpvar200ResponseSyncgatewayPerReplicationInner

 Object

| Property                        |  | Schema                                                                                                                                                               |
| ------------------------------- |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **$replication\_id** _optional_ |  | [GetExpvar200ResponseSyncgatewayPerReplicationInnerReplicationId](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner%5F%5Freplication%5Fid) |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner%5F%5Freplication%5Fid)GetExpvar200ResponseSyncgatewayPerReplicationInnerReplicationId

 Object

| Property                                                |                                                                                                                                                                                                                                                                                                                     | Schema  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **sgr\_active** _optional_                              | Whether the replication is active at this time. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                       | Boolean |
| **sgr\_docs\_checked\_sent** _optional_                 | The total number of documents checked for changes since replication started. This represents the number of potential change notifications pushed by Sync Gateway. **Constraints**This is not necessarily the number of documents pushed, as a given target might already have the change. Used by versions 1 and 2. | Integer |
| **sgr\_num\_attachments\_transferred** _optional_       | The total number of attachments transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                | Integer |
| **sgr\_num\_attachment\_bytes\_transferred** _optional_ | The total number of attachment bytes transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                           | Integer |
| **sgr\_num\_docs\_failed\_to\_push** _optional_         | The total number of documents that failed to be pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                         | Integer |
| **sgr\_num\_docs\_pushed** _optional_                   | The total number of documents that were pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                                 | Integer |

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

### [](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse)GetKeyspaceRawDocid200Response

 Object

| Property              |  | Schema                                                                                            |
| --------------------- |  | ------------------------------------------------------------------------------------------------- |
| **\_sync** _optional_ |  | [GetKeyspaceRawDocid200ResponseSync](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync) |

### [](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync)GetKeyspaceRawDocid200ResponseSync

 Object

| Property                             |                                                                                    | Schema                                                                                                                                                         |
| ------------------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **rev** _optional_                   | The current document revision ID.                                                  | String                                                                                                                                                         |
| **sequence** _optional_              | The most recent sequence number of the document.                                   | Big Decimal                                                                                                                                                    |
| **recent\_sequences** _optional_     | The previous sequence numbers of the document.                                     | Big Decimal array                                                                                                                                              |
| **history** _optional_               |                                                                                    | [GetKeyspaceRawDocid200ResponseSyncHistory](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fhistory)                                             |
| **cas** _optional_                   | The document CAS (Concurrent Document Mutations) number used for document locking. | String                                                                                                                                                         |
| **value\_crc32c** _optional_         | The documents CRC32 number.                                                        | String                                                                                                                                                         |
| **channel\_set** _optional_          | The channels the document has been in.                                             | [GetKeyspaceRawDocid200ResponseSyncChannelSetInner](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fchannel%5Fset%5Finner)array                  |
| **channel\_set\_history** _optional_ |                                                                                    | [GetKeyspaceRawDocid200ResponseSyncChannelSetHistoryInner](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fchannel%5Fset%5Fhistory%5Finner)array |
| **time\_saved** _optional_           | The time and date the document was most recently changed.                          | String                                                                                                                                                         |

### [](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fchannel%5Fset%5Fhistory%5Finner)GetKeyspaceRawDocid200ResponseSyncChannelSetHistoryInner

 Object

| Property             |  | Schema |
| -------------------- |  | ------ |
| **name** _optional_  |  | String |
| **start** _optional_ |  | String |
| **end** _optional_   |  | String |

### [](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fchannel%5Fset%5Finner)GetKeyspaceRawDocid200ResponseSyncChannelSetInner

 Object

| Property             |                                                                                        | Schema |
| -------------------- | -------------------------------------------------------------------------------------- | ------ |
| **name** _optional_  | The name of the channel.                                                               | String |
| **start** _optional_ | The sequence number that document was added to the channel.                            | String |
| **end** _optional_   | The sequence number the document was removed from the channel. Omitted if not removed. | String |

### [](#get%5Fkeyspace%5F%5Fraw%5Fdocid%5F200%5Fresponse%5F%5Fsync%5Fhistory)GetKeyspaceRawDocid200ResponseSyncHistory

 Object

| Property                |                                                                                                                          | Schema            |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **revs** _optional_     | The past revision IDs.                                                                                                   | String array      |
| **parents** _optional_  |                                                                                                                          | Big Decimal array |
| **channels** _optional_ | The past channel history. Can contain string arrays, strings, or be null depending on if and how the channels where set. | List array        |

### [](#get%5F%5Fsgcollect%5Finfo%5F200%5Fresponse)GetSgcollectInfo200Response

 Object

| Property              |                                                                 | Schema |
| --------------------- | --------------------------------------------------------------- | ------ |
| **status** _required_ | The status of sgcollect\_info. **Values:** "stopped", "running" | String |

### [](#get%5F%5Fstats%5F200%5Fresponse)GetStats200Response

 Object

| Property                |                                        | Schema      |
| ----------------------- | -------------------------------------- | ----------- |
| **memstats** _optional_ | A set of Go runtime memory statistics. | [Map](#Map) |

### [](#HTTP%5FError)HTTP-Error

 Object

| Property              |                        | Schema |
| --------------------- | ---------------------- | ------ |
| **error** _required_  | The error name.        | String |
| **reason** _required_ | The error description. | String |

### [](#Log%5Frotation%5Fconfig)Log-rotation-config

 Object

| Property                                  |                                                                                                                                                                                                                                                             | Schema  |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                                                                                              | Integer |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp.                                                                                                                                                                                  | Boolean |
| **rotated\_logs\_size\_limit** _optional_ | Max Size (in mb) of log files before deletion                                                                                                                                                                                                               | Integer |
| **rotation\_interval** _optional_         | If set, the interval at which log files are rotated, even if max\_size is not reached. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. By default, there is no rotation, max\_age=0.                                                                                                                                                           | Integer |

### [](#Logging-config)LoggingConfig

 Object

| Property                        |                                                                                                                                                              | Schema                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **log\_file\_path** _optional_  | Absolute or relative path on the filesystem to the log file directory. A relative path is from the directory that contains the Sync Gateway executable file. | String                                                           |
| **redaction\_level** _optional_ | Redaction level to apply to log output. **Values:** "none", "partial", "full", "unset"                                                                       | String                                                           |
| **console** _optional_          |                                                                                                                                                              | [ConsoleLoggingConfig](#Console%5Flogging%5Fconfig)              |
| **error** _optional_            | Error logging configuration.                                                                                                                                 | [StartupConfigLoggingError](#Startup%5Fconfig%5Flogging%5Ferror) |
| **warn** _optional_             | Warning logging configuration.                                                                                                                               | [StartupConfigLoggingWarn](#Startup%5Fconfig%5Flogging%5Fwarn)   |
| **info** _optional_             | Info logging configuration.                                                                                                                                  | [StartupConfigLoggingInfo](#Startup%5Fconfig%5Flogging%5Finfo)   |
| **debug** _optional_            | Debug logging configuration.                                                                                                                                 | [StartupConfigLoggingDebug](#Startup%5Fconfig%5Flogging%5Fdebug) |
| **trace** _optional_            | Trace logging configuration.                                                                                                                                 | [StartupConfigLoggingTrace](#Startup%5Fconfig%5Flogging%5Ftrace) |
| **stats** _optional_            | Trace logging configuration.                                                                                                                                 | [StartupConfigLoggingStats](#Startup%5Fconfig%5Flogging%5Fstats) |

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

### [](#post%5Fdb%5F%5Fonline%5Frequest)PostDbOnlineRequest

 Object

| Property             |                                                              | Schema  |
| -------------------- | ------------------------------------------------------------ | ------- |
| **delay** _optional_ | The amount of seconds to delay bringing the database online. | Integer |

### [](#post%5Fdb%5F%5Fresync%5Frequest)PostDbResyncRequest

 Object

| Property                             |                                                                                                                                                                                                           | Schema      |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **scopes** _optional_                | This controls for which collections resync will run                                                                                                                                                       | [Map](#Map) |
| **regenerate\_sequences** _optional_ | This can be used as an alternative to query param regenerate\_sequences. If either query param or this is set to true, then the request will regenerate the sequence numbers for each document processed. | Boolean     |

### [](#post%5Fdb%5F%5Fsession%5F200%5Fresponse)PostDbSession200Response

 Object

| Property                    |                                                                                                             | Schema |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- | ------ |
| **session\_id** _optional_  | The ID of the session. This is the value that would be put in to the cookie to keep the user authenticated. | String |
| **expires** _optional_      | The date and time the cookie expires.                                                                       | String |
| **cookie\_name** _optional_ | The name of the cookie that would be used to store the users session.                                       | String |

### [](#post%5Fdb%5F%5Fsession%5Frequest)PostDbSessionRequest

 Object

| Property            |                                                                               | Schema  |
| ------------------- | ----------------------------------------------------------------------------- | ------- |
| **name** _optional_ | User name to generate the session for.                                        | String  |
| **ttl** _optional_  | Time until the session expires. Uses default value of 24 hours if left blank. | Integer |

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

| Property                     |                                                                                                                                                                                                                                                                                                                                                                                                                            | Schema |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **limit** _optional_         | Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                       | String |
| **style** _optional_         | Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                                                                | String |
| **active\_only** _optional_  | Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                              | String |
| **include\_docs** _optional_ | Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                            | String |
| **revocations** _optional_   | If true, revocation messages will be sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                             | String |
| **filter** _optional_        | Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                                                                 | String |
| **channels** _optional_      | A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                        | String |
| **doc\_ids** _optional_      | A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal.                                                                                                                                                                                                   | String |
| **heartbeat** _optional_     | The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This will override any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the server replication configuration. | String |
| **timeout** _optional_       | This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                                               | String |
| **feed** _optional_          | The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                                                           | String |
| **request\_plus** _optional_ | When true, ensures all valid documents written prior to the request being issued are included in the response. This is only applicable for non-continuous feeds.                                                                                                                                                                                                                                                           | String |

### [](#post%5Fkeyspace%5F%5Fpurge%5F200%5Fresponse)PostKeyspacePurge200Response

 Object

| Property              |                | Schema      |
| --------------------- | -------------- | ----------- |
| **purged** _required_ | **Values:** \* | [Map](#Map) |

### [](#post%5Fkeyspace%5F%5Fpurge%5Frequest)PostKeyspacePurgeRequest

 Object

| Property               |                                                                                                                                                     | Schema       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **doc\_id** _optional_ | The document ID to purge. The array must only be 1 element which is \*. All revisions will be permanently removed for that document. **Values:** \* | String array |
| _additionalproperty_   | **Values:** \*                                                                                                                                      | String array |

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

### [](#post%5F%5Fpost%5Fupgrade%5F200%5Fresponse)PostPostUpgrade200Response

 Object

| Property                              |                                                                                                                                          | Schema      |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **post\_upgrade\_results** _required_ | A map of databases.                                                                                                                      | [Map](#Map) |
| **preview** _optional_                | If set, nothing in the database was changed as this was a dry-run. This can be controlled by the preview query parameter in the request. | Boolean     |

### [](#post%5F%5Fpost%5Fupgrade%5F200%5Fresponse%5Fpost%5Fupgrade%5Fresults%5Fvalue)PostPostUpgrade200ResponsePostUpgradeResultsValue

 Object

| Property                             |                                                    | Schema       |
| ------------------------------------ | -------------------------------------------------- | ------------ |
| **removed\_design\_docs** _required_ | The design documents that have or will be removed. | String array |
| **removed\_indexes** _required_      | The indexes that have or will be removed.          | String array |

### [](#post%5F%5Fprofile%5Fprofilename%5Frequest)PostProfileProfilenameRequest

 Object

| Property            |                                                  | Schema |
| ------------------- | ------------------------------------------------ | ------ |
| **file** _optional_ | This is the file to output the pprof profile at. | String |

### [](#post%5F%5Fsgcollect%5Finfo%5F200%5Fresponse)PostSgcollectInfo200Response

 Object

| Property              |                                 | Schema |
| --------------------- | ------------------------------- | ------ |
| **status** _optional_ | The new sgcollect\_info status. | String |

### [](#post%5F%5Fsgcollect%5Finfo%5Frequest)PostSgcollectInfoRequest

 Object

| Property                     |                                                                                                                                                                          | Schema  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| **redact\_level** _optional_ | The redaction level to use for redacting the collected logs. **Values:** "partial", "none"                                                                               | String  |
| **redact\_salt** _optional_  | The salt to use for the log redactions.                                                                                                                                  | String  |
| **output\_dir** _optional_   | The directory to output the collected logs zip file at. This overrides the configured default output directory configured in the startup config logging.log\_file\_path. | String  |
| **upload** _optional_        | If set, upload the logs to Couchbase Support. A customer name must be set if this is set.                                                                                | Boolean |
| **upload\_host** _optional_  | The host to send the logs too.                                                                                                                                           | String  |
| **upload\_proxy** _optional_ | The proxy to use while uploading the logs.                                                                                                                               | String  |
| **customer** _optional_      | The customer name to use when uploading the logs.                                                                                                                        | String  |
| **ticket** _optional_        | The Zendesk ticket number to use when uploading logs. **Minimum length:** 1 **Maximum length:** 7                                                                        | String  |

### [](#put%5Fkeyspace%5F%5Flocal%5Fdocid%5Frequest)PutKeyspaceLocalDocidRequest

 Object

| Property             |                                                                    | Schema |
| -------------------- | ------------------------------------------------------------------ | ------ |
| **\_rev** _optional_ | Revision to replace. Required if updating existing local document. | String |

### [](#Replication)User configurable replication properties

 Object

| Property                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Schema       |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **replication\_id** _optional_            | This is the ID of the replication. When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set. When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String       |
| **remote** _optional_                     | This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's push, pull, or pushAndPull action. Typically this would include the URI, port, and database name. For example, http://localhost:4985/db. How this remote is used depends on the direction of the replication: pull \- this replicator _pulls_ changes from the remote push \- this replicator _pushes_ changes to this remote pushAndPull \- this replicator _pushes_ changes to this remote, while also pulling receiving changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String       |
| **username** _optional_                   | **This has been deprecated in favour of remote\_username.** This is the username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **password** _optional_                   | **This has been deprecated in favour of remote\_password.** This is the password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String       |
| **remote\_username** _optional_           | The username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |
| **remote\_password** _optional_           | The password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String       |
| **direction** _required_                  | This specifies which direction the replication will be replicating with the remote replicator. The directions are: pull \- changes are pulled from the remote database push \- changes are pushed to the remote database pushAndPull \- changes are both push-to and pulled-from the remote database Replications created prior to Sync Gateway 2.8 derive their direction from the source/target URL of the replication. **Values:** "push", "pull", "pushAndPull"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String       |
| **conflict\_resolution\_type** _optional_ | This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions. Changing this is an enterprise-edition only feature. **Behaviour** _default_ \- In priority order, this will cause Deletes to always win (the delete with the longest revision history wins if both revisions are deletes) The revision with the longest revision history to win. This means the the revision with the most changes and therefore the highest revision ID will win. _localWins_ \- This will result in local revisions always being the winner in any conflict. _remoteWins_ \- This will result in remote revisions always being the winner in any conflict. _custom_ \- This will result in conflicts going through your own custom conflict resolver. You must provide this logic as a Javascript function in the custom\_conflict\_resolver parameter. This is an enterprise-edition only feature. Note: replications created prior to Sync Gateway 2.8 will default to default. **Values:** "default", "remoteWins", "localWins", "custom"                                                                                                               | String       |
| **custom\_conflict\_resolver** _optional_ | This specifies the Javascript function to use to resolve conflicts between conflicting revisions. This **must** be used when conflict\_resolution\_type=custom. This property will be ignored when conflict\_resolution\_type is not custom. The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties: LocalDocument \- The local document. This contains the document ID under the \_id key. RemoteDocument \- The remote document The function should return the new documents body. This can be the winning revision (for example, return conflict.LocalDocument), a new body, or nil to resolve as a delete. Example: "custom\_conflict\_resolver":\\\` 	function(conflict) { 		console.log("Doc ID: "+conflict.LocalDocument.\_id); 		console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument)); 		return conflict.RemoteDocument; 	} \\\` Using complex custom\_conflict\_resolver functions can noticeably degrade performance. Use a built-in resolver whenever possible. This is an enterprise-edition only feature. | String       |
| **purge\_on\_removal** _optional_         | Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote. If false, documents will not be replicated and not be purged when the user loses access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean      |
| **enable\_delta\_sync** _optional_        | This will turn on delta- sync for the replication. This works in conjunction with the database level setting delta\_sync.enabled If set to true, delta-sync will be used as long as both databases involved in the replication have delta-sync enabled. If a database does not have delta-sync enabled, then the replication will run without delta-sync. Replications created prior to Sync Gateway 2.8 must have delta-sync disabled. Enabling this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean      |
| **max\_backoff\_time** _optional_         | Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote. When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every max\_backoff\_time minutes. If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication. Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer      |
| **initial\_state** _optional_             | This is what state to start the replication in when creating a new replication. This allows you to control if the replication starts in a stopped start or running state. Replications prior to Sync Gateway 2.8 will run in the default state running. **Values:** "running", "stopped"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | String       |
| **continuous** _optional_                 | If true, changes will be immediately synced when they happen. This is known as a continuous replication. If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean      |
| **filter** _optional_                     | This defines whether to filter documents by their channels or not. If set to sync\_gateway/bychannel then a **pull** replication will be limited to a specific set of channels specified by the query\_params.channels property. This only can be used with pull replications. **Values:** "sync\_gateway/bychannel"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String       |
| **query\_params** _optional_              | This is a set of key/value pairs used in the query string of the replication. If filters=sync\_gateway/bychannel then this can be used to set the channels to filter by in a pull replication. To do this, set the channels key to a string array of the channels to filter by. For example: "filter":"sync\_gateway/bychannel", "query\_params": {   "channels":\["chanUser1"\] },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String array |
| **adhoc** _optional_                      | Set to true to run the replication as an adhoc replication instead of a persistent one. This means that the replication will only last the period of the replication until the status is changed to stopped and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean      |
| **batch\_size** _optional_                | The amount of changes to be sent in one batch of replications. Changing this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer      |
| **run\_as** _optional_                    | This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | String       |
| **collections\_enabled** _optional_       | If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by keyspace\_map. If false, the replicator will only replicate the default collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean      |
| **collections\_local** _optional_         | Limits the set of collections replicated to those listed in this array. The replication will use all collections defined on the database if this list is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String array |
| **collections\_remote** _optional_        | Remaps the local collection name to the one specified in this array when replicating with the remote. If only a subset of collections need remapping, elements in this array can be specified as null to preserve the local collection name. The same index is used for both collections\_remote and collections\_local, and both arrays must be the same length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String array |

### [](#Replication%5F1)Replication

 Object

| Property                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Schema       |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **replication\_id** _optional_            | This is the ID of the replication. When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set. When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String       |
| **remote** _optional_                     | This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's push, pull, or pushAndPull action. Typically this would include the URI, port, and database name. For example, http://localhost:4985/db. How this remote is used depends on the direction of the replication: pull \- this replicator _pulls_ changes from the remote push \- this replicator _pushes_ changes to this remote pushAndPull \- this replicator _pushes_ changes to this remote, while also pulling receiving changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String       |
| **username** _optional_                   | **This has been deprecated in favour of remote\_username.** This is the username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **password** _optional_                   | **This has been deprecated in favour of remote\_password.** This is the password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String       |
| **remote\_username** _optional_           | The username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |
| **remote\_password** _optional_           | The password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String       |
| **direction** _optional_                  | This specifies which direction the replication will be replicating with the remote replicator. The directions are: pull \- changes are pulled from the remote database push \- changes are pushed to the remote database pushAndPull \- changes are both push-to and pulled-from the remote database Replications created prior to Sync Gateway 2.8 derive their direction from the source/target URL of the replication. **Values:** "push", "pull", "pushAndPull"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String       |
| **conflict\_resolution\_type** _optional_ | This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions. Changing this is an enterprise-edition only feature. **Behaviour** _default_ \- In priority order, this will cause Deletes to always win (the delete with the longest revision history wins if both revisions are deletes) The revision with the longest revision history to win. This means the the revision with the most changes and therefore the highest revision ID will win. _localWins_ \- This will result in local revisions always being the winner in any conflict. _remoteWins_ \- This will result in remote revisions always being the winner in any conflict. _custom_ \- This will result in conflicts going through your own custom conflict resolver. You must provide this logic as a Javascript function in the custom\_conflict\_resolver parameter. This is an enterprise-edition only feature. Note: replications created prior to Sync Gateway 2.8 will default to default. **Values:** "default", "remoteWins", "localWins", "custom"                                                                                                               | String       |
| **custom\_conflict\_resolver** _optional_ | This specifies the Javascript function to use to resolve conflicts between conflicting revisions. This **must** be used when conflict\_resolution\_type=custom. This property will be ignored when conflict\_resolution\_type is not custom. The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties: LocalDocument \- The local document. This contains the document ID under the \_id key. RemoteDocument \- The remote document The function should return the new documents body. This can be the winning revision (for example, return conflict.LocalDocument), a new body, or nil to resolve as a delete. Example: "custom\_conflict\_resolver":\\\` 	function(conflict) { 		console.log("Doc ID: "+conflict.LocalDocument.\_id); 		console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument)); 		return conflict.RemoteDocument; 	} \\\` Using complex custom\_conflict\_resolver functions can noticeably degrade performance. Use a built-in resolver whenever possible. This is an enterprise-edition only feature. | String       |
| **purge\_on\_removal** _optional_         | Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote. If false, documents will not be replicated and not be purged when the user loses access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean      |
| **enable\_delta\_sync** _optional_        | This will turn on delta- sync for the replication. This works in conjunction with the database level setting delta\_sync.enabled If set to true, delta-sync will be used as long as both databases involved in the replication have delta-sync enabled. If a database does not have delta-sync enabled, then the replication will run without delta-sync. Replications created prior to Sync Gateway 2.8 must have delta-sync disabled. Enabling this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean      |
| **max\_backoff\_time** _optional_         | Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote. When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every max\_backoff\_time minutes. If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication. Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer      |
| **initial\_state** _optional_             | This is what state to start the replication in when creating a new replication. This allows you to control if the replication starts in a stopped start or running state. Replications prior to Sync Gateway 2.8 will run in the default state running. **Values:** "running", "stopped"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | String       |
| **continuous** _optional_                 | If true, changes will be immediately synced when they happen. This is known as a continuous replication. If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean      |
| **filter** _optional_                     | This defines whether to filter documents by their channels or not. If set to sync\_gateway/bychannel then a **pull** replication will be limited to a specific set of channels specified by the query\_params.channels property. This only can be used with pull replications. **Values:** "sync\_gateway/bychannel"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String       |
| **query\_params** _optional_              | This is a set of key/value pairs used in the query string of the replication. If filters=sync\_gateway/bychannel then this can be used to set the channels to filter by in a pull replication. To do this, set the channels key to a string array of the channels to filter by. For example: "filter":"sync\_gateway/bychannel", "query\_params": {   "channels":\["chanUser1"\] },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String array |
| **adhoc** _optional_                      | Set to true to run the replication as an adhoc replication instead of a persistent one. This means that the replication will only last the period of the replication until the status is changed to stopped and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean      |
| **batch\_size** _optional_                | The amount of changes to be sent in one batch of replications. Changing this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer      |
| **run\_as** _optional_                    | This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | String       |
| **collections\_enabled** _optional_       | If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by keyspace\_map. If false, the replicator will only replicate the default collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean      |
| **collections\_local** _optional_         | Limits the set of collections replicated to those listed in this array. The replication will use all collections defined on the database if this list is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String array |
| **collections\_remote** _optional_        | Remaps the local collection name to the one specified in this array when replicating with the remote. If only a subset of collections need remapping, elements in this array can be specified as null to preserve the local collection name. The same index is used for both collections\_remote and collections\_local, and both arrays must be the same length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String array |
| **assigned\_node** _optional_             | The unique ID of the node assigned to the replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **target\_state** _optional_              | This is the state that the replicator is in or that trying to transition in to. **Values:** "running", "stopped", "resetting", "error", "starting", "reconnecting"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |

### [](#Replication%5Fstatus)Replication-status

 Object

| Property                              |                                                                                                                                                 | Schema                                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **replication\_id** _required_        | The ID of the replication.                                                                                                                      | String                                                                                   |
| **config** _optional_                 | Properties of a replication                                                                                                                     | [UserConfigurableReplicationProperties](#User%5Fconfigurable%5Freplication%5Fproperties) |
| **status** _optional_                 | The status of the replication. **Values:** "stopped", "running", "reconnecting", "resetting", "error", "starting"                               | String                                                                                   |
| **error\_message** _optional_         | The error message of the replication if an error has occurred.                                                                                  | String                                                                                   |
| **docs\_read** _optional_             | The number of documents that have been read (fetched) from the source database.                                                                 | Integer                                                                                  |
| **docs\_checked\_pull** _optional_    |                                                                                                                                                 | Integer                                                                                  |
| **docs\_purged** _optional_           | The number of documents that have been purged.                                                                                                  | Integer                                                                                  |
| **rejected\_by\_local** _optional_    | The number of documents that were received by the local but did not get replicated due to getting rejected by the sync function on the local.   | Integer                                                                                  |
| **last\_seq\_pull** _optional_        | The last changes sequence number that was pulled from the remote.                                                                               | String                                                                                   |
| **deltas\_recv** _optional_           | The number of deltas that have been received from the remote.                                                                                   | Integer                                                                                  |
| **deltas\_requested** _optional_      |                                                                                                                                                 | Integer                                                                                  |
| **docs\_written** _optional_          | The number of documents that have been wrote (pushed) to the target database.                                                                   | Integer                                                                                  |
| **docs\_checked\_push** _optional_    |                                                                                                                                                 | Integer                                                                                  |
| **docs\_write\_failures** _optional_  | The number of documents that have failed to be wrote (pushed) to the target database. There will be no attempt to try to push these docs again. | Integer                                                                                  |
| **docs\_write\_conflicts** _optional_ | The number of documents that had a conflict.                                                                                                    | Integer                                                                                  |
| **rejected\_by\_remote** _optional_   | The number of documents that were received by the remote but did not get replicated due to getting rejected by the sync function on the remote. | Integer                                                                                  |
| **last\_seq\_push** _optional_        | The last changes sequence number that was pushed to the remote.                                                                                 | String                                                                                   |
| **deltas\_sent** _optional_           | The number of deltas that have been sent to the remote.                                                                                         | Integer                                                                                  |

### [](#Resync%5Fstatus)Resync-status

 Object

| Property                               |                                                                                                         | Schema      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| **status** _required_                  | The status of the current operation. **Values:** "running", "completed", "stopping", "stopped", "error" | String      |
| **start\_time** _required_             | The ISO-8601 date and time the resync operation was started.                                            | String      |
| **last\_error** _required_             | The last error that occurred in the resync operation (if any).                                          | String      |
| **docs\_changed** _required_           | The amount of documents that have been changed as a result of the resync operation.                     | Integer     |
| **docs\_processed** _required_         | The amount of docs that have been processed so far in the resync operation.                             | Integer     |
| **collections\_processing** _optional_ | The collections that the resync operation is running on.                                                | [Map](#Map) |

### [](#Retrieved-replication)Replication

 Object

| Property                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Schema       |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **replication\_id** _optional_            | This is the ID of the replication. When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set. When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String       |
| **remote** _optional_                     | This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's push, pull, or pushAndPull action. Typically this would include the URI, port, and database name. For example, http://localhost:4985/db. How this remote is used depends on the direction of the replication: pull \- this replicator _pulls_ changes from the remote push \- this replicator _pushes_ changes to this remote pushAndPull \- this replicator _pushes_ changes to this remote, while also pulling receiving changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String       |
| **username** _optional_                   | **This has been deprecated in favour of remote\_username.** This is the username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **password** _optional_                   | **This has been deprecated in favour of remote\_password.** This is the password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String       |
| **remote\_username** _optional_           | The username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |
| **remote\_password** _optional_           | The password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String       |
| **direction** _optional_                  | This specifies which direction the replication will be replicating with the remote replicator. The directions are: pull \- changes are pulled from the remote database push \- changes are pushed to the remote database pushAndPull \- changes are both push-to and pulled-from the remote database Replications created prior to Sync Gateway 2.8 derive their direction from the source/target URL of the replication. **Values:** "push", "pull", "pushAndPull"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String       |
| **conflict\_resolution\_type** _optional_ | This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions. Changing this is an enterprise-edition only feature. **Behaviour** _default_ \- In priority order, this will cause Deletes to always win (the delete with the longest revision history wins if both revisions are deletes) The revision with the longest revision history to win. This means the the revision with the most changes and therefore the highest revision ID will win. _localWins_ \- This will result in local revisions always being the winner in any conflict. _remoteWins_ \- This will result in remote revisions always being the winner in any conflict. _custom_ \- This will result in conflicts going through your own custom conflict resolver. You must provide this logic as a Javascript function in the custom\_conflict\_resolver parameter. This is an enterprise-edition only feature. Note: replications created prior to Sync Gateway 2.8 will default to default. **Values:** "default", "remoteWins", "localWins", "custom"                                                                                                               | String       |
| **custom\_conflict\_resolver** _optional_ | This specifies the Javascript function to use to resolve conflicts between conflicting revisions. This **must** be used when conflict\_resolution\_type=custom. This property will be ignored when conflict\_resolution\_type is not custom. The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties: LocalDocument \- The local document. This contains the document ID under the \_id key. RemoteDocument \- The remote document The function should return the new documents body. This can be the winning revision (for example, return conflict.LocalDocument), a new body, or nil to resolve as a delete. Example: "custom\_conflict\_resolver":\\\` 	function(conflict) { 		console.log("Doc ID: "+conflict.LocalDocument.\_id); 		console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument)); 		return conflict.RemoteDocument; 	} \\\` Using complex custom\_conflict\_resolver functions can noticeably degrade performance. Use a built-in resolver whenever possible. This is an enterprise-edition only feature. | String       |
| **purge\_on\_removal** _optional_         | Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote. If false, documents will not be replicated and not be purged when the user loses access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean      |
| **enable\_delta\_sync** _optional_        | This will turn on delta- sync for the replication. This works in conjunction with the database level setting delta\_sync.enabled If set to true, delta-sync will be used as long as both databases involved in the replication have delta-sync enabled. If a database does not have delta-sync enabled, then the replication will run without delta-sync. Replications created prior to Sync Gateway 2.8 must have delta-sync disabled. Enabling this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean      |
| **max\_backoff\_time** _optional_         | Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote. When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every max\_backoff\_time minutes. If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication. Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer      |
| **initial\_state** _optional_             | This is what state to start the replication in when creating a new replication. This allows you to control if the replication starts in a stopped start or running state. Replications prior to Sync Gateway 2.8 will run in the default state running. **Values:** "running", "stopped"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | String       |
| **continuous** _optional_                 | If true, changes will be immediately synced when they happen. This is known as a continuous replication. If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean      |
| **filter** _optional_                     | This defines whether to filter documents by their channels or not. If set to sync\_gateway/bychannel then a **pull** replication will be limited to a specific set of channels specified by the query\_params.channels property. This only can be used with pull replications. **Values:** "sync\_gateway/bychannel"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String       |
| **query\_params** _optional_              | This is a set of key/value pairs used in the query string of the replication. If filters=sync\_gateway/bychannel then this can be used to set the channels to filter by in a pull replication. To do this, set the channels key to a string array of the channels to filter by. For example: "filter":"sync\_gateway/bychannel", "query\_params": {   "channels":\["chanUser1"\] },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String array |
| **adhoc** _optional_                      | Set to true to run the replication as an adhoc replication instead of a persistent one. This means that the replication will only last the period of the replication until the status is changed to stopped and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean      |
| **batch\_size** _optional_                | The amount of changes to be sent in one batch of replications. Changing this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer      |
| **run\_as** _optional_                    | This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | String       |
| **collections\_enabled** _optional_       | If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by keyspace\_map. If false, the replicator will only replicate the default collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean      |
| **collections\_local** _optional_         | Limits the set of collections replicated to those listed in this array. The replication will use all collections defined on the database if this list is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String array |
| **collections\_remote** _optional_        | Remaps the local collection name to the one specified in this array when replicating with the remote. If only a subset of collections need remapping, elements in this array can be specified as null to preserve the local collection name. The same index is used for both collections\_remote and collections\_local, and both arrays must be the same length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String array |
| **assigned\_node** _optional_             | The unique ID of the node assigned to the replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **target\_state** _optional_              | This is the state that the replicator is in or that trying to transition in to. **Values:** "running", "stopped", "resetting", "error", "starting", "reconnecting"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |

### [](#Role)Role

 Object

| Property                          |                                                                                                                                                                             | Schema       |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **name** _optional_               | The name of the role. Role names can only have alphanumeric ASCII characters and underscores.                                                                               | String       |
| **admin\_channels** _optional_    | The channels that users in the role are able to access for the default collection.                                                                                          | String array |
| **all\_channels** _optional_      | The channels that the role grants access to for the default collection. These channels could have been assigned by the Sync function or using the admin\_channels property. | String array |
| **collection\_access** _optional_ | A set of access grants by scope and collection.                                                                                                                             | [Map](#Map)  |

### [](#Role%5F1)Role

 Object

| Property                          |                                                                                                                                                                             | Schema       |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **name** _optional_               | The name of the role. Role names can only have alphanumeric ASCII characters and underscores.                                                                               | String       |
| **admin\_channels** _optional_    | The channels that users in the role are able to access for the default collection.                                                                                          | String array |
| **all\_channels** _optional_      | The channels that the role grants access to for the default collection. These channels could have been assigned by the Sync function or using the admin\_channels property. | String array |
| **collection\_access** _optional_ | A set of access grants by scope and collection.                                                                                                                             | [Map](#Map)  |

### [](#Role%5F2)Role

 Object

| Property                          |                                                                                                                                                                             | Schema       |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **name** _optional_               | The name of the role. Role names can only have alphanumeric ASCII characters and underscores.                                                                               | String       |
| **admin\_channels** _optional_    | The channels that users in the role are able to access for the default collection.                                                                                          | String array |
| **all\_channels** _optional_      | The channels that the role grants access to for the default collection. These channels could have been assigned by the Sync function or using the admin\_channels property. | String array |
| **collection\_access** _optional_ | A set of access grants by scope and collection.                                                                                                                             | [Map](#Map)  |

### [](#Runtime%5Fconfig)Runtime-config

 Object

| Property                                     |                                                                                                       | Schema                                              |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **logging** _optional_                       |                                                                                                       | [RuntimeConfigLogging](#Runtime%5Fconfig%5Flogging) |
| **max\_concurrent\_replications** _optional_ | Maximum number of concurrent replication connections allowed. If set to 0 this limit will be ignored. | Integer                                             |

### [](#Runtime%5Fconfig%5Flogging)RuntimeConfigLogging

 Object

| Property                        |                                                                                                                                                              | Schema                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **log\_file\_path** _optional_  | Absolute or relative path on the filesystem to the log file directory. A relative path is from the directory that contains the Sync Gateway executable file. | String                                                           |
| **redaction\_level** _optional_ | Redaction level to apply to log output. **Values:** "none", "partial", "full", "unset"                                                                       | String                                                           |
| **console** _optional_          |                                                                                                                                                              | [ConsoleLoggingConfig](#Console%5Flogging%5Fconfig)              |
| **error** _optional_            | Error logging configuration.                                                                                                                                 | [StartupConfigLoggingError](#Startup%5Fconfig%5Flogging%5Ferror) |
| **warn** _optional_             | Warning logging configuration.                                                                                                                               | [StartupConfigLoggingWarn](#Startup%5Fconfig%5Flogging%5Fwarn)   |
| **info** _optional_             | Info logging configuration.                                                                                                                                  | [StartupConfigLoggingInfo](#Startup%5Fconfig%5Flogging%5Finfo)   |
| **debug** _optional_            | Debug logging configuration.                                                                                                                                 | [StartupConfigLoggingDebug](#Startup%5Fconfig%5Flogging%5Fdebug) |
| **trace** _optional_            | Trace logging configuration.                                                                                                                                 | [StartupConfigLoggingTrace](#Startup%5Fconfig%5Flogging%5Ftrace) |
| **stats** _optional_            | Trace logging configuration.                                                                                                                                 | [StartupConfigLoggingStats](#Startup%5Fconfig%5Flogging%5Fstats) |

### [](#Scopes)Scopes

 Object

| Property                   |                                                                                   | Schema      |
| -------------------------- | --------------------------------------------------------------------------------- | ----------- |
| **collections** _optional_ | An object keyed by collection name containing config for the specific collection. | [Map](#Map) |

### [](#Scopes%5F1)Scopes

 Object

| Property                   |                                                                                   | Schema      |
| -------------------------- | --------------------------------------------------------------------------------- | ----------- |
| **collections** _optional_ | An object keyed by collection name containing config for the specific collection. | [Map](#Map) |

### [](#Serverless)Serverless

 Object

| Property                                    |                                                                                                                                                                                                                                                                                                                                                             | Schema  |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **enabled** _optional_                      | Run SG in to serverless mode                                                                                                                                                                                                                                                                                                                                | Boolean |
| **min\_config\_fetch\_interval** _optional_ | How long database configs should be kept for in Sync Gateway before refreshing. Set to 0 to fetch configs everytime. This is used for requested databases that SG does not know about. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |

### [](#Startup%5Fconfig)Startup-config

 Object

| Property                                            |                                                                                                                                           | Schema                                                      |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **bootstrap** _optional_                            | Configuration settings for interacting with Couchbase Server.                                                                             | [StartupConfigBootstrap](#Startup%5Fconfig%5Fbootstrap)     |
| **api** _optional_                                  | Configuration settings for modifying how the REST API is interacted with.                                                                 | [StartupConfigApi](#Startup%5Fconfig%5Fapi)                 |
| **logging** _optional_                              | The configuration settings for modifying Sync Gateway logging.                                                                            | [StartupConfigLogging](#Startup%5Fconfig%5Flogging)         |
| **auth** _optional_                                 |                                                                                                                                           | [StartupConfigAuth](#Startup%5Fconfig%5Fauth)               |
| **replicator** _optional_                           |                                                                                                                                           | [StartupConfigReplicator](#Startup%5Fconfig%5Freplicator)   |
| **unsupported** _optional_                          | Settings that are not officially supported. It is highly recommended these are **not** used.                                              | [StartupConfigUnsupported](#Startup%5Fconfig%5Funsupported) |
| **database\_credentials** _optional_                | A map of database name to credentials, that can be used instead of the bootstrap ones.                                                    | [Map](#Map)                                                 |
| **bucket\_credentials** _optional_                  | A map of bucket names to credentials, that can be used instead of the bootstrap ones.                                                     | [Map](#Map)                                                 |
| **max\_file\_descriptors** _optional_               | Max of open file descriptors (RLIMIT\_NOFILE) **Minimum:** 0                                                                              | Big Decimal                                                 |
| **couchbase\_keepalive\_interval** _optional_       | TCP keep-alive interval between SG and Couchbase server. This is unused.                                                                  | Integer                                                     |
| **heap\_profile\_collection\_threshold** _optional_ | Threshold in bytes for automatic collection of heap profiles. If not specified, defaults to 85% of the lesser of cgroup or system memory. | Integer                                                     |
| **heap\_profile\_disable\_collection** _optional_   | Disables automatic heap profile collection.                                                                                               | Boolean                                                     |

### [](#Startup%5Fconfig%5Fapi)StartupConfigApi

 Object

| Property                                          |                                                                                                                                                                                                                                                            | Schema                                                   |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **public\_interface** _optional_                  | Network interface to bind public API to                                                                                                                                                                                                                    | String                                                   |
| **admin\_interface** _optional_                   | Network interface to bind admin API to. By default, this will only be accessible to the localhost.                                                                                                                                                         | String                                                   |
| **metrics\_interface** _optional_                 | Network interface to bind metrics API to. By default, this will only be accessible to the localhost.                                                                                                                                                       | String                                                   |
| **profile\_interface** _optional_                 | Network interface to bind profiling API to                                                                                                                                                                                                                 | String                                                   |
| **admin\_interface\_authentication** _optional_   | Whether the admin API requires authentication                                                                                                                                                                                                              | Boolean                                                  |
| **metrics\_interface\_authentication** _optional_ | Whether the metrics API requires authentication                                                                                                                                                                                                            | Boolean                                                  |
| **enable\_advanced\_auth\_dp** _optional_         | Whether to enable the DP permissions check feature of admin auth. Defaults to true if using enterprise-edition or false if using community-edition.                                                                                                        | Boolean                                                  |
| **server\_read\_timeout** _optional_              | Maximum duration before timing out read of the HTTP(S) request. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s.                       | String                                                   |
| **server\_write\_timeout** _optional_             | Maximum duration before timing out write of the HTTP(S) response. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s.                     | String                                                   |
| **read\_header\_timeout** _optional_              | The amount of time allowed to read request headers. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s.                                   | String                                                   |
| **idle\_timeout** _optional_                      | The maximum amount of time to wait for the next request when keep-alives are enabled. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String                                                   |
| **pretty** _optional_                             | Pretty-print JSON responses. This property is deprecated.                                                                                                                                                                                                  | Boolean                                                  |
| **max\_connections** _optional_                   | Max of incoming HTTP connections to accept                                                                                                                                                                                                                 | Big Decimal                                              |
| **compress\_responses** _optional_                | If false, disables compression of HTTP responses                                                                                                                                                                                                           | Boolean                                                  |
| **hide\_product\_version** _optional_             | Whether product versions removed from Server headers and REST API responses                                                                                                                                                                                | Boolean                                                  |
| **https** _optional_                              |                                                                                                                                                                                                                                                            | [StartupConfigApiHttps](#Startup%5Fconfig%5Fapi%5Fhttps) |
| **cors** _optional_                               |                                                                                                                                                                                                                                                            | [StartupConfigApiCors](#Startup%5Fconfig%5Fapi%5Fcors)   |

### [](#Startup%5Fconfig%5Fapi%5Fcors)StartupConfigApiCors

 Object

| Property                     |                                                                       | Schema       |
| ---------------------------- | --------------------------------------------------------------------- | ------------ |
| **origin** _optional_        | List of allowed origins, use \['\*'\] to allow access from everywhere | String array |
| **login\_origin** _optional_ | List of allowed login origins                                         | String array |
| **headers** _optional_       | List of allowed headers                                               | String array |
| **max\_age** _optional_      | Maximum age of the CORS Options request                               | Integer      |

### [](#Startup%5Fconfig%5Fapi%5Fhttps)StartupConfigApiHttps

 Object

| Property                             |                                                     | Schema |
| ------------------------------------ | --------------------------------------------------- | ------ |
| **tls\_minimum\_version** _optional_ | The minimum allowable TLS version for the REST APIs | String |
| **tls\_cert\_path** _optional_       | The TLS cert file to use for the REST APIs          | String |
| **tls\_key\_path** _optional_        | The TLS key file to use for the REST APIs           | String |

### [](#Startup%5Fconfig%5Fauth)StartupConfigAuth

 Object

| Property                    |                                                                        | Schema  |
| --------------------------- | ---------------------------------------------------------------------- | ------- |
| **bcrypt\_cost** _optional_ | Cost to use for bcrypt password hashes **Minimum:** 10 **Maximum:** 31 | Integer |

### [](#Startup%5Fconfig%5Fbootstrap)StartupConfigBootstrap

 Object

| Property                                 |                                                                                                                                                                                                                                 | Schema  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **group\_id** _optional_                 | The config group ID to use when discovering databases. Allows for non-homogenous configuration.                                                                                                                                 | String  |
| **config\_update\_frequency** _optional_ | How often to poll Couchbase Server for new config changes. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |
| **server** _required_                    | Couchbase Server connection string/URL.                                                                                                                                                                                         | String  |
| **username** _required_                  | Username for authenticating to server.                                                                                                                                                                                          | String  |
| **password** _required_                  | Password for authenticating to server                                                                                                                                                                                           | String  |
| **ca\_cert\_path** _optional_            | Root CA cert path for TLS connection                                                                                                                                                                                            | String  |
| **server\_tls\_skip\_verify** _optional_ | Allow empty server CA Cert Path without attempting to use system root pool                                                                                                                                                      | Boolean |
| **x509\_cert\_path** _optional_          | Cert path (public key) for X.509 bucket auth                                                                                                                                                                                    | String  |
| **x509\_key\_path** _optional_           | Key path (private key) for X.509 bucket auth                                                                                                                                                                                    | String  |
| **use\_tls\_server** _optional_          | Enforces a secure or non-secure server scheme                                                                                                                                                                                   | Boolean |

### [](#Startup%5Fconfig%5Flogging)StartupConfigLogging

 Object

| Property                        |                                                                                                                                                              | Schema                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **log\_file\_path** _optional_  | Absolute or relative path on the filesystem to the log file directory. A relative path is from the directory that contains the Sync Gateway executable file. | String                                                           |
| **redaction\_level** _optional_ | Redaction level to apply to log output. **Values:** "none", "partial", "full", "unset"                                                                       | String                                                           |
| **console** _optional_          |                                                                                                                                                              | [ConsoleLoggingConfig](#Console%5Flogging%5Fconfig)              |
| **error** _optional_            | Error logging configuration.                                                                                                                                 | [StartupConfigLoggingError](#Startup%5Fconfig%5Flogging%5Ferror) |
| **warn** _optional_             | Warning logging configuration.                                                                                                                               | [StartupConfigLoggingWarn](#Startup%5Fconfig%5Flogging%5Fwarn)   |
| **info** _optional_             | Info logging configuration.                                                                                                                                  | [StartupConfigLoggingInfo](#Startup%5Fconfig%5Flogging%5Finfo)   |
| **debug** _optional_            | Debug logging configuration.                                                                                                                                 | [StartupConfigLoggingDebug](#Startup%5Fconfig%5Flogging%5Fdebug) |
| **trace** _optional_            | Trace logging configuration.                                                                                                                                 | [StartupConfigLoggingTrace](#Startup%5Fconfig%5Flogging%5Ftrace) |
| **stats** _optional_            | Trace logging configuration.                                                                                                                                 | [StartupConfigLoggingStats](#Startup%5Fconfig%5Flogging%5Fstats) |

### [](#Startup%5Fconfig%5Flogging%5Fdebug)StartupConfigLoggingDebug

 Object

| Property                               |                                      | Schema                                                                              |
| -------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------- |
| **enabled** _optional_                 | Toggle for this log output           | Boolean                                                                             |
| **rotation** _optional_                |                                      | [StartupConfigLoggingDebugRotation](#Startup%5Fconfig%5Flogging%5Fdebug%5Frotation) |
| **collation\_buffer\_size** _optional_ | The size of the log collation buffer | Integer                                                                             |

### [](#Startup%5Fconfig%5Flogging%5Fdebug%5Frotation)StartupConfigLoggingDebugRotation

 Object

| Property                                  |                                                                                                                                                                                                                                                             | Schema  |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                                                                                              | Integer |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp.                                                                                                                                                                                  | Boolean |
| **rotated\_logs\_size\_limit** _optional_ | Max Size (in mb) of log files before deletion                                                                                                                                                                                                               | Integer |
| **rotation\_interval** _optional_         | If set, the interval at which log files are rotated, even if max\_size is not reached. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |
| **max\_age** _optional_                   | The maximum number of days to retain old log files.                                                                                                                                                                                                         | Integer |

### [](#Startup%5Fconfig%5Flogging%5Ferror)StartupConfigLoggingError

 Object

| Property                               |                                       | Schema                                                                              |
| -------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| **enabled** _optional_                 | Toggle for this log output            | Boolean                                                                             |
| **rotation** _optional_                |                                       | [StartupConfigLoggingErrorRotation](#Startup%5Fconfig%5Flogging%5Ferror%5Frotation) |
| **collation\_buffer\_size** _optional_ | The size of the log collation buffer. | Integer                                                                             |

### [](#Startup%5Fconfig%5Flogging%5Ferror%5Frotation)StartupConfigLoggingErrorRotation

 Object

| Property                                  |                                                                                                                                                                                                                                                             | Schema  |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                                                                                              | Integer |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp.                                                                                                                                                                                  | Boolean |
| **rotated\_logs\_size\_limit** _optional_ | Max Size (in mb) of log files before deletion                                                                                                                                                                                                               | Integer |
| **rotation\_interval** _optional_         | If set, the interval at which log files are rotated, even if max\_size is not reached. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |
| **max\_age** _optional_                   | The maximum number of days to retain old log files.                                                                                                                                                                                                         | Integer |

### [](#Startup%5Fconfig%5Flogging%5Finfo)StartupConfigLoggingInfo

 Object

| Property                               |                                      | Schema                                                                            |
| -------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------- |
| **enabled** _optional_                 | Toggle for this log output           | Boolean                                                                           |
| **rotation** _optional_                |                                      | [StartupConfigLoggingInfoRotation](#Startup%5Fconfig%5Flogging%5Finfo%5Frotation) |
| **collation\_buffer\_size** _optional_ | The size of the log collation buffer | Integer                                                                           |

### [](#Startup%5Fconfig%5Flogging%5Finfo%5Frotation)StartupConfigLoggingInfoRotation

 Object

| Property                                  |                                                                                                                                                                                                                                                             | Schema  |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                                                                                              | Integer |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp.                                                                                                                                                                                  | Boolean |
| **rotated\_logs\_size\_limit** _optional_ | Max Size (in mb) of log files before deletion                                                                                                                                                                                                               | Integer |
| **rotation\_interval** _optional_         | If set, the interval at which log files are rotated, even if max\_size is not reached. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |
| **max\_age** _optional_                   | The maximum number of days to retain old log files.                                                                                                                                                                                                         | Integer |

### [](#Startup%5Fconfig%5Flogging%5Fstats)StartupConfigLoggingStats

 Object

| Property                               |                                      | Schema                                                                            |
| -------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------- |
| **enabled** _optional_                 | Toggle for this log output           | Boolean                                                                           |
| **rotation** _optional_                |                                      | [StartupConfigLoggingInfoRotation](#Startup%5Fconfig%5Flogging%5Finfo%5Frotation) |
| **collation\_buffer\_size** _optional_ | The size of the log collation buffer | Integer                                                                           |

### [](#Startup%5Fconfig%5Flogging%5Ftrace)StartupConfigLoggingTrace

 Object

| Property                               |                                      | Schema                                                                              |
| -------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------- |
| **enabled** _optional_                 | Toggle for this log output           | Boolean                                                                             |
| **rotation** _optional_                |                                      | [StartupConfigLoggingDebugRotation](#Startup%5Fconfig%5Flogging%5Fdebug%5Frotation) |
| **collation\_buffer\_size** _optional_ | The size of the log collation buffer | Integer                                                                             |

### [](#Startup%5Fconfig%5Flogging%5Fwarn)StartupConfigLoggingWarn

 Object

| Property                               |                                      | Schema                                                                            |
| -------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------- |
| **enabled** _optional_                 | Toggle for this log output           | Boolean                                                                           |
| **rotation** _optional_                |                                      | [StartupConfigLoggingWarnRotation](#Startup%5Fconfig%5Flogging%5Fwarn%5Frotation) |
| **collation\_buffer\_size** _optional_ | The size of the log collation buffer | Integer                                                                           |

### [](#Startup%5Fconfig%5Flogging%5Fwarn%5Frotation)StartupConfigLoggingWarnRotation

 Object

| Property                                  |                                                                                                                                                                                                                                                             | Schema  |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                                                                                              | Integer |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp.                                                                                                                                                                                  | Boolean |
| **rotated\_logs\_size\_limit** _optional_ | Max Size (in mb) of log files before deletion                                                                                                                                                                                                               | Integer |
| **rotation\_interval** _optional_         | If set, the interval at which log files are rotated, even if max\_size is not reached. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |
| **max\_age** _optional_                   | The maximum number of days to retain old log files.                                                                                                                                                                                                         | Integer |

### [](#Startup%5Fconfig%5Freplicator)StartupConfigReplicator

 Object

| Property                                         |                                                                                                                                                                                                                 | Schema  |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **max\_heartbeat** _optional_                    | Max heartbeat value for \_changes request. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |
| **blip\_compression** _optional_                 | BLIP data compression level (0-9) **Minimum:** 0 **Maximum:** 9                                                                                                                                                 | Integer |
| **max\_concurrent\_replications** _optional_     | Maximum number of concurrent replication connections allowed. If set to 0 this limit will be ignored.                                                                                                           | Integer |
| **max\_concurrent\_changes\_batches** _optional_ | Maximum number of changes batches to process concurrently per replication (1-5)" **Minimum:** 1 **Maximum:** 5                                                                                                  | Integer |
| **max\_concurrent\_revs** _optional_             | Maximum number of revs to process concurrently per replication (5-200) **Minimum:** 5 **Maximum:** 200                                                                                                          | Integer |

### [](#Startup%5Fconfig%5Funsupported)StartupConfigUnsupported

 Object

| Property                                  |                                                                                                                                                                                                                       | Schema                                                                             |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **serverless** _optional_                 | Configuration for when SG is running in serverless mode                                                                                                                                                               | [StartupConfigUnsupportedServerless](#Startup%5Fconfig%5Funsupported%5Fserverless) |
| **use\_xattr\_config** _optional_         | Store database configurations in system xattrs                                                                                                                                                                        | Boolean                                                                            |
| **stats\_log\_frequency** _optional_      | How often should stats be written to stats logs. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String                                                                             |
| **use\_stdlib\_json** _optional_          | Bypass the jsoniter package and use Go's stdlib instead                                                                                                                                                               | Boolean                                                                            |
| **http2** _optional_                      |                                                                                                                                                                                                                       | [StartupConfigUnsupportedHttp2](#Startup%5Fconfig%5Funsupported%5Fhttp2)           |
| **allow\_dbconfig\_env\_vars** _optional_ | Can be set to false to skip environment variable expansion in database configs                                                                                                                                        | Boolean                                                                            |

### [](#Startup%5Fconfig%5Funsupported%5Fhttp2)StartupConfigUnsupportedHttp2

 Object

| Property               |                                  | Schema  |
| ---------------------- | -------------------------------- | ------- |
| **enabled** _optional_ | Whether HTTP2 support is enabled | Boolean |

### [](#Startup%5Fconfig%5Funsupported%5Fserverless)StartupConfigUnsupportedServerless

 Object

| Property                                    |                                                                                                                                                                                                                                                                                                                                                             | Schema  |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **enabled** _optional_                      | Run SG in to serverless mode                                                                                                                                                                                                                                                                                                                                | Boolean |
| **min\_config\_fetch\_interval** _optional_ | How long database configs should be kept for in Sync Gateway before refreshing. Set to 0 to fetch configs everytime. This is used for requested databases that SG does not know about. This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be 5h20m30s. | String  |

### [](#Status)Status

 Object

| Property                 |                                                                                                                                                   | Schema      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **databases** _optional_ | Contains a map of all the databases in the node along with their status.                                                                          | [Map](#Map) |
| **version** _optional_   | The product version including the build number and edition (ie. EE or CE). Blank if api.hide\_product\_version=true in the startup configuration. | String      |

### [](#Status%5F1)Status

 Object

| Property                 |                                                                                                                                                   | Schema      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **databases** _optional_ | Contains a map of all the databases in the node along with their status.                                                                          | [Map](#Map) |
| **version** _optional_   | The product version including the build number and edition (ie. EE or CE). Blank if api.hide\_product\_version=true in the startup configuration. | String      |

### [](#Status%5F1%5Fdatabases%5Fvalue)Status1DatabasesValue

 Object

| Property                           |                                                                                                                 | Schema                                                                    |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **seq** _optional_                 | The latest sequence number in the database. **Minimum:** 0                                                      | Big Decimal                                                               |
| **server\_uuid** _optional_        | The server unique identifier.                                                                                   | String                                                                    |
| **state** _optional_               | Whether the database is online or offline. **Values:** "Online", "Offline", "Starting", "Stopping", "Resyncing" | String                                                                    |
| **replication\_status** _optional_ |                                                                                                                 | [ReplicationStatus](#Replication%5Fstatus)array                           |
| **cluster** _optional_             |                                                                                                                 | [Status1DatabasesValueCluster](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster) |

### [](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster)Status1DatabasesValueCluster

 Object

| Property                   |                                                     | Schema                                                                                             |
| -------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **replication** _optional_ | Map of replication configs defined for the cluster. | [Status1DatabasesValueClusterReplication](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Freplication) |
| **nodes** _optional_       | Map of all Sync Gateway nodes in the cluster.       | [Status1DatabasesValueClusterNodes](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Fnodes)             |

### [](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Fnodes)Status1DatabasesValueClusterNodes

 Object

| Property                  |                              | Schema                                                                                                       |
| ------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **node\_uuid** _optional_ | The nodes unique identifier. | [Status1DatabasesValueClusterNodesNodeUuid](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Fnodes%5Fnode%5Fuuid) |

### [](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Fnodes%5Fnode%5Fuuid)Status1DatabasesValueClusterNodesNodeUuid

 Object

| Property            |                              | Schema |
| ------------------- | ---------------------------- | ------ |
| **uuid** _optional_ | The nodes unique identifier. | String |
| **host** _optional_ | The nodes host name.         | String |

### [](#Status%5F1%5Fdatabases%5Fvalue%5Fcluster%5Freplication)Status1DatabasesValueClusterReplication

 Object

| Property                       |                             | Schema                           |
| ------------------------------ | --------------------------- | -------------------------------- |
| **replication\_id** _optional_ | Properties of a replication | [Replication1](#Replication%5F1) |

### [](#User)User

 Object

| Property                          |                                                                                                                                                                                                                      | Schema           |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **name** _optional_               | The name of the user. User names can only have alphanumeric ASCII characters and underscores.                                                                                                                        | String           |
| **password** _optional_           | The password of the user. Mandatory. unless allow\_empty\_password is true in the database configs.                                                                                                                  | String           |
| **admin\_channels** _optional_    | A list of channels to explicitly grant to the user for the default collection.                                                                                                                                       | String array     |
| **all\_channels** _optional_      | All the channels that the user has been granted access to for the default collection. Access could have been granted through the sync function, roles, or explicitly on the user under the admin\_channels property. | String array     |
| **collection\_access** _optional_ | A set of access grants by scope and collection.                                                                                                                                                                      | [Map](#Map)      |
| **email** _optional_              | The email address of the user.                                                                                                                                                                                       | String           |
| **disabled** _optional_           | If true, the user will not be able to login to the account as it is disabled.                                                                                                                                        | Boolean          |
| **admin\_roles** _optional_       | A list of roles to explicitly grant to the user.                                                                                                                                                                     | String array     |
| **roles** _optional_              | All the roles that the user has been granted access to. Access could have been granted through the sync function, roles\_claim, or explicitly on the user under the admin\_roles property.                           | String array     |
| **jwt\_roles** _optional_         | The roles that the user has been added to through roles\_claim.                                                                                                                                                      | String array     |
| **jwt\_channels** _optional_      | The channels that the user has been granted access to through channels\_claim.                                                                                                                                       | String array     |
| **jwt\_issuer** _optional_        | The issuer of the last JSON Web Token that the user last used to sign in.                                                                                                                                            | String           |
| **jwt\_last\_updated** _optional_ | The last time that the user's JWT roles/channels were updated.                                                                                                                                                       | Date (date-time) |

### [](#User%5F1)User

 Object

| Property                          |                                                                                                                                                                                                                      | Schema           |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **name** _optional_               | The name of the user. User names can only have alphanumeric ASCII characters and underscores.                                                                                                                        | String           |
| **password** _optional_           | The password of the user. Mandatory. unless allow\_empty\_password is true in the database configs.                                                                                                                  | String           |
| **admin\_channels** _optional_    | A list of channels to explicitly grant to the user for the default collection.                                                                                                                                       | String array     |
| **all\_channels** _optional_      | All the channels that the user has been granted access to for the default collection. Access could have been granted through the sync function, roles, or explicitly on the user under the admin\_channels property. | String array     |
| **collection\_access** _optional_ | A set of access grants by scope and collection.                                                                                                                                                                      | [Map](#Map)      |
| **email** _optional_              | The email address of the user.                                                                                                                                                                                       | String           |
| **disabled** _optional_           | If true, the user will not be able to login to the account as it is disabled.                                                                                                                                        | Boolean          |
| **admin\_roles** _optional_       | A list of roles to explicitly grant to the user.                                                                                                                                                                     | String array     |
| **roles** _optional_              | All the roles that the user has been granted access to. Access could have been granted through the sync function, roles\_claim, or explicitly on the user under the admin\_roles property.                           | String array     |
| **jwt\_roles** _optional_         | The roles that the user has been added to through roles\_claim.                                                                                                                                                      | String array     |
| **jwt\_channels** _optional_      | The channels that the user has been granted access to through channels\_claim.                                                                                                                                       | String array     |
| **jwt\_issuer** _optional_        | The issuer of the last JSON Web Token that the user last used to sign in.                                                                                                                                            | String           |
| **jwt\_last\_updated** _optional_ | The last time that the user's JWT roles/channels were updated.                                                                                                                                                       | Date (date-time) |

### [](#User%5F1%5Fcollection%5Faccess%5Fvalue%5Fvalue)User1CollectionAccessValueValue

 Object

| Property                          |                                                                                                                                                                                           | Schema           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **admin\_channels** _optional_    | A list of channels to explicitly grant to the user.                                                                                                                                       | String array     |
| **all\_channels** _optional_      | All the channels that the user has been granted access to. Access could have been granted through the sync function, roles, or explicitly on the user under the admin\_channels property. | String array     |
| **jwt\_channels** _optional_      | The channels that the user has been granted access to through channels\_claim.                                                                                                            | String array     |
| **jwt\_last\_updated** _optional_ | The last time that the user's JWT roles/channels were updated.                                                                                                                            | Date (date-time) |

### [](#User%5F2)User

 Object

| Property                          |                                                                                                                                                                                                                      | Schema           |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **name** _optional_               | The name of the user. User names can only have alphanumeric ASCII characters and underscores.                                                                                                                        | String           |
| **password** _optional_           | The password of the user. Mandatory. unless allow\_empty\_password is true in the database configs.                                                                                                                  | String           |
| **admin\_channels** _optional_    | A list of channels to explicitly grant to the user for the default collection.                                                                                                                                       | String array     |
| **all\_channels** _optional_      | All the channels that the user has been granted access to for the default collection. Access could have been granted through the sync function, roles, or explicitly on the user under the admin\_channels property. | String array     |
| **collection\_access** _optional_ | A set of access grants by scope and collection.                                                                                                                                                                      | [Map](#Map)      |
| **email** _optional_              | The email address of the user.                                                                                                                                                                                       | String           |
| **disabled** _optional_           | If true, the user will not be able to login to the account as it is disabled.                                                                                                                                        | Boolean          |
| **admin\_roles** _optional_       | A list of roles to explicitly grant to the user.                                                                                                                                                                     | String array     |
| **roles** _optional_              | All the roles that the user has been granted access to. Access could have been granted through the sync function, roles\_claim, or explicitly on the user under the admin\_roles property.                           | String array     |
| **jwt\_roles** _optional_         | The roles that the user has been added to through roles\_claim.                                                                                                                                                      | String array     |
| **jwt\_channels** _optional_      | The channels that the user has been granted access to through channels\_claim.                                                                                                                                       | String array     |
| **jwt\_issuer** _optional_        | The issuer of the last JSON Web Token that the user last used to sign in.                                                                                                                                            | String           |
| **jwt\_last\_updated** _optional_ | The last time that the user's JWT roles/channels were updated.                                                                                                                                                       | Date (date-time) |

### [](#User%5Fconfigurable%5Freplication%5Fproperties)User configurable replication properties

 Object

| Property                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Schema       |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **replication\_id** _optional_            | This is the ID of the replication. When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set. When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String       |
| **remote** _optional_                     | This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's push, pull, or pushAndPull action. Typically this would include the URI, port, and database name. For example, http://localhost:4985/db. How this remote is used depends on the direction of the replication: pull \- this replicator _pulls_ changes from the remote push \- this replicator _pushes_ changes to this remote pushAndPull \- this replicator _pushes_ changes to this remote, while also pulling receiving changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String       |
| **username** _optional_                   | **This has been deprecated in favour of remote\_username.** This is the username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **password** _optional_                   | **This has been deprecated in favour of remote\_password.** This is the password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String       |
| **remote\_username** _optional_           | The username to use to authenticate with the remote. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |
| **remote\_password** _optional_           | The password to use to authenticate with the remote. This password will be redacted in the replication config. This can only be used for a pull replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String       |
| **direction** _required_                  | This specifies which direction the replication will be replicating with the remote replicator. The directions are: pull \- changes are pulled from the remote database push \- changes are pushed to the remote database pushAndPull \- changes are both push-to and pulled-from the remote database Replications created prior to Sync Gateway 2.8 derive their direction from the source/target URL of the replication. **Values:** "push", "pull", "pushAndPull"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String       |
| **conflict\_resolution\_type** _optional_ | This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions. Changing this is an enterprise-edition only feature. **Behaviour** _default_ \- In priority order, this will cause Deletes to always win (the delete with the longest revision history wins if both revisions are deletes) The revision with the longest revision history to win. This means the the revision with the most changes and therefore the highest revision ID will win. _localWins_ \- This will result in local revisions always being the winner in any conflict. _remoteWins_ \- This will result in remote revisions always being the winner in any conflict. _custom_ \- This will result in conflicts going through your own custom conflict resolver. You must provide this logic as a Javascript function in the custom\_conflict\_resolver parameter. This is an enterprise-edition only feature. Note: replications created prior to Sync Gateway 2.8 will default to default. **Values:** "default", "remoteWins", "localWins", "custom"                                                                                                               | String       |
| **custom\_conflict\_resolver** _optional_ | This specifies the Javascript function to use to resolve conflicts between conflicting revisions. This **must** be used when conflict\_resolution\_type=custom. This property will be ignored when conflict\_resolution\_type is not custom. The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties: LocalDocument \- The local document. This contains the document ID under the \_id key. RemoteDocument \- The remote document The function should return the new documents body. This can be the winning revision (for example, return conflict.LocalDocument), a new body, or nil to resolve as a delete. Example: "custom\_conflict\_resolver":\\\` 	function(conflict) { 		console.log("Doc ID: "+conflict.LocalDocument.\_id); 		console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument)); 		return conflict.RemoteDocument; 	} \\\` Using complex custom\_conflict\_resolver functions can noticeably degrade performance. Use a built-in resolver whenever possible. This is an enterprise-edition only feature. | String       |
| **purge\_on\_removal** _optional_         | Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote. If false, documents will not be replicated and not be purged when the user loses access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean      |
| **enable\_delta\_sync** _optional_        | This will turn on delta- sync for the replication. This works in conjunction with the database level setting delta\_sync.enabled If set to true, delta-sync will be used as long as both databases involved in the replication have delta-sync enabled. If a database does not have delta-sync enabled, then the replication will run without delta-sync. Replications created prior to Sync Gateway 2.8 must have delta-sync disabled. Enabling this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean      |
| **max\_backoff\_time** _optional_         | Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote. When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every max\_backoff\_time minutes. If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication. Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer      |
| **initial\_state** _optional_             | This is what state to start the replication in when creating a new replication. This allows you to control if the replication starts in a stopped start or running state. Replications prior to Sync Gateway 2.8 will run in the default state running. **Values:** "running", "stopped"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | String       |
| **continuous** _optional_                 | If true, changes will be immediately synced when they happen. This is known as a continuous replication. If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean      |
| **filter** _optional_                     | This defines whether to filter documents by their channels or not. If set to sync\_gateway/bychannel then a **pull** replication will be limited to a specific set of channels specified by the query\_params.channels property. This only can be used with pull replications. **Values:** "sync\_gateway/bychannel"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String       |
| **query\_params** _optional_              | This is a set of key/value pairs used in the query string of the replication. If filters=sync\_gateway/bychannel then this can be used to set the channels to filter by in a pull replication. To do this, set the channels key to a string array of the channels to filter by. For example: "filter":"sync\_gateway/bychannel", "query\_params": {   "channels":\["chanUser1"\] },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String array |
| **adhoc** _optional_                      | Set to true to run the replication as an adhoc replication instead of a persistent one. This means that the replication will only last the period of the replication until the status is changed to stopped and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean      |
| **batch\_size** _optional_                | The amount of changes to be sent in one batch of replications. Changing this is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer      |
| **run\_as** _optional_                    | This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | String       |
| **collections\_enabled** _optional_       | If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by keyspace\_map. If false, the replicator will only replicate the default collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean      |
| **collections\_local** _optional_         | Limits the set of collections replicated to those listed in this array. The replication will use all collections defined on the database if this list is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String array |
| **collections\_remote** _optional_        | Remaps the local collection name to the one specified in this array when replicating with the remote. If only a subset of collections need remapping, elements in this array can be specified as null to preserve the local collection name. The same index is used for both collections\_remote and collections\_local, and both arrays must be the same length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String array |

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