---
title: Set Up Capella SSO Using PingOne
description: Configure Single Sign-On (SSO) between PingOne and Couchbase
  Capella to allow your organization's users to authenticate securely without
  managing separate credentials. This integration enables streamlined access
  management while maintaining enterprise-grade security.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/organizations/pages/ui-auth/sso-ping.adoc
  xref: xref:cloud:organizations:ui-auth/sso-ping.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/organizations/ui-auth/sso-ping.html)

# Set Up Capella SSO Using PingOne

> Configure Single Sign-On (SSO) between PingOne and Couchbase Capella to allow your organization's users to authenticate securely without managing separate credentials. This integration enables streamlined access management while maintaining enterprise-grade security. 

## [](#prerequisites)Prerequisites

To configure Ping as an IdP, you need:

* To [enable SSO](add-sso-auth.md#access-and-enable-sso-settings) for your Capella organization.
* A [Ping](https://www.pingidentity.com) account.
* To be signed in to the Ping admin console as an admin.

## [](#procedure)Procedure

Choose the tab corresponding to your preferred authentication protocol.

* SAML
* OIDC

To configure federated and SSO authentication using SAML with Ping as your identity provider (IdP), you must complete three procedures in the following order:

1. [In Ping, create an Application](#create-ping-app)
2. [In Capella, create a realm](#create-ping-realm)
3. [In Ping, complete the configuration](#complete-ping-config)

---

Add a Ping Application

Start by creating a Ping Application in the Ping admin console. You need the information resulting from this step to create a realm in Capella.

1. Create a key pair:

  1. In the Ping admin console, click **Connections** **Certificates & Key Pairs**.
  2. Click **Add** **Create Key Pair**.
  3. In the **Create Key Pair** form, enter the following:

    * **Common Name**: Enter a name for the new key pair.
    * **Usage Type**: Choose **`Signing - Verification`**.
    * **Organization**: Enter an organization name.
    * **Country**: Enter your country.
  4. Click **Save & Finish**.
2. Click **Applications**.
3. Create the application:

  1. Click the plus sign  icon.
  2. Fill in the following fields:

    * **Application Name**: Enter a meaningful application name.
    * (Optional) **Description**: Add a description of the application.
    * (Optional) **Icon**: Add the Capella logo.
    * **Choose Application Type**: Select **`SAML Application`**.
  3. Click **Configure**.
4. Start the SAML configuration:

  1. Choose **Manually Enter**.
  2. Add the following placeholders:

| Field     | Value                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------ |
| ACS URLs  | Enter a placeholder, such as https://example.com. You'll provide the real value in a later step. |
| Entity ID | Enter a placeholder, such as placeholder. You'll provide the real value in a later step.         |
  3. Click **Save**.
5. Add attributes:

  1. Click the **Attributes** button containing the pencil  icon.
  2. In the **Attribute Mapping** section, add the following attributes using the **\+ Add** button:

| Attributes    | PingOne Mappings | Required |
| ------------- | ---------------- | -------- |
| saml\_subject | User ID          |          |
| email         | Email Address    |          |
| family\_name  | Family Name      |          |
| given\_name   | Given Name       |          |
| groups        | Group Name       |          |  
  {footnote-1}
  3. Click **Save**.
6. Click the **Overview** tab.
7. Update the SAML configuration with signing key information:

  1. Click the **Protocol** button containing the gear  icon.
  2. In the **Configuration** section, enter or edit the following fields:

| Field             | Value                                                   |
| ----------------- | ------------------------------------------------------- |
| Signing Key       | [The name of the signing key you created](#create-key). |
| Signing Algorithm | RSA\_SHA256                                             |
  3. Click **Save**.
8. Near the top right corner of the details panel, [enable the application](https://docs.pingidentity.com/bundle/pingone/page/isz1564020490044.html) by clicking the toggle switch.

---

Create a Realm in Capella

With a Ping application created, you need to create a realm in Capella using information from Ping.

1. In the Capella UI, click **Settings** **SSO**.
2. Click **Create Realm** **SAML**.
3. Complete the **Create Realm** page:

  1. Copy the following information from your Ping configuration to Capella:  
  > [!TIP]  
  > To find this information in the Ping admin console, go to **Connections** **Applications**. Find and click the application that you want to view. In the details panel, click the **Configuration** tab.

| Ping Field                                                       |                          | Capella Field |
| ---------------------------------------------------------------- | ------------------------ | ------------- |
| Contents of **Download Signing Certificate** **X509 PEM (.crt)** | SAML Signing Certificate |               |
| Single Sign On Service                                           | Sign-in Endpoint URL     |               |
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
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project's **Collaborators** tab.
4. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

---

Complete the Ping Configuration

Now that you have created the realm, you need to configure Ping to replace the placeholder values you used.

1. In the Ping admin console, open the application you [created](#create-ping-app) for Capella.
2. With the **Overview** tab open, click the **Protocol** button with the gear  icon.
3. Edit the configuration settings:

  1. Copy the following fields from your Capella realm configuration to the Ping configuration:  
  > [!TIP]  
  > To find this information for your organization's Capella realm, open the **Settings** **SSO** page. Listed on this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page.

| Capella Field |           | Ping Field |
| ------------- | --------- | ---------- |
| Callback URL  | ACS URLs  |            |
| Entity ID     | Entity ID |            |
4. Click **Save**.
5. Assign users to the application.

  1. With the application details open, click the **Access** tab.
  2. Add the groups whose members need access to Couchbase Capella. See the [Application access control](https://docs.pingidentity.com/bundle/pingone/page/xgv1612384834961.html) page of the Ping documentation for more detail.

To configure federated and SSO authentication using OIDC with Ping as your identity provider (IdP), you must complete three procedures in the following order:

1. [In Ping, create an Application](#create-ping-app-oidc)
2. [In Capella, create a realm](#create-ping-realm-oidc)
3. [In Ping, complete the configuration](#complete-ping-config-oidc)

---

Add a Ping Application

Start by creating a Ping Application in the Ping admin console. You need information from this step to create a realm in Capella.

1. Click **Applications** **Applications**.
2. Click the  icon.
3. Fill in the following fields:

  * **Application Name**: A unique name for the application.
  * (Optional) **Description**: Add a description of the application.
  * (Optional) **Icon**: Add the Capella logo.
  * **Application Type**: Select **OIDC Web App**.
4. Click **Save**.
5. On the Application screen, click the **Resources** tab.
6. Click **Save**.

---

Create a Realm in Capella

With the application created in Ping, you need to create a realm in Capella using its information.

1. In Capella, click **Settings** **SSO**.
2. Click **Create Realm** **OpenID Connect**.
3. Copy the following information from your Ping application to Capella:  
> [!TIP]  
> To find this information in the Ping admin console, go to **Applications** **Applications**. Find and click the application that you want to view. The **Overview** tab includes the OIDC Discovery URL, Client ID, and Client Secret information.

| Ping Field              |                              | Capella Field |
| ----------------------- | ---------------------------- | ------------- |
| OIDC Discovery Endpoint | OpenID Connect Discovery URL |               |
| Client ID               | Client ID                    |               |
| Client Secret           | Client Secret                |               |
4. Configure scopes:  
Scopes determine which user information Capella requests from your identity provider. The `openid`, `email`, and `profile` scopes are automatically included in the realm by default, so you do not need to add them.  
When adding additional scopes, separate each entry with a space.
5. Configure a default team and group mapping.

  1. Choose a default team.  
  Capella automatically assigns users to the chosen default team when they do not match any team based on their SSO groups. All users assigned to the default team have its chosen permission set.  
  For more information, see [Map User Roles](manage-role-mapping.md).
  2. Choose to turn on or off group mapping.  
  Group mapping allows you to assign roles to SSO users based on which teams map to their SSO group.  
  If you do not use group mapping, Capella uses the [default team](manage-role-mapping.md#default-teams) to give SSO users their roles when they first sign in. Without group mapping, you must manage your users' organization roles using the **People** tab and project roles using each project's **Collaborators** tab.
6. Click **Create Realm**.  
Capella creates the new realm with an auto-generated name.  
> [!IMPORTANT]  
> Users need to know the realm name to sign in with SSO. You can change the a realm name after you create the realm. For more information, see [Change the Realm Name](manage-identity-providers.md#change-realm-name).

---

Complete the Ping Configuration

Now that you have created the realm, you need to finishing configuring the Ping application.

1. In the Ping admin console, open the application you [created](#create-ping-app) for Capella.
2. Open the **Configuration** tab and click the Edit () icon
3. Change the **Token Endpoint Authentication Method** to **Client Secret Post**.
4. Copy the following fields from your Capella realm configuration to the Ping configuration:  
> [!TIP]  
> To find this information for your organization's Capella realm, open the **Settings** **SSO** page. Listed on this page is the realm you just created with an auto-generated name. Click its listing to open the realm information page.

| Capella Field |               | Ping Field |
| ------------- | ------------- | ---------- |
| Callback URL  | Redirect URIs |            |
5. Click **Save**.
6. Assign users to the application.

  1. With the application details open, click the **Access** tab.
  2. Add the groups whose members need access to Couchbase Capella. See the [Application access control](https://docs.pingidentity.com/bundle/pingone/page/xgv1612384834961.html) page of the Ping documentation for more detail.
7. When viewing your applications in **Applications** **Applications**, enable the application by clicking the toggle switch.

## [](#next-steps)Next Steps

* [Sign in to Capella with SSO](sign-in-with-sso.md)
* [Map User Roles](manage-role-mapping.md)
* [Manage Identity Providers](manage-identity-providers.md)