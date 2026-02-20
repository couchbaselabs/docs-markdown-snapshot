---
title: Set Up Capella SSO Using CyberArk
description: Configure Single Sign-On (SSO) between CyberArk and Couchbase
  Capella to allow your organization's users to authenticate securely without
  managing separate credentials. This integration enables streamlined access
  management while maintaining enterprise-grade security.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/sso-cyberark.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:organizations:ui-auth/sso-cyberark.adoc[]
---

[View original HTML](/cloud/organizations/ui-auth/sso-cyberark.html)

# Set Up Capella SSO Using CyberArk

> Configure Single Sign-On (SSO) between CyberArk and Couchbase Capella to allow your organization’s users to authenticate securely without managing separate credentials. This integration enables streamlined access management while maintaining enterprise-grade security. 

## [](#prerequisites)Prerequisites

To configure CyberArk as an IdP, you need:

* To [enable SSO](add-sso-auth.md#access-and-enable-sso-settings) for your Capella organization.
* A [CyberArk](https://www.cyberark.com) account.
* To sign in to the CyberArk Admin Portal as an admin.

## [](#procedure)Procedure

Choose the tab for your preferred authentication protocol.

* SAML
* OIDC

To configure federated and SSO authentication using SAML with CyberArk as your identity provider (IdP), you must complete three procedures in the following order:

1. [In CyberArk, create an Application](#create-cyberark-app)
2. [In Capella, create a realm](#create-cyberark-realm)
3. [In CyberArk, complete the configuration](#complete-cyberark-config)

---

Add a CyberArk Web App

Start by creating a CyberArk web application in the CyberArk Admin Portal. You need information from this step to create a realm in Capella.

1. In the CyberArk Admin Portal, click **Apps & Widgets** **Web Apps**.
2. Create the web application:

  1. Click **Add Web Apps**.
  2. Click the **Custom** tab.
  3. In the list of templates, find the **SAML** option and click **Add**.
  4. To add this application, click **Yes**.
  5. Exit the **Add Web Apps** dialog by clicking **Close**.  
  You now see the **Settings** page for the SAML app.
  6. Fill in the following fields:

    * **Name**: Enter a meaningful name.
    * (Optional) **Description**: Add a description of the application.
    * (Optional) **Logo**: Add the Capella logo.
  7. Click **Save**.
3. Start the SAML configuration:

  1. Click **SAML Response**:
  2. Use the **Add** button to add the following attributes:  
  > [!TIP]  
  > After adding an attribute, you can show the **Add** button again by clearing the checkbox.

| Attributes Name | Attribute Value     |
| --------------- | ------------------- |
| email           | LoginUser.Email     |
| given\_name     | LoginUser.FirstName |
| family\_name    | LoginUser.LastName  |
| groups          | LoginUser.RoleNames |
  3. Click **Save**.
4. Assign your admin account with permissions to the app:

  1. Click **Permissions**.
  2. Click **Add**.
  3. Using the search field, find and add your admin account.
  4. Grant your admin account the following permissions:

    * Grant
    * View
    * Manage
    * Delete
    * Run
    * Automatically Deploy
  5. Click **Save**.  
  Your web app status shows as **Deployed**.
5. Click the **Trust** tab.  
You need information from this page to create a realm in Capella.

---

Create a Realm in Capella

With a CyberArk web application created, you need to create a realm in Capella using information from CyberArk.

1. In the Capella UI, click **Settings** **SSO**.
2. Click **Create Realm** **SAML**.
3. Complete the **Create Realm** page:

  1. Copy the following information from your CyberArk configuration to Capella:  
  > [!TIP]  
  > To find this information in the CyberArk Admin Portal, go to **Apps & Widgets** **Web Apps**. Find and open the web application that you want to view. Click **Trust**.

| CyberArk Field                                   |                          | Capella Field |
| ------------------------------------------------ | ------------------------ | ------------- |
| Contents of **Signing Certificate** **Download** | SAML Signing Certificate |               |
| Single Sign-On URL                               | Sign-in Endpoint URL     |               |
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

---

Complete the CyberArk Configuration

Now that you have created the realm, you must finish configuring the CyberArk web application.

1. In the CyberArk Portal, open the application you [created](#create-cyberark-app) for Capella.
2. Click **Trust**.
3. At the end of the page, edit the **Service Provider Configuration** settings:

  1. Select **Manual Configuration**.
  2. Copy the following fields from your Capella realm configuration to the CyberArk configuration:  
  > [!TIP]  
  > To find this information for your organization’s Capella realm, open the **Settings** **SSO** page. On this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page.

| Capella Field |                                      | CyberArk Field |
| ------------- | ------------------------------------ | -------------- |
| Callback URL  | Assertion Consumer Service (ACS) URL |                |
| Entity ID     | SP Entity ID / Issuer / Audience     |                |
4. Click **Save**.
5. Assign users to the application.

  1. Click **Permissions**.
  2. Add the groups whose members need access to Couchbase Capella. See the [Deploy applications](https://docs.cyberark.com/identity/Latest/en/Content/Applications/AppsOvw/AllowAppAccess.htm) page of the CyberArk documentation for more detail.

To configure federated and SSO authentication using CyberArk as your identity provider (IdP), you must complete three procedures in the following order:

1. [In CyberArk, create an Application](#create-cyberark-app-oidc)
2. [In Capella, create a realm](#create-cyberark-realm-oidc)
3. [In CyberArk, complete the configuration](#complete-cyberark-config-oidc)

---

Add a CyberArk Web App

Start by creating a CyberArk web application in the CyberArk Admin Portal. You need the information from this step to create a realm in Capella.

1. In the CyberArk Admin Portal, click **Apps & Widgets** **Web Apps**.
2. Click **Add Web Apps**.
3. Click the **Custom** tab.
4. In the list of templates, find and add **OpenID Connect**.
5. Configure the basic settings:

  * **Name**: Add a unique application name.
  * (Optional) **Description**: Add a description of the application.
  * (Optional) **Logo**: Add the Capella logo.
6. Click **Save**.
7. Assign your admin account with permissions to the app:

  1. Click **Permissions**.
  2. Click **Add**.
  3. Using the search field, find and add your admin account.
  4. Grant your admin account the following permissions:

    * Grant
    * View
    * Manage
    * Delete
    * Run
    * Automatically Deploy
  5. Click **Save**.  
  Your web app status shows as **Deployed**.
8. Click **Trust**.  
You need information from this page to create a realm in Capella.

---

Create a Realm in Capella

With the web application created in CyberArk, you need to create a realm in Capella using its information.

1. In Capella, click **Settings** **SSO**.
2. Click **Create Realm** **OpenID Connect**.
3. Copy the following information from your CyberArk web application configuration to Capella:  
> [!TIP]  
> To find this information in the CyberArk Admin Portal, go to **Apps & Widgets** **Web Apps**. Find and open the web application that you want to view. Click **Trust**.

| CyberArk Field               |                              | Capella Field |
| ---------------------------- | ---------------------------- | ------------- |
| OpenID Connect Metadata URL  | OpenID Connect Discovery URL |               |
| OpenID Connect Client ID     | Client ID                    |               |
| OpenID Connect Client Secret | Client Secret                |               |
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

---

Complete the CyberArk Configuration

Now that you have created the realm, you must finish configuring the CyberArk web application.

1. In the CyberArk Portal, open the application you [created](#create-cyberark-app-oidc) for Capella.
2. Click **Trust**.
3. Edit the following field with information from your Capella realm.  
> [!TIP]  
> To find this information for your organization’s Capella realm, open the **Settings** **SSO** page. On this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page.

| Capella Field |                          | CyberArk Field |
| ------------- | ------------------------ | -------------- |
| Callback URL  | Authorized Redirect URIs |                |
4. Click **Save**.

For more information about adding a custom OpenID Connect application, see the [CyberArk documentation](https://docs.cyberark.com/identity/latest/en/content/applications/appscustom/openidaddconfigapp.htm).

## [](#next-steps)Next Steps

* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Map User Roles](manage-role-mapping.md)
* [Manage Identity Providers](manage-identity-providers.md)