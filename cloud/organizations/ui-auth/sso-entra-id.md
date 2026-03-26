---
title: Set Up Capella SSO Using Microsoft Entra ID
description: Configure Single Sign-On (SSO) between Microsoft Entra ID and
  Couchbase Capella to allow your organization's users to authenticate securely
  without managing separate credentials. This integration enables streamlined
  access management while maintaining enterprise-grade security.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/sso-entra-id.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:organizations:ui-auth/sso-entra-id.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/ui-auth/sso-entra-id.html)

# Set Up Capella SSO Using Microsoft Entra ID

> Configure Single Sign-On (SSO) between Microsoft Entra ID and Couchbase Capella to allow your organization's users to authenticate securely without managing separate credentials. This integration enables streamlined access management while maintaining enterprise-grade security. 

## [](#prerequisites)Prerequisites

To configure Microsoft Entra ID as an IdP, you need:

* To [enable SSO](add-sso-auth.md#access-and-enable-sso-settings) for your Capella organization.
* An Azure subscription with Microsoft Entra ID. For more information, see [Microsoft](https://learn.microsoft.com/en-us/entra/fundamentals/get-started-premium).
* An Entra ID tenant associated with your Azure subscription. For more information, see the [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/).
* [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) privileges for your Entra ID tenant.
* The `family_name` or `given_name` fields populated for your users in Entra ID.

## [](#procedures)Procedures

Choose the tab for your preferred authentication protocol.

* SAML
* OIDC

To configure federated and SSO authentication using SAML with Entra ID as your identity provider (IdP), you must complete 3 procedures in the following order:

1. [In Entra ID, create an application](#create-azuread-app)
2. [In Capella, create a realm](#create-azuread-realm)
3. [In Entra ID, complete the configuration](#complete-azuread-config)

---

Create an Application

Start by creating a new application with Entra ID. Use the information from your enterprise application in Entra to create a realm in Capella.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/) or the [Microsoft Azure Portal](https://portal.azure.com).
2. Do 1 of the following to go to your Enterprise Apps page:

  1. In the Entra admin center, go to **Entra ID** **Enterprise Apps**.
  2. In the Azure Portal, open **Microsoft Entra ID**, then go to **Manage** **Enterprise Applications**.
3. Click **New application**.
4. In the search bar, search for the **Couchbase Capella - SSO** application.
5. Enter a meaningful display name for the new application.
6. Click **Create**.  
The **Overview** page of the app appears once it's created.
7. Go to **Manage** **Single sign-on**.
8. Choose **SAML**.
9. Under **SAML Signing Certificates**, next to the **Token Signing Certificate**, click **Edit**.
10. Click **New Certificate**.
11. Click **Save**.
12. Next to the new certificate, go to **…​** **Make Certificate Active**.
13. Confirm that you want to make the certificate active.
14. Next to the new certificate, go to **…​** **PEM Certificate Download**.  
Keep the certificate file open in a text editor for creating your Capella realm.
15. Keep the SAML configuration page for your Capella application in Entra ID open while creating your Capella realm.

---

Create a Realm in Capella

After you have created an application with Entra ID, you need to create a realm in Capella. To create a realm, you need some information from Entra ID.

1. In Capella, click **Settings** **SSO**.
2. Click **Create Realm** **SAML**.
3. In the **SAML Signing Certificate** field, paste the contents of the downloaded PEM certificate from Entra ID, removing the first and last lines (`-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`)  
> [!TIP]  
> If you need to update your signing certificate later, see [Change Signing Endpoint URL and Certificate](manage-identity-providers.md#change-cert).
4. Copy the Login URL from Entra ID to Capella.

  1. In Entra ID, under your Capella application name, copy the **Login URL**.
  2. In Capella, paste the copied URL into the **Sign-in Endpoint URL** field.
  3. Verify that the remaining SAML protocol settings are as follows:

| Field                 | Value      |
| --------------------- | ---------- |
| Signature Algorithm   | RSA-SHA256 |
| Digest Algorithm      | SHA256     |
| SAML Protocol Binding | HTTP-POST  |
  4. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  5. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project's **Collaborators** tab.
5. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

---

Complete the Entra ID Configuration

Add the Entity ID, Callback URL, and Sign on URL from your Capella realm to your Entra ID configuration. You need to have both Capella and Entra ID open in your browser.

1. In Capella, show the **Realm Summary** for the realm you created for this configuration.

  1. Click **Settings** **SSO**.
  2. In the realm listing, click the arrow to show the **Realm Summary**.
2. In Entra ID, next to **Basic SAML configuration**, click **Edit**.
3. Add the Entity ID to Entra ID:

  1. In Capella, copy the **Entity ID** field.
  2. In Entra ID, in the **Identifier** field, paste the **Entity ID**.
4. Add the Callback URL to Entra ID:

  1. In Capella, copy the **Callback URL** field.
  2. In Entra ID, in the **Reply URL** field, paste the **Callback URL**.
5. Add the Sign on URL to Entra ID:

  1. In Entra ID, in the **Sign on URL** field, paste `https://cloud.couchbase.com/enterprise-sso`.
6. In Entra ID, click **Save**.
7. Add optional claims to Entra ID:

  1. In Entra ID, click **Token configuration**.
  2. Click **Add groups claim**.
  3. In the **Edit groups claim** flyout, select all the group types.
  4. Click **Add**.  
  > [!NOTE]  
  > Microsoft Entra limits the total number of groups emitted in a token for SAML assertions to 150\. If you have a user that's in more than 150 groups on Entra ID, their group claims do not emit properly to Capella. To avoid group claims limits, make sure to [filter your groups](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-group-claims#group-filtering) to only the groups you need for Capella.
  5. On the **Optional claims** page, click **Add optional claim**.
  6. In the **Add optional claim** flyout, choose the **SAML** option.
  7. Select the **email** claim.
  8. Click **Add**.
  9. In the dialog box, select **Turn on the Microsoft Graph email permission**.
  10. Click **Add**.
8. Assign users to the application.

  1. Add the users and groups whose members need access to Couchbase Capella.  
  For more information, see [Quickstart: Create and assign a user account](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-assign-users) in the Azure documentation.

To configure federated and SSO authentication using OIDC with Entra ID as your identity provider (IdP), you must complete 3 procedures in the following order:

1. [In Entra ID, register an application](#create-azuread-app-oidc)
2. [In Capella, create a realm](#create-azuread-realm-oidc)
3. [In Entra ID, complete the configuration](#complete-azuread-config-oidc)

---

Register an Application

Start by registering an application with Entra ID. You need information from your registered application to create a realm in Capella.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
2. Click **Identity** **Applications** **App registrations**.
3. Click **New registration**.
4. Configure the basic settings:

  * **Name**: Enter a meaningful display name for this application.
  * **Supported account types**: Choose who can use this application. Typically, this is the default option—​Accounts in this organizational directory only.
  * **Redirect URI**: Leave empty for now—​you'll add this later.
5. Click **Register**.

---

Create a Realm in Capella

With an application registered with Entra ID, you need to create a realm in Capella. To create a realm, you need some information from Entra ID.

1. In Capella, click **Settings** **SSO**.
2. Click **Create Realm** **OpenID Connect**.
3. Add the OpenID Connect Discovery URL to your realm configuration.

  1. In Entra ID, on your new app's **Overview** page, click **Endpoints**
  2. On the **Endpoints** flyout, copy the **OpenID Connect metadata document** field.
  3. In Capella, paste the URL into the **OpenID Connect Discovery URL** field.
4. Add the Client ID to your realm configuration.

  1. In Entra ID, on your new app's **Overview** page, copy the **Application (client) ID**.
  2. In Capella, paste the Client ID into the **Client ID** field.
5. Create and add the Client Secret to your realm configuration.  
> [!TIP]  
> The secret is only shown once. You must copy it at the time of creation. If you forget to copy the secret value, you must create a new one.

  1. In Entra ID, on your new app's **Overview** page, click **Add a certificate or secret**.
  2. Click **New client secret**.
  3. Enter an optional description and choose the expiration time frame.
  4. Click **Add**.
  5. Copy the secret **Value**.
  6. In Capella, paste the Value into the **Client Secret** field.
6. Configure scopes:  
Scopes determine which user information Capella requests from your identity provider. The `openid`, `email`, and `profile` scopes are automatically included in the realm by default, so you do not need to add them.  
When adding additional scopes, separate each entry with a space.
7. Configure a default team and group mapping.

  1. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  2. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project's **Collaborators** tab.
8. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

---

Complete the Entra ID Configuration

Copy the Application ID, Redirect URI, and optional claim information from your Capella realm to your Entra ID configuration. You need to have both Capella and Entra ID open in your browser.

1. In Capella, show the **Realm Summary** for the realm you created for this configuration.

  1. Click **Settings** **SSO**.
  2. In the realm listing, click the down arrow to show the **Realm Summary**.
2. Add the Redirect URI to Entra ID:

  1. In Capella, copy the **Callback URL** field.
  2. In Entra ID, on the **Overview** page of the [registered application](#create-azuread-app-oidc), click **Add a Redirect URI**.
  3. Click **Add a platform**.
  4. In the **Configure platforms** flyout, click **Web**.
  5. Paste the Callback URL into the **Redirect URIs** field.
  6. Select **ID tokens (used for implicit and hybrid flows)**.
  7. Click **Configure**.
3. Add optional claims to Entra ID:

  1. In Entra ID, click **Token configuration**.
  2. Click **Add groups claim**.
  3. In the **Edit groups claim** flyout, select all of the group types:

    * Security groups
    * Directory roles
    * All groups
    * Groups assigned to the application
  4. Click **Add**.
  5. On the **Optional claims** page, click **Add optional claim**.
  6. In the **Add optional claim** flyout, choose the **ID** token type and select the following claims:

    * `email`
    * `family_name`
    * `given_name`
  7. Click **Add**.
  8. In the dialog box, select **Turn on the Microsoft Graph email permission** and click **Add**.
4. Assign users to the application.

  1. Add the users and groups whose members need access to Couchbase Capella.  
  See [Quickstart: Create and assign a user account](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-assign-users) in the Azure documentation for more detail.

## [](#next-steps)Next Steps

* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Map User Roles](manage-role-mapping.md)
* [Manage Identity Providers](manage-identity-providers.md)