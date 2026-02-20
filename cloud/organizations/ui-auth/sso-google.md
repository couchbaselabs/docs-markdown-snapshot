---
title: Set Up Capella SSO Using Google Workspace
description: Configure Single Sign-On (SSO) between Google Workspace and
  Couchbase Capella to allow your organization's users to authenticate securely
  without managing separate credentials. This integration enables streamlined
  access management while maintaining enterprise-grade security.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/sso-google.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:organizations:ui-auth/sso-google.adoc[]
---

[View original HTML](/cloud/organizations/ui-auth/sso-google.html)

# Set Up Capella SSO Using Google Workspace

> Configure Single Sign-On (SSO) between Google Workspace and Couchbase Capella to allow your organization’s users to authenticate securely without managing separate credentials. This integration enables streamlined access management while maintaining enterprise-grade security. 

## [](#prerequisites)Prerequisites

To configure Google Workspace as an IdP, you need:

* To [enable SSO](add-sso-auth.md#access-and-enable-sso-settings) for your Capella organization.
* To sign in to the Google Cloud Console as a [super administrator](https://support.google.com/a/answer/2405986?sjid=13657301824554967820-NA#super%5Fadmin).

## [](#procedure)Procedure

Choose the tab for your preferred authentication protocol.

* SAML
* OIDC

To configure federated and SSO authentication using SAML with Google as your identity provider (IdP), you must complete three procedures in the following order:

1. [In Google Workspace, create a custom SAML app](#create-google-app).
2. [In Capella, create a realm](#create-google-realm).
3. [In Google Workspace, complete the configuration](#complete-google-config).

---

Add a custom SAML app in Google Workspace

Start by adding an app for Capella in the Google Cloud Console. You need information resulting from this step to create a realm in Capella.

1. In the Google Cloud Console, click **Apps** **Web and mobile apps**.
2. Click **Add app** **Add custom SAML app**.
3. Complete these fields:

  * **App Name**: Enter the display name for this app.
  * (Optional) **Description**: Add a description of the application.
  * (Optional) **App Icon**: Add the Capella logo.

    1. Click **Continue**.  
      Leave this new page open as you need its information for the next step.

Create a Realm in Capella

Create a realm in Capella using information from Google.

1. In the Capella UI, click **Settings** **SSO**.
2. Click **Create Realm** **SAML**.
3. Complete the **Create Realm** page:

  1. Copy the following configuration details from Google into Capella:

| Google Field |                          | Capella Field |
| ------------ | ------------------------ | ------------- |
| Certificate  | SAML Signing Certificate |               |
| SSO URL      | Sign-in Endpoint URL     |               |
  2. Verify that the remaining SAML protocol settings are as follows:

| Field                 | Value      |
| --------------------- | ---------- |
| Signature Algorithm   | RSA-SHA256 |
| Digest Algorithm      | SHA256     |
| SAML Protocol Binding | HTTP-POST  |
  3. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  4. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project’s **Collaborators** tab.
4. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

Complete the configuration in Google Workspace

Now that you have created the realm, you must finish configuring the custom SAML app in Google.

1. Returning to the Google Cloud Console, on the **Add custom SAML app** setup page, click **Continue**.
2. Copy and paste the following fields from your Capella realm configuration into the Google custom SAML app setup:  
> [!TIP]  
> To find this information for your organization’s Capella realm, open the **Settings** **SSO** page. Listed on this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page.

| Capella Field |           | Google Field |
| ------------- | --------- | ------------ |
| Callback URL  | ACS URL   |              |
| Entity ID     | Entity ID |              |
3. In the Google Cloud Console, click **Continue**.
4. Add the following attributes:

| Google Directory attributes | App attributes |
| --------------------------- | -------------- |
| Primary email               | email          |
| First name                  | given\_name    |
| Last name                   | family\_name   |
5. Add group membership.

| Google groups                           | App attribute |
| --------------------------------------- | ------------- |
| Relevant Google groups, such as admins. | Groups        |
6. Click **Finish**.  
A page for the new custom SAML web app automatically loads with its configuration details.
7. Turn on the SAML web app for everyone:  
> [!NOTE]  
> To turn on the service for an organizational unit or user group, see [Google Workspace Admin Help](https://support.google.com/a/answer/6087519?hl=en).

  1. Click **User access**.
  2. Click **On for everyone**.
  3. Click **Save**.  
  It may take a few minutes for these changes to apply.

To configure federated and SSO authentication using OIDC with Google as your identity provider (IdP), you must complete three procedures in the following order:

1. [In Google Workspace, create a new OAuth client configuration](#create-google-app-oidc).
2. [In Capella, create a realm](#create-google-realm-oidc).
3. [In Google Workspace, complete the configuration](#complete-google-config-oidc).

---

Add a new OAuth client configuration

Start by adding an OAuth client configuration for Capella in the Google Cloud Console. You need information from this step to create a realm in Capella.

1. In the Google Cloud Console, [create a new project](https://console.cloud.google.com/projectcreate).
2. With the new project open, click **APIs & Services** **Credentials**.
3. Click **Configure consent screen**.
4. Click **Get started**.
5. Complete the **App Information**, **Audience**, **Contact Information**, and **Finish** sections of the consent screen configuration:

  * **App name**: Enter a meaningful app name.
  * **User support email**: Choose or add a contact email for questions about users' consent.
  * **Audience**: Choose the **Internal** audience type.
  * **Contact information**: Add a contact email for Google to notify you about changes to your project.
6. Review the User Data Policy. Click **Continue**
7. Click **Create**.
8. Click **Data Access** **Add or remove scopes**.
9. Add the following scopes:

  * `…​/auth/userinfo.email`
  * `…​/auth/userinfo.profile`
  * `openid`
10. Click **Update**.
11. Click **Save**.
12. Click **Clients** **Create Client** and configure the OAuth client:

  * **Application type**: Select **Web application**.
  * **Name**: Enter a name for your Capella integration.
  * **Authorized JavaScript origins**: Leave empty.
  * **Authorized redirect URIs**: Leave empty for now—​you’ll add this later.
13. Click **Create**.  
Your Client ID and Client Secret are shown. Keep this information secure as you’ll need it for the next step.

Create a Realm in Capella

With the OAuth client created in Google, you need to create a realm in Capella using its information.

1. In Capella, click **Settings** **SSO**.
2. Click **Create Realm** **OpenID Connect**.
3. Copy the following information from your Google Oauth client to Capella:

| Google Field                                                                 |                              | Capella Field |
| ---------------------------------------------------------------------------- | ---------------------------- | ------------- |
| https://accounts.google.com/.well-known/openid-configuration (this is fixed) | OpenID Connect Discovery URL |               |
| Client ID                                                                    | Client ID                    |               |
| Client secret                                                                | Client Secret                |               |
4. Configure scopes:  
Scopes determine which user information Capella requests from your identity provider. The `openid`, `email`, and `profile` scopes are automatically included in the realm by default, so you do not need to add them.  
When adding additional scopes, separate each entry with a space.
5. Configure a default team and group mapping.

  1. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  2. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project’s **Collaborators** tab.
6. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

Complete the configuration in Google Workspace

Now that you have created the realm, you need to finish configuring the Google Workspace OAuth client.

1. In the Google Cloud Console, open the OAuth client you [created](#create-google-app-oidc) for Capella.
2. Copy the following field from your Capella realm configuration to the Google OAuth client configuration:  
> [!TIP]  
> To find this information for your organization’s Capella realm, open the **Settings** **SSO** page. Listed on this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page.

| Capella Field |                          | Google Field |
| ------------- | ------------------------ | ------------ |
| Callback URL  | Authorized redirect URIs |              |
3. Click **Save**.

## [](#next-steps)Next Steps

* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Map User Roles](manage-role-mapping.md)
* [Manage Identity Providers](manage-identity-providers.md)