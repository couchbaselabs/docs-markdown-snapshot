---
title: Set Up an Authentication Provider
description: Capella supports a number of authentication providers, which can be
  configured from the Capella UI.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/security/set-up-authentication-provider.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:app-services::security/set-up-authentication-provider.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/security/set-up-authentication-provider.html)

# Set Up an Authentication Provider

> Capella supports a number of authentication providers, which can be configured from the Capella UI. 

Out of the box, Capella supports `Basic`, `Anonymous`, and `OpenID Connect` as methods for authentication.

1. Select your App Endpoint
2. Select the **Security** tab.
3. From the menu on the left, select **Authentication Providers**

![App Provider](../_images/user-management/authentication-provider-screen.png) 

Figure 1\. Authentication Provider set-up screen

## [](#basic-authentication)Basic Authentication

The authentication credentials are passed through the HTTPS headers of the calling client.

> [!TIP]
> Your [Couchbase Lite SDK](../app-endpoints/connect-apps-to-endpoint.md) will handle the details of this for you. It will pass an HTTPS header like `Authorization: Basic c3luY19nYXRld2F5OnBhc3N3b3Jk`. This random looking string is simply a Base64 encoded representation of the Username and Password that you have passed in.

## [](#anonymous-authentication)Anonymous Authentication

Allowing anonymous authentication is useful for testing as it allows access to the endpoint without the need for authentication. It is also useful for endpoints that might synchronize static information such as information pages which anyone is allowed to access.

> [!NOTE]
> It is recommended that either _basic authentication_ or _OIDC_ is used for production environments.

## [](#openid-connect-oidc)OpenID Connect (OIDC)

Capella App Services supports OpenID Connect. This allows your application to use Couchbase for data synchronization and delegate the authentication to a third-party server (known as the Provider).

Capella’s implementation of OpenID Connect uses Implicit Flow. This means that the retrieval of the ID token takes place on the device. Capella handles the background set up for the app service, using the details provided in the settings:

Issuer

This is the URL of the authentication provider. For example, if you are using Google’s authentication service, then the URL would be <https://accounts.google.com>. Details of the URL required should be available on your provider’s website.

Client ID

When you register your App Service with your OIDC provider, you will be given a `Client ID` unique to your application. The provider will use this ID to identify the application using the authentication service.

Discovery URL

Providers usually provide a configuration application for their users, which can be accessed through the URL given here. This setting is optional.

Username prefix

The OIDC username is taken from the App Service user and a prefix is added. The prefix itself is derived from the name of the OIDC provider, or optionally, you can supply your own prefix here.

Username claim

Specifies a claim other than the subject to use as the App Services username. By default, the `issuer` is used, but you can use another `claim` field, such as the email address.

Scope

Specifies what information to request from the authentication provider upon successful user authentication. The scope field is an array where each value references a group of "claims" on the OIDC provider. For example, a `profile` scope could reference `first_name` and `last_name` claims. The authentication provider returns these claim properties on successful OIDC authentication. If no custom scopes are defined, App Services uses the scopes `openid` and `email` by default. When configuring OIDC providers in the Capella UI, this field is automatically populated with these default values.

Roles claim

Specifies a JWT claim to use for assigning a role to the OIDC user. This setting is optional.

Auto register

The App Service service can be configured to create a new user if it receives a valid authorization from an unregistered user.

### [](#oidc-authorization-step-by-step)OIDC Authorization: step by step

![OIDC Authorization Sequence](../_images/diag-0d6c18608b18cd50f772e36f43b48a64d8fc3377.svg) 

Figure 2\. OIDC Authorization Sequence

## [](#configure-multiple-oidc-providers)Configure Multiple OIDC Providers

You can add multiple OIDC providers in Capella App Services:

1. Go to the security tab in App Endpoint settings.
2. Click the **OpenID Connect** checkbox to enable OIDC.
3. Click the **Add OIDC Provider** button.

> [!NOTE]
> After enabling OIDC authentication, you must create a user-defined OIDC provider.

Once you have configured an OIDC provider, the **Add OIDC Provider** button is replaced by the **OIDC Providers List** table.

### [](#set-a-default-oidc-provider)Set a Default OIDC Provider

When multiple OIDC providers are configured, the first OIDC provider is automatically designated as the default provider. After you enable OIDC, all client requests will use the default OIDC provider, unless the OIDC provider for the request is explicitly specified. You can then choose which among them is the default provider via selecting the relevant radio button from the **Default OIDC Provider** column in the **OIDC Providers List** table.

> [!NOTE]
> Using non-default OIDC providers in Capella App Services requires requests to `/db/_oidc/` to specify the provider parameter.

### [](#editing-a-configured-oidc-provider)Editing a Configured OIDC Provider

You can edit configured OIDC providers via the OIDC providers table in the Auth Providers tab in the App Endpoint configuration settings.

### [](#delete-a-configured-oidc-provider)Delete a Configured OIDC Provider

To delete a configured OIDC provider:

1. In the **OIDC Providers List** table, find the OIDC provider you want to delete.
2. Go to **More Options (⋮)** **Delete**.
3. Confirm that you want to delete the selected OIDC provider.

To delete a configured OIDC provider, the provider must meet the following conditions:

* It must not be the only configured provider.
* It must not be the default provider.

> [!NOTE]
> If you want to delete the current default provider, you must select a new default provider first from the **OIDC Providers List** table.