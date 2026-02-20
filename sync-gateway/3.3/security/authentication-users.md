---
title: User Authentication
description: Access {sgw} securely to sync from cloud to edge
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/security/pages/authentication-users.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.3@sync-gateway:security:authentication-users.adoc[]
---

[View original HTML](/sync-gateway/3.3/security/authentication-users.html)

# User Authentication

> Access {sgw} securely to sync from cloud to edge  
> This content explains how to implement user authentication in sync gateway

Related _Security_ topics: [TLS Certificate Authentication](authentication-certs.md) | [Sync Function](../access-control/sync-function/sync-function.md) | [Import filter](../sync/import-processing.md) | [Read Access](../access-control/access-control-how-control-document-access.md#lbl-read-access) | [Write Access](../access-control/access-control-how-control-document-access.md#lbl-write-access)

## [](#introduction)Introduction

Authentication is the process of verifying the identity of a user. _Sync Gateway_ supports the following authentication methods:

[Anonymous Access](#anonymous-access)

sync gateway does not allow anonymous or guest access by default, but it can be enabled by editing the configuration file or by using the Admin REST API.

[Basic Authentication](#basic-authentication)

Provide a username and password to authenticate users.

[Auth Providers](#auth-providers)

sync gateway provides a turn-key solution to authenticate with Facebook or Google.  
For other providers we recommend to use Custom Authentication or OpenID Connect.

* [Custom Authentication](#custom-authentication)Use an App Server to handle the authentication yourself and create user sessions on the sync gateway Admin REST API.
* [OpenID Connect Authentication](#openid-connect)Use OpenID Connect providers (Google+, Paypal, etc.) to authenticate users. Static providers: sync gateway currently supports authentication endpoints for Facebook, Google+ and OpenID Connect providers

## [](#anonymous-access)Anonymous Access

A special user account named `GUEST` applies to unauthenticated requests. Any request to the Public REST API that does not have an `Authorization` header or a session cookie is treated as coming from the `GUEST` account. This account and all anonymous access is disabled by default.

To enable the GUEST account, set its `disabled` property to false. You might also want to give it access to some channels. If you don’t assign some channels to the GUEST account, anonymous requests won’t be able to access any documents. The following sample command enables the GUEST account and allows it access to a channel named public.

```bash
$ curl -X PUT localhost:4985/$DB/_user/GUEST --data \
   '{"disabled":false, "collection_access": {"scopename": {"collectionname": {"admin_channels":["public"]}}}}'
```

## [](#basic-authentication)Basic Authentication

Once the user has been created on sync gateway, you can provide the same **username**/**password** to the `BasicAuthenticator` class of _Couchbase Lite_. Under the hood, the replicator will send the credentials in the first request to retrieve a `SyncGatewaySession` cookie and use it for all subsequent requests during the replication. This is the recommended way of using basic authentication.

Related Couchbase Lite content

[Android](../../../couchbase-lite/3.3/android/replication.md#basic-authentication) | [C](../../../couchbase-lite/3.3/c/replication.md#basic-authentication) | [C#](../../../couchbase-lite/3.3/csharp/replication.md#basic-authentication) | [Java](../../../couchbase-lite/3.3/java/replication.md#basic-authentication) | [Objective-C](../../../couchbase-lite/3.3/objc/replication.md#basic-authentication) | [Swift](../../../couchbase-lite/3.3/swift/replication.md#basic-authentication)

## [](#auth-providers)Auth Providers

> [!CAUTION]
> Deprecation Notice
> 
> This feature is deprecated.  
> It can be enabled **only** when running in legacy mode.

sync gateway provides a turn-key solution to authenticate with Facebook or Google.

The app is responsible for retrieving the auth provider token and must send it to sync gateway which will return a session ID. The session ID can be used to configure the Couchbase Lite replicator or for other HTTP requests to the sync gateway REST API.

The following diagram describes the sequence of steps.

![static auth provider](../_images/static-auth-provider.png) 

API reference:

* [/{db}/\_facebook](../rest-api/rest%5Fapi%5Fpublic.md#tag/Authentication/operation/post%5Fdb-%5Ffacebook)
* [/{db}/\_google](../rest-api/rest%5Fapi%5Fpublic.md#tag/Authentication/operation/post%5Fdb-%5Fgoogle)

For other providers we recommend to use Custom Authentication or OpenID Connect.

## [](#custom-authentication)Custom Authentication

It’s possible for an application server associated with a remote Couchbase sync gateway to provide its own custom form of authentication. Generally this will involve a particular URL that the app needs to post some form of credentials to; the App Server will verify those, then tell the sync gateway to create a new session for the corresponding user, and return session credentials in its response to the client app.

The following diagram shows an example architecture to support Google SignIn in a Couchbase Mobile application, the client sends an access token to the App Server where a server side validation is done with the Google API and a corresponding sync gateway user is then created if it’s the first time the user logs in. The last request creates a session.

![custom auth flow](../_images/custom-auth-flow.png) 

Given a user that has already been created, a new session for that user can be created on the Admin [POST /{db}/\_session](../rest-api/rest%5Fapi%5Fadmin.md#tag/Session/operation/post%5Fdb-%5Fsession) endpoint.

```bash
$ curl -vX POST -H 'Content-Type: application/json' \
        -d '{"name": "john", "ttl": 180}' \
        http://localhost:4985/sync_gateway/_session
// Response message body
{
  "session_id": "904ac010862f37c8dd99015a33ab5a3565fd8447",
  "expires": "2015-09-23T17:27:17.555065803+01:00",
  "cookie_name": "SyncGatewaySession"
}
```

The HTTP response body contains the credentials of the session.

* **name** corresponds to the `cookie_name`
* **value** corresponds to the `session_id`
* **path** is the hostname of the sync gateway
* **expirationDate** corresponds to the cookie’s expiration time. The endpoint’s [API reference](../rest-api/rest%5Fapi%5Fadmin.md#tag/Session/operation/post%5Fdb-%5Fsession) contains more information about how the expiration time is automatically extended according to the user session activity.
* **secure** Whether the cookie should only be sent using a secure protocol (e.g. HTTPS)
* **httpOnly** Whether the cookie should only be used when transmitting HTTP, or HTTPS, requests thus restricting access from other, non-HTTP APIs

It is recommended to return the session details to the client application in the same form and to use the `SessionAuthenticator` class to authenticate with that session id.

Unresolved directive in authentication-users.adoc - include::{root-partials}blocklinks-cbl.adoc\[\]

## [](#openid-connect)OpenID Connect

sync gateway supports OpenID Connect. This allows your application to use Couchbase for data synchronization and delegate the authentication to a 3rd party server (known as the Provider). There are two implementation methods available with OpenID Connect:

[Implicit Flow](#implicit-flow)

With this method, the retrieval of the ID token takes place on the device. You can then create a user session using the POST `/{db}/_session` endpoint on the Public REST API with the ID token.

[Authorization Code Flow](#authorization-code-flow)

This method relies on sync gateway to retrieve the ID token.

### [](#implicit-flow)Implicit Flow

[Implicit Flow](https://openid.net/specs/openid-connect-core-1%5F0.html#ImplicitFlowAuth) has the key feature of allowing clients to obtain their own Open ID token and use it to authenticate against sync gateway. The implicit flow with sync gateway is as follows:

1. The client obtains a **signed** Open ID token directly from an OpenID Connect provider. Note that only signed tokens are supported. To verify that the Open ID token being sent is indeed signed, you can use the [jwt.io Debugger](https://jwt.io/#debugger-io). In the algorithm dropdown, make sure to select `RS256` as the signing algorithm (other options such as `HS256` are not yet supported by sync gateway).
2. The client includes the Open ID token as an `Authorization: Bearer <id_token>` header on requests made against the sync gateway REST API.
3. sync gateway matches the token to a provider in its configuration file based on the issuer and audience in the token.
4. sync gateway validates the token, based on the provider definition.
5. Upon successful validation, sync gateway authenticates the user based on the subject and issuer in the token.

Since Open ID tokens are typically large, the usual approach is to use the Open ID token to obtain a sync gateway session id (using the [POST /{db}/\_session](../rest-api/rest%5Fapi%5Fpublic.md#tag/Session/operation/post%5Fdb-%5Fsession)endpoint), and then use the returned session id for subsequent authentication requests.

**Note:** This example is based on a deployment using legacy configuration.

* REST API
* Configuration File

```bash
curl --location --request PUT 'http://localhost:4985/ourdb/_config' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  oidc: {
    providers: {
      google_implicit: {
        issuer:https://accounts.google.com,
        client_id:yourclientid-uso.apps.googleusercontent.com,
        register:true (1)
      },
    },
  }
}'
```

| **1** | Use register to auto-register a sync gateway user on successful completion of the validation |
| ----- | -------------------------------------------------------------------------------------------- |

Here is a sample sync gateway config file, configured to use the Implicit Flow.

```json
{
  "databases": {
    "default": {
      "name": "dbname",
      "bucket": "default",
      "oidc": {
        "providers": {
          "google_implicit": {
            "issuer":"https://accounts.google.com",
            "client_id":"yourclientid-uso.apps.googleusercontent.com",
            "register":true (1)
          },
        },
      }
    }
  }
}
```

| **1** | Use register to auto-register a sync gateway user on successful completion of the validation |
| ----- | -------------------------------------------------------------------------------------------- |

#### [](#client-authentication)Client Authentication

With the implicit flow, the mechanism to refresh the token and sync gateway session must be handled in the application code. On launch, the application should check if the token has expired. If it has then you must request a new token (Google SignIn for iOS has a method called `signInSilently` for this purpose). By doing this, the application can then use the token to create a sync gateway session.

![client auth](../_images/client-auth.png) 

1. The Google SignIn SDK prompts the user to login and if successful it returns an ID token to the application.
2. The ID token is used to create a sync gateway session by sending a POST `/{db}/_session` request.
3. sync gateway returns a cookie session in the response header.
4. The sync gateway cookie session is used on the replicator object.

sync gateway sessions also have an expiration date. The replication `lastError` property will return a **401 Unauthorized** when it’s the case and then the application must retrieve create a new sync gateway session and set the new cookie on the replicator.

A complete tutorial is available [here](https://docs.couchbase.com/tutorials/openid-connect-implicit-flow/index.html) for your reference.

You can configure your application for Google SignIn by following [this guide](https://developers.google.com/identity/).

### [](#authorization-code-flow)Authorization Code Flow

Whilst sync gateway supports [Authorization Code Flow](https://openid.net/specs/openid-connect-core-1%5F0.html#CodeFlowAuth), there is considerable work involved to implement the **Authorization Code Flow** on the client side. Couchbase Lite 1.x has an API to hide this complexity called `OpenIDConnectAuthenticator` but since it is not available in the 2.0 API we recommend to use the **Implicit Flow**.